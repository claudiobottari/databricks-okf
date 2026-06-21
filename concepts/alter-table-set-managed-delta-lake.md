---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 77450f2afd6efab1b248c64dfeb6ec0f3aa5992cb5c6e1746d85fcdefdb74aea
  pageDirectory: concepts
  sources:
    - delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - alter-table-set-managed-delta-lake
    - ATSM(L
  citations:
    - file: delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md
title: ALTER TABLE SET MANAGED (Delta Lake)
description: A Delta Lake SQL command that attempts to convert an unmanaged (external) table to a managed table in Databricks.
tags:
  - sql-command
  - delta-lake
  - table-management
timestamp: "2026-06-18T15:16:36.467Z"
---

# ALTER TABLE SET MANAGED (Delta Lake)

**`ALTER TABLE SET MANAGED`** is a Delta Lake command that converts an existing table into a [managed table](/concepts/unity-catalog-managed-tables.md). The operation migrates the table’s metadata and data to be fully managed by the [Metastore](/concepts/metastore.md), but can fail under certain conditions.

## Error: DELTA_ALTER_TABLE_SET_MANAGED_TABLE_NOT_MIGRATABLE

When the migration cannot be completed, Delta Lake raises the error class `DELTA_ALTER_TABLE_SET_MANAGED_TABLE_NOT_MIGRATABLE` (SQLSTATE: 55019). The core error message is:

> `ALTER TABLE <table> SET MANAGED` is unable to migrate the given table. Make sure the table is in a valid state and retry the command. If the issue persists, contact Databricks support.

^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

### Sub‑error: METADATA_CLEANUP_ERROR

A known sub‑error is **METADATA_CLEANUP_ERROR**. This occurs when Delta Lake cannot create a checkpoint or clean up old metadata files before completing the migration. The accompanying detail provides additional context about the underlying cause.

```
METADATA_CLEANUP_ERROR
== Error ==
<error>
```

^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Common Causes

- The table is in an inconsistent or invalid state (e.g., missing files, corrupted transaction log).
- Metadata files from previous operations cannot be cleaned up or checkpointed.
- Insufficient permissions to modify the table’s underlying storage.

## Troubleshooting Steps

1. **Verify table state** — Ensure all Delta transaction log entries are valid and no concurrent writes are interfering.
2. **Retry the command** — Simple transient issues may resolve on retry.
3. **Contact Databricks support** — If the error persists, provide the full error details for further investigation.

^[delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md]

## Related Concepts

- [Managed tables](/concepts/managed-tables-in-databricks.md) — Tables whose data and metadata are fully owned by the [Metastore](/concepts/metastore.md).
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that provides ACID transactions and time travel.
- ALTER TABLE command — General syntax for modifying table properties.
- Checkpointing in Delta Lake — Mechanism that compacts the transaction log and influences the `METADATA_CLEANUP_ERROR`.

## Sources

- delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md

# Citations

1. [delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws.md](/references/delta_alter_table_set_managed_table_not_migratable-error-condition-databricks-on-aws-c36210c9.md)
