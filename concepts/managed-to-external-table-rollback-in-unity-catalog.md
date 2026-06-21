---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3452f62dffa93a1b640ccbad98f1728896ecd0cf13b0fb454f6e41a9a927d64a
  pageDirectory: concepts
  sources:
    - delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - managed-to-external-table-rollback-in-unity-catalog
    - MTETRIUC
  citations:
    - file: delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
title: Managed to External Table Rollback in Unity Catalog
description: The operation of reverting a Unity Catalog managed table back to an external table, which may fail under certain conditions
tags:
  - databricks
  - unity-catalog
  - delta-lake
timestamp: "2026-06-19T18:21:40.342Z"
---

# Managed to External Table Rollback in Unity Catalog

**Managed to External Table Rollback** refers to the operation of reverting a Unity Catalog managed table back to its original external (unmanaged) state. This operation is supported only within a specific time window after the table was migrated to a managed table in Unity Catalog. If the rollback fails, Databricks returns the `DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED` error (SQLSTATE 42809). The error message states: “`<table>` cannot be rolled back from managed to external table”. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Error Sub‑Conditions

The `DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED` error class contains several sub‑conditions that indicate the specific reason the rollback cannot be completed.

### TIME_WINDOW_EXCEEDED

The time window for performing the rollback has been exceeded. Rollback is only supported within `<numDays>` days after the migration to a Unity Catalog managed table. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

### TRUNCATED_HISTORY

The table’s Delta history has been truncated (e.g., by `VACUUM` or log retention settings), so the necessary commits to restore the original external state are no longer available. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

### UNEXPECTED_ERROR

An unexpected error occurred during the rollback attempt. The error details are included in the message: `"<error>"`. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

### VERSION_MISMATCH

The version of the managed Delta Log (`<managedDeltaLogVersion>`) does not match the version of the external Delta Log (`<externalDeltaLogVersion>`). This can happen if a concurrent `ALTER TABLE <tbl> UNSET MANAGED` command has already successfully rolled back the table to external. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md)
- [External Tables in Unity Catalog](/concepts/external-tables-in-unity-catalog.md)
- Delta Lake table history
- [ALTER TABLE UNSET MANAGED](/concepts/alter-table-unset-managed-command.md)
- [SQLSTATE 42809](/concepts/sqlstate-42809.md)

## Sources

- delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws-a24f2e75.md)
