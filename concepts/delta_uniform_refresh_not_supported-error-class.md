---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 47267906a224ce511690313e9442187220c9f3e680561726dcf8bcd7e52a1f1d
  pageDirectory: concepts
  sources:
    - delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_uniform_refresh_not_supported-error-class
    - DEC
    - DELTA_UNIFORM_REFRESH_NOT_SUPPORTED
    - DELTA_UNIFORM_REFRESH_NOT_SUPPORTED error class
    - DELTA_UNIFORM_REFRESH_NOT_SUPPORTED error condition
  citations:
    - file: delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
title: DELTA_UNIFORM_REFRESH_NOT_SUPPORTED error class
description: A Databricks error class raised when REFRESH SYNC UNIFORM cannot be performed due to various incompatibilities
tags:
  - databricks
  - error
  - delta-uniform
timestamp: "2026-06-19T18:28:07.716Z"
---

# DELTA_UNIFORM_REFRESH_NOT_SUPPORTED Error Class

The **DELTA_UNIFORM_REFRESH_NOT_SUPPORTED** error class occurs when a `REFRESH` operation with the `SYNC UNIFORM` clause fails because the target Delta table has an incompatible feature, configuration, or type. The error carries SQLSTATE code `0AKDC`, which belongs to the "Feature Not Supported" class.^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Error Message

The general form of the error is:

```
REFRESH identifier SYNC UNIFORM is not supported for reason: <reason>
```

The `<reason>` placeholder is replaced by one of the sub-condition messages described below.^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Sub-Conditions

Each sub-condition provides a specific reason why the `REFRESH SYNC UNIFORM` operation is not supported.

### COLUMN_MASK

> Column mask is not supported by `REFRESH` identifier `SYNC UNIFORM`.

The table has a column mask applied, which is incompatible with the Uniform format refresh.^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

### COMPATIBILITY_NOT_ENABLED

> `REFRESH` identifier `SYNC UNIFORM` requires compatibility to be included in `delta.universalFormat.enabledFormats`.

The table property `delta.universalFormat.enabledFormats` does not include `compatibility` as one of the enabled formats, which is required for the `SYNC UNIFORM` refresh.^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

### ROW_LEVEL_SECURITY

> Row level security is not supported by `REFRESH` identifier `SYNC UNIFORM`.

The table has a [row filter](/concepts/row-filter-policies.md) (row-level security) applied, which is incompatible with the Uniform format refresh.^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

### UNSUPPORTED_READER_FEATURES

> The reader table feature(s) `<readerFeatures>` are not supported by `REFRESH` identifier `SYNC UNIFORM`.

The table has one or more reader table features enabled that are not compatible with the Uniform format refresh. The placeholder `<readerFeatures>` lists the specific unsupported features.^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

### UNSUPPORTED_TYPE

> `<sourceType>` is not supported by `REFRESH` identifier `SYNC UNIFORM`.

The source table type (`<sourceType>`) is not supported for the `SYNC UNIFORM` refresh operation.^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

### WRONG_TYPE

> `REFRESH <keyword>` identifier `SYNC UNIFORM` cannot be used for `<sourceType>`.

The `SYNC UNIFORM` refresh was attempted on a table type (`<sourceType>`) that does not support this operation. The `<keyword>` indicates the keyword used in the `REFRESH` statement.^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Sources

- delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md

## Suggested Links

- SQLSTATE error classes
- [Delta Uniform (Delta Sharing)](/concepts/delta-uniform-databricks.md)
- Delta table features
- [Column masking in Delta](/concepts/column-masks-in-delta-lake.md)
- [Row filters in Delta](/concepts/row-filters-in-unity-catalog.md)
- [REFRESH SYNC UNIFORM](/concepts/refresh-sync-uniform.md)

# Citations

1. [delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md](/references/delta_uniform_refresh_not_supported-error-condition-databricks-on-aws-9dd3f333.md)
