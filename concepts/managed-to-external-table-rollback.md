---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5268668110b3cec2e5de78b8d450db3cbbac5720afb8e7a1350566e7329e1c40
  pageDirectory: concepts
  sources:
    - delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - managed-to-external-table-rollback
    - MTETR
  citations:
    - file: delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
title: Managed to External Table Rollback
description: The operation of reverting a Unity Catalog managed table back to an external table, which is time-limited and has specific failure modes.
tags:
  - databricks
  - delta-lake
  - unity-catalog
  - table-management
timestamp: "2026-06-18T15:16:30.269Z"
---

# Managed to External Table Rollback

**Managed to External Table Rollback** refers to a Databricks operation that attempts to convert a [Unity Catalog](/concepts/unity-catalog.md) managed table back to an external table. This rollback is supported only within a limited time window after the original migration to managed table and requires a complete, unaltered table history. If the prerequisites are not met, the `DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED` error is raised.^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Error Condition: `DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED`

The error `DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED` is thrown when a `ALTER TABLE ... UNSET MANAGED` command cannot complete successfully. The error message includes a sub‑reason that identifies the specific cause.^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

### `TIME_WINDOW_EXCEEDED`

The rollback is only permitted within `<numDays>` days after the table was migrated to a Unity Catalog managed table. If the operation is attempted after this window closes, the error reports `TIME_WINDOW_EXCEEDED`.^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

### `TRUNCATED_HISTORY`

The rollback requires that the [Delta Lake](/concepts/delta-lake.md) transaction log contains all commits needed to reconstruct the original external table state. If the history has been truncated (e.g., via `VACUUM` or log retention policies), the system cannot locate the necessary commits and raises `TRUNCATED_HISTORY`.^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

### `UNEXPECTED_ERROR`

A generic error condition when an unexpected failure occurs. The error details are provided in the `<error>` field of the message.^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

### `VERSION_MISMATCH`

The managed table’s Delta log version (`<managedDeltaLogVersion>`) does not match the external table’s Delta log version (`<externalDeltaLogVersion>`). This typically happens when a concurrent `ALTER TABLE ... UNSET MANAGED` command has already succeeded, leaving the table in external state and making a second rollback attempt invalid.^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Managed Tables](/concepts/unity-catalog-managed-tables.md)
- [External Tables in Unity Catalog](/concepts/external-tables-in-unity-catalog.md)
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md)
- [ALTER TABLE UNSET MANAGED](/concepts/alter-table-unset-managed-command.md)
- VACUUM and history retention

## Sources

- delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws-a24f2e75.md)
