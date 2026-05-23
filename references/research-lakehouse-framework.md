# Research Lakehouse Framework

This reference adapts lakehouse-style data quality layering to equity research.
The goal is to prevent raw source text from flowing directly into a high-
conviction report.

## Layer Model

Use four layers:

| Layer | Purpose | Objects |
|---|---|---|
| Bronze | Preserve raw source fidelity | `SourceSnapshot`, `SourceDocument`, raw filing, transcript, presentation, regulator record, OHLCV, screenshot |
| Silver | Clean and validate extracted evidence | `EvidenceItem`, `Claim`, `MetricObservation`, `ContractOrder`, `DebtInstrument`, `DilutionInstrument` |
| Gold | Analysis-ready research products | `BusinessModelThesis`, `CurrentMarketImpliedBridge`, `ValuationCase`, `ShortSellerAssessment`, `TechnicalSetup`, `TradePlan` |
| Report View | Final user-facing projection | `Report`, `ReportSection` |

## Layer Rules

- Report View reads Gold objects and cited evidence only.
- Gold reads Silver and must preserve links to the Silver objects used.
- Silver reads Bronze and must preserve source snapshot lineage.
- Bronze is never rewritten. If a source changes, create a new snapshot.
- A high-conviction conclusion cannot skip layers.

## Source Snapshot Standard

Each source used in a research run needs a `SourceSnapshot`:

- retrieval date
- document date
- source locator
- content hash or explicit hash gap
- version label or explicit version gap
- source freshness status

This allows later report review to answer which source version supported a
claim, valuation bridge, short-risk signal, technical level, or trade plan.

## Research Run Ledger

Each report generation or update creates a `ResearchRun`:

- input sources
- changed sources
- executed actions
- failed gates
- blocked conclusions
- output report id

The run ledger is the audit trail. Do not treat the final prose as the audit
trail.

## Data Quality Expectations

Every workflow gate should return one of three outcomes:

- `warn`: allowed into report with low-conviction caveat
- `block`: conclusion cannot be made until a source or object is supplied
- `fail`: report contract is violated and must be fixed before final output

Typical `fail` outcomes:

- high-materiality claim lacks evidence
- material number lacks source marker or date
- target price appears while share count or net debt is unresolved
- weak order signal drives valuation
- chart date is missing for technical levels
- valuation method averaging appears

Typical `block` outcomes:

- source conflict exists and source priority cannot resolve it
- debt maturity schedule is missing for a levered company
- current OHLCV is unavailable for a requested trade plan

Typical `warn` outcomes:

- weak order signal is discussed but not used for target value
- secondary source is used only to frame context
- non-critical source freshness is imperfect but does not drive valuation

## Report Implication

The report should say less when the data layer is weak. A clean lakehouse flow
is more important than a longer report.
