---
name: stock-research-report
description: >
  Self-contained ontology-backed public-company deep research report skill.
  Produces analyst style reports with integrated business-model logic, profit
  and cash-flow quality, valuation with assets/orders/debt, short-seller risk,
  decision scorecard, and K-line technical trade planning. Uses authoritative
  sources first and treats user-provided historical reports only as style and
  structure patterns, never as factual evidence.
homepage: https://github.com/OctavianYimingZhang/Stock-DeepResearch-Skill
user-invocable: true
metadata: {"settings_schema":"config/settings.schema.json","onboarding_flow":"config/onboarding.flow.yaml","default_profile":"config/profiles/default.json"}
triggers:
  - stock research report
  - deep dive report
  - analyst report
  - equity research
  - public company analysis
  - stock deep research
---

# Stock Research Report

## Purpose

Produce one self-contained deep research report on a public company. This Skill
does not dispatch the former standalone research, valuation, short-risk, or
technical-analysis Skills at runtime. It consolidates their useful methods into
one evidence-backed report system.

Historical user reports are style and depth references only. They are never
factual evidence for a new issuer unless the same claim is independently
verified from primary or high-quality current sources.

## Required Reference Files

Read these files before writing a full report or changing the Skill contract:

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

Use the YAML and JSON contracts in `ontology/`, `config/`, and `evals/` as the
machine-readable version of the workflow.

## Non-Negotiable Rules

1. Evidence before thesis. Use filings, issuer investor relations,
   earnings-call transcripts, exchange/regulator/government records,
   customer/partner disclosures, and reliable market data before secondary
   research.
2. Historical reports are not evidence. They teach style, section rhythm, and
   depth only.
3. No invented facts. If a needed data point is missing, state the missing item
   and block the affected conclusion.
4. One report, one voice. Do not expose separate module outputs.
5. One primary valuation method. Use other methods only as brief sanity checks;
   do not average methods into a target.
6. Assets, orders, cash, debt, maturity wall, dilution, and share count are
   mandatory in valuation.
7. Profit and cash-flow quality is mandatory. Reconcile earnings to OCF, EBITDA
   to OCF to FCF, FCF per share, working capital, capex quality, and dilution.
8. Short-seller risk is mandatory. Grade the risk and state how it affects
   valuation, position sizing, or confidence.
9. Technical analysis is decision-oriented. Output trend, pattern,
   support/resistance, entry, stop, and take-profit levels, or block the setup.
10. Decision scorecard is a projection, not evidence. It compresses supported
    analysis into an action grade and binding cap reason.
11. Use CFA-aligned formulas and method logic without copying textbook prose.
12. No third-party code copying. Public projects may inspire workflow design
    only; preserve links and license notes.
13. No baked-in company triggers. Never use prior report issuers, tickers, or
    temporary calibration targets as runtime conditions.
14. Material numbers need source markers. Revenue, cash, debt, backlog, share
    count, target price, and technical levels must be traceable or labeled as
    assumptions.
15. Runtime settings are not evidence. User settings and user hypotheses
    configure the run and must be tested against sources.
16. Ontology before prose. Build the object graph first; report sections are
    projections from evidence-backed claims.
17. Maintenance is explicit. Use `skill_manifest.json` and
    `scripts/skill_maintenance.py` for doctor checks, dry-run update previews,
    explicit updates, and proposal-only improvement planning. Do not silently
    update, rewrite, or push repository state from normal report generation.

## Workflow

### 1. Runtime Settings And Source Map

Use `references/user-intake-settings-framework.md`.

Capture `ResearchSettings`, `UserHypothesis`, and `OutputView`. Resolve issuer
identity, ticker, exchange, currency, fiscal year, reporting standard, current
market data, and industry archetype. Label every research statement as
`verified_fact`, `inference`, `scenario_assumption`, or `opinion`.

Use concise source markers such as `[filing]`, `[earnings call]`,
`[IR presentation]`, `[regulator]`, `[counterparty]`, or `[market data]`.

### 2. Research Lakehouse And Evidence Index

Use `references/research-lakehouse-framework.md`,
`references/evidence-indexing-framework.md`, and
`references/incremental-refresh-framework.md`.

Process evidence in layers:

- Bronze: immutable `SourceSnapshot` and `SourceDocument`
- Source Index: `SourcePartition` routing before extraction
- Silver: `EvidencePartition`, `EvidenceItem`, `Claim`, metrics, orders, debt,
  and dilution
- Gold: business thesis, financial quality, valuation, short-risk, technical
  setup, scorecard, and trade plan
- Report View: final `ReportSection` projections

Use partitions to avoid loading irrelevant source text. If new source material
arrives, build an `IncrementalRefreshPlan` and refresh only affected objects
unless a high-materiality claim is invalidated.

### 3. Ontology Object Graph

Use `references/ontology-framework.md` and the YAML contracts in `ontology/`.

Minimum graph path:

