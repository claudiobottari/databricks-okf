---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 270b8f02c5a1601a9771897953b1aaf5031c6751d710f4f075e732356b26930e
  pageDirectory: concepts
  sources:
    - delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sqlstate-55019
  citations:
    - file: delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md
title: SQLSTATE 55019
description: "A SQL state code (class 55: Object not in prerequisite state) associated with table migration failures in Databricks."
tags:
  - sqlstate
  - error-codes
  - databricks
timestamp: "2026-06-19T18:21:31.748Z"
---

# SQLSTATE 55019

**SQLSTATE 55019** is a SQL standard error class indicating that an object is not in the prerequisite state required for the requested operation. In Databricks, this error is most commonly encountered when attempting to convert an unmanaged Delta table to a managed table using `ALTER TABLE ... SET MANAGED`. ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Error Class

SQLSTATE 55019 belongs to **Class 55 – Object not in prerequisite state**. This class groups errors where an operation fails because the target object is not in the correct state to perform the requested transformation. ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Error Message

The generic error message for SQLSTATE 55019 when related to table migration is:

```
DELTA_ALTER_TABLE_SET_MANAGED_TABLE_NOT_MIGRATABLE: ALTER TABLE <table> SET MANAGED is unable to migrate the given table. Make sure the table is in a valid state and retry the command. If the issue persists, contact Databricks support.
```

^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

### METADATA_CLEANUP_ERROR Sub-Error

A specific sub-error condition can accompany the main error. When the `METADATA_CLEANUP_ERROR` sub-condition occurs, the full error message is:

```
Unable to create checkpoint or clean up old metadata files before migrating the table.

== Error ==
<error>
```

Where `<error>` is replaced by the underlying cause (e.g., a filesystem or permission error). ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Cause

The error occurs when `ALTER TABLE ... SET MANAGED` is executed on a table that is not in a valid state for migration. The most common cause is the `METADATA_CLEANUP_ERROR` sub-condition, which indicates an inability to create a checkpoint or clean up old metadata files before migrating the table. This can happen due to:

- Filesystem issues or errors on the underlying storage location
- Insufficient permissions on the [Delta transaction log](/concepts/delta-transaction-log.md) directory
- Corruption in the Delta transaction log
- Transient storage latency or connectivity problems ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Resolution

1. **Check the table's current state.** Verify that the table is valid and not locked by another operation. Use `DESCRIBE EXTENDED <table>` to inspect the table type and location.
2. **Retry the command.** Some transient issues (e.g., temporary storage latency) may resolve on retry.
3. **Inspect the underlying storage.** If the `METADATA_CLEANUP_ERROR` sub-error appears, examine the storage location for the Delta log directory (`_delta_log/`). Ensure the location is accessible and that the [Metastore](/concepts/metastore.md) user has write permissions.
4. **Run `FSCK REPAIR TABLE`** to fix any metadata inconsistencies before retrying the migration.
5. **Check for concurrent operations.** Ensure no other session is running OPTIMIZE, VACUUM, or other maintenance commands on the table.
6. **Contact Databricks support** if the issue persists after taking the above steps. ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Related Concepts

- Error classes in Databricks — The framework that groups errors by SQLSTATE codes
- SQLSTATE codes — Standard SQL error codes for diagnosing problems
- [Delta Lake](/concepts/delta-lake.md) — The storage format underlying the ALTER TABLE migration
- ALTER TABLE — The SQL command that triggers this error
- Managed tables vs unmanaged tables — The difference between table types that SET MANAGED migrates between
- [Delta transaction log](/concepts/delta-transaction-log.md) — The metadata layer whose state determines migration eligibility
- METADATA_CLEANUP_ERROR — A specific sub-error of this SQLSTATE
- [FSCK REPAIR TABLE](/concepts/fsck-repair-table.md) — Command to fix metadata inconsistencies

## Sources

- delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md](/references/delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws-c36210c9.md)
