---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7cc52cf27b3921f57c69c41a459ff222cdf978c9b3270db4591bac2f25be7b76
  pageDirectory: concepts
  sources:
    - delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - sqlstate-0akdc-feature-not-supported
    - S0(NS
    - Feature not supported
    - SQLSTATE 0AKDC — Feature Not Supported (table_changes view)
  citations:
    - file: delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
    - file: delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md
title: SQLSTATE 0AKDC (Feature Not Supported)
description: A Databricks SQLSTATE class indicating a feature is not supported by the source or operation context.
tags:
  - databricks
  - sqlstate
  - error-classification
timestamp: "2026-06-19T15:02:05.822Z"
---

# SQLSTATE 0AKDC — Feature Not Supported

**SQLSTATE 0AKDC** is a Databricks error that occurs when a requested feature is not supported for the given operation. The SQLSTATE class `0A` indicates a general *Feature Not Supported* error. The specific sub‑code `KDC` corresponds to two distinct error conditions: `DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED` and `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE`. ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md, delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Error Conditions

### DELTA_TABLE_CHANGES_VIEW_UNSUPPORTED

This error is raised when the `table_changes` function is called on a view that does not meet the required conditions for change data capture. The error message generally reads:

```
table_changes on view '<viewName>' is not supported.
```

^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

Common causes are identified by sub‑reason codes. For details, see the dedicated page on [SQLSTATE 0AKDC — Feature Not Supported (table_changes view)](/concepts/sqlstate-0akdc-feature-not-supported.md).

### DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE

This error is raised when the `CLONE` operation with history is attempted on an unsupported source table. The full error class is `DELTA_CLONE_WITH_HISTORY_UNSUPPORTED_SOURCE`. ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

Two sub‑reasons are defined:

- **NON_DELTA** – The source table is of a format other than Delta (e.g., Parquet, CSV, JSON). The error message reads:  
  `Source table of <format> format is not supported.` ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]
- **TIME_TRAVELLED_BY_TIMESTAMP** – The source table uses a timestamp‑based time travel specification. The error message reads:  
  `Source table time travelled by timestamp is not supported.` ^[delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md]

## Related Concepts

- [CLONE with history](/concepts/delta-clone-with-history.md) – The Delta feature that triggers this error for non‑Delta or time‑travelled sources.
- [Delta table](/concepts/delta-lake-table.md) – The required source format for `CLONE` with history.
- table_changes function|table_changes – The function that triggers the view unsupported error.
- Change Data Capture (CDC) – The broader feature set for capturing row changes.
- [Delta Sharing](/concepts/delta-sharing.md) – Protocol that imposes additional view requirements for `table_changes`.

## Sources

- delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
- delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md](/references/delta_table_changes_view_unsupported-error-condition-databricks-on-aws-c5e200eb.md)
2. [delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_clone_with_history_unsupported_source-error-condition-databricks-on-aws-0e0c9b78.md)
