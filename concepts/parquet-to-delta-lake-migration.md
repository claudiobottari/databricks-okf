---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ecdce226fcc076ccf89d9742cdcdeb7040051414a95210e85f1d23f73e806b56
  pageDirectory: concepts
  sources:
    - migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - parquet-to-delta-lake-migration
    - PTDLM
  citations:
    - file: migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md
title: Parquet to Delta Lake Migration
description: The process and strategies for converting existing Apache Parquet data lakes into Delta Lake format on Databricks.
tags:
  - data-migration
  - delta-lake
  - parquet
timestamp: "2026-06-19T19:32:25.935Z"
---

# Parquet to Delta Lake Migration

**Parquet to Delta Lake Migration** refers to the process of converting existing Parquet data lakes into [Delta Lake](/concepts/delta-lake.md) format on Databricks. Delta Lake is the underlying format in the Databricks lakehouse, providing ACID transactions, scalable metadata handling, and unified batch and streaming capabilities. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Considerations Before Conversion

Before migrating, evaluate your existing Parquet data lake's partitioning strategy. While you can maintain the current partitioning structure during conversion, over-partitioned tables are a common cause of slow workloads on Delta Lake. Consider whether the data being converted is still growing and how frequently it is queried, as different Parquet tables may warrant different migration approaches. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

Also consider whether conversion is appropriate. You might choose to maintain data in Parquet format if an upstream system writes data to Parquet without native support for Delta Lake, or if a downstream system that reads Parquet data cannot read Delta Lake. In such cases, replicating tables to Delta Lake allows you to leverage performance benefits while reading, writing, updating, and deleting records. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Migration Approaches

### CLONE Parquet

The `CLONE` Parquet approach allows incremental copying from a Parquet data lake to Delta Lake. **Shallow clones** create pointers to existing Parquet files, maintaining your Parquet table in its original location and format while providing optimized access through collected file statistics. You can write to the table created by a shallow clone without impacting the original data source. **Deep clones** copy all data files from the source to a new location while converting to Delta Lake, supporting incremental detection of new files including backfill operations on subsequent executions. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

```sql
CREATE OR REPLACE TABLE <target-table-name> [SHALLOW] CLONE parquet.`/path/to/data`;
```

### CONVERT TO DELTA

The `CONVERT TO DELTA` command transforms a directory of Parquet files into a Delta table with a single command. After conversion, stop reading and writing from the table using Parquet logic, as data written to the target directory after conversion has started might not be reflected in the resultant Delta table. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

```sql
CONVERT TO DELTA parquet.`s3://my-bucket/parquet-data`;
```

### Auto Loader

While designed for incremental data ingestion from cloud object storage, Auto Loader can implement a pattern that incrementally copies all data from a directory to a target table. The following example processes all existing files, triggers automatic weekly backfill to capture missed files, allows Spark to use many jobs to avoid spill and out-of-memory errors, and provides exactly-once processing guarantees: ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

```python
(spark.readStream
  .format("cloudFiles")
  .option("cloudFiles.format", "parquet")
  .option("cloudFiles.includeExistingFiles", "true")
  .option("cloudFiles.backfillInterval", "1 week")
  .option("cloudFiles.schemaLocation", checkpoint_path)
  .load(file_path)
  .writeStream
  .option("checkpointLocation", checkpoint_path)
  .trigger(availableNow=True)
  .toTable(table_name))
```

### Custom Apache Spark Batch Logic

Writing custom Apache Spark logic provides flexibility in controlling how and when different data is migrated, but may require extensive configuration to replicate capabilities built into other approaches. At its core, this approach is a simple read and write operation: ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

```python
spark.read.format("parquet").load(file_path).write.mode("append").saveAsTable(table_name)
```

For backfills or incremental migration, you can rely on the source's partitioning structure or write custom logic to track new files. While Delta Lake merge capabilities can avoid duplicate records, comparing all records from a large Parquet source to a large Delta table is computationally expensive. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Approach Comparison

| Approach | Incremental | Duplicates Data | Maintains Structure | Backfill Data | Ease of Use |
|---|---|---|---|---|---|
| CLONE Parquet | Yes | Shallow: No; Deep: Yes | Yes | Yes | Medium |
| CONVERT TO DELTA | No | No | Yes | No | High |
| Auto Loader | Yes | Yes | Yes | Yes | Medium |
| Custom Spark Logic | Configurable | Yes | Configurable | Configurable | Low |

^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## When Not to Convert

Databricks recommends using Delta Lake for all tables that receive regular updates or queries from Databricks. However, maintain data in Parquet format when an upstream system that writes data to Parquet does not support native writing to Delta Lake, or when a downstream system that reads Parquet data cannot read Delta Lake. Simultaneously modifying data in the same Delta table stored in S3 from multiple workspaces or data systems is not recommended. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The underlying format in the Databricks lakehouse
- Databricks Lakehouse — The architecture Delta Lake enables
- Auto Loader — Incremental data ingestion from cloud object storage
- Delta Lake merge — Capability to avoid duplicate records during upserts
- [Table partitioning](/concepts/delta-table-partitioning-mismatch.md) — Partitioning strategy considerations when migrating
- CLONE (Delta Lake) — Incremental cloning from Parquet to Delta

## Sources

- migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md

# Citations

1. [migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md](/references/migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws-01ccec95.md)
