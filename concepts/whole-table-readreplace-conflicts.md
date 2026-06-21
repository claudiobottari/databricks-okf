---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0afdc6305b53a9823cc8f1c523e9744b078fe67bebcc50e132ee676f2f5e38f0
  pageDirectory: concepts
  sources:
    - delta_concurrent_append-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - whole-table-readreplace-conflicts
    - WTRC
    - WHOLE_TABLE_READ
    - WHOLE_TABLE_REPLACE
  citations:
    - file: delta_concurrent_append-error-condition-databricks-on-aws.md
title: Whole Table Read/Replace Conflicts
description: Conflict scenarios where a transaction reads or replaces the entire table while a concurrent modification occurs, with recommendations to narrow data scope or retry.
tags:
  - delta-lake
  - concurrency
  - transactions
timestamp: "2026-06-19T18:22:57.323Z"
---

# Whole Table Read/Replace Conflicts

**Whole Table Read/Replace Conflicts** are specific error conditions within the `DELTA_CONCURRENT_APPEND` error class that occur when a transaction attempts to read or replace an entire Delta table while a concurrent modification is in progress. These conflicts are detected by Delta Lake's row-level conflict resolution mechanism and require the operation to be retried.

## WHOLE_TABLE_READ

The `WHOLE_TABLE_READ` error occurs when a transaction attempts to read the entire table, conflicting with a concurrent modification. This happens because the read operation's scope overlaps with changes being made by another transaction. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

To resolve this conflict, consider adding filters to your query to narrow the data scope, or retry the operation. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## WHOLE_TABLE_REPLACE

The `WHOLE_TABLE_REPLACE` error occurs when a concurrent operation replaces all data in the table while another transaction is in progress. This represents a fundamental conflict where the entire table's contents are being overwritten simultaneously by another operation. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

The recommended resolution is to retry the operation. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Related Error Conditions

Both `WHOLE_TABLE_READ` and `WHOLE_TABLE_REPLACE` are part of the broader `DELTA_CONCURRENT_APPEND` error class, which includes other conflict types such as:

- ROW_LEVEL_CHANGES — When concurrent operations modify the same rows
- [PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE](/concepts/partitioned-table-merge-conflicts-in-delta-lake.md) — When row-level conflict detection cannot be performed on partitioned tables
- PREDICATES_NEED_REWRITE — When filter predicates cannot be applied for conflict detection
- PROTOCOL_CHANGE — When a concurrent operation upgrades the table protocol
- ALLOTTED_TIME_EXCEEDED Sub-error|ALLOTTED_TIME_EXCEEDED — When row-level conflict resolution exceeds the time limit

## Related Concepts

- [Delta Lake Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) — The mechanism for handling concurrent transactions
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — The foundation for conflict detection
- [Row-Level Conflict Resolution](/concepts/row-level-conflict-resolution.md) — The system that detects and resolves conflicts at the row level
- [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) — The underlying concurrency model used by Delta Lake

## Sources

- delta_concurrent_append-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_append-error-condition-databricks-on-aws.md](/references/delta_concurrent_append-error-condition-databricks-on-aws-47a87778.md)
