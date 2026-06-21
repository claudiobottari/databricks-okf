---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7bfec7b08b7042844553909d880c056f4687a2f9d5d17cf5671415a51428b88e
  pageDirectory: concepts
  sources:
    - delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-uniform-compatibility-requirement
    - DUCR
  citations:
    - file: delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
title: Delta Uniform compatibility requirement
description: The delta.universalFormat.enabledFormats config must include 'compatibility' for REFRESH SYNC UNIFORM to work
tags:
  - databricks
  - delta-uniform
  - configuration
timestamp: "2026-06-19T18:28:56.213Z"
---

# Delta Uniform compatibility requirement

The **Delta Uniform compatibility requirement** defines the conditions that must be met for the `REFRESH` identifier `SYNC UNIFORM` operation to succeed on [Delta Lake](/concepts/delta-lake.md) tables. When certain Delta table features or configurations are incompatible with the uniform refresh mechanism, Databricks returns the `DELTA_UNIFORM_REFRESH_NOT_SUPPORTED` error, which includes a specific reason code indicating which requirement was violated. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Error structure

The `DELTA_UNIFORM_REFRESH_NOT_SUPPORTED` error is thrown with `SQLSTATE: 0AKDC` and includes the message "`REFRESH` identifier `SYNC UNIFORM` is not supported for reason:" followed by one of the sub-reasons below. Each sub-reason maps to a specific [Delta Uniform](/concepts/delta-uniform.md) compatibility requirement that was not met. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Reasons and requirements

### COLUMN_MASK

**Column mask** is not supported by `REFRESH` identifier `SYNC UNIFORM`. If a table has column masks defined, the uniform refresh cannot proceed because the masking logic cannot be properly translated or applied during the sync operation. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

### COMPATIBILITY_NOT_ENABLED

`REFRESH` identifier `SYNC UNIFORM` requires [Delta Uniform](/concepts/delta-uniform.md) compatibility to be included in the `delta.universalFormat.enabledFormats` configuration. If that configuration does not list the target format, the refresh operation is blocked. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

### ROW_LEVEL_SECURITY

**Row level security** is not supported by `REFRESH` identifier `SYNC UNIFORM`. When a Delta table has row‑level security filters defined, the uniform refresh cannot execute because the security rules cannot be faithfully represented or enforced during the conversion. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

### UNSUPPORTED_READER_FEATURES

The reader table feature(s) listed in the error payload are not supported by `REFRESH` identifier `SYNC UNIFORM`. The table has enabled reader‑side features that are incompatible with the uniform refresh protocol, so the operation is denied. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

### UNSUPPORTED_TYPE

The `<sourceType>` specified in the error is not supported by `REFRESH` identifier `SYNC UNIFORM`. The source table format is one for which no uniform refresh path exists. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

### WRONG_TYPE

`REFRESH <keyword>` identifier `SYNC UNIFORM` cannot be used for `<sourceType>`. The keyword used in the `REFRESH` statement does not match the actual type of the source table, so the uniform refresh cannot proceed. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Related concepts

- [Delta Uniform](/concepts/delta-uniform.md) – The feature that syncs Delta table metadata to other formats for interoperability.
- [Delta Lake](/concepts/delta-lake.md) – The core storage format on Databricks.
- [Column masking](/concepts/delta-lake-column-masking.md) – A Delta table security feature that can block uniform refresh.
- [Row-level security](/concepts/row-level-security-rls-policies.md) – A Delta table security feature that can block uniform refresh.
- [SQLSTATE 0AKDC](/concepts/sqlstate-0akdc.md) – The SQL state code associated with feature-not-supported errors.

## Sources

- delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md](/references/delta_uniform_refresh_not_supported-error-condition-databricks-on-aws-9dd3f333.md)
