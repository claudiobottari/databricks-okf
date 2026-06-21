---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1df91dff25087388f45d32e52667025b45365effe7c806cb1b424e5435a2b7f5
  pageDirectory: concepts
  sources:
    - delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time_window_exceeded
  citations:
    - file: delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
title: TIME_WINDOW_EXCEEDED
description: Sub-error indicating the time window for rolling back a managed table to external has elapsed (beyond numDays)
tags:
  - databricks
  - error-message
  - time-limit
timestamp: "2026-06-19T18:21:42.173Z"
---

# TIME\_WINDOW\_EXCEEDED

**TIME\_WINDOW\_EXCEEDED** is a specific error condition that occurs under the DELTA\_ALTER\_TABLE\_UNSET\_MANAGED\_FAILED error class. It indicates that an attempt to roll back a managed table to an external table has failed because the allowed time window for that rollback has expired. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Cause

Rollback from managed to external is only supported within a fixed number of days (`<numDays>`) after the table was migrated to a [Unity Catalog](/concepts/unity-catalog.md) managed table. When a user issues `ALTER TABLE ... UNSET MANAGED` after that window has passed, the command returns the `TIME_WINDOW_EXCEEDED` error. The time limit is designed to ensure that rollback can only happen while the necessary Delta history is still available. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Related Error Conditions

The `DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED` error class includes several other failure modes for the same operation: ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

- **TRUNCATED_HISTORY** — The table history has been truncated, so the commits needed to reconstruct the original external table state are missing.
- **VERSION_MISMATCH** — The version of the managed [Delta Lake](/concepts/delta-lake.md) log (`<managedDeltaLogVersion>`) and the external Delta log (`<externalDeltaLogVersion>`) do not match, often because a concurrent `ALTER TABLE ... UNSET MANAGED` command already succeeded.
- **UNEXPECTED_ERROR** — An unexpected internal error occurred during the operation.

## Resolving the Error

Because the time window has closed, the table cannot be reverted to its external state using the standard `UNSET MANAGED` command. To recover the table to an external location, alternative approaches (outside the scope of this error) must be used, such as manually recreating the external table from the underlying data files after ensuring no managed metadata remains.

## Related Concepts

- [Managed Table](/concepts/unity-catalog-managed-tables.md) – A Unity Catalog table whose data and metadata are governed by the [Metastore](/concepts/metastore.md).
- External Table – A table whose data resides at a user-specified location outside the [Metastore](/concepts/metastore.md).
- [Delta Lake](/concepts/delta-lake.md) – The storage format that tracks table history and enables rollback.
- Rollback – The process of undoing a migration from external to managed.
- DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED error class|DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED – The parent error class for this condition.

## Sources

- delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws-a24f2e75.md)
