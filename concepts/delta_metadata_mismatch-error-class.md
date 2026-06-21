---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3247995f3da1642ff89a0f60bd5dc959ad6a0aa7d29a565f48923f7b123b233f
  pageDirectory: concepts
  sources:
    - delta_metadata_mismatch-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_metadata_mismatch-error-class
    - DEC
    - DELTA_METADATA_MISMATCH Error Class
    - DELTA_METADATA_MISMATCH error
    - DELTA_METADATA_MISMATCH error class
    - Delta Metadata Mismatch Error
    - DELTA_METADATA_MISMATCH
    - delta_metadata_mismatch-error-condition
    - DELTA_METADATA_MISMATCH error condition
  citations:
    - file: delta_metadata_mismatch-error-condition-databricks-on-aws.md
title: DELTA_METADATA_MISMATCH Error Class
description: A Databricks error condition triggered when a metadata mismatch is detected during writes to a Delta table, with several specific subtypes.
tags:
  - delta-lake
  - error-handling
  - databricks
timestamp: "2026-06-19T10:06:53.785Z"
---

# DELTA_METADATA_MISMATCH Error Class

The **DELTA_METADATA_MISMATCH** error class is a runtime error with SQLSTATE **42KDG** that occurs when a metadata mismatch is detected while writing to a [Delta Lake](/concepts/delta-lake.md) table. This error is raised during write operations when the schema or partitioning of the incoming data does not match the existing table definition. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Error Sub-Categories

The DELTA_METADATA_MISMATCH error class includes several specific sub-categories that describe the nature of the mismatch.

### ACL_ENABLED

This error occurs when **Table ACLs** are enabled on the cluster and an automatic schema migration is attempted. Because table ACLs enforce strict access control, automatic schema changes are not permitted. To resolve this error, use the `ALTER TABLE` command to manually change the table schema instead of relying on automatic migration. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

### ENABLE_LIQUID

This error is raised when attempting to enable [Liquid Clustering](/concepts/liquid-clustering.md) on an existing table. To activate clustering, you must use "overwrite" mode and set the option `.option("overwriteSchema", "true")` in your write operation. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

### OVERWRITE_REQUIRED

This error indicates that a schema or partitioning change requires explicit overwrite permission. To overwrite the schema or change partitioning, set `.option("overwriteSchema", "true")` in your write configuration. Note that the schema cannot be overwritten when using `replaceWhere` in the same operation. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

### PARTITIONING_MISMATCH

This error is raised when the partition columns in the data do not match the partition columns of the existing Delta table. The error message displays both the provided partition columns and the table's original partition columns, allowing you to identify the specific mismatch. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

### SCHEMA_MISMATCH

This error occurs when a schema mismatch is detected during a write operation to a Delta table. The error message includes the **Table ID** and displays both the table schema and the data schema for comparison. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

To enable [schema migration](/concepts/delta-lake-schema-migration.md) when using `DataFrameWriter` or `DataStreamWriter`, set the option `.option("mergeSchema", "true")`. For other operations, configure the session setting `spark.databricks.delta.schema.autoMerge.enabled` to `"true"`. See the documentation specific to the operation for details. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md)
- [Schema migration](/concepts/delta-lake-schema-migration.md)
- Table ACLs
- SQLSTATE error codes
- [Liquid Clustering](/concepts/liquid-clustering.md)
- DataFrameWriter
- DataStreamWriter

## Sources

- delta_metadata_mismatch-error-condition-databricks-on-aws.md

# Citations

1. [delta_metadata_mismatch-error-condition-databricks-on-aws.md](/references/delta_metadata_mismatch-error-condition-databricks-on-aws-7ce7a126.md)
