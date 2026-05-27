# Stock DeepResearch Skill

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Validation](https://img.shields.io/badge/validation-local%20contracts-brightgreen.svg)](#validation)
[![Language](https://img.shields.io/badge/repository%20text-English%20only-lightgrey.svg)](#core-rules)

`stock-research-report` is a self-contained Codex Skill for producing
evidence-first public-company deep research reports. It combines business-model
analysis, profit and cash-flow quality, valuation, short-seller risk review,
decision scorecard grading, and technical trade planning into one
ontology-backed research workflow.

The project is designed for analysts who need a report that says what can be
verified, what is only an inference, what is still blocked by missing data, and
how valuation and trade conclusions change when evidence quality is weak.

## What It Produces

The Skill generates analyst-style reports with five integrated pillars:

1. business-model logic
2. profit and cash-flow quality, including owner FCF, working capital, capex,
   SBC, dilution, and per-share cash flow
3. valuation, including assets, orders/backlog, debt, dilution, and an explicit
   equity bridge
4. short-seller risk
5. decision scorecard, technical analysis, and trade planning

The default report has nine sections: company overview, business model,
operations and orders, financials and debt, valuation, short-seller risk,
technical analysis, risk factors, and trade plan.

## Why This Exists

Most AI-generated equity reports fail in predictable ways: they mix facts with
opinions, treat weak order language as backlog, skip the EV-to-equity bridge,
ignore debt and dilution, or invent trade levels from stale charts. This
repository turns those failure modes into object contracts, gates, and
validators.

The final report is not written directly from raw text. It is projected from an
evidence-backed object graph that connects source snapshots, source partitions,
evidence items, claims, metrics, orders, assets, debt, valuation cases,
profit/cash-flow quality, short-risk signals, decision scorecards, technical
setups, data gaps, gate results, and report sections.

## Architecture At A Glance

```text
ResearchSettings
  -> SourceSnapshot
  -> SourcePartition
  -> EvidenceItem
  -> Claim
  -> analysis objects
  -> ReportSection
```

The research data flow uses a lightweight lakehouse pattern:

- Bronze: immutable source snapshots
- Source Index: pre-extraction source partitions
- Silver: validated evidence, claims, metrics, orders, debt, and dilution
- Gold: business thesis, profit/cash-flow quality, equity bridge, valuation,
  short risk, technical setup, decision scorecard, and trade plan
- Report View: final output sections

Gate results are explicit: `pass`, `warn`, `block`, `fail`, or
`not_applicable`. A blocked target price, blocked trade plan, or blocked
high-conviction conclusion is treated as a correct output when evidence is
insufficient.

This repository provides a research workflow and validation framework. It does
not provide investment advice, trading advice, or a guarantee that source data
is complete or current.

## Quick Start

```text
Use $stock-research-report to analyze [TICKER]
```

Useful optional inputs:

- company name, exchange, and currency
- filings, investor presentations, or earnings-call transcripts
- terminal screenshots for price, market cap, EV, share count, cash, debt, and
  peer multiples
- K-line screenshots or OHLCV data with chart date and adjusted status
- user focus areas such as valuation, short-seller risk, order quality, debt,
  dilution, or technical entry

Runtime settings can also be supplied through `config/settings.schema.json`.
The default profile is `config/profiles/default.json`, and the onboarding flow
is `config/onboarding.flow.yaml`.

This repository has been refactored from the old architecture that stitched
together four standalone Skills. The Skill no longer depends at runtime on:

- `Stock-Analysis-Skill`
- `valuation-calculator`
- `short-seller-risk-analysis`
- `technical-analysis-patterns`

The strongest methods from those repositories are now consolidated into this
repository's reference framework.

## Output Structure

The default `full_report` output view uses this fixed structure:

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
- Capture runtime settings and user hypotheses before source work.
- Treat user hypotheses as questions to test, not as evidence.
- Preserve source snapshots and run lineage for material claims.
- Use source partitions before loading long source text, then use evidence
  partitions after extraction.
- Use incremental refresh when only a subset of source material changed.
- Use one primary valuation method; other methods are sanity checks only.
- Build an explicit equity bridge before allowing a per-share target.
- Valuation must cover assets, orders/backlog, debt, cash, and dilution.
- Profit and cash-flow quality must cover OCF versus net income,
  EBITDA-to-OCF-to-FCF, working capital, capex quality, SBC-adjusted FCF, FCF
  per share, and diluted share count.
- Short-seller risk must cover customer/contract authenticity, revenue
  recognition, cash-flow quality, related parties, audit quality, insider
  behavior, equity financing, and regulatory risk.
- Technical analysis must output trend, pattern, support/resistance, entry, stop
  loss, and take-profit levels.
- Decision scorecard grading must use qualitative action grades with a binding
  cap reason rather than numeric score averaging.
- Each analysis layer must make a judgment: business transition, operating ramp,
  order-to-revenue path, funding bridge, valuation re-rating condition,
  short-risk falsification lens, and trim/add trade logic.

## Reference Files

- `references/business-model-framework.md`
- `references/valuation-framework.md`
- `references/profit-cash-flow-quality-framework.md`
- `references/short-seller-risk-framework.md`
- `references/technical-analysis-framework.md`
- `references/scorecard-decision-framework.md`
- `references/report-style-patterns.md`
- `references/research-lakehouse-framework.md`
- `references/evidence-indexing-framework.md`
- `references/incremental-refresh-framework.md`
- `references/user-intake-settings-framework.md`
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
`ResearchSettings`, `UserHypothesis`, `SourceSnapshot`, `SourcePartition`,
`EvidencePartition`, `ResearchRun`, `ActionExecution`, `GateResult`,
`OutputView`, `IncrementalRefreshPlan`, `EquityBridge`, and
`ConflictResolution`.

Additional decision objects support profit/cash-flow quality and final action
grading: `ProfitCashFlowQualityAnalysis`, `ExpectationRevisionAssessment`,
`MomentumRegimeAssessment`, `ValuationOddsAssessment`, `RiskFilterAssessment`,
and `DecisionScorecard`.

Gate results use `pass`, `warn`, `block`, `fail`, or `not_applicable`.

## Calibration Method

The current Skill was calibrated with a fresh public-company test outside the
prior reference-report set. The temporary company name, ticker, and generated
draft are intentionally not committed, because company-specific cases must not
become runtime triggers.

The comparison found gaps in six areas:

- valuation needed a current-market-implied expectation before the analyst
  target
- orders needed a quality ladder for cases where formal backlog is absent
- financial quality needed net-income-to-operating-cash-flow reconciliation
- technical analysis needed chart-date freshness and adjusted-OHLCV controls
- trade planning needed an explicit decision scorecard and action-grade cap
- layer depth needed stronger links between structural thesis, operating proof,
  cash funding, valuation re-rating, and executable trade management

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
- [OpenClaw skills documentation](https://docs.openclaw.ai/tools/skills)
- [User-provided ChatGPT Pro design discussion](https://chatgpt.com/share/6a1779ca-13b0-83eb-a9f0-157203a052f1)

License notes are documented in
`references/external-inspirations-and-license-notes.md`.

## Skill Health And Maintenance

The maintenance contract is explicit and separate from normal report
generation:

- `skill_manifest.json` declares the Skill id, GitHub repository, branch,
  entrypoint, health commands, and post-update commands.
- `requirements.txt` records validation dependencies.
- `scripts/skill_maintenance.py` provides read-only doctor checks, dry-run
  update previews, explicit update execution, and proposal-only maintenance
  planning.
- `.github/workflows/skill-health.yml` runs the doctor and dry-run preview in
  CI with read-only repository permissions.

Commands:

```bash
python3 scripts/skill_maintenance.py doctor --json
python3 scripts/skill_maintenance.py update --dry-run --json
python3 scripts/skill_maintenance.py proposal --json
```

`python3 scripts/skill_maintenance.py update --yes` is reserved for explicit
update requests. It creates a backup, attempts a fast-forward-only update, runs
the manifest health commands, and rolls back if health checks fail.

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

To check settings and the optional research manifest contract:

```bash
python3 scripts/validate_settings.py
python3 scripts/validate_research_manifest.py evals/fixtures/report-contract-fixture.manifest.json
python3 scripts/validate_report_against_manifest.py evals/fixtures/report-contract-fixture.md evals/fixtures/report-contract-fixture.manifest.json
python3 scripts/skill_maintenance.py doctor --json
```

The repository includes `evals/fixtures/report-contract-fixture.md` as a
minimal report contract fixture for CI and
`evals/fixtures/report-contract-fixture.manifest.json` as the matching object
manifest fixture.

The validator checks:

- Skill metadata
- reference links
- eval case metadata
- required report structure
- removal of old orchestration dependencies
- absence of baked-in company names or ticker-based prompts
- English-only repository text for Skill and GitHub-facing files
- ontology object, link, action, function, and gate contracts
- settings schema and onboarding flow contracts
- manifest lineage and report-manifest consistency
- Skill maintenance manifest, doctor, dry-run update, and CI health contracts
- quality-loop contracts for source markers, implied valuation, order quality,
  cash conversion, short risk, and technical freshness

## License

MIT
