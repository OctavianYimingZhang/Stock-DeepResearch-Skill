# Scorecard Decision Framework

This reference defines the decision layer used after the evidence graph,
business thesis, profit/cash-flow quality, valuation, short-risk screen, and
technical setup are complete.

`DecisionScorecard` is a report projection. It does not create new facts and it
does not override source priority. It compresses supported research objects
into an action grade, a binding cap reason, and a trade-plan constraint.

## Design Rule

Do not average numeric scores. Do not build a weighted model that turns weak
evidence into false precision. The final action grade is capped by the weakest
decision-critical blocker.

Use a qualitative grade:

- `A`: evidence quality, valuation odds, momentum, and risk filter all support a
  high-conviction stance.
- `B`: constructive but capped by one material issue.
- `C`: investable only with reduced size, milestone confirmation, or better
  entry.
- `D`: unfavorable balance of evidence, valuation, risk, or technical setup.
- `F`: avoid or no actionable long stance until a blocking issue is resolved.

The grade must always include `binding_cap_reason`.

## Required Objects

`ExpectationRevisionAssessment` captures whether revenue, EBITDA, EPS, FCF,
orders, or guidance are likely to be revised up, revised down, or remain
unconfirmed. It must separate verified guidance from analyst inference.

`MomentumRegimeAssessment` captures monthly, weekly, and daily trend alignment,
volume confirmation, overextension, support/resistance quality, chart
freshness, and whether the chart confirms or contradicts fundamentals.

`ValuationOddsAssessment` compares the current-market-implied expectation with
the report's base case, upside/downside asymmetry, target blockers, and the
fragile assumption behind the primary valuation method.

`RiskFilterAssessment` combines short-seller grade, balance-sheet constraint,
cash-flow quality, debt maturity, dilution, governance, regulatory, and evidence
quality issues. It determines whether the action grade must be capped.

`DecisionScorecard` contains:

- `company_quality`
- `operating_trend`
- `expectation_revision`
- `growth_logic`
- `momentum_state`
- `valuation_odds`
- `risk_filter`
- `action_grade`
- `binding_cap_reason`
- `trade_plan_effect`

## Build Order

Build the scorecard only after these objects exist or are explicitly blocked:

- `BusinessModelThesis`
- `ValueDriverTransition`
- `OrderQualityAssessment`
- `ProfitCashFlowQualityAnalysis`
- `CurrentMarketImpliedBridge`
- `ValuationMethodSelection`
- `EquityBridge`
- `ValuationCase`
- `ShortSellerAssessment`
- `TechnicalSetup`
- `DataGap`

If any required object is blocked, the scorecard can still be produced, but its
grade must state the blocker. A blocked valuation bridge, stale chart, weak
cash conversion, or unresolved debt maturity can cap the action grade even when
the narrative thesis is strong.

## Component Logic

Company quality should reflect the durability of the customer problem, value
capture mechanism, asset or software moat, customer concentration, operating
leverage, and evidence quality.

Operating trend should summarize revenue, margin, backlog/order conversion,
capacity utilization, working capital, cash conversion, and debt pressure.

Expectation revision should ask whether the next measurable update is more
likely to improve or weaken market expectations. Use filings, formal guidance,
earnings calls, and reliable market data before secondary commentary.

Growth logic should summarize why the company can grow profitably, not merely
why the end market may grow.

Momentum state should translate K-line structure into confirmation,
distribution, exhaustion, accumulation, or no clear setup.

Valuation odds should state whether current price already discounts the base
case, whether upside requires multiple expansion, and whether the downside is
protected by assets, cash flow, backlog, or balance-sheet strength.

Risk filter should name the issue that prevents a higher grade. Typical caps
include weak order evidence, unexplained OCF shortfall, share-count uncertainty,
debt maturity risk, elevated short-seller risk, stale technical levels, or
valuation already pricing the upside scenario.

## Thesis Grade Versus Trade Grade

Separate business attractiveness from trade action. A company can have a strong
business thesis and a lower action grade if the chart is extended, current price
already discounts the ramp, customer conversion is not yet visible, or dilution
is unresolved.

Use this decision chain:

```text
business quality -> operating proof -> cash-flow proof -> valuation odds ->
short-risk filter -> momentum state -> action grade
```

The `binding_cap_reason` must be the first issue that prevents a higher action
grade. Do not let a compelling industry narrative override a weak cap reason.

## Position-Size Translation

Translate grade into action:

- `A`: normal maximum size only if valuation upside and technical invalidation
  are both clear.
- `B`: constructive but use partial size or wait for a better entry.
- `C`: reduced size, milestone-dependent, or trade only around defined levels.
- `D`: observe, avoid new long exposure, or wait for evidence repair.
- `F`: no actionable long stance.

When TP1 is close to major resistance, the scorecard should allow partial
profit-taking even if the business thesis remains intact.

## Report Placement

Do not add a tenth default report section. Place the compact scorecard summary
in `Company Overview` when it helps frame the report, and place the final action
grade in `Trade Plan`.

The trade plan must state:

- action grade
- binding cap reason
- stance
- position size effect
- entry, stop, TP1, and TP2 or observation stance
- catalyst and invalidation

The scorecard can support a separate `scorecard_summary` output view, but the
default `full_report` remains the fixed nine-section report.
