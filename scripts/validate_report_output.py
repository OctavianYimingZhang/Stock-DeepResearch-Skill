#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_SECTIONS = [
    "Core Conclusion",
    "Why This Stock Exists Now",
    "Industry Chain And Bottleneck",
    "Company Position In The Chain",
    "Business Model Logic",
    "Scarcity And Moat Assessment",
    "Customers, Orders, And Commercialization Path",
    "Operations, Capacity, And Execution Quality",
    "Financial Quality, Assets, Debt, And Dilution",
    "Valuation And Market-Implied Expectation",
    "Catalysts, Risks, And Falsification",
    "Technical Structure And Trade Plan",
]

SOURCE_MARKERS = [
    "filing",
    "earnings call",
    "IR presentation",
    "regulator",
    "counterparty",
    "market data",
]

AUDIT_LABELS = [
    "Verified fact:",
    "Inference:",
    "Unanswered question:",
    "ArticleThesisMap note:",
    "Data gap:",
]

MIN_FULL_REPORT_CHARS = 15000
MIN_SECTION_PARAGRAPHS = 2


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def require(pattern: str, text: str, message: str, flags: int = re.IGNORECASE) -> None:
    if not re.search(pattern, text, flags):
        fail(message)


def is_contract_fixture(path: Path) -> bool:
    return path.name == "report-contract-fixture.md"


def section_body(text: str, section: str) -> str:
    pattern = rf"^##\s+{re.escape(section)}\s*$"
    match = re.search(pattern, text, re.MULTILINE)
    if not match:
        return ""
    start = match.end()
    next_match = re.search(r"^##\s+", text[start:], re.MULTILINE)
    end = start + next_match.start() if next_match else len(text)
    return text[start:end].strip()


def paragraph_count(section_text: str) -> int:
    blocks = [block.strip() for block in re.split(r"\n\s*\n", section_text) if block.strip()]
    prose_blocks = []
    for block in blocks:
        stripped = block.strip()
        if stripped.startswith("|") or stripped.startswith("```"):
            continue
        prose_blocks.append(stripped)
    return len(prose_blocks)


def validate_depth_and_readability(path: Path, text: str) -> None:
    if is_contract_fixture(path):
        return

    if len(text.strip()) < MIN_FULL_REPORT_CHARS:
        fail(
            f"full report is too short: {len(text.strip())} characters; "
            f"expected at least {MIN_FULL_REPORT_CHARS} unless the report is explicitly source-blocked"
        )

    for section in REQUIRED_SECTIONS:
        body = section_body(text, section)
        count = paragraph_count(body)
        if count < MIN_SECTION_PARAGRAPHS:
            fail(f"section '{section}' is too compressed: {count} prose paragraphs; expected at least {MIN_SECTION_PARAGRAPHS}")

    label_count = sum(text.count(label) for label in AUDIT_LABELS)
    if label_count > 18:
        fail(
            "report uses too many audit-style labels in final prose; "
            "convert internal labels into readable causal paragraphs"
        )

    one_line_sections = []
    for section in REQUIRED_SECTIONS:
        body = section_body(text, section)
        body_lines = [line for line in body.splitlines() if line.strip() and not line.strip().startswith("|")]
        if len(" ".join(body_lines).split()) < 90:
            one_line_sections.append(section)
    if one_line_sections:
        fail(f"sections lack explanatory prose depth: {one_line_sections}")


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: validate_report_output.py <report.md>")

    path = Path(sys.argv[1])
    if not path.exists():
        fail(f"missing report file: {path}")
    text = path.read_text(encoding="utf-8")

    for section in REQUIRED_SECTIONS:
        require(rf"^##\s+{re.escape(section)}\s*$", text, f"missing section: {section}", re.MULTILINE)

    if not any(f"[{marker}]" in text for marker in SOURCE_MARKERS):
        fail("report must include source markers for material numbers")

    require(r"investment dispute|re[- ]rating dispute|market debate|what the market is pricing", text, "missing opening investment dispute")
    require(r"outside thesis|thesis path|ArticleThesisMap|external thesis", text, "missing outside thesis-path replay")
    require(r"opportunity archetype|scarcity_bottleneck|policy_protected_supply_chain|customer_funded_capacity_ramp|industry beta|watchlist", text, "missing opportunity archetype routing")
    require(r"demand[-\s]+expansion", text, "missing demand-expansion assessment")
    require(r"scaling difficulty|supply cannot expand|qualification|certification|capex barrier", text, "missing scaling-difficulty assessment")
    require(r"bottleneck|scarcity", text, "missing bottleneck or scarcity assessment")
    require(r"commercialization visibility|commercialization path|order-to-revenue", text, "missing commercialization-path assessment")
    require(r"current[- ]market[- ]implied|current price implies|market implies", text, "missing current-market-implied valuation bridge")
    require(r"re[- ]rating|multiple expansion|market bucket", text, "missing re-rating bridge or multiple-expansion condition")
    require(r"EV[- ]to[- ]equity|target equity value|net debt", text, "missing EV-to-equity bridge")
    require(r"diluted shares|share count|pro[- ]forma shares", text, "missing share-count bridge")
    require(r"cash|short-term investments", text, "missing cash discussion")
    require(r"debt|lease liabilities|maturity", text, "missing debt or maturity discussion")
    require(r"backlog|order|purchase obligation|capacity reservation|contract", text, "missing order or backlog discussion")
    require(r"capacity|utilization|facility|production|ramp", text, "missing capacity or operating-ramp discussion")
    require(r"funding bridge|cash runway|funding gap|capital need", text, "missing funding bridge or cash-runway analysis")
    require(r"operating cash flow|OCF|cash conversion|working capital", text, "missing cash-conversion reconciliation")
    require(r"EBITDA[- ]to[- ]OCF[- ]to[- ]FCF|EBITDA.*OCF.*FCF", text, "missing EBITDA-to-OCF-to-FCF bridge")
    require(r"FCF margin|FCF conversion", text, "missing FCF margin or FCF conversion")
    require(r"SBC[- ]adjusted|stock[- ]based compensation", text, "missing SBC-adjusted cash-flow treatment")
    require(r"FCF per share|free cash flow per share", text, "missing FCF per-share analysis")
    require(r"Short-Seller Risk:\s*[ABCDF]\b|grade:\s*[ABCDF]\b", text, "missing short-seller risk grade")
    require(r"verified fact|inference|unanswered question|allegation", text, "missing fact/inference separation")
    require(r"falsification|would break the thesis|monitoring item", text, "missing short-risk falsification lens")
    require(r"chart date|OHLCV|adjusted", text, "missing chart freshness or adjustment note")
    require(r"entry", text, "missing entry level")
    require(r"stop", text, "missing stop loss or invalidation")
    require(r"take[- ]profit|TP1|TP2", text, "missing take-profit levels")
    require(r"Decision Grade|action grade", text, "missing decision scorecard action grade")
    require(r"binding cap|cap reason", text, "missing scorecard binding cap reason")
    require(r"trim|add|partial profit|observe", text, "missing trim/add or observation logic")

    validate_depth_and_readability(path, text)

    if re.search(r"probability-weighted|method average|average of.*DCF.*P/E", text, re.IGNORECASE | re.DOTALL):
        fail("report appears to average valuation methods")

    print("OK: report output validation passed")


if __name__ == "__main__":
    main()