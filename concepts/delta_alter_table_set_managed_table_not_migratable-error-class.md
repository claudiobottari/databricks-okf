---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1e40eec1c96d99237d5f23665ff1b32db96f2cd550427dac42422cfaa39e7354
  pageDirectory: concepts
  sources:
    - delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_alter_table_set_managed_table_not_migratable-error-class
    - DEC
  citations:
    - file: delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md
title: DELTA_ALTER_TABLE_SET_MANAGED_TABLE_NOT_MIGRATABLE error class
description: A Databricks error class indicating that ALTER TABLE SET MANAGED failed to migrate the given table to a managed table.
tags:
  - error-messages
  - databricks
  - delta-lake
timestamp: "2026-06-19T18:21:31.738Z"
---

# DELTA_ALTER_TABLE_SET_MANAGED_TABLE_NOT_MIGRATABLE error class

**SQLSTATE: 55019** (Object not in prerequisite state) ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

The `DELTA_ALTER_TABLE_SET_MANAGED_TABLE_NOT_MIGRATABLE` error occurs when an `ALTER TABLE <table> SET MANAGED` command fails to migrate the specified table. This error indicates that the table is not in a valid state to be converted to a [Managed Tables | managed table](/concepts/managed-tables-in-databricks.md). ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Error Message

The error message follows this pattern:

```
ALTER TABLE <table> SET MANAGED is unable to migrate the given table. Make sure the table is in a valid state and retry the command. If the issue persists, contact Databricks support.
```

^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Sub-Error: METADATA_CLEANUP_ERROR

The `METADATA_CLEANUP_ERROR` sub-error occurs when Databricks cannot create a Checkpoint or clean up old metadata files before migrating the table. The error message provides additional details about the underlying issue:

```
Unable to create checkpoint or clean up old metadata files before migrating the table.

== Error ==
<error>
```

^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Common Causes

The error typically arises due to one or more of the following conditions:

- **Table metadata corruption** — The [Delta Lake](/concepts/delta-lake.md) table's transaction log contains inconsistencies or corrupted metadata files that prevent checkpoint creation.
- **Concurrent table operations** — Another operation is modifying the table simultaneously, interfering with the migration process.
- **Stale metadata files** — Old or orphaned metadata files cannot be cleaned up properly during the migration.
- **Insufficient permissions** — The user or service principal lacks the necessary permissions to modify table metadata or create checkpoints.

## Troubleshooting Steps

### Step 1: Verify Table State

Check whether the table is in a valid state by running a `DESCRIBE DETAIL` or `DESCRIBE HISTORY` command to inspect the table's metadata and transaction history. Look for incomplete transactions or errors in the history. ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

### Step 2: Retry the Command

If the table appears to be in a healthy state after verification, retry the `ALTER TABLE SET MANAGED` command. Transient issues such as concurrent operations may resolve on a subsequent attempt. ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

### Step 3: Resolve METADATA_CLEANUP_ERROR

If the error includes `METADATA_CLEANUP_ERROR`, attempt the following:

1. Run `FSCK REPAIR TABLE` to fix any file system inconsistencies.
2. Use `VACUUM` to clean up stale files.
3. Try running `ALTER TABLE SET MANAGED` again.

### Step 4: Contact Databricks Support

If the issue persists after verifying the table state and retrying the command, contact Databricks Support for assistance. Provide the full error message and the output of `DESCRIBE HISTORY` for the affected table. ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Related Concepts

- [Managed Tables](/concepts/managed-tables-in-databricks.md) — Tables whose data and metadata are fully managed by Databricks
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that powers Delta tables
- [ALTER TABLE SET MANAGED](/concepts/alter-table-set-managed.md) — The command that converts a table to a managed table
- [Delta Table Transaction Log](/concepts/delta-lake-transaction-log.md) — The transaction log that records all changes to a Delta table
- Checkpoint — A snapshot of the Delta table state used for efficient reads
- [FSCK REPAIR TABLE](/concepts/fsck-repair-table.md) — A command to fix file system inconsistencies
- VACUUM — A command to clean up stale files from a Delta table

## Sources

- delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md](/references/delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws-c36210c9.md)
