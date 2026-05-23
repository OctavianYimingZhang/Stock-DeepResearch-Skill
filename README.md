# stock-research-report

A self-contained ontology-backed public-company deep research report Skill.

The Skill produces analyst style deep research reports with four integrated
modules:

1. business-model logic
2. valuation, including assets, orders/backlog, debt, and dilution
3. short-seller risk
4. technical analysis and trade planning

This repository has been refactored from the old architecture that stitched
together four standalone Skills. The Skill no longer depends at runtime on:

- `Stock-Analysis-Skill`
- `valuation-calculator`
- `short-seller-risk-analysis`
- `technical-analysis-patterns`

The strongest methods from those repositories are now consolidated into this
repository's reference framework.

The final report is a projection from an evidence-backed object graph. The graph
connects source documents, evidence items, claims, metrics, orders, assets,
debt, valuation cases, short-risk signals, technical setups, data gaps, and
report sections.

The research data flow uses a lightweight lakehouse pattern: Bronze source
snapshots, Silver validated evidence, Gold analysis objects, and Report View
sections. Evidence partitions and incremental refresh plans keep context narrow
when only part of the research graph changed.

## Usage

```text
Use $stock-research-report to analyze [TICKER]
```

Optional inputs:

- company name, exchange, and currency
- Bloomberg, FactSet, or Capital IQ screenshots
- filings, investor presentations, or earnings-call transcripts
- K-line screenshots or OHLCV data
- user focus areas such as valuation, short-seller risk, order quality, or
  technical entry

## Output Structure

The report uses this fixed structure:

1. Company Overview
2. Business Model Logic
3. Operations, Customers, And Orders
4. Financials, Assets, And Debt
5. Valuation
6. Short-Seller Risk
7. Technical Analysis
8. Risk Factors
9. Trade Plan

## Evidence Priority

Use sources in this order:

1. issuer filings, exchange notices, and regulator records
2. issuer investor relations, earnings-call transcripts, and formal guidance
3. government, regulator, industry association, customer, and partner
   disclosures
4. reliable market-data providers and terminal data
5. high-quality secondary research

User-provided historical reports are style, structure, and depth references
only. They are not factual sources for a new report.

## Core Rules

- Do not invent data, dates, contracts, customers, orders, or target prices.
- State data gaps explicitly.
- Build the ontology object graph before drafting report prose.
- Preserve source snapshots and run lineage for material claims.
- Use evidence partitions before loading long source text.
- Use incremental refresh when only a subset of source material changed.
- Use one primary valuation method; other methods are sanity checks only.
- Valuation must cover assets, orders/backlog, debt, cash, and dilution.
- Short-seller risk must cover customer/contract authenticity, revenue
  recognition, cash-flow quality, related parties, audit quality, insider
  behavior, equity financing, and regulatory risk.
- Technical analysis must output trend, pattern, support/resistance, entry, stop
  loss, and take-profit levels.

## Reference Files

- `references/business-model-framework.md`
- `references/valuation-framework.md`
- `references/short-seller-risk-framework.md`
- `references/technical-analysis-framework.md`
- `references/report-style-patterns.md`
- `references/research-lakehouse-framework.md`
- `references/evidence-indexing-framework.md`
- `references/incremental-refresh-framework.md`
- `references/ontology-framework.md`
- `references/quality-calibration-loop.md`
- `references/external-inspirations-and-license-notes.md`

## Ontology Layer

The lightweight ontology is stored in:

- `ontology/object_types.yaml`
- `ontology/link_types.yaml`
- `ontology/action_types.yaml`
- `ontology/functions.yaml`
- `ontology/workflow_gates.yaml`

The central object is `Claim`. Material claims must link to evidence or become
explicit data gaps. Workflow gates then check evidence, source priority, order
quality, cash conversion, debt, valuation, short risk, technical freshness, and
blocked conclusions before report composition.

Additional ontology objects support source lineage and efficient refresh:
`SourceSnapshot`, `EvidencePartition`, `ResearchRun`, `ActionExecution`,
`IncrementalRefreshPlan`, and `ConflictResolution`.

## Calibration Method

The current Skill was calibrated with a fresh public-company test outside the
prior reference-report set. The temporary company name, ticker, and generated
draft are intentionally not committed, because company-specific cases must not
become runtime triggers.

The comparison found gaps in four areas:

- valuation needed a current-market-implied expectation before the analyst
  target
- orders needed a quality ladder for cases where formal backlog is absent
- financial quality needed net-income-to-operating-cash-flow reconciliation
- technical analysis needed chart-date freshness and adjusted-OHLCV controls

Those gaps are now encoded in the Skill, reference framework, eval metadata, and
validation script.

## External Inspirations And Licenses

The Skill borrows workflow ideas from public projects but does not copy
third-party code or long prompt text. Referenced projects:

- [Kronos](https://github.com/shiyu-coder/Kronos)
- [FinRobot](https://github.com/AI4Finance-Foundation/FinRobot)
- [TradingAgents](https://github.com/TauricResearch/TradingAgents)
- [ai-hedge-fund](https://github.com/virattt/ai-hedge-fund)
- [Anthropic financial-services plugins](https://github.com/anthropics/financial-services-plugins)
- [TraderMonty Claude Trading Skills](https://github.com/tradermonty/claude-trading-skills)
- [OctagonAI skills](https://github.com/OctagonAI/skills)
- [Palantir Foundry Ontology documentation](https://www.palantir.com/docs/foundry/ontology/overview/)
- [Databricks documentation](https://docs.databricks.com/)
- [Snowflake documentation](https://docs.snowflake.com/)

License notes are documented in
`references/external-inspirations-and-license-notes.md`.

## Validation

Run:

```bash
python3 scripts/validate.py
```

To check the ontology contracts directly:

```bash
python3 scripts/validate_ontology.py
```

To check a generated markdown report against the output contract:

```bash
python3 scripts/validate_report_output.py path/to/report.md
```

The repository includes `evals/fixtures/report-contract-fixture.md` as a
minimal contract fixture for CI.

The validator checks:

- Skill metadata
- reference links
- eval case metadata
- required report structure
- removal of old orchestration dependencies
- absence of baked-in company names or ticker-based prompts
- English-only repository text for Skill and GitHub-facing files
- ontology object, link, action, function, and gate contracts
- quality-loop contracts for source markers, implied valuation, order quality,
  cash conversion, short risk, and technical freshness

## License

MIT
