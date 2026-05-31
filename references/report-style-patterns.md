# Report Style Patterns

This file captures the output style learned from the user's recent reports
without treating those reports as factual evidence.

## Target Style

The report should read like one analyst explaining a stock to an investor:

- the user-requested report language
- clear thesis tension in the opening
- outside thesis replay when outside articles shaped the research path
- opportunity archetype routing before section emphasis
- demand expansion, scaling difficulty, bottleneck scarcity, and
  commercialization visibility for high-conviction theses
- concrete numbers
- inline arithmetic
- visible source markers for material numbers
- current-market-implied expectations before the analyst target
- profit-to-cash-flow quality before valuation confidence
- compact decision scorecard summary where it sharpens the trade conclusion
- compact tables only when they reduce ambiguity
- direct conclusion
- final trade plan

Avoid sounding like four separate modules stitched together.

## Opening Rule

Start with the current investment tension:

The first sentence should explain what is being repriced or disputed now.
Founding year, headquarters, and listing venue belong after that sentence.

Do not open with static corporate genealogy.

If outside research or user notes motivated the ticker, the opening should say
what market question those sources raised, then immediately separate verified
facts from unverified narrative.

## Readability Standard

A final report must not read like an audit log. The object graph may contain
labels such as `verified_fact`, `inference`, and `scenario_assumption`, but final
prose should translate those labels into readable paragraphs.

Use this paragraph pattern:

```text
claim -> evidence -> mechanism -> investment judgment
```

The source marker should support the sentence, not replace the sentence. Avoid
long runs of colon labels such as `Verified fact:`, `Inference:`, `Unanswered
question:`, and `ArticleThesisMap note:`. Those labels are useful internally, but
heavy use makes the memo hard to read and too compressed.

Preferred final prose:

```text
Revenue growth matters only if it converts into cash after working capital and
capex. The latest filing shows revenue acceleration, but OCF remains negative
because inventory and receivables consumed cash [filing]. That means the growth
story is still investable only as an order-conversion thesis, not yet as an owner
cash-flow thesis.
```

Weak final prose:

```text
Verified fact: revenue increased. Inference: growth is positive. Data gap: FCF.
```

Use short labels only inside compact tables, scorecards, or blocked-conclusion
notes. The main body should use complete causal paragraphs.

## Output Depth Standard

A full report should be materially deeper than a summary. If enough evidence is
available, target roughly 18,000 to 35,000 visible characters for a full report.
A report below that range is acceptable only when source access is genuinely
blocked, and it must say which sections are blocked and why.

Depth should come from reasoning, not filler. Add detail where it changes the
investment conclusion:

- industry-chain context that explains the scarce node
- customer pain and why the customer pays
- order quality and order-to-revenue conversion
- capacity, utilization, capex, and ramp timing
- working capital, cash conversion, debt, and dilution
- current-market-implied expectation and re-rating condition
- falsification pattern and trade execution

Default paragraph counts for `full_report`:

- `Core Conclusion`: 3 to 5 dense paragraphs or a short decision block plus
  explanatory prose.
- `Why This Stock Exists Now`: at least 4 paragraphs.
- `Industry Chain And Bottleneck`: at least 5 paragraphs when the thesis is
  technical or policy-driven.
- `Company Position In The Chain`: at least 4 paragraphs.
- `Business Model Logic`: at least 5 paragraphs.
- `Scarcity And Moat Assessment`: at least 4 paragraphs plus a compact table if
  helpful.
- `Customers, Orders, And Commercialization Path`: at least 5 paragraphs.
- `Operations, Capacity, And Execution Quality`: at least 4 paragraphs.
- `Financial Quality, Assets, Debt, And Dilution`: at least 5 paragraphs.
- `Valuation And Market-Implied Expectation`: at least 5 paragraphs with inline
  arithmetic.
- `Catalysts, Risks, And Falsification`: at least 4 paragraphs.
- `Technical Structure And Trade Plan`: at least 3 paragraphs or a complete
  blocked setup.

Do not satisfy depth by adding generic background. A paragraph is useful only if
it contains at least one of: source-backed fact, mechanism, implication,
contradiction, blocker, or action judgment.

## Reference-Caliber Memo Assembly

A strong report should be assembled as one causal memo, not as a sequence of
filled headings. Before drafting, compress the research into a thesis kernel:

```text
repricing dispute -> demand shock -> industry constraint -> scarce node
-> issuer control point -> order or capacity proof -> cash conversion
-> current-implied expectation -> action grade cap -> trade execution
```

