---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d0b310952b23e666b8552d8246fcbee8265d702367ca6c0338c36e4446bd74d1
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_read-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-transaction-protocol-changes
    - DLTPC
    - Delta Lake Transaction Protocol
    - Delta Lake transaction protocol
    - Delta Transaction Log Protocol
  citations:
    - file: delta_concurrent_delete_read-error-condition-databricks-on-aws.md
title: Delta Lake Transaction Protocol Changes
description: A conflict scenario where a concurrent operation upgrades the table protocol, which can invalidate ongoing transactions and require retries.
tags:
  - delta-lake
  - protocol
  - versioning
timestamp: "2026-06-19T18:23:56.133Z"
---

# Delta Lake Transaction Protocol Changes

**Delta Lake Transaction Protocol Changes** refer to modifications made to the underlying table protocol during concurrent operations on [Delta Lake](/concepts/delta-lake.md) tables. These changes can cause transaction conflicts that result in error conditions, particularly when a concurrent operation upgrades the table protocol while another transaction is in progress.

## Overview

The [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) maintains the protocol version of a table, which defines the capabilities and features available for that table. When a concurrent operation upgrades the table protocol (for example, by adding new features or changing metadata), any in-progress transactions may encounter conflicts. The Delta Lake transaction protocol handles these conflicts through various error conditions and resolution mechanisms. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Protocol Change Error Condition

The `PROTOCOL_CHANGE` error condition occurs when a concurrent operation upgrades the table protocol during an active transaction. This is one of several transaction conflict errors classified under SQLSTATE class `2D521` (invalid transaction termination). ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### Error Message

When a protocol change conflict is detected, the system returns:

```
Transaction conflict detected, a concurrent <operation> deleted data from table <tableName> (committed at version <version>) that this transaction read.
```

With the specific sub-error:

```
The concurrent operation upgraded the table protocol. Please retry the operation.
```

^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Related Conflict Conditions

Protocol changes are one category of transaction conflicts in [Delta Lake](/concepts/delta-lake.md). Other related conflict conditions include:

- **ROW_LEVEL_CHANGES**: The concurrent operation deleted rows that this transaction attempted to read. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]
- **WHOLE_TABLE_REPLACE**: The concurrent operation replaced all data in the table. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]
- **EMPTY_READ_PREDICATES**: The transaction did not include any filters and read the entire table. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]
- **ALLOTTED_TIME_EXCEEDED**: Row-level conflict resolution exceeded the allotted time. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Row-Level Conflict Detection Considerations

Row-level conflict detection may be affected by protocol or metadata changes. The following sub-errors relate to detection limitations:

- **CHANGE_TYPE_COLUMN**: The table contains a column named `_change_type` which conflicts with Change Data Feed (CDC) metadata columns. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]
- **PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE**: Row-level conflict detection could not be performed on this partitioned table. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]
- **PREDICATES_NEED_REWRITE**: Filter predicates could not be applied for row-level conflict detection. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]
- **WITHOUT_HINT**: The concurrent operation deleted data that was read by this operation without partition hints. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]
- **WITH_PARTITION_HINT**: The concurrent operation deleted data in a specific partition that was read by this operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Resolution

The recommended resolution for protocol change conflicts is to **retry the operation**. In most cases, retrying allows the transaction to run against the updated protocol version. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### Best Practices

1. **Add filters** to narrow the data scope and reduce the likelihood of conflicts. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]
2. **Retry operations** when protocol changes are detected, as the update is typically a one-time change. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]
3. **Avoid concurrent protocol upgrades** when possible to minimize conflicts during active workloads.

## Related Concepts

- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) — The ordered record of all changes to a Delta table.
- [Delta Lake Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) — How Delta Lake handles concurrent reads and writes.
- Change Data Feed (CDC) — Captures row-level changes for data synchronization.
- [Delta Lake Protocol Versioning](/concepts/delta-lake-table-protocol-changes.md) — How protocol versions track feature availability.
- Databricks SQL States — Error classification system for SQL operations.

## Sources

- delta_concurrent_delete_read-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_read-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_read-error-condition-databricks-on-aws-d0015916.md)
