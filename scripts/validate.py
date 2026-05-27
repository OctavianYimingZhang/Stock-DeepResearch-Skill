#!/usr/bin/env python3
from __future__ import annotations

import re
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".py", ".json"}


REQUIRED_REFERENCES = [
    "references/business-model-framework.md",
    "references/valuation-framework.md",
    "references/profit-cash-flow-quality-framework.md",
    "references/short-seller-risk-framework.md",
    "references/technical-analysis-framework.md",
    "references/scorecard-decision-framework.md",
    "references/report-style-patterns.md",
    "references/research-lakehouse-framework.md",
    "references/evidence-indexing-framework.md",
    "references/incremental-refresh-framework.md",
    "references/user-intake-settings-framework.md",
    "references/ontology-framework.md",
    "references/quality-calibration-loop.md",
    "references/external-inspirations-and-license-notes.md",
]

REQUIRED_CONFIG_FILES = [
    "config/settings.schema.json",
    "config/profiles/default.json",
    "config/onboarding.flow.yaml",
]

REQUIRED_ONTOLOGY_FILES = [
    "ontology/object_types.yaml",
    "ontology/link_types.yaml",
    "ontology/action_types.yaml",
    "ontology/functions.yaml",
    "ontology/workflow_gates.yaml",
]

REQUIRED_MAINTENANCE_FILES = [
    "skill_manifest.json",
    "requirements.txt",
    "scripts/skill_maintenance.py",
    ".github/workflows/skill-health.yml",
]

REQUIRED_SECTIONS = [
    "Company Overview",
    "Business Model Logic",
    "Operations, Customers, And Orders",
    "Financials, Assets, And Debt",
    "Valuation",
    "Short-Seller Risk",
    "Technical Analysis",
    "Risk Factors",
    "Trade Plan",
]

FORBIDDEN_SKILL_PATTERNS = [
    r"Launch ALL FOUR",
    r"Agent 1",
    r"Agent 2",
    r"Agent 3",
    r"Agent 4",
    r"sub-skills required",
    r"Skill tool with skill",
    r"four specialized analysis skills in parallel",
    r"must be installed",
]

FORBIDDEN_CASE_WORDS = [
    "ex" + "ample",
    "Ex" + "ample",
    "EX" + "AMPLE",
]

FORBIDDEN_REFERENCE_CASES = [
    "T" + "E",
    "T" + "ER",
    "U" + "MAC",
    "U" + "AMY",
    "T" + "SEM",
    "A" + "EHR",
    "A" + "MKR",
    "Tera" + "dyne",
    "Unusual " + "Machines",
    "Ae" + "hr",
    "Am" + "kor",
    "Tower " + "Semiconductor",
    "T1 " + "Energy",
]

