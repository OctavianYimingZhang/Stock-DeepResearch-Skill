#!/usr/bin/env python3
"""Read-only health checks and explicit update controls for the Skill repo."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "skill_manifest.json"
BACKUP_DIR = ROOT / ".skill_backups"


@dataclass
class CommandResult:
    command: str
    returncode: int
    stdout: str
    stderr: str

    @property
    def ok(self) -> bool:
        return self.returncode == 0

    def as_dict(self) -> dict[str, Any]:
        return {
            "command": self.command,
            "returncode": self.returncode,
            "ok": self.ok,
            "stdout": self.stdout.strip(),
            "stderr": self.stderr.strip(),
        }


def run_command(command: str, check: bool = False) -> CommandResult:
    env = os.environ.copy()
    env.setdefault("PYTHONDONTWRITEBYTECODE", "1")
    completed = subprocess.run(
        command,
        cwd=ROOT,
        env=env,
        shell=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    result = CommandResult(command, completed.returncode, completed.stdout, completed.stderr)
    if check and not result.ok:
        raise RuntimeError(f"Command failed: {command}\n{result.stderr.strip()}")
    return result


def git_output(*args: str, check: bool = True) -> str:
    completed = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if check and completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or f"git {' '.join(args)} failed")
    return completed.stdout.strip()


def load_manifest() -> tuple[dict[str, Any], list[str]]:
    issues: list[str] = []
    if not MANIFEST_PATH.exists():
        return {}, ["skill_manifest.json is missing"]
    try:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return {}, [f"skill_manifest.json is invalid JSON: {exc}"]

    required = {
        "schema_version": int,
        "skill_id": str,
        "repo": str,
        "branch": str,
        "entrypoint": str,
        "health_commands": list,
        "post_update_commands": list,
    }
    for key, expected_type in required.items():
        if key not in manifest:
            issues.append(f"skill_manifest.json is missing {key}")
        elif not isinstance(manifest[key], expected_type):
            issues.append(f"skill_manifest.json field {key} has the wrong type")

    if manifest.get("schema_version") != 1:
        issues.append("skill_manifest.json schema_version must be 1")
    if manifest.get("skill_id") != "stock-research-report":
        issues.append("skill_manifest.json skill_id must be stock-research-report")
    if manifest.get("entrypoint") and not (ROOT / manifest["entrypoint"]).exists():
        issues.append("manifest entrypoint does not exist")

    return manifest, issues


def git_state(manifest: dict[str, Any]) -> dict[str, Any]:
    state: dict[str, Any] = {
        "is_git_repo": False,
        "branch": None,
        "head": None,
        "remote_url": None,
        "remote_head": None,
        "dirty": None,
        "up_to_date": None,
        "issues": [],
    }
    try:
        git_output("rev-parse", "--is-inside-work-tree")
        state["is_git_repo"] = True
        state["branch"] = git_output("rev-parse", "--abbrev-ref", "HEAD")
        state["head"] = git_output("rev-parse", "HEAD")
        state["remote_url"] = git_output("remote", "get-url", "origin", check=False) or None
        status = git_output("status", "--porcelain")
        state["dirty"] = bool(status)
        branch = manifest.get("branch", "main")
        remote = git_output("ls-remote", "origin", f"refs/heads/{branch}", check=False)
        if remote:
            state["remote_head"] = remote.split()[0]
            state["up_to_date"] = state["remote_head"] == state["head"]
        else:
            state["issues"].append(f"remote branch not found: {branch}")
    except Exception as exc:
        state["issues"].append(str(exc))
    return state


def run_health(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for command in manifest.get("health_commands", []):
        results.append(run_command(command).as_dict())
    return results


def build_doctor_report(run_health_commands: bool = True) -> dict[str, Any]:
    manifest, manifest_issues = load_manifest()
    health = run_health(manifest) if run_health_commands and not manifest_issues else []
    health_failed = [item for item in health if not item["ok"]]
    report = {
        "tool": "stock-research-report skill doctor",
        "mode": "read-only",
        "manifest": manifest,
        "manifest_issues": manifest_issues,
        "git": git_state(manifest) if manifest else {},
        "health": health,
        "ok": not manifest_issues and not health_failed,
    }
    return report


def print_report(report: dict[str, Any], as_json: bool) -> None:
    if as_json:
        print(json.dumps(report, indent=2, sort_keys=True))
        return
    print(f"{report.get('tool', 'skill maintenance')}: {'OK' if report.get('ok') else 'FAILED'}")
    for issue in report.get("manifest_issues", []):
        print(f"- manifest: {issue}")
    for issue in report.get("git", {}).get("issues", []):
        print(f"- git: {issue}")
    for action in report.get("actions", []):
        print(f"- action: {action}")
    for action in report.get("recommended_actions", []):
        print(f"- recommendation: {action}")
    for item in report.get("health", []):
        status = "OK" if item["ok"] else "FAILED"
        print(f"- {status}: {item['command']}")
        if not item["ok"] and item.get("stderr"):
            print(item["stderr"])


def make_backup(manifest: dict[str, Any]) -> Path:
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = time.strftime("%Y%m%d%H%M%S")
    backup_path = BACKUP_DIR / f"{manifest['skill_id']}.{timestamp}.zip"
    with zipfile.ZipFile(backup_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in ROOT.rglob("*"):
            relative = path.relative_to(ROOT)
            parts = set(relative.parts)
            if ".git" in parts or ".skill_backups" in parts or "__pycache__" in parts:
                continue
            if path.suffix == ".pyc" or path.is_dir():
                continue
            archive.write(path, relative.as_posix())
    return backup_path


def restore_backup(backup_path: Path) -> None:
    for path in ROOT.iterdir():
        if path.name in {".git", ".skill_backups"}:
            continue
        if path.is_dir():
            shutil.rmtree(path)
        else:
            path.unlink()
    with zipfile.ZipFile(backup_path) as archive:
        archive.extractall(ROOT)


def update_preview(manifest: dict[str, Any]) -> dict[str, Any]:
    branch = manifest.get("branch", "main")
    state = git_state(manifest)
    report: dict[str, Any] = {
        "tool": "stock-research-report skill update",
        "mode": "dry-run",
        "git": state,
        "safe_to_update": False,
        "actions": [],
        "ok": False,
    }
    if not state.get("is_git_repo"):
        report["actions"].append("No git repository was detected.")
        return report
    if state.get("dirty"):
        report["actions"].append("Tracked or untracked local changes must be resolved before update.")
        report["ok"] = True
        return report
    if not state.get("remote_head"):
        report["actions"].append("Remote branch state is unavailable.")
        return report
    if state.get("up_to_date"):
        report["safe_to_update"] = True
        report["ok"] = True
        report["actions"].append("Local checkout already matches the configured remote branch.")
        return report

    ancestor = subprocess.run(
        ["git", "merge-base", "--is-ancestor", "HEAD", f"origin/{branch}"],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if ancestor.returncode == 0:
        report["safe_to_update"] = True
        report["ok"] = True
        report["actions"].append("A fast-forward update can be attempted with --yes.")
    else:
        report["ok"] = True
        report["actions"].append("The configured remote cannot be fast-forwarded from this checkout.")
    return report


def explicit_update(manifest: dict[str, Any], as_json: bool) -> int:
    preview = update_preview(manifest)
    if not preview["safe_to_update"]:
        print_report(preview, as_json)
        return 1

    previous_head = git_output("rev-parse", "HEAD")
    backup_path = make_backup(manifest)
    branch = manifest.get("branch", "main")
    report: dict[str, Any] = {
        "tool": "stock-research-report skill update",
        "mode": "explicit",
        "backup": str(backup_path),
        "previous_head": previous_head,
        "steps": [],
        "ok": False,
    }
    try:
        report["steps"].append(run_command(f"git fetch origin {branch}", check=True).as_dict())
        report["steps"].append(run_command(f"git merge --ff-only origin/{branch}", check=True).as_dict())
        for command in manifest.get("post_update_commands", []):
            report["steps"].append(run_command(command, check=True).as_dict())
        health = run_health(manifest)
        report["health"] = health
        failed = [item for item in health if not item["ok"]]
        if failed:
            raise RuntimeError("post-update health commands failed")
        report["new_head"] = git_output("rev-parse", "HEAD")
        report["ok"] = True
    except Exception as exc:
        report["error"] = str(exc)
        run_command(f"git reset --hard {previous_head}")
        restore_backup(backup_path)
        report["rolled_back_to"] = previous_head
    print_report(report, as_json)
    return 0 if report["ok"] else 1


def proposal_report(as_json: bool) -> int:
    doctor = build_doctor_report(run_health_commands=True)
    failed = [item for item in doctor.get("health", []) if not item["ok"]]
    proposal = {
        "tool": "stock-research-report skill proposal",
        "mode": "proposal-only",
        "ok": doctor["ok"],
        "recommended_actions": [],
    }
    if doctor.get("manifest_issues"):
        proposal["recommended_actions"].append("Fix manifest structure before changing analytical content.")
    if failed:
        proposal["recommended_actions"].append("Open a branch and fix failing health commands before release.")
    if doctor.get("git", {}).get("dirty"):
        proposal["recommended_actions"].append("Review local changes before update or release.")
    if not proposal["recommended_actions"]:
        proposal["recommended_actions"].append("No maintenance change is required by current checks.")
    print_report(proposal, as_json)
    return 0 if proposal["ok"] else 1


def main() -> int:
    parser = argparse.ArgumentParser(description="Maintain the stock-research-report Skill safely.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    doctor_parser = subparsers.add_parser("doctor", help="Run read-only Skill health checks.")
    doctor_parser.add_argument("--json", action="store_true", help="Emit machine-readable output.")

    update_parser = subparsers.add_parser("update", help="Preview or perform an explicit Skill update.")
    update_parser.add_argument("--dry-run", action="store_true", help="Preview update state without changing tracked files.")
    update_parser.add_argument("--yes", action="store_true", help="Perform backup, fast-forward update, and validation.")
    update_parser.add_argument("--json", action="store_true", help="Emit machine-readable output.")

    proposal_parser = subparsers.add_parser("proposal", help="Generate a maintenance proposal without changing files.")
    proposal_parser.add_argument("--json", action="store_true", help="Emit machine-readable output.")

    args = parser.parse_args()
    manifest, issues = load_manifest()
    if args.command == "doctor":
        report = build_doctor_report(run_health_commands=True)
        print_report(report, args.json)
        return 0 if report["ok"] else 1
    if issues:
        report = {"tool": "stock-research-report skill maintenance", "ok": False, "manifest_issues": issues}
        print_report(report, getattr(args, "json", False))
        return 1
    if args.command == "update":
        if args.yes:
            return explicit_update(manifest, args.json)
        preview = update_preview(manifest)
        print_report(preview, args.json)
        return 0 if preview["ok"] else 1
    if args.command == "proposal":
        return proposal_report(args.json)
    return 1


if __name__ == "__main__":
    sys.exit(main())
