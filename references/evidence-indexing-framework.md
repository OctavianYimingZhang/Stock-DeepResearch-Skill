# Evidence Indexing Framework

This reference defines evidence partitioning and metadata pruning for research
context control. It adapts data-warehouse pruning ideas to reduce context
pollution in stock research.

## Source Partition

Create `SourcePartition` objects before evidence extraction. A source partition
is a routing slice, not a factual claim.

Required metadata:

- source snapshot id
- document section
- page or line range, or explicit gap
- source type
- period
- candidate object type
- candidate metric name or gap
- freshness status
- estimated materiality

Use source partitions to decide which parts of long filings, transcripts, and
presentations should be read for the current task.

## Evidence Partition

Create `EvidencePartition` objects after extraction. An evidence partition is
not a separate factual source. It is metadata that tells the agent which
evidence and claims to read for a specific analysis task.

Required metadata:

- company id
- fiscal period
- source type
- source date
- object type
- metric name or gap
- materiality
- freshness status
- source strength
- claim count
- conflict count

## Pruning Rules

Use `SourcePartition` metadata before loading long documents:

- debt source partitions read debt, lease, maturity, covenant, interest, cash,
  and dilution sections first
- order source partitions read revenue, backlog, purchase obligation, customer,
  counterparty, and conversion sections first
- valuation source partitions read metric, order, debt, dilution, asset, peer
  multiple, and current-price sections first
- short-risk source partitions read governance, cash conversion, related party,
  receivable, inventory, auditor, dilution, legal, and regulatory sections first
- technical source partitions read OHLCV, chart date, split or dividend
  adjustment, support, resistance, and volume sections first

Use `EvidencePartition` metadata after extraction:

- debt analysis reads debt, lease, maturity, covenant, interest, cash, and
  dilution partitions first
- order analysis reads revenue, backlog, purchase obligation, customer,
  counterparty, and conversion partitions first
- valuation reads metrics, orders, debt, dilution, asset, peer multiple, and
  current-price partitions first
- short-risk analysis reads governance, cash conversion, related party,
  receivable, inventory, auditor, dilution, legal, and regulatory partitions
  first
- technical analysis reads OHLCV, chart date, split or dividend adjustment, gap,
  support, resistance, and volume partitions first

If a source partition is stale, do not use it as current evidence. If an
evidence partition shows high conflict count or stale freshness, resolve that
before using it for valuation or trade decisions.

## Source Priority With Partitions

When two evidence partitions conflict:

1. issuer filing or regulator source
2. issuer transcript or formal guidance
3. government, customer, partner, court, or exchange source
4. market-data source
5. high-quality secondary source

Use the higher-priority partition unless it is stale and a later primary source
supersedes it.

## Context Budget Rule

Do not load all source text by default. Load:

- the highest-materiality source partition for the current section
- the evidence partition tied to the selected source partition
- the most recent primary source for the same metric or claim
- one contradicting or qualifying partition if conflict exists
- the linked source snapshot for lineage

If the needed partition does not exist, create a `DataGap` rather than filling
the missing fact from narrative memory.

## Report Implication

Every report section should be traceable to the partitions it used. This makes
the final report shorter, cleaner, and less likely to mix unrelated source
material.
