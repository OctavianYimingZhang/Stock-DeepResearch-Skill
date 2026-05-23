# Ontology Framework

This reference turns the report Skill into an ontology-driven research workflow.
The report is the final view. The source of truth is an object graph of
evidence, claims, metrics, orders, assets, debt, valuation cases, short-risk
signals, technical setups, data gaps, and report sections.

## Design Principle

Do not model the report outline as the core system. Model the real research
objects first, then project them into the fixed report sections.

The central object is the evidence-backed `Claim`. A claim can be a verified
fact, inference, scenario assumption, or opinion. Material claims must be linked
to evidence before they can support valuation, risk, technical levels, or final
trade recommendations.

## Core Object Graph

Use the lightweight ontology files in `ontology/`:

- `ontology/object_types.yaml`
- `ontology/link_types.yaml`
- `ontology/action_types.yaml`
- `ontology/functions.yaml`
- `ontology/workflow_gates.yaml`

Minimum object layer:

- `Company`
- `Security`
- `SourceDocument`
- `EvidenceItem`
- `Claim`
- `MetricObservation`
- `ContractOrder`
- `OrderQualityAssessment`
- `AssetFacility`
- `DebtInstrument`
- `DilutionInstrument`
- `FinancialQualityAssessment`
- `CurrentMarketImpliedBridge`
- `ValuationMethodSelection`
- `ValuationCase`
- `ShortRiskSignal`
- `ShortSellerAssessment`
- `TechnicalSetup`
- `TradePlan`
- `DataGap`
- `Report`
- `ReportSection`

## Claim Standard

Every material claim needs:

- `claim_text`
- `claim_type`
- `evidence_status`
- `source_strength`
- `materiality`
- `freshness_status`
- `confidence`
- `blocked_by_data_gap`

If `materiality` is `high`, at least one `EvidenceItem` must support or
contradict the claim before it can be used in a report section. Unsupported
high-materiality claims become `DataGap` objects.

## Link Standard

The most important links are:

- `SourceDocument -> contains -> EvidenceItem`
- `EvidenceItem -> supports -> Claim`
- `EvidenceItem -> contradicts -> Claim`
- `Claim -> feeds -> BusinessModelThesis`
- `ContractOrder -> supports -> ValuationCase`
- `OrderQualityAssessment -> constrains -> ValuationCase`
- `DebtInstrument -> affects -> EquityBridge`
- `DilutionInstrument -> affects -> TargetPrice`
- `ShortRiskSignal -> discounts -> ValuationCase`
- `TechnicalSetup -> constrains -> TradePlan`
- `DataGap -> blocks -> Claim`
- `ReportSection -> cites -> EvidenceItem`

The link verbs matter. They force the agent to distinguish evidence, causality,
valuation effects, blockers, and final report citations.

## Action Standard

Use actions as workflow transactions:

- `StartResearchRun`
- `AttachSourceDocument`
- `ExtractEvidence`
- `ClassifyClaim`
- `ResolveConflictingFacts`
- `GradeOrderQuality`
- `ReconcileFinancials`
- `ReconcileShareCountAndEV`
- `InferCurrentMarketPricing`
- `SelectPrimaryValuationMethod`
- `BuildValuationCase`
- `RunShortRiskScreen`
- `ValidateTechnicalSetup`
- `GenerateReportSection`
- `FinalizeReport`

Each action reads defined object types and writes defined object types. This
prevents a report from being produced directly from unstructured source text.

## Function Standard

Calculations and repeatable decisions belong in functions:

- enterprise value
- FCFF and FCFE
- risk-adjusted backlog value
- order-quality grade
- cash-conversion score
- debt-safety score
- valuation-method selection
- target-price blocker detection
- short-risk grade
- technical freshness check
- position sizing from stop distance

Functions should return either a value, a grade, or a blocking data gap.

## Workflow Gates

Before report composition, pass these gates:

- Evidence Gate: material claims have evidence links
- Source Priority Gate: conflicting facts follow the source-priority order
- Order Gate: order evidence is graded and weak order signals do not support
  valuation without conversion proof
- Financial Gate: net income, OCF, working capital, and cash conversion are
  reconciled
- Debt Gate: cash, debt, maturity, interest, dilution, and share count feed the
  equity bridge
- Valuation Gate: current-market-implied expectation appears before the target
- Short Risk Gate: elevated short risk affects valuation or position sizing
- Technical Gate: chart date, adjusted status, entry, stop, and take-profit are
  supported or blocked
- Data Gap Gate: blocked conclusions are not forced into the report

## Report Projection

The final report sections should read from the object graph:

- `Company Overview`: `Company`, `Security`, current dispute, material claims
- `Business Model Logic`: business model claims and value-driver transition
- `Operations, Customers, And Orders`: counterparties, orders, capacity, order
  quality
- `Financials, Assets, And Debt`: metrics, assets, debt, dilution, financial
  quality
- `Valuation`: current-implied bridge, selected method, valuation cases, equity
  bridge
- `Short-Seller Risk`: short-risk signals and short-seller assessment
- `Technical Analysis`: technical setup and freshness gate
- `Risk Factors`: data gaps and high-risk claims
- `Trade Plan`: final trade plan constrained by valuation, risk, and technical
  setup

Do not let a section own facts that are absent from the graph. Sections cite
evidence-backed claims.
