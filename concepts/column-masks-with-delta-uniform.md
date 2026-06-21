---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6ea5d62007eb549fa3283d181fdd305a617c81522e29aefaa40ab82b82e8e9e4
  pageDirectory: concepts
  sources:
    - delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - column-masks-with-delta-uniform
    - CMWDU
  citations:
    - file: delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
title: Column masks with Delta Uniform
description: Column mask table features are incompatible with REFRESH SYNC UNIFORM operations on Delta tables
tags:
  - databricks
  - delta-uniform
  - column-mask
timestamp: "2026-06-19T18:28:11.987Z"
---

# Column masks with Delta Uniform

**Column masks with Delta Uniform** refers to the incompatibility between [Delta Lake](/concepts/delta-lake.md)'s column masking feature and the Delta Uniform format. When a Delta table has column masks defined, the `REFRESH SYNC UNIFORM` operation cannot be performed on that table. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Error Condition

Attempting to refresh a Delta table's uniform format synchronization when the table has column masks results in the `DELTA_UNIFORM_REFRESH_NOT_SUPPORTED` error class with the reason code `COLUMN_MASK`. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

### Error Code

```
SQLSTATE: 0AKDC
```

Full error message:

> Column mask is not supported by `REFRESH` identifier `SYNC UNIFORM`. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Cause

[Delta Uniform](/concepts/delta-uniform.md) (Delta Universal Format) enables Delta tables to be read by external systems like Apache Iceberg and Apache Hive by synchronizing metadata. However, Column Masking is a Delta Lake reader table feature that is not supported by the `SYNC UNIFORM` refresh operation. When a table has column masks enabled, the synchronization process cannot proceed. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Related Unsupported Features

Column masks are part of a broader set of Delta reader features incompatible with Delta Uniform refresh:

- **Column masks** (`COLUMN_MASK`)
- **Row-level security** (`ROW_LEVEL_SECURITY`)
- Other unsupported [reader table features](/concepts/delta-lake-reader-table-features.md) (`UNSUPPORTED_READER_FEATURES`) ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Additional Error Reasons

The `DELTA_UNIFORM_REFRESH_NOT_SUPPORTED` error class includes several other reason codes beyond column masks that may be encountered:

- `COMPATIBILITY_NOT_ENABLED` — Delta Uniform compatibility must be included in `delta.universalFormat.enabledFormats`
- `ROW_LEVEL_SECURITY` — Row filters are not supported
- `UNSUPPORTED_READER_FEATURES` — Other incompatible reader table features are present
- `UNSUPPORTED_TYPE` — The source type is not supported
- `WRONG_TYPE` — The `REFRESH` identifier cannot be used for the specified source type ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Resolution

To use Delta Uniform with a table that has column masks, you must either:

1. Remove the column masks from the table before performing the `REFRESH SYNC UNIFORM` operation.
2. Avoid using Delta Uniform on tables that require column masking.

Alternatively, consider using [Delta Sharing](/concepts/delta-sharing.md) or other methods to make masked data available externally.

## Related Concepts

- [Delta Lake Column Masking](/concepts/delta-lake-column-masking.md) — A security feature that applies masking rules to sensitive columns
- [Delta Uniform](/concepts/delta-uniform.md) — The universal format that enables cross-engine compatibility
- Iceberg and Apache Hive — External engines that can read Delta Uniform tables
- [Row filters with Delta Uniform](/concepts/row-level-security-with-delta-uniform.md) — A related incompatibility with row-level security features
- [Delta reader table features](/concepts/delta-lake-reader-table-features.md) — Features that are incompatible with uniform format refresh

## Sources

- delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md](/references/delta_uniform_refresh_not_supported-error-condition-databricks-on-aws-9dd3f333.md)
