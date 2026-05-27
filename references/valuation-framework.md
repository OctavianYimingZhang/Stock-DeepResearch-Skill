# Valuation Framework

This reference defines the valuation system for the integrated research report.
It uses standard CFA-aligned public-company valuation methods without copying
textbook prose.

## Required Inputs

Before valuation, reconcile:

- current share price and market capitalization
- basic and diluted shares
- cash and short-term investments
- total debt, lease liabilities if material, and preferred/convertible
  securities
- enterprise value
- latest revenue, gross margin, EBITDA, EBIT, net income, EPS, CFO, capex, FCF
- OCF / net income, EBITDA -> OCF -> FCF, FCF margin, FCF conversion,
  SBC-adjusted FCF, FCF per share, and diluted share count
- segment revenue and margin where relevant
- backlog/orders/contracts and expected conversion schedule
- asset base, replacement value, book value, resource/NAV, or liquidation value
  where relevant
- debt maturities, interest cost, covenants, cash runway, ATM capacity, warrants,
  convertibles, and expected dilution

If diluted share count, net debt, or order quality cannot be reconciled, do not
present a high-conviction target price.

Create an `EquityBridge` object before any per-share target. The bridge must
stand apart from `ValuationCase` so validators can block target prices when
cash, debt, senior claims, non-operating assets, or diluted shares do not
reconcile.

Create `ProfitCashFlowQualityAnalysis` before method selection. A company with
weak or unexplained cash conversion should not receive mature-cash-flow
multiples unless the report states why the weakness is temporary and what
observable would confirm recovery.

## Market Pricing Mechanism

Reverse-engineer what the market is pricing before selecting the model:

- Does the stock move on EPS, EBITDA, revenue, backlog, policy news, commodity
  price, trial/regulatory events, book value, or technical momentum?
- What denominator do closest peers trade on?
- What multiple or assumption is implied by the current price?
- Which assumption is fragile?

The primary valuation method must match both company economics and the market's
actual pricing mechanism.

## Re-Rating Bridge

Reference-caliber reports explain why the market might change the multiple, not
only why the company might grow. Build a re-rating bridge:

```text
old market bucket -> new market bucket -> evidence of transition ->
future denominator -> target multiple condition -> blocker
```

Use this bridge when the thesis depends on the market moving from one valuation
identity to another, such as cyclical supplier to strategic infrastructure,
commodity processor to sovereign supply asset, low-margin manufacturing to
technology premium, or small growth story to funded order conversion.

The bridge must answer:

- what the old multiple or denominator was
- what the new denominator should be
- which verified event justifies the change
- whether current price already discounts the new identity
- what would prevent the multiple from expanding

## Current-Price-Implied Bridge

Before giving an analyst target, state what the current share price already
implies. In short, state what the current price already implies. This is the
main test that prevents a report from becoming a generic model.

Use the pricing denominator that the market is using:

```text
implied metric = current EV / current trading multiple
implied multiple = current EV / forward metric
implied EPS = current share price / current P/E
implied revenue conversion = current EV / expected backlog-to-revenue path
```

Then compare it with the analyst assumption:

```text
current price implies [metric or multiple]; the report's base case assumes
[metric or multiple] because [verified operational evidence].
```

If the current price already discounts the upside scenario, say so and do not
force a bullish target.

If the company looks expensive on trailing numbers, state whether the market is
pricing forward capacity, backlog conversion, EPS ramp, EBITDA ramp, strategic
scarcity, or balance-sheet optionality. Expensive is not a conclusion by itself;
the report must say which future event is already in the price.

## Method Selection

Use one primary method.

