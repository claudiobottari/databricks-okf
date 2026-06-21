---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 87e5ba8387490ad39439e55ca46d43ac682710a44dfed033c1deeaebb606ba5c
  pageDirectory: concepts
  sources:
    - delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - alter-table-set-managed-operation
    - ATSMO
    - ALTER TABLE operations
    - External table to managed table migration
  citations:
    - file: delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
title: ALTER TABLE SET MANAGED operation
description: A Delta Lake DDL operation that migrates an external (unmanaged) table to a managed table, which can fail due to concurrent operations or file validation issues.
tags:
  - delta-lake
  - ddl
  - databricks
timestamp: "2026-06-18T15:16:03.456Z"
---

# ALTER TABLE SET MANAGED Operation

**ALTER TABLE SET MANAGED operation** is a Delta Lake SQL command that converts an existing external table into a managed table within [Unity Catalog](/concepts/unity-catalog.md). This operation migrates the table's underlying data files from an external location into the Unity Catalog-managed storage location.

## Overview

The `ALTER TABLE <table> SET MANAGED` command transitions a table from external (unmanaged) to managed status. In a managed table, Unity Catalog takes ownership of the data files and manages their lifecycle. The operation involves validating and migrating the data files, updating metadata, and establishing a redirect configuration. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Migration Status

After initiating the operation, you can verify whether the migration succeeded using the `DESC EXTENDED` command:

```sql
DESC EXTENDED <table_name>
```

This command shows the current table properties and indicates whether the table has transitioned to the managed state. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Error Conditions

The `ALTER TABLE SET MANAGED` operation can fail under several conditions, producing the error class `DELTA_ALTER_TABLE_SET_MANAGED_FAILED` with SQLSTATE 42809 (syntax error or access rule violation). ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

### CANNOT_FINALIZE_REDIRECT

This error occurs when the operation cannot finalize the redirect on the external location because the redirect configuration does not exist. This can happen if the table is currently rolling back to external. If the rollback is not the cause, contact Databricks support. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

### FILE_VALIDATION_FAILED

File validation fails when one or more data files cannot be migrated. The error message specifies the number of missing files that could not be transferred. The recommended action is to retry the operation or contact Databricks support if the issue persists. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

### REDIRECT_READY_ALREADY_EXISTS

This error indicates the table already has a `RedirectReady` state, which means a concurrent `ALTER TABLE SET MANAGED` command may have already completed the migration. To verify, run `DESC EXTENDED <table_name>` to check if the table is already managed. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

### VERSION_MISMATCH

A version mismatch occurs when the version of the managed DeltaLog does not match the expected version. This typically happens when a concurrent `ALTER TABLE SET MANAGED` command has already successfully migrated the table. As with the redirect error, verify the current state using `DESC EXTENDED <table_name>`. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Related Concepts

- [Managed vs External tables in Unity Catalog](/concepts/managed-vs-external-tables-in-unity-catalog.md)
- [Delta Lake](/concepts/delta-lake.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [DESC EXTENDED Command](/concepts/desc-extended-diagnostic-command.md)
- Table Lifecycle Management

## Sources

- delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_set_managed_failed-error-condition-databricks-on-aws-ddfd0547.md)
