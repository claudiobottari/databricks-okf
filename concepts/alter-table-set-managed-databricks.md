---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c16c2f116a8d80ac2689598004016df94d0b93c1c6da2253a944d21a1acaac93
  pageDirectory: concepts
  sources:
    - delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - alter-table-set-managed-databricks
    - ATSM(
  citations:
    - file: delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
title: ALTER TABLE SET MANAGED (Databricks)
description: Databricks SQL command to convert an external (unmanaged) Delta table to a managed table, with associated error conditions
tags:
  - sql
  - databricks
  - delta-lake
  - table-management
timestamp: "2026-06-19T10:00:46.187Z"
---

# ALTER TABLE SET MANAGED (Databricks)

**ALTER TABLE SET MANAGED** is a Databricks SQL command that converts an external (unmanaged) Delta table to a managed table. This operation migrates the table's underlying data files from an external location into the Databricks-managed storage location associated with the table's schema. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Overview

When you execute `ALTER TABLE <table> SET MANAGED`, Databricks moves the table's data files from the external storage location specified during table creation to the managed storage location for the database schema. This operation changes the table's metadata to mark it as managed, meaning Databricks controls the lifecycle of the underlying data files. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

The command is useful when you want to consolidate data into Databricks-managed storage or apply managed table policies that aren't available for external tables.

## Error Conditions

The command can fail with several specific error conditions under the `DELTA_ALTER_TABLE_SET_MANAGED_FAILED` error class ([SQLSTATE 42809](/concepts/sqlstate-42809.md)). The following subsections describe each error subtype. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

### CANNOT_FINALIZE_REDIRECT

This error occurs when Databricks cannot finalize a redirect on the external location because the redirect configuration does not exist. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

**Causes:** This can happen if the table is currently rolling back to external status. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

**Resolution:** Contact Databricks support if the issue persists. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

### FILE_VALIDATION_FAILED

This error indicates that file validation failed during migration. The error message includes the count of files that could not be migrated. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

**Error format:** `File validation failed: <missingFileCount> file(s) could not be migrated.` ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

**Resolution:** Retry the operation. If the issue persists, contact Databricks support. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

### REDIRECT_READY_ALREADY_EXISTS

This error occurs when the table already has a `RedirectReady` state, meaning a concurrent `ALTER TABLE tbl SET MANAGED` command may have already completed the migration. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

**Verification:** Check if the table is already migrated to managed by running `DESC EXTENDED tbl`. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

### VERSION_MISMATCH

This error indicates that the version of the managed Delta log does not match the expected version. The error message includes both the actual managed Delta log version and the expected version. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

**Error format:** `The version of the managed DeltaLog (<managedDeltaLogVersion>) does not match the expected one (<expectedVersion>).` ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

**Causes:** This can happen if a concurrent `ALTER TABLE tbl SET MANAGED` command already successfully migrated the table. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

**Verification:** Check if the table is already migrated to managed by running `DESC EXTENDED tbl`. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Best Practices

- **Check for concurrent operations:** Before retrying a failed `ALTER TABLE SET MANAGED`, verify whether another session may have already completed the migration using `DESC EXTENDED`. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]
- **Verify file availability:** Ensure all table files are accessible before initiating the migration to avoid `FILE_VALIDATION_FAILED` errors.
- **Contact support for persistent issues:** If the error persists after retrying, contact Databricks support for assistance with `CANNOT_FINALIZE_REDIRECT` or recurring file validation failures. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Related Concepts

- [Managed vs External Tables in Databricks](/concepts/managed-tables-in-databricks.md) — The distinction between managed and unmanaged tables
- [DESC EXTENDED](/concepts/desc-extended-diagnostic-command.md) — Command to verify table migration status
- Delta Table Migration — General process of converting between table types
- Databricks Error Conditions — Other error classes for troubleshooting

## Sources

- delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_set_managed_failed-error-condition-databricks-on-aws-ddfd0547.md)
