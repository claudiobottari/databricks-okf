---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 52d20ccaeb42a431cc73c294aa55dc92dbd3d088b30b81a513f2359fc4b6dbde
  pageDirectory: concepts
  sources:
    - delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - version_mismatch-in-delta-logs
    - VIDL
  citations:
    - file: delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
title: VERSION_MISMATCH in Delta Logs
description: A sub-error of DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED where the managed DeltaLog and external DeltaLog versions do not match, often due to concurrent rollback operations.
tags:
  - error-messages
  - databricks
  - delta-lake
  - concurrency
timestamp: "2026-06-18T15:16:44.274Z"
---

# VERSION_MISMATCH in Delta Logs

**VERSION_MISMATCH** is an error condition that occurs when rolling a table back from a managed table to an external table fails because the internal Delta Log versions of the two table types do not match. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Cause

The error is raised when an `ALTER TABLE tbl UNSET MANAGED` command detects that the managed DeltaLog version (`<managedDeltaLogVersion>`) and the external DeltaLog version (`<externalDeltaLogVersion>`) are out of sync. This typically happens because a concurrent `ALTER TABLE tbl UNSET MANAGED` command already successfully rolled back the table to an external state, changing the external DeltaLog version after the current transaction started. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Error Message

The full error message includes the mismatched versions for diagnostic purposes:

```
VERSION_MISMATCH
The versions of the managed DeltaLog (<managedDeltaLogVersion>) and external DeltaLog (<externalDeltaLogVersion>) do not match.
```

## Resolution

The VERSION_MISMATCH error indicates a concurrency conflict. To resolve it, the user should retry the `ALTER TABLE tbl UNSET MANAGED` command. On retry, the command will read the latest committed DeltaLog versions and proceed if the versions are now consistent.

## Related Concepts

- Delta Log
- [ALTER TABLE UNSET MANAGED](/concepts/alter-table-unset-managed-command.md)
- [Managed vs External Tables](/concepts/managed-vs-external-tables-in-unity-catalog.md)
- [Delta Lake Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md)
- DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED error class

## Sources

- delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws-a24f2e75.md)
