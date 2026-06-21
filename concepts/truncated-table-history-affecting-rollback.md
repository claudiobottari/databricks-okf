---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0499725346e26e9637280ff35f36b21b66ffb77d401b4ebe68d37ddf4c39fe78
  pageDirectory: concepts
  sources:
    - delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - truncated-table-history-affecting-rollback
    - TTHAR
  citations:
    - file: delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
title: Truncated Table History Affecting Rollback
description: A condition where the Delta table history has been truncated (e.g., via VACUUM or retention policies), making it impossible to find all necessary commits to rollback a table to its original state.
tags:
  - databricks
  - delta-lake
  - history
  - rollback
timestamp: "2026-06-18T11:49:58.513Z"
---

# Truncated Table History Affecting Rollback

**Truncated Table History Affecting Rollback** is an error condition that occurs when attempting to roll back a Unity Catalog managed table to an external table, but the table's Delta history has been truncated and cannot provide all the necessary commits to complete the rollback operation. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Error Message

When this condition is triggered, the system returns the following error:

```
DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED
TRUNCATED_HISTORY: The table history is truncated and cannot find all the necessary commits to rollback the table to its original state.
```

^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Cause

The `TRUNCATED_HISTORY` error occurs when a table's Delta transaction log has been truncated — meaning older commits have been removed — and the rollback operation requires access to those historical commits to revert the table from a managed state back to an external table. Without the complete history, Unity Catalog cannot reconstruct the table's original external metadata and configuration. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

This error is one of several conditions that can prevent a table from being rolled back from managed to external. Other related conditions include:

| Error Condition | Description |
|-----------------|-------------|
| `TIME_WINDOW_EXCEEDED` | The time window for rollback has been exceeded. Rollback is only supported within `<numDays>` days after migration to Unity Catalog managed table. |
| `VERSION_MISMATCH` | The versions of the managed DeltaLog and external DeltaLog do not match, which can happen if a concurrent `ALTER TABLE ... UNSET MANAGED` command already successfully rolled back the table. |
| `UNEXPECTED_ERROR` | An unexpected error occurred. |

^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Impact

When this error occurs, the table cannot be rolled back from a managed table to an external table. The table remains in its managed state within Unity Catalog, and the rollback operation fails with the `DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED` error class (SQLSTATE: 42809). ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Prevention

To avoid the `TRUNCATED_HISTORY` error, ensure that table history is preserved for the duration of the rollback window. Consider the following practices:

- **Avoid aggressive history cleanup** on tables that may need to be rolled back from managed to external.
- **Understand the rollback window** — rollback is only supported within a specific number of days after migration to Unity Catalog managed table.
- **Perform rollback operations promptly** within the allowed time window to reduce the risk of history truncation.

## Related Concepts

- Delta Table History — The transaction log that records all changes to a Delta table
- [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md) — Tables managed by Unity Catalog with full governance
- External Tables — Tables where data is stored outside of Unity Catalog's managed storage
- [ALTER TABLE UNSET MANAGED](/concepts/alter-table-unset-managed-command.md) — The command used to roll back a managed table to external
- Delta Log — The transaction log that tracks table versions and commits
- Table Rollback — The process of reverting a table from managed to external state

## Sources

- delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws-a24f2e75.md)