```text
SourceDocument -> EvidenceItem -> Claim -> analysis object -> ReportSection
```

Required analysis objects include:

- `BusinessModelThesis`, `ValueDriverTransition`, `OrderQualityAssessment`
- `FinancialQualityAssessment`, `ProfitCashFlowQualityAnalysis`
- `CurrentMarketImpliedBridge`, `ValuationMethodSelection`, `EquityBridge`,
  `ValuationCase`
- `ShortRiskSignal`, `ShortSellerAssessment`
- `TechnicalSetup`
- `ExpectationRevisionAssessment`, `MomentumRegimeAssessment`,
  `ValuationOddsAssessment`, `RiskFilterAssessment`, `DecisionScorecard`
- `TradePlan`, `GateResult`, `DataGap`, `ReportSection`

Run all workflow gates before final prose, including ProfitCashFlowQualityGate
and DecisionScorecardGate. Each gate result must be `pass`, `warn`, `block`,
`fail`, or `not_applicable`.

### 4. Business Model Logic

Use `references/business-model-framework.md`.

Explain the industry-to-company bridge: structural bottleneck, customer pain,
company solution, value capture, revenue denominator, margin mechanism, and
falsification observable. End the section with a bold one-sentence judgment
naming the value driver, current stage, and key observable.

### 5. Operations, Customers, And Orders

Use `references/business-model-framework.md` and
`references/valuation-framework.md`.

Separate recognized revenue, firm backlog, purchase orders, capacity
reservations, framework agreements, customer concentration, pipeline language,
and management guidance. Grade order quality before any order-based valuation
use. Tie orders to delivery cadence, capacity match, margin visibility,
working-capital burden, and customer funding. Weak order signals can support a
narrative but cannot drive a target.

### 6. Profit Cash Flow Quality Analysis

Use `references/profit-cash-flow-quality-framework.md`.

Build `ProfitCashFlowQualityAnalysis` before valuation and short-risk scoring.
Cover:

- OCF / net income and cumulative cash conversion
- EBITDA -> OCF -> FCF bridge
- FCF margin, FCF conversion, and FCF sustainability
- DSO, DIO, DPO, inventory, receivables, and working-capital cycle
- capex / D&A and maintenance versus growth capex
- stock-based compensation, SBC-adjusted FCF, FCF per share, and diluted shares
- Rule of 40 applicability, with `not_applicable` when the business model does
  not fit the metric

Embed conclusions in `Financials, Assets, And Debt`, `Valuation`,
`Short-Seller Risk`, and `Trade Plan`. Do not add a tenth report section.

### 7. Valuation With Assets, Orders, And Debt

Use `references/valuation-framework.md`.

First infer the current-market-implied expectation. Then select one primary
method based on business economics and actual market pricing. Build an explicit
EV-to-equity-to-diluted-share bridge through `EquityBridge` before any per-share
target.

Required valuation outputs:

- current market cap and EV
- asset base and replacement/liquidation relevance
- backlog/order quality and conversion schedule
- cash, debt, maturity wall, interest burden, dilution, and share count
- profit-to-cash-flow quality and owner FCF
- primary method derivation with inline arithmetic
- bull/base/bear cases tied to concrete observables
- target price or target market cap, unless blocked by evidence gaps
- one secondary sanity check at most

### 8. Short-Seller Risk

Use `references/short-seller-risk-framework.md`.

Assess customer/contract authenticity, related parties, revenue recognition,
cash-flow quality, receivables, inventory, auditor changes, insider behavior,
dilution, promotion versus execution, regulatory/legal risk, and market short
signals where reliable data exists.

Output a grade `A/B/C/D/F`, the activist-short attack narrative, strongest red
and green flags, and valuation or position-size effect. Keep verified facts,
allegations, inferences, and unanswered questions separate.

### 9. Technical Analysis And Trade Plan Inputs

Use `references/technical-analysis-framework.md`.

Use fresh daily, weekly, and monthly OHLCV data or reliable chart screenshots.
State chart date and adjusted/unadjusted status. Output monthly trend, weekly
trend, daily trend, pattern, volume confirmation, support, resistance, entry,
stop, TP1, TP2, and whether the chart confirms or contradicts the fundamental
thesis.

If no defensible setup exists, state the observation stance and the price or
catalyst that would change it.

### 10. Decision Scorecard

Use `references/scorecard-decision-framework.md`.

Build `DecisionScorecard` after valuation, short-risk, and technical setup. The
scorecard must summarize company quality, operating trend, expectation
revision, growth logic, momentum state, valuation odds, risk filter, final
action grade, and binding cap reason.

Do not use numeric score averaging. The grade is capped by the weakest
decision-critical blocker, such as unresolved evidence, stretched valuation,
negative revision risk, weak cash conversion, elevated short risk, or
overextended momentum.

### 11. Quality Calibration Loop

Use `references/quality-calibration-loop.md` before finalizing substantial
reports or when improving this Skill.

