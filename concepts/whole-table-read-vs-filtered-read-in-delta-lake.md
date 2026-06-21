---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9c48620599abf1ba00041f137f8a4e7e38c43515bd1f17dddb6a5143ba93c10c
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_read-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - whole-table-read-vs-filtered-read-in-delta-lake
    - WTRVFRIDL
  citations:
    - file: delta_concurrent_delete_read-error-condition-databricks-on-aws.md
title: Whole Table Read vs Filtered Read in Delta Lake
description: A pattern where reading an entire Delta table (without filters) increases the likelihood of transaction conflicts with concurrent delete operations, mitigated by adding filter predicates.
tags:
  - delta-lake
  - query-optimization
  - transaction-conflicts
timestamp: "2026-06-19T15:04:04.191Z"
---

# Whole Table Read vs Filtered Read in Delta Lake

**Whole Table Read vs Filtered Read in Delta Lake** describes a fundamental distinction in how read transactions interact with concurrent write operations, particularly deletions. The difference determines whether a transaction can use [Row-Level Conflict Resolution](/concepts/row-level-conflict-resolution.md) or will encounter a conflict that requires a retry.

## Overview

When a Delta Lake read transaction conflicts with a concurrent delete operation, the system evaluates whether the read was scoped to a subset of data or read the entire table. This distinction affects the error condition returned and the retry strategy available. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Whole Table Read

A **Whole Table Read** occurs when a transaction reads all data in a table without applying any filters. If a concurrent delete operation removes data from the table, the read transaction receives a `WHOLE_TABLE_READ` error condition under the `DELTA_CONCURRENT_DELETE_READ` error class. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

The error message states that the transaction "attempted to read the entire table, conflicting with the concurrent deletion." The recommended resolution is to add filters to narrow the data scope and retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Filtered Read

A **Filtered Read** restricts the data scope using predicates such as `WHERE` clauses or partition filters. Filtered reads are eligible for [Row-Level Conflict Resolution](/concepts/row-level-conflict-resolution.md), which can resolve conflicts at the row level without requiring a full retry.

The system provides several sub-conditions related to filtered reads that encountered issues during row-level conflict detection:

- **EMPTY_READ_PREDICATES**: The transaction did not include any filters and read the entire table, conflicting with the concurrent deletion.
- **PREDICATES_NEED_REWRITE**: The filter predicates could not be applied for row-level conflict detection.
- **ROW_LEVEL_CHANGES**: The concurrent operation deleted rows that this transaction attempted to read, requiring a retry.

## Partition-Based Reads

Reads that are scoped to specific partitions use a different conflict resolution path. The `WITH_PARTITION_HINT` condition indicates that "the concurrent operation deleted data in the partition that was read by this operation." ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Retry Strategy

The general recommendation for whole table reads that encounter conflicts is to:

1. **Add filters** to your query to narrow the data scope
2. **Retry the operation**

For filtered reads where row-level resolution succeeds, no retry is necessary. For filtered reads where row-level resolution fails (e.g., `ROW_LEVEL_CHANGES`), a retry is still required, but the conflict scope is limited to the affected rows rather than the entire table. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Related Conditions

Other conditions under the `DELTA_CONCURRENT_DELETE_READ` error class that relate to read scope include:

- **WHOLE_TABLE_REPLACE**: The concurrent operation replaced all data in the table, regardless of read scope.
- **WITHOUT_HINT**: The concurrent operation deleted data that was read by this operation, with no specific hint provided.
- **PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE**: Row-level conflict detection could not be performed on a partitioned table.

## Related Concepts

- [Delta Lake Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md)
- Transaction Conflict Resolution in Delta Lake
- Delta Lake Error Classes
- [Row-Level Conflict Resolution](/concepts/row-level-conflict-resolution.md)
- [Delta Lake Read Transactions](/concepts/delta-lake-transaction-log.md)

## Sources

- delta_concurrent_delete_read-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_read-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_read-error-condition-databricks-on-aws-d0015916.md)
