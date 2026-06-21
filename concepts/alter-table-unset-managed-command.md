---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7b04e18f7d46d2cdd41b4ebb53ec6d5a87105b48aa38bf655cd55caa2e807a6a
  pageDirectory: concepts
  sources:
    - delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - alter-table-unset-managed-command
    - ATUMC
    - ALTER TABLE ... UNSET MANAGED
    - ALTER TABLE UNSET MANAGED
  citations:
    - file: delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
title: ALTER TABLE UNSET MANAGED command
description: A Databricks SQL command used to roll back a Unity Catalog managed table to its original external table state.
tags:
  - sql
  - sql-commands
  - unity-catalog
timestamp: "2026-06-19T10:02:06.709Z"
---

# ALTER TABLE UNSET MANAGED command

The `ALTER TABLE ... UNSET MANAGED` command converts a Unity Catalog managed table back into an external table. This rollback operation is supported only under specific conditions, and attempting it when those conditions are not met raises the `DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED` error. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Error condition: DELTA\_ALTER\_TABLE\_UNSET\_MANAGED\_FAILED

**SQLSTATE**: `42809` *— Syntax Error or Access Rule Violation* ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

The error message states that `<table>` cannot be rolled back from managed to external table. The error includes a sub‑reason that identifies the specific cause of failure. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

### Sub‑error reasons

| Reason | Description |
|--------|-------------|
| `TIME_WINDOW_EXCEEDED` | The time window for rolling back the table has been exceeded. Rollback is only supported within `<numDays>` days after the migration to Unity Catalog managed table. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md] |
| `TRUNCATED_HISTORY` | The table history is truncated and cannot find all the necessary commits to rollback the table to its original state. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md] |
| `UNEXPECTED_ERROR` | An unexpected error occurred. `== Error == <error>` ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md] |
| `VERSION_MISMATCH` | The versions of the managed DeltaLog (`<managedDeltaLogVersion>`) and external DeltaLog (`<externalDeltaLogVersion>`) do not match. This can happen if there is a concurrent `ALTER TABLE tbl UNSET MANAGED` command that already successfully rolled back the table to external. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md] |

## Common causes

The command fails primarily because the table’s Delta transaction history no longer contains the original external-table metadata. This can happen when the retention window has passed (`TIME_WINDOW_EXCEEDED`), the history has been vacuumed or truncated (`TRUNCATED_HISTORY`), or another concurrent rollback has modified the table in a conflicting way (`VERSION_MISMATCH`). ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Related concepts

- [Managed Tables in Unity Catalog](/concepts/managed-tables-in-unity-catalog.md) – Tables whose data and metadata are fully managed by Unity Catalog.
- [External Tables in Unity Catalog](/concepts/external-tables-in-unity-catalog.md) – Tables that reference data stored outside the catalog’s managed location.
- [Delta Lake](/concepts/delta-lake.md) – The transaction log that underpins these rollback operations.
- ALTER TABLE – The broader SQL command family for modifying table properties.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that enforces the rollback constraints.

## Sources

- delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws-a24f2e75.md)
