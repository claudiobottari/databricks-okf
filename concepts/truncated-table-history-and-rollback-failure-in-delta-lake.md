---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bb78d70b7c3ab42a29e60570804e9d62991aab7919cc066ec0f057a7a5e93501
  pageDirectory: concepts
  sources:
    - delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - truncated-table-history-and-rollback-failure-in-delta-lake
    - Rollback Failure in Delta Lake and Truncated Table History
    - TTHARFIDL
  citations:
    - file: delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
title: Truncated Table History and Rollback Failure in Delta Lake
description: When Delta table history is truncated (e.g., VACUUM or log cleanup), the necessary commits to rollback a managed-to-external migration may be missing, causing TRUNCATED_HISTORY error.
tags:
  - delta-lake
  - table-history
  - rollback
timestamp: "2026-06-19T10:02:25.628Z"
---

Here is the wiki page for "Truncated Table History and Rollback Failure in Delta Lake".

---

## Truncated Table History and Rollback Failure in Delta Lake

**Truncated Table History and Rollback Failure** is a specific error condition that occurs in [Delta Lake](/concepts/delta-lake.md) on Databricks when attempting to roll back a table from a managed table to an external table using `ALTER TABLE ... UNSET MANAGED`. The rollback fails because the table's transaction history has been truncated, making it impossible to find all the necessary commits to restore the table to its original external state. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

### Error Condition

This error is identified by the `TRUNCATED_HISTORY` sub-condition within the broader `DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED` error class. It returns the SQLSTATE code `42809` and produces the following error message:

```
<table> cannot be rolled back from managed to external table.
```

^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

### Cause

The rollback operation requires a complete history of all Delta transaction log commits to reverse the migration from a managed table to an external table. If the table history has been truncated—typically through operations like `VACUUM` or manual deletion of old Delta log files—the missing commits prevent Delta Lake from reconstructing the necessary state for a successful rollback. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

### Related Error Conditions

The `DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED` error class includes several other sub-conditions:

- **TIME_WINDOW_EXCEEDED**: The time window for performing the rollback has been exceeded. Rollback is only supported within `<numDays>` days after the migration to a Unity Catalog managed table. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]
- **UNEXPECTED_ERROR**: An unexpected generic error occurred. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]
- **VERSION_MISMATCH**: The versions of the managed `DeltaLog` (`<managedDeltaLogVersion>`) and external `DeltaLog` (`<externalDeltaLogVersion>`) do not match. This can occur if a concurrent `ALTER TABLE ... UNSET MANAGED` command has already successfully rolled back the table. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

### Prevention

To avoid this error, ensure that the Delta table transaction history is preserved during the rollback window. Key preventive measures include:

- Avoid running `VACUUM` on Delta tables that may need to be rolled back to external tables. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]
- Perform the rollback operation within the defined time window after the migration to a managed table. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]
- Maintain sufficient [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) retention to support rollback operations. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

### Related Concepts

- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md)
- [ALTER TABLE ... UNSET MANAGED](/concepts/alter-table-unset-managed-command.md)
- [Managed vs External Tables](/concepts/managed-vs-external-tables-in-unity-catalog.md)
- Table Migration to Unity Catalog
- VACUUM in Delta Lake

### Sources

- delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws-a24f2e75.md)
