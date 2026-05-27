# Ontology Framework

This reference turns the report Skill into an ontology-driven research workflow.
The report is the final view. The source of truth is an object graph of
evidence, claims, metrics, orders, assets, debt, valuation cases, short-risk
signals, profit/cash-flow quality, decision scorecards, technical setups, data
gaps, and report sections.

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

Research objects move through the research lakehouse described in
`references/research-lakehouse-framework.md`: Bronze source snapshots, Source
Index partitions, Silver validated evidence, Gold analysis products, and Report
View projections.

Minimum object layer:

- `ResearchSettings`
- `UserHypothesis`
- `ResearchRun`
- `Company`
- `Security`
- `SourceDocument`
- `SourceSnapshot`
- `SourcePartition`
- `EvidencePartition`
- `EvidenceItem`
- `Claim`
- `ConflictResolution`
- `MetricObservation`
- `ContractOrder`
- `OrderQualityAssessment`
- `AssetFacility`
- `DebtInstrument`
- `DilutionInstrument`
- `FinancialQualityAssessment`
- `ProfitCashFlowQualityAnalysis`
- `CurrentMarketImpliedBridge`
- `ValuationMethodSelection`
- `EquityBridge`
- `ValuationCase`
- `ShortRiskSignal`
- `ShortSellerAssessment`
- `TechnicalSetup`
- `ExpectationRevisionAssessment`
- `MomentumRegimeAssessment`
- `ValuationOddsAssessment`
- `RiskFilterAssessment`
- `DecisionScorecard`
- `TradePlan`
- `IncrementalRefreshPlan`
- `ActionExecution`
- `GateResult`
- `OutputView`
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

- `ResearchSettings -> configures_run -> ResearchRun`
- `UserHypothesis -> tests_hypothesis -> Claim`
- `SourceDocument -> contains -> EvidenceItem`
- `SourcePartition -> partitions_source -> SourceSnapshot`
- `SourcePartition -> routes_to_evidence -> EvidenceItem`
- `EvidenceItem -> derives_from -> SourceSnapshot`
- `EvidenceItem -> supports -> Claim`
- `EvidenceItem -> contradicts -> Claim`
- `EvidenceItem -> invalidates -> Claim`
- `EvidencePartition -> pruned_by_partition -> EvidenceItem`
- `Claim -> feeds -> BusinessModelThesis`
- `ContractOrder -> supports -> ValuationCase`
- `OrderQualityAssessment -> constrains -> ValuationCase`
- `DebtInstrument -> affects_equity_bridge -> EquityBridge`
- `DilutionInstrument -> affects_target_price -> EquityBridge`
- `EquityBridge -> bridges_to_target_price -> ValuationCase`
- `ProfitCashFlowQualityAnalysis -> cash_quality_supports_valuation -> ValuationCase`
- `ProfitCashFlowQualityAnalysis -> cash_quality_flags_short_risk -> ShortRiskSignal`
- `ShortRiskSignal -> discounts -> ValuationCase`
- `TechnicalSetup -> constrains -> TradePlan`
- `ExpectationRevisionAssessment -> expectation_feeds_scorecard -> DecisionScorecard`
- `MomentumRegimeAssessment -> momentum_feeds_scorecard -> DecisionScorecard`
- `ValuationOddsAssessment -> valuation_odds_feeds_scorecard -> DecisionScorecard`
- `RiskFilterAssessment -> risk_filter_feeds_scorecard -> DecisionScorecard`
- `DecisionScorecard -> scorecard_constrains_trade -> TradePlan`
- `ValuationCase -> valuation_constrains_trade -> TradePlan`
- `ShortSellerAssessment -> short_risk_constrains_trade -> TradePlan`
- `DataGap -> blocks -> Claim`
- `IncrementalRefreshPlan -> refreshed_by -> ActionExecution`
- `ResearchRun -> executes -> ActionExecution`
- `ActionExecution -> records_gate_result -> GateResult`
- `OutputView -> projects_view -> ReportSection`
- `ReportSection -> cites -> EvidenceItem`

The link verbs matter. They force the agent to distinguish evidence, causality,
valuation effects, blockers, and final report citations.

## Action Standard

Use actions as workflow transactions:

