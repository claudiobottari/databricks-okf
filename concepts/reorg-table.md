---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 703788eb621ad7111b90337ae9abb98365bd5d21b41261ade3696ce74cce4758
  pageDirectory: concepts
  sources:
    - reorg-table-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - reorg-table
  citations:
    - file: reorg-table-databricks-on-aws.md
title: REORG TABLE
description: A Databricks SQL command to reorganize Delta Lake tables by rewriting files to purge soft-deleted data, upgrade to Iceberg format, or perform checkpointing.
tags:
  - delta-lake
  - sql-command
  - table-maintenance
timestamp: "2026-06-19T20:13:15.711Z"
---

# REORG TABLE

**REORG TABLE** is a SQL command in Databricks that reorganizes a [Delta Lake](/concepts/delta-lake.md) table by rewriting files to purge soft-deleted data or by performing Delta Lake checkpointing to improve metadata management. It helps maintain table performance and supports cleanup operations that are not handled by standard DML commands. ^[reorg-table-databricks-on-aws.md]

## Syntax

```
REORG [ TABLE ] table_name { [ WHERE predicate ] APPLY ( PURGE ) |
                             APPLY ( UPGRADE UNIFORM ( ICEBERG_COMPAT_VERSION = version ) |
                                     CHECKPOINT ) }
```

For Databricks Runtime versions before 15.4, `TABLE` is a mandatory keyword. ^[reorg-table-databricks-on-aws.md]

## Behavior

REORG TABLE is an _idempotent_ operation, meaning that if it is run twice on the same dataset, the second run has no effect. ^[reorg-table-databricks-on-aws.md]

- `APPLY (PURGE)` only rewrites files that contain soft-deleted data. ^[reorg-table-databricks-on-aws.md]
- `APPLY (UPGRADE)` may rewrite all files. ^[reorg-table-databricks-on-aws.md]
- After running `APPLY (PURGE)`, the soft-deleted data may still exist in the old files. You can run `VACUUM` to physically delete the old files. ^[reorg-table-databricks-on-aws.md]
- `APPLY (CHECKPOINT)` requires the table to have Checkpoint V2 enabled to prevent corruption caused by race conditions. ^[reorg-table-databricks-on-aws.md]

## Parameters

- **table_name**: Identifies an existing Delta table. The name must not include a [temporal specification or options specification](/concepts/temporal-specification-restriction-on-describe-history.md). ^[reorg-table-databricks-on-aws.md]

- **WHERE predicate**: For `APPLY (PURGE)`, reorganizes only the files that match the given partition predicate. Only filters involving partition key attributes are supported. ^[reorg-table-databricks-on-aws.md]

- **APPLY (PURGE)**: Specifies that the purpose of file rewriting is to purge soft-deleted data, such as column data dropped by ALTER TABLE DROP COLUMN. ^[reorg-table-databricks-on-aws.md]

- **APPLY (UPGRADE UNIFORM ( ICEBERG_COMPAT_VERSION = version ))**: Specifies that the purpose of file rewriting is to upgrade the table to the given [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) version. `version` must be either `1` or `2`. Available in Databricks Runtime 14.3 and above. ^[reorg-table-databricks-on-aws.md]

- **APPLY (CHECKPOINT)**: Performs Delta checkpointing on the table's latest Delta version. Available in Databricks Runtime 16.3 and above. ^[reorg-table-databricks-on-aws.md]

## Examples

```sql
> REORG TABLE events APPLY (PURGE);

> REORG TABLE events WHERE date >= '2022-01-01' APPLY (PURGE);

> REORG TABLE events
    WHERE date >= current_timestamp() - INTERVAL '1' DAY
    APPLY (PURGE);

> REORG TABLE events APPLY (UPGRADE UNIFORM(ICEBERG_COMPAT_VERSION=2));

> REORG TABLE events APPLY (CHECKPOINT);
```

^[reorg-table-databricks-on-aws.md]

## Use Cases

- **Purging dropped columns**: When you use `ALTER TABLE DROP COLUMN`, the column data is only soft-deleted. `REORG TABLE APPLY (PURGE)` rewrites the files to physically remove the dropped column data. ^[reorg-table-databricks-on-aws.md]
- **Upgrading to Iceberg format**: Convert a Delta table to be compatible with Apache Iceberg readers by specifying the target Iceberg version. ^[reorg-table-databricks-on-aws.md]
- **Improving metadata management**: Perform checkpointing to compact the Delta transaction log and improve metadata query performance. ^[reorg-table-databricks-on-aws.md]

## Related Concepts

- VACUUM – Physically deletes old files after purging soft-deleted data
- Delta Lake Checkpointing – Metadata management technique for Delta tables
- Checkpoint V2 – Required for safe `APPLY (CHECKPOINT)` operations
- ALTER TABLE DROP COLUMN – Operation that creates soft-deleted data requiring purge
- [Delta Lake on Databricks](/concepts/delta-lake-on-databricks.md) – Overview of Delta Lake capabilities
- Apache Iceberg Compatibility – Reading Delta tables as Iceberg format

## Sources

- reorg-table-databricks-on-aws.md

# Citations

1. [reorg-table-databricks-on-aws.md](/references/reorg-table-databricks-on-aws-58d61683.md)
