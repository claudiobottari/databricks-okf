---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 997d551a05b83566efc31487b9d132e06b64ea4df8c24e3967982ffb5212d182
  pageDirectory: concepts
  sources:
    - best-practices-delta-lake-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-merge-performance-tuning
    - DLMPT
    - Delta Lake Performance Tuning
    - Delta Lake performance tuning
    - Optimizing Delta Lake Performance
    - delta-lake-merge-performance-optimization
    - DLMPO
    - Delta Lake merge optimization
  citations:
    - file: best-practices-delta-lake-databricks-on-aws.md
title: Delta Lake MERGE Performance Tuning
description: Techniques to reduce merge operation time including reducing search space, compacting files, controlling shuffle partitions, enabling optimized writes, and tuning file sizes
tags:
  - delta-lake
  - merge
  - performance
timestamp: "2026-06-19T22:12:47.225Z"
---

# Delta Lake MERGE Performance Tuning

**Delta Lake MERGE Performance Tuning** refers to a set of techniques and configuration best practices that reduce the execution time of `MERGE` operations on [Delta Lake](/concepts/delta-lake.md) tables. These optimizations focus on minimizing the search space for matches, improving data layout, controlling parallelism, and leveraging specialized execution modes.

## Overview

The `MERGE` operation (often used for upserts) can be expensive because it must scan the entire target table to find rows matching the source by default. Tuning strategies aim to limit this scan and reduce the overhead caused by small files, excessive shuffling, and suboptimal write patterns. ^[best-practices-delta-lake-databricks-on-aws.md]

## Reduce the Search Space for Matches

By default, the `merge` operation searches the entire [Delta Lake Table](/concepts/delta-lake-table.md) to find matches in the source table. Adding known constraints in the match condition can speed up the query by limiting the scan to only relevant partitions or files. For example, if the table is partitioned by `country` and `date` and you intend to update only the last day for a specific country, include:

```sql
events.date = current_date() AND events.country = 'USA'
```

This reduction not only improves performance but also lowers the chance of conflicts with other concurrent operations. See Isolation levels and write conflicts for more details. ^[best-practices-delta-lake-databricks-on-aws.md]

## Compact Files

If the data is stored in many small files, reading the data to search for matches becomes slow. Running OPTIMIZE compacts small files into larger ones, improving read throughput. Note that `OPTIMIZE` does not remove old files; to reclaim storage, run VACUUM. When using Unity Catalog, [Predictive optimization](/concepts/predictive-optimization-for-delta-lake.md) can automate both operations. ^[best-practices-delta-lake-databricks-on-aws.md]

## Control Shuffle Partitions for Writes

The `merge` operation shuffles data multiple times to compute and write updated records. The number of shuffle tasks is controlled by the Spark session configuration `spark.sql.shuffle.partitions`. Increasing this value increases parallelism but also generates a larger number of smaller output files. Tune this parameter to balance parallel execution with file size. ^[best-practices-delta-lake-databricks-on-aws.md]

## Enable Optimized Writes

For partitioned tables, `merge` can produce many more small files than the number of shuffle partitions, because each shuffle task may write multiple files into multiple partitions. Enabling [Optimized writes](/concepts/optimized-writes-for-partitioned-tables.md) reduces the number of files by coordinating writes, alleviating this bottleneck. ^[best-practices-delta-lake-databricks-on-aws.md]

## Tune File Sizes in the Table

Databricks automatically adjusts file sizes based on table size—smaller tables get smaller files, larger tables get larger files. This behavior can be further tuned via table properties. Proper file sizing helps both read and write performance during `MERGE`. See the documentation on tuning file sizes for details. ^[best-practices-delta-lake-databricks-on-aws.md]

## Use Low Shuffle Merge

[Low Shuffle Merge](/concepts/low-shuffle-merge.md) provides an optimized implementation of `MERGE` that delivers better performance for most common workloads. It also preserves existing data layout optimizations, such as [Liquid Clustering](/concepts/liquid-clustering.md), on unmodified data. When available, this should be the preferred execution mode for `MERGE`. ^[best-practices-delta-lake-databricks-on-aws.md]

## General Delta Lake Best Practices

Although not specific to `MERGE`, the following general recommendations apply to all Delta Lake workloads, including merge operations:

- Use [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md).
- Enable [Predictive optimization](/concepts/predictive-optimization-for-delta-lake.md) for automated compaction and vacuum.
- Prefer [Liquid Clustering](/concepts/liquid-clustering.md) for flexible data layout.
- Delete and recreate tables using `CREATE OR REPLACE TABLE` rather than manual delete.
- Remove legacy Delta configurations to allow new optimizations to take effect.
- Avoid Spark caching with Delta Lake, as it can prevent data skipping and return stale data.

^[best-practices-delta-lake-databricks-on-aws.md]

## Sources

- best-practices-delta-lake-databricks-on-aws.md

## Related Concepts

- OPTIMIZE
- VACUUM
- [Low Shuffle Merge](/concepts/low-shuffle-merge.md)
- [Optimized writes](/concepts/optimized-writes-for-partitioned-tables.md)
- [Liquid Clustering](/concepts/liquid-clustering.md)
- [Predictive optimization](/concepts/predictive-optimization-for-delta-lake.md)
- [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md)
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md)

# Citations

1. [best-practices-delta-lake-databricks-on-aws.md](/references/best-practices-delta-lake-databricks-on-aws-aef26632.md)
