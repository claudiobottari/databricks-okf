---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4e4704b96de505cf9957df15bb8462933b85a6ff05f5d99d04896fc092be5d88
  pageDirectory: concepts
  sources:
    - delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metadata_cleanup_error-sub-error
  citations:
    - file: delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md
title: METADATA_CLEANUP_ERROR sub-error
description: A specific sub-error of DELTA_ALTER_TABLE_SET_MANAGED_TABLE_NOT_MIGRATABLE indicating failure to create checkpoint or clean up old metadata files before migrating the table.
tags:
  - error-messages
  - metadata
  - delta-lake
timestamp: "2026-06-18T11:49:41.296Z"
---

# METADATA_CLEANUP_ERROR sub-error

The **METADATA_CLEANUP_ERROR** is a sub-error of the `DELTA_ALTER_TABLE_SET_MANAGED_TABLE_NOT_MIGRATABLE` error class. It occurs when an `ALTER TABLE <table> SET MANAGED` command fails because the system cannot create a checkpoint or clean up old metadata files before migrating the table. ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Error Message

When this sub-error is raised, the engine returns the following diagnostic information:

```
DELTA_ALTER_TABLE_SET_MANAGED_TABLE_NOT_MIGRATABLE
  Sub-error: METADATA_CLEANUP_ERROR
  Message: Unable to create checkpoint or clean up old metadata files before migrating the table.

== Error ==
<error>
```

^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Cause

The `ALTER TABLE ... SET MANAGED` command must first bring the Delta table into a clean state by creating a checkpoint and removing stale metadata files. If this cleanup step fails, the command cannot guarantee a safe migration from an external table to a managed table. Common triggers include concurrent write operations, permission issues on the underlying storage, or corruption of the transaction log. ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Resolution

- Ensure the table is in a valid state with no ongoing write operations.
- Retry the `ALTER TABLE ... SET MANAGED` command.
- If the error persists, contact Databricks support for further investigation. ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Related Concepts

- DELTA_ALTER_TABLE_SET_MANAGED_TABLE_NOT_MIGRATABLE error|DELTA_ALTER_TABLE_SET_MANAGED_TABLE_NOT_MIGRATABLE error condition — The parent error class for migration failures.
- [ALTER TABLE SET MANAGED](/concepts/alter-table-set-managed.md) — The SQL command that triggers this error.
- Delta Lake checkpoint — The mechanism that creates a snapshot of the transaction log.
- [External table to managed table migration](/concepts/alter-table-set-managed-operation.md) — The overall process affected by this error.

## Sources

- delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md](/references/delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws-c36210c9.md)
