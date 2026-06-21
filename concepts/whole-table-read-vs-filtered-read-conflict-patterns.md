---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6e742668d8aabe7596408ea14ba8dc5fe7993616d915c059fac14daaf66ca3b9
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_read-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - whole-table-read-vs-filtered-read-conflict-patterns
    - WRVFRCP
  citations:
    - file: delta_concurrent_delete_read-error-condition-databricks-on-aws.md
title: Whole-Table Read vs Filtered Read Conflict Patterns
description: A class of Delta Lake transaction conflicts arising when a transaction reads an entire table (without filters) concurrently with a delete operation, resolvable by adding query filters to narrow the data scope.
tags:
  - delta-lake
  - query-optimization
  - transactions
timestamp: "2026-06-18T15:18:33.701Z"
---

# Whole-Table Read vs Filtered Read Conflict Patterns

**Whole-Table Read vs Filtered Read Conflict Patterns** describe a class of [Delta Lake](/concepts/delta-lake.md) transaction conflicts that occur when a concurrent operation deletes data from a table while another transaction reads from that same table. The Delta Lake conflict detection engine treats whole-table reads and filtered reads differently, producing distinct error sub-conditions depending on whether the reading transaction scoped its access with filters or scanned the entire table. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Conflict Overview

The DELTA_CONCURRENT_DELETE_READ Error Class|DELTA_CONCURRENT_DELETE_READ error class (SQLSTATE 2D521) signals a transaction conflict where a concurrent operation deleted data that the current transaction had already read or was in the process of reading. The conflict resolution system attempts row-level conflict detection, but if that fails or is inadequate, it returns one of several sub-conditions. Two of the most important sub-conditions distinguish whole-table scans from filtered reads. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Whole-Table Read Sub-Conditions

### WHOLE\_TABLE\_READ

The `WHOLE_TABLE_READ` sub-condition fires when the current transaction read the entire table (i.e., performed a full scan without any predicates) and a concurrent deletion operation committed data changes. The error message states: "This transaction attempted to read the entire table, conflicting with the concurrent deletion. Add filters to your query to narrow the data scope and retry the operation." ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

This pattern is the canonical **whole-table read conflict**. Because the reading transaction had no filter, row-level conflict detection cannot determine which specific rows were read, so any concurrent deletion triggers the conflict. The recommended remediation is to add filters to the query so that conflict detection can operate on a narrower data scope. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### EMPTY\_READ\_PREDICATES

The `EMPTY_READ_PREDICATES` sub-condition is closely related: "This transaction did not include any filters and read the entire table, conflicting with the concurrent deletion. Add filters to your query to narrow the data scope and retry the operation." This essentially mirrors `WHOLE_TABLE_READ` but also notes that the concurrent operation may have changed table metadata (e.g., schema or partitioning). In that case, simply retrying without changes may suffice. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Filtered Read Sub-Conditions

When a transaction provides filter predicates, Delta Lake attempts row-level conflict detection. Several sub-conditions can arise:

### PREDICATES\_NEED\_REWRITE

If the filter predicates used by the transaction cannot be applied for row-level conflict detection (e.g., because they are too complex or reference columns that have changed), the engine returns `PREDICATES_NEED_REWRITE`. The user should retry the operation, and the engine may automatically rewrite the predicates on retry. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### ROW\_LEVEL\_CHANGES

When row-level conflict detection succeeds and identifies that the concurrent deletion actually removed rows that the transaction read, the `ROW_LEVEL_CHANGES` sub-condition is raised. This is a genuine conflict: the read data has been deleted. The recommended action is to retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### WITH\_PARTITION\_HINT

If the concurrent operation deleted data in a specific partition that the reading transaction accessed (e.g., via a partition hint), the conflict is reported as `WITH_PARTITION_HINT`. The error includes the partition values involved. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### WITHOUT\_HINT

If no explicit partition hint was used but a concurrent deletion still conflicts, the `WITHOUT_HINT` sub-condition is returned. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### ALLOTTED\_TIME\_EXCEEDED

Row-level conflict resolution itself can exceed the allotted time, resulting in `ALLOTTED_TIME_EXCEEDED`. This is a timeout of the conflict detection mechanism, not a direct data conflict. Retrying is advised. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Implications for Design

The distinction between whole-table and filtered reads has significant operational consequences:

- **Whole-table reads** force Delta Lake to raise a conflict on *any* concurrent deletion, regardless of which rows were actually deleted. To reduce false conflicts, queries should always include filters (e.g., a `WHERE` clause) that scope the data being read. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]
- **Filtered reads** enable row-level conflict detection, which can avoid conflicts when concurrent deletions touch entirely different rows than those being read. However, complex or non-rewritable predicates may still escalate to a full conflict. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]
- Partitioned tables require special attention: when the merge source is not properly aligned, row-level conflict detection may not be possible (`PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE`), leading to a forced retry. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Related Concepts

- Delta Lake transaction conflicts
- Serializable isolation in Delta Lake
- [MERGE and row-level conflict detection](/concepts/delta-lake-row-level-conflict-detection.md)
- [Change Data Feed metadata columns](/concepts/change-data-feed-cdf-metadata-conflicts.md)
- Partition pruning and conflict resolution
- DDL operations and table protocol changes

## Sources

- delta_concurrent_delete_read-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_read-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_read-error-condition-databricks-on-aws-d0015916.md)
