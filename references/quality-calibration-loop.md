# Quality Calibration Loop

This reference defines how to test and improve the Skill without embedding any
reference company names, tickers, or trigger phrases into the Skill.

## Purpose

The Skill should be calibrated against prior high-quality reports by extracting
methods, not by copying companies. Prior reports are used to identify structural
patterns: opening tension, business-model depth, valuation mechanics, order and
debt treatment, profit/cash-flow quality, short-risk thinking, decision
scorecard discipline, and trade-plan usefulness.

## Fresh-Company Test

When iterating the Skill, use a public company outside the prior reference set.
The test company should be used only as a temporary calibration target. Do not
commit the company name, ticker, or generated report as a Skill trigger.

The test must check whether the Skill forces the analyst to produce:

- a first-paragraph current re-rating dispute
- old value driver, new value driver, and one verification variable
- industry-to-company bridge and explicit value-capture mechanism
- source markers for material facts and numbers
- order evidence graded by legal and financial quality
- order-to-revenue path, customer funding, and capacity match
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

## Gap Diagnosis

After drafting the test report, compare it against the quality bar:

| Gap type | Failure signal | Contract response |
|---|---|---|
| opening is generic | starts with static company background | require re-rating dispute first |
| business logic is shallow | lists products without value capture | require causal chain and verification variable |
| transition is vague | old and new value drivers are not separated | require strategic transition tests |
| orders are overstated | treats pipeline as backlog | require order-proxy ladder and haircut |
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

## Repository Explanation Standard

GitHub-facing docs should explain the calibration method in abstract terms:

- what was tested
- which quality gaps were found
- what contract changes closed them
- what validation now enforces

Do not commit temporary generated stock reports unless the user explicitly asks
for a report corpus.
