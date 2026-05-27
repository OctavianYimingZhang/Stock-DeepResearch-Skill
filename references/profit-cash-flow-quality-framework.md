# Profit Cash Flow Quality Framework

This reference defines the profit-to-cash-flow layer used before valuation,
short-seller risk, decision scoring, and trade planning. Its object is
`ProfitCashFlowQualityAnalysis`.

The goal is to determine whether reported earnings translate into owner cash
flow and whether per-share economics survive working-capital needs, capex, SBC,
and dilution.

## Required Analysis Lenses

The report must cover these lenses when data is available:

- OCF / net income: compare operating cash flow with net income for the latest
  period and cumulatively across the analysis window.
- EBITDA -> OCF -> FCF: reconcile EBITDA to operating cash flow and then to
  free cash flow, naming working-capital, tax, interest, lease, and capex
  drivers.
- FCF quality: distinguish recurring FCF from one-time working-capital release,
  asset sale proceeds, deferred capex, or unusually low cash tax.
- FCF margin and FCF conversion: compute free cash flow as a percentage of
  revenue and as a percentage of EBITDA or net income.
- Working-capital cycle: explain DSO, DIO, DPO, inventory, receivables, payable
  timing, contract assets, deferred revenue, and customer prepayments.
- Capex / D&A: compare capex with depreciation and amortization and state
  whether current capex appears maintenance-like, growth-like, catch-up, or
  temporarily suppressed.
- Maintenance versus growth capex: do not call all capex discretionary when the
  company needs it to sustain capacity, certification, safety, compliance, or
  customer commitments.
- Rule of 40 applicability: use `not_applicable` when the business is not a
  software or subscription model where revenue growth plus FCF margin is a
  relevant quality screen.
- SBC-adjusted FCF: subtract stock-based compensation from free cash flow when
  dilution is economically meaningful.
- FCF per share: divide owner FCF by diluted or pro-forma shares, not basic
  shares when warrants, convertibles, preferred stock, or ATM issuance matter.
- Diluted shares outstanding: reconcile current and pro-forma share count before
  making any per-share owner cash-flow claim.

## Object Contract

`ProfitCashFlowQualityAnalysis` should contain:

- `ocf_to_net_income_reconciliation`
- `ebitda_to_ocf_to_fcf_bridge`
- `fcf_margin_or_conversion`
- `working_capital_cycle`
- `capex_quality`
- `maintenance_vs_growth_capex`
- `sbc_adjusted_fcf`
- `fcf_per_share`
- `diluted_share_count_effect`
- `rule_of_40_applicability`
- `cash_quality_verdict`
- `valuation_effect`
- `short_risk_effect`

The object reads from `MetricObservation`, `FinancialQualityAssessment`,
`DebtInstrument`, `DilutionInstrument`, and evidence-backed `Claim` objects.
It writes a verdict that can support or block `ValuationCase`,
`ShortSellerAssessment`, `RiskFilterAssessment`, and `TradePlan`.

## Interpretation Rules

Positive quality signals:

- OCF is consistently close to or above net income.
- FCF remains positive after maintenance capex.
- Working-capital release is not the main source of cash generation.
- Capex supports visible customer demand or asset productivity.
- Customer prepayments, grants, or paid reservations fund expansion before the
  company carries the full cash burden.
- Inventory build is matched to signed orders, production ramps, or disclosed
  delivery schedules.
- Diluted share count is stable or accretion offsets dilution.
- SBC-adjusted FCF remains positive.

Negative quality signals:

- Net income grows while OCF deteriorates.
- Receivables, inventory, or contract assets grow materially faster than
  revenue.
- FCF depends on delayed payables, deferred capex, or one-time cash inflows.
- Capex is described as growth but is required to maintain operations.
- Inventory or contract assets rise before evidence of customer conversion.
- Customer-funded capex is assumed but not supported by payment terms.
- SBC or financing dilution turns firm-level cash flow into weak per-share cash
  flow.
- The company reports strong adjusted EBITDA while cash flow stays weak.

These signals are not fraud claims by themselves. They determine valuation
confidence, short-seller vulnerability, and position sizing.

## Valuation Integration

Before selecting a primary valuation method, decide whether cash flow is mature,
transitional, or unreliable:

- Mature cash flow can support P/FCF, FCFF, FCFE, EV/EBITDA, or shareholder
  yield methods.
- Transitional cash flow may support EV/EBITDA only if the bridge to future FCF
  is explicit.
- Unreliable cash flow should cap multiple expansion, reduce position size, or
  block a high-conviction target.

For per-share value, use owner cash flow:

```text
owner FCF = operating cash flow - maintenance capex - economically recurring SBC
owner FCF per share = owner FCF / diluted or pro-forma shares
```

If maintenance capex cannot be separated from growth capex, state the gap and
use total capex as the conservative default for sanity checking.

## Ramp-Stage Cash Discipline

For companies transitioning from small revenue to contracted ramp, separate
strategic cash from operating cash:

- cash raised for expansion
- cash produced by operations
- cash locked in working capital
- cash required for committed capex
- cash protected by customer prepayment, grants, or credits
- cash consumed before the next revenue milestone

Use this bridge:

```text
net cash runway = cash and marketable securities + expected near-term OCF
  + verified customer funding or grants
  - committed capex
  - working-capital build
  - debt maturities
```

If cash runway is strong but per-share dilution is large, state both facts. A
fortress balance sheet can reduce bankruptcy risk while still capping per-share
upside.

## Short-Seller And Scorecard Integration

Cash-flow quality feeds the forensic screen. A weak OCF / net income pattern,
rapid DSO/DIO expansion, aggressive capitalization, or recurring dilution should
be tested as a short-seller risk signal.

Cash-flow quality also feeds `DecisionScorecard`. Strong business logic cannot
receive a high action grade when owner FCF is negative, cash conversion is
unexplained, or per-share dilution offsets operating progress. The scorecard
must state the binding cap reason instead of hiding the issue in a generic risk
paragraph.
