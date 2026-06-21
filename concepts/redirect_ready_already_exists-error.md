---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 622856cfab93f99cfd4d9cbc31f7821afab017692350527d70cf97aa434354e8
  pageDirectory: concepts
  sources:
    - delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - redirect_ready_already_exists-error
    - REDIRECT_READY_ALREADY_EXISTS error (Delta managed migration)
  citations:
    - file: delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
title: REDIRECT_READY_ALREADY_EXISTS error
description: A sub-error of DELTA_ALTER_TABLE_SET_MANAGED_FAILED indicating the table already has a RedirectReady state, possibly due to a concurrent migration command completing first.
tags:
  - databricks
  - error-messages
  - concurrency
timestamp: "2026-06-19T15:00:34.327Z"
---

# REDIRECT_READY_ALREADY_EXISTS error

**REDIRECT_READY_ALREADY_EXISTS** is a sub-error condition under DELTA_ALTER_TABLE_SET_MANAGED_FAILED Error Class|DELTA_ALTER_TABLE_SET_MANAGED_FAILED error condition that occurs when executing an `ALTER TABLE SET MANAGED` command on a Delta table that has already been successfully migrated to the managed state. This indicates the migration process has already completed, often due to a concurrent operation.

## Error Classification

The error is classified under SQLSTATE 42809, which falls under the category of syntax errors or access rule violations. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Cause

The `ALTER TABLE <table> SET MANAGED` command fails with a `REDIRECT_READY_ALREADY_EXISTS` error when the table already has a RedirectReady state. This situation typically arises when another concurrent `ALTER TABLE tbl SET MANAGED` command has already finished the migration process. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Resolution

To verify whether the table has already been successfully migrated to managed status, execute the following command:

```sql
DESC EXTENDED <table_name>
```

This command displays extended table metadata, including the current table type and management status. If the output confirms the table is already managed, no further action is required. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Related Concepts

- DELTA_ALTER_TABLE_SET_MANAGED_FAILED Error Class|DELTA_ALTER_TABLE_SET_MANAGED_FAILED error condition – The parent error condition containing this sub-error
- CANNOT_FINALIZE_REDIRECT – Related sub-error when redirect configuration is missing
- FILE_VALIDATION_FAILED – Related sub-error when file migration fails
- VERSION_MISMATCH – Related sub-error when delta log versions don't match
- [ALTER TABLE SET MANAGED](/concepts/alter-table-set-managed.md) – The command triggering this migration
- Delta Lake table management – Managed vs. external table concepts
- Concurrent operations in Delta Lake – How concurrent table operations interact

## Sources

- delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_set_managed_failed-error-condition-databricks-on-aws-ddfd0547.md)
