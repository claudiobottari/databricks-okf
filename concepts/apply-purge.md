---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3da05d4f5cf1382b7c7446b376beaa9e2ae04e2c391a1825da61bc6f0c616df1
  pageDirectory: concepts
  sources:
    - reorg-table-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - apply-purge
    - PURGE
  citations:
    - file: reorg-table-databricks-on-aws.md
title: APPLY (PURGE)
description: A REORG TABLE subcommand that rewrites files containing soft-deleted data (e.g., from ALTER TABLE DROP COLUMN) to physically remove it from files.
tags:
  - data-purging
  - delta-lake
  - soft-delete
timestamp: "2026-06-19T20:13:54.989Z"
---

# APPLY (PURGE)

The `APPLY (PURGE)` operation is a subcommand of the [REORG TABLE](/concepts/reorg-table.md) statement in [Delta Lake](/concepts/delta-lake.md) on Databricks. It triggers a file rewrite that permanently removes soft-deleted data from a Delta table’s storage layer, such as column data dropped by `ALTER TABLE DROP COLUMN`. ^[reorg-table-databricks-on-aws.md]

## Description

When columns or rows are logically removed from a Delta table via metadata-only operations, the underlying data files still contain the discarded information. `APPLY (PURGE)` identifies those files and rewrites them to exclude the soft-deleted data, thereby reclaiming space at the logical level. The command does **not** physically delete the old files; those must be removed separately with `VACUUM`. ^[reorg-table-databricks-on-aws.md]

This operation is available in Databricks Runtime 11.3 LTS and above. ^[reorg-table-databricks-on-aws.md]

## Syntax

```sql
REORG TABLE table_name [ WHERE predicate ] APPLY ( PURGE )
```

For Databricks Runtime versions before 15.4, the `TABLE` keyword is mandatory. ^[reorg-table-databricks-on-aws.md]

### Parameters

- **table_name**  
  Identifies an existing Delta table. The name must not include a temporal specification or options specification. ^[reorg-table-databricks-on-aws.md]

- **`WHERE` predicate** (optional)  
  A boolean expression that restricts which files are rewritten. Only filters involving partition key attributes are supported. If omitted, all files containing soft-deleted data are processed. ^[reorg-table-databricks-on-aws.md]

- **`APPLY (PURGE)`**  
  Specifies that the purpose of file rewriting is to purge soft-deleted data (e.g., columns removed by `DROP COLUMN`). ^[reorg-table-databricks-on-aws.md]

## Behavior

- `APPLY (PURGE)` rewrites **only** files that contain soft-deleted data; files without any dropped columns or rows are left unchanged. ^[reorg-table-databricks-on-aws.md]
- The operation is **idempotent**: running it multiple times on the same data produces no additional effect after the first successful execution. ^[reorg-table-databricks-on-aws.md]
- After `APPLY (PURGE)`, the soft-deleted data may still exist in the old (unreferenced) files. To physically remove those files from storage, run `VACUUM` on the table. ^[reorg-table-databricks-on-aws.md]

## Example

Purge all soft-deleted data from the `events` table:

```sql
REORG TABLE events APPLY (PURGE);
```

Purge only from partitions where `date` is on or after `2022-01-01`:

```sql
REORG TABLE events WHERE date >= '2022-01-01' APPLY (PURGE);
```

Purge from partitions within the last day:

```sql
REORG TABLE events
  WHERE date >= current_timestamp() - INTERVAL '1' DAY
  APPLY (PURGE);
```

^[reorg-table-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The storage engine behind this operation.
- VACUUM – Command to physically delete old files after purging.
- ALTER TABLE DROP COLUMN – A common source of soft-deleted column data.
- Soft Delete – The logical removal mechanism that `APPLY (PURGE)` resolves.
- Partition Predicate – Used in the `WHERE` clause to limit file rewriting.
- [REORG TABLE](/concepts/reorg-table.md) – The parent command that includes `APPLY (PURGE)` as well as other operations like `APPLY (CHECKPOINT)` and `APPLY (UPGRADE UNIFORM)`.

## Sources

- reorg-table-databricks-on-aws.md

# Citations

1. [reorg-table-databricks-on-aws.md](/references/reorg-table-databricks-on-aws-58d61683.md)
