---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: da93be694b80d2d62cb41c0eefd6a593bcb637329f2846ce001adcc8691be7ec
  pageDirectory: concepts
  sources:
    - best-practices-delta-lake-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - optimized-writes-for-partitioned-tables
    - OWFPT
    - Optimized writes
  citations:
    - file: best-practices-delta-lake-databricks-on-aws.md
title: Optimized Writes for Partitioned Tables
description: Technique to reduce the number of small output files produced by MERGE on partitioned tables by enabling optimized writes, addressing a common performance bottleneck.
tags:
  - delta-lake
  - partitioning
  - performance
timestamp: "2026-06-19T14:08:53.118Z"
---

# Optimized Writes for Partitioned Tables

**Optimized Writes for Partitioned Tables** is a performance optimization technique in [Delta Lake](/concepts/delta-lake.md) that reduces the number of small files produced during write operations on partitioned tables. This technique is particularly valuable for operations like `MERGE`, `UPDATE`, and `INSERT` on partitioned datasets, where standard shuffle-based writes can generate an excessive number of small files per partition.

## Overview

When writing to a partitioned table using operations such as `MERGE`, the shuffle mechanism in Apache Spark can produce a much larger number of small files than the configured number of shuffle partitions. This occurs because every shuffle task writes data into potentially multiple partitions, and each partition-targeted write can create its own file. For partitioned tables, this effect is amplified — each of the `spark.sql.shuffle.partitions` tasks may write one or more files to each partition it touches, resulting in a file count that scales as `(shuffle partitions) × (number of partitions written to)`.^[best-practices-delta-lake-databricks-on-aws.md]

## How Optimized Writes Work

Optimized writes mitigate the small-files problem by first sorting data within each partition and then writing it out in coalesced files. Instead of allowing every shuffle task to independently write files to each partition, optimized writes group the data for each partition and write a smaller number of larger files. This reduces the total file count and improves read performance for subsequent queries.^[best-practices-delta-lake-databricks-on-aws.md]

## When to Use Optimized Writes

Optimized writes are most beneficial for:

- **Partitioned tables** where `MERGE`, `UPDATE`, or `INSERT` operations occur frequently
- **Workloads producing many small files** — if the number of output files noticeably exceeds `spark.sql.shuffle.partitions`, optimized writes can help
- **Tables with many partitions** — the file explosion problem worsens as the number of target partitions increases
- **Performance-sensitive write paths** — reducing file count improves downstream read performance and lowers metadata overhead

Without optimized writes, partitioned `MERGE` operations can become a performance bottleneck because every shuffle task may write multiple files into multiple partitions.^[best-practices-delta-lake-databricks-on-aws.md]

## Configuration

Optimized writes can be enabled in [Delta Lake](/concepts/delta-lake.md) using one of the following settings:

| Setting | Scope | Description |
|---------|-------|-------------|
| `spark.databricks.delta.optimizeWrite.enabled` | Spark configuration | Enables optimized writes globally for all Delta Lake write operations |
| `delta.autoOptimize.optimizeWrite` | Table property | Enables optimized writes for a specific table |

The [Spark configuration] option applies to all tables in a session, while the [table property] option gives granular control per table.

## Relationship to Other File Size Optimization Techniques

Optimized writes work alongside other file size management strategies:

- **File size tuning**: Databricks automatically tunes file sizes based on table size, using smaller files for smaller tables and larger files for larger tables. Optimized writes complement this by ensuring that writes produce appropriately sized files from the start.
- **Low Shuffle Merge**: This optimized implementation of `MERGE` provides better performance for most common workloads while preserving existing data layout optimizations like [Liquid Clustering](/concepts/liquid-clustering.md). Optimized writes can further improve file size outcomes when used with Low Shuffle Merge.
- **`OPTIMIZE` command**: While optimized writes prevent file explosion at write time, `OPTIMIZE` is a maintenance operation that compacts existing small files. For actively written partitioned tables, using optimized writes reduces the need for frequent `OPTIMIZE` runs.

## Best Practices

1. **Enable optimized writes for partitioned tables** that experience frequent `MERGE` operations.
2. **Monitor file counts** in target partitions to identify when optimized writes are needed.
3. **Combine with file size tuning** — set appropriate shuffle partition counts alongside optimized writes for best results.
4. **Use predictive optimization** for [Unity Catalog](/concepts/unity-catalog.md) managed tables, which automatically runs `OPTIMIZE` and `VACUUM` commands.

## Related Concepts

- [Delta Lake merge optimization](/concepts/delta-lake-merge-performance-optimization.md) — Techniques for accelerating merge operations
- Partitioning strategies for Delta Lake — How partition design affects write performance
- [Liquid Clustering](/concepts/liquid-clustering.md) — Modern clustering approach that can reduce partitioning overhead
- [Predictive optimization](/concepts/predictive-optimization-for-delta-lake.md) — Automated maintenance that complements write-time optimizations
- File size tuning in Delta Lake — Strategies for managing file sizes
- [Low Shuffle Merge](/concepts/low-shuffle-merge.md) — Optimized merge implementation

## Sources

- best-practices-delta-lake-databricks-on-aws.md

# Citations

1. [best-practices-delta-lake-databricks-on-aws.md](/references/best-practices-delta-lake-databricks-on-aws-aef26632.md)
