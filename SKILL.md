---
name: stock-research-report
description: >
  Self-contained ontology-backed public-company deep research report skill.
  Produces analyst style causal memos with outside thesis replay, opportunity
  archetype routing, business-model logic, profit and cash-flow quality,
  valuation with assets/orders/debt, short-seller risk, decision scorecard, and
  K-line technical trade planning. Uses authoritative sources first and treats
  outside articles or user-provided historical reports only as research-path,
  style, and structure inputs unless independently verified.
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

Produce one self-contained deep research report on a public company. The output
is not a generic company profile. It is a causal investment memo that starts with
what is being repriced now, identifies the scarce value-chain node, verifies
whether commercial evidence can convert into revenue and cash, then translates
that evidence into valuation, falsification, and an executable trade plan.

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
- `references/article-thesis-distillation-framework.md`
- `references/opportunity-discovery-framework.md`
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
   earnings-call transcripts, exchange/regulator records, customer/partner
   disclosures, and reliable market data before secondary research.
2. Outside articles are research-path hints, not evidence. Extract the thesis
   path, then verify each material claim independently.
3. Historical reports are not evidence. They teach style, section rhythm,
   causal depth, and trade-plan usefulness only.
4. Start with the current repricing dispute. Do not open with generic company
   history unless identity itself is the investment issue.
5. Every high-conviction thesis must test demand expansion, scaling difficulty,
   bottleneck or scarcity, and commercialization visibility.
6. No invented facts. If a needed data point is missing, state the missing item
   and block the affected conclusion.
7. One report, one voice. Do not expose separate module outputs.
8. One primary valuation method. Use other methods only as brief sanity checks;
   do not average methods into a target.
9. Assets, orders, cash, debt, maturity wall, dilution, and share count are
   mandatory in valuation.
10. Profit and cash-flow quality is mandatory. Reconcile earnings to OCF,
    EBITDA to OCF to FCF, FCF per share, working capital, capex quality, and
    dilution.
11. Short-seller risk is mandatory. Grade the risk and state how it affects
    valuation, position sizing, or confidence.
12. Technical analysis is decision-oriented. Output trend, pattern,
    support/resistance, entry, stop, and take-profit levels, or block the setup.
13. Decision scorecard is a projection, not evidence. It compresses supported
    analysis into an action grade and binding cap reason.
14. Use CFA-aligned formulas and method logic without copying textbook prose.
15. No third-party code copying. Public projects may inspire workflow design
    only; preserve links and license notes.
16. No baked-in company triggers. Never use prior report issuers, tickers, or
    temporary calibration targets as runtime conditions.
17. Material numbers need source markers. Revenue, cash, debt, backlog, share
    count, target price, and technical levels must be traceable or labeled as
    assumptions.
18. Runtime settings are not evidence. User settings and user hypotheses
    configure the run and must be tested against sources.
19. Ontology before prose. Build the object graph first; report sections are
    projections from evidence-backed claims.
20. Maintenance is explicit. Use `skill_manifest.json` and
    `scripts/skill_maintenance.py` for doctor checks, dry-run update previews,
    explicit updates, and proposal-only improvement planning. Do not silently
    update, rewrite, or push repository state from normal report generation.
21. The final report must pass an anti-checklist reconstruction pass. If a
    paragraph could fit most peers, rewrite it around the issuer control point,
    scarcity economics, commercial proof, cash conversion, or trade action.

## Workflow

### 1. Runtime Settings And Source Map

Use `references/user-intake-settings-framework.md`.

Capture `ResearchSettings`, `UserHypothesis`, and `OutputView`. Resolve issuer
identity, ticker, exchange, currency, fiscal year, reporting standard, current
market data, and industry archetype. Label every research statement as
`verified_fact`, `inference`, `scenario_assumption`, or `opinion`.

Use concise source markers such as `[filing]`, `[earnings call]`,
`[IR presentation]`, `[regulator]`, `[counterparty]`, or `[market data]`.

### 2. Research Path Replay And Opportunity Discovery

Use `references/opportunity-discovery-framework.md` and
`references/article-thesis-distillation-framework.md`.

Before building the final evidence graph, reconstruct why the issuer is worth
researching now:

- collect issuer filings, investor relations, transcripts, press releases,
  customer disclosures, supplier disclosures, regulator records, reliable market
  data, and high-quality outside research when available
- build `ArticleThesisMap` for each outside thesis path
- extract what each outside source believes, which causal chain it uses, what
  facts it relies on, which facts are missing, and what would falsify it
- build `ThesisPathReplay` to compare outside-in thesis discovery with
  inside-out primary-source reconstruction
- reject or qualify every outside claim that primary sources do not support

Do not copy article language. Use outside research only to discover candidate
paths and missing questions.

