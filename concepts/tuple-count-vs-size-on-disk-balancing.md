---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9525e8b8a188ccb4fcd7efd1f0d6d16d33e4a60bbf3d4ac0012b9f4ca94247aa
  pageDirectory: concepts
  sources:
    - optimize-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tuple-count-vs-size-on-disk-balancing
    - TVSB
  citations:
    - file: optimize-databricks-on-aws.md
title: Tuple-count vs size-on-disk balancing
description: The distinction between optimizations that balance files by number of records (Z-ordering) versus those that balance by byte size (bin-packing), and the implications for task skew.
tags:
  - delta-lake
  - optimization
  - data-engineering
  - performance
timestamp: "2026-06-19T19:51:22.580Z"
---

# Tuple-count vs size-on-disk balancing

**Tuple-count vs size-on-disk balancing** refers to the trade-off between two different optimization objectives when performing data file compaction operations in [Delta Lake](/concepts/delta-lake.md). Depending on the optimization technique used, the resulting data files may be balanced by the number of rows (tuples) they contain or by their physical size on disk, and these two measures are not always aligned.

## Overview

When optimizing data layout in Delta Lake, the goal is to produce evenly-sized files to improve query performance and resource utilization. However, the two primary optimization methods—[bin-packing optimization](/concepts/bin-packing-optimization-delta-lake.md) and [Z-Ordering](/concepts/z-ordering-delta-lake.md)—balance files according to different metrics. While tuple count and file size are most often correlated, they can diverge, leading to skew in optimization task times. ^[optimize-databricks-on-aws.md]

## Bin-packing optimization

Bin-packing optimization produces evenly-balanced data files with respect to their **size on disk**, but not necessarily the number of tuples per file. This means that after bin-packing, files will have similar byte sizes, but may contain different numbers of rows if the data within those rows varies in width. ^[optimize-databricks-on-aws.md]

Bin-packing is idempotent: running it twice on the same data set has no effect on the second run. ^[optimize-databricks-on-aws.md]

## Z-Ordering

Z-Ordering produces evenly-balanced data files with respect to the **number of tuples**, but not necessarily data size on disk. This means that after Z-Ordering, files will contain similar numbers of rows, but may have different byte sizes if the data values vary in storage requirements. ^[optimize-databricks-on-aws.md]

Z-Ordering is **not idempotent** but operates incrementally. The time Z-Ordering takes is not guaranteed to decrease over multiple runs. However, if no new data was added to a partition that was just Z-Ordered, running Z-Ordering again on that partition has no effect. ^[optimize-databricks-on-aws.md]

## Practical implications

The divergence between tuple-count balancing and size-on-disk balancing can cause skew in optimization task times. When the two measures are correlated, optimization runs efficiently. When they diverge—for example, due to variable-length columns or skewed data distributions—some tasks may take significantly longer than others, leading to uneven resource utilization. ^[optimize-databricks-on-aws.md]

## Related concepts

- [Delta Lake OPTIMIZE](/concepts/delta-lake-optimized-writes.md) — The command that triggers file compaction
- [Data file compaction](/concepts/delta-lake-file-compaction.md) — The general process of merging small files into larger ones
- Data skew — A condition that can cause tuple-count and size-on-disk to diverge
- Query performance optimization — The broader goal of file balancing

## Sources

- optimize-databricks-on-aws.md

# Citations

1. [optimize-databricks-on-aws.md](/references/optimize-databricks-on-aws-342a11f5.md)
