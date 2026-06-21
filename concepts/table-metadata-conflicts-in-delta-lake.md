---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 41364091be059c475a2361efbd1be3331c3f977b81bacc1087e75c6753fab116
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_read-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - table-metadata-conflicts-in-delta-lake
    - TMCIDL
  citations:
    - file: delta_concurrent_delete_read-error-condition-databricks-on-aws.md
title: Table Metadata Conflicts in Delta Lake
description: Conflicts arising from concurrent schema or partitioning changes to a Delta table while a transaction is in progress, requiring transaction retry.
tags:
  - delta-lake
  - schema-evolution
  - partitioning
timestamp: "2026-06-19T18:24:04.803Z"
---

# Table Metadata Conflicts in Delta Lake

**Table metadata conflicts in Delta Lake** are a class of transaction conflicts that occur when a concurrent [Delta Lake] write operation (such as `DELETE`, `UPDATE`, or `MERGE`) modifies the table’s metadata — for example, schema, partitioning, or the [Delta protocol] version — while another transaction is reading or writing the table. These conflicts are reported under the SQLSTATE class `2D521` as part of the `DELTA_CONCURRENT_DELETE_READ` error condition. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Subtypes of Metadata-Related Conflicts

The `DELTA_CONCURRENT_DELETE_READ` error includes several subtypes that explicitly involve metadata changes or metadata-dependent conflict detection mechanisms:

### CHANGE_TYPE_COLUMN[​](#change_type_column)

The table contains a physical column named `_change_type`, which conflicts with [Change Data Feed (CDF)] metadata columns. This collision prevents Delta Lake from performing row-level conflict detection. To resolve, either rename the conflicting column or disable Change Data Feed on the table. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### PROTOCOL_CHANGE[​](#protocol_change)

A concurrent operation upgraded the [Delta table protocol]. This metadata change invalidates the current transaction’s conflict resolution assumptions. The recommended action is to retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE[​](#partitioned_table_without_merge_source)

Row-level conflict detection could not be performed on a partitioned table when the concurrent deletion occurred. This typically happens when a [MERGE] operation is applied without an explicit source that can be used for fine-grained conflict resolution. Retrying the operation may succeed. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### PREDICATES_NEED_REWRITE[​](#predicates_need_rewrite)

The filter predicates used by the current transaction could not be applied for row-level conflict detection, often because the table’s metadata (such as partitioning or schema) was altered concurrently. Retrying the operation is the recommended resolution. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### EMPTY_READ_PREDICATES / WHOLE_TABLE_READ[​](#empty_read_predicates-whole_table_read)

These two sub‑errors indicate that the transaction read the entire table without any filters (`EMPTY_READ_PREDICATES`) or attempted to read the whole table (`WHOLE_TABLE_READ`), and a concurrent deletion deleted some or all of the data. While not directly a metadata conflict, the inability to narrow the read scope often stems from the transaction’s design; adding filters can resolve the issue. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### WHOLE_TABLE_REPLACE[​](#whole_table_replacement)

A concurrent operation replaced all data in the table (for example, via an `INSERT OVERWRITE`). This is a full metadata replacement of the table’s data files. Retrying the operation is the prescribed action. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### WITHOUT_HINT / WITH_PARTITION_HINT[​](#without_hint-with_partition_hint)

These errors occur when a concurrent operation deletes data that was read by the current transaction. `WITHOUT_HINT` indicates no partition hint was used; `WITH_PARTITION_HINT` specifies the exact partition (for example, `partitionValues`) where the concurrent deletion happened. Both require a retry. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### ALLOTTED_TIME_EXCEEDED[​](#allotted_time_exceeded)

Row-level conflict resolution exceeded the allotted time. This can happen when metadata‑based resolution logic takes too long. The solution is to retry the operation. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

### ROW_LEVEL_CHANGES[​](#row_level_changes)

A concurrent operation deleted specific rows that the current transaction attempted to read. Row-level conflict detection flagged the change; retrying is recommended. ^[delta_concurrent_delete_read-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md)
- Concurrent Write Conflicts
- [Change Data Feed (CDF)](/concepts/delta-change-data-feed-cdf.md)
- Delta Protocol
- SQLSTATE 2D521
- Table Metadata Changes

## Sources

- delta_concurrent_delete_read-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_read-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_read-error-condition-databricks-on-aws-d0015916.md)
