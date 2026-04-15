# Companion Skills — Extensions to the 5 Core Skills

The `stock-research-report` orchestrator can optionally dispatch these 6 additional Claude Skills from `anthropics/financial-services-plugins` (Apache-2.0). They are NOT required for the default deep-research workflow, but they strengthen specific phases or cover new use cases.

All 6 skills are drop-in SKILL.md files and can be installed to `~/.claude/skills/` directly.

---

## 1. `catalyst-calendar` — Forward Event Tracker

**Source**: `anthropics/financial-services-plugins/equity-research/skills/catalyst-calendar`

**When to use**: When the user asks "what's coming up for [TICKER]" or the orchestrator's 催化剂 block in `stock-analysis` needs a more rigorous events table with dated earnings, investor days, regulatory decisions, product launches, and macro events.

**What it adds beyond `stock-analysis` Block E (催化剂)**:
- Multi-company coverage universe support
- Macro event integration (Fed meetings, economic data, regulatory deadlines)
- Explicit Impact (H/M/L) × Our Positioning columns
- Weekly preview format for follow-up review cycles

**How to dispatch**:

```
Use the Skill tool with `skill: "catalyst-calendar"` and provide:
- Ticker(s)
- Time horizon (default: next 90 days)
- Macro events to include (Fed, CPI, jobs report, etc.)
```

**Where the output fits in the final report**: Expand 催化剂 block in `stock-analysis` with the catalyst-calendar output OR append as a standalone section before 交易计划 if the user wants a multi-ticker calendar.

---

## 2. `thesis-tracker` — Follow-Up Thesis Validation

**Source**: `anthropics/financial-services-plugins/equity-research/skills/thesis-tracker`

**When to use**: When the user says "is my DIOD thesis still intact", "update thesis for X", "thesis check", or "review my positions". This is a DIFFERENT use case from first-time deep research — it's for ongoing position management.

**What it does**:
- Load or define a thesis (pillars, risks, catalysts, target, stop-loss trigger)
- Log new data points with impact assessment (strengthens / weakens / neutralizes specific pillar)
- Update conviction level
- Falsification check — which pillars are now broken?

**How to dispatch**:

```
Use the Skill tool with `skill: "thesis-tracker"`. The user should provide:
- Existing thesis (or the previous deep research report file)
- New data point (earnings release, management change, competitor move, etc.)
- Current position and size
```

**Where this sits relative to `stock-research-report`**: `thesis-tracker` is run AFTER a prior deep research report exists. Output feeds back into the trade plan decisions:
- Pillars intact → maintain position
- Pillars partially broken → trim
- Pillars broken → exit and re-run full deep research

---

## 3. `earnings-preview` — Pre-Earnings Setup

**Source**: `anthropics/financial-services-plugins/equity-research/skills/earnings-preview`

**When to use**: 1-2 weeks before a company reports. The user asks "preview Q4 for [TICKER]" or "what to watch for [TICKER] earnings". This is a targeted pre-earnings skill — much narrower than a full deep research report.

**What it produces**:
- Consensus estimates (revenue, EPS, segment metrics) vs your model
- Sector-specific KPI checklist (SaaS: ARR/NRR/RPO; Retail: SSS/traffic/basket; Financials: NIM/credit; Healthcare: scripts/volumes; Industrials: backlog/book-to-bill)
- Bull / Base / Bear scenario table with implied stock moves
- Options-implied move vs historical move
- "Whisper number" callout if one exists
- Key questions for the earnings call

**How to dispatch**:

```
Use the Skill tool with `skill: "earnings-preview"` and provide:
- Ticker
- Reporting date/time (pre-market vs after-hours)
- Expected reporting quarter
- Any prior-quarter guidance points to check against
```

**Where this sits in the workflow**: Standalone skill — does NOT feed into `stock-research-report` orchestrator. Use it for pre-earnings positioning decisions.

---

## 4. `earnings-analysis` — Post-Earnings Update

**Source**: `anthropics/financial-services-plugins/equity-research/skills/earnings-analysis`

**When to use**: 0-3 days AFTER a company reports. Produces the "earnings update report" — beat/miss vs consensus, guidance delta, management tone, stock reaction analysis.

**What it produces**:
- Results table: actual vs consensus vs prior quarter
- Guidance changes with magnitude and direction
- Management tone assessment (confident / cautious / defensive / evasive)
- Key surprises (positive and negative)
- Stock reaction (actual move vs options-implied)
- Thesis update recommendation
- Updated target price (if materially changed)

**How to dispatch**:

