---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7d2d728e21155560b3e51c59144fd313fc92ad8a85a10c3b18641e2b36086a9c
  pageDirectory: concepts
  sources:
    - delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - version_mismatch-error-delta-managed-migration
    - VE(MM
    - VERSION_MISMATCH error (Delta managed migration)
  citations:
    - file: delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
title: VERSION_MISMATCH error (Delta managed migration)
description: Sub-error of DELTA_ALTER_TABLE_SET_MANAGED_FAILED indicating the managed DeltaLog version doesn't match expectations, typically due to a concurrent migration
tags:
  - error-messages
  - databricks
  - delta-lake
  - concurrency
timestamp: "2026-06-19T10:01:18.948Z"
---

# VERSION_MISMATCH error (Delta managed migration)

**VERSION_MISMATCH** is an error condition that occurs when running `ALTER TABLE <table> SET MANAGED` on a [Delta table](/concepts/delta-lake-table.md) in Databricks, and the managed Delta log version does not match the expected version. This error indicates that the table migration from external to managed may have already been completed by a concurrent operation.

## Error Message

The error message reports that the version of the managed DeltaLog (`<managedDeltaLogVersion>`) does not match the expected one (`<expectedVersion>`). ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Cause

This error occurs when there is a concurrent `ALTER TABLE <table> SET MANAGED` command that has already successfully migrated the table to managed before the current command completes its validation. The version mismatch arises because the table's state changed between the time the current command read the expected version and the time it attempted to finalize the migration. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Resolution

To verify whether the table has already been successfully migrated to managed, run the following command: ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

```sql
DESC EXTENDED <table>;
```

If the table shows as `MANAGED` in the extended description, the migration has already been completed by the concurrent operation, and no further action is needed. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Related Concepts

- DELTA_ALTER_TABLE_SET_MANAGED_FAILED Error Class|DELTA_ALTER_TABLE_SET_MANAGED_FAILED error condition — The parent error class that contains VERSION_MISMATCH and other related sub-errors
- CANNOT_FINALIZE_REDIRECT — Another sub-error in the same error class, related to redirect configuration issues
- FILE_VALIDATION_FAILED — Another sub-error in the same error class, related to file migration failures
- REDIRECT_READY_ALREADY_EXISTS — Another sub-error in the same error class, indicating the table already has RedirectReady state
- [ALTER TABLE SET MANAGED](/concepts/alter-table-set-managed.md) — The DDL operation that triggers this error
- Delta table migration — The process of converting external tables to managed tables

## Sources

- delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_set_managed_failed-error-condition-databricks-on-aws-ddfd0547.md)
