---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 676e7ab1749ab56423a46fe66c82b20f4bd98b54723bdc5bfb5124c09208feb4
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - table-wide-vs-filtered-delta-operations
    - TVFDO
  citations:
    - file: delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
title: Table-wide vs filtered Delta operations
description: A category of transaction conflicts caused by operations that modify an entire table (no filter predicates) rather than a subset of data, including WHOLE_TABLE_READ, WHOLE_TABLE_REPLACE, and EMPTY_READ_PREDICATES sub-errors.
tags:
  - delta-lake
  - concurrency
  - query-optimization
timestamp: "2026-06-19T10:03:56.529Z"
---

# Table-wide vs Filtered Delta Operations

**Table-wide vs Filtered Delta Operations** refers to the distinction between Delta Lake transactions that operate on an entire table versus those that target a specific subset of rows using filter predicates. This distinction is critical for understanding [Delta Lake concurrency control](/concepts/delta-lake-optimistic-concurrency-control.md) and avoiding transaction conflicts in concurrent workloads.

## Overview

Delta Lake uses [optimistic concurrency control](/concepts/delta-lake-optimistic-concurrency-control.md) to manage concurrent reads and writes. When multiple transactions attempt to modify the same table simultaneously, Delta Lake detects conflicts and may fail one of the transactions. The scope of an operation — whether it targets the whole table or a filtered subset — directly affects how conflicts are detected and resolved. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Table-Wide Operations

A **table-wide operation** is a transaction that modifies the entire table without applying any filter predicates. These operations are more likely to conflict with concurrent modifications because they affect all data in the table. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### Conflict Scenarios

When a transaction attempts to modify the entire table and a concurrent operation has already modified the table, Delta Lake may raise the following error conditions:

- **WHOLE_TABLE_READ**: The transaction attempted to modify the entire table, conflicting with a concurrent modification. The recommended resolution is to add filters to narrow the data scope and retry the operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]
- **WHOLE_TABLE_REPLACE**: A concurrent operation replaced all data in the table. The recommended resolution is to retry the operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]
- **EMPTY_READ_PREDICATES**: The transaction did not include any filters and modified the entire table, conflicting with a concurrent modification. The recommended resolution is to add filters to narrow the data scope and retry the operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Filtered Operations

A **filtered operation** is a transaction that uses filter predicates (such as `WHERE` clauses) to target a specific subset of rows. Filtered operations reduce the likelihood of conflicts because they only affect a portion of the table, allowing concurrent transactions to operate on non-overlapping data. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### Conflict Scenarios

Even with filters, conflicts can still occur. Delta Lake may raise the following error conditions for filtered operations:

- **WITH_PARTITION_HINT**: A concurrent operation deleted data in a specific partition that was read by this operation. The recommended resolution is to retry the operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]
- **WITHOUT_HINT**: A concurrent operation deleted data that was read by this operation. The recommended resolution is to retry the operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]
- **ROW_LEVEL_CHANGES**: A concurrent operation modified the same rows that this transaction attempted to modify. The recommended resolution is to retry the operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Best Practices

### Use Filter Predicates

To minimize conflicts, always include filter predicates in your write operations. Narrowing the data scope reduces the chance of overlapping with concurrent modifications. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### Handle Conflicts Gracefully

When a conflict is detected, Delta Lake provides specific error conditions that indicate the nature of the conflict. The general recommendation is to retry the operation, as conflicts are often transient. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### Avoid Table-Wide Modifications in Concurrent Workloads

If multiple writers are operating on the same table simultaneously, avoid table-wide operations that modify all data. Instead, use filtered operations that target specific partitions or row ranges. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Related Error Conditions

The following error conditions are specifically related to the table-wide vs filtered distinction:

| Error Condition | Description | Resolution |
|----------------|-------------|------------|
| `WHOLE_TABLE_READ` | Transaction attempted to modify the entire table | Add filters and retry |
| `WHOLE_TABLE_REPLACE` | Concurrent operation replaced all data | Retry the operation |
| `EMPTY_READ_PREDICATES` | No filters used, entire table modified | Add filters and retry |
| `WITH_PARTITION_HINT` | Concurrent operation deleted data in a partition | Retry the operation |
| `WITHOUT_HINT` | Concurrent operation deleted read data | Retry the operation |
| `ROW_LEVEL_CHANGES` | Concurrent operation modified same rows | Retry the operation |

^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) — How Delta Lake manages concurrent transactions
- [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) — The underlying concurrency model
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — The mechanism for tracking changes
- Partition Pruning — Using partitions to narrow operation scope
- [Delta Lake Error Conditions](/concepts/delta-error-sub-conditions.md) — Complete list of Delta Lake error conditions

## Sources

- delta_concurrent_delete_delete-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_delete-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_delete-error-condition-databricks-on-aws-6fcec7a7.md)