```
Use the Skill tool with `skill: "earnings-analysis"` and provide:
- Ticker
- Reporting date
- Consensus estimates and actuals
- Any management guidance from the earnings call
- The prior `earnings-preview` report (if one exists) for explicit scorecard
```

**Integration pattern**: `earnings-preview` → company reports → `earnings-analysis` → `thesis-tracker` update → decide action (hold/trim/exit/add)

---

## 5. `comps-analysis` — Institutional Peer Comparable Analysis

**Source**: `anthropics/financial-services-plugins/financial-analysis/skills/comps-analysis`

**When to use**: When the user needs a standalone peer comps sheet (not part of a full report). This skill is **Excel/spreadsheet-oriented** and uses MCP data sources (S&P Kensho, FactSet, Daloopa) first, web search second.

**What it adds beyond `valuation-calculator`'s Phase 4 peer quartile table**:
- Excel output with formula-driven cells
- Full quartile statistics block (Max / 75th / Median / 25th / Min) per column
- Rule-of-40 automatic calculation for SaaS
- "Stats-worthy" column filtering (ratios/margins get stats, absolute sizes don't)
- Outlier identification (>1.5× IQR from median)

**How to dispatch**:

```
Use the Skill tool with `skill: "comps-analysis"` and provide:
- Target ticker
- Peer set (3-5 tickers) OR "suggest peers"
- Data source preference (MCP > Bloomberg > SEC EDGAR > web)
```

**Where the output fits**: Feeds into `valuation-calculator`'s Phase 4 as a pre-computed comparison table. The orchestrator can reference `comps-analysis` output when the user wants institutional-grade peer analysis.

---

## 6. `dcf-model` — Rigorous Excel DCF Builder

**Source**: `anthropics/financial-services-plugins/financial-analysis/skills/dcf-model`

**When to use**: When the user wants a full audit-grade DCF model in Excel with formula enforcement, 4-color conventions, and sensitivity tables — not just "here's a DCF number".

**What it adds beyond `valuation-calculator`'s DCF phase**:
- "Formulas over hardcodes" discipline — every projection cell MUST be a live Excel formula
- 4-color convention: blue = inputs, black = formulas, purple = same-tab link, green = cross-tab link
- 5×5 or 7×7 sensitivity table with center-cell sanity check
- Per-section user confirmation gates (data → revenue → margin → FCF → WACC → terminal → sensitivity)
- Cell comments with source/date/URL attached to each hardcode

**How to dispatch**:

```
Use the Skill tool with `skill: "dcf-model"` and provide:
- Ticker
- Historical financial data file (or fetch from SEC EDGAR)
- Base assumptions (revenue growth, terminal growth, WACC override if any)
```

**Where this sits relative to `valuation-calculator`**: `valuation-calculator` produces the NUMBER (target price from DCF as one input among many). `dcf-model` produces the AUDITABLE SPREADSHEET that a bank MD can review. Use `dcf-model` when the deliverable is a model file, not just a narrative report.

---

## Dispatch Decision Matrix

Use this table to decide which companion skill to invoke:

| User Ask | Primary Skill | Companion to Add |
|----------|--------------|------------------|
| "Deep research report on X" | `stock-research-report` (orchestrator) | Optional: `investor-council` if controversial |
| "What's coming up for X" | `catalyst-calendar` | — |
| "Is my X thesis still intact" | `thesis-tracker` | `earnings-analysis` if recent earnings |
| "Preview Q4 for X" | `earnings-preview` | — |
| "X reported, what do I do" | `earnings-analysis` | `thesis-tracker` for position action |
| "Compare X to peers" | `comps-analysis` | `valuation-calculator` for target |
| "Build a DCF model for X" | `dcf-model` | `valuation-calculator` for sanity check |
| "Second opinion on X" | `stock-research-report` with `investor-council` | — |
| "Bull/bear debate on X" | `investor-council` | — |

---

## Installation

All 6 anthropics skills install to `~/.claude/skills/`:

```bash
cd /path/to/financial-services-plugins
for skill in catalyst-calendar earnings-preview earnings-analysis thesis-tracker; do
  cp -r equity-research/skills/$skill ~/.claude/skills/$skill
done
for skill in comps-analysis dcf-model; do
  cp -r financial-analysis/skills/$skill ~/.claude/skills/$skill
done
```

**Verification**: After install, the Skill tool's auto-complete should show all 6 new skills. They are callable directly by name (`skill: "catalyst-calendar"`, etc.) without namespacing.

**License note**: `anthropics/financial-services-plugins` is Apache-2.0. Attribution preserved in the original SKILL.md files.
