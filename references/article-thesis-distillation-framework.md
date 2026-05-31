# Article Thesis Distillation Framework

This reference defines how outside research is used without turning it into
evidence. Outside articles, public analyst notes, user-supplied thesis notes,
and market writeups can reveal why a stock is being watched. They cannot support
material facts until the claims are verified through primary or high-quality
sources.

## Purpose

Use outside sources to reconstruct the market's thesis path:

```text
outside thesis -> causal chain -> claimed proof -> missing proof
-> primary-source check -> usable, rejected, or blocked thesis component
```

The goal is not to copy language. The goal is to identify which question the
market is trying to answer, which evidence would make that question investable,
and which parts of the market narrative fail when checked.

## ArticleThesisMap

Create one `ArticleThesisMap` for each outside thesis path that materially
influences the research direction.

Required fields:

- `source_title_or_locator`
- `source_type`
- `source_date_or_gap`
- `thesis_summary`
- `implied_causal_chain`
- `claimed_catalysts`
- `claimed_bottleneck`
- `claimed_order_or_customer_proof`
- `evidence_used_by_source`
- `evidence_missing`
- `unsupported_claims`
- `falsification_test`
- `usable_angle`
- `verification_status`

Classify `verification_status` as `confirmed`, `partially_supported`,
`unsupported`, `contradicted`, or `blocked_by_missing_source`.

## Market Thesis Map

When several outside sources discuss the same stock, do not summarize them one
by one in the final report. First build a market thesis map:

- what the bull side believes
- what the bear side believes
- what the market is already pricing
- which catalyst created attention
- which fact is repeatedly cited but weakly sourced
- which fact appears only in company filings or direct disclosures
- which fact would change valuation if confirmed

The market thesis map should not become a report section unless the user asks
for it. It is a research instrument that helps the final memo start from the
current repricing dispute.

## ThesisPathReplay

Build `ThesisPathReplay` after mapping outside theses:

- original outside logic
- primary-source reconstruction
- confirmed components
- rejected components
- unresolved claims
- improved thesis
- valuation implications that survive verification
- action-grade cap created by remaining uncertainty

Do not allow an outside claim to flow into valuation, order quality, short-risk
assessment, or technical trade planning unless it is independently supported or
clearly labeled as an unverified scenario assumption.

## Cross-Validation

Run two distillations:

1. Outside-in distillation:
   - start from outside thesis paths
   - extract the implied causal logic
   - list proof claims and missing proof
   - test material claims against filings, issuer materials, counterparty
     disclosures, regulator records, and reliable market data

2. Inside-out distillation:
   - start from primary and high-quality sources
   - independently build business logic, order quality, financial quality, and
     valuation inputs
   - compare the result with the outside thesis map

Only overlapping or explicitly resolved claims may support a high-conviction
conclusion. Contradictions create `ConflictResolution` or `DataGap` objects.

## Claim Use Rules

Use this rule set when deciding where an article claim can appear:

| Verification result | Final report use |
|---|---|
| confirmed by primary source | may support base-case thesis |
| confirmed by high-quality non-primary source only | may support qualified thesis language |
| partially supported | may support upside case or open question only |
| unsupported | omit or place in risk section |
| contradicted | state as rejected thesis path if material |
| blocked by missing source | mark as data gap and cap action grade if decision-critical |

The final report should never use article conviction as a substitute for source
quality.

## ArticleMapGate

The gate passes only when:

- at least one outside thesis path is extracted or the lack of outside research
  is marked as a gap
- each outside thesis lists missing evidence
- no outside thesis is used as fact without primary verification
- the surviving thesis path is selected, rejected, or blocked
- the final opening reflects the verified repricing dispute, not the article's
  rhetoric

If a stock is moving because of a narrative that cannot be verified, the report
can still discuss the narrative, but valuation confidence and position size must
be capped.

## Output Standard

Before drafting, produce one compact internal table:

| Claim | Outside thesis says | Source check says | Verdict | Report use |
|---|---|---|---|---|
| demand driver | filled or gap | filled or gap | confirmed / partial / rejected / blocked | base / upside / risk / omitted |
| bottleneck | filled or gap | filled or gap | confirmed / partial / rejected / blocked | base / upside / risk / omitted |
| commercial proof | filled or gap | filled or gap | confirmed / partial / rejected / blocked | base / upside / risk / omitted |
| valuation anchor | filled or gap | filled or gap | confirmed / partial / rejected / blocked | base / upside / risk / omitted |

The table is not normally shown. It exists to prevent unsupported market stories
from entering the final memo.