The kernel controls paragraph order. A section may contain background only when
that background makes the next link in the chain understandable. Background that
does not change demand, scarcity, order conversion, cash flow, valuation, or
trade action should be removed.

The report should create the same reading effect as a carefully written manual
memo:

- the reader understands why the stock matters before learning the full company
  profile
- the industry primer explains the bottleneck, not the whole industry
- the company section shows the control point in the value chain
- the order section grades what has converted from narrative into demand
- the operations section shows whether supply can meet that demand
- the financial section shows whether revenue becomes owner cash flow
- the valuation section shows what must go right for the current price to work
- the trade plan converts the thesis into size, entry, stop, trim, and
  invalidation

## Industry Primer Rule

Add a compact industry primer when the thesis depends on technical context,
policy structure, supply-chain architecture, or asset economics that a normal
investor may not already understand.

The primer must answer only four items:

1. what the bottleneck technology or policy mechanism does
2. why that mechanism became more important now
3. where money flows through the chain
4. which node controls price, delivery, reliability, compliance, or yield

The primer is not a textbook. It should end by locating the issuer at the scarce
node and by naming the first observable that would confirm or break the thesis.

## Reference-Caliber Quality Bar

A report is not complete merely because all headings exist. It must satisfy
these quality tests:

- the opening names the disputed repricing question, not a generic theme
- outside thesis paths are verified, rejected, or blocked before use
- the issuer is routed to a supported opportunity archetype or explicitly capped
- the business model explains the customer pain, the product, the capture
  mechanism, the bottleneck, and the observable that proves the thesis
- the opportunity test explains demand expansion, scaling difficulty,
  bottleneck scarcity, and commercialization visibility
- the operations section separates disclosed backlog from weaker order proxies
- the financial section reconciles net income to operating cash flow and
  explains working-capital movement, capex quality, SBC-adjusted FCF, and FCF
  per share
- the valuation section states what the current price already implies before
  presenting the analyst assumption
- the short-seller section names the plausible attack narrative even when the
  final grade is clean
- the technical section converts trend into entry, invalidation, and take-profit
  levels
- the decision scorecard states action grade and binding cap reason without
  numeric score averaging
- the final trade plan ties position size to evidence quality and stop distance
- the final report contains enough prose depth to explain mechanisms, not only
  list conclusions
- the final report avoids compressed audit-label style in the main body

## Layer Depth Standard

Each layer must contain a judgment, not only a description:

- Business layer: identify the structural bottleneck, value-capture mechanism,
  and falsification observable.
- Opportunity layer: classify the archetype and identify what makes the stock
  investable now.
- Operations layer: connect capacity, utilization, capex, customer funding,
  delivery cadence, and margin at scale.
- Customer/order layer: separate revenue, binding orders, funded reservations,
  framework agreements, pipeline, and management guidance.
- Financial layer: connect cash, debt, capex, working capital, dilution, and
  owner FCF.
- Valuation layer: show current-implied expectations, re-rating bridge, one
  primary method, and EV-to-equity-to-share bridge.
- Short-risk layer: state the activist-short attack narrative and the monitoring
  fact pattern that would strengthen it.
- Technical layer: turn monthly/weekly/daily structure into entry, stop, TP1,
  TP2, trim/add logic, and position size.
- Scorecard layer: separate business thesis strength from trade action grade.

The report should feel like an integrated investment memo. Do not let sections
become independent checklists.

## Section Rhythm

Use these default `full_report` sections in order:

1. Core Conclusion
2. Why This Stock Exists Now
3. Industry Chain And Bottleneck
4. Company Position In The Chain
5. Business Model Logic
6. Scarcity And Moat Assessment
7. Customers, Orders, And Commercialization Path
8. Operations, Capacity, And Execution Quality
9. Financial Quality, Assets, Debt, And Dilution
10. Valuation And Market-Implied Expectation
11. Catalysts, Risks, And Falsification
12. Technical Structure And Trade Plan

Do not expose module labels. Older section aliases may be accepted by validators
for legacy fixtures, but new full reports should use the mainline-driven
structure.

## Section Output Contract

Each section must output one decision-useful conclusion:

- `Core Conclusion`: stance, cap reason, position sizing range, and invalidation.
- `Why This Stock Exists Now`: the market variable that changed and the evidence
  that it changed.