| Company type | Primary method | Secondary check |
|---|---|---|
| Semiconductor cyclical | Mid-cycle EPS x through-cycle P/E | EV/EBITDA |
| Specialty semi or advanced manufacturing growth | Forward EV/EBITDA with re-rating catalyst | P/E or SOTP |
| Resource or commodity | Unit volume x price x margin -> EBITDA x peer EV/EBITDA | NAV or asset value |
| Early commercialization with firm orders | Risk-adjusted backlog or forward EV/revenue | Cash runway and dilution |
| Pre-revenue binary asset | rNPV or scenario framing | Cash less burn |
| Turnaround | Normalized FCF, normalized EBITDA, or replacement/liquidation floor | Debt recovery value |
| Financial institution | Residual income or P/B x sustainable ROE | P/E |
| Multi-segment company | SOTP | Consolidated EV/EBITDA |
| Stable cash generator | P/FCF or FCFF DCF | Dividend/shareholder yield |

Do not average methods. A secondary method can invalidate or sanity-check the
primary method, but it is not an equal vote.

## Forward Ramp Math

For companies being repriced on a ramp rather than current earnings, model the
path explicitly:

```text
capacity or units x utilization x ASP or realized price = revenue
revenue x gross margin = gross profit
gross profit - fixed operating cost = EBITDA or operating income
EBITDA or EPS x selected multiple = target EV or equity value
```

Use the ramp only if capacity, timing, customer demand, funding, and gross
margin have enough evidence. If any link is weak, make the link a scenario
assumption and cap conviction.

For EPS-led cases:

```text
future EPS x justified P/E = future share value
```

The P/E must be tied to growth durability, cycle position, peer set, and rate
environment. Do not use historical average P/E without explaining why the future
business mix deserves that multiple.

## Profit And Cash-Flow Quality Before Method Selection

Use `references/profit-cash-flow-quality-framework.md` before selecting the
primary method. The valuation denominator must match cash-flow maturity:

- use P/FCF, FCFF, or FCFE only when owner cash flow is traceable and durable
- use EV/EBITDA only when the bridge from EBITDA to FCF is credible
- use revenue or backlog only when cash conversion is not yet mature and order
  quality is strong enough to support scenario work
- block or heavily haircut target value when SBC, capex, working capital, or
  dilution erase per-share economics

Owner FCF should be visible in the valuation discussion:

```text
owner FCF = operating cash flow - maintenance capex - economically recurring SBC
owner FCF per share = owner FCF / diluted or pro-forma shares
```

## Standard Formulas

### Enterprise Value

```text
EV = equity market value + debt + preferred stock + minority interest - cash
```

### FCFF

```text
FCFF = EBIT x (1 - tax rate) + D&A - capex - change in net working capital
FCFF = CFO + interest x (1 - tax rate) - capex
```

Use FCFF when capital structure is changing, leverage is material, or valuing
the firm before debt holders.

### FCFE

```text
FCFE = CFO - capex + net borrowing
FCFE = net income + D&A - capex - change in net working capital + net borrowing
```

Use FCFE only when leverage is stable and equity cash flow is meaningful.

### WACC

```text
WACC = E/(D+E) x cost of equity + D/(D+E) x pre-tax cost of debt x (1 - tax rate)
```

Use market values where available. If debt market value is unavailable, book
debt can be used with a note.

### Cost Of Equity

```text
cost of equity = risk-free rate + beta x equity risk premium + specific risk adjustments
```

Add country, size, liquidity, or project risk only if justified and stated.

### Terminal Value

```text
perpetuity TV = FCFF[n+1] / (WACC - terminal growth)
exit multiple TV = terminal metric x terminal multiple
```

Terminal growth must not exceed a sustainable economy-level growth assumption
without explicit justification.

### Residual Income

```text
residual income = net income - required return on equity x beginning book equity
equity value = current book equity + present value of future residual income
```

Use for banks, lenders, and firms where book capital and ROE are the relevant
value drivers.

### SOTP

```text
equity value =
  sum(segment metric x segment multiple)
  + non-operating assets
  - net debt
  - minority interest
  - holding/company-specific discount if justified
```

Use only when segments have materially different economics.

### Equity Bridge

```text
target equity value =
  target EV
  + cash and short-term investments
  + non-operating assets
  - debt
  - preferred or convertible senior claims
  - minority interest
target price = target equity value / diluted or pro-forma shares
```

