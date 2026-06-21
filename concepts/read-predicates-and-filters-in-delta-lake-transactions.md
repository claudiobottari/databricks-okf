---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b9066f58959423803adf6af31870a34c56ce6ccfd7fd6b0622af76d6636e6f51
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_read-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - read-predicates-and-filters-in-delta-lake-transactions
    - Filters in Delta Lake Transactions and Read Predicates
    - RPAFIDLT
  citations:
    - file: delta_concurrent_delete_read-error-condition-databricks-on-aws.md
title: Read Predicates and Filters in Delta Lake Transactions
description: The use of filter predicates and partition hints to narrow data scope for transaction reads, enabling row-level conflict detection and preventing full-table read conflicts.
tags:
  - delta-lake
  - optimization
  - query-filtering
timestamp: "2026-06-19T18:23:56.998Z"
---

# Read Predicates and Filters in Delta Lake Transactions

**Read Predicates and Filters** are query conditions used by Delta Lake transactions to narrow the scope of data being read, enabling row-level conflict detection and reducing the likelihood of transaction conflicts. When a transaction reads an entire table without any filters, it becomes vulnerable to conflicts with concurrent write operations.

## Overview

Delta Lake implements [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) for transaction management. When multiple transactions operate on the same table concurrently, Delta Lake uses read predicates and filters to determine which rows a transaction has read. This information is critical for [Row-Level Conflict Detection](/concepts/delta-lake-row-level-conflict-detection.md), which allows Delta Lake to resolve conflicts at a finer granularity rather than aborting entire transactions. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## How Read Predicates Work

Read predicates are the filter conditions that a transaction applies to its read operations. When a transaction reads data from a Delta table, the system records which rows were accessed based on the predicates used. If a concurrent write operation modifies or deletes data that falls within the scope of those predicates, a conflict may be detected. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

The more specific the read predicates, the smaller the potential conflict window. For example, a query filtering on a specific partition or key range will only conflict with concurrent operations that modify data within that same range. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Importance of Using Filters

Transactions that read entire tables without any filters create the widest possible conflict window. Such operations can conflict with any concurrent write that modifies any part of the table. This leads to the `EMPTY_READ_PREDICATES` and `WHOLE_TABLE_READ` error conditions when a concurrent deletion or replacement operation occurs. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

The DELTA_CONCURRENT_DELETE_READ Error|DELTA_CONCURRENT_DELETE_READ error condition documentation lists several sub-conditions that arise when read predicates are missing or insufficient:

- **EMPTY_READ_PREDICATES**: The transaction did not include any filters and read the entire table, conflicting with a concurrent deletion. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]
- **WHOLE_TABLE_READ**: The transaction attempted to read the entire table, conflicting with a concurrent deletion. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]
- **WHOLE_TABLE_REPLACE**: A concurrent operation replaced all data in the table. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]
- **WITHOUT_HINT**: A concurrent operation deleted data that was read by this operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]
- **WITH_PARTITION_HINT**: A concurrent operation deleted data in a specific partition that was read by this operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Best Practices

### Add Filters to Queries

Always include specific filter conditions in your read operations to narrow the data scope. This reduces the likelihood of conflicts with concurrent write operations and improves overall transaction throughput. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### Use Partition Pruning

When working with Partitioned Tables, leverage partition columns in your filters. This allows Delta Lake to perform Partition Pruning and only read the relevant partitions, reducing the conflict window significantly. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### Handle Conflicts with Retry Logic

When a `DELTA_CONCURRENT_DELETE_READ` conflict is detected, the recommended approach is to retry the operation. In many cases, the conflict is transient and the operation will succeed on retry. The error messages include a link to documentation with more details on how to resolve each specific sub-condition. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Related Concepts

- [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) – The foundational concurrency model used by Delta Lake.
- [Row-Level Conflict Detection](/concepts/delta-lake-row-level-conflict-detection.md) – How Delta Lake resolves conflicts at the row level rather than the table level.
- [Delta Lake Transactions](/concepts/delta-acid-transactions.md) – The transactional semantics of Delta Lake operations.
- Partition Pruning – Optimization technique for narrowing read scope using partition columns.
- Change Data Feed (CDC) – Metadata that tracks row-level changes, which can conflict with `_change_type` columns.
- SQLSTATE 2D521 – The SQL state code associated with invalid transaction termination conflicts.

## Sources

- delta_concurrent_delete_read-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_read-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_read-error-condition-databricks-on-aws-d0015916.md)
