---
name: stock-research-report
description: >
  Self-contained ontology-backed public-company deep research report skill.
  Produces analyst style reports with four integrated pillars: business-model
  logic, valuation with assets/orders/debt, short-seller risk, and K-line
  technical trade planning. Uses authoritative sources first and treats
  user-provided historical reports only as style and structure patterns, never
  as factual evidence.
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
does not dispatch `Stock-Analysis-Skill`, `valuation-calculator`,
`short-seller-risk-analysis`, or `technical-analysis-patterns` at runtime. It
absorbs the useful workflows from those Skills into one report system.

The required output should match the recurring quality patterns in the user's
prior deep-research reports. Those reports are style references only. Do not
reuse their factual claims for a new company unless the same claim is verified
from primary or high-quality current sources.

## Required Reference Files

Read these files before writing the report:

- `references/business-model-framework.md`
- `references/valuation-framework.md`
- `references/short-seller-risk-framework.md`
- `references/technical-analysis-framework.md`
- `references/report-style-patterns.md`
- `references/ontology-framework.md`
- `references/quality-calibration-loop.md`
- `references/external-inspirations-and-license-notes.md`

## Non-Negotiable Rules

1. **Evidence before thesis.** Use issuer filings, issuer investor relations,
   earnings-call transcripts, exchange/regulator/government records, customer
   or partner disclosures, and reliable market data before any secondary source.
2. **Historical reports are not evidence.** They teach style, section rhythm,
   and depth. They do not validate facts for another company.
3. **No invented facts.** If a needed data point is missing, state the exact
   missing item and continue only where the conclusion does not depend on it.
4. **One report, one voice.** Do not expose separate sub-skill outputs. The four
   pillars must be woven into the fixed report structure.
5. **One primary valuation method.** Select the method from the business
   mechanics and market-pricing mechanism. Other methods are brief sanity checks
   only. Do not average multiple valuation methods.
6. **Assets, orders, and debt are mandatory.** Every valuation section must
   explicitly address asset base, backlog/orders/contracts, cash, debt, maturity
   wall, dilution, and share count.
7. **Short-seller risk is mandatory.** Analyze the company as a potential
   activist short target. For normal companies, embed the result in prose. If
   serious red flags exist, expand the section.
8. **Technical analysis is decision-oriented.** Output only monthly/weekly/daily
   trend, primary pattern, support/resistance, entry, stop loss, and take-profit
   levels. Keep detailed pattern taxonomy internal unless needed for a specific
   price level.
9. **CFA-aligned formulas, not copied textbook prose.** Use standard formulas and
   method selection logic, but do not quote copyrighted finance textbooks.
10. **No third-party code copying.** External GitHub projects may influence
    workflow design and optional tool ideas only. Do not copy their code or
    proprietary prompts.
11. **No baked-in company triggers.** Do not use prior report companies,
    tickers, or temporary calibration companies as runtime trigger conditions.
    Extract methods only.
12. **Material numbers need source markers.** Revenue, cash, debt, share count,
    backlog, customer concentration, target price, and technical levels must be
    traceable to a source or clearly labeled as an assumption.
13. **Ontology before prose.** Build an internal object graph before writing the
    report. Report sections are projections from evidence-backed claims, not the
    storage layer for facts.

## Workflow

### 1. Scope And Source Map

Identify:

- company legal name, ticker, exchange, currency, fiscal year, and reporting
  standard
- current market cap, share price, diluted share count, cash, total debt, and
  enterprise value
- industry archetype:
  - mature compounder
  - semiconductor cyclical
  - specialty semiconductor or advanced manufacturing growth
  - resource or commodity policy
  - defense or strategic supply-chain beneficiary
  - early commercialization/frontier
  - turnaround or levered recovery
  - software/platform/fintech
  - bank/lender/financial institution
  - healthcare or reimbursement
  - multi-segment/SOTP

Build an internal evidence ledger with four labels:

- `verified_fact`: directly supported by primary or high-quality source
- `inference`: derived from verified facts
- `scenario_assumption`: explicit forward assumption
- `opinion`: analyst judgment

Facts and judgments must not blur in the final report.

For material facts in the final report, include concise source markers such as
`[filing]`, `[earnings call]`, `[IR presentation]`, `[regulator]`,
`[counterparty]`, or `[market data]`. The marker must make the evidence class
clear even when a full bibliography is not requested.

### 2. Ontology Object Graph

Use `references/ontology-framework.md` and the YAML contracts in `ontology/`.

Create an internal graph with these minimum objects before report composition:

