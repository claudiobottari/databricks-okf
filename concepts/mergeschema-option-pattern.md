---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5b5b102cb6bd38ef425c5bc1bfdc6105319587a7e1efa32bbdd32a333d7ed9d5
  pageDirectory: concepts
  sources:
    - delta_metadata_mismatch-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mergeschema-option-pattern
    - MOP
  citations:
    - file: delta_metadata_mismatch-error-condition-databricks-on-aws.md
title: mergeSchema Option Pattern
description: A Delta Lake DataFrameWriter option (.option('mergeSchema', 'true')) used to enable automatic schema migration when writing, allowing new columns to be added to the table.
tags:
  - delta-lake
  - schema-evolution
  - configuration
timestamp: "2026-06-19T18:26:01.990Z"
---

# mergeSchema Option Pattern

The **mergeSchema option pattern** resolves `DELTA_METADATA_MISMATCH` errors caused by a SCHEMA_MISMATCH sub-error|schema mismatch when writing data to a [Delta table](/concepts/delta-lake-table.md). When the schema of the incoming data does not match the existing table schema — for example, new columns are present or column types differ — Delta Lake raises the error `DELTA_METADATA_MISMATCH / SCHEMA_MISMATCH`. The `mergeSchema` option tells Delta to automatically merge the schemas rather than rejecting the write.^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## When to Use

Use `mergeSchema` when you want to append data that contains new columns or has a slightly different schema than the target Delta table, and you are comfortable with automatic schema evolution. The option is specified on the DataFrameWriter or DataStreamWriter.^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

For operations that are not based on DataFrameWriter or DataStreamWriter, the session configuration `spark.databricks.delta.schema.autoMerge.enabled` can be set to `true` to enable automatic schema merging.^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## How to Use

### With DataFrameWriter

When writing with `DataFrameWriter`, set the option `mergeSchema` to `true`:

```scala
df.write
  .mode("append")
  .option("mergeSchema", "true")
  .save("/path/to/delta-table")
```

### With DataStreamWriter (Structured Streaming)

For streaming writes, use the same option on `DataStreamWriter`:

```scala
streamingDF.writeStream
  .option("checkpointLocation", "/checkpoint")
  .option("mergeSchema", "true")
  .table("target_table")
```

## Related Error Messages

The `DELTA_METADATA_MISMATCH` error class includes several sub‑errors that may arise from schema or partitioning mismatches. The two that specifically relate to schema evolution are:

- **SCHEMA_MISMATCH** – Raised when the data schema differs from the table schema. The recommended fix is to set `mergeSchema` to `true` or enable the session-level auto‑merge configuration.^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]
- **OVERWRITE_REQUIRED** – Raised when you try to change partitioning or overwrite the schema without specifying `overwriteSchema`; this is a different pattern from `mergeSchema`.^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Limitations

The `mergeSchema` option cannot be used together with `replaceWhere`. When using `replaceWhere`, you must handle schema changes differently (e.g., by overwriting the full schema first).^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The storage layer that manages ACID transactions and schema evolution.
- Schema Evolution – The general practice of adapting table schemas over time.
- [Overwrite Schema Option Pattern](/concepts/overwriteschema-option-pattern.md) – The pattern used to replace the entire schema via `overwriteSchema`.
- DataFrameWriter – The Spark API for writing DataFrames to external storage.
- DataStreamWriter – The Spark API for writing streaming DataFrames.

## Sources

- delta_metadata_mismatch-error-condition-databricks-on-aws.md

# Citations

1. [delta_metadata_mismatch-error-condition-databricks-on-aws.md](/references/delta_metadata_mismatch-error-condition-databricks-on-aws-7ce7a126.md)
