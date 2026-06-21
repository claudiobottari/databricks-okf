---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 79c4a4f0be8aa7d1695cecb209cbd374b9196c45e76bbd4cd3c1f1e593da7c38
  pageDirectory: concepts
  sources:
    - best-practices-delta-lake-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spark-caching-anti-pattern-with-delta-lake
    - SCAWDL
    - spark-caching-incompatibility-with-delta-lake
    - SCIWDL
  citations:
    - file: best-practices-delta-lake-databricks-on-aws.md
title: Spark Caching Anti-pattern with Delta Lake
description: Databricks recommends against using Spark caching with Delta Lake because it loses data skipping benefits and can return stale data if the table is accessed via a different identifier
tags:
  - delta-lake
  - spark
  - caching
timestamp: "2026-06-19T22:12:49.000Z"
---

# Spark Caching Anti-pattern with Delta Lake

**Spark Caching Anti-pattern with Delta Lake** refers to the practice of using Spark's built-in caching mechanism (e.g., `.cache()`, `.persist()`) on DataFrames or tables that are backed by [Delta Lake](/concepts/delta-lake.md). Databricks explicitly advises against this practice because it can degrade query performance and lead to stale data issues. ^[best-practices-delta-lake-databricks-on-aws.md]

## Why Spark Caching Is Discouraged

Databricks recommends against using Spark caching with Delta Lake for two primary reasons:

1. **Loss of data skipping optimizations.** When a DataFrame is cached, any additional filters that are applied after caching cannot leverage Delta Lake's built-in data skipping (e.g., partition pruning or file-level statistics). The cached data is a static snapshot, so the engine cannot take advantage of metadata or statistics from the Delta transaction log to skip irrelevant files. ^[best-practices-delta-lake-databricks-on-aws.md]

2. **Stale data risk.** The cached data may become outdated if the underlying Delta table is modified through a different identifier or from a concurrent operation. Delta Lake tables are designed to always return the latest committed version; caching interferes with this by serving a frozen copy of the data that does not reflect subsequent writes or updates. ^[best-practices-delta-lake-databricks-on-aws.md]

## Recommended Alternatives

Instead of caching, Databricks recommends relying on Delta Lake's native optimizations:

- **Use predictive optimization** (for Unity Catalog managed tables) to automatically run `OPTIMIZE` and `VACUUM`, which reduce file count and improve read performance. ^[best-practices-delta-lake-databricks-on-aws.md]
- **Use liquid clustering** to co-locate similar data, accelerating queries without manual caching. ^[best-practices-delta-lake-databricks-on-aws.md]
- **Compact small files** with `OPTIMIZE` to improve read throughput. ^[best-practices-delta-lake-databricks-on-aws.md]
- **Use Delta Lake's transaction log** to maintain consistent snapshots; Delta Lake tables always return the most up-to-date information without requiring `REFRESH TABLE`. ^[best-practices-delta-lake-databricks-on-aws.md]
- **Use `WHERE` clauses for data skipping** instead of reading partitions directly. For example, `spark.read.table("<table-name>").where("date = '2017-01-01'")` allows Delta Lake to skip irrelevant files automatically. ^[best-practices-delta-lake-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Best Practices](/concepts/delta-lake-general-best-practices.md)
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md)
- Data Skipping in Delta Lake
- Predictive Optimization
- [Liquid Clustering](/concepts/liquid-clustering.md)
- OPTIMIZE Command
- [VACUUM Command](/concepts/vacuum-command-databricks.md)
- [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md)

## Sources

- best-practices-delta-lake-databricks-on-aws.md

# Citations

1. [best-practices-delta-lake-databricks-on-aws.md](/references/best-practices-delta-lake-databricks-on-aws-aef26632.md)
