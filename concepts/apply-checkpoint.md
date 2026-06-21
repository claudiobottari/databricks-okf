---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b003b2785e40afb6b0f36b0557297928bd397928255be98ff48d742dfb88a26e
  pageDirectory: concepts
  sources:
    - reorg-table-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - apply-checkpoint
  citations:
    - file: reorg-table-databricks-on-aws.md
title: APPLY (CHECKPOINT)
description: A REORG TABLE subcommand that performs Delta checkpointing on the table's latest Delta version to improve metadata management.
tags:
  - checkpointing
  - delta-lake
  - metadata
timestamp: "2026-06-19T20:13:22.565Z"
---

## APPLY (CHECKPOINT)

`APPLY (CHECKPOINT)` is a subcommand of the `REORG TABLE` statement in Databricks SQL and Databricks Runtime. It performs Delta checkpointing on the latest Delta version of the target table, helping to improve metadata management by compacting the transaction log. ^[reorg-table-databricks-on-aws.md]

### Syntax

```sql
REORG TABLE table_name APPLY (CHECKPOINT)
```

The `TABLE` keyword is mandatory in Databricks Runtime versions before 15.4. The `table_name` must identify an existing Delta table and must not include a temporal specification or options specification. ^[reorg-table-databricks-on-aws.md]

### Requirements

`APPLY (CHECKPOINT)` requires the table to have Checkpoint V2 enabled. Checkpoint V2 prevents corruption that can arise from race conditions during concurrent write operations. ^[reorg-table-databricks-on-aws.md]

### Applicability

- **Applies to:** ![check marked yes] Databricks SQL and Databricks Runtime 16.3 and above. ^[reorg-table-databricks-on-aws.md]

### Idempotency

Like other `REORG TABLE` operations, `APPLY (CHECKPOINT)` is idempotent: running it twice on the same dataset has no additional effect. ^[reorg-table-databricks-on-aws.md]

### Related Subcommands

- `APPLY (PURGE)` – Rewrites files to purge soft-deleted data (e.g., columns dropped by `ALTER TABLE DROP COLUMN`). After `APPLY (PURGE)`, the old files still exist and can be physically removed with VACUUM. ^[reorg-table-databricks-on-aws.md]
- `APPLY (UPGRADE UNIFORM ( ICEBERG_COMPAT_VERSION = version ))` – Upgrades the table to a given Apache Iceberg version (1 or 2). Applies to Databricks Runtime 14.3 and above. ^[reorg-table-databricks-on-aws.md]

### Example

```sql
REORG TABLE events APPLY (CHECKPOINT);
```

### Related Concepts

- [REORG TABLE](/concepts/reorg-table.md) – The parent command that reorganizes a Delta table.
- [Delta Lake](/concepts/delta-lake.md) – The storage layer underlying Delta tables.
- Checkpoint V2 – The checkpoint mechanism required for `APPLY (CHECKPOINT)`.
- VACUUM – Command to physically delete old files after purging soft-deleted data.
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) – The log that checkpointing compacts.

### Sources

- reorg-table-databricks-on-aws.md

# Citations

1. [reorg-table-databricks-on-aws.md](/references/reorg-table-databricks-on-aws-58d61683.md)