### 3. Thesis Kernel Construction

Before drafting, compress the research into one internal thesis kernel:

```text
repricing dispute -> demand shock -> scaling constraint -> scarce node
-> issuer control point -> commercial proof -> operating proof
-> cash proof -> current-market-implied expectation -> action cap
-> execution plan
```

This kernel is not normally shown as a section. It controls section order,
paragraph order, and the final action grade. Every section must advance the
kernel. If a section only lists facts, it has failed the memo standard.

### 4. Opportunity Archetype Routing

Classify the issuer before drafting:

- `scarcity_bottleneck`
- `policy_protected_supply_chain`
- `customer_funded_capacity_ramp`
- `operating_leverage_recovery`
- `order_backlog_repricing`
- `strategic_asset_optional_value`
- `levered_residual_equity`
- `early_commercialization`
- `mature_infrastructure_compounder`
- `commodity_or_resource_processing`

The archetype determines section emphasis, evidence burden, order quality
threshold, and valuation method. If no archetype is supported, mark the issuer
as industry beta or watchlist-only.

### 5. Research Lakehouse And Evidence Index

Use `references/research-lakehouse-framework.md`,
`references/evidence-indexing-framework.md`, and
`references/incremental-refresh-framework.md`.

Process evidence in layers:

- Bronze: immutable `SourceSnapshot` and `SourceDocument`
- Source Index: `SourcePartition` routing before extraction
- Silver: `EvidencePartition`, `EvidenceItem`, `Claim`, metrics, orders, debt,
  dilution, and conflict records
- Gold: opportunity thesis, scarcity assessment, commercialization path,
  business thesis, financial quality, valuation, short-risk, technical setup,
  scorecard, and trade plan
- Report View: final `ReportSection` projections

Use partitions to avoid loading irrelevant source text. If new source material
arrives, build an `IncrementalRefreshPlan` and refresh only affected objects
unless a high-materiality claim is invalidated.

### 6. Ontology Object Graph

Use `references/ontology-framework.md` and the YAML contracts in `ontology/`.

Minimum graph path:

```text
SourceDocument -> EvidenceItem -> Claim -> analysis object -> ReportSection
```

Required analysis objects include:

- `ResearchSettings`, `UserHypothesis`, `ArticleThesisMap`, `ThesisPathReplay`
- `OpportunityArchetype`, `DemandExpansionAssessment`,
  `ScalingDifficultyAssessment`, `ScarcityBottleneckAssessment`,
  `CommercializationPathAssessment`
- `BusinessModelThesis`, `ValueDriverTransition`, `OrderQualityAssessment`,
  `OperatingLeverageMap`
- `FinancialQualityAssessment`, `ProfitCashFlowQualityAnalysis`
- `CurrentMarketImpliedBridge`, `ValuationMethodSelection`, `EquityBridge`,
  `ValuationCase`
- `ShortRiskSignal`, `ShortSellerAssessment`, `FalsificationPattern`
- `TechnicalSetup`, `PositionSizingRationale`
- `ExpectationRevisionAssessment`, `MomentumRegimeAssessment`,
  `ValuationOddsAssessment`, `RiskFilterAssessment`, `DecisionScorecard`
- `TradePlan`, `GateResult`, `DataGap`, `ReportSection`

Run all workflow gates before final prose. Each gate result must be `pass`,
`warn`, `block`, `fail`, or `not_applicable`.

### 7. Four-Part Opportunity Test

Every high-conviction report must pass or explicitly block this sequence:

1. Demand expansion:
   - name the end demand
   - identify who is spending
   - explain why demand is growing now
   - separate structural demand from cyclical rebound
   - determine whether exposure is direct or merely thematic

2. Scaling difficulty:
   - explain why supply cannot expand easily
   - identify qualification, certification, capex, construction time, yield,
     customer approval, regulation, financing, or supply-chain barriers
   - state what would prove replication is easier than the thesis assumes

3. Bottleneck or scarcity:
   - identify the exact value-chain node
   - explain why this company controls or benefits from that node
   - classify scarcity as technical, capacity, qualification, policy,
     customer-relationship, asset, financing, or channel scarcity
   - determine whether scarcity is temporary, cyclical, or structural
   - map scarcity to economics: pricing, utilization, customer funding, gross
     margin, cash conversion, or downside floor

4. Commercialization visibility:
   - separate recognized revenue, binding purchase order, firm backlog, paid
     reservation, customer-funded capacity, contract, IDIQ/framework, pilot,
     MOU, LOI, pipeline, and management aspiration
   - state which evidence can support the base case and which belongs only in
     upside optionality

If any of the four parts fails, cap the final action grade unless valuation is
already priced as a discounted option.

### 8. Business Logic Build

Use `references/business-model-framework.md`.

Build the business logic as:

