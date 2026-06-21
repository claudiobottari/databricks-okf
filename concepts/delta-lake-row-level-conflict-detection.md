---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 23801876595883e693829508d51b14f1e84264b5dd4704ccd68b75c419c6b5d8
  pageDirectory: concepts
  sources:
    - delta_concurrent_append-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-row-level-conflict-detection
    - DLRCD
    - Table-Level Conflict Detection
    - MERGE and row-level conflict detection
    - Row-Level Conflict Detection
    - Row-level Conflict Detection
    - Row-level conflict detection
    - row-level conflict detection
  citations:
    - file: delta_concurrent_append-error-condition-databricks-on-aws.md
    - file: |-
        delta_concurrent_append-error-condition-databricks-on-aws.md>

        All sub‑conditions refer to a `<docLink>` for more information
    - file: indicating that Delta Lake provides detailed guidance for each scenario. ^[delta_concurrent_append-error-condition-databricks-on-aws.md
title: Delta Lake Row-Level Conflict Detection
description: A mechanism used by Delta Lake to detect and resolve transaction conflicts at the granularity of individual rows, with constraints on time, predicates, and metadata.
tags:
  - delta-lake
  - concurrency
  - transactions
timestamp: "2026-06-19T15:02:46.701Z"
---

# Delta Lake Row-Level Conflict Detection

**Delta Lake Row-Level Conflict Detection** is a mechanism that identifies and resolves conflicts when multiple concurrent transactions attempt to modify the same rows in a Delta table. It is part of Delta Lake’s [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) and is exposed through the `DELTA_CONCURRENT_APPEND` error class, which is raised when a transaction conflict is detected. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Error Class: `DELTA_CONCURRENT_APPEND`

When Delta Lake detects a transactional conflict, it returns the error `DELTA_CONCURRENT_APPEND` with the message: *"Transaction conflict detected. A concurrent `<operation>` added data to table `<tableName>` committed at version `<version>`."* ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

The error class includes several sub‑conditions that provide detailed information about why row‑level conflict detection failed or was not possible. These sub‑conditions help users understand the nature of the conflict and how to resolve it. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Sub‑Conditions of `DELTA_CONCURRENT_APPEND`

Each sub‑condition corresponds to a specific conflict scenario. The following are described in the Delta Lake error documentation:

- **`ROW_LEVEL_CHANGES`** — The concurrent operation modified the same rows that the current transaction attempted to modify. The recommended action is to retry the operation. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]
- **`ALLOTTED_TIME_EXCEEDED`** — Row‑level conflict resolution exceeded the allotted time. The operation should be retried. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]
- **`CHANGE_TYPE_COLUMN`** — The table contains a column named `_change_type`, which conflicts with Change Data Feed (CDC) metadata columns, preventing row‑level conflict detection. The column must be renamed. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]
- **`PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE`** — Row‑level conflict detection could not be performed on this partitioned table. The operation should be retried. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]
- **`PREDICATES_NEED_REWRITE`** — The filter predicates used by this transaction could not be applied for row‑level conflict detection. The operation should be retried. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]
- **`PROTOCOL_CHANGE`** — The concurrent operation upgraded the table protocol (e.g., schema or partitioning). The operation should be retried. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]
- **`WHOLE_TABLE_READ`** — This transaction attempted to read the entire table, conflicting with the concurrent modification. Consider adding filters to narrow the data scope, or retry the operation. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]
- **`WHOLE_TABLE_REPLACE`** — The concurrent operation replaced all data in the table. The operation should be retried. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]
- **`WITHOUT_HINT`** — A generic conflict detection failure occurred. The operation should be retried. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]
- **`WITH_PARTITION_HINT`** — The concurrent operation modified data in the partition `<partitionValues>` that should have been read by this operation. The operation should be retried. ^[delta_concurrent_append-error-condition-databricks-on-aws.md>

All sub‑conditions refer to a `<docLink>` for more information, indicating that Delta Lake provides detailed guidance for each scenario. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Related Concepts

- [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) — The underlying concurrency model used by Delta Lake.
- MERGE — An operation that often triggers row‑level conflict detection.
- UPDATE and DELETE — Operations that can conflict when overlapping rows are modified.
- Change Data Feed (CDC) — A metadata feature that can interfere with conflict detection if column names clash.
- [Delta Lake Transactions](/concepts/delta-acid-transactions.md) — The atomic commit mechanism that detects and resolves conflicts.

## Sources

- delta_concurrent_append-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_append-error-condition-databricks-on-aws.md](/references/delta_concurrent_append-error-condition-databricks-on-aws-47a87778.md)
2. delta_concurrent_append-error-condition-databricks-on-aws.md>

All sub‑conditions refer to a `<docLink>` for more information
3. indicating that Delta Lake provides detailed guidance for each scenario. ^[delta_concurrent_append-error-condition-databricks-on-aws.md
