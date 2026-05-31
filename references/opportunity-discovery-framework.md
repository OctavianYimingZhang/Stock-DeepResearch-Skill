# Opportunity Discovery Framework

This reference defines how the Skill decides what investment question it is
answering before drafting a report. The report should not force every issuer
through the same emphasis. It should route the company by opportunity archetype,
then set the evidence burden, section weight, valuation method, and action-grade
cap from that route.

The report must start from why the stock matters now. It should then move from
industry pressure to scarce node, company control point, commercial proof,
operating proof, cash conversion, valuation, and trade action.

## Thesis Kernel

Before drafting prose, compress the research into one kernel:

```text
repricing dispute -> demand expansion -> scaling constraint -> scarce node
-> company control point -> commercialization proof -> operating proof
-> cash conversion -> current-implied valuation -> action cap
```

The kernel is the report spine. Every major section must advance one part of the
kernel. Static company description is allowed only when it explains the control
point, scarce node, customer payment reason, or valuation denominator.

## Opportunity Archetype

Create an `OpportunityArchetype` object before valuation:

- `scarcity_bottleneck`
- `policy_protected_supply_chain`
- `customer_funded_capacity_ramp`
- `operating_leverage_recovery`
- `order_backlog_repricing`
- `strategic_asset_optional_value`
- `levered_residual_equity`
- `early_commercialization`
- `mature_infrastructure_compounder`
- `commodity_or_resource_processing`

If no archetype is supported, classify the issuer as `industry_beta` or
`watchlist_only` and cap the action grade until a company-specific mechanism is
verified.

## Routing Rules

Use `scarcity_bottleneck` when the thesis depends on unique capacity,
qualification, process know-how, supply-chain chokepoint, restricted access, or
customer approval.

Use `policy_protected_supply_chain` when the thesis depends on law, subsidy,
tariffs, domestic-content rules, regulated sourcing, or public-sector customer
preferences.

Use `customer_funded_capacity_ramp` when a plant, mine, factory, fab, production
line, or data center must scale and the funding source is central.

Use `operating_leverage_recovery` when fixed-cost absorption, utilization,
cycle recovery, or mix shift drives earnings more than new demand.

Use `order_backlog_repricing` when the market is repricing recognized revenue,
binding purchase orders, contracted backlog, or customer-funded commitments.

Use `strategic_asset_optional_value` when hard assets, permits, licenses,
location, reserves, data, or infrastructure create downside floor or strategic
optionality.

Use `levered_residual_equity` when debt, preferred stock, warrants,
convertibles, or maturity walls can absorb most upside or block a per-share
target.

Use `early_commercialization` when the company is moving from prototype, pilot,
or framework agreement to revenue, orders, and cash conversion.

Use `mature_infrastructure_compounder` when durable cash flow, reinvestment
rate, pricing power, and capital allocation matter more than a single catalyst.

Use `commodity_or_resource_processing` when spread, cost curve, reserve quality,
processing margin, logistics, or policy-linked supply drives value.

## Four-Part Opportunity Test

Every high-conviction thesis must create these objects:

- `DemandExpansionAssessment`
- `ScalingDifficultyAssessment`
- `ScarcityBottleneckAssessment`
- `CommercializationPathAssessment`

The test asks:

1. Demand expansion:
   - What end demand is growing?
   - Who is spending?
   - Why now?
   - Is this structural demand or cyclical rebound?
   - Does the company have direct exposure or only thematic exposure?

2. Scaling difficulty:
   - Why can supply not expand quickly?
   - Which barrier matters: certification, qualification, capex, build time,
     yield, customer approval, regulation, financing, or channel access?
   - How long would replication likely take?
   - What source would prove that replication is easy or hard?

3. Bottleneck or scarcity:
   - Which exact value-chain node is scarce?
   - Why does this company control, relieve, or monetize that scarcity?
   - Is scarcity technical, capacity-based, policy-based, customer-based,
     asset-based, financing-based, or channel-based?
   - Is it temporary, cyclical, or structural?
   - Does the scarcity create pricing power, order priority, customer funding,
     margin expansion, reliability value, or compliance value?

4. Commercialization visibility:
   - What evidence converts the thesis into revenue and cash?
   - Separate recognized revenue, binding purchase order, contracted backlog,
     paid reservation, customer prepayment, framework, pilot, MOU, LOI,
     pipeline, and management aspiration.
   - State which evidence level can support the base case and which belongs only
     in the upside case.

If any part fails, the report may still be useful, but the conclusion must be
observation, watchlist, scenario, or capped conviction unless valuation already
prices the equity as a discounted option.

## Alpha Versus Beta Test

Industry growth is not enough. The report must decide whether the issuer has
company alpha or only industry beta.

Company alpha requires at least one supported control point:

- scarce process capability
- unique capacity or facility status
- customer qualification
- regulatory or policy gate
- switching cost
- proprietary consumable, service, or attach stream
- strategic location or supply-chain access
- cost curve or funding advantage
- order conversion stronger than peers

If the report cannot identify a control point, cap the action grade and state
that the issuer is mainly a vehicle for the industry theme.

## Scarcity-To-Economics Test

A scarce node matters only when it changes economics. For every scarcity claim,
map the effect to at least one of:

- higher price
- shorter customer cycle time
- lower customer scrap, downtime, compliance risk, or project delay
- higher gross margin
- higher utilization
- customer prepayment or funded expansion
- repeat consumable or service revenue
- stronger backlog conversion
- lower downside through asset value or policy support

Scarcity without economics is not enough for valuation.

## Commercialization Visibility Ladder

Use this order when grading commercial proof:

```text
recognized revenue > binding purchase order > firm backlog > paid capacity
reservation > customer prepayment > commercial contract > IDIQ/framework
> pilot/MOU/LOI > pipeline > management aspiration
```

Base-case valuation normally requires recognized revenue, binding purchase
orders, firm backlog, paid reservations, customer prepayment, or customer-funded
capacity. Weaker evidence can support upside optionality, but it must receive a
haircut and cannot carry the action grade by itself.

## Section Emphasis

The archetype changes the report emphasis:

- scarcity and policy routes require industry-chain and bottleneck depth
- capacity-ramp routes require asset, funding, utilization, and execution depth
- order routes require order-quality and order-to-revenue depth
- levered routes require debt, maturity, dilution, and residual-equity depth
- mature compounders require reinvestment, cash conversion, and capital
  allocation depth

The final report still uses one integrated voice. The archetype should shape
emphasis, not create a visible module dump.

## Discovery Exit Standard

Do not proceed to final prose until these fields are filled or blocked:

- `investment_question`
- `repricing_dispute`
- `opportunity_archetype`
- `industry_chain_node`
- `scarcity_type`
- `company_control_point`
- `commercialization_stage`
- `base_case_evidence_level`
- `key_operating_observable`
- `current_market_implied_expectation`
- `action_grade_cap_reason`

If these fields are weak, the report should say so directly and avoid a high
conviction action grade.