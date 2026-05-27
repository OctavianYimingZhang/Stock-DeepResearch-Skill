# Short-Seller Risk Framework

This reference translates common activist short-seller perspectives into an
investment-report risk module. It is not a fraud accusation template. Every
claim must be sourced.

## Output Modes

### Embedded Mode

Use when red flags are low or moderate.

Output:

```text
Short-Seller Risk: [A/B/C/D/F] grade - [one-sentence verdict].
[One compact paragraph covering balance sheet, earnings quality, governance,
customer/order quality, and named red/green flags.]
```

### Expanded Mode

Use when any of these is true:

- three or more material red flags are present
- OCF materially trails net income for multiple years
- auditor resigned, downgraded, or issued going-concern/qualified language
- management has material undisclosed conflicts or severe promotional behavior
- active SEC/DOJ/regulatory investigation exists
- backlog/contracts are central to valuation but weak or unverifiable
- share count has increased materially and dilution is ongoing

Expanded mode explains how the risk affects valuation or position sizing.

## Letter Grade

| Grade | Meaning |
|---|---|
| A | Clean enough for the report; no material short-seller angle found |
| B | Some monitoring items; not thesis-breaking |
| C | Elevated risk; valuation or position size must be discounted |
| D | High risk; short thesis elements are material |
| F | Critical risk; avoid numeric long target unless issues are resolved |

## Core Checks

Label sensitive claims precisely:

- `verified fact`: directly sourced
- `allegation`: claim made by a short report, lawsuit, regulator, or other
  external party
- `inference`: analyst conclusion derived from verified facts
- `unanswered question`: unresolved item that needs a filing, transcript,
  counterparty confirmation, or market-data source

Do not present an inference as a verified fact.

### 1. Customer And Contract Authenticity

Check:

- named customers in filings vs. press releases
- counterparty disclosure from the other side
- contract form: revenue, PO, backlog, capacity reservation, IDIQ, framework,
  MOU, pilot, LOI
- delivery schedule vs. recognized revenue
- customer prepayments, take-or-pay terms, cancellation rights, and procurement
  authority
- concentration above 10%, 20%, and 50%
- customer credit quality and procurement authority

Common risk pattern: promotional contract announcements without disclosed value,
counterparty confirmation, revenue conversion, or purchase obligation.

For government, policy-linked, or procurement-led demand, verify budget source,
award status, prime/subcontract position, certification requirement, and whether
the company is selling directly or through another vendor.

### 2. Revenue Recognition And Round-Tripping

Check:

- revenue-recognition policy
- gross vs. net presentation
- related vendor/customer relationships
- two-way contracts where the company is both buyer and seller
- deferred revenue vs. recognized revenue
- quarter-end concentration
- rebates, credits, channel incentives, bill-and-hold, or distributor stuffing

If revenue grows while receivables, contract assets, or inventory grow much
faster, explain the working-capital risk.

### 3. Cash Flow Quality

Read `ProfitCashFlowQualityAnalysis` before assigning the final grade.

Check:

- cumulative OCF vs. cumulative net income
- EBITDA -> OCF -> FCF bridge
- FCF margin and FCF conversion
- CFO conversion ratio
- FCF after maintenance capex
- working-capital drivers
- DSO, DIO, DPO, inventory, receivables, and contract assets
- capitalized costs
- non-GAAP add-backs
- stock-based compensation
- SBC-adjusted FCF and FCF per share
- diluted shares outstanding and per-share cash-flow dilution

OCF consistently below net income is not proof of fraud, but it is a strong
quality warning that must be explained.

### 4. Balance Sheet And Dilution

Check:

- cash, restricted cash, and burn rate
- short-term and long-term debt
- debt maturity wall
- interest coverage
- covenants
- preferred stock, convertibles, warrants
- ATM or shelf registration
- share count growth over 1, 3, and 5 years
- short interest, borrow availability/cost, failures to deliver, and options
  skew where reliable market data is available

Dilution matters twice: it funds survival and changes per-share upside.

### 5. Governance And Related Parties

Check:

- auditor identity, tenure, changes, and PCAOB issues if relevant
- material weaknesses and restatements
- board independence
- executive compensation vs. revenue/market cap
- insider ownership, pledges, and selling
- related-party sales, purchases, leases, acquisitions, financing, or shared
  addresses
- SPAC/reverse-merger origin and business pivots

Do not imply wrongdoing without evidence. State the verified governance fact and
why it matters.

### 6. Promotion Versus Execution

Check:

- press release frequency vs. material revenue conversion
- paid media, celebrity marketing, or unusually promotional investor relations
- repeated missed milestones
- vague "pipeline", "strategic partnership", or "AI/defense/policy" language
  without commercial conversion
- management selling during promotional periods

Promotion is a risk only when it outruns verifiable execution.

Compare every major narrative claim with one execution metric: shipped units,
recognized revenue, gross margin, OCF, customer payment, capacity utilization,
or recurring reorder. A narrative that cannot be tied to an execution metric is
a short-risk monitoring item.

### 7. Legal, Regulatory, Sanctions, And Policy

Check:

- litigation and regulatory investigations
- sanctions or restricted-customer exposure
- permits, certification, reimbursement, or government-procurement gates
- policy subsidy dependence
- changes in law or procurement rules

If policy is central to valuation, specify what happens if policy support
changes.

## Falsification Lens

For each major upside thesis, name the fact pattern that would make a short
seller's attack stronger:

- announced orders do not convert into revenue
- revenue converts but gross margin or OCF disappoints
- capex rises faster than customer funding
- customer concentration increases instead of diversifying
- policy support changes or certification is delayed
- related-party sales, purchases, or financing become material
- dilution funds operating losses rather than asset-backed expansion
- inventory builds ahead of sell-through evidence

Use these as risk tests, not accusations. The final report should state what
would need to be monitored after publication.

## Red Flag Inventory

Use named red flags, not vague risk language:

- fabricated or unverified customer/contract
- related-party transaction not clearly disclosed
- revenue grows while cash conversion deteriorates
- DSO or inventory growth materially exceeds revenue growth
- repeated capital raises with weak per-share economics
- auditor resignation/downgrade/restatement/material weakness
- insider selling or pledged shares during promotion
- margin far above peers without operating explanation
- regulatory gate presented as realized economics
- backlog counted before binding conversion evidence

## Green Flag Inventory

Name offsetting positives:

- net cash balance sheet
- Big 4 or strong auditor with stable tenure
- clean OCF conversion
- binding backlog with delivery history
- customer confirmation from official counterparty source
- insider ownership with limited selling
- low dilution and no near-term maturity wall
- paid capacity reservations or take-or-pay commitments
- transparent segment reporting

## Integration With Valuation

Short-seller risk must affect the report:

- A/B grade: mention as financial-quality support
- C grade: discount multiple, reduce position size, or require milestone
  confirmation
- D/F grade: avoid high-conviction target unless the issue is resolved

Also state the most plausible activist-short attack narrative in one sentence.
If the company is clean, the sentence should explain why that narrative is weak.

Do not bury material red flags only in `Risk Factors`; place them where they affect
business logic, order quality, debt safety, or valuation.
