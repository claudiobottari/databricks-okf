---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2dcdefca070f94ad693981c9c354fffa030b2880348f0043c3f912aadf7fd257
  pageDirectory: concepts
  sources:
    - delta_metadata_mismatch-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - schema_mismatch-sub-error
    - SCHEMA_MISMATCH sub-error
    - schema mismatch
  citations:
    - file: delta_metadata_mismatch-error-condition-databricks-on-aws.md
title: SCHEMA_MISMATCH sub-error
description: A DELTA_METADATA_MISMATCH sub-error that occurs when the data schema does not match the Delta table schema, resolvable via mergeSchema or auto-merge configuration
tags:
  - databricks
  - delta-lake
  - schema-migration
  - error-messages
timestamp: "2026-06-19T15:06:41.534Z"
---

# SCHEMA_MISMATCH sub-error

The **SCHEMA_MISMATCH** sub-error is a specific `DELTA_METADATA_MISMATCH` error condition (SQLSTATE: 42KDG) raised when a write operation attempts to write data whose schema does not match the existing schema of the target Delta table. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Error Message

When a schema mismatch is detected, the error message includes the Table ID and both the table schema and the data schema for debugging:

```
A schema mismatch detected when writing to the Delta table (Table ID: <id>).

Table schema:
<tableSchema>

Data schema:
<dataSchema>
```

^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Resolution

The error provides two mechanisms for enabling automatic schema migration, depending on the API used:

- **`DataFrameWriter` or `DataStreamWriter`**: Set the option `.option("mergeSchema", "true")` to allow automatic schema merging during the write operation.
- **Other operations**: Set the session configuration `spark.databricks.delta.schema.autoMerge.enabled` to `"true"`. This enables schema auto-merge for operations that do not support the option directly (consult the operation-specific documentation for details).

^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Related Concepts

- DELTA_METADATA_MISMATCH Error Condition|DELTA_METADATA_MISMATCH error condition – The parent error class.
- [Delta Lake](/concepts/delta-lake.md) – The storage layer that enforces schema validation.
- Schema Evolution – The broader concept of safely updating table schemas.
- [mergeSchema](/concepts/mergeschema-option.md) – The DataFrameWriter option that enables schema merging.
- DataStreamWriter – Streaming API that uses the same `mergeSchema` option.
- [Auto Merge Schema](/concepts/mergeschema-option.md) – The session configuration for automatic schema migration.

## Sources

- delta_metadata_mismatch-error-condition-databricks-on-aws.md

# Citations

1. [delta_metadata_mismatch-error-condition-databricks-on-aws.md](/references/delta_metadata_mismatch-error-condition-databricks-on-aws-7ce7a126.md)
