---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c3b46ecc60e6a8adcaa2fc4852aca0dbab52b59553a6997844fc902c669a6a76
  pageDirectory: concepts
  sources:
    - delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - refresh-sync-uniform-command
    - RSUC
  citations:
    - file: delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
title: REFRESH SYNC UNIFORM Command
description: A Databricks SQL command to synchronize the UniForm (Iceberg/Hudi) metadata of a Delta table.
tags:
  - databricks
  - delta-lake
  - sql-commands
timestamp: "2026-06-19T10:09:56.871Z"
---

# REFRESH SYNC UNIFORM Command

The **REFRESH SYNC UNIFORM command** is a Databricks SQL identifier that, when used, can return the error class `DELTA_UNIFORM_REFRESH_NOT_SUPPORTED`. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Error Conditions

When the `REFRESH SYNC UNIFORM` command fails, it returns a specific reason code indicating why the operation cannot proceed. The following reasons are defined: ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

### COLUMN_MASK

Column mask is not supported by `REFRESH` identifier `SYNC UNIFORM`. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

### COMPATIBILITY_NOT_ENABLED

`REFRESH` identifier `SYNC UNIFORM` requires compatibility to be included in `delta.universalFormat.enabledFormats`. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

### ROW_LEVEL_SECURITY

Row level security is not supported by `REFRESH` identifier `SYNC UNIFORM`. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

### UNSUPPORTED_READER_FEATURES

The reader table feature(s) `<readerFeatures>` are not supported by `REFRESH` identifier `SYNC UNIFORM`. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

### UNSUPPORTED_TYPE

`<sourceType>` is not supported by `REFRESH` identifier `SYNC UNIFORM`. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

### WRONG_TYPE

`REFRESH <keyword>` identifier `SYNC UNIFORM` cannot be used for `<sourceType>`. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## SQL State

The error class `DELTA_UNIFORM_REFRESH_NOT_SUPPORTED` maps to SQLSTATE: `0AKDC` (Feature not supported). ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta tables](/concepts/delta-lake-table.md) — The underlying table format in Databricks.
- [Universal Format (UniForm)](/concepts/delta-lake-universal-format-uniform.md) — The feature enabling multi-format representation of Delta tables.
- SQLSTATE — The classification system for SQL error states.

## Sources

- delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md](/references/delta_uniform_refresh_not_supported-error-condition-databricks-on-aws-9dd3f333.md)
