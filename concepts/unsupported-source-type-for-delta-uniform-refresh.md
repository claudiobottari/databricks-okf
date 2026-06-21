---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6360e3d1c7bcbbc4995a2bd4b6bb4d7fa8f547f7fa2cf2933fd4cce5a412471f
  pageDirectory: concepts
  sources:
    - delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unsupported-source-type-for-delta-uniform-refresh
    - USTFDUR
  citations:
    - file: delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
title: Unsupported source type for Delta Uniform refresh
description: REFRESH SYNC UNIFORM cannot be applied to certain source table types, raising UNSUPPORTED_TYPE or WRONG_TYPE sub-errors
tags:
  - databricks
  - delta-uniform
  - source-type
timestamp: "2026-06-19T18:28:27.699Z"
---

# Unsupported Source Type for Delta Uniform Refresh

The **Unsupported source type for Delta Uniform refresh** error is part of the `DELTA_UNIFORM_REFRESH_NOT_SUPPORTED` error class (SQLSTATE: 0AKDC). It occurs when attempting to use the `REFRESH` identifier `SYNC UNIFORM` on a table that is not compatible with the operation, either because of an unsupported underlying source type or because the table has reader features that are not supported by the refresh command. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Error Conditions

The error class includes the following sub‑conditions that describe the specific reason for failure:

### COLUMN_MASK

Column mask is not supported by `REFRESH` identifier `SYNC UNIFORM`. If the table has a column mask defined, the uniform refresh cannot proceed. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

### COMPATIBILITY_NOT_ENABLED

`REFRESH` identifier `SYNC UNIFORM` requires that compatibility be included in `delta.universalFormat.enabledFormats`. This means the table must have the appropriate universal format compatibility enabled in its table properties. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

### ROW_LEVEL_SECURITY

[Row-level security](/concepts/row-level-security-rls-policies.md) is not supported by `REFRESH` identifier `SYNC UNIFORM`. Tables with row filters cannot be refreshed using this command. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

### UNSUPPORTED_READER_FEATURES

One or more reader table features (identified as `<readerFeatures>`) are not supported by `REFRESH` identifier `SYNC UNIFORM`. This indicates that the table was written with reader‑side protocols that are incompatible with the uniform refresh operation. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

### UNSUPPORTED_TYPE

`<sourceType>` is not supported by `REFRESH` identifier `SYNC UNIFORM`. This is the specific condition that matches the page title: the source type of the table (e.g., a non‑Delta format or an unsupported Delta feature combination) prevents the uniform refresh. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

### WRONG_TYPE

`REFRESH <keyword>` identifier `SYNC UNIFORM` cannot be used for `<sourceType>`. This sub‑condition indicates that the refresh command was invoked on a table whose type does not match the expected target for the operation (e.g., refreshing a view as if it were a Delta table). ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md) – The feature that enables unified table formats.
- [REFRESH SYNC UNIFORM](/concepts/refresh-sync-uniform.md) – The SQL command that triggers the error.
- Delta Lake Table Properties – Includes `delta.universalFormat.enabledFormats`.
- Column Mask – A security feature that blocks uniform refresh.
- [Row-Level Security](/concepts/row-level-security-rls-policies.md) – Another security feature that blocks uniform refresh.
- [Reader Table Features](/concepts/delta-lake-reader-table-features.md) – Protocol‑level capabilities of a Delta table.

## Sources

- delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md](/references/delta_uniform_refresh_not_supported-error-condition-databricks-on-aws-9dd3f333.md)