```text
demand shock -> industry bottleneck -> customer pain -> company solution
-> value capture -> revenue denominator -> margin mechanism
-> cash-flow pattern -> valuation denominator -> falsification observable
```

The section must identify old driver, new driver, why the transition is
happening now, how the company captures value, what evidence proves the
transition is real, and what evidence would break it.

Industry context is allowed only when it explains the bottleneck or control
point. The business section must close with a bold one-sentence judgment naming
the value driver, current stage, and key observable.

### 9. Commercialization And Order Quality

Use `references/business-model-framework.md` and
`references/valuation-framework.md`.

Separate:

- recognized revenue
- binding purchase order
- contracted backlog
- paid capacity reservation
- customer prepayment
- commercial contract
- IDIQ or framework
- pilot
- MOU
- LOI
- pipeline
- management aspiration

Only recognized revenue, binding purchase orders, contracted backlog, paid
reservations, or customer-funded capacity can normally support base-case
valuation. Weaker order types may support upside optionality only.

For every order-heavy thesis, build:

```text
order evidence -> customer identity -> legal strength -> delivery cadence
-> capacity match -> margin visibility -> working-capital burden
-> cash conversion -> valuation usability
```

### 10. Operations, Capacity, And Execution Quality

Use `references/opportunity-discovery-framework.md` and
`references/business-model-framework.md`.

Tie asset, facility, production, capacity, utilization, capex, and ramp timing
to the opportunity archetype. For asset-heavy or capacity-ramp theses, show the
current capacity, target capacity, funding source, bottleneck, and date by which
failure would become visible.

The operations section must answer whether the issuer can deliver the demand it
claims, not merely whether management has announced an expansion plan.

### 11. Profit Cash Flow Quality Analysis

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

Embed conclusions in `Financial Quality, Assets, Debt, And Dilution`,
`Valuation And Market-Implied Expectation`, `Catalysts, Risks, And
Falsification`, and `Technical Structure And Trade Plan`. Do not add a separate
report section.

### 12. Valuation With Assets, Orders, And Debt

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

### 13. Short-Seller Risk

Use `references/short-seller-risk-framework.md`.

Assess customer/contract authenticity, related parties, revenue recognition,
cash-flow quality, receivables, inventory, auditor changes, insider behavior,
dilution, promotion versus execution, regulatory/legal risk, and market short
signals where reliable data exists.

Output a grade `A/B/C/D/F`, the activist-short attack narrative, strongest red
and green flags, and valuation or position-size effect. Keep verified facts,
allegations, inferences, and unanswered questions separate.

### 14. Technical Analysis And Trade Plan Inputs

Use `references/technical-analysis-framework.md`.

Use fresh daily, weekly, and monthly OHLCV data or reliable chart screenshots.
State chart date and adjusted/unadjusted status. Output monthly trend, weekly
trend, daily trend, pattern, volume confirmation, support, resistance, entry,
stop, TP1, TP2, and whether the chart confirms or contradicts the fundamental
thesis.

If no defensible setup exists, state the observation stance and the price or
catalyst that would change it.

### 15. Decision Scorecard

Use `references/scorecard-decision-framework.md`.

Build `DecisionScorecard` after valuation, short-risk, and technical setup. The
scorecard must summarize company quality, operating trend, expectation
revision, growth logic, momentum state, valuation odds, risk filter, final
action grade, and binding cap reason.

Do not use numeric score averaging. The grade is capped by the weakest
decision-critical blocker, such as unresolved evidence, stretched valuation,
negative revision risk, weak cash conversion, elevated short risk, or
overextended momentum.

### 16. Quality Calibration Loop

Use `references/quality-calibration-loop.md` before finalizing substantial
reports or when improving this Skill.

Compare the draft against the reference-caliber quality bar: opening tension,
business causal chain, order quality, cash conversion, current-implied
valuation, per-share bridge, short-risk effect, technical freshness, scorecard
discipline, and final trade usefulness. Fix data gaps, reasoning gaps,
structure gaps, or validation gaps until no actionable gap remains.

Run the anti-checklist reconstruction pass: remove peer-generic paragraphs,
convert weak order language into an order-quality level, convert operating
claims into capacity and failure signals, convert risk into valuation or size
impact, and convert technical commentary into action or a blocked setup.

Do not commit temporary issuer names, tickers, or generated reports as triggers
or reusable prompts.

### 17. Skill Health And Maintenance

Use `skill_manifest.json` as the repository contract for Skill identity,
entrypoint, branch, health commands, and post-update commands.

Use `scripts/skill_maintenance.py doctor --json` for read-only health checks.
Use `scripts/skill_maintenance.py update --dry-run --json` to preview remote
update state. Use `scripts/skill_maintenance.py update --yes` only when the user
explicitly requests an update; it must create a backup, use a fast-forward-only
update, run validation, and roll back on failed health checks. Use
`scripts/skill_maintenance.py proposal` to produce maintenance proposals without
changing files.

