---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9af8901e7a274156f7940df21a01de500654d348ac3675e04eddb003c174ba1d
  pageDirectory: concepts
  sources:
    - delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - alter-table-set-managed
    - ATSM
    - ALTER TABLE ... UNSET MANAGED
    - ALTER TABLE UNSET MANAGED
    - alter-table-set-managed-command
    - ATSMC
    - alter-table-set-managed-databricks
    - ATSM(
    - alter-table-set-managed-delta-lake
    - ATSM(L
    - alter-table-set-managed-operation
    - ATSMO
    - ALTER TABLE operations
    - External table to managed table migration
  citations:
    - file: delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
    - file: delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md
title: ALTER TABLE SET MANAGED
description: A Databricks SQL DDL command to convert an external table into a managed (Metastore-owned) table, which can fail with metadata cleanup errors.
tags:
  - ddl
  - databricks
  - delta-lake
  - table-management
timestamp: "2026-06-19T18:21:29.871Z"
---

# ALTER TABLE SET MANAGED

`ALTER TABLE <table> SET MANAGED` is a Databricks SQL DDL command that converts an external table to a [managed table](/concepts/unity-catalog-managed-tables.md). During the migration, the command performs redirect configuration and file validation steps. If the migration fails, a specific error condition is raised indicating the cause of the failure. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md] ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Error Conditions

### DELTA_ALTER_TABLE_SET_MANAGED_FAILED (SQLSTATE: 42809)

This error class contains the following sub‑conditions that can occur when `ALTER TABLE SET MANAGED` fails:

#### CANNOT_FINALIZE_REDIRECT

Cannot finalize a redirect on the external location because the redirect configuration does not exist. This can happen if the table is currently rolling back to external. Otherwise, contact Databricks support. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

#### FILE_VALIDATION_FAILED

File validation failed. The error message includes the number of files that could not be migrated. Retry the operation or contact Databricks support if the issue persists. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

#### REDIRECT_READY_ALREADY_EXISTS

The table already has a `RedirectReady` state. This likely means a concurrent `ALTER TABLE tbl SET MANAGED` command has already migrated the table. Check whether the table is already managed by running:

```sql
DESC EXTENDED tbl;
```

^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

#### VERSION_MISMATCH

The version of the managed DeltaLog (`<managedDeltaLogVersion>`) does not match the expected version (`<expectedVersion>`). This can occur if a concurrent `ALTER TABLE tbl SET MANAGED` command already successfully migrated the table. Verify the table's current state with `DESC EXTENDED tbl`. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

### DELTA_ALTER_TABLE_SET_MANAGED_TABLE_NOT_MIGRATABLE (SQLSTATE: 55019)

This error class occurs when `ALTER TABLE <table> SET MANAGED` is unable to migrate the given table at all. Make sure the table is in a valid state and retry the command. If the issue persists, contact Databricks support. ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

#### METADATA_CLEANUP_ERROR

Unable to create checkpoint or clean up old metadata files before migrating the table. The error message includes the underlying error details:

```
== Error ==
<error>
```

^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Troubleshooting

- If you see `REDIRECT_READY_ALREADY_EXISTS` or `VERSION_MISMATCH`, a concurrent migration may have succeeded. Run `DESC EXTENDED tbl` to confirm the table is managed. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]
- For `FILE_VALIDATION_FAILED`, retry the command. If the failure persists, contact Databricks support. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]
- For `CANNOT_FINALIZE_REDIRECT`, check whether the table is rolling back from a previous migration attempt. If not, contact Databricks support. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]
- For `TABLE_NOT_MIGRATABLE` with `METADATA_CLEANUP_ERROR`, ensure the table is in a valid state and retry the command. Contact Databricks support if the issue persists. ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Related Concepts

- [Managed table](/concepts/unity-catalog-managed-tables.md) — Tables whose data files are managed by Databricks
- External table — Tables whose data resides in a customer-managed location
- [Delta Lake](/concepts/delta-lake.md) — The storage layer for Delta tables
- [SQLSTATE 42809](/concepts/sqlstate-42809.md) — Syntax error or access rule violation class
- [SQLSTATE 55019](/concepts/sqlstate-55019.md) — Object not in prerequisite state error class
- [DESC EXTENDED](/concepts/desc-extended-diagnostic-command.md) — Command to inspect table metadata and current state

## Sources

- delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
- delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_set_managed_failed-error-condition-databricks-on-aws-ddfd0547.md)
2. [delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md](/references/delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws-c36210c9.md)
