---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7f1270523fefa6e3fc74df0ec46d84d879f5114b7c9e34f5da80f52da09b4a89
  pageDirectory: concepts
  sources:
    - delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_alter_table_set_managed_failed
    - DELTA_ALTER_TABLE_SET_MANAGED_FAILED
    - delta_alter_table_set_managed_failed-error-class
    - DEC
    - DELTA_ALTER_TABLE_SET_MANAGED_FAILED Error Condition
    - DELTA_ALTER_TABLE_SET_MANAGED_FAILED error class
    - DELTA_ALTER_TABLE_SET_MANAGED_FAILED error condition
  citations:
    - file: delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
title: DELTA_ALTER_TABLE_SET_MANAGED_FAILED
description: A Databricks error class that occurs when ALTER TABLE ... SET MANAGED fails, with multiple sub-error types indicating specific failure modes during external-to-managed table migration.
tags:
  - databricks
  - error-messages
  - delta-lake
  - tables
timestamp: "2026-06-18T11:49:14.961Z"
---

# DELTA_ALTER_TABLE_SET_MANAGED_FAILED

**`DELTA_ALTER_TABLE_SET_MANAGED_FAILED`** is a Databricks error class (SQLSTATE: 42809) raised when an `ALTER TABLE <table> SET MANAGED` statement fails to convert an external Delta table into a managed table. The error includes one of several sub‑errors that indicate the specific reason for the failure. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Sub‑Errors

### CANNOT_FINALIZE_REDIRECT

The operation cannot finalize a redirect on the external location because the redirect configuration does not exist. This can occur if the table is currently rolling back to external. Otherwise, contact Databricks support. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

### FILE_VALIDATION_FAILED

File validation failed because `<missingFileCount>` file(s) could not be migrated. Retry the operation, or contact Databricks support if the issue persists. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

### REDIRECT_READY_ALREADY_EXISTS

The table already has a `RedirectReady` state, meaning another concurrent `ALTER TABLE tbl SET MANAGED` command may have already completed the migration. Check whether the table is already migrated to managed by running `DESC EXTENDED tbl`. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

### VERSION_MISMATCH

The version of the managed Delta Log (`<managedDeltaLogVersion>`) does not match the expected version (`<expectedVersion>`). This can happen if a concurrent `ALTER TABLE tbl SET MANAGED` command already successfully migrated the table. Verify the table’s current state using `DESC EXTENDED tbl`. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Related Concepts

- ALTER TABLE — The SQL statement that triggers this error
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format of the table
- [External tables](/concepts/unity-catalog-external-table-conversion.md) — Tables whose data resides outside the managed location
- [Managed tables](/concepts/managed-tables-in-databricks.md) — Tables whose data is fully managed by Databricks
- [DESC EXTENDED](/concepts/desc-extended-diagnostic-command.md) — Command used to inspect a table’s properties and migration state

## Sources

- delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_set_managed_failed-error-condition-databricks-on-aws-ddfd0547.md)
