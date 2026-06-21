---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: edab28b63c39bc041f9d9ced4bb9b50a3170fb7c9d6c8ac3e3183e1e53701804
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - change-data-feed-metadata-column-conflict
    - CDFMCC
  citations:
    - file: delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
title: Change Data Feed Metadata Column Conflict
description: A conflict condition where a table contains a column named '_change_type' that clashes with Change Data Feed (CDC) metadata columns, preventing row-level conflict detection.
tags:
  - delta-lake
  - change-data-feed
  - metadata
timestamp: "2026-06-19T15:03:27.669Z"
---

# Change Data Feed Metadata Column Conflict

**Change Data Feed Metadata Column Conflict** is a specific error condition that occurs when a Delta table contains a user-defined column named `_change_type`, which conflicts with internal metadata columns used by the [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) feature. This conflict prevents row-level conflict detection from functioning correctly during concurrent write operations.

## Error Details

When a transaction attempts to perform delete or update operations on a table that has a column named `_change_type`, the system identifies this as a naming conflict with the reserved metadata column that Change Data Feed uses to track changes. The error message returned is:

```
The table contains a column named '_change_type' which conflicts with Change Data Feed (CDC) metadata columns, preventing row-level conflict detection.
```

^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

This is a sub-condition of the `DELTA_CONCURRENT_DELETE_DELETE` error class (SQLSTATE: 2D521), which indicates a transaction conflict was detected with a concurrent operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Cause

The `_change_type` column is a reserved metadata column name that [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) uses internally to record the type of change applied to each row (such as insert, update, or delete). When a user-created column with the same name exists in the table schema, the system cannot distinguish between user data and Change Data Feed metadata, breaking the row-level conflict resolution mechanism. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Resolution

To resolve this conflict, choose one of the following approaches:

1. **Rename the conflicting column**: Change the name of the user-defined `_change_type` column to something that does not conflict with CDF metadata column names.
2. **Disable Change Data Feed**: If Change Data Feed is not required for the table, disable it to remove the need for the reserved `_change_type` metadata column.

^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Related Concepts

- [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md) – The feature that tracks row-level changes in Delta tables
- [Delta Lake Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) – How Delta Lake handles concurrent transactions
- Delta Table Metadata Columns – Reserved column names used internally by Delta Lake features
- DELTA_CONCURRENT_DELETE_DELETE Error Class|delta_concurrent_delete_delete_error_class – The broader error class for transaction conflicts
- [Row-Level Conflict Detection](/concepts/delta-lake-row-level-conflict-detection.md) – The mechanism that resolves conflicts at the row level

## Sources

- delta_concurrent_delete_delete-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_delete-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_delete-error-condition-databricks-on-aws-6fcec7a7.md)
