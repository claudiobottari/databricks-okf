---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dbbdb8fd25c5137d9587dd6b54c3eb97bc5e155085670206fe0a92077ed8924e
  pageDirectory: concepts
  sources:
    - delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - version_mismatch-sub-error
  citations:
    - file: delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
title: VERSION_MISMATCH Sub-Error
description: Sub-error raised when the managed DeltaLog version does not match the expected version, often due to concurrent migration
tags:
  - error-messages
  - databricks
  - delta-log
  - versioning
timestamp: "2026-06-19T18:21:16.643Z"
---

# VERSION_MISMATCH Sub-Error

The **VERSION_MISMATCH Sub-Error** is a specific error condition that occurs during an `ALTER TABLE <table> SET MANAGED` operation on Databricks. It indicates a version conflict in the managed Delta log during the table migration process.

## Error Condition

The VERSION_MISMATCH error arises when the version of the managed DeltaLog (`<managedDeltaLogVersion>`) does not match the expected version (`<expectedVersion>`). This mismatch prevents the `ALTER TABLE SET MANAGED` command from completing successfully. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Cause

This error typically occurs when there is a concurrent `ALTER TABLE tbl SET MANAGED` command that has already successfully migrated the table to managed. The version conflict arises because two operations are attempting to modify the same table's metadata simultaneously. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Resolution

To resolve the VERSION_MISMATCH error, check whether the table has already been migrated to managed status by running the `DESC EXTENDED tbl` command. If the table is already managed, no further action is needed. If the table has not been migrated, retry the operation when no concurrent migration commands are running. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## SQLSTATE

This error is associated with [SQLSTATE: 42809](https://docs.databricks.com/aws/en/error-messages/sqlstates#class-42-syntax-error-or-access-rule-violation). ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Related Concepts

- DELTA_ALTER_TABLE_SET_MANAGED_FAILED Error Class|DELTA_ALTER_TABLE_SET_MANAGED_FAILED Error Condition — The parent error class containing VERSION_MISMATCH and other sub-errors
- [Managed vs External Tables](/concepts/managed-vs-external-tables-in-unity-catalog.md) — The difference between managed and external tables in Databricks
- [DeltaLog Versioning](/concepts/delta-table-versioning.md) — How Delta Lake tracks table metadata versions
- Concurrent Operations in Delta Lake — How Delta Lake handles concurrent table modifications
- [DESC EXTENDED](/concepts/desc-extended-diagnostic-command.md) — The command used to inspect table metadata

## Sources

- delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_set_managed_failed-error-condition-databricks-on-aws-ddfd0547.md)
