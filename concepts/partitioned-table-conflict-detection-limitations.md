---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4e023a282ea7345a46cf865aba279299ef7292fa1777fc8f477ede8e9b1e2eb0
  pageDirectory: concepts
  sources:
    - delta_concurrent_append-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - partitioned-table-conflict-detection-limitations
    - PTCDL
  citations:
    - file: delta_concurrent_append-error-condition-databricks-on-aws.md
title: Partitioned Table Conflict Detection Limitations
description: A scenario in Delta Lake where row-level conflict detection cannot be performed on partitioned tables under certain conditions, requiring a retry of the operation.
tags:
  - delta-lake
  - partitioning
  - transaction-conflicts
timestamp: "2026-06-18T15:18:02.047Z"
---

Here is the wiki page for "Partitioned Table Conflict Detection Limitations", based solely on the provided source material.

---

## Partitioned Table Conflict Detection Limitations

**Partitioned Table Conflict Detection Limitations** refer to a specific error condition encountered during concurrent write operations on [Delta Lake](/concepts/delta-lake.md) tables when row-level conflict detection cannot be performed due to the table's partitioning structure.

## Error: `PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE`

This error occurs under the `DELTA_CONCURRENT_APPEND` error class with the sub-type `PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE`. The full error message is: ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

> Row-level conflict detection could not be performed on this partitioned table. Please retry the operation.

## Cause

When a concurrent operation attempts to modify a partitioned table and the transaction does not provide a merge source (or the source cannot be matched against the partition boundaries), Delta Lake cannot perform row-level conflict detection. This limitation prevents the system from identifying which specific rows were affected by a conflicting transaction. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

This error is one of several sub-types within the `DELTA_CONCURRENT_APPEND` error class, all of which signify that a transaction conflict has been detected due to a concurrent operation modifying the same table. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Affected Scenarios

The `PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE` error specifically applies when:

- A table is partitioned (for example, by date or by a category column).
- A concurrent operation (such as an `INSERT`, `UPDATE`, `MERGE`, or `DELETE`) is executed.
- The system cannot determine which rows within the partitions were modified by the concurrent transaction, making row-level resolution impossible. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Related `DELTA_CONCURRENT_APPEND` Error Sub-Types

This error is part of a broader class of transaction conflict errors, each with a specific cause:

- **`ALLOTTED_TIME_EXCEEDED`**: Row-level conflict resolution exceeded the allotted time. Retry the operation. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]
- **`CHANGE_TYPE_COLUMN`**: The table contains a column named `_change_type` which conflicts with Change Data Feed (CDC) metadata columns, preventing row-level conflict detection. Rename the column. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]
- **`PREDICATES_NEED_REWRITE`**: The filter predicates used by the transaction could not be applied for row-level conflict detection. Retry the operation. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]
- **`ROW_LEVEL_CHANGES`**: The concurrent operation modified the same rows this transaction attempted to modify. Retry the operation. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]
- **`WITH_PARTITION_HINT`**: The concurrent operation modified data in a partition that should have been read by this operation. Retry the operation. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Resolution

The recommended resolution for all `DELTA_CONCURRENT_APPEND` errors is to retry the operation. The documentation advises: ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

> Please retry the operation. Refer to `<docLink>` for more information.

For the `PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE` sub-type, the specific advice is:

> Row-level conflict detection could not be performed on this partitioned table. Please retry the operation.

Retrying the operation allows Delta Lake to re-attempt the transaction with updated information about the table state, which may resolve the conflict on subsequent attempts. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Related Concepts

- Delta Lake conflict resolution — How Delta Lake handles concurrent modifications to the same data.
- Partitioned tables in Delta Lake — How partitioning affects transaction concurrency and conflict detection.
- [Optimistic concurrency control](/concepts/delta-lake-optimistic-concurrency-control.md) — The underlying mechanism for detecting and resolving transaction conflicts.
- Delta Lake error classes — The complete list of error types and SQL states for Delta Lake operations.

## Sources

- delta_concurrent_append-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_append-error-condition-databricks-on-aws.md](/references/delta_concurrent_append-error-condition-databricks-on-aws-47a87778.md)
