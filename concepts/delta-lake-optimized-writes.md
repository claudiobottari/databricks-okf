---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e01129cf86b61d806a66b5acb08ed93312bff35f7e86bd78015ab04b47a9a3ae
  pageDirectory: concepts
  sources:
    - best-practices-delta-lake-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-optimized-writes
    - DLOW
    - Delta Lake OPTIMIZE
    - Optimized Writes
    - optimized writes
  citations:
    - file: best-practices-delta-lake-databricks-on-aws.md
title: Delta Lake Optimized Writes
description: A feature that reduces the number of small files produced by MERGE operations on partitioned tables by reducing the number of files each shuffle task writes across multiple partitions
tags:
  - delta-lake
  - writes
  - optimization
timestamp: "2026-06-19T22:12:57.143Z"
---

## Delta Lake Optimized Writes

**Delta Lake Optimized Writes** is a feature that reduces the number of small files produced by write-heavy operations, particularly the Merge command on partitioned tables. By aggregating output files per partition, optimized writes improve write performance and help maintain a clean file layout. ^[best-practices-delta-lake-databricks-on-aws.md]

### Overview

When a `MERGE` operation runs on a partitioned [Delta Lake Table](/concepts/delta-lake-table.md), each shuffle task can write multiple files across multiple partitions. This can result in a much larger number of small files than the number of shuffle partitions, creating a performance bottleneck during writes and degrading subsequent reads. ^[best-practices-delta-lake-databricks-on-aws.md]

Optimized writes mitigate this by co-locating output files per partition before committing them, reducing the total file count. The feature is especially beneficial for partitioned tables where the number of output partitions is high relative to the shuffle parallelism. ^[best-practices-delta-lake-databricks-on-aws.md]

### When to Enable

Enable optimized writes when running `MERGE` on partitioned tables that produce a large number of small output files. The feature is configurable via the Spark session configuration `spark.sql.adaptive.coalescePartitions.enabled` or the Delta-specific `delta.autoOptimize.optimizeWrite` table property. ^[best-practices-delta-lake-databricks-on-aws.md]

Databricks automatically tunes file sizes based on table size, using smaller files for smaller tables and larger files for larger tables. Optimized writes work in concert with this auto‑tuning to keep file sizes within a healthy range. ^[best-practices-delta-lake-databricks-on-aws.md]

### Benefits

- **Reduced file count**: Fewer small files means less metadata overhead and faster file listing during reads. ^[best-practices-delta-lake-databricks-on-aws.md]
- **Better write performance**: By avoiding the bottleneck of writing many small files from many shuffle tasks, `MERGE` completes more quickly. ^[best-practices-delta-lake-databricks-on-aws.md]
- **Improved maintainability**: A smaller number of files makes subsequent OPTIMIZE and VACUUM operations more efficient. ^[best-practices-delta-lake-databricks-on-aws.md]

### Relationship with Other Optimizations

Optimized writes are part of a broader set of best practices for Delta Lake Merge performance. Databricks also recommends:

- [Low Shuffle Merge](/concepts/low-shuffle-merge.md) — an alternative merge implementation that preserves existing data layout optimizations (such as [Liquid Clustering](/concepts/liquid-clustering.md)) on unmodified data. ^[best-practices-delta-lake-databricks-on-aws.md]
- Regular OPTIMIZE and VACUUM operations, which are automatically run by Predictive Optimization on Unity Catalog managed tables. ^[best-practices-delta-lake-databricks-on-aws.md]

### Sources

- best-practices-delta-lake-databricks-on-aws.md

# Citations

1. [best-practices-delta-lake-databricks-on-aws.md](/references/best-practices-delta-lake-databricks-on-aws-aef26632.md)
