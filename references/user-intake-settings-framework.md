# User Intake And Settings Framework

This reference converts a vague research request into a controlled
`ResearchSettings` object, optional `UserHypothesis` objects, a source preflight,
and an `OutputView`.

## Core Rule

Runtime settings configure the run. They are not evidence.

User hypotheses are questions to test. They are not verified facts.

User-uploaded documents may become `SourceDocument` objects. User opinions may
only become `UserHypothesis` objects until supported or contradicted by
evidence.

## Presets

Use six preset entry points:

| Preset | Internal mode | Output view |
|---|---|---|
| Full Deep Research | `full_report` | `full_report` |
| Incremental Refresh | `incremental_refresh` | `incremental_refresh_summary` |
| Valuation Memo | `valuation_only` | `valuation_memo` |
| Short-Seller Audit | `short_risk_only` | `short_seller_attack_memo` |
| Trade Plan | `technical_only` | `trade_plan_only` |
| Evidence Gap Scan | `gap_scan` | `evidence_gap_report` |

Do not ask many questions up front. Capture the preset, ticker, exchange or
listing context if supplied, and any user focus areas. Ask follow-up questions
only when a missing input blocks a required conclusion.

## Required Settings

`ResearchSettings` must include:

- `report_language`
- `research_mode`
- `output_view`
- `source_policy`
- `valuation_strictness`
- `short_risk_threshold`
- `technical_requirement`
- `incremental_refresh_mode`
- `user_risk_budget_or_gap`
- `citation_detail_level`
- `interaction_level`

Default settings:

- source policy: primary public sources first
- historical reports: style only
- valuation strictness: block target if share count, net debt, senior claims,
  debt maturity, or order quality cannot be reconciled
- short-risk threshold: expand if grade is C or worse
- technical requirement: current chart data with chart date and adjusted status
- interaction level: ask only for blocking gaps

## Output Views

Supported views:

- `full_report`
- `valuation_memo`
- `short_seller_attack_memo`
- `trade_plan_only`
- `evidence_gap_report`
- `source_conflict_report`
- `incremental_refresh_summary`

All output views read the same object graph. The view changes projection only.
It must not change factual source of truth, valuation strictness, gate results,
or evidence lineage.

## Preflight Contract

Before source extraction, create a preflight state with:

- resolved or unresolved company identity
- security and listing context
- required source classes
- uploaded source classes
- expected public source classes to fetch
- likely blockers
- selected output view
- planned sections or omitted sections

Typical blockers:

- unresolved share count
- unresolved net debt
- missing debt maturity schedule for a levered company
- weak order evidence used for valuation
- stale or missing chart data for trade levels
- unresolved primary-source conflict

The agent may continue with non-blocked sections, but blocked targets, trade
levels, or high-conviction conclusions must remain blocked.

## Prompt Builder Contract

When settings are supplied through UI or configuration, build a canonical prompt
with these fields:

- ticker or company identifier
- exchange or listing context if supplied
- research mode
- output view
- horizon
- source policy
- valuation strictness
- short-risk threshold
- technical requirement
- interaction level
- user focus areas

The canonical prompt is a run instruction. It does not override evidence rules.

## Progress Status Contract

During a long run, show user-facing progress through object and gate status:

- Bronze source snapshots
- Source Index partitions
- Silver evidence and claims
- Gold analysis objects
- Report View projection
- gate results
- blockers

Do not expose hidden reasoning. Show only objects created, gates passed,
warnings, blockers, and source gaps.

## Follow-Up Actions

After a report, supported follow-up actions are:

- show evidence gaps
- refresh with a new source
- project valuation memo from the same graph
- project trade plan from the same graph after chart refresh
- project short-seller attack memo from the same graph
- export a source map or evidence ledger summary

Follow-up actions should reuse the existing graph through incremental refresh
unless the new source invalidates a high-materiality claim.
