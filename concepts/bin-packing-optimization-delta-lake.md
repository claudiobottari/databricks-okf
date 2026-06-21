---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3790bf00e3bcd17a73a9cbfddc144b6747b4e8563723aa951ceb0bd3d5a901d8
  pageDirectory: concepts
  sources:
    - optimize-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - bin-packing-optimization-delta-lake
    - BO(L
    - Bin-packing optimization
    - bin-packing optimization
  citations:
    - file: optimize-databricks-on-aws.md
title: Bin-packing optimization (Delta Lake)
description: An idempotent compaction technique that balances data files by size on disk, producing evenly-sized files without effect on re-run.
tags:
  - delta-lake
  - optimization
  - data-engineering
timestamp: "2026-06-19T19:51:46.795Z"
---

# Bin-packing optimization (Delta Lake)

**Bin-packing optimization** in [Delta Lake](/concepts/delta-lake.md) is a data compaction technique that coalesces many small files into fewer, larger files to improve query performance and reduce metadata overhead. It is one of the key operations performed by the OPTIMIZE command on Delta tables.

## Overview

Bin-packing optimization is _idempotent_: if you run it twice on the same data set, the second run has no effect. It produces evenly-balanced data files with respect to their size on disk, but not necessarily the number of tuples per file. The two measures are most often correlated. ^[optimize-databricks-on-aws.md]

The optimization works by grouping small files together and rewriting them as larger, optimally-sized files. This reduces the number of files that queries must scan and improves Delta Lake performance.

## Relationship to Z-Ordering

Bin-packing optimization differs from [Z-Ordering](/concepts/z-ordering-delta-lake.md) in several important ways:

- **Idempotence**: Bin-packing is idempotent; Z-Ordering is not idempotent, but operates incrementally. ^[optimize-databricks-on-aws.md]
- **File balance**: Bin-packing produces files balanced by size on disk; Z-Ordering produces files balanced by number of tuples. ^[optimize-databricks-on-aws.md]
- **Behavior on unchanged data**: If no new data was added to a partition that was just Z-Ordered, running Z-Ordering again on that partition has no effect. Z-Ordering time is not guaranteed to decrease over multiple runs. ^[optimize-databricks-on-aws.md]

While both operations may produce correlated file sizes and tuple counts, skew in optimize task times can occur when the two measures diverge. ^[optimize-databricks-on-aws.md]

## Use Cases

Bin-packing optimization is most beneficial for tables that accumulate many small files over time, such as:

- [Streaming data ingestion](/concepts/streamingdataset.md) that creates micro-batches
- Tables with frequent MERGE operations
- Tables that have not been optimized for a long period

The optimization reduces Delta table metadata size, improves query scan performance, and lowers the cost of reading data.

## Related Concepts

- Delta Lake maintenance — Regular operations to keep Delta tables performant
- [VACUUM command](/concepts/vacuum-command-databricks.md) — Removes old file versions after optimization
- Delta table partitioning — Affects how bin-packing operates across partitions
- [Z-Ordering](/concepts/z-ordering-delta-lake.md) — Complementary optimization for data clustering

## Sources

- optimize-databricks-on-aws.md

# Citations

1. [optimize-databricks-on-aws.md](/references/optimize-databricks-on-aws-342a11f5.md)
