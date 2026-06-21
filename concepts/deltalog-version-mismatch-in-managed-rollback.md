---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e213bea6918498f29ebd171d26b2e3f8b88952910369864b4ec74a27dd79aa0a
  pageDirectory: concepts
  sources:
    - delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deltalog-version-mismatch-in-managed-rollback
    - DVMIMR
  citations:
    - file: delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
title: DeltaLog Version Mismatch in Managed Rollback
description: A VERSION_MISMATCH error occurs when the managed DeltaLog and external DeltaLog versions diverge, often due to a concurrent ALTER TABLE UNSET MANAGED command succeeding first.
tags:
  - delta-lake
  - concurrency
  - version-mismatch
timestamp: "2026-06-19T10:01:55.312Z"
---

# DeltaLog Version Mismatch in Managed Rollback

**DeltaLog Version Mismatch in Managed Rollback** is a specific error condition that occurs when attempting to roll back a managed table to an external table in Unity Catalog, but the internal DeltaLog versions of the managed and external table states do not match.

## Error Condition

The error is raised with the `VERSION_MISMATCH` subcondition under the `DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED` error class. The error message reports both the managed DeltaLog version (`<managedDeltaLogVersion>`) and the external DeltaLog version (`<externalDeltaLogVersion>`) that are out of sync. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Cause

This version mismatch typically occurs when there is a concurrent `ALTER TABLE tbl UNSET MANAGED` command that has already successfully rolled back the table to external. Because the rollback operation modifies the DeltaLog, a second concurrent attempt finds that the versions no longer match, preventing the operation from proceeding. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Related Error Conditions

The `DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED` error class includes several other subconditions that may occur during managed rollback operations:

- **TIME_WINDOW_EXCEEDED**: The time window for rolling back the table has been exceeded. Rollback is only supported within a specified number of days after migration to a Unity Catalog managed table. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]
- **TRUNCATED_HISTORY**: The table history is truncated and cannot find all necessary commits to roll back the table to its original state. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]
- **UNEXPECTED_ERROR**: An unexpected error occurred during the rollback operation. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Resolution

To resolve a `VERSION_MISMATCH` error, verify whether another concurrent operation has already completed the rollback. If the table has already been successfully rolled back to external by another process, no further action is needed. If the rollback was not completed, ensure that no concurrent `ALTER TABLE ... UNSET MANAGED` operations are running simultaneously before retrying. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Related Concepts

- [Managed Tables in Unity Catalog](/concepts/managed-tables-in-unity-catalog.md)
- [External Tables in Unity Catalog](/concepts/external-tables-in-unity-catalog.md)
- DeltaLog
- [ALTER TABLE UNSET MANAGED](/concepts/alter-table-unset-managed-command.md)
- Table Migration to Unity Catalog

## Sources

- delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws-a24f2e75.md)
