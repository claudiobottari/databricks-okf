---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6c2c51a95c81f58800810a44812878366cdd5edad1a58bd55f1f0a2d441e13e3
  pageDirectory: concepts
  sources:
    - delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
    - describe-history-databricks-on-aws.md
  confidence: 0.8
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - table_changes-function
    - table_changes Function
    - table_changes function
    - Table changes
    - table_changes
  citations:
    - file: describe-history-databricks-on-aws.md
    - file: delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
title: table_changes function
description: A Delta Lake function that reads Change Data Feed (CDF) records, but is unsupported on views.
tags:
  - delta-lake
  - function
  - change-data-feed
timestamp: "2026-06-19T18:27:17.633Z"
---

# table_changes Function

The `table_changes` function is a Delta Lake SQL function that returns a row-level changelog for [Delta tables](/concepts/delta-lake-table.md), enabling change data capture (CDC) workflows by tracking inserts, updates, and deletes over a specified time range or version interval. ^[describe-history-databricks-on-aws.md]

## Overview

The `table_changes` function provides a way to consume incremental changes from Delta tables without scanning the entire dataset. It is commonly used for incremental processing, [data synchronization](/concepts/dataset-synchronization.md), and replication pipelines.

When invoked, the function returns the table's data columns along with additional metadata columns:
- `_change_type` — Indicates the operation: `insert`, `update`, `delete`, or `update_preimage` (the row before an update).
- `_commit_version` — The Delta Lake version number associated with the change.
- `_commit_timestamp` — The timestamp when the change was committed.

## Syntax

```sql
SELECT *
FROM table_changes('table_name', start_version)
```

Or with a starting timestamp:

```sql
SELECT *
FROM table_changes('table_name', start_timestamp)
```

## Parameters

- **table_name**: A string literal specifying the name or path of the [Delta table](/concepts/delta-lake-table.md) to track changes for.
- **start_version** or **start_timestamp**: The starting point (version number or timestamp) from which to return changes. Both are inclusive.

## Requirements

- The table must be a Delta table with [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) enabled (via `delta.enableChangeDataFeed = true`).
- The table history must be retained; by default, Delta Lake retains history for 30 days.

## Limitations

The `table_changes` function does not support querying changes against views. If applied to a view, it returns an error with a specific reason: ^[delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md]

| Reason | Description |
|--------|-------------|
| `MULTIPLE_RELATIONS` | The view references more than one relation |
| `NON_DETERMINISTIC_EXPRESSIONS` | The view contains non-deterministic expressions |
| `NOT_DELTA_TABLE` | The view does not reference a Delta table |
| `NOT_SHARED_VIEW` | The view is not an OpenSharing view |
| `SUBQUERY` | The view contains a subquery |
| `UNSUPPORTED_OPERATOR` | The view contains an operator that is not allowed |

## Usage Examples

### Track changes since a specific date

```sql
SELECT * FROM table_changes('sales_data', '2024-01-01');
```

This returns all changes made to the `sales_data` table since January 1, 2024.

### Filter by change type

```sql
SELECT *
FROM table_changes('employees', '2024-01-01')
WHERE _change_type = 'delete';
```

This returns only deleted records from the `employees` table since the specified date.

## Related Concepts

- [DESCRIBE HISTORY](/concepts/describe-history.md) — Returns provenance information for each write to a table
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) — The underlying mechanism that powers `table_changes`
- [Delta table](/concepts/delta-lake-table.md) — The primary data format supporting change tracking
- Temporal queries — Querying table state at specific points in time

## Sources

- delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md
- describe-history-databricks-on-aws.md

# Citations

1. [describe-history-databricks-on-aws.md](/references/describe-history-databricks-on-aws-c4aeec74.md)
2. [delta_table_changes_view_unsupported-error-condition-databricks-on-aws.md](/references/delta_table_changes_view_unsupported-error-condition-databricks-on-aws-c5e200eb.md)
