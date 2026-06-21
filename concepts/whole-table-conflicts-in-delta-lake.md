---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9cc2f88e307a1e0e977ec41cfc6faefadf52a9c4cc3ed12bbbdb1b08108fb32e
  pageDirectory: concepts
  sources:
    - delta_concurrent_append-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - whole-table-conflicts-in-delta-lake
    - WCIDL
  citations:
    - file: delta_concurrent_append-error-condition-databricks-on-aws.md
title: Whole-Table Conflicts in Delta Lake
description: Transaction conflicts that arise when an operation attempts to read or replace an entire table while a concurrent modification is in progress.
tags:
  - delta-lake
  - concurrency
  - transactions
timestamp: "2026-06-19T15:02:52.588Z"
---

Here is the wiki page for "Whole-Table Conflicts in Delta Lake", written solely from the provided source material.

## Whole-Table Conflicts in Delta Lake

**Whole-Table Conflicts in Delta Lake** are a category of transaction conflict errors that occur when a write or read operation attempts to access an entire table, but a concurrent modification has changed the table in a way that prevents the operation from completing safely. These conflicts are a subset of the `DELTA_CONCURRENT_APPEND` error class in Databricks.

### Overview

When a transaction reads or writes all data in a Delta table, it can conflict with concurrent operations that also modify the table at a broad scope. Delta Lake uses optimistic concurrency control and detects these conflicts during the commit phase, raising an error and requiring the user to retry or adjust the operation. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### WHOLE_TABLE_REPLACE

The `WHOLE_TABLE_REPLACE` error occurs when a concurrent operation replaces all data in the table. If a transaction was in progress when another operation completely replaced the table's contents, Delta Lake detects this conflict and raises the error. The recommended action is to retry the operation. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### WHOLE_TABLE_READ

The `WHOLE_TABLE_READ` error occurs when a transaction attempts to read the entire table, but a concurrent modification conflicts with that full-table scan. This can happen when an operation reads all rows without filters, and another transaction modifies the table concurrently. Delta Lake provides two mitigation strategies: ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

- **Add filters** to narrow the data scope of the query, reducing the chance of conflict with concurrent modifications.
- **Retry the operation** if the full-table read is truly necessary.

### Related Error Conditions

Whole-table conflicts belong to the broader `DELTA_CONCURRENT_APPEND` error class (SQLSTATE: 2D521). Other related sub-errors include:

- **ROW_LEVEL_CHANGES** – A concurrent operation modified the same rows that this transaction attempted to modify. Retry is recommended. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]
- **WITHOUT_HINT** – A generic conflict where no specific hint is available. Retry is recommended. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]
- **WITH_PARTITION_HINT** – A concurrent operation modified data in a specific partition. Retry is recommended. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]
- **PARTITIONED_TABLE_WITHOUT_MERGE_SOURCE** – Row-level conflict detection could not be performed on this partitioned table. Retry is recommended. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### Best Practices

To minimize whole-table conflicts:

- Use selective filters and predicates to narrow read and write scopes when possible, rather than reading entire tables. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]
- Retry operations that fail with whole-table conflict errors, as conflicts are often transient. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### Related Concepts

- [Delta Lake Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) – Optimistic concurrency model that detects conflicts at commit time.
- DELTA_CONCURRENT_APPEND Error Condition|DELTA_CONCURRENT_APPEND error condition – The parent error class that encompasses all whole-table and row-level conflicts.
- [Row-Level Conflicts in Delta Lake](/concepts/row-level-conflict-resolution-in-delta-lake.md) – Conflicts where concurrent operations modify the same rows.
- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) – The mechanism that tracks all changes and enables conflict detection.

### Sources

- delta_concurrent_append-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_append-error-condition-databricks-on-aws.md](/references/delta_concurrent_append-error-condition-databricks-on-aws-47a87778.md)
