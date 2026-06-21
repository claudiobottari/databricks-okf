---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7c3636401acf74e4ee4428b814e64b9df30c3e18fbc64c7d1a4049c76e409fa7
  pageDirectory: concepts
  sources:
    - delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - truncated_history-rollback-error
    - TRE
  citations:
    - file: delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
title: TRUNCATED_HISTORY rollback error
description: A sub-error of DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED indicating the Delta table history has been truncated, preventing the system from finding all necessary commits to rollback.
tags:
  - error-messages
  - databricks
  - delta-lake
timestamp: "2026-06-18T15:16:38.493Z"
---

# TRUNCATED_HISTORY Rollback Error

The **TRUNCATED_HISTORY rollback error** is a specific error condition that occurs when attempting to roll back a managed [Unity Catalog](/concepts/unity-catalog.md) table to an external table using `ALTER TABLE ... UNSET MANAGED`, but the rollback cannot complete because the table's history has been truncated.^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Error Message

When this error occurs, it appears as part of the DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED error class with the following description:

> The table history is truncated and cannot find all the necessary commits to rollback the table to its original state.

^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Cause

The `ALTER TABLE ... UNSET MANAGED` operation requires access to the full [Delta Lake](/concepts/delta-lake.md) history of the table to reverse the migration from an external table to a managed table. If the table's [Delta transaction log](/concepts/delta-transaction-log.md) has been Delta table retention policy|cleaned up or vacuumed past the point of migration, the necessary commit records are no longer available.^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

Without those historical commits, the system cannot reconstruct the table's original external state, and the rollback fails with `TRUNCATED_HISTORY`.^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Related Error Conditions

The `DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED` error class includes several sub-conditions that may also be relevant:^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

| Error Condition | Description |
|----------------|-------------|
| `TIME_WINDOW_EXCEEDED` | Rollback is only supported within the retention window (specified number of days) after migration |
| `TRUNCATED_HISTORY` | Table history has been truncated; necessary commits are missing |
| `VERSION_MISMATCH` | The managed and external DeltaLog versions differ due to concurrent operations |
| `UNEXPECTED_ERROR` | An unspecified error occurred |

## Resolution

Once the table history has been truncated, the rollback operation is no longer possible. There is no automatic recovery mechanism to restore the truncated history.^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

To avoid this error:

- Ensure rollback occurs within the supported time window after migration.
- Configure an appropriate Delta table retention policy (for example, by adjusting `delta.logRetentionDuration` or vacuum settings) to preserve history long enough for the rollback window.
- Do not run VACUUM operations that would remove historical commits from tables that might need to be rolled back.

## Related Concepts

- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md)
- [Managed vs External tables in Unity Catalog](/concepts/managed-vs-external-tables-in-unity-catalog.md)
- Delta table history and versioning
- TIME_WINDOW_EXCEEDED error|TIME_WINDOW_EXCEEDED error condition
- VERSION_MISMATCH error|VERSION_MISMATCH error condition
- UNEXPECTED_ERROR
- Delta retention policy configuration

## Sources

- delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws-a24f2e75.md)
