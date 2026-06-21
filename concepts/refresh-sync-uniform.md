---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 44580876eb4e977b72ed214dcab240b72a4dab4ff21b8c500d5ac7fe0cf72db6
  pageDirectory: concepts
  sources:
    - delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - refresh-sync-uniform
    - RSU
    - refresh-sync-uniform-command
    - RSUC
  citations:
    - file: delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
title: REFRESH SYNC UNIFORM
description: A Databricks SQL identifier/command used to synchronize Uniform format metadata for Delta tables
tags:
  - databricks
  - sql
  - delta-uniform
timestamp: "2026-06-19T18:28:14.407Z"
---

# REFRESH SYNC UNIFORM

**REFRESH SYNC UNIFORM** is a Databricks SQL command identifier used with the `REFRESH` statement to synchronize a Delta Lake table’s metadata so the table can be read using Uniform formats such as Apache Iceberg or Hudi. The command triggers a metadata refresh that updates the table’s Uniform format representation. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Error Conditions

The `DELTA_UNIFORM_REFRESH_NOT_SUPPORTED` error (SQLSTATE class 0A) occurs when the `REFRESH` operation with identifier `SYNC UNIFORM` cannot be performed. The error includes a detailed reason indicating which aspect of the table prevents the operation. The following sub-reasons are defined:

### COLUMN_MASK

Column masks are not supported by `REFRESH` identifier `SYNC UNIFORM`. Tables that have column masks defined cannot use this refresh operation. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

### COMPATIBILITY_NOT_ENABLED

`REFRESH` identifier `SYNC UNIFORM` requires compatibility to be included in `delta.universalFormat.enabledFormats`. The table must have the appropriate Universal Format compatibility enabled before the refresh can succeed. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

### ROW_LEVEL_SECURITY

Row‑level security is not supported by `REFRESH` identifier `SYNC UNIFORM`. Tables with row filters applied cannot use this refresh operation. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

### UNSUPPORTED_READER_FEATURES

The reader table feature(s) `<readerFeatures>` are not supported by `REFRESH` identifier `SYNC UNIFORM`. Specific reader features enabled on the table may be incompatible with Uniform format synchronization. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

### UNSUPPORTED_TYPE

`<sourceType>` is not supported by `REFRESH` identifier `SYNC UNIFORM`. The source table type is incompatible with this refresh operation. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

### WRONG_TYPE

`REFRESH <keyword>` identifier `SYNC UNIFORM` cannot be used for `<sourceType>`. The table type does not match what the `SYNC UNIFORM` identifier expects. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Requirements

For `REFRESH SYNC UNIFORM` to succeed, the target table must:

- Have [Delta Uniform](/concepts/delta-uniform.md) compatibility enabled in `delta.universalFormat.enabledFormats`.
- Not have incompatible features such as column mask or [row filter](/concepts/row-filter-policies.md).
- Have only supported reader table features.
- Be of a supported source type.

## Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md) – The feature that allows Delta Lake tables to be read by Apache Iceberg, Hudi, or other formats.
- [Column mask](/concepts/column-mask-policies.md) – A data‑masking feature that blocks this refresh operation.
- [Row filter](/concepts/row-filter-policies.md) – A row‑level security feature that blocks this refresh operation.
- [Unity Catalog](/concepts/unity-catalog.md) – The catalog that stores and manages table metadata.
- REFRESH command – The parent SQL command for metadata synchronization.

## Sources

- delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md](/references/delta_uniform_refresh_not_supported-error-condition-databricks-on-aws-9dd3f333.md)
