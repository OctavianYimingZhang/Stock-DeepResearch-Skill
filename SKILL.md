---
name: stock-research-report
description: Build source-backed public-company deep research reports, valuation context, risk reviews, and investment memo drafts from current filings, market data, transcripts, and cited evidence.
---

# Stock Deep Research Report

Use this skill when the user asks for deep research on a listed company, ticker, sector, equity thesis, earnings setup, valuation context, risk review, or public-company investment memo.

## Operating rules

- Treat every factual claim as source-bound. Use primary filings, company investor-relations materials, exchange disclosures, earnings transcripts, and reputable market data before secondary commentary.
- Use current sources when prices, guidance, estimates, ownership, valuation multiples, macro data, or company leadership may have changed.
- Separate verified facts, calculations, estimates, and interpretation.
- State source dates and reporting periods.
- Do not provide personalized financial advice. Frame conclusions as research, scenarios, and decision considerations.
- If evidence is insufficient or conflicting, say so and keep the conclusion blocked or conditional.

## Workflow

1. Define scope: ticker/company, exchange, report date, time horizon, target audience, required depth, and whether the user wants a full report or a focused section.
2. Collect sources: latest annual/interim filings, earnings releases, transcripts, investor presentations, segment disclosures, balance-sheet data, peer data, price/volume data, and relevant industry sources.
3. Build an evidence register: claim, source, date, metric period, extraction note, confidence level, and unresolved conflicts.
4. Analyze the business: revenue model, segments, customers, supply chain, competitive position, unit economics, cyclicality, regulation, and capital intensity.
5. Analyze financial quality: revenue durability, gross margin, operating leverage, cash conversion, working capital, capital allocation, leverage, dilution, and accounting risks.
6. Analyze valuation: market capitalization, enterprise value, share count, net debt/cash, peer multiples, historical range, scenario assumptions, and sensitivity drivers.
7. Analyze risks and catalysts: earnings inflections, order backlog, customer concentration, policy changes, refinancing, litigation, technological displacement, short-interest context, and market positioning.
8. Draft the report with citations beside the claims they support. Keep assumptions explicit.
9. Run local validation scripts only when producing or changing repository artifacts.

## Report structure

Use this order unless the user requests a narrower output:

1. Scope and data cutoff
2. Executive view
3. Company profile
4. Business model and segment economics
5. Industry and competitive position
6. Financial quality
7. Valuation and scenarios
8. Technical and positioning context, if requested
9. Risks, catalysts, and watch items
10. Source log and unresolved evidence gaps

## Repository resources

Read only the files needed for the user request:

- `references/business-model-framework.md`: business model and segment analysis.
- `references/evidence-indexing-framework.md`: evidence register and source traceability.
- `references/incremental-refresh-framework.md`: updating an existing report with new filings or market data.
- `references/opportunity-discovery-framework.md`: screening and idea discovery.
- `references/profit-cash-flow-quality-framework.md`: earnings quality and cash conversion checks.
- `references/quality-calibration-loop.md`: report quality review.
- `references/report-style-patterns.md`: formatting and writing patterns.
- `references/scorecard-decision-framework.md`: scoring discipline.
- `references/short-seller-risk-framework.md`: short-risk review.
- `references/technical-analysis-framework.md`: optional price/volume analysis.
- `references/user-intake-settings-framework.md`: user preference and scope settings.
- `references/valuation-framework.md`: valuation process.
- `references/article-thesis-distillation-framework.md`: turning source articles into thesis notes.

## Local commands

- `python3 scripts/validate.py`: repository sanity check.
- `python3 scripts/validate_settings.py`: settings schema/profile check.
- `python3 scripts/validate_report_output.py <report.md>`: report format check.
- `python3 scripts/validate_research_manifest.py <manifest.json>`: source-manifest check.
- `python3 scripts/validate_report_against_manifest.py <report.md> <manifest.json>`: report-to-source consistency check.
