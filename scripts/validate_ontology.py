#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ONTOLOGY_DIR = ROOT / "ontology"

REQUIRED_OBJECTS = {
    "ResearchSettings",
    "UserHypothesis",
    "ResearchRun",
    "Company",
    "Security",
    "SourceDocument",
    "SourceSnapshot",
    "SourcePartition",
    "EvidencePartition",
    "EvidenceItem",
    "Claim",
    "ConflictResolution",
    "MetricObservation",
    "ContractOrder",
    "OrderQualityAssessment",
    "DebtInstrument",
    "DilutionInstrument",
    "FinancialQualityAssessment",
    "ProfitCashFlowQualityAnalysis",
    "CurrentMarketImpliedBridge",
    "ValuationMethodSelection",
    "EquityBridge",
    "ValuationCase",
    "ShortRiskSignal",
    "ShortSellerAssessment",
    "TechnicalSetup",
    "ExpectationRevisionAssessment",
    "MomentumRegimeAssessment",
    "ValuationOddsAssessment",
    "RiskFilterAssessment",
    "DecisionScorecard",
    "TradePlan",
    "IncrementalRefreshPlan",
    "ActionExecution",
    "GateResult",
    "OutputView",
    "DataGap",
    "Report",
    "ReportSection",
}

REQUIRED_LINKS = {
    "configures_run",
    "tests_hypothesis",
    "executes",
    "uses_snapshot",
    "contains",
    "derives_from",
    "partitions_source",
    "routes_to_evidence",
    "supports",
    "contradicts",
    "invalidates",
    "pruned_by_partition",
    "supersedes",
    "blocks_claim",
    "refreshed_by",
    "executed_action",
    "cites",
    "supports_valuation",
    "refines_financial_quality",
    "cash_quality_supports_valuation",
    "cash_quality_flags_short_risk",
    "bridges_to_target_price",
    "discounts_valuation",
    "constrains_trade_plan",
    "expectation_feeds_scorecard",
    "momentum_feeds_scorecard",
    "valuation_odds_feeds_scorecard",
    "risk_filter_feeds_scorecard",
    "scorecard_constrains_trade",
    "valuation_constrains_trade",
    "short_risk_constrains_trade",
    "records_gate_result",
    "projects_view",
}

REQUIRED_ACTIONS = {
    "CaptureResearchSettings",
    "StartResearchRun",
    "AttachSourceDocument",
    "BuildSourcePartitions",
    "BuildEvidencePartitions",
    "ExtractEvidence",
    "NormalizeOperatingObjects",
    "ClassifyClaim",
    "ResolveConflictingFacts",
    "BuildBusinessModelThesis",
    "DetectSourceChange",
    "IncrementalRefresh",
    "GradeOrderQuality",
    "ReconcileFinancials",
    "AnalyzeProfitCashFlowQuality",
    "ReconcileShareCountAndEV",
    "InferCurrentMarketPricing",
    "SelectPrimaryValuationMethod",
    "BuildValuationCase",
    "BuildEquityBridge",
    "RunShortRiskScreen",
    "ValidateTechnicalSetup",
    "BuildDecisionScorecard",
    "BuildTradePlan",
    "GenerateReportSection",
    "SelectOutputView",
    "FinalizeReport",
}

REQUIRED_FUNCTIONS = {
    "build_source_partition_index",
    "extract_material_metric",
    "classify_claim_materiality",
    "detect_source_conflict",
    "calculate_enterprise_value",
    "risk_adjust_backlog_value",
    "build_order_to_revenue_bridge",
    "cash_conversion_score",
    "calculate_cash_quality_bridge",
    "assess_working_capital_cycle",
    "calculate_sbc_adjusted_fcf_per_share",
    "debt_safety_score",
    "select_valuation_method",
    "build_re_rating_bridge",
    "build_funding_bridge",
    "detect_target_price_blockers",
    "calculate_equity_bridge",
    "short_risk_grade",
    "build_falsification_lens",
    "build_decision_scorecard",
    "determine_action_grade_cap",
    "technical_freshness_check",
    "position_size_from_stop_distance",
    "determine_gate_result",
    "select_output_view",
}

REQUIRED_GATES = {
    "LakehouseLayerGate",
    "SettingsGate",
    "EvidenceGate",
    "LineageGate",
    "PartitionCoverageGate",
    "OrderGate",
    "FinancialGate",
    "ProfitCashFlowQualityGate",
    "DebtGate",
    "EquityBridgeGate",
    "ValuationGate",
    "ShortRiskGate",
    "TechnicalGate",
    "DecisionScorecardGate",
    "FreshnessGate",
    "IncrementalRefreshGate",
    "OutputViewGate",
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
            if key == "reads" and item.get("name") in {"CaptureResearchSettings"}:
                if not isinstance(item.get(key), list):
                    fail(f"{item['name']} reads must be a list")
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
