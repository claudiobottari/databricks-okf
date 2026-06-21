---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6555c1c27829fd26607e95131cefb2c2f85583944374012785cea102635c0741
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_concurrent_delete_delete-error-class
    - DEC
    - DELTA_CONCURRENT_DELETE_DELETE
    - DELTA_CONCURRENT_DELETE_DELETE Error
    - DELTA_CONCURRENT_DELETE_DELETE Error Class
    - DELTA_CONCURRENT_DELETE_DELETE error class
    - DELTA_CONCURRENT_DELETE_DELETE error condition
    - delta_concurrent_delete_delete_error_class
  citations:
    - file: delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
title: DELTA_CONCURRENT_DELETE_DELETE Error Class
description: A Databricks error class for transaction conflicts where a concurrent delete operation conflicts with another delete on the same Delta table.
tags:
  - databricks
  - delta-lake
  - error-handling
  - concurrency
timestamp: "2026-06-19T18:23:14.515Z"
---

```markdown
---
title: DELTA_CONCURRENT_DELETE_DELETE Error Class
summary: A Delta Lake error class indicating a transaction conflict where a concurrent operation deleted data that the current transaction was attempting to delete.
sources:
  - delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:52:14.597Z"
updatedAt: "2026-06-19T15:02:57.021Z"
tags:
  - delta-lake
  - error-handling
  - concurrency
aliases:
  - delta_concurrent_delete_delete-error-class
  - DEC
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# DELTA_CONCURRENT_DELETE_DELETE Error Class

**SQLSTATE: 2D521** (Invalid Transaction Termination)

The `DELTA_CONCURRENT_DELETE_DELETE` error class occurs when a Delta Lake transaction encounters a conflict because a concurrent operation has deleted data from the same table that the current transaction is attempting to delete. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Error Message

The standard error message follows this format:

```
Transaction conflict detected, a concurrent <operation> deleted data from table <tableName> (committed at version <version>) that this transaction attempted to delete.
```

^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Sub-Error Conditions

### ALLOTTED_TIME_EXCEEDED

Row-level conflict resolution exceeded the allotted time. Retry the operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### CHANGE_TYPE_COLUMN

The table contains a column named `_change_type` which conflicts with [[Delta Change Data Feed (CDF)|Change Data Feed]] (CDC) metadata columns, preventing row-level conflict detection. Rename this column or disable CDC. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### EMPTY_READ_PREDICATES

This transaction did not include any filters and modified the entire table, conflicting with the concurrent modification. Add filters to narrow the data scope and retry the operation. Separately, the concurrent operation may have changed the table metadata (for example, schema or partitioning) – retry the operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE

Row-level conflict detection could not be performed on this partitioned table. Retry the operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### PREDICATES_NEED_REWRITE

The filter predicates used by this transaction could not be applied for row-level conflict detection. Retry the operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### PROTOCOL_CHANGE

The concurrent operation upgraded the table protocol. Retry the operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### ROW_LEVEL_CHANGES

The concurrent operation modified the same rows that this transaction attempted to modify. Retry the operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### WHOLE_TABLE_READ

This transaction attempted to modify the entire table, conflicting with the concurrent modification. Add filters to narrow the data scope and retry the operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### WHOLE_TABLE_REPLACE

The concurrent operation replaced all data in the table. Retry the operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### WITHOUT_HINT

The concurrent operation deleted data that was read by this operation. Retry the operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### WITH_PARTITION_HINT

The concurrent operation deleted data in the partition `<partitionValues>` that was read by this operation. Retry the operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Related Concepts

- [[Delta Lake]] – The lakehouse storage layer where this conflict occurs.
- [[Delta Change Data Feed (CDF)|Change Data Feed]] – A feature that can conflict with row-level detection when a `_change_type` column exists.
- [[Delta Lake Optimistic Concurrency Control|Delta Lake Concurrency Control]] – The underlying mechanism that detects transaction conflicts.
- SQLSTATE – Standard SQL state code for error classification.

## Sources

- delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
```

# Citations

1. [delta_concurrent_delete_delete-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_delete-error-condition-databricks-on-aws-6fcec7a7.md)
