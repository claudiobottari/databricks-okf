---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6dcf38f4618230a0bd0d77b2cbcb6b0c106c9e3cd433201374a2356dfadce7af
  pageDirectory: concepts
  sources:
    - delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - redirect_ready_already_exists-sub-error
  citations:
    - file: delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
title: REDIRECT_READY_ALREADY_EXISTS Sub-Error
description: Sub-error indicating another concurrent ALTER TABLE SET MANAGED command already migrated the table to managed state
tags:
  - error-messages
  - databricks
  - concurrency
timestamp: "2026-06-19T18:21:09.365Z"
---

# REDIRECT_READY_ALREADY_EXISTS Sub-Error

**REDIRECT_READY_ALREADY_EXISTS** is a sub-error of the DELTA_ALTER_TABLE_SET_MANAGED_FAILED Error Class|DELTA_ALTER_TABLE_SET_MANAGED_FAILED error class. It indicates that an attempt to migrate a table to managed storage failed because the table already has the `RedirectReady` state. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Error Context

The error occurs when running `ALTER TABLE <table> SET MANAGED` and the table is already in the `RedirectReady` state. This state is set as part of the migration process; its presence means that the migration may have already been completed by a concurrent `ALTER TABLE tbl SET MANAGED` command. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Recommended Action

Verify whether the table is already migrated to managed storage by running `DESC EXTENDED tbl`. If the table metadata shows it is now managed, no further action is required. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Related Concepts

- DELTA_ALTER_TABLE_SET_MANAGED_FAILED Error Class|DELTA_ALTER_TABLE_SET_MANAGED_FAILED error class – The parent error class.
- [Managed table](/concepts/unity-catalog-managed-tables.md) – A table managed by Databricks where the data is stored in the workspace's managed storage location.
- External table – A table whose data resides in an external location.
- [ALTER TABLE SET MANAGED](/concepts/alter-table-set-managed.md) – The SQL command for migrating a table from external to managed storage.
- Concurrent migration conflicts – Issues that can arise when multiple statements try to migrate the same table simultaneously.

## Sources

- delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_set_managed_failed-error-condition-databricks-on-aws-ddfd0547.md)
