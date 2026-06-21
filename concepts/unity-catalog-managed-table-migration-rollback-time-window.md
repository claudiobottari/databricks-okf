---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cad6fd7da90a789146f622481d768cf07221801b71e011372bad0e454cc07cfe
  pageDirectory: concepts
  sources:
    - delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-managed-table-migration-rollback-time-window
    - UCMTMRTW
  citations:
    - file: delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
title: Unity Catalog Managed Table Migration Rollback Time Window
description: The time-limited window (in days) after migrating a table to Unity Catalog managed during which rollback via ALTER TABLE UNSET MANAGED is supported.
tags:
  - unity-catalog
  - time-window
  - rollback
timestamp: "2026-06-19T10:01:52.188Z"
---

# Unity Catalog Managed Table Migration Rollback Time Window

The **Unity Catalog Managed Table Migration Rollback Time Window** is the limited period during which a table that has been converted to a [Unity Catalog](/concepts/unity-catalog.md) [Managed Table](/concepts/unity-catalog-managed-tables.md) can be rolled back to an External Table. After this window expires, the rollback operation is no longer supported. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Time Window

When a table is migrated from an external table to a Unity Catalog managed table, a rollback to the original external state is permitted only within a configurable number of days. The exact duration is represented as `<numDays>` in the error message; the source document does not specify a default value. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Error Condition: TIME_WINDOW_EXCEEDED

If a user attempts to roll back a managed table to an external table after the time window has elapsed, the operation fails with the error class `DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED` and the reason `TIME_WINDOW_EXCEEDED`. The full error message states:

> `<table>` cannot be rolled back from managed to external table.
> The time window for rolling back the table has been exceeded. Rollback is only supported within `<numDays>` days after the migration to Unity Catalog managed table.

^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Other Failure Reasons (for context)

The same error class includes additional failure reasons that are unrelated to the time window:

- **TRUNCATED_HISTORY** – The table’s Delta history has been truncated, so necessary commits for rollback are missing.
- **VERSION_MISMATCH** – The managed Delta log and external Delta log versions do not match, often because a concurrent rollback already succeeded.
- **UNEXPECTED_ERROR** – An unspecified error occurred.

^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Implications

After the rollback window closes, a managed table cannot be converted back to an external table via the `ALTER TABLE ... UNSET MANAGED` command. This enforces a commitment to the managed state and prevents accidental or late reversals. Users must plan migrations carefully and perform any desired rollback within the allowed period. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Related Concepts

- DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED error class|DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED – The full error class for rollback failures.
- [Managed Table](/concepts/unity-catalog-managed-tables.md) – A table whose data and metadata are fully managed by Unity Catalog.
- External Table – A table that references data stored outside Unity Catalog.
- Table Migration to Unity Catalog – The process of converting an external table to a managed table.
- [Delta Lake](/concepts/delta-lake.md) – The storage layer underlying Unity Catalog tables.
- Rollback in Unity Catalog – The operation to undo a managed table migration.

## Sources

- delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws-a24f2e75.md)
