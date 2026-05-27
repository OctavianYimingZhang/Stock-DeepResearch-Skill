#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path


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

SOURCE_MARKERS = [
    "filing",
    "earnings call",
    "IR presentation",
    "regulator",
    "counterparty",
    "market data",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def require(pattern: str, text: str, message: str, flags: int = re.IGNORECASE) -> None:
    if not re.search(pattern, text, flags):
        fail(message)


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

    if re.search(r"probability-weighted|method average|average of.*DCF.*P/E", text, re.IGNORECASE | re.DOTALL):
        fail("report appears to average valuation methods")

    print("OK: report output validation passed")


if __name__ == "__main__":
    main()
