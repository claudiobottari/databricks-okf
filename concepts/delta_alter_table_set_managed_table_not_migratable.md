---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 935f80fb712333ad8e52d8ebc629df1559856613ebd88c398b020cccf115ecb3
  pageDirectory: concepts
  sources:
    - delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_alter_table_set_managed_table_not_migratable
    - DELTA_ALTER_TABLE_SET_MANAGED_TABLE_NOT_MIGRATABLE
    - delta_alter_table_set_managed_table_not_migratable-error
    - DELTA_ALTER_TABLE_SET_MANAGED_TABLE_NOT_MIGRATABLE error condition
    - delta_alter_table_set_managed_table_not_migratable-error-class
    - DEC
  citations:
    - file: delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md
title: DELTA_ALTER_TABLE_SET_MANAGED_TABLE_NOT_MIGRATABLE
description: A Databricks error raised when ALTER TABLE SET MANAGED fails to migrate a table to managed storage.
tags:
  - error-message
  - databricks
  - delta-lake
timestamp: "2026-06-19T10:01:27.283Z"
---

# DELTA_ALTER_TABLE_SET_MANAGED_TABLE_NOT_MIGRATABLE error condition

**DELTA_ALTER_TABLE_SET_MANAGED_TABLE_NOT_MIGRATABLE** is an error class in Databricks that occurs when the `ALTER TABLE <table> SET MANAGED` command cannot migrate a table to a managed state. This error indicates that the table is not in a valid state for migration, or that metadata cleanup operations failed during the process. ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Error details

- **SQLSTATE**: [55019](https://docs.databricks.com/aws/en/error-messages/sqlstates#class-55-object-not-in-prerequisite-state) (class 55 – Object not in prerequisite state) ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]
- **Default error message**:  
  `ALTER TABLE <table> SET MANAGED is unable to migrate the given table. Make sure the table is in a valid state and retry the command. If the issue persists, contact Databricks support.` ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Sub‑conditions and causes

The error class includes the following sub‑condition:

### METADATA_CLEANUP_ERROR

This sub‑condition is raised when the system is unable to create a checkpoint or clean up old metadata files before migrating the table. The full error message takes the form: ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

```
== Error ==
<error>
== Error ==
Unable to create checkpoint or clean up old metadata files before migrating the table.
```

Causes of metadata cleanup failure may include transient system issues, corrupted metadata, or insufficient permissions to write checkpoints or delete stale files. ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Resolution steps

1. **Verify table state**: Ensure the table is in a valid, non‑corrupt state and that the `ALTER TABLE SET MANAGED` command is applicable. ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]
2. **Retry the command**: Simple transient issues may resolve on retry. ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]
3. **Contact Databricks support**: If the problem persists, reach out to Databricks support for further investigation. ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Related concepts

- Managed tables in Delta Lake — The target state for the migration.
- [ALTER TABLE SET MANAGED](/concepts/alter-table-set-managed.md) — The command that triggers this error.
- Error classes in Databricks — Overview of structured error reporting.
- [SQLSTATE 55019](/concepts/sqlstate-55019.md) — The standard SQL error code for “object not in prerequisite state.”

## Sources

- delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md](/references/delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws-c36210c9.md)
