---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e3856abe12d7dc8fd377db1b778370803eb1f4ff3c8d5e7fbe92cd93167f0779
  pageDirectory: concepts
  sources:
    - delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - alter-table-set-managed-command
    - ATSMC
  citations:
    - file: delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
title: ALTER TABLE SET MANAGED Command
description: Databricks SQL command to convert an external Delta table into a managed (internal) table
tags:
  - sql
  - databricks
  - delta-lake
  - table-management
timestamp: "2026-06-19T18:21:05.628Z"
---

# ALTER TABLE SET MANAGED Command

The `ALTER TABLE SET MANAGED` command transitions a table from unmanaged (external) to managed storage in [Unity Catalog](/concepts/unity-catalog.md). When a table is unmanaged, its data files exist independently of the [Metastore](/concepts/metastore.md); after conversion, the table becomes managed and its lifecycle is controlled by the catalog. The command syntax is `ALTER TABLE <table_name> SET MANAGED`.^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## DELTA_ALTER_TABLE_SET_MANAGED_FAILED Error

If the migration fails, Databricks returns the error condition `DELTA_ALTER_TABLE_SET_MANAGED_FAILED` with SQLSTATE 42809 (class 42: syntax error or access rule violation).^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

### Error Subtypes

#### CANNOT_FINALIZE_REDIRECT

The system cannot finalize a redirect on the external location because a redirect configuration does not exist. This can occur if the table is currently rolling back to external. If the table is not undergoing a rollback, contact Databricks support.^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

#### FILE_VALIDATION_FAILED

File validation failed because a specified number of files could not be migrated. The error message includes the count of missing files: `File validation failed: <missingFileCount> file(s) could not be migrated.` Retry the operation or contact Databricks support if the issue persists.^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

#### REDIRECT_READY_ALREADY_EXISTS

The table already has a `RedirectReady` state, meaning the migration may have already completed by a concurrent `ALTER TABLE tbl SET MANAGED` command. Verify the current table state by running `DESC EXTENDED tbl` to check if the table is already migrated to managed.^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

#### VERSION_MISMATCH

The version of the managed DeltaLog (`<managedDeltaLogVersion>`) does not match the expected version (`<expectedVersion>`). This can happen if a concurrent `ALTER TABLE tbl SET MANAGED` command already successfully migrated the table to managed. Run `DESC EXTENDED tbl` to check if the table is already managed.^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

### Resolution

1. **Verify table state**: Run `DESC EXTENDED <table_name>` to confirm whether the migration already completed successfully.^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]
2. **Check for concurrent operations**: Ensure no other `ALTER TABLE SET MANAGED` commands are running against the same table simultaneously.^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]
3. **Retry the command**: For `FILE_VALIDATION_FAILED`, retrying the operation may resolve transient file migration issues.^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]
4. **Contact support**: If the table is not rolling back and the error persists (especially for `CANNOT_FINALIZE_REDIRECT`), contact Databricks support.^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Requirements

- The table must be in a valid state—not corrupted, not undergoing concurrent modifications, and with a complete transaction log.
- Only tables registered in [Unity Catalog](/concepts/unity-catalog.md) can be converted using this command.^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Related Concepts

- Managed vs Unmanaged Tables — The distinction between catalog-controlled and externally-controlled table storage
- ALTER TABLE — The SQL command for modifying table properties
- Table Migration — The broader process of changing storage management for tables
- [Delta Table](/concepts/delta-lake-table.md) — The storage format underlying the migration operation
- [SQLSTATE 42809](/concepts/sqlstate-42809.md) — The SQL state for syntax error or access rule violation

## Sources

- delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_set_managed_failed-error-condition-databricks-on-aws-ddfd0547.md)
