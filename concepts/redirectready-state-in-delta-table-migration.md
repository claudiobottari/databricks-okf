---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e31652a7eac3d49e77fe7aa2a5fc4efc7679e9e81e0c055b19073c2485948405
  pageDirectory: concepts
  sources:
    - delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - redirectready-state-in-delta-table-migration
    - RSIDTM
  citations:
    - file: delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
title: RedirectReady state in Delta table migration
description: An intermediate state during the ALTER TABLE SET MANAGED migration indicating the table is ready for redirect; duplicate RedirectReady state suggests concurrent migration already finished.
tags:
  - delta-lake
  - table-migration
  - databricks
timestamp: "2026-06-18T15:16:17.685Z"
---

# RedirectReady State in Delta Table Migration

The **RedirectReady state** is an intermediate state that a [Delta table](/concepts/delta-lake-table.md) enters during migration from an external table to a managed table via the `ALTER TABLE SET MANAGED` command. This state indicates that the migration process has been initiated but not yet finalized.

## Overview

When executing `ALTER TABLE <table> SET MANAGED` to convert an external Delta table to a managed table, the table transitions through a **RedirectReady state** before completion. This state represents a checkpoint in the migration process where the redirect configuration has been partially established. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Related Error Condition

### REDIRECT_READY_ALREADY_EXISTS

The `REDIRECT_READY_ALREADY_EXISTS` error occurs when attempting to run `ALTER TABLE SET MANAGED` on a table that is already in the RedirectReady state. This can happen if:

- A concurrent `ALTER TABLE tbl SET MANAGED` command already started the migration process.
- The migration may have already completed successfully by a concurrent operation. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

#### Resolution

When encountering the `REDIRECT_READY_ALREADY_EXISTS` error, check if the table is already fully migrated to managed by running:

```sql
DESC EXTENDED tbl;
```

This command displays the table's metadata, including its current state and whether it has been successfully converted to a managed table. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

### CANNOT_FINALIZE_REDIRECT

The `CANNOT_FINALIZE_REDIRECT` error can occur if the redirect configuration doesn't exist during finalization. This may happen if the table is currently rolling back to external. If the issue persists, contact Databricks support. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Migration Process

The RedirectReady state is part of a two-phase migration process:

1. **Phase 1**: The `ALTER TABLE SET MANAGED` command initiates the migration and establishes redirect configuration, placing the table in RedirectReady state.
2. **Phase 2**: The migration finalizes, moving the table from RedirectReady to fully managed state.

Concurrent migration attempts on the same table will result in `REDIRECT_READY_ALREADY_EXISTS` or `VERSION_MISMATCH` errors if another process has already initiated or completed the migration. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Related Error Conditions

### VERSION_MISMATCH

The `VERSION_MISMATCH` error indicates that the managed DeltaLog version does not match the expected version. This can occur if a concurrent `ALTER TABLE SET MANAGED` command has already successfully migrated the table. Verify the table state with `DESC EXTENDED tbl`. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

### FILE_VALIDATION_FAILED

The `FILE_VALIDATION_FAILED` error occurs when file validation fails during migration, indicating that some files could not be migrated. The error message specifies the missing file count. Retry the operation or contact Databricks support if the issue persists. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Related Concepts

- [Managed vs External Tables](/concepts/managed-vs-external-tables-in-unity-catalog.md) — The distinction between table types in Databricks
- Delta Table Architecture — How Delta Lake manages table metadata and state transitions
- [ALTER TABLE SET MANAGED](/concepts/alter-table-set-managed.md) — The command that triggers the migration into RedirectReady state

## Sources

- delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_set_managed_failed-error-condition-databricks-on-aws-ddfd0547.md)
