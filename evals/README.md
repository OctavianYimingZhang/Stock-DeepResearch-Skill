# Regression Evals

These cases validate the behavior contract for `stock-research-report`.

They are not live financial-data tests. They check whether the Skill contract
requires the correct report structure and decision gates for representative
company archetypes from the user's reference-report set.

## Coverage

- semiconductor cyclical
- early commercialization and order-quality gating
- resource/commodity policy and backlog/NAV gating
- specialty semiconductor growth and capacity reservation
- equipment cycle, customer concentration, and order inflection
- advanced packaging, asset intensity, and customer commitments
- policy-linked manufacturing, debt/cash runway, and subsidy dependence
- fresh outside-reference public-company calibration without committed ticker
  triggers
- source lineage, evidence partition pruning, incremental refresh, and blocked
  conclusions when required evidence is missing or stale

## Required Assertions

Each case specifies:

- fixed report sections
- one primary valuation method
- asset/order/debt coverage
- source snapshots, run lineage, and evidence partitions where source scope is
  large or refreshed
- short-seller risk grade
- technical-analysis trade plan or explicit observation stance
- forbidden method averaging
- source markers for material numbers
- ontology object graph and gate status
- incremental refresh handling for changed source material
- current-market-implied valuation bridge
- cash-conversion reconciliation
- technical chart freshness and adjusted-data status

Run:

```bash
python3 scripts/validate.py
```
