---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ab851973c8f3a3480dbf2649026a15a3d318dbb1c059a4faeead8d7509acde58
  pageDirectory: concepts
  sources:
    - delta_concurrent_append-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - whole-table-scan-conflicts-in-delta-lake
    - WTSCIDL
  citations:
    - file: delta_concurrent_append-error-condition-databricks-on-aws.md
title: Whole Table Scan Conflicts in Delta Lake
description: Transaction conflicts arising when a Delta Lake operation reads or replaces an entire table concurrently with other modifications, resolvable by narrowing query scope with filters or retrying.
tags:
  - delta-lake
  - transaction-conflicts
  - query-optimization
timestamp: "2026-06-18T15:18:07.015Z"
---

# Whole Table Scan Conflicts in Delta Lake

**Whole Table Scan Conflicts** are a specific class of [Delta Lake](/concepts/delta-lake.md) transaction conflicts that occur when a concurrent modification to a table conflicts with an operation that reads or replaces the entire table. These conflicts are reported under the `DELTA_CONCURRENT_APPEND` error condition (SQLSTATE 2D521) and manifest as two distinct sub-errors: `WHOLE_TABLE_READ` and `WHOLE_TABLE_REPLACE`.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Overview

Delta Lake uses optimistic concurrency control. When two transactions attempt to modify the same table concurrently, the second transaction to commit will fail if it cannot resolve the conflict. A whole table scan conflict arises when one transaction reads all data in the table (or replaces all data) while another transaction modifies the table in the same delta. Because Delta Lake tracks modifications at file granularity, an operation that touches every file in the table will conflict with any concurrent write that changes files.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Sub-Conditions

### WHOLE_TABLE_READ

This sub-condition occurs when a transaction attempts to read the entire table while a concurrent modification has added or changed data. The error message states: "This transaction attempted to read the entire table, conflicting with the concurrent modification. Consider adding filters to your query to narrow the data scope or retrying the operation."^[delta_concurrent_append-error-condition-databricks-on-aws.md]

**Typical scenarios:**
- A `SELECT *` or aggregation over an unpartitioned table runs concurrently with an `INSERT`, `DELETE`, or `UPDATE`.
- A table-scanning read operation (e.g., full table join) executes while another transaction modifies the table.

**Resolution:**  
- Add filter predicates (e.g., `WHERE` clauses on partition columns or indexed columns) to limit the read scope.  
- Retry the operation; the concurrent modification may have completed by then.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### WHOLE_TABLE_REPLACE

This sub-condition occurs when a concurrent operation replaces all data in the table, causing any concurrent read or write that depends on the previous table state to fail. The error message states: "The concurrent operation replaced all data in the table. Please retry the operation."^[delta_concurrent_append-error-condition-databricks-on-aws.md]

**Typical scenarios:**
- An `INSERT OVERWRITE` or `CREATE OR REPLACE TABLE` runs while another transaction tries to read or write to the same table.
- A full table deletion followed by a re-creation.

**Resolution:**  
- Retry the operation. Once the replace operation commits, subsequent transactions will see the new table state.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Comparison with Other Concurrent Conflicts

| Sub-condition | Cause | Resolution |
|---------------|-------|------------|
| `WHOLE_TABLE_READ` | Read of entire table conflicts with concurrent modification | Add filters or retry |
| `WHOLE_TABLE_REPLACE` | Concurrent operation replaced all data | Retry |
| `ROW_LEVEL_CHANGES` | Concurrent operation modified the same rows | Retry |
| `WITH_PARTITION_HINT` | Concurrent modification to a partition that should have been read | Retry |

All these sub-conditions require the operation to be retried, but adding partition filters or narrowing the read scope can prevent `WHOLE_TABLE_READ` specifically.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Best Practices to Avoid Whole Table Scan Conflicts

- **Partition tables** by a frequently filtered column (e.g., date, region) so that reads can target specific partitions instead of the whole table.^[delta_concurrent_append-error-condition-databricks-on-aws.md]
- **Use `WHERE` clauses** on read queries to limit the scan to relevant files. Delta Lake performs file-level pruning based on partition and data skipping, reducing conflict probability.^[delta_concurrent_append-error-condition-databricks-on-aws.md]
- **Avoid mixing full-table reads with concurrent writes** in high-concurrency workloads. Consider separating batch replacement jobs from interactive read queries.^[delta_concurrent_append-error-condition-databricks-on-aws.md]
- **Retry logic**: Implement exponential backoff retry in applications to handle transient conflicts.^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md)
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md)
- [Optimistic Concurrency Control in Delta Lake](/concepts/delta-lake-optimistic-concurrency-control.md)
- Partition Pruning
- DELTA_CONCURRENT_APPEND Error Condition|DELTA_CONCURRENT_APPEND error condition
- [Row-Level Conflict Detection](/concepts/delta-lake-row-level-conflict-detection.md)
- Data Skipping

## Sources

- delta_concurrent_append-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_append-error-condition-databricks-on-aws.md](/references/delta_concurrent_append-error-condition-databricks-on-aws-47a87778.md)
