---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e4e7bac87e24bb077b50778a8eaabe7278c8ca3182da5288a3b0c4a36b530ae1
  pageDirectory: concepts
  sources:
    - best-practices-delta-lake-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - low-shuffle-merge
    - LSM
  citations:
    - file: best-practices-delta-lake-databricks-on-aws.md
title: Low Shuffle Merge
description: An optimized implementation of MERGE in Delta Lake that provides better performance for most common workloads and preserves existing data layout optimizations like liquid clustering on unmodified data
tags:
  - delta-lake
  - merge
  - optimization
timestamp: "2026-06-19T22:12:51.346Z"
---

# Low Shuffle Merge

**Low Shuffle Merge** is an optimized implementation of the `MERGE` operation in Delta Lake that provides better performance for most common workloads while preserving existing data layout optimizations on unmodified data. ^[best-practices-delta-lake-databricks-on-aws.md]

## Overview

The standard `MERGE` operation in [Delta Lake](/concepts/delta-lake.md) shuffles data multiple times to compute and write updated data, which can become a performance bottleneck. Low Shuffle Merge addresses this by using a more efficient shuffle strategy that reduces data movement across the cluster. ^[best-practices-delta-lake-databricks-on-aws.md]

## Key Benefits

Low Shuffle Merge offers two primary advantages over the standard `MERGE` implementation:

- **Improved performance**: It delivers better performance for most common merge workloads by reducing the amount of data that must be shuffled across the network. ^[best-practices-delta-lake-databricks-on-aws.md]
- **Preserves data layout**: It maintains existing data layout optimizations, such as [Liquid Clustering](/concepts/liquid-clustering.md), on rows that are not modified by the merge operation. This means subsequent queries against unmodified data continue to benefit from optimized file layouts. ^[best-practices-delta-lake-databricks-on-aws.md]

## When to Use

Low Shuffle Merge is recommended as a general improvement to the standard merge operation. It provides particular value in the following scenarios: ^[best-practices-delta-lake-databricks-on-aws.md]

- Tables that have undergone OPTIMIZE or compaction, where preserving the optimized layout on unmodified rows is important.
- Workloads where a small portion of the table is updated while most data remains unchanged.
- Tables using [Liquid Clustering](/concepts/liquid-clustering.md), where maintaining the clustered layout on unchanged data improves query performance.

## Relationship to Other Performance Optimizations

Low Shuffle Merge complements other Delta Lake performance optimization techniques. For best merge performance, consider combining Low Shuffle Merge with: ^[best-practices-delta-lake-databricks-on-aws.md]

- **Reducing the search space for matches**: Adding known constraints in the match condition (e.g., partition filters) to limit the data scanned.
- **Compacting files**: Using `OPTIMIZE` to consolidate small files into larger ones.
- **Controlling shuffle partitions**: Tuning `spark.sql.shuffle.partitions` to balance parallelism and output file count.
- **Enabling optimized writes**: Reducing the number of small files produced during merge operations on partitioned tables.
- **Tuning file sizes**: Leveraging Databricks' automatic file size tuning.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer providing ACID transactions and merge operations
- [MERGE Statement](/concepts/delta-lake-dml-statements.md) — The SQL statement that Low Shuffle Merge optimizes
- [Liquid Clustering](/concepts/liquid-clustering.md) — A data layout optimization preserved by Low Shuffle Merge
- OPTIMIZE — The command used to compact and optimize data files
- Predictive Optimization — Automatic optimization for Unity Catalog managed tables

## Sources

- best-practices-delta-lake-databricks-on-aws.md

# Citations

1. [best-practices-delta-lake-databricks-on-aws.md](/references/best-practices-delta-lake-databricks-on-aws-aef26632.md)
