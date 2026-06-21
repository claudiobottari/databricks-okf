---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7bf802c1e232fdd2f46e1d652e8b9c01d6034c4e9a8261eaa63c4f176e61ea87
  pageDirectory: concepts
  sources:
    - delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_alter_table_set_managed_failed-error-class
    - DEC
    - DELTA_ALTER_TABLE_SET_MANAGED_FAILED Error Condition
    - DELTA_ALTER_TABLE_SET_MANAGED_FAILED error class
    - DELTA_ALTER_TABLE_SET_MANAGED_FAILED error condition
  citations:
    - file: delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
title: DELTA_ALTER_TABLE_SET_MANAGED_FAILED Error Class
description: Error class raised when ALTER TABLE SET MANAGED fails on a Delta table in Databricks
tags:
  - error-messages
  - databricks
  - delta-lake
timestamp: "2026-06-19T18:21:03.415Z"
---

# DELTA_ALTER_TABLE_SET_MANAGED_FAILED Error Class

**SQLSTATE: 42809**

The `DELTA_ALTER_TABLE_SET_MANAGED_FAILED` error class occurs when an `ALTER TABLE <table> SET MANAGED` command fails. This operation attempts to convert an External Delta tables|external Delta table to a [Managed tables vs external tables|managed table](/concepts/managed-vs-external-tables-in-unity-catalog.md). The error class includes several sub-errors that indicate specific failure reasons. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## CANNOT_FINALIZE_REDIRECT

The redirect configuration on the external location cannot be finalized because no redirect configuration exists. This can happen if the table is currently rolling back to external. If the rollback is not the cause, contact Databricks support. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## FILE_VALIDATION_FAILED

File validation failed because one or more files could not be migrated. The error message includes the count of missing files (`<missingFileCount>`). Retry the operation, and if the issue persists, contact Databricks support. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## REDIRECT_READY_ALREADY_EXISTS

The table already has a `RedirectReady` state, which means a concurrent `ALTER TABLE tbl SET MANAGED` command may have already completed the migration. Check whether the table is already managed by running `DESC EXTENDED tbl`. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## VERSION_MISMATCH

The version of the managed DeltaLog (`<managedDeltaLogVersion>`) does not match the expected version (`<expectedVersion>`). This typically occurs when a concurrent `ALTER TABLE tbl SET MANAGED` command has already migrated the table to managed. Verify the table's current state with `DESC EXTENDED tbl`. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Related Concepts

- ALTER TABLE (Delta Lake) – The SQL command that triggers this error.
- [Managed tables vs external tables](/concepts/managed-vs-external-tables-in-unity-catalog.md) – The distinction between managed and external Delta tables.
- [DESC EXTENDED](/concepts/desc-extended-diagnostic-command.md) – Command used to verify table properties.
- [Delta Lake](/concepts/delta-lake.md) – The storage layer used by Databricks.

## Sources

- delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_set_managed_failed-error-condition-databricks-on-aws-ddfd0547.md)
