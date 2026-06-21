---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c4d7af82a6dfbbccb62261c83d2eabe4d061c6d95dca64959f6c57d974edef14
  pageDirectory: concepts
  sources:
    - best-practices-delta-lake-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-general-best-practices
    - DLGBP
    - Delta Lake Best Practices
    - Delta Lake best practices
  citations:
    - file: best-practices-delta-lake-databricks-on-aws.md
title: Delta Lake General Best Practices
description: High-level recommendations for Delta Lake including Unity Catalog managed tables, predictive optimization, liquid clustering, and safe table replacement patterns.
tags:
  - delta-lake
  - best-practices
  - databricks
timestamp: "2026-06-19T09:09:37.422Z"
---

Here is the wiki page for "Delta Lake General Best Practices", written solely from the provided source material.

---

## Delta Lake General Best Practices

**Delta Lake General Best Practices** are a set of recommendations for configuring and using [Delta Lake](/concepts/delta-lake.md) tables on Databricks to maximize performance, reliability, and maintainability.

### Overview

These practices cover table management, file compaction, caching, and query optimization. They apply to most Delta Lake workloads and help avoid common pitfalls related to legacy configurations and manual data operations. ^[best-practices-delta-lake-databricks-on-aws.md]

### General Recommendations

Databricks recommends the following as a baseline for any Delta Lake workload:

- Use [Unity Catalog](/concepts/unity-catalog.md) managed tables. These provide centralized governance and automatic optimization.
- Enable predictive optimization, which automatically runs `OPTIMIZE` and `VACUUM` on Unity Catalog managed tables.
- Use liquid clustering for table layout. See [Use liquid clustering for tables](/concepts/liquid-clustering.md).
- When deleting and recreating a table in the same location, always use a `CREATE OR REPLACE TABLE` statement. ^[best-practices-delta-lake-databricks-on-aws.md]

### Remove Legacy Delta Configurations

When upgrading to a new Databricks Runtime version, remove most explicit legacy Delta configurations from Spark configurations and table properties. Legacy configurations can prevent new optimizations and default values introduced by Databricks from being applied to migrated workloads. ^[best-practices-delta-lake-databricks-on-aws.md]

### Compact Files

Frequently run the `OPTIMIZE` command to compact small files. This improves read throughput. Note that `OPTIMIZE` does not remove old files; to remove them, run the `VACUUM` command. ^[best-practices-delta-lake-databricks-on-aws.md]

| Action | Command |
|--------|---------|
| Compact small files | `OPTIMIZE` |
| Remove old/obsolete files | `VACUUM` |

### Do Not Use Spark Caching with Delta Lake

Databricks does not recommend using Spark caching (e.g., `.cache()` or `.persist()`) for Delta Lake tables because:

- You lose any data skipping that could come from additional filters added on top of the cached `DataFrame`.
- The cached data might not be updated if the table is accessed using a different identifier. ^[best-practices-delta-lake-databricks-on-aws.md]

### Differences Between Delta Lake and Parquet on Apache Spark

Delta Lake handles several operations automatically that were traditionally performed manually with Parquet. You should never perform these manually:

| Operation Delta Lake handles | Do not do manually |
|------------------------------|--------------------|
| **`REFRESH TABLE`** | Not needed. Delta Lake tables always return the most up-to-date information. |
| **Add and remove partitions** | Do not run `ALTER TABLE [ADD\|DROP] PARTITION` or `MSCK`. Delta Lake tracks partitions automatically. |
| **Load a single partition** | Do not read a partition directly (e.g., `spark.read.format("parquet").load("/data/date=2017-01-01")`). Use a `WHERE` clause for data skipping instead. |
| **Modify data files** | Do not directly modify, add, or delete Parquet data files in a [Delta Lake Table](/concepts/delta-lake-table.md). This can cause data loss or corruption. |

^[best-practices-delta-lake-databricks-on-aws.md]

### Improve Performance for Delta Lake Merge

To reduce the time it takes for `MERGE` operations, consider the following approaches:

- **Reduce the search space for matches**: Add known constraints in the match condition (e.g., `events.date = current_date() AND events.country = 'USA'`) so the search only examines relevant partitions. This also reduces the chances of conflicts with other concurrent operations. ^[best-practices-delta-lake-databricks-on-aws.md]
- **Compact files**: If data is stored in many small files, reading the data to search for matches becomes slow. Compact small files into larger files to improve read throughput. ^[best-practices-delta-lake-databricks-on-aws.md]
- **Control the shuffle partitions for writes**: The `merge` operation shuffles data multiple times. The number of shuffle partitions is controlled by the Spark session configuration `spark.sql.shuffle.partitions`. Increasing this value increases parallelism but also generates more smaller data files. ^[best-practices-delta-lake-databricks-on-aws.md]
- **Enable optimized writes**: For partitioned tables, `merge` can produce a much larger number of small files than the number of shuffle partitions. Enable optimized writes to reduce the number of files. ^[best-practices-delta-lake-databricks-on-aws.md]
- **Tune file sizes**: Databricks automatically tunes file sizes based on table size, using smaller files for smaller tables and larger files for larger tables. ^[best-practices-delta-lake-databricks-on-aws.md]
- **Low Shuffle Merge**: An optimized implementation of `MERGE` that provides better performance for most common workloads and preserves existing data layout optimizations (such as liquid clustering) on unmodified data. ^[best-practices-delta-lake-databricks-on-aws.md]

### Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- Optimize command
- [Vacuum command](/concepts/vacuum-command-databricks.md)
- [Liquid Clustering](/concepts/liquid-clustering.md)
- Predictive Optimization
- [Low Shuffle Merge](/concepts/low-shuffle-merge.md)

### Sources

- best-practices-delta-lake-databricks-on-aws.md

# Citations

1. [best-practices-delta-lake-databricks-on-aws.md](/references/best-practices-delta-lake-databricks-on-aws-aef26632.md)
