---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea23e2cbbbf013a93dc17711bde81e001335ce81215d41478c48aa6907005d60
  pageDirectory: concepts
  sources:
    - delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-window-for-unity-catalog-rollback
    - TWFUCR
  citations:
    - file: delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
title: Time Window for Unity Catalog Rollback
description: The constraint that rolling back a managed table to external status is only supported within a limited number of days (numDays) after the migration to Unity Catalog managed table.
tags:
  - databricks
  - unity-catalog
  - time-windows
  - table-management
timestamp: "2026-06-18T11:49:53.607Z"
---

# Time Window for Unity Catalog Rollback

The **Time Window for Unity Catalog Rollback** is a constraint that limits the ability to reverse a table migration from a managed table back to an external table in Unity Catalog. When you run `ALTER TABLE <table> UNSET MANAGED` to revert a managed table to an external table, Unity Catalog enforces a time window within which this operation is permitted. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Overview

When a table is migrated to a [Unity Catalog managed table](/concepts/unity-catalog-managed-tables.md), Databricks provides a limited window during which the migration can be rolled back. The `TIME_WINDOW_EXCEEDED` error occurs when attempting to reverse the migration after this window has closed. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Error Condition

The specific error condition is raised as part of the `DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED` error class:

```
TIME_WINDOW_EXCEEDED: The time window for rolling back the table has been exceeded. Rollback is only supported within <numDays> days after the migration to Unity Catalog managed table.
```

^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Duration

The time window for rollback is measured in days (`<numDays>`) from the date of the original migration to a Unity Catalog managed table. After this period expires, the rollback operation is no longer supported. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Related Error Conditions

The `DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED` error class also includes other conditions that can prevent a successful rollback: ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

| Condition | Description |
|-----------|-------------|
| `TRUNCATED_HISTORY` | The table history is truncated and cannot find all necessary commits to roll back the table to its original state |
| `VERSION_MISMATCH` | The versions of the managed DeltaLog and external DeltaLog do not match, possibly due to a concurrent successful rollback |
| `UNEXPECTED_ERROR` | An unexpected error occurred during the rollback attempt |

## Best Practices

- **Plan migrations carefully** by ensuring you are committed to the conversion before migrating tables to managed storage in Unity Catalog.
- **Perform rollbacks promptly** if needed, within the allowed time window after migration.
- **Preserve table history** to avoid the `TRUNCATED_HISTORY` error, which can also prevent rollback regardless of the time window.
- **Check for concurrent operations** before attempting a rollback to avoid `VERSION_MISMATCH` errors.

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that manages table ownership
- [Managed vs External tables in Unity Catalog](/concepts/managed-vs-external-tables-in-unity-catalog.md) — The distinction between table types
- DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED error class|DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED — The error class for rollback failures
- Delta Log — The transaction log that tracks table changes
- Table Migration to Unity Catalog — The process of converting external tables to managed tables

## Sources

- delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws-a24f2e75.md)