The `EquityBridge` must state whether each adjustment is verified, assumed, or
blocked. If senior claims or diluted share count are unresolved, the bridge
outputs a blocker rather than a target price.

### Commodity/Resource Unit Math

```text
revenue = volume x realized price
unit margin = realized price - cash cost
EBITDA = volume x unit margin - fixed cash cost + byproduct credits
equity value = EBITDA x peer EV/EBITDA - net debt
```

For resources, include reserve/resource confidence, permitting status, recovery
rate, capex, byproduct credits, and realized vs. spot pricing.

### rNPV

```text
rNPV = probability of success x present value of conditional cash flows
       - remaining development cost
company equity value = sum(asset rNPV) + cash - debt
```

Use for drug pipelines, single-asset projects, reserves, permits, or other
binary outcomes. Do not use full-success DCF for assets that still face major
approval or commercialization gates.

## Orders And Backlog

Order valuation requires evidence quality.

| Evidence | Valuation use |
|---|---|
| recognized revenue | strong |
| binding PO or firm backlog | strong if delivery and margin are visible |
| paid capacity reservation | medium to strong depending on cancellation terms |
| IDIQ/framework | scenario input only unless conversion history exists |
| MOU/LOI/pilot | not a valuation denominator |
| management pipeline | narrative only |

For backlog:

```text
risk-adjusted backlog value =
  backlog x delivery probability x expected gross margin
  - required capex/working capital
```

Backlog is not profit. Always convert to margin and cash flow.

When formal backlog is absent, use an order-proxy ladder rather than treating
all demand signals as equal:

| Proxy | How to use it |
|---|---|
| revenue already recognized | strongest proof of conversion |
| customer concentration in filings | evidence of demand, but adds credit and concentration risk |
| inventory purchase obligation | supply-side commitment, not customer demand |
| management revenue guide | forecast input, haircut unless repeatedly met |
| capacity expansion funded by customers | strong only if payment and cancellation terms are disclosed |
| production capacity sold out | useful, but weak unless buyer, price, and margin are visible |

The report must state whether the order evidence is a revenue fact, legal
contract, financial obligation, management guide, or unsupported pipeline.

## Assets And Debt

Every valuation must address:

- asset replacement value or liquidation relevance
- cash and restricted cash
- gross debt and net debt
- maturity schedule by year
- interest burden and coverage
- covenants or going-concern language
- convertibles, warrants, preferred stock, ATM usage, and dilution
- lease liabilities if material

Debt can change the equity thesis even if enterprise value looks attractive.

For growth companies with large capex needs, build a funding bridge:

```text
cash + expected OCF + customer prepayments + grants or credits + available
credit - committed capex - working-capital build - debt maturities = funding
surplus or gap
```

If the funding bridge depends on future equity issuance, the valuation must show
the pro-forma share count effect before stating per-share upside. If the bridge
depends on government funding or customer prepayments, state the evidence class
and timing risk.

## Inline Arithmetic Standard

Show the main math in prose:

State the forecast metric, selected multiple or discount rate, resulting equity
value, net debt adjustment, share count bridge, and implied upside in one
readable chain.

Tables can support the math, but the reader must see the equation in the
narrative.

For equity targets, include the full per-share bridge:

```text
target EV = forecast metric x selected multiple
target equity value = target EV - net debt + non-operating assets
target price = target equity value / diluted shares
```

Do not skip directly from EV to target price. If share count may change through
warrants, convertibles, preferred stock, or expected equity issuance, use the
diluted or pro-forma share count and say why.

## When Not To Give A Target

Do not give a target price when:

- share count cannot be reconciled
- debt or preferred stack materially changes equity value and is unknown
- backlog quality is weak but central to the thesis
- the company has no revenue denominator and no binary-asset rNPV support
- the available evidence cannot support the implied cash-flow path

In these cases, write a scenario frame and list the data needed to unblock a
target.
