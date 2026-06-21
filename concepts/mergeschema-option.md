---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2896b4e7f8693a48f95d2ccc9e091b4ec2a6b94c8db1e29bbe99a30a6bb7be9c
  pageDirectory: concepts
  sources:
    - delta_metadata_mismatch-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mergeschema-option
    - Auto Merge Schema
    - mergeSchema
    - mergeschema-option-pattern
    - MOP
  citations:
    - file: delta_metadata_mismatch-error-condition-databricks-on-aws.md
title: mergeSchema Option
description: A Spark/Delta Lake DataFrameWriter option that enables automatic schema migration by merging the provided schema with the existing table schema during writes.
tags:
  - delta-lake
  - configuration
  - schema-evolution
timestamp: "2026-06-18T15:21:22.522Z"
---

# mergeSchema Option

The **mergeSchema option** is a DataFrameWriter and DataStreamWriter configuration flag that, when set to `true`, allows Delta Lake to automatically evolve the table schema during write operations to accommodate new columns or changes in data schema. It is the primary mechanism for schema migration when using DataFrame-based writes to Delta tables. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## How It Works

When a write operation detects a difference between the data schema and the existing Delta table schema, a `DELTA_METADATA_MISMATCH` error with sub-type `SCHEMA_MISMATCH` is raised. The error message instructs the user to enable schema migration by either:

- Setting `.option("mergeSchema", "true")` on the DataFrameWriter or DataStreamWriter, or
- Setting the session configuration `spark.databricks.delta.schema.autoMerge.enabled` to `true` for operations that do not use DataFrame/DataStream writers. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

The `mergeSchema` option is specifically recommended for writes using `DataFrameWriter` or `DataStreamWriter` (e.g., `df.write.format("delta").option("mergeSchema", "true").save(...)`). For other operations, you must use the session-level configuration. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Example Usage

```python
# DataFrame write with schema merge enabled
df.write \
  .format("delta") \
  .option("mergeSchema", "true") \
  .mode("append") \
  .save("/path/to/table")
```

If `mergeSchema` is not set and a schema mismatch occurs, the write fails with the `SCHEMA_MISMATCH` error. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Session Configuration Alternative

For operations that are not DataFrame or DataStream writes (e.g., SQL inserts, structured streaming with certain modes), you can enable automatic schema merge globally via:

```scala
spark.conf.set("spark.databricks.delta.schema.autoMerge.enabled", "true")
```

This session-level flag allows schema migration for a broader class of write operations without requiring the `mergeSchema` option on each writer. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Schema Evolution](/concepts/delta-lake-schema-migration.md) – Overarching concept of managing schema changes over time.
- Delta Lake Write Modes – How `mergeSchema` interacts with `append`, `overwrite`, and other modes.
- DELTA_METADATA_MISMATCH Error Condition|DELTA_METADATA_MISMATCH error condition – The error that triggers the need for `mergeSchema`.
- DataFrameWriter and DataStreamWriter – APIs where the `mergeSchema` option is applied.
- Automatic Schema Merge – The broader configuration controlled by `spark.databricks.delta.schema.autoMerge.enabled`.

## Sources

- delta_metadata_mismatch-error-condition-databricks-on-aws.md

# Citations

1. [delta_metadata_mismatch-error-condition-databricks-on-aws.md](/references/delta_metadata_mismatch-error-condition-databricks-on-aws-7ce7a126.md)
