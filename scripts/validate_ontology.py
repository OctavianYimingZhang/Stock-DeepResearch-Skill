#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ONTOLOGY_DIR = ROOT / "ontology"

REQUIRED_OBJECTS = {
    "Company",
    "Security",
    "SourceDocument",
    "EvidenceItem",
    "Claim",
    "MetricObservation",
    "ContractOrder",
    "OrderQualityAssessment",
    "DebtInstrument",
    "DilutionInstrument",
    "FinancialQualityAssessment",
    "CurrentMarketImpliedBridge",
    "ValuationMethodSelection",
    "ValuationCase",
    "ShortRiskSignal",
    "ShortSellerAssessment",
    "TechnicalSetup",
    "TradePlan",
    "DataGap",
    "Report",
    "ReportSection",
}

REQUIRED_LINKS = {
    "contains",
    "supports",
    "contradicts",
    "blocks_claim",
    "cites",
    "supports_valuation",
    "discounts_valuation",
    "constrains_trade_plan",
}

REQUIRED_ACTIONS = {
    "StartResearchRun",
    "ExtractEvidence",
    "ClassifyClaim",
    "ResolveConflictingFacts",
    "GradeOrderQuality",
    "ReconcileFinancials",
    "ReconcileShareCountAndEV",
    "InferCurrentMarketPricing",
    "SelectPrimaryValuationMethod",
    "BuildValuationCase",
    "RunShortRiskScreen",
    "ValidateTechnicalSetup",
    "GenerateReportSection",
    "FinalizeReport",
}

REQUIRED_FUNCTIONS = {
    "calculate_enterprise_value",
    "risk_adjust_backlog_value",
    "cash_conversion_score",
    "debt_safety_score",
    "select_valuation_method",
    "detect_target_price_blockers",
    "short_risk_grade",
    "technical_freshness_check",
    "position_size_from_stop_distance",
}

REQUIRED_GATES = {
    "EvidenceGate",
    "OrderGate",
    "FinancialGate",
    "DebtGate",
    "ValuationGate",
    "ShortRiskGate",
    "TechnicalGate",
    "DataGapGate",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def load_yaml(path: Path) -> dict[str, object]:
    if not path.exists():
        fail(f"missing ontology file: {path.relative_to(ROOT)}")
    try:
        import yaml  # type: ignore
    except ImportError as exc:
        fail(f"PyYAML is required to validate ontology files: {exc}")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        fail(f"{path.relative_to(ROOT)} did not parse to a mapping")
    if data.get("version") != 1:
        fail(f"{path.relative_to(ROOT)} must declare version: 1")
    return data


def names(items: object, file_label: str) -> set[str]:
    if not isinstance(items, list) or not items:
        fail(f"{file_label} must contain a non-empty list")
    result: set[str] = set()
    for item in items:
        if not isinstance(item, dict):
            fail(f"{file_label} contains a non-mapping item")
        name = item.get("name")
        if not isinstance(name, str) or not name:
            fail(f"{file_label} item missing name")
        if name in result:
            fail(f"{file_label} contains duplicate name: {name}")
        result.add(name)
    return result


def require_list(item: dict[str, object], key: str, context: str) -> None:
    value = item.get(key)
    if not isinstance(value, list) or not value:
        fail(f"{context} must contain non-empty {key}")
    if not all(isinstance(v, str) and v for v in value):
        fail(f"{context} {key} must contain only non-empty strings")


def validate() -> None:
    object_data = load_yaml(ONTOLOGY_DIR / "object_types.yaml")
    link_data = load_yaml(ONTOLOGY_DIR / "link_types.yaml")
    action_data = load_yaml(ONTOLOGY_DIR / "action_types.yaml")
    function_data = load_yaml(ONTOLOGY_DIR / "functions.yaml")
    gate_data = load_yaml(ONTOLOGY_DIR / "workflow_gates.yaml")

    object_items = object_data.get("object_types")
    object_names = names(object_items, "object_types")
    missing_objects = REQUIRED_OBJECTS - object_names
    if missing_objects:
        fail(f"missing required object types: {sorted(missing_objects)}")
    assert isinstance(object_items, list)
    for item in object_items:
        assert isinstance(item, dict)
        require_list(item, "required_properties", f"object {item['name']}")
        if not item.get("purpose"):
            fail(f"object {item['name']} missing purpose")

    link_items = link_data.get("link_types")
    link_names = names(link_items, "link_types")
    missing_links = REQUIRED_LINKS - link_names
    if missing_links:
        fail(f"missing required link types: {sorted(missing_links)}")
    assert isinstance(link_items, list)
    for item in link_items:
        assert isinstance(item, dict)
        for key in ["from", "to"]:
            endpoint = item.get(key)
            if endpoint not in object_names:
                fail(f"link {item['name']} has unknown {key}: {endpoint}")
        if not item.get("purpose"):
            fail(f"link {item['name']} missing purpose")

    action_items = action_data.get("action_types")
    action_names = names(action_items, "action_types")
    missing_actions = REQUIRED_ACTIONS - action_names
    if missing_actions:
        fail(f"missing required action types: {sorted(missing_actions)}")
    assert isinstance(action_items, list)
    for item in action_items:
        assert isinstance(item, dict)
        for key in ["reads", "writes", "required_checks"]:
            if key == "reads" and item.get("name") == "StartResearchRun":
                if not isinstance(item.get(key), list):
                    fail("StartResearchRun reads must be a list")
                continue
            require_list(item, key, f"action {item['name']}")
        for key in ["reads", "writes"]:
            for object_name in item.get(key, []):
                if object_name not in object_names:
                    fail(f"action {item['name']} references unknown object: {object_name}")

    function_items = function_data.get("functions")
    function_names = names(function_items, "functions")
    missing_functions = REQUIRED_FUNCTIONS - function_names
    if missing_functions:
        fail(f"missing required functions: {sorted(missing_functions)}")
    assert isinstance(function_items, list)
    for item in function_items:
        assert isinstance(item, dict)
        require_list(item, "inputs", f"function {item['name']}")
        require_list(item, "blocking_gaps", f"function {item['name']}")
        if not item.get("output"):
            fail(f"function {item['name']} missing output")

    gate_items = gate_data.get("workflow_gates")
    gate_names = names(gate_items, "workflow_gates")
    missing_gates = REQUIRED_GATES - gate_names
    if missing_gates:
        fail(f"missing required workflow gates: {sorted(missing_gates)}")
    assert isinstance(gate_items, list)
    for item in gate_items:
        assert isinstance(item, dict)
        require_list(item, "required_objects", f"gate {item['name']}")
        require_list(item, "pass_conditions", f"gate {item['name']}")
        for object_name in item.get("required_objects", []):
            if object_name not in object_names:
                fail(f"gate {item['name']} references unknown object: {object_name}")

    print("OK: ontology validation passed")


if __name__ == "__main__":
    validate()