- `Company`, `Security`, `SourceDocument`, `EvidenceItem`, `Claim`
- `MetricObservation`, `ContractOrder`, `OrderQualityAssessment`
- `AssetFacility`, `DebtInstrument`, `DilutionInstrument`
- `FinancialQualityAssessment`, `CurrentMarketImpliedBridge`
- `ValuationMethodSelection`, `ValuationCase`
- `ShortRiskSignal`, `ShortSellerAssessment`
- `TechnicalSetup`, `TradePlan`, `DataGap`, `ReportSection`

Core rule:

```text
SourceDocument -> EvidenceItem -> Claim -> analysis object -> ReportSection
```

High-materiality claims must be supported, contradicted, qualified, or blocked.
If evidence is missing, create a data-gap object and block the affected target,
technical level, or trade conclusion.

Run the ontology gates before final prose:

- Evidence Gate
- Source Priority Gate
- Order Gate
- Financial Gate
- Debt Gate
- Valuation Gate
- Short Risk Gate
- Technical Gate
- Data Gap Gate

### 3. Business Model Logic

Use `references/business-model-framework.md`.

Answer in narrative form:

- what economic problem the company solves
- who pays it, why they pay, and what cost they avoid
- old value driver versus new value driver
- why the change is happening now
- how the company captures value rather than merely benefiting from industry
  growth
- TAM, market share, competitors, customer concentration, and supply-chain
  bottleneck
- capacity, utilization, product mix, order conversion, and operating leverage

The business section must end with a bold one-sentence judgment that names the
value driver, current stage, and key observable.

### 4. Valuation With Assets, Orders, And Debt

Use `references/valuation-framework.md`.

Before selecting the valuation method, reverse-engineer the current market
pricing mechanism:

- What metric does the market seem to price: EPS, EBITDA, revenue, FCF, book,
  NAV, backlog, or optionality?
- Which events moved the stock recently?
- Are sell-side or peer multiples using the same denominator?
- What operating or financial assumption is already implied by the current
  share price or enterprise value?

Then select one primary method:

- semiconductor cyclical: mid-cycle EPS x historical or through-cycle P/E
- specialty semiconductor/growth manufacturing: forward EV/EBITDA with a
  re-rating catalyst
- resource/commodity: volume x realized price x unit margin -> EBITDA -> peer
  EV/EBITDA, with asset/NAV cross-check
- early commercialization with firm backlog: risk-adjusted backlog or EV/sales
  scenario, but only if order quality is strong
- pre-revenue binary asset: rNPV, scenario framing, or no target if evidence is
  insufficient
- turnaround: P/FCF, normalized EBITDA, replacement value, or liquidation floor
- financial institution: residual income or P/B x ROE
- multi-segment: SOTP

Required valuation outputs:

- current market cap and EV
- asset base and liquidation/replacement relevance
- backlog/order quality and revenue conversion schedule
- debt stack, maturity wall, cash runway, interest burden, and dilution risk
- net income to operating cash flow reconciliation and working-capital movement
- current-market-implied expectation before the analyst target
- primary valuation derivation with inline arithmetic
- EV-to-equity-to-diluted-share bridge for any per-share target
- bull/base/bear cases, each tied to a concrete observable
- one target price or target market cap, unless evidence is insufficient
- short sanity check from one secondary method

Do not close with a range-only conclusion or probability-weighted average.

### 5. Short-Seller Risk

Use `references/short-seller-risk-framework.md`.

Run the forensic screen internally:

- customer and contract authenticity
- related-party transactions
- revenue recognition and round-tripping
- OCF versus net income
- receivables, DSO, inventory, DIO, and allowances
- auditor quality and auditor changes
- management background, insider selling, pledges, and compensation
- share dilution, convertibles, warrants, and ATM usage
- promotional activity versus real milestones
- litigation, regulatory, sanctions, and policy risk
- short interest, borrow cost, failures to deliver, and options skew when
  reliable market data is available

Output:

- a concise letter grade: `A/B/C/D/F`
- a one-sentence activist-short attack narrative and why it is strong or weak
- strict separation of verified facts, allegations, inferences, and unanswered
  questions
- green flags and red flags
- if grade is A/B, embed in financial/debt discussion and keep the standalone
  short-seller section short
- if grade is C or worse, expand the short-seller section with specific evidence
  and explain how it changes valuation or position sizing

### 6. Technical Analysis And Trade Plan

Use `references/technical-analysis-framework.md`.

Required inputs:

- daily, weekly, and monthly OHLCV chart data or reliable chart screenshots
- chart date and adjusted/unadjusted status for historical prices
- recent catalyst calendar from the fundamental work

Required output:

- monthly trend, weekly trend, daily trend
- primary pattern and status
- 2-3 support levels and 2-3 resistance levels
- volume confirmation
- whether chart structure confirms or contradicts the fundamental thesis
- entry zone, stop loss, first take-profit, second take-profit
- position size tied to evidence quality and stop distance

If no defensible setup exists, state that there is no clear entry point and name
the price or catalyst that would change the setup. Do not invent levels.

### 7. Quality Calibration Loop

Use `references/quality-calibration-loop.md` before finalizing substantial
reports or when improving this Skill.

Process:

1. Draft the report for the requested company or a temporary public-company
   calibration target.
2. Compare the draft against the reference-caliber quality bar: opening tension,
   business causal chain, order quality, cash conversion, current-implied
   valuation, per-share bridge, short-risk effect, technical freshness, and
   final trade usefulness.
3. Diagnose every gap as either a data gap, reasoning gap, structure gap, or
   validation gap.
4. Revise the report or Skill contract until no actionable gap remains.

Do not commit temporary company names, tickers, or generated reports as triggers
or reusable prompts.

### 8. Final Report Composition

The final report must use this fixed structure:

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

- `Company Overview`: 1-2 paragraphs. Start with the current investment tension,
  not founding-date boilerplate. Read from `Company`, `Security`, and the
  highest-materiality current-dispute claims.
- `Business Model Logic`: longest section. Explain old -> new value driver,
  value capture, TAM/share, and why now. Read from `BusinessModelThesis` and
  `ValueDriverTransition`.
- `Operations, Customers, And Orders`: named facilities, capacity, utilization,
  named customers, backlog/order table, delivery cadence, bottlenecks. Read from
  `CustomerCounterparty`, `ContractOrder`, and `OrderQualityAssessment`.
- `Financials, Assets, And Debt`: 3-year financial table, forward model, asset
  base, cash, debt, maturities, dilution, cash-conversion reconciliation, and
  embedded short-seller quality note. Read from `MetricObservation`,
  `AssetFacility`, `DebtInstrument`, `DilutionInstrument`, and
  `FinancialQualityAssessment`.
- `Valuation`: one primary method with inline arithmetic; no method averaging.
  State the current-market-implied assumption before the analyst target and show
  the EV-to-equity-to-diluted-share bridge. Read from
  `CurrentMarketImpliedBridge`, `ValuationMethodSelection`, and `ValuationCase`.
- `Short-Seller Risk`: concise unless red flags are material. Read from
  `ShortRiskSignal` and `ShortSellerAssessment`.
- `Technical Analysis`: compact, fresh, adjusted where needed, and
  decision-oriented. Read from `TechnicalSetup`.
- `Risk Factors`: specific risk list; do not bury thesis-breaking evidence here
  if it affects valuation. Read from `DataGap` and high-risk claims.
- `Trade Plan`: final actionable conclusion with stance, position size, entry,
  stop, take-profit, catalyst, and invalidation. Read from `TradePlan`.

## Style Rules

- Use the language requested by the user for the final report.
- Use concrete numbers, dates, and source attribution.
- Prefer narrative paragraphs plus a few compact tables.
- Use inline arithmetic in prose for important valuation and operating leverage
  links.
- Write defensible conviction. Confidence must come from evidence, not tone.
- Avoid generic filler, method averaging, and dashboard clutter.
- Do not output a full forensic dashboard unless the red flags justify it.
- Do not output a technical-analysis appendix. It is part of the report.

## Data Gaps

Ask the user for missing data only when the gap blocks a required conclusion and
cannot be filled from public sources. Typical blocking gaps:

- current diluted share count cannot be reconciled
- debt maturity schedule is missing for a levered company
- backlog is central to valuation but contract quality is undisclosed
- customer names or concentration are needed but neither filings nor supply-chain
  data disclose them
- chart data is unavailable for technical levels

When blocked, write the report sections that can be completed and mark the
blocked conclusion precisely.

## Pre-Final Self-Check

Before final output, verify:

- all nine fixed sections are present
- ontology gates have either passed or produced explicit blocked conclusions
- every high-materiality claim used in a section has evidence, contradiction,
  qualification, or a data-gap blocker
- every material number has a source or is clearly labeled as an assumption
- business logic explains value capture, not only industry growth
- valuation uses one primary method and one secondary sanity check at most
- asset, order/backlog, debt, maturity, and dilution are discussed
- short-seller risk has a grade and named red/green flags
- technical analysis has trend, pattern, support/resistance, entry, stop, and
  take-profit, or a clear observation reason
- final trade plan contains thesis, catalyst, stop, and invalidation
