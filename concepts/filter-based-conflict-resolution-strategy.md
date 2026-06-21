---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b8cfb6c4cc36ec02f51cfb103532dfd1d10c8be7aae84c23d00d06521c442372
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - filter-based-conflict-resolution-strategy
    - FCRS
  citations:
    - file: delta-concurrent-delete-delete-error-condition-databricks-on-aws.md
title: Filter-Based Conflict Resolution Strategy
description: The recommended approach to resolve certain Delta Lake concurrent delete conflicts by adding filter predicates to narrow the data scope of operations, reducing the chance of whole-table conflicts and enabling row-level detection.
tags:
  - delta-lake
  - concurrency
  - best-practices
timestamp: "2026-06-18T11:52:17.286Z"
---

# Filter-Based Conflict Resolution Strategy

**Filter-Based Conflict Resolution** is a strategy used in [Delta Lake](/concepts/delta-lake.md) to handle concurrent write operations by applying predicate-based filtering to detect and resolve transaction conflicts at the row level. When multiple operations attempt to modify the same data simultaneously, the system can detect conflicts using filter predicates and determine the appropriate resolution approach.

## Overview

Filter-based conflict resolution operates by evaluating the predicates (filters) specified in write operations against concurrent modifications. When a transaction includes filter conditions that narrow the scope of data being modified, the system can identify which specific rows or partitions are affected by conflicting operations and determine the appropriate resolution action. ^[delta-concurrent-delete-delete-error-condition-databricks-on-aws.md]

### How It Works

The conflict detection mechanism compares the filter predicates of the current transaction against concurrent operations that have already been committed. If the filters overlap with data that was modified by another transaction, the system identifies a conflict and provides specific error guidance. ^[delta-concurrent-delete-delete-error-condition-databricks-on-aws.md]

## Conflict Scenarios

### Empty Read Predicates

When a transaction does not include any filters and attempts to modify the entire table, it conflicts with any concurrent modification. The solution is to add filters to narrow the data scope and retry the operation. ^[delta-concurrent-delete-delete-error-condition-databricks-on-aws.md]

### Whole Table Read

This occurs when a transaction attempts to modify the entire table without row-level filtering, conflicting with the concurrent modification. Add filters to your query and retry. ^[delta-concurrent-delete-delete-error-condition-databricks-on-aws.md]

### Whole Table Replace

This conflict happens when a concurrent operation replaces all data in the table. The system recommends retrying the operation. ^[delta-concurrent-delete-delete-error-condition-databricks-on-aws.md]

### Partitioned Table Without Merge Source

Row-level conflict detection cannot be performed on partitioned tables that lack a merge source. The recommended action is to retry the operation. ^[delta-concurrent-delete-delete-error-condition-databricks-on-aws.md]

## Conflict Resolution Outcomes

### Row-Level Changes

When a concurrent operation modifies the same rows that a transaction attempts to modify, the system detects row-level changes and requires retrying the operation. ^[delta-concurrent-delete-delete-error-condition-databricks-on-aws.md]

### Predicates Need Rewrite

If the filter predicates used by a transaction cannot be applied for row-level conflict detection, the system indicates that these predicates need to be rewritten. Retry the operation. ^[delta-concurrent-delete-delete-error-condition-databricks-on-aws.md]

### Without Hint

When a concurrent operation deletes data that was read by the current operation without using partition hints, the conflict is resolved by retrying the operation. ^[delta-concurrent-delete-delete-error-condition-databricks-on-aws.md]

### With Partition Hint

When a concurrent operation deletes data in specific partitions that were read by the current operation with partition hints, the conflict requires retrying the operation. ^[delta-concurrent-delete-delete-error-condition-databricks-on-aws.md]

## Conflict Detection Mechanisms

### Row-Level Conflict Detection

The system uses row-level conflict detection to identify when two concurrent operations modify identical rows. This detection mechanism requires sufficient filtering to narrow the scope of affected data. ^[delta-concurrent-delete-delete-error-condition-databricks-on-aws.md]

### Allotted Time Exceeded

If row-level conflict resolution exceeds the allotted time, the operation is considered a timeout and requires retrying. ^[delta-concurrent-delete-delete-error-condition-databricks-on-aws.md]

### Change Type Column Conflict

Tables containing a column named `_change_type` conflict with Change Data Feed (CDC) metadata columns, preventing proper row-level conflict detection. The recommended solution is to rename the column or disable CDC. ^[delta-concurrent-delete-delete-error-condition-databricks-on-aws.md]

## Best Practices

To minimize filter-based conflicts:

1. **Always include filters** in write operations to narrow the data scope
2. **Use partition hints** when working with partitioned tables to enable partition-level conflict detection
3. **Retry operations** when conflicts are detected, as the system allows subsequent attempts to succeed
4. **Monitor conflict frequency** to identify patterns in concurrent write operations

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer that provides ACID transactions
- Concurrent Operations — Multiple simultaneous write operations
- Transaction Conflict — When concurrent operations cannot be serialized
- [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) — The approach used by Delta Lake for conflict resolution
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) — CDC mechanisms that track row-level changes

## Sources

- delta-concurrent-delete-delete-error-condition-databricks-on-aws.md

# Citations

1. delta-concurrent-delete-delete-error-condition-databricks-on-aws.md
