---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c61a55533a60fd939eab116fc9bf6a1ae9b330e33975d6a4c387619b5be1ef89
  pageDirectory: concepts
  sources:
    - best-practices-delta-lake-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-vs-parquet-on-spark
    - DLVPOS
    - delta-lake-vs-parquet-on-apache-spark
    - DLVPOAS
  citations:
    - file: best-practices-delta-lake-databricks-on-aws.md
title: Delta Lake vs Parquet on Spark
description: "Key operational differences: Delta Lake automatically handles REFRESH TABLE, partition management, partition loading, and data file modifications, whereas Parquet on Spark requires manual management."
tags:
  - delta-lake
  - parquet
  - spark
timestamp: "2026-06-19T14:08:29.844Z"
---

# Delta Lake vs Parquet on Spark

**Delta Lake** and **Apache Parquet** are both file formats commonly used with Apache Spark, but they serve different purposes. Parquet is a columnar storage format optimized for analytical queries, while Delta Lake is an open‑source storage layer that adds transactional reliability, schema enforcement, and time‑travel capabilities on top of Parquet data files.^[best-practices-delta-lake-databricks-on-aws.md]

## Automatic management of table metadata

Delta Lake handles several operations automatically that require manual intervention when using raw Parquet tables on Spark.^[best-practices-delta-lake-databricks-on-aws.md]

### `REFRESH TABLE`

Because Delta Lake always returns the most up‑to‑date information through its [transaction log](/concepts/delta-transaction-log.md), there is no need to call `REFRESH TABLE` after changes. With raw Parquet files, Spark’s metadata cache can become stale, and you must manually refresh the table to see new data.^[best-practices-delta-lake-databricks-on-aws.md]

### Partition management

Delta Lake automatically tracks the set of partitions present in a table and updates the list as data is added or removed. This means you never need to run `ALTER TABLE [ADD|DROP] PARTITION` or `MSCK REPAIR TABLE`. Raw Parquet tables require these commands to keep partition metadata synchronized.^[best-practices-delta-lake-databricks-on-aws.md]

### Reading a single partition

When using raw Parquet, it is common to load a single partition directly by path, for example:

```python
spark.read.format("parquet").load("/data/date=2017-01-01")
```

Delta Lake instead encourages using a `WHERE` clause on the table name, which enables data skipping for better performance:

```python
spark.read.table("<table-name>").where("date = '2017-01-01'")
```

^[best-practices-delta-lake-databricks-on-aws.md]

## Data file integrity

Delta Lake uses a transaction log to commit changes atomically. You must never directly modify, add, or delete Parquet data files inside a [Delta Lake Table](/concepts/delta-lake-table.md), because that can lead to lost data or table corruption. With raw Parquet, such manual file manipulation is possible but requires careful orchestration to maintain consistency.^[best-practices-delta-lake-databricks-on-aws.md]

## Best practices for Delta Lake (and contrast with Parquet)

### File compaction

[Predictive optimization](/concepts/predictive-optimization-for-delta-lake.md) automatically runs `OPTIMIZE` and `VACUUM` on Unity Catalog managed tables. Frequently running OPTIMIZE to compact small files is recommended for both Delta Lake and raw Parquet, but Delta Lake adds atomicity and the ability to track file-level statistics. After compaction, old files are not removed until VACUUM is run.^[best-practices-delta-lake-databricks-on-aws.md]

### Caching

Databricks does not recommend using Spark caching with Delta Lake because cached DataFrames lose data‑skipping benefits from later filters, and the cached data may become stale if the table is accessed via a different identifier. This concern is less pronounced with raw Parquet tables because they do not have the same multi‑version concurrency control.^[best-practices-delta-lake-databricks-on-aws.md]

### Legacy configurations

When upgrading Databricks Runtime, explicit legacy Delta configurations should be removed so that new optimizations and default values can take effect. Raw Parquet tables do not have such configuration complexity, but also lack Delta Lake’s performance features.^[best-practices-delta-lake-databricks-on-aws.md]

## Performance optimizations for `MERGE`

Delta Lake’s `MERGE` operation can be tuned with several techniques that have no direct equivalent in raw Parquet because Parquet lacks transactional `MERGE` support. For example, reducing the search space with known constraints in the match condition, compacting files, controlling shuffle partitions, enabling optimized writes, tuning file sizes, and using [Low Shuffle Merge](/concepts/low-shuffle-merge.md) all improve performance on Delta Lake.^[best-practices-delta-lake-databricks-on-aws.md]

## Related concepts

- [Delta Lake](/concepts/delta-lake.md)
- Apache Parquet
- Apache Spark
- [Transaction log](/concepts/delta-transaction-log.md)
- [Liquid Clustering](/concepts/liquid-clustering.md)
- [Predictive optimization](/concepts/predictive-optimization-for-delta-lake.md)
- OPTIMIZE
- VACUUM
- [Low Shuffle Merge](/concepts/low-shuffle-merge.md)
- [Unity Catalog](/concepts/unity-catalog.md)

## Sources

- best-practices-delta-lake-databricks-on-aws.md

# Citations

1. [best-practices-delta-lake-databricks-on-aws.md](/references/best-practices-delta-lake-databricks-on-aws-aef26632.md)
