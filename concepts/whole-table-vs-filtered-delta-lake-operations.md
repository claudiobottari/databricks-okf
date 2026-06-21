---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c929e7cf71d355813e256f471a61cf1ca1afc5069aaf81f1b3acb935f7fb1e99
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - whole-table-vs-filtered-delta-lake-operations
    - WVFDLO
  citations:
    - file: delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
title: Whole-Table vs Filtered Delta Lake Operations
description: Conflict patterns arising when one transaction modifies an entire table (no filters, full replace) while another attempts concurrent modifications, requiring narrowing data scope via filters.
tags:
  - delta-lake
  - concurrency
  - optimization
timestamp: "2026-06-19T18:23:49.821Z"
---

# Whole-Table vs Filtered Delta Lake Operations

**Whole-Table vs Filtered Delta Lake Operations** refers to the distinction between Delta Lake transactions that operate on an entire table versus those that apply filters to scope operations to a subset of data. This distinction is critical for understanding and avoiding transaction conflicts in concurrent write environments.

## Overview

Delta Lake supports concurrent read and write operations, but conflicts can arise when multiple transactions modify the same data simultaneously. The type of operation — whether it targets the whole table or a filtered subset — directly impacts how Delta Lake detects and resolves these conflicts. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Whole-Table Operations

**Whole-table operations** are transactions that modify or read all data in a table without applying any filters. These operations are particularly prone to conflicts in concurrent environments.

### Characteristics

- No filter predicates are applied to scope the operation to specific rows or partitions.
- The transaction interacts with the entire table dataset.
- Includes operations like full table scans, complete table replacements, and unqualified DML statements.

### Conflict Scenarios

When a transaction performs a whole-table modification, it conflicts with any concurrent operation that also modifies the table. Delta Lake raises specific error conditions for these scenarios:

- **WHOLE_TABLE_READ**: Occurs when a transaction attempts to modify the entire table, conflicting with a concurrent modification. The recommended resolution is to "add filters to your query to narrow the data scope and retry the operation." ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

- **WHOLE_TABLE_REPLACE**: Raised when a concurrent operation has replaced all data in the table while another transaction was in progress. The recommended action is to "retry the operation." ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

- **EMPTY_READ_PREDICATES**: Occurs when a transaction "did not include any filters and modified the entire table, conflicting with the concurrent modification." The resolution is to "add filters to your query to narrow the data scope and retry the operation." ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### Error Condition Details

| Error Condition | Situation | Recommended Action |
|----------------|-----------|-------------------|
| `WHOLE_TABLE_READ` | Transaction attempted whole-table modification conflicting with concurrent modification | Add filters to narrow data scope |
| `WHOLE_TABLE_REPLACE` | Concurrent operation replaced all table data | Retry the operation |
| `EMPTY_READ_PREDICATES` | No filters applied, entire table modified | Add filters to narrow data scope |

^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Filtered (Scoped) Operations

**Filtered operations** apply predicates to scope transactions to specific rows or partitions, reducing the likelihood of conflicts with concurrent operations.

### Benefits

- **Reduced conflict surface**: By targeting only relevant data, filtered operations minimize the chance of interfering with other concurrent transactions.
- **Improved concurrency**: Multiple filtered operations can run simultaneously if they target non-overlapping data.
- **Row-level conflict resolution**: Delta Lake can perform row-level conflict detection when filter predicates are provided, enabling more granular conflict resolution.

### Best Practices

- Always include filter predicates in UPDATE, DELETE, and MERGE operations when possible.
- Use partition-aware filters to scope operations to specific partitions.
- For operations that genuinely need to affect all data, consider serializing access to avoid conflicts.

## Conflict Resolution with Filters

When filtered operations encounter conflicts, Delta Lake provides several error conditions specific to filtered scenarios:

- **WITH_PARTITION_HINT**: The concurrent operation deleted data in a specific partition that was read by this operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

- **WITHOUT_HINT**: The concurrent operation deleted data that was read by this operation, without a partition hint being available. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

- **ROW_LEVEL_CHANGES**: The concurrent operation modified the same rows that this transaction attempted to modify. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

- **PREDICATES_NEED_REWRITE**: The filter predicates used could not be applied for row-level conflict detection. The recommended action is to retry the operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### Partitioned Tables

For partitioned tables, special considerations apply:

- **PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE**: "Row-level conflict detection could not be performed on this partitioned table." The resolution is to retry the operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

- Delta Lake can use partition pruning to improve conflict detection when filters align with partition boundaries.

## Practical Guidelines

### When to Use Whole-Table Operations

- During initial data loads or table replacements
- When performing schema changes that require full table rewrites
- In single-writer environments where concurrency is not a concern

### When to Use Filtered Operations

- For incremental updates, deletes, or merges in concurrent environments
- When targeting specific date ranges, categories, or other identifiable subsets
- In multi-writer scenarios common in production pipelines

### Error Recovery

When encountering whole-table or filtered operation conflicts:

1. **Identify the conflict type** from the error condition
2. **For whole-table conflicts**: Add filter predicates to scope the operation, or serialize access patterns
3. **For filtered conflicts**: Retry the operation (Delta Lake's optimistic concurrency control will resolve once the conflicting transaction completes)
4. **Consider table-level settings**: Configure appropriate Delta Lake isolation levels and retry logic

## Related Concepts

- Delta Lake Transaction Conflicts — General overview of concurrent access conflicts
- Delta Lake Isolation Levels — Configurable isolation guarantees
- [Delta Lake MERGE Operation](/concepts/delta-lake-dml-operations.md) — A common filtered operation pattern
- [Delta Lake Partitioning](/concepts/delta-lake-partitioning-constraints.md) — How partitioning affects conflict detection
- [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) — The underlying concurrency mechanism in Delta Lake
- [Delta Lake Protocol Changes](/concepts/delta-lake-table-protocol-changes.md) — How protocol upgrades interact with concurrent operations

## Sources

- delta_concurrent_delete_delete-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_delete-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_delete-error-condition-databricks-on-aws-6fcec7a7.md)
