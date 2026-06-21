---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 27f47272dddd5cec8e0c798c181a050239b53d508211dd644c57bc9a91a621b3
  pageDirectory: concepts
  sources:
    - delta_concurrent_append-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - filter-predicates-in-conflict-detection
    - FPICD
  citations:
    - file: delta_concurrent_append-error-condition-databricks-on-aws.md
title: Filter Predicates in Conflict Detection
description: The requirement that filter predicates used by a transaction must be applicable for row-level conflict detection, otherwise the operation may fail with PREDICATES_NEED_REWRITE
tags:
  - delta-lake
  - query-optimization
  - predicates
timestamp: "2026-06-19T10:03:43.818Z"
---

# Filter Predicates in Conflict Detection

**Filter Predicates in Conflict Detection** refers to the query conditions that a transaction attempts to apply to a Delta table for row-level conflict resolution. When a concurrent modification makes these predicates inapplicable, Delta Lake raises a `DELTA_CONCURRENT_APPEND` error with the `PREDICATES_NEED_REWRITE` sub-type, requiring the operation to be retried. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Overview

Delta Lake uses [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) to manage concurrent writes to a table. When two transactions attempt to modify the same table simultaneously, Delta Lake performs row-level conflict detection to determine if the changes can be safely merged. Filter predicates play a critical role in this process — they define which rows a transaction intends to read or modify. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## PREDICATES_NEED_REWRITE Error

The `PREDICATES_NEED_REWRITE` error occurs when the filter predicates used by a transaction cannot be applied for row-level conflict detection due to concurrent changes to the table. This typically happens when: ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

- A concurrent operation modifies the table metadata (schema, partitioning, or protocol), invalidating the original predicates. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]
- The table's data layout changes in a way that prevents predicate pushdown or predicate-based conflict resolution. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### Error Message

Delta Lake returns the following error when this condition is detected:

```
DELTA_CONCURRENT_APPEND.PREDICATES_NEED_REWRITE
The filter predicates used by this transaction could not be applied for row-level conflict detection. Please retry the operation.
```

^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Common Causes

### Metadata Changes

When a concurrent transaction alters the table schema, partitioning scheme, or other metadata, the filter predicates from the original transaction may no longer be valid. For example, if a column referenced in the predicate was renamed or dropped, the predicate cannot be evaluated. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### Protocol Changes

If a concurrent operation upgrades the Delta Lake [table protocol](/concepts/delta-lake-table-protocol-changes.md) version, the conflict detection logic for the original transaction may become incompatible, leading to the `PREDICATES_NEED_REWRITE` error. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

### Full Table Operations

Transactions that attempt to read or modify the entire table (such as a full table scan or replace) are particularly susceptible to this error, as they have no narrow predicates that can be checked for conflicts. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Resolution

The recommended resolution is to **retry the operation**. Delta Lake will re-read the table metadata and attempt to apply the new filter predicates against the updated table state. In most cases, the retry succeeds. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Best Practices

- **Add narrow filters** to queries to minimize the scope of conflict detection. For example, use `WHERE` clauses that limit data to specific partitions or date ranges. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]
- **Avoid concurrent metadata changes** (schema, partitioning, protocol upgrades) when other transactions are actively writing to the table. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]
- **Implement retry logic** in your application to handle transient `DELTA_CONCURRENT_APPEND` errors automatically. ^[delta_concurrent_append-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) — The framework for managing concurrent table modifications.
- [Row-Level Conflict Detection](/concepts/delta-lake-row-level-conflict-detection.md) — How Delta Lake resolves conflicts at the row level.
- DELTA_CONCURRENT_APPEND Error — The parent error class for transaction conflicts.
- [Optimistic Concurrency Control](/concepts/delta-lake-optimistic-concurrency-control.md) — The underlying concurrency model used by Delta Lake.
- Table Protocol in Delta Lake — How protocol versions affect conflict detection.

## Sources

- delta_concurrent_append-error-condition-databricks-on-aws.md

# Citations

1. [delta_concurrent_append-error-condition-databricks-on-aws.md](/references/delta_concurrent_append-error-condition-databricks-on-aws-47a87778.md)
