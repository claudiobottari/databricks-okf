---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1c385b78362b6edc6e114578a2625f38f4783b198836e69ca7bf444878eeb902
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_read-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-sqlstate-2d521
    - DLS2
  citations:
    - file: delta_concurrent_delete_read-error-condition-databricks-on-aws.md
title: Delta Lake SQLSTATE 2D521
description: The SQL state code (2D521) indicating an invalid transaction termination due to a transaction conflict in Delta Lake.
tags:
  - databricks
  - sqlstate
  - error-codes
timestamp: "2026-06-19T18:24:11.603Z"
---

Here is the wiki page for "Delta Lake SQLSTATE 2D521".

---

## Delta Lake SQLSTATE 2D521

**SQLSTATE 2D521** is an error condition in [Delta Lake](/concepts/delta-lake.md) that signals an invalid transaction termination. It is raised when a transaction conflict is detected during a concurrent read and write operation. The error class is "DELTA_CONCURRENT_DELETE_READ". ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### Overview

The `2D521` SQL state code indicates a transaction conflict: a concurrent operation (such as a `DELETE`) deleted data from a table that the current transaction attempted to read. The table and the version at which the deletion occurred are included in the error message. The exact cause of the conflict can be one of several sub-conditions, each providing a specific reason for why row-level conflict detection could not proceed. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### Common Sub-Conditions

The error message includes a sub‑condition that identifies why the conflict occurred. Below are the most common sub‑conditions:

*   **ALLOTTED\_TIME\_EXCEEDED** – Row-level conflict resolution exceeded the allotted time. Retrying the operation is recommended. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]
*   **EMPTY\_READ\_PREDICATES** – The transaction did not include any filters and read the entire table, conflicting with the concurrent deletion. Adding filters to narrow the data scope and retrying is recommended. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]
*   **PARTITIONED\_TABLE\_WITHOUT\_MERGE\_SOURCE** – Row-level conflict detection could not be performed on a partitioned table. Retrying the operation is recommended. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]
*   **WHOLE\_TABLE\_READ** – The transaction attempted to read the entire table, conflicting with the concurrent deletion. Adding filters to narrow the data scope and retrying is recommended. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]
*   **WHOLE\_TABLE\_REPLACE** – The concurrent operation replaced all data in the table. Retrying the operation is recommended. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]
*   **ROW\_LEVEL\_CHANGES** – The concurrent operation deleted rows that this transaction attempted to read. Retrying the operation is recommended. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### Resolution Strategies

Most sub‑conditions recommend retrying the operation. For `EMPTY_READ_PREDICATES` and `WHOLE_TABLE_READ`, adding filters to the query to narrow the data scope is advised before retrying. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### Related Concepts

- [Delta Lake](/concepts/delta-lake.md)
- [Concurrent write operations](/concepts/concurrent-copy-into-invocations.md)
- Transaction isolation
- [Optimistic concurrency control](/concepts/delta-lake-optimistic-concurrency-control.md)

### Sources

- delta_concurrent_delete_read-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_read-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_read-error-condition-databricks-on-aws-d0015916.md)
