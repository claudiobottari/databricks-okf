---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6e5e9b61b0c7b58d418f411f81e1bd2bf9972f77527c69d906a7618232a1cff0
  pageDirectory: concepts
  sources:
    - migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-spark-batch-migration
    - CSBM
  citations:
    - file: migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md
title: Custom Spark Batch Migration
description: Using custom Apache Spark batch logic to migrate Parquet data to Delta Lake, offering flexibility but requiring manual tracking and handling of incremental updates.
tags:
  - apache-spark
  - delta-lake
  - data-migration
timestamp: "2026-06-19T19:32:15.155Z"
---

# Custom Spark Batch Migration

**Custom Spark Batch Migration** is an approach for converting a Parquet data lake to [Delta Lake](/concepts/delta-lake.md) using hand-written Apache Spark batch logic. This method offers great flexibility in controlling how and when data is migrated, but typically requires more configuration than other approaches such as [CLONE Parquet](/concepts/clone-parquet.md), [CONVERT TO DELTA](/concepts/convert-to-delta.md), or Auto Loader. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Core Pattern

The heart of the custom batch approach is a standard Spark read and write operation:

```python
spark.read.format("parquet").load(file_path).write.mode("append").saveAsTable(table_name)
```

This reads the source Parquet files and appends them to a Delta table. The mode can be adjusted (e.g., `overwrite`) depending on the migration strategy. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Incremental Migration and Backfills

To perform incremental migrations or backfills, you can rely on the partitioning structure of the source Parquet data. Alternatively, you may need to write custom logic to track which files have been added since the last load. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

Delta Lake’s merge operation can be used to avoid writing duplicate records. However, comparing all records from a large Parquet source table to the contents of a large Delta table is a computationally expensive task and should be used with care. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Considerations

- **Flexibility:** You control exactly when and what data is migrated, which is useful when the source has custom partitioning or complex transformation requirements.
- **Configuration Overhead:** Capabilities such as incremental file tracking and exactly-once processing are not built in and must be implemented manually. Other approaches (e.g., Auto Loader) provide these out of the box. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]
- **Performance:** Without careful optimization, large full-table comparisons for deduplication can be slow and resource intensive.

## When to Use This Approach

Use custom Spark batch logic when you need fine-grained control over the conversion process that is not provided by higher-level tools. For example, if the source data uses a non-standard partitioning scheme that cannot be easily expressed in `CLONE` or `CONVERT TO DELTA`, or if you need to apply per-row transformations during migration.

If you do not require custom logic, consider one of the other methods listed in the migration matrix: `CLONE` Parquet (incremental, shallow or deep), `CONVERT TO DELTA` (one-time conversion), or Auto Loader (continuous incremental ingestion). ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md)
- Parquet
- [CLONE Parquet](/concepts/clone-parquet.md)
- [CONVERT TO DELTA](/concepts/convert-to-delta.md)
- Auto Loader
- Apache Spark
- Databricks Lakehouse

## Sources

- migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md

# Citations

1. [migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md](/references/migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws-01ccec95.md)