- `Industry Chain And Bottleneck`: the scarce node and why it has pricing or
  availability power.
- `Company Position In The Chain`: whether the issuer is company alpha or only
  industry beta.
- `Business Model Logic`: value-capture mechanism and falsification observable.
- `Scarcity And Moat Assessment`: replication difficulty and duration of the
  scarcity.
- `Customers, Orders, And Commercialization Path`: order quality grade and
  valuation usability.
- `Operations, Capacity, And Execution Quality`: ramp bottleneck and date by
  which failure becomes visible.
- `Financial Quality, Assets, Debt, And Dilution`: whether the equity owner gets
  cash flow after capex, working capital, dilution, and senior claims.
- `Valuation And Market-Implied Expectation`: what the current price already
  requires and what must be revised for upside.
- `Catalysts, Risks, And Falsification`: monitorable events that raise or lower
  conviction.
- `Technical Structure And Trade Plan`: trade stance, entry, stop, TP1, TP2,
  trim/add logic, and size.

## Section Exit Judgment

Every major section should close with a short judgment sentence. Use the same
language as the report. The sentence should say what the section changes about
the investment view.

Pattern:

```text
Section judgment: this evidence strengthens / weakens / caps the thesis because
[specific mechanism].
```

Do not overuse this label if it makes the prose stiff. The important rule is
that each section ends with a decision-useful judgment.

## Business Logic Prose

Strong reports explain:

- old value driver
- new value driver
- structural reason for transition
- customer or policy evidence
- operating bottleneck
- opportunity archetype and four-part opportunity test result
- 3-5 year end state

Weak reports merely list products, markets, and catalysts.

The business section must close with one sentence that names the value driver,
current stage, and key observable.

## Anti-Checklist Reconstruction Pass

After a draft exists, run this repair pass before final output:

1. Remove any paragraph that could apply to most peers in the same industry.
2. Move industry context ahead of company description only when it explains the
   bottleneck.
3. Convert every generic catalyst into a dated or source-linked observable.
4. Convert every order claim into an order-quality level and revenue-conversion
   path.
5. Convert every valuation multiple into a current-implied expectation and one
   re-rating condition.
6. Convert every risk into either a thesis-breaker, a valuation haircut, or a
   position-size cap.
7. Convert every technical comment into an action or a blocked setup.
8. Expand any one-paragraph section that compresses evidence, mechanism,
   valuation, and action into the same paragraph.
9. Replace repeated audit labels with readable prose unless the label marks a
   blocked conclusion.

A report that still reads like headings filled with facts has failed this pass.

## Inline Arithmetic

Use prose math:

State the variables, operator, result, and interpretation in the sentence.

Do not hide all math in tables.

## Valuation Voice

State why the chosen valuation denominator matches the business mechanism and
current market-pricing mechanism. Do not average DCF, P/E, EV/EBITDA, P/S, and
P/B into a single target.

## Short-Seller Risk Style

For clean companies, short-seller risk is a paragraph, not a forensic appendix.
For risky companies, name the specific issue and valuation impact.

The short-seller paragraph should identify the risk type, evidence, and effect
on valuation or position sizing. Avoid dashboard-style scoring unless serious
red flags justify an expanded forensic section.

## Decision Scorecard Style

Use the scorecard as a compact decision summary, not as a separate model. The
reader should see why the grade is capped:

- strong company quality but weak cash conversion
- improving operations but valuation already prices the upside
- good fundamental setup but overextended momentum
- clean short-seller risk but unresolved share-count bridge

The scorecard must use an action grade and binding cap reason. Do not average
numeric scores or let a clean category hide a blocking gap.

## Technical Style

Technical analysis must end in a trade decision:

- entry
- stop
- TP1
- TP2
- if no setup, observe and wait

Technical analysis must translate the pattern into levels, invalidation, and
trade action. Vague mixed-signal commentary is not sufficient.

## Banned Or Weak Patterns

Avoid:

- "overall"
- "notably"
- "therefore"
- "multi-dimensional analysis"
- "probability-weighted fair value"
- "three-method average"
- "data sufficiency note"
- large generic risk matrices
- conclusion without trade plan
- technical analysis without price levels
- target price without share count and net debt bridge
- one-paragraph sections in a full report
- repeated audit-label sentences in the main body
- a report that has headings but not enough explanatory prose

## Data Gap Style

If data is missing:

State the blocked conclusion, the specific missing input, and the source that
would resolve it.

Do not smooth over the gap with vague language.