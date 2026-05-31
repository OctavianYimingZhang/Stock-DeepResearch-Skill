# Quality Calibration Loop

This reference defines how to test and improve the Skill without embedding any
reference company names, tickers, or trigger phrases into the Skill.

## Purpose

The Skill should be calibrated against prior high-quality reports by extracting
methods, not by copying companies. Prior reports are used to identify structural
patterns: opening tension, business-model depth, industry-chain bottleneck
logic, order and commercialization quality, operations and capacity execution,
profit/cash-flow quality, valuation mechanics, short-risk thinking, decision
scorecard discipline, and trade-plan usefulness.

Historical reports are not factual sources. They are only a benchmark for how a
research path becomes a causal investment memo.

## Calibration Target

A reference-caliber report should not merely complete headings. It should answer
one investable question:

```text
what is being repriced now, why the company sits at the scarce node, whether the
commercial evidence can become revenue and cash, and whether the current price
already discounts that outcome
```

The Skill must therefore force this sequence before final prose:

```text
outside thesis path -> independent verification -> opportunity archetype
-> demand expansion -> scaling difficulty -> bottleneck scarcity
-> order/commercialization visibility -> operating and financial conversion
-> current-implied valuation -> falsification -> trade plan
```

## Fresh-Company Test

When iterating the Skill, use a public company outside the prior reference set.
The test company should be used only as a temporary calibration target. Do not
commit the company name, ticker, or generated report as a Skill trigger.

The test must check whether the Skill forces the analyst to produce:

- a first-paragraph current re-rating dispute
- outside thesis replay when public articles or user notes shaped the ticker
  path
- opportunity archetype routing before report section emphasis
- demand expansion, scaling difficulty, bottleneck scarcity, and
  commercialization visibility for any high-conviction thesis
- industry primer only when it clarifies the bottleneck or policy mechanism
- old value driver, new value driver, and one verification variable
- industry-to-company bridge and explicit value-capture mechanism
- source markers for material facts and numbers
- order evidence graded by legal and financial quality
- order-to-revenue path, customer funding, capacity match, margin visibility,
  working-capital burden, and cash conversion
- operations analysis that ties facility status, utilization, capex, ramp date,
  bottleneck, and margin at scale to the thesis
- cash, debt, maturity, dilution, and share-count bridge
- net income to operating cash flow reconciliation
- EBITDA-to-OCF-to-FCF bridge, capex quality, SBC-adjusted FCF, and FCF per
  share
- current-market-implied expectation before analyst valuation
- re-rating bridge and funding bridge when the thesis depends on ramped
  capacity or strategic scarcity
- one primary valuation method and one secondary sanity check
- short-seller risk grade with verified fact versus inference separation
- falsification lens for the main upside thesis
- technical analysis using current adjusted OHLCV or a blocked-status note
- action grade and binding cap reason from the decision scorecard
- entry, stop, first take-profit, second take-profit, position size, and
  invalidation

## Reference-Caliber Memo Test

After the first draft, compress the report into one thesis kernel:

```text
repricing dispute -> demand shock -> scarce node -> issuer control point
-> commercial proof -> operating proof -> cash proof -> valuation implication
-> action cap -> execution plan
```

The draft passes only if each section advances that kernel. If a section can be
removed without weakening the investment conclusion, the section is filler and
must be rewritten or deleted.

A passing draft has these features:

- the reader understands why the stock matters before reading corporate history
- industry context explains the bottleneck, not the entire industry
- company positioning separates company alpha from industry beta
- customer and order discussion separates binding demand from pipeline
- operations show whether the company can deliver the demand it claims
- financial quality shows whether growth converts to owner cash flow
- valuation starts from what the current price already implies
- risks include a plausible short-seller attack narrative
- the trade plan contains actual action logic, not only commentary

## Anti-Checklist Reconstruction Pass

Before final output, run this repair pass:

1. Remove any paragraph that could apply to most peers in the same industry.
2. Move industry context ahead of company description only when it explains the
   bottleneck.
3. Convert every generic catalyst into a dated or source-linked observable.
4. Convert every order claim into an order-quality level and revenue-conversion
   path.
5. Convert every operating claim into capacity, utilization, funding, ramp date,
   and failure signal.
6. Convert every financial claim into a cash-conversion, capex, dilution, or
   senior-claim effect.
7. Convert every valuation multiple into a current-implied expectation and one
   re-rating condition.
8. Convert every risk into either a thesis-breaker, valuation haircut, or
   position-size cap.
9. Convert every technical comment into an action or a blocked setup.

A report that still reads like headings filled with facts has failed this pass.

## Gap Diagnosis

After drafting the test report, compare it against the quality bar:

| Gap type | Failure signal | Contract response |
|---|---|---|
| opening is generic | starts with static company background | require re-rating dispute first |
| outside thesis is untested | article narrative becomes fact | require thesis-path replay and primary verification |
| opportunity route is missing | every issuer receives the same emphasis | require opportunity archetype routing |
| opportunity test is shallow | demand, scaling, scarcity, or commercialization is not tested | require four-part opportunity assessment |
| industry primer is generic | explains the whole industry instead of the scarce node | require bottleneck-only primer |
| business logic is shallow | lists products without value capture | require causal chain and verification variable |
| transition is vague | old and new value drivers are not separated | require strategic transition tests |
| scarcity is unsupported | calls a theme scarce without replication analysis | require scarcity type, duration, and replication barrier |
| orders are overstated | treats pipeline as backlog | require order-proxy ladder and haircut |
| commercialization is vague | order evidence is not linked to revenue and cash | require order-to-revenue and cash-conversion bridge |
| operating ramp is vague | capacity growth is not tied to customers and funding | require operating ramp bridge |
| valuation is mechanical | gives target without current implied assumption | require current-price-implied bridge |
| re-rating is asserted | multiple expansion lacks proof event | require re-rating bridge |
| target math is incomplete | skips EV-to-equity-to-share bridge | require per-share bridge |
| financial quality is missed | net income and cash flow diverge without explanation | require cash-conversion reconciliation |
| owner cash flow is missed | FCF ignores capex, SBC, or diluted shares | require profit/cash-flow quality analysis |
| short risk is isolated | red flags do not affect valuation or size | require valuation or position-size impact |
| falsification is absent | upside thesis has no monitorable failure pattern | require short-risk falsification lens |
| technical work is stale | levels lack chart date or adjusted OHLCV status | require freshness and adjustment check |
| scorecard is cosmetic | high grade ignores a binding blocker | require action-grade cap reason |
| trade plan is vague | no entry, stop, take-profit, or size | require full trade contract |

## Exit Criteria

Iteration can stop only when no actionable gap remains in the Skill contract,
reference framework, eval metadata, or validation script.

Acceptable residual limits:

- live data availability can remain a runtime limitation if the Skill blocks
  unsupported conclusions instead of inventing data
- a company-specific fact gap can remain if the report names the exact missing
  source
- no company-specific test name or ticker may be committed as a trigger
- no outside article thesis may drive valuation unless independently verified or
  clearly labeled as a scenario assumption

## Repository Explanation Standard

GitHub-facing docs should explain the calibration method in abstract terms:

- what was tested
- which quality gaps were found
- what contract changes closed them
- what validation now enforces

Do not commit temporary generated stock reports unless the user explicitly asks
for a report corpus.