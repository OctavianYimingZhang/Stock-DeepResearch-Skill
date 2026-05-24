#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    if len(sys.argv) != 3:
        fail("usage: validate_report_against_manifest.py <report.md> <manifest.json>")
    report_path = Path(sys.argv[1])
    manifest_path = Path(sys.argv[2])
    if not report_path.exists():
        fail(f"missing report file: {report_path}")
    if not manifest_path.exists():
        fail(f"missing manifest file: {manifest_path}")
    report = report_path.read_text(encoding="utf-8")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not isinstance(manifest, dict):
        fail("manifest must be an object")

    sections = manifest.get("report_sections")
    if not isinstance(sections, list) or not sections:
        fail("manifest must contain report sections")
    for section in sections:
        if not isinstance(section, dict):
            fail("report section manifest item must be an object")
        name = section.get("section_name")
        if not isinstance(name, str) or not name:
            fail("report section missing section_name")
        if not re.search(rf"^##\s+{re.escape(name)}\s*$", report, re.MULTILINE):
            fail(f"report missing manifest section: {name}")
        if section.get("blocked_status") == "blocked":
            blocked_terms = ["blocked", "cannot be concluded", "data gap"]
            if not any(term in report.lower() for term in blocked_terms):
                fail(f"blocked section {name} is not marked in report text")

    if re.search(r"target price|price target", report, re.IGNORECASE):
        bridges = manifest.get("equity_bridges")
        if not isinstance(bridges, list) or not bridges:
            fail("report target language requires equity bridge manifest")
        usable_bridge = False
        for bridge in bridges:
            if not isinstance(bridge, dict):
                continue
            blocker = bridge.get("blocker_reason_or_gap")
            target = bridge.get("target_price_or_blocker")
            if blocker in (None, "", "none") and target not in (None, "", "blocked"):
                usable_bridge = True
        if not usable_bridge:
            fail("report target language lacks unblocked equity bridge")

    print("OK: report-manifest validation passed")


if __name__ == "__main__":
    main()
