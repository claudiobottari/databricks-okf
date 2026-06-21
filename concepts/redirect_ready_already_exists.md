---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f0268f02f36e4ce049b5136d5dd7ea818b6d139a20f83b1cfaeaf8dcc4ec974f
  pageDirectory: concepts
  sources:
    - delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - redirect_ready_already_exists
    - REDIRECT_READY_ALREADY_EXISTS
    - redirect_ready_already_exists-error
    - REDIRECT_READY_ALREADY_EXISTS error (Delta managed migration)
    - redirect_ready_already_exists-sub-error
  citations:
    - file: delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
title: REDIRECT_READY_ALREADY_EXISTS
description: A sub-error of DELTA_ALTER_TABLE_SET_MANAGED_FAILED indicating the table already has a RedirectReady state, likely due to a concurrent ALTER TABLE SET MANAGED completing the migration first.
tags:
  - databricks
  - error-messages
  - concurrency
timestamp: "2026-06-18T11:49:36.894Z"
---

---
title: REDIRECT_READY_ALREADY_EXISTS
summary: An error condition in Databricks that occurs when a table already has the `RedirectReady` state, typically because a concurrent `ALTER TABLE ... SET MANAGED` command has already migrated the table.
sources:
  - delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:00:00.000Z"
updatedAt: "2026-06-18T12:00:00.000Z"
tags:
  - databricks
  - error
  - delta-lake
  - troubleshooting
aliases:
  - redirect_ready_already_exists
  - RRAE
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 1
---

# REDIRECT_READY_ALREADY_EXISTS

**REDIRECT_READY_ALREADY_EXISTS** is an error condition that occurs within the `DELTA_ALTER_TABLE_SET_MANAGED_FAILED` error class when an `ALTER TABLE ... SET MANAGED` command fails because the table already has the `RedirectReady` state. This typically indicates that a concurrent operation has already started or completed the migration to a managed table.

## Error Message

When this condition is triggered, the error message resembles:

```
DELTA_ALTER_TABLE_SET_MANAGED_FAILED
REDIRECT_READY_ALREADY_EXISTS
```

The full error class is `DELTA_ALTER_TABLE_SET_MANAGED_FAILED` with SQLSTATE 42809 (syntax error or access rule violation). ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Cause

The table already has the `RedirectReady` state, which means a previous or concurrent `ALTER TABLE <table> SET MANAGED` command has placed the table in a transitional state or has already completed the migration. The error is raised because the system cannot initiate a second migration on a table already in the `RedirectReady` state. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Solution

1. **Check whether the migration already succeeded.** Run `DESC EXTENDED <table>` and inspect the table type. If the table is now `MANAGED`, no further action is required. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]
2. If the table is still `EXTERNAL` or the migration is incomplete, verify that no other concurrent `ALTER TABLE ... SET MANAGED` command is running, then retry the operation.
3. If the issue persists, contact Databricks support.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer underlying managed and external tables
- [ALTER TABLE SET MANAGED](/concepts/alter-table-set-managed.md) — The DDL command that migrates an external table to a managed table
- [Managed Table](/concepts/unity-catalog-managed-tables.md) — A table whose data is managed by Databricks
- External Table — A table whose data resides in an external location
- DELTA_ALTER_TABLE_SET_MANAGED_FAILED — The parent error class that includes this and other conditions such as `CANNOT_FINALIZE_REDIRECT`, `FILE_VALIDATION_FAILED`, and `VERSION_MISMATCH`

## Sources

- delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_set_managed_failed-error-condition-databricks-on-aws-ddfd0547.md)
