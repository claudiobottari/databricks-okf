---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 29e077afcde3b0bd44ed90219d10476dda348ab97377e71ab62250fd1de97886
  pageDirectory: concepts
  sources:
    - delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - desc-extended-diagnostic-command
    - DEDC
    - DESC EXTENDED
    - DESC EXTENDED Command
  citations:
    - file: delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md
title: DESC EXTENDED diagnostic command
description: A Databricks SQL command used to inspect a table's metadata and verify whether an ALTER TABLE SET MANAGED migration has already completed.
tags:
  - databricks
  - sql
  - diagnostics
  - table-management
timestamp: "2026-06-19T15:00:32.836Z"
---

# DESC EXTENDED Diagnostic Command

**DESC EXTENDED** is a diagnostic command used in Databricks to inspect the current state of a table, particularly to verify whether a table has been successfully migrated from external to managed storage. It is commonly referenced in troubleshooting scenarios involving the `DELTA_ALTER_TABLE_SET_MANAGED_FAILED` error condition. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Overview

The `DESC EXTENDED` command (short for `DESCRIBE EXTENDED`) provides detailed metadata about a table, including its storage location, table properties, and current state. When used after an `ALTER TABLE ... SET MANAGED` operation, it reveals whether the migration completed successfully by showing the table's current state. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Usage

Run the command against the table you want to inspect:

```sql
DESC EXTENDED <table_name>;
```

Replace `<table_name>` with the fully qualified name of the table (e.g., `catalog.schema.table_name`). ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Diagnostic Purpose

The primary diagnostic use of `DESC EXTENDED` is to check whether a table has already been migrated to managed storage after a failed or concurrent `ALTER TABLE ... SET MANAGED` command. This is specifically relevant for two error subconditions: ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

- **REDIRECT_READY_ALREADY_EXISTS**: When the error indicates the table already has a `RedirectReady` state, running `DESC EXTENDED` confirms whether the migration was completed by a concurrent command. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]
- **VERSION_MISMATCH**: When the managed DeltaLog version does not match the expected version, `DESC EXTENDED` verifies if a concurrent `ALTER TABLE ... SET MANAGED` command already migrated the table. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Interpreting Results

After running `DESC EXTENDED`, examine the output for:

- **Table Type**: Indicates whether the table is `MANAGED` or `EXTERNAL`.
- **Location**: Shows the storage path. A managed table will have a location within the managed storage location.
- **Table Properties**: May include state information relevant to the migration process.

If the table shows as `MANAGED`, the migration has already succeeded and no further action is needed. If it still shows as `EXTERNAL`, the migration failed and may need to be retried. ^[delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md]

## Related Concepts

- [ALTER TABLE SET MANAGED](/concepts/alter-table-set-managed.md) — The command that triggers table migration from external to managed storage.
- DELTA_ALTER_TABLE_SET_MANAGED_FAILED — The error condition that occurs when migration fails.
- [Managed vs External Tables](/concepts/managed-vs-external-tables-in-unity-catalog.md) — The distinction between table storage types in Databricks.
- Delta Log — The transaction log that tracks table state changes.
- [Table Metadata](/concepts/trace-metadata.md) — The detailed information displayed by `DESC EXTENDED`.

## Sources

- delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_set_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_set_managed_failed-error-condition-databricks-on-aws-ddfd0547.md)