FORBIDDEN_LANGUAGE_CONFLICTS = [
    "Ch" + "inese",
    "Ch" + "inese " + "prose",
    "plain " + "Ch" + "inese",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def read(path: str) -> str:
    target = ROOT / path
    if not target.exists():
        fail(f"missing file: {path}")
    return target.read_text(encoding="utf-8")


def repo_text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ".git" in path.parts:
            continue
        if path.name == "LICENSE":
            continue
        if path.suffix in TEXT_SUFFIXES:
            files.append(path)
    return sorted(files)


def parse_frontmatter(text: str) -> dict[str, object]:
    if not text.startswith("---\n"):
        fail("SKILL.md missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail("SKILL.md frontmatter is not closed")
    raw = text[4:end]
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(raw)
    except Exception:
        data = {}
        current_key = None
        for line in raw.splitlines():
            if not line.strip():
                continue
            if re.match(r"^[A-Za-z_-]+:", line):
                key, value = line.split(":", 1)
                data[key.strip()] = value.strip()
                current_key = key.strip()
            elif current_key and line.startswith("  "):
                data[current_key] = str(data.get(current_key, "")) + "\n" + line.strip()
    if not isinstance(data, dict):
        fail("SKILL.md frontmatter did not parse to a mapping")
    return data


def validate_skill() -> None:
    skill = read("SKILL.md")
    meta = parse_frontmatter(skill)
    if meta.get("name") != "stock-research-report":
        fail("SKILL.md frontmatter name must be stock-research-report")
    if "Self-contained" not in str(meta.get("description", "")):
        fail("SKILL.md description must identify the self-contained architecture")

    for ref in REQUIRED_REFERENCES:
        if ref not in skill:
            fail(f"SKILL.md does not reference {ref}")
        if not (ROOT / ref).exists():
            fail(f"referenced file does not exist: {ref}")

    for section in REQUIRED_SECTIONS:
        if section not in skill:
            fail(f"SKILL.md missing required report section: {section}")

    for pattern in FORBIDDEN_SKILL_PATTERNS:
        if re.search(pattern, skill, re.IGNORECASE):
            fail(f"SKILL.md still contains old orchestration pattern: {pattern}")

    permissive_average_patterns = [
        r"use\s+(a\s+)?probability-weighted",
        r"allow probability-weighting",
        r"use method averaging",
    ]
    for pattern in permissive_average_patterns:
        if re.search(pattern, skill, re.IGNORECASE):
            fail("SKILL.md appears to allow probability-weighted or averaged valuation targets")

    for phrase in [
        "Quality Calibration Loop",
        "Ontology Object Graph",
        "Research Lakehouse And Evidence Index",
        "Runtime Settings And Source Map",
        "current-market-implied",
        "source markers",
        "EV-to-equity-to-diluted-share",
        "Profit Cash Flow Quality Analysis",
        "Decision Scorecard",
        "No baked-in company triggers",
    ]:
        if phrase not in skill:
            fail(f"SKILL.md missing quality-loop requirement: {phrase}")


def validate_readme() -> None:
    readme = read("README.md")
    for ref in REQUIRED_REFERENCES:
        if ref not in readme:
            fail(f"README.md does not reference {ref}")
    for path in REQUIRED_CONFIG_FILES:
        if path not in readme:
            fail(f"README.md does not reference {path}")
    for path in REQUIRED_MAINTENANCE_FILES:
        if path not in readme:
            fail(f"README.md does not reference {path}")
    if "no longer depends at runtime" not in readme:
        fail("README.md must state that old standalone Skill dependencies were removed")


def load_yaml(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(text)
        if not isinstance(data, dict):
            fail(f"{path} did not parse to a mapping")
        return data
    except ImportError:
        data: dict[str, object] = {}
        for line in text.splitlines():
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            if re.match(r"^[A-Za-z0-9_-]+:", line):
                key, value = line.split(":", 1)
                data[key.strip()] = value.strip()
        return data


def validate_evals() -> None:
    case_dir = ROOT / "evals" / "cases"
    if not case_dir.exists():
        fail("missing evals/cases")
    cases = sorted(case_dir.glob("*.yaml"))
    if len(cases) < 15:
        fail("expected at least 15 eval case YAML files")
    seen_archetypes = set()
    for case in cases:
        data = load_yaml(case)
        for key in ["id", "archetype", "expected_primary_valuation"]:
            if key not in data:
                fail(f"{case} missing required key: {key}")
        seen_archetypes.add(str(data["archetype"]))
        text = case.read_text(encoding="utf-8")
        for section in REQUIRED_SECTIONS:
            if section not in text:
                fail(f"{case} missing required section assertion: {section}")
        for check in [
            "one_primary_valuation_method",
            "short_seller_grade",
        ]:
            if check not in text:
                fail(f"{case} missing required check: {check}")
    expected = {
        "semiconductor_cyclical",
        "early_commercialization_frontier",
        "resource_policy",
        "specialty_semiconductor_growth",
        "semiconductor_equipment_growth",
        "advanced_packaging_asset_intensive",
        "policy_linked_manufacturing",
        "fresh_outside_reference",
        "lineage_incremental_refresh",
        "unreconciled_share_count_blocks_target",
        "weak_order_signal_blocks_valuation",
        "stale_chart_blocks_trade_plan",
        "short_risk_c_grade_reduces_position_size",
        "conflicting_source_priority_resolution",
        "missing_debt_maturity_blocks_equity_bridge",
        "cash_conversion_quality",
        "sbc_dilution_owner_fcf_cap",
        "working_capital_deterioration_caps_valuation",
        "rule_of_40_not_applicable",
        "valuation_stretch_scorecard_cap",
        "momentum_overextension_scorecard_cap",
        "unresolved_evidence_blocks_scorecard",
        "business_transition_layer_depth",
        "order_to_revenue_ramp_bridge",
        "re_rating_and_funding_bridge",
        "falsification_lens_trim_plan",
    }
    missing = expected - seen_archetypes
    if missing:
        fail(f"eval coverage missing archetypes: {sorted(missing)}")


def validate_references() -> None:
    if (ROOT / "DEPRECATION.md").exists():
        fail("DEPRECATION.md conflicts with the active standalone Skill repository")

    for ref in REQUIRED_REFERENCES:
        text = read(ref)
        if len(text.strip()) < 500:
            fail(f"{ref} is unexpectedly short")
    refs = {p.name for p in (ROOT / "references").glob("*")}
    expected = {Path(p).name for p in REQUIRED_REFERENCES}
    stale = refs - expected
    if stale:
        fail(f"unexpected stale reference files: {sorted(stale)}")


def validate_english_only_repo_text() -> None:
    for path in repo_text_files():
        text = path.read_text(encoding="utf-8")
        if re.search(r"[\u4e00-\u9fff]", text):
            rel = path.relative_to(ROOT)
            fail(f"{rel} contains non-English CJK text")


def validate_no_baked_case_language() -> None:
    for path in repo_text_files():
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT)
        for word in FORBIDDEN_CASE_WORDS:
            if word.lower() in text.lower():
                fail(f"{rel} contains banned case-word language")
        for term in FORBIDDEN_REFERENCE_CASES:
            if re.search(rf"(?<![A-Za-z0-9]){re.escape(term)}(?![A-Za-z0-9])", text, re.IGNORECASE):
                fail(f"{rel} contains a baked-in reference-company term")
        for phrase in FORBIDDEN_LANGUAGE_CONFLICTS:
            if phrase.lower() in text.lower():
                fail(f"{rel} contains conflicting language-output instruction")


def validate_quality_contracts() -> None:
    if not (ROOT / "scripts" / "validate_report_output.py").exists():
        fail("missing generated-report output validator")
    if not (ROOT / "scripts" / "validate_ontology.py").exists():
        fail("missing ontology validator")
    if not (ROOT / "evals" / "fixtures" / "report-contract-fixture.md").exists():
        fail("missing report output contract fixture")
    for path in REQUIRED_ONTOLOGY_FILES:
        if not (ROOT / path).exists():
            fail(f"missing ontology contract file: {path}")
    for path in REQUIRED_CONFIG_FILES:
        if not (ROOT / path).exists():
            fail(f"missing config contract file: {path}")
    for path in [
        "scripts/validate_settings.py",
        "scripts/validate_research_manifest.py",
        "scripts/validate_report_against_manifest.py",
        "scripts/build_prompt_from_settings.py",
        "evals/fixtures/report-contract-fixture.manifest.json",
    ]:
        if not (ROOT / path).exists():
            fail(f"missing productization contract file: {path}")
    for path in REQUIRED_MAINTENANCE_FILES:
        if not (ROOT / path).exists():
            fail(f"missing maintenance contract file: {path}")

    valuation = read("references/valuation-framework.md")
    for phrase in [
        "Current-Price-Implied Bridge",
        "current price already implies",
        "target equity value = target EV - net debt + non-operating assets",
        "target price = target equity value / diluted shares",
        "order-proxy ladder",
        "ProfitCashFlowQualityAnalysis",
        "owner FCF per share",
        "Re-Rating Bridge",
        "Forward Ramp Math",
        "funding bridge",
    ]:
        if phrase not in valuation:
            fail(f"valuation framework missing quality contract: {phrase}")

    business = read("references/business-model-framework.md")
    for phrase in [
        "industry-to-company bridge",
        "Strategic Transition Tests",
        "operating ramp bridge",
        "order-to-revenue path",
    ]:
        if phrase not in business:
            fail(f"business-model framework missing quality contract: {phrase}")

    profit_cash = read("references/profit-cash-flow-quality-framework.md")
    for phrase in [
        "ProfitCashFlowQualityAnalysis",
        "OCF / net income",
        "EBITDA -> OCF -> FCF",
        "FCF per share",
        "Rule of 40 applicability",
        "not_applicable",
        "SBC-adjusted FCF",
    ]:
        if phrase not in profit_cash:
            fail(f"profit cash-flow framework missing quality contract: {phrase}")

    short = read("references/short-seller-risk-framework.md")
    for phrase in [
        "verified fact",
        "allegation",
        "inference",
        "unanswered question",
        "short interest",
        "activist-short attack narrative",
        "Falsification Lens",
    ]:
        if phrase not in short:
            fail(f"short-seller framework missing quality contract: {phrase}")

    technical = read("references/technical-analysis-framework.md")
    for phrase in [
        "chart date",
        "split-adjusted",
        "dividend-adjusted",
        "stale",
        "adjusted/unadjusted status",
        "Trade-Execution Calibration",
    ]:
        if phrase not in technical:
            fail(f"technical framework missing quality contract: {phrase}")

    style = read("references/report-style-patterns.md")
    for phrase in [
        "Layer Depth Standard",
        "separate business thesis strength from trade action grade",
    ]:
        if phrase not in style:
            fail(f"report style framework missing quality contract: {phrase}")

    scorecard = read("references/scorecard-decision-framework.md")
    for phrase in [
        "DecisionScorecard",
        "action grade",
        "binding cap reason",
        "Do not average numeric scores",
        "report projection",
    ]:
        if phrase not in scorecard:
            fail(f"scorecard framework missing quality contract: {phrase}")

    ontology = read("references/ontology-framework.md")
    for phrase in [
        "evidence-backed `Claim`",
        "object graph",
        "Lakehouse Layer Gate",
        "Settings Gate",
        "Equity Bridge Gate",
        "Incremental Refresh Gate",
        "Output View Gate",
        "Gate results use",
        "Workflow Gates",
        "Report Projection",
        "ProfitCashFlowQualityAnalysis",
        "DecisionScorecard",
    ]:
        if phrase not in ontology:
            fail(f"ontology framework missing quality contract: {phrase}")

    lakehouse = read("references/research-lakehouse-framework.md")
    for phrase in [
        "Bronze",
        "Source Index",
        "Silver",
        "Gold",
        "Report View",
        "SourceSnapshot",
        "ResearchRun",
    ]:
        if phrase not in lakehouse:
            fail(f"research lakehouse framework missing quality contract: {phrase}")

    indexing = read("references/evidence-indexing-framework.md")
    for phrase in [
        "SourcePartition",
        "EvidencePartition",
        "Pruning Rules",
        "source strength",
        "conflict count",
    ]:
        if phrase not in indexing:
            fail(f"evidence indexing framework missing quality contract: {phrase}")

    refresh = read("references/incremental-refresh-framework.md")
    for phrase in [
        "IncrementalRefreshPlan",
        "Source Change Routing",
        "Stale Object Handling",
        "IncrementalRefreshGate",
    ]:
        if phrase not in refresh:
            fail(f"incremental refresh framework missing quality contract: {phrase}")

    intake = read("references/user-intake-settings-framework.md")
    for phrase in [
        "ResearchSettings",
        "UserHypothesis",
        "Output Views",
        "Preflight Contract",
        "Prompt Builder Contract",
    ]:
        if phrase not in intake:
            fail(f"user intake framework missing quality contract: {phrase}")


def validate_maintenance_contracts() -> None:
    manifest = json.loads(read("skill_manifest.json"))
    if manifest.get("schema_version") != 1:
        fail("skill_manifest.json schema_version must be 1")
    if manifest.get("skill_id") != "stock-research-report":
        fail("skill_manifest.json skill_id must be stock-research-report")
    if manifest.get("repo") != "OctavianYimingZhang/Stock-DeepResearch-Skill":
        fail("skill_manifest.json repo is not aligned with GitHub")
    if manifest.get("branch") != "main":
        fail("skill_manifest.json branch must be main")
    if manifest.get("entrypoint") != "SKILL.md":
        fail("skill_manifest.json entrypoint must be SKILL.md")

    health = "\n".join(manifest.get("health_commands", []))
    for command in [
        "python3 scripts/validate.py",
        "python3 scripts/validate_ontology.py",
        "python3 scripts/validate_settings.py",
        "python3 scripts/validate_report_output.py evals/fixtures/report-contract-fixture.md",
        "python3 scripts/validate_research_manifest.py evals/fixtures/report-contract-fixture.manifest.json",
        "python3 scripts/validate_report_against_manifest.py evals/fixtures/report-contract-fixture.md evals/fixtures/report-contract-fixture.manifest.json",
    ]:
        if command not in health:
            fail(f"skill_manifest.json missing health command: {command}")
    post_update = "\n".join(manifest.get("post_update_commands", []))
    if "python3 -m pip install -r requirements.txt" not in post_update:
        fail("skill_manifest.json missing requirements installation command")

    requirements = read("requirements.txt").lower()
    if "pyyaml" not in requirements:
        fail("requirements.txt must include pyyaml")

    maintenance = read("scripts/skill_maintenance.py")
    for phrase in [
        "doctor",
        "read-only",
        "dry-run",
        "--yes",
        "backup",
        "--ff-only",
        "health_commands",
        "rolled_back_to",
        "proposal-only",
    ]:
        if phrase not in maintenance:
            fail(f"scripts/skill_maintenance.py missing maintenance phrase: {phrase}")
    if "git push" in maintenance:
        fail("scripts/skill_maintenance.py must not push changes")

    workflow = read(".github/workflows/skill-health.yml")
    for phrase in [
        "permissions:",
        "contents: read",
        "scripts/skill_maintenance.py doctor --json",
        "scripts/skill_maintenance.py update --dry-run --json",
    ]:
        if phrase not in workflow:
            fail(f"skill-health workflow missing phrase: {phrase}")
    if "contents: write" in workflow:
        fail("skill-health workflow must not request write permissions")


def validate_ontology_contracts() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_ontology.py")],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        message = result.stderr.strip() or result.stdout.strip()
        fail(f"ontology validation failed: {message}")


def validate_settings_contracts() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_settings.py")],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        message = result.stderr.strip() or result.stdout.strip()
        fail(f"settings validation failed: {message}")


def validate_manifest_contracts() -> None:
    manifest = ROOT / "evals" / "fixtures" / "report-contract-fixture.manifest.json"
    report = ROOT / "evals" / "fixtures" / "report-contract-fixture.md"
    for command in [
        [sys.executable, str(ROOT / "scripts" / "validate_research_manifest.py"), str(manifest)],
        [
            sys.executable,
            str(ROOT / "scripts" / "validate_report_against_manifest.py"),
            str(report),
            str(manifest),
        ],
    ]:
        result = subprocess.run(
            command,
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        if result.returncode != 0:
            message = result.stderr.strip() or result.stdout.strip()
            fail(f"manifest validation failed: {message}")


def main() -> None:
    validate_skill()
    validate_readme()
    validate_references()
    validate_evals()
    validate_english_only_repo_text()
    validate_no_baked_case_language()
    validate_quality_contracts()
    validate_maintenance_contracts()
    validate_ontology_contracts()
    validate_settings_contracts()
    validate_manifest_contracts()
    print("OK: validation passed")


if __name__ == "__main__":
    main()
