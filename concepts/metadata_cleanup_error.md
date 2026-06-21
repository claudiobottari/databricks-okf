---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6544532ea57b8ff955a81af0ac2f883fc50babec8b544081a8075e8264565d00
  pageDirectory: concepts
  sources:
    - delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metadata_cleanup_error
    - METADATA_CLEANUP_ERROR
    - metadata_cleanup_error-sub-error
  citations:
    - file: delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md
title: METADATA_CLEANUP_ERROR
description: A specific sub-error under DELTA_ALTER_TABLE_SET_MANAGED_TABLE_NOT_MIGRATABLE indicating failure to create a checkpoint or clean up old metadata files before migration.
tags:
  - error-messages
  - metadata
  - databricks
timestamp: "2026-06-19T18:21:56.865Z"
---

---
title: METADATA_CLEANUP_ERROR
summary: A sub-error of the DELTA_ALTER_TABLE_SET_MANAGED_TABLE_NOT_MIGRATABLE class, indicating failure to create a checkpoint or clean up old metadata files during table migration
sources:
  - delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T15:16:38.634Z"
updatedAt: "2026-06-19T15:01:22.437Z"
tags:
  - databricks
  - error-messages
  - delta-lake
aliases:
  - metadata_cleanup_error
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# METADATA_CLEANUP_ERROR

**METADATA_CLEANUP_ERROR** is a specific error condition that occurs during the execution of `ALTER TABLE <table> SET MANAGED` when Databricks is unable to create a checkpoint or clean up old metadata files before migrating the table. ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Overview

This error is a subtype of the broader DELTA_ALTER_TABLE_SET_MANAGED_TABLE_NOT_MIGRATABLE error condition (SQLSTATE: 55019). It indicates that the table migration process to managed status cannot proceed because the system encountered a failure during the metadata cleanup phase. ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Error Message Format

```
METADATA_CLEANUP_ERROR

Unable to create checkpoint or clean up old metadata files before migrating the table.

== Error ==

<error>
```

^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Cause

The error occurs when the [Delta Lake](/concepts/delta-lake.md) transaction log cannot be properly checkpointed or when old metadata files cannot be cleaned up as part of the table migration process. This may be caused by:

- Insufficient permissions on the underlying storage location
- Concurrent operations on the table that conflict with the migration
- Corrupted or inconsistent metadata files
- Storage system issues or transient failures

## Resolution

### Recommended Steps

1. **Ensure the table is in a valid state.** Verify that the table is not currently involved in concurrent write operations or other ALTER TABLE commands. ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]
2. **Retry the command.** The issue may be transient; retrying the `ALTER TABLE <table> SET MANAGED` command can often resolve the problem. ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]
3. **Contact Databricks support.** If the issue persists after retrying, contact Databricks support for further assistance. ^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

### Preventive Measures

- Run table maintenance operations such as OPTIMIZE and VACUUM before attempting migration.
- Ensure that no other processes are writing to the table during the migration.
- Verify storage credentials and permissions are correctly configured.

## Related Concepts

- DELTA_ALTER_TABLE_SET_MANAGED_TABLE_NOT_MIGRATABLE — The parent error condition for table migration failures.
- [Managed Tables in Databricks](/concepts/managed-tables-in-databricks.md) — The target state of the migration operation.
- Delta Lake Checkpoints — The checkpointing mechanism that may fail during migration.
- Table Migration Best Practices — Guidelines for safely converting between table types.
- [SQLSTATE 55019](/concepts/sqlstate-55019.md) — The SQL standard error class for object-not-in-prerequisite-state.

## Sources

- delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md](/references/delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws-c36210c9.md)