Compare the draft against the reference-caliber quality bar: opening tension,
business causal chain, order quality, cash conversion, current-implied
valuation, per-share bridge, short-risk effect, technical freshness, scorecard
discipline, and final trade usefulness. Fix data gaps, reasoning gaps,
structure gaps, or validation gaps until no actionable gap remains.

Do not commit temporary issuer names, tickers, or generated reports as triggers
or reusable prompts.

### 12. Skill Health And Maintenance

Use `skill_manifest.json` as the repository contract for Skill identity,
entrypoint, branch, health commands, and post-update commands.

Use `scripts/skill_maintenance.py doctor --json` for read-only health checks.
Use `scripts/skill_maintenance.py update --dry-run --json` to preview remote
update state. Use `scripts/skill_maintenance.py update --yes` only when the
user explicitly requests an update; it must create a backup, use a
fast-forward-only update, run validation, and roll back on failed health checks.
Use `scripts/skill_maintenance.py proposal` to produce maintenance proposals
without changing files.

Maintenance logic is operational support. It must not change the report
contract, evidence hierarchy, ontology graph, or English-only repository rule
without corresponding documentation and validation updates.

### 13. Final Report Composition

The default `full_report` output view must use this fixed structure:

```markdown
# [Company Name] ([Ticker]) Deep Research Report:
## [One-line thesis subtitle]

## Company Overview
## Business Model Logic
## Operations, Customers, And Orders
## Financials, Assets, And Debt
## Valuation
## Short-Seller Risk
## Technical Analysis
## Risk Factors
## Trade Plan
```

Section requirements:

- `Company Overview`: current investment tension, company identity, and compact
  decision scorecard summary.
- `Business Model Logic`: old driver, new driver, value capture, bottleneck,
  and verification variable.
- `Operations, Customers, And Orders`: facilities, capacity, customers, order
  evidence, conversion cadence, and bottlenecks.
- `Financials, Assets, And Debt`: financial trend, assets, cash, debt,
  maturities, dilution, profit-to-cash-flow bridge, SBC-adjusted FCF, FCF per
  share, and embedded quality note.
- `Valuation`: one primary method, current-market-implied expectation, inline
  arithmetic, EV-to-equity-to-diluted-share bridge, and one sanity check.
- `Short-Seller Risk`: grade, attack narrative, fact/inference separation, and
  valuation or position-size effect.
- `Technical Analysis`: trend, pattern, freshness, support/resistance, entry,
  stop, TP1, and TP2.
- `Risk Factors`: thesis-breaking risks and blocked conclusions.
- `Trade Plan`: stance, action grade, binding cap reason, position size, entry,
  stop, take-profit, catalyst, and invalidation.

## Style Rules

- Use the language requested by the user for the final report.
- Keep repository and Skill files in English.
- Use the configured `OutputView`; change projection only, not the source graph.
- Use concrete numbers, dates, inline arithmetic, and source attribution.
- Prefer narrative paragraphs plus compact tables only where tables reduce
  ambiguity.
- Write defensible conviction. Confidence comes from evidence, not tone.
- Avoid generic filler, dashboard clutter, method averaging, and unsupported
  technical levels.

## Data Gaps

Ask for missing data only when the gap blocks a required conclusion and cannot
be filled from public sources. Common blockers:

- current diluted share count cannot be reconciled
- debt maturity schedule is missing for a levered company
- backlog is central to valuation but contract quality is undisclosed
- customer concentration is material but unsupported by filings or
  counterparty sources
- current chart data is unavailable for technical levels
- cash-flow statement, capex, or SBC data is missing when owner FCF is central

When blocked, complete the sections that can be supported and mark the blocked
conclusion precisely.

## Pre-Final Self-Check

Before final output, verify:

- all nine fixed sections are present
- ontology gates have passed or produced explicit blocked conclusions
- every layer contains a judgment, not only a description
- high-materiality claims have evidence, contradiction, qualification, or a
  data-gap blocker
- material numbers have source markers or are labeled assumptions
- business logic explains value capture rather than industry growth alone
- operations connect capacity, utilization, customer funding, and revenue
  conversion
- assets, orders/backlog, debt, maturity, dilution, and share count are covered
- profit and cash-flow quality reconciles OCF, EBITDA, FCF, SBC, capex,
  working capital, and FCF per share
- valuation uses one primary method and one secondary sanity check at most
- valuation explains current-implied expectation, re-rating bridge, and funding
  bridge when relevant
- the EV-to-equity-to-diluted-share bridge is complete or target value is
  blocked
- short-seller risk has a grade, attack narrative, red flags, and green flags
- short-seller risk includes a falsification lens for the main upside thesis
- technical analysis has fresh trend, pattern, levels, entry, stop, and TP
  levels, trim/add logic, or a clear observation stance
- decision scorecard has an action grade and binding cap reason
- final trade plan contains stance, catalyst, invalidation, and position sizing
