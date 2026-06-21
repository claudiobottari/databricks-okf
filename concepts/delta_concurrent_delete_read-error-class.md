---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b7fdd1ed2bebfe09e0afdd297691b6923ccab6180c1db4b6c07a59ae52b93c96
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_read-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_concurrent_delete_read-error-class
    - DEC
    - Concurrent delete read error class
    - DELTA_CONCURRENT_DELETE_READ error class
    - DELTA_CONCURRENT_DELETE_READ - WHOLE_TABLE_REPLACE
  citations:
    - file: delta_concurrent_delete_read-error-condition-databricks-on-aws.md
title: DELTA_CONCURRENT_DELETE_READ Error Class
description: A Delta Lake transaction conflict error that occurs when a concurrent operation deletes data that another transaction has read, with multiple sub-types describing specific conflict scenarios.
tags:
  - delta-lake
  - error-handling
  - transactions
timestamp: "2026-06-18T15:18:30.321Z"
---

# DELTA_CONCURRENT_DELETE_READ Error Class

The **DELTA_CONCURRENT_DELETE_READ** error class occurs in [Delta Lake](/concepts/delta-lake.md) when a transaction conflict is detected: a concurrent operation deleted data from a table that the current transaction had already read. The error has SQLSTATE 2D521 and indicates an Invalid Transaction Termination. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Error Message

The base error message is:

```
Transaction conflict detected, a concurrent <operation> deleted data from table <tableName> (committed at version <version>) that this transaction read.
```

^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Sub-Error Conditions

### ALLOTTED_TIME_EXCEEDED

Row-level conflict resolution exceeded the allotted time. Retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### CHANGE_TYPE_COLUMN

The table contains a column named `_change_type`, which conflicts with Change Data Feed (CDC) metadata columns and prevents row-level conflict detection. Rename this column or disable CDC. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### EMPTY_READ_PREDICATES

The transaction did not include any filters and read the entire table, conflicting with a concurrent deletion. Add filters to narrow the data scope and retry. This sub-error can also occur when the concurrent operation changed table metadata (e.g., schema or partitioning). ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE

Row-level conflict detection could not be performed on a partitioned table. Retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### PREDICATES_NEED_REWRITE

The filter predicates used by this transaction could not be applied for row-level conflict detection. Retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### PROTOCOL_CHANGE

A concurrent operation upgraded the table protocol. Retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### ROW_LEVEL_CHANGES

A concurrent operation deleted rows that this transaction attempted to read. Retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### WHOLE_TABLE_READ

This transaction attempted to read the entire table, conflicting with a concurrent deletion. Add filters to narrow the data scope and retry. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### WHOLE_TABLE_REPLACE

A concurrent operation replaced all data in the table. Retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### WITHOUT_HINT

A concurrent operation deleted data that was read by this operation. Retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### WITH_PARTITION_HINT

A concurrent operation deleted data in a specific partition (`<partitionValues>`) that was read by this operation. Retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Common Causes

This error class typically arises in environments with high-concurrency workloads where multiple operations attempt to read from and delete from the same table simultaneously. Common scenarios include:

- Running concurrent DELETE and SELECT/UPDATE/MERGE operations on the same table.
- Long-running read transactions that conflict with deletions performed by other processes.
- Missing filter predicates that cause full table scans, increasing conflict zones.

## Recommended Remediation

The primary remediation strategy is to **retry the operation**, as many of the sub-error conditions are transient and may resolve on subsequent attempts. Additional strategies include:

- **Add filter predicates** to queries to narrow the data scope, reducing the likelihood of conflict (applies to EMPTY_READ_PREDICATES, WHOLE_TABLE_READ).
- **Rename conflicting columns** if a column named `_change_type` exists and CDC is enabled (applies to CHANGE_TYPE_COLUMN).
- **Optimize partitioning** to enable row-level conflict detection (applies to PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE).

## Related Concepts

- [Delta Lake Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) – How Delta Lake manages concurrent read and write operations.
- [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) – The underlying concurrency model used by Delta Lake.
- Change Data Feed (CDC) – A feature that can conflict with row-level conflict detection.
- Invalid Transaction Termination – SQLSTATE class for transaction termination errors.

## Sources

- delta_concurrent_delete_read-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_read-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_read-error-condition-databricks-on-aws-d0015916.md)
