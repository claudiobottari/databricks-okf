---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 18bb2237e3ba8257074039b12c438f246f7a05a5af4cadd711267223cad1a9a9
  pageDirectory: concepts
  sources:
    - delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-log-version-mismatch-on-concurrent-rollback
    - DLVMOCR
  citations:
    - file: delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
title: Delta Log Version Mismatch on Concurrent Rollback
description: A concurrency conflict where the managed and external DeltaLog versions diverge, typically because a concurrent ALTER TABLE UNSET MANAGED command already succeeded.
tags:
  - databricks
  - delta-lake
  - concurrency
  - versioning
timestamp: "2026-06-18T11:49:58.932Z"
---

# Delta Log Version Mismatch on Concurrent Rollback

The **Delta Log Version Mismatch on Concurrent Rollback** error occurs when an `ALTER TABLE tbl UNSET MANAGED` command attempts to roll back a managed table to an external table, but a concurrent transaction has already completed the rollback, causing the managed and external Delta Log versions to diverge. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Error Condition (VERSION_MISMATCH)

This is one of the error sub‑conditions under the `DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED` error class (SQLSTATE 42809). The full error message includes the version numbers of both logs:

```
The versions of the managed DeltaLog (<managedDeltaLogVersion>) and external DeltaLog (<externalDeltaLogVersion>) do not match.
```

^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Cause

The mismatch is caused by a concurrent `ALTER TABLE tbl UNSET MANAGED` command that already successfully rolled back the table to an external table. When the second command reads the logs, it sees a different external Delta Log version than the managed Delta Log version it was expecting, and the operation fails. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

Other possible sub‑conditions for the same `DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED` error include:

- `TIME_WINDOW_EXCEEDED` – The rollback must occur within a limited number of days after migration to a Unity Catalog managed table.
- `TRUNCATED_HISTORY` – The table history was truncated and cannot find all commits needed to roll back.
- `UNEXPECTED_ERROR` – An unexpected error occurred. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Solution

The `VERSION_MISMATCH` condition indicates that another transaction has already performed the rollback. The table is now external, so the attempted operation is effectively redundant. To resolve the error:

- Verify the current state of the table using `DESCRIBE EXTENDED <table>` or querying the Unity Catalog metadata.
- If the table is already external, no further action is required.
- If you still need to reapply the change (e.g., because the other transaction rolled back the wrong table), re‑run the `ALTER TABLE tbl UNSET MANAGED` command again after confirming the logs are synchronized.

## Related Concepts

- [Managed Table](/concepts/unity-catalog-managed-tables.md) – A table whose data and metadata are fully managed by Unity Catalog.
- External Table – A table that references data stored outside the managed location.
- [Unity Catalog](/concepts/unity-catalog.md) – The data governance layer that manages table ownership and lifecycle.
- Delta Log – The transaction log that records all changes to a Delta table.
- [ALTER TABLE UNSET MANAGED](/concepts/alter-table-unset-managed-command.md) – The command that converts a managed table to an external table.
- DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED error class|DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED – The error class that includes the VERSION_MISMATCH condition.

## Sources

- delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws-a24f2e75.md)
