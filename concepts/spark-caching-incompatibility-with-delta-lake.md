---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e08a0ccea8b5f61d922b92e398db42dea7578ffc6dcd2076481676778648ab9f
  pageDirectory: concepts
  sources:
    - best-practices-delta-lake-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spark-caching-incompatibility-with-delta-lake
    - SCIWDL
  citations:
    - file: best-practices-delta-lake-databricks-on-aws.md
title: Spark Caching Incompatibility with Delta Lake
description: Databricks recommends against using Spark caching with Delta Lake because it loses data skipping benefits and can become stale if the table is accessed via different identifiers.
tags:
  - delta-lake
  - spark
  - caching
timestamp: "2026-06-18T14:31:46.299Z"
---

# Spark Caching Incompatibility with Delta Lake

**Spark Caching Incompatibility with Delta Lake** refers to a set of documented issues that arise when using Apache Spark’s DataFrame caching mechanism with Delta Lake tables. Databricks explicitly recommends against using Spark caching for Delta Lake workloads because it can lead to incorrect query results and lost performance optimizations.

## Reasons Not to Use Spark Caching with Delta Lake

Databricks advises against using Spark caching with Delta Lake for two primary reasons: ^[best-practices-delta-lake-databricks-on-aws.md]

1. **Loss of data skipping** – When a DataFrame is cached, any additional filters applied on top of the cached data cannot leverage data skipping optimizations. Delta Lake normally uses file‑level statistics (min/max values) to skip irrelevant data files during query planning. Caching short‑circuits this mechanism, potentially reading more data than necessary and degrading query performance. ^[best-practices-delta-lake-databricks-on-aws.md]

2. **Stale cached data** – The data that gets cached might not be updated if the table is accessed using a different identifier (for example, reading the same underlying data through a different path or table alias). Delta Lake’s transaction log guarantees that every read returns the most recent committed version of the data, but a cached DataFrame holds a snapshot of the data at the time the cache was built. If the table is modified and later read through a different identifier, the cache may serve an outdated result. ^[best-practices-delta-lake-databricks-on-aws.md]

## Recommended Alternatives

Instead of relying on Spark caching, Databricks recommends using Delta Lake’s native optimizations:

- **Use Unity Catalog managed tables** and enable [predictive optimization](/concepts/delta-lake-predictive-optimization.md), which automatically runs `OPTIMIZE` and `VACUUM` commands to compact files and maintain performance. ^[best-practices-delta-lake-databricks-on-aws.md]
- **Use liquid clustering** to improve data layout for common query patterns. ^[best-practices-delta-lake-databricks-on-aws.md]
- **Frequently run `OPTIMIZE`** to compact small files into larger ones, improving read throughput. ^[best-practices-delta-lake-databricks-on-aws.md]

## Related Considerations

Delta Lake tables always return the most up‑to‑date information, so there is no need to call `REFRESH TABLE` manually after changes. Unlike traditional Parquet tables on Spark, Delta Lake automatically tracks partitions and transaction history, making manual partition management and direct data file modifications unnecessary. ^[best-practices-delta-lake-databricks-on-aws.md]

## Sources

- best-practices-delta-lake-databricks-on-aws.md

# Citations

1. [best-practices-delta-lake-databricks-on-aws.md](/references/best-practices-delta-lake-databricks-on-aws-aef26632.md)