- `CaptureResearchSettings`
- `StartResearchRun`
- `AttachSourceDocument`
- `BuildSourcePartitions`
- `BuildEvidencePartitions`
- `ExtractEvidence`
- `NormalizeOperatingObjects`
- `ClassifyClaim`
- `ResolveConflictingFacts`
- `BuildBusinessModelThesis`
- `DetectSourceChange`
- `IncrementalRefresh`
- `GradeOrderQuality`
- `ReconcileFinancials`
- `AnalyzeProfitCashFlowQuality`
- `ReconcileShareCountAndEV`
- `InferCurrentMarketPricing`
- `SelectPrimaryValuationMethod`
- `BuildValuationCase`
- `BuildEquityBridge`
- `RunShortRiskScreen`
- `ValidateTechnicalSetup`
- `BuildDecisionScorecard`
- `BuildTradePlan`
- `GenerateReportSection`
- `SelectOutputView`
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
- cash-quality bridge
- working-capital cycle assessment
- SBC-adjusted FCF per share
- order-to-revenue bridge
- re-rating bridge
- funding bridge
- debt-safety score
- valuation-method selection
- target-price blocker detection
- explicit equity bridge calculation
- short-risk grade
- falsification lens
- decision scorecard construction
- action-grade cap determination
- technical freshness check
- position sizing from stop distance
- source conflict detection
- materiality classification
- material metric extraction
- gate-result classification
- output-view selection

Functions should return either a value, a grade, or a blocking data gap.

## Workflow Gates

Before report composition, pass these gates:

- Lakehouse Layer Gate: Bronze, Source Index, Silver, Gold, and Report View
  boundaries are respected
- Settings Gate: runtime settings are complete and user hypotheses are not
  treated as evidence
- Evidence Gate: material claims have evidence links
- Lineage Gate: material conclusions trace to source snapshots
- Partition Coverage Gate: relevant evidence partitions are available or
  blocked
- Source Priority Gate: conflicting facts follow the source-priority order
- Order Gate: order evidence is graded and weak order signals do not support
  valuation without conversion proof
- Financial Gate: net income, OCF, working capital, and cash conversion are
  reconciled
- Profit Cash Flow Quality Gate: OCF, EBITDA, FCF, capex, SBC, dilution, and
  owner FCF are reconciled or explicitly blocked
- Debt Gate: cash, debt, maturity, interest, dilution, and share count feed the
  equity bridge
- Equity Bridge Gate: target price is blocked unless EV, cash, senior claims,
  non-operating assets, and diluted shares reconcile
- Valuation Gate: current-market-implied expectation appears before the target
- Short Risk Gate: elevated short risk affects valuation or position sizing
- Technical Gate: chart date, adjusted status, entry, stop, and take-profit are
  supported or blocked
- Decision Scorecard Gate: action grade and binding cap reason are supported by
  underlying analysis objects
- Freshness Gate: stale objects cannot drive valuation or technical levels
- Incremental Refresh Gate: changed sources refresh dependent objects or trigger
  a full rerun
- Output View Gate: output view changes projection without changing the source
  graph
- Data Gap Gate: blocked conclusions are not forced into the report

Gate results use `pass`, `warn`, `block`, `fail`, or `not_applicable`. Store the
status, reason, affected objects, blocked conclusions, and required user input
in `GateResult` through `ActionExecution`.

## Report Projection

The final report sections should read from the object graph:

- `Company Overview`: `Company`, `Security`, current dispute, material claims
- `Business Model Logic`: business model claims and value-driver transition
- `Operations, Customers, And Orders`: counterparties, orders, capacity, order
  quality
- `Financials, Assets, And Debt`: metrics, assets, debt, dilution, financial
  quality, and profit/cash-flow quality
- `Valuation`: current-implied bridge, selected method, equity bridge,
  valuation cases
- `Short-Seller Risk`: short-risk signals and short-seller assessment
- `Technical Analysis`: technical setup and freshness gate
- `Risk Factors`: data gaps and high-risk claims
- `Trade Plan`: final trade plan constrained by valuation, risk, scorecard, and
  technical setup

Do not let a section own facts that are absent from the graph. Sections cite
evidence-backed claims.
