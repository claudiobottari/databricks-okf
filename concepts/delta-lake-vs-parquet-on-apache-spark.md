---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d2acf04ddda291a958fd61c8191ca1117ce9cf14d4caaccc95aecce1f954e9a5
  pageDirectory: concepts
  sources:
    - best-practices-delta-lake-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-vs-parquet-on-apache-spark
    - DLVPOAS
  citations:
    - file: best-practices-delta-lake-databricks-on-aws.md
title: Delta Lake vs Parquet on Apache Spark
description: Key differences where Delta Lake automatically handles REFRESH TABLE, partition management, partition reading, and data file modifications that must be done manually with Parquet
tags:
  - delta-lake
  - parquet
  - spark
timestamp: "2026-06-19T22:13:23.153Z"
---

# Delta Lake vs Parquet on Apache Spark

**Delta Lake** and **Apache Parquet** are both storage formats commonly used with Apache Spark, but they serve different purposes and handle data management operations differently. Parquet is a columnar storage format, while Delta Lake is an open-source storage layer that builds on top of Parquet to provide ACID transactions, schema enforcement, and other data reliability features.

## Key Differences

### Automatic vs Manual Operations

Delta Lake handles several operations automatically that must be performed manually when using Parquet directly:

- **`REFRESH TABLE`**: Delta Lake tables always return the most up-to-date information, eliminating the need to call `REFRESH TABLE` manually after changes. With Parquet, you may need to refresh metadata caches. ^[best-practices-delta-lake-databricks-on-aws.md]
- **Partition management**: Delta Lake automatically tracks the set of partitions present in a table and updates the list as data is added or removed. This means you never need to run `ALTER TABLE [ADD|DROP] PARTITION` or `MSCK` commands, which are often required with Parquet tables. ^[best-practices-delta-lake-databricks-on-aws.md]
- **Loading partitions**: With Parquet, it's common practice to load a specific partition directly (e.g., `spark.read.format("parquet").load("/data/date=2017-01-01")`). Delta Lake discourages this approach and recommends using `WHERE` clauses for data skipping, such as `spark.read.table("<table-name>").where("date = '2017-01-01'")`. ^[best-practices-delta-lake-databricks-on-aws.md]

### Data Modification Safety

Delta Lake uses a transaction log to commit changes to the table atomically. You should never directly modify, add, or delete Parquet data files in a [Delta Lake Table](/concepts/delta-lake-table.md), as this can lead to lost data or table corruption. When using raw Parquet files, manual file operations are sometimes performed, but this is not safe practice. ^[best-practices-delta-lake-databricks-on-aws.md]

## Using Delta Lake Together with Parquet

Delta Lake does not replace Parquet but rather builds upon it. Delta Lake stores data in Parquet format while adding a transaction log and metadata layer on top. This means that when you work with Delta Lake, you still benefit from Parquet's efficient columnar storage and compression, while also gaining additional reliability and performance features. ^[best-practices-delta-lake-databricks-on-aws.md]

## Performance Considerations

### Merge Operations

For Delta Lake merge operations specifically, several optimizations differ from working with Parquet directly:

- **Reducing search space**: Delta Lake merge can be optimized by adding known constraints in the match condition. For example, if a table is partitioned by `country` and `date`, adding `events.date = current_date() AND events.country = 'USA'` to the match condition makes the query faster and reduces conflicts with other concurrent operations. ^[best-practices-delta-lake-databricks-on-aws.md]
- **File compaction**: Delta Lake supports predictive optimization that automatically runs OPTIMIZE and VACUUM commands, compacting small files into larger ones for better read throughput. ^[best-practices-delta-lake-databricks-on-aws.md]
- **Low Shuffle Merge**: Delta Lake provides an optimized implementation of `MERGE` that offers better performance for most common workloads and preserves existing data layout optimizations on unmodified data. ^[best-practices-delta-lake-databricks-on-aws.md]

### File Size Management

Databricks automatically tunes file sizes based on table size when using Delta Lake, using smaller files for smaller tables and larger files for larger tables. This automated tuning is not available when working with raw Parquet files. ^[best-practices-delta-lake-databricks-on-aws.md]

## When to Use Each Format

- **Use Delta Lake** when you need ACID transactions, time travel (data versioning), schema enforcement, scalable metadata handling, and unified batch/streaming processing. It is the recommended format for production data pipelines on Databricks.
- **Use Apache Parquet** for simpler read-heavy workloads where you don't need transaction support or when interoperating with systems that don't support Delta Lake. Parquet is also appropriate as an intermediate format for data exchange.

## Limitations of Parquet on Spark

When using plain Parquet tables with Spark, you must handle several maintenance tasks manually:

- Running `MSCK REPAIR TABLE` to add new partitions
- Executing `REFRESH TABLE` to update metadata caches
- Manually adding and removing partitions with `ALTER TABLE [ADD|DROP] PARTITION`
- Directly loading partition directories rather than using predicate pushdown

Delta Lake eliminates these manual steps, reducing the potential for errors and simplifying data pipeline code.

## Sources

- best-practices-delta-lake-databricks-on-aws.md

# Citations

1. [best-practices-delta-lake-databricks-on-aws.md](/references/best-practices-delta-lake-databricks-on-aws-aef26632.md)
