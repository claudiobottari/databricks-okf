---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c0f1d3973fff1529de8d9753d2f940045750258090cbd247257e344b99c16c7f
  pageDirectory: concepts
  sources:
    - delta_metadata_mismatch-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_metadata_mismatch-error-condition
    - DEC
    - DELTA_METADATA_MISMATCH error condition
  citations:
    - file: delta_metadata_mismatch-error-condition-databricks-on-aws.md
title: DELTA_METADATA_MISMATCH Error Condition
description: A Databricks error condition (SQLSTATE 42KDG) raised when a metadata mismatch is detected while writing to a Delta table, with multiple subtypes for different root causes.
tags:
  - delta-lake
  - error-handling
  - databricks
timestamp: "2026-06-19T18:26:16.444Z"
---

# DELTA_METADATA_MISMATCH Error Condition

**DELTA_METADATA_MISMATCH** is a [Delta Lake](/concepts/delta-lake.md) error condition (SQLSTATE: 42KDG) raised when a metadata mismatch is detected during a write operation to a Delta table. It belongs to SQL class 42 (Syntax Error or Access Rule Violation). ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Error Subtypes

### ACL_ENABLED

Table ACLs are enabled on the cluster, which prevents automatic schema migration. To resolve, use `ALTER TABLE` to change the schema manually instead of relying on automatic migration. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

### ENABLE_LIQUID

Occurs when attempting to enable [Liquid Clustering](/concepts/liquid-clustering.md) on an existing table. The solution is to use overwrite mode with the option `overwriteSchema` set to `"true"`. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

### OVERWRITE_REQUIRED

To overwrite the schema or change partitioning, set `.option("overwriteSchema", "true")`. Note that the schema cannot be overwritten when using `replaceWhere`. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

### PARTITIONING_MISMATCH

The partition columns in the data being written do not match the partition columns of the target table. The error message displays both the provided and the table’s original partition columns. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

### SCHEMA_MISMATCH

A schema mismatch is detected when writing to the Delta table (identified by Table ID). To enable schema migration:

- For DataFrameWriter or DataStreamWriter operations, set `.option("mergeSchema", "true")`.
- For other operations, set the session configuration `spark.databricks.delta.schema.autoMerge.enabled` to `"true"`.

The error message includes both the table schema and the data schema for comparison. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Schema Evolution](/concepts/delta-lake-schema-migration.md) – Strategies for handling schema changes in Delta tables.
- [Delta Table Partitioning](/concepts/delta-table-partitioning-mismatch.md) – Understanding partition column requirements.
- [Delta Merge Operations](/concepts/delta-lake-dml-operations.md) – Operations that may trigger schema merging.
- [Liquid Clustering](/concepts/liquid-clustering.md) – Data organization technique that can trigger the ENABLE_LIQUID error.
- Delta Table ACLs – Access control lists affecting schema operations.
- SQLSTATE Error Codes – Broader classification of SQL error conditions (42KDG is a member).

## Sources

- delta_metadata_mismatch-error-condition-databricks-on-aws.md

# Citations

1. [delta_metadata_mismatch-error-condition-databricks-on-aws.md](/references/delta_metadata_mismatch-error-condition-databricks-on-aws-7ce7a126.md)
