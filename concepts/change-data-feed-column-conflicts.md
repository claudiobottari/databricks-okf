---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 44c4c94b9cee08352e1735e68bd5d5307938b6e15c68592662509894c736c29f
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_read-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - change-data-feed-column-conflicts
    - CDFCC
  citations:
    - file: delta_concurrent_delete_read-error-condition-databricks-on-aws.md
title: Change Data Feed Column Conflicts
description: An error condition where a user-created column named '_change_type' conflicts with Change Data Feed (CDF) metadata columns, preventing row-level conflict detection in Delta Lake.
tags:
  - delta-lake
  - change-data-feed
  - error-messages
timestamp: "2026-06-19T15:03:46.692Z"
---

# Change Data Feed Column Conflicts

**Change Data Feed Column Conflicts** occur when a Delta table contains a user-defined column named `_change_type`, which conflicts with the metadata columns used by [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) (CDF) for row-level conflict detection. This conflict prevents Delta Lake from performing row-level conflict resolution during concurrent write operations.^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Error Condition

When a table has a column named `_change_type` and Change Data Feed is enabled, operations that trigger row-level conflict detection fail with the following error:^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

```
DELTA_CONCURRENT_DELETE_READ.CHANGE_TYPE_COLUMN
```

This error is a specific subtype of the `DELTA_CONCURRENT_DELETE_READ` error class, which indicates a transaction conflict where a concurrent operation deleted data that the current transaction had read. The full error message includes a reference to documentation for more information.^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Cause

The `_change_type` column is a reserved metadata column that Databricks uses internally to track row-level changes when [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) is enabled on a table. If a table already contains a column with this name — whether created explicitly or through schema evolution — Delta Lake cannot distinguish between user data and CDC metadata, making row-level conflict detection impossible.^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Resolution Options

### Option 1: Rename the Conflicting Column

Rename the `_change_type` column in the table to a name that does not conflict with CDC metadata columns. After renaming, row-level conflict detection can function normally.^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### Option 2: Disable Change Data Feed

If the table does not require CDC functionality, disable [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) on the table. This removes the need for the `_change_type` metadata column, allowing the existing column to remain without conflict.^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Affected Operations

Any operation that performs row-level conflict resolution is affected, including:^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

- **MERGE** operations with concurrent deletes
- **UPDATE** operations with concurrent deletes
- **DELETE** operations with concurrent deletes
- Any transaction involving row-level conflict detection on a table with a `_change_type` column

## Prevention

- Avoid naming any columns `_change_type` in tables where [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) is or will be enabled.^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]
- Review schema design to ensure no column names conflict with reserved CDC metadata column names.
- When enabling CDC on existing tables, check for column name conflicts first.

## Related Concepts

- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) — The feature that uses `_change_type` as a metadata column
- DELTA_CONCURRENT_DELETE_READ Error|Delta Concurrent Delete Read Error — The parent error class containing the `CHANGE_TYPE_COLUMN` subtype
- [Row-Level Conflict Detection](/concepts/delta-lake-row-level-conflict-detection.md) — The conflict resolution mechanism affected by this error
- [Delta Table](/concepts/delta-lake-table.md) — The table type where this conflict occurs
- [MERGE INTO](/concepts/merge-into-delta-lake.md) — An operation commonly affected by column conflicts

## Sources

- delta_concurrent_delete_read-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_read-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_read-error-condition-databricks-on-aws-d0015916.md)
