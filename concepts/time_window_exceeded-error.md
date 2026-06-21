---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a3ade17298df78b12995ab149791b2ac1a181a48f9d667766e4c2e5a65609b36
  pageDirectory: concepts
  sources:
    - delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time_window_exceeded-error
    - TIME_WINDOW_EXCEEDED error condition
  citations:
    - file: delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
title: TIME_WINDOW_EXCEEDED error
description: A sub-error of DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED indicating the rollback window (measured in days after migration to Unity Catalog) has expired.
tags:
  - error-messages
  - databricks
  - rollback
timestamp: "2026-06-18T15:16:35.233Z"
---

# TIME_WINDOW_EXCEEDED Error

The **TIME_WINDOW_EXCEEDED** error occurs when attempting to roll back a table from a managed table to an external table in Unity Catalog, but the allowed time window for this operation has expired.

## Error Condition

This error is a sub-condition of the `DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED` error class (SQLSTATE: 42809). It indicates that the time window for rolling back the table has been exceeded. Rollback is only supported within a specified number of days (`<numDays>`) after the migration to a Unity Catalog managed table. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Cause

When a table is migrated to a Unity Catalog managed table, there is a limited time window during which the migration can be reversed. If you attempt to use `ALTER TABLE ... UNSET MANAGED` after this window has passed, the system returns the `TIME_WINDOW_EXCEEDED` error because the rollback period has expired. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Related Error Conditions

The `DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED` error class includes several related conditions:

| Condition | Description |
|-----------|-------------|
| `TIME_WINDOW_EXCEEDED` | The rollback time window has expired |
| `TRUNCATED_HISTORY` | Table history is truncated and necessary commits cannot be found |
| `VERSION_MISMATCH` | Versions of managed and external DeltaLogs do not match |
| `UNEXPECTED_ERROR` | An unexpected error occurred |

^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Resolution

To resolve this error, you must perform the rollback within the allowed time window after migration. If the window has already passed, the table cannot be rolled back from managed to external using this method. Consider alternative approaches such as:

- Creating a new external table and copying data from the managed table
- Consulting with your Databricks administrator for migration reversal options

## Related Concepts

- [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md) – Tables managed by Unity Catalog with full governance
- External Tables – Tables where data is stored outside of Unity Catalog's managed storage
- DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED error class|DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED – The parent error class for this condition
- Table Migration – The process of moving tables to Unity Catalog

## Sources

- delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws-a24f2e75.md)
