#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def load_settings(path: Path) -> dict[str, Any]:
    if not path.exists():
        fail(f"missing settings file: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        fail("settings file must contain a JSON object")
    return data


def value(data: dict[str, Any], path: str, fallback: str = "unspecified") -> str:
    current: Any = data
    for part in path.split("."):
        if not isinstance(current, dict) or part not in current:
            return fallback
        current = current[part]
    if current is None:
        return fallback
    return str(current)


def build_prompt(settings: dict[str, Any], identifier: str) -> str:
    lines = [
        f"Use $stock-research-report to analyze {identifier}.",
        "",
        "Settings:",
        f"- language: {value(settings, 'report_language')}",
        f"- mode: {value(settings, 'research_mode')}",
        f"- output view: {value(settings, 'output_view')}",
        f"- horizon: {value(settings, 'horizon')}",
        f"- source policy: {value(settings, 'source_policy.mode')}; secondary research {value(settings, 'source_policy.secondary_research')}",
        f"- valuation strictness: share count blocker {value(settings, 'valuation_policy.block_target_if_share_count_unresolved')}, net debt blocker {value(settings, 'valuation_policy.block_target_if_net_debt_unresolved')}, senior claims blocker {value(settings, 'valuation_policy.block_target_if_senior_claims_unresolved')}",
        f"- short-risk threshold: {value(settings, 'short_risk_policy.expand_threshold')}",
        f"- technical requirement: current OHLCV {value(settings, 'technical_policy.require_current_ohlcv')}, chart date {value(settings, 'technical_policy.require_chart_date')}, adjusted status {value(settings, 'technical_policy.require_adjusted_status')}",
        f"- interaction level: {value(settings, 'interaction_level')}",
        "",
        "Apply the Skill evidence rules. Treat user hypotheses as questions to test, not as evidence.",
    ]
    return "\n".join(lines)


def main() -> None:
    if len(sys.argv) != 3:
        fail("usage: build_prompt_from_settings.py <settings.json> <ticker-or-company-identifier>")
    settings_path = Path(sys.argv[1])
    if not settings_path.is_absolute():
        settings_path = ROOT / settings_path
    print(build_prompt(load_settings(settings_path), sys.argv[2]))


if __name__ == "__main__":
    main()
