---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d5504ad57739c4c2182bcb582e0297d5b63b3510d8f8b0e3d4b8dcb4c9e42026
  pageDirectory: concepts
  sources:
    - migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - auto-loader-for-parquet-migration
    - ALFPM
  citations:
    - file: migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md
title: Auto Loader for Parquet Migration
description: Using Databricks Auto Loader's incremental ingestion capabilities to migrate Parquet data to Delta Lake with exactly-once guarantees.
tags:
  - delta-lake
  - data-ingestion
  - auto-loader
timestamp: "2026-06-19T19:32:16.691Z"
---

# Auto Loader for Parquet Migration

**Auto Loader for Parquet Migration** is a pattern for converting an existing Parquet data lake to [Delta Lake](/concepts/delta-lake.md) using Auto Loader, Databricks' incremental ingestion engine for cloud object storage. While Auto Loader is primarily designed for incremental data ingestion, it can be configured to incrementally copy all data from a given Parquet directory to a target Delta table. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Overview

When migrating Parquet data to Delta Lake, Auto Loader provides several advantages over batch conversion approaches. It can process all existing files in the source directory, trigger automatic weekly backfill jobs to capture missed files, use multiple Spark jobs to avoid spill and out-of-memory errors associated with large data partitions, and provide end-to-end exactly-once processing guarantees. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Configuration Example

The following code example demonstrates an Auto Loader configuration for Parquet migration:

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

^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

### Key Configuration Options

- **`cloudFiles.includeExistingFiles`** — When set to `true`, processes all existing files in the source directory at the start of the stream, not just newly arriving files. This is critical for migrating historical Parquet data. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]
- **`cloudFiles.backfillInterval`** — Triggers an automatic weekly backfill job to capture files that might have been missed during initial processing. The example uses `"1 week"`. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]
- **`trigger(availableNow=True)`** — Processes all available data in micro-batches without keeping the stream continuously running, which is appropriate for one-time or scheduled migration jobs. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]
- **`cloudFiles.schemaLocation`** and **`checkpointLocation`** — Required for tracking schema evolution and stream progress, respectively. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Integration with Lakeflow

Auto Loader can also be used in [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) with either Python or SQL, including through streaming tables. This provides a declarative approach to defining migration pipelines. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Comparison with Other Migration Approaches

Auto Loader sits alongside three other main approaches to Parquet-to-Delta migration:

| Approach | Incremental | Duplicates Data | Maintains Structure | Backfill Support |
|---|---|---|---|---|
| [CLONE Parquet](/concepts/clone-parquet.md) | Yes | Shallow: No; Deep: Yes | Yes | Yes |
| [CONVERT TO DELTA](/concepts/convert-to-delta.md) | No | No | Yes | No |
| Auto Loader | Yes | Yes | Yes | Yes (via backfill interval) |
| Custom Spark Batch Logic | Custom | Custom | Custom | Custom |

Auto Loader offers incremental migration with backfill support, but it duplicates data by writing to a new Delta location rather than converting files in place. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Considerations

Before using Auto Loader for migration, consider that:

- The approach **duplicates data** by writing Parquet data to a new Delta table location. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]
- Existing Parquet partitioning strategies may need review, as over-partitioned tables can cause slow workloads on Delta Lake. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]
- Data being converted may still be growing, and Auto Loader's incremental capabilities handle this well through its file discovery mechanism. ^[migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md]

## Related Concepts

- Auto Loader — The underlying incremental ingestion engine
- [Delta Lake](/concepts/delta-lake.md) — The target format for migration
- [CLONE Parquet](/concepts/clone-parquet.md) — Alternative migration approach using shallow or deep clones
- [CONVERT TO DELTA](/concepts/convert-to-delta.md) — Alternative single-command batch conversion
- Streaming Tables — Declarative pipeline support for Auto Loader
- Partitioning in Delta Lake — Best practices for table partitioning

## Sources

- migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md

# Citations

1. [migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws.md](/references/migrate-a-parquet-data-lake-to-delta-lake-databricks-on-aws-01ccec95.md)
