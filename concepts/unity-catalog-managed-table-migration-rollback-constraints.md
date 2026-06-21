---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 05524c0e45e03c68b60f38201419606c46a3e9a0ca8823ae0840bbf87d303414
  pageDirectory: concepts
  sources:
    - delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - unity-catalog-managed-table-migration-rollback-constraints
    - UCMTMRC
  citations:
    - file: delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
title: Unity Catalog Managed Table Migration Rollback Constraints
description: Constraints governing the ability to roll back a table from managed to external in Unity Catalog, including time windows and history retention requirements.
tags:
  - databricks
  - unity-catalog
  - migration
  - governance
timestamp: "2026-06-18T15:16:45.983Z"
---

# Unity Catalog Managed Table Migration Rollback Constraints

**Unity Catalog Managed Table Migration Rollback Constraints** refer to the conditions under which a Unity Catalog managed table cannot be rolled back to an external (unmanaged) table. When a user executes `ALTER TABLE <table> UNSET MANAGED`, the operation may fail with the error class `DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED` if one or more of these constraints are violated. Understanding these constraints helps administrators plan migrations and avoid irrecoverable states.^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Rollback Time Window Exceeded

The rollback operation must be performed within a specific time window after the table was originally migrated to a Unity Catalog managed table. If the time since migration exceeds the allowed number of days (`<numDays>`), the rollback fails with the **TIME_WINDOW_EXCEEDED** sub‑condition.^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Truncated Table History

The Delta table’s commit history must contain all the information needed to reconstruct its original external state. If the history has been truncated (e.g., by `VACUUM` or automatic cleanup), the rollback fails with **TRUNCATED_HISTORY**, because the required commits are no longer available.^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Version Mismatch Between Delta Logs

A managed table maintains two Delta transaction logs: the managed DeltaLog and the (shadow) external DeltaLog. The rollback succeeds only when the versions of these two logs match. A **VERSION_MISMATCH** error occurs when the managed DeltaLog version (`<managedDeltaLogVersion>`) differs from the external DeltaLog version (`<externalDeltaLogVersion>`). This commonly happens if a concurrent `ALTER TABLE ... UNSET MANAGED` command has already successfully rolled back the table to external, leaving inconsistent versions for a subsequent attempt.^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Unexpected Error

A generic **UNEXPECTED_ERROR** sub‑condition may also occur, with the details provided in the `<error>` field. This indicates an unforeseen failure during the rollback process that does not match the other known constraints.^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Managing and Avoiding Rollback Failures

To avoid rollback failures:

- Perform the rollback within the time window that your Unity Catalog environment enforces (typically a fixed number of days after migration).
- Preserve table history by avoiding aggressive `VACUUM` or retention‑shortening operations during the rollback window.
- Ensure that no other concurrent operations are issuing `UNSET MANAGED` on the same table.

When a rollback fails, the error class and sub‑condition help diagnose which constraint was violated.

## Related Concepts

- [Unity Catalog Managed Table](/concepts/unity-catalog-managed-tables.md)
- External (Unmanaged) Table
- [ALTER TABLE UNSET MANAGED](/concepts/alter-table-unset-managed-command.md)
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md)
- DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED error class
- VACUUM and History Retention

## Sources

- delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws-a24f2e75.md)
