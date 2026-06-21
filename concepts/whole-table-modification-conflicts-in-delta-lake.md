---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4c5919f5a2a841ca791537904ad9f2399279c71ec476a21dd2531acbb8d63c0a
  pageDirectory: concepts
  sources:
    - delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - whole-table-modification-conflicts-in-delta-lake
    - WMCIDL
  citations:
    - file: delta_concurrent_delete_delete-error-condition-databricks-on-aws.md
title: Whole-Table Modification Conflicts in Delta Lake
description: A class of transaction conflicts in Delta Lake where either the current or concurrent transaction attempts to operate on the entire table without filters, causing a conflict.
tags:
  - delta-lake
  - concurrency
  - optimization
timestamp: "2026-06-19T15:03:14.691Z"
---

# Whole-Table Modification Conflicts in Delta Lake

**Whole-table modification conflicts** are a subtype of Delta Lake transaction conflict that arise when a transaction attempts to modify all rows of a table (or replaces all data) concurrently with another transaction that also touches a broad portion of the table. These conflicts are reported through the `DELTA_CONCURRENT_DELETE_DELETE` error class and its associated sub‑error conditions.

## Overview

Delta Lake uses [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) to detect conflicts between concurrent write operations. When a transaction reads an entire table without filters and then attempts to delete, update, or merge data, it creates a **whole-table read conflict** if another transaction has concurrently modified the same table. Similarly, if a concurrent operation replaces all data in the table, a **whole-table replace conflict** occurs. Both situations prevent automatic conflict resolution and require the user to retry or restructure the operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Sub‑error Conditions

The following sub‑error conditions under `DELTA_CONCURRENT_DELETE_DELETE` directly relate to whole‑table modifications:

### EMPTY_READ_PREDICATES

This transaction did not include any filters and modified the entire table, conflicting with the concurrent modification. **Action:** Add filters to your query to narrow the data scope and retry the operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### WHOLE_TABLE_READ

This transaction attempted to modify the entire table, conflicting with the concurrent modification. **Action:** Add filters to your query to narrow the data scope and retry the operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

### WHOLE_TABLE_REPLACE

The concurrent operation replaced all data in the table. **Action:** Retry the operation. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Common Causes

- Running a `DELETE`, `UPDATE`, or `MERGE` statement on a table **without a `WHERE` clause** (or with a predicate that evaluates to true for all rows) while another write is in progress. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]
- A concurrent operation that **truncates** or **overwrites** the entire table (e.g., `INSERT OVERWRITE` without a partition filter) while another transaction is reading the same table. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## How Delta Lake Handles These Conflicts

Delta Lake’s **row-level conflict detection** works by analyzing the read and write predicates of concurrent transactions. When a transaction reads the whole table (i.e., its read predicate is empty or always true), the system cannot narrow the conflict to a subset of rows. In such cases, it raises `WHOLE_TABLE_READ` or `EMPTY_READ_PREDICATES` instead of attempting automatic resolution. For whole-table replacements, the system detects that all data has been rewritten and raises `WHOLE_TABLE_REPLACE`. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Resolution

The recommended resolution depends on the sub‑error:

| Sub‑error | Recommended action |
|-----------|-------------------|
| `EMPTY_READ_PREDICATES` | Add filters to the query to limit the scope of the modification. |
| `WHOLE_TABLE_READ` | Add filters to the query to limit the scope of the modification. |
| `WHOLE_TABLE_REPLACE` | Retry the operation. The concurrent replacement has already completed, so a retry will likely succeed. |

For all whole-table modification conflicts, the primary mitigation is to **avoid unbounded writes** by using partition‑level or row‑level filters wherever possible. ^[delta_concurrent_delete_delete-error-condition-databricks-on-aws.md]

## Related Concepts

- Delta Lake Transaction Conflicts – Overview of all conflict types (delete‑delete, delete‑update, etc.).
- [Row-Level Conflict Detection](/concepts/delta-lake-row-level-conflict-detection.md) – How Delta Lake resolves conflicts at the row level.
- [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) – The underlying concurrency model used by Delta Lake.
- Partitioned Tables in Delta Lake – Using partitions to reduce conflict scope and improve concurrency.
- Change Data Feed (CDC) – Metadata columns that can interfere with conflict detection if a column named `_change_type` exists.

## Sources

- delta_concurrent_delete_delete-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_delete_delete-error-condition-databricks-on-aws.md](/references/delta_concurrent_delete_delete-error-condition-databricks-on-aws-6fcec7a7.md)
