#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_TOP_LEVEL = [
    "research_run",
    "source_snapshots",
    "source_partitions",
    "evidence_items",
    "claims",
    "data_gaps",
    "valuation_cases",
    "equity_bridges",
    "technical_setups",
    "trade_plans",
    "short_seller_assessments",
    "report_sections",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def require_dict(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        fail(f"{label} must be an object")
    return value


def require_list(value: Any, label: str) -> list[Any]:
    if not isinstance(value, list):
        fail(f"{label} must be a list")
    return value


def ids(items: list[Any], label: str) -> set[str]:
    result: set[str] = set()
    for item in items:
        obj = require_dict(item, label)
        object_id = obj.get("id")
        if not isinstance(object_id, str) or not object_id:
            fail(f"{label} item missing id")
        if object_id in result:
            fail(f"{label} contains duplicate id: {object_id}")
        result.add(object_id)
    return result


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: validate_research_manifest.py <manifest.json>")
    path = Path(sys.argv[1])
    if not path.exists():
        fail(f"missing manifest file: {path}")
    manifest = json.loads(path.read_text(encoding="utf-8"))
    root = require_dict(manifest, "manifest")

    for key in REQUIRED_TOP_LEVEL:
        if key not in root:
            fail(f"manifest missing top-level key: {key}")

    run = require_dict(root["research_run"], "research_run")
    gate_results = require_list(run.get("gate_results"), "research_run.gate_results")
    allowed_gate_status = {"pass", "warn", "block", "fail", "not_applicable"}
    for result in gate_results:
        obj = require_dict(result, "gate result")
        if obj.get("status") not in allowed_gate_status:
            fail(f"unsupported gate status: {obj.get('status')}")

    source_snapshot_ids = ids(require_list(root["source_snapshots"], "source_snapshots"), "source_snapshots")
    source_partition_ids = ids(require_list(root["source_partitions"], "source_partitions"), "source_partitions")
    evidence_ids = ids(require_list(root["evidence_items"], "evidence_items"), "evidence_items")
    claim_ids = ids(require_list(root["claims"], "claims"), "claims")
    data_gap_ids = ids(require_list(root["data_gaps"], "data_gaps"), "data_gaps")
    valuation_ids = ids(require_list(root["valuation_cases"], "valuation_cases"), "valuation_cases")
    equity_bridge_ids = ids(require_list(root["equity_bridges"], "equity_bridges"), "equity_bridges")
    technical_ids = ids(require_list(root["technical_setups"], "technical_setups"), "technical_setups")
    short_ids = ids(require_list(root["short_seller_assessments"], "short_seller_assessments"), "short_seller_assessments")

    for partition in require_list(root["source_partitions"], "source_partitions"):
        obj = require_dict(partition, "source partition")
        if obj.get("source_snapshot_id") not in source_snapshot_ids:
            fail(f"source partition {obj.get('id')} lacks valid source_snapshot_id")

    for evidence in require_list(root["evidence_items"], "evidence_items"):
        obj = require_dict(evidence, "evidence item")
        if obj.get("source_snapshot_id") not in source_snapshot_ids:
            fail(f"evidence item {obj.get('id')} lacks source snapshot lineage")
        if obj.get("source_partition_id") not in source_partition_ids:
            fail(f"evidence item {obj.get('id')} lacks source partition lineage")

    for claim in require_list(root["claims"], "claims"):
        obj = require_dict(claim, "claim")
        linked_evidence = set(obj.get("evidence_ids") or [])
        linked_gaps = set(obj.get("data_gap_ids") or [])
        if obj.get("materiality") == "high" and not linked_evidence and not linked_gaps:
            fail(f"high-materiality claim {obj.get('id')} lacks evidence or data gap")
        if linked_evidence - evidence_ids:
            fail(f"claim {obj.get('id')} references unknown evidence")
        if linked_gaps - data_gap_ids:
            fail(f"claim {obj.get('id')} references unknown data gap")

    for bridge in require_list(root["equity_bridges"], "equity_bridges"):
        obj = require_dict(bridge, "equity bridge")
        if obj.get("valuation_case_id") not in valuation_ids:
            fail(f"equity bridge {obj.get('id')} references unknown valuation case")
        blocker = obj.get("blocker_reason_or_gap")
        target = obj.get("target_price_or_blocker")
        if blocker in (None, "", "none") and target in (None, "", "blocked"):
            fail(f"equity bridge {obj.get('id')} lacks target or blocker")

    for valuation in require_list(root["valuation_cases"], "valuation_cases"):
        obj = require_dict(valuation, "valuation case")
        if obj.get("equity_bridge_id") not in equity_bridge_ids:
            fail(f"valuation case {obj.get('id')} lacks equity bridge")

    for setup in require_list(root["technical_setups"], "technical_setups"):
        obj = require_dict(setup, "technical setup")
        if obj.get("freshness_status") == "stale" and obj.get("drives_trade_plan") is True:
            fail(f"stale technical setup {obj.get('id')} drives trade plan")

    for plan in require_list(root["trade_plans"], "trade_plans"):
        obj = require_dict(plan, "trade plan")
        if obj.get("valuation_case_id") not in valuation_ids:
            fail(f"trade plan {obj.get('id')} references unknown valuation case")
        if obj.get("technical_setup_id") not in technical_ids:
            fail(f"trade plan {obj.get('id')} references unknown technical setup")
        if obj.get("short_seller_assessment_id") not in short_ids:
            fail(f"trade plan {obj.get('id')} references unknown short assessment")

    for assessment in require_list(root["short_seller_assessments"], "short_seller_assessments"):
        obj = require_dict(assessment, "short-seller assessment")
        if obj.get("grade") in {"C", "D", "F"} and not obj.get("valuation_or_size_effect"):
            fail(f"short-seller grade {obj.get('grade')} lacks valuation or size effect")

    for section in require_list(root["report_sections"], "report_sections"):
        obj = require_dict(section, "report section")
        cited_claims = set(obj.get("claim_ids") or [])
        if cited_claims - claim_ids:
            fail(f"report section {obj.get('section_name')} references unknown claim")

    print("OK: research manifest validation passed")


if __name__ == "__main__":
    main()