Maintenance logic is operational support. It must not change the report
contract, evidence hierarchy, ontology graph, or English-only repository rule
without corresponding documentation and validation updates.

### 18. Final Report Composition

The default `full_report` output view must use this mainline-driven structure:

```markdown
# [Company Name] ([Ticker]) Deep Research Report:
## [One-line thesis subtitle]

## Core Conclusion
## Why This Stock Exists Now
## Industry Chain And Bottleneck
## Company Position In The Chain
## Business Model Logic
## Scarcity And Moat Assessment
## Customers, Orders, And Commercialization Path
## Operations, Capacity, And Execution Quality
## Financial Quality, Assets, Debt, And Dilution
## Valuation And Market-Implied Expectation
## Catalysts, Risks, And Falsification
## Technical Structure And Trade Plan
```

Section requirements:

- `Core Conclusion`: current repricing dispute, action stance, position-size
  logic, main upside variable, main invalidation variable, and action-grade cap.
- `Why This Stock Exists Now`: demand expansion, market attention trigger, what
  changed versus the prior 6-12 months, and whether the move is structural or
  cyclical.
- `Industry Chain And Bottleneck`: compact industry primer only when needed,
  industry pain, insufficient alternatives, scarce value-chain node, and
  scarcity duration.
- `Company Position In The Chain`: what the company sells, who pays, why they
  pay, which cost or risk is avoided, and whether the stock is industry beta or
  company alpha.
- `Business Model Logic`: old driver, new driver, value capture, bottleneck,
  and verification variable.
- `Scarcity And Moat Assessment`: technical, capacity, certification,
  customer-relationship, policy, switching-cost, and replication-difficulty
  evidence.
- `Customers, Orders, And Commercialization Path`: revenue, binding demand,
  backlog, paid reservations, frameworks, pilots, delivery cadence, customer
  funding, working-capital burden, and order-to-revenue bridge.
- `Operations, Capacity, And Execution Quality`: facilities, assets, capacity,
  utilization, expansion plan, capex source, ramp date, bottleneck, and margin
  at scale.
- `Financial Quality, Assets, Debt, And Dilution`: revenue and margin trend,
  cash, debt, maturities, dilution, OCF, EBITDA-to-OCF-to-FCF bridge, working
  capital, capex quality, SBC-adjusted FCF, FCF per share, and cash runway.
- `Valuation And Market-Implied Expectation`: current-market-implied
  expectation, one primary method, inline arithmetic, EV-to-equity-to-diluted
  share bridge, base/bull/bear cases, re-rating condition, downside floor, and
  one sanity check.
- `Catalysts, Risks, And Falsification`: 3-6 month catalysts, 12-24 month
  catalysts, thesis-breaking risks, short-seller attack narrative, and evidence
  that would prove the thesis wrong.
- `Technical Structure And Trade Plan`: monthly trend, weekly trend, daily
  trend, pattern, volume, entry, stop, TP1, TP2, add/trim logic, position size,
  action grade, binding cap reason, catalyst, and invalidation.

Legacy aliases such as `Company Overview`, `Operations, Customers, And Orders`,
`Financials, Assets, And Debt`, `Valuation`, `Short-Seller Risk`, `Technical
Analysis`, `Risk Factors`, and `Trade Plan` may be recognized when validating
older fixtures, but new `full_report` outputs should use the mainline-driven
structure above.

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
- customer concentration is material but unsupported by filings or counterparty
  sources
- current chart data is unavailable for technical levels
- cash-flow statement, capex, or SBC data is missing when owner FCF is central

When blocked, complete the sections that can be supported and mark the blocked
conclusion precisely.

## Pre-Final Self-Check

Before final output, verify:

- all twelve mainline sections are present unless the selected `OutputView`
  intentionally uses a shorter projection
- the thesis kernel is clear before prose begins
- the current repricing dispute appears before corporate background
- every outside thesis path is verified, rejected, or blocked before use
- the issuer is routed to an opportunity archetype or capped as industry beta
- demand expansion, scaling difficulty, bottleneck/scarcity, and
  commercialization visibility are passed or explicitly blocked
- ontology gates have passed or produced explicit blocked conclusions
- every layer contains a judgment, not only a description
- high-materiality claims have evidence, contradiction, qualification, or a
  data-gap blocker
- material numbers have source markers or are labeled assumptions
- business logic explains value capture rather than industry growth alone
- industry context explains the bottleneck and does not become generic filler
- operations connect capacity, utilization, customer funding, and revenue
  conversion
- order claims are mapped to order-quality level and valuation usability
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