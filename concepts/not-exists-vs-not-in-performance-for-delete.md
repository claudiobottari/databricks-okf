---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2f72ddf1224bdaaa26082c3d63fc2593bfe208bfbfba39d1242bb23f3873f78e
  pageDirectory: concepts
  sources:
    - delete-from-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - not-exists-vs-not-in-performance-for-delete
    - NEVNIPFD
  citations:
    - file: delete-from-databricks-on-aws.md
title: NOT EXISTS vs NOT IN Performance for DELETE
description: Databricks recommends using NOT EXISTS over NOT IN in DELETE WHERE clauses because NOT IN subqueries can be slow.
tags:
  - sql
  - performance
  - optimization
  - dml
timestamp: "2026-06-18T11:48:05.937Z"
---

# NOT EXISTS vs NOT IN Performance for DELETE

**NOT EXISTS vs NOT IN Performance for DELETE** refers to the performance difference between using `NOT EXISTS` and `NOT IN` subqueries in a `DELETE` statement on [Delta Lake](/concepts/delta-lake.md) tables. Databricks recommends using `NOT EXISTS` whenever possible, as `DELETE` with `NOT IN` subqueries can be slow.

## Overview

When deleting rows from a Delta table based on a subquery that excludes matching records, you have two syntax options: `NOT IN` and `NOT EXISTS`. Although both can produce the same logical result, their performance characteristics differ significantly on Databricks. ^[delete-from-databricks-on-aws.md]

## Performance Recommendation

Databricks explicitly recommends using `NOT EXISTS` instead of `NOT IN` for `DELETE` statements. The documentation states that `DELETE` with `NOT IN` subqueries can be slow, and in most cases, you can rewrite `NOT IN` subqueries using `NOT EXISTS`. ^[delete-from-databricks-on-aws.md]

### Example: NOT EXISTS (Preferred)

```sql
DELETE FROM events
WHERE category NOT EXISTS (
  SELECT category FROM events2 WHERE date > '2001-01-01'
);
```

^[delete-from-databricks-on-aws.md]

### Example: NOT IN (Slower)

```sql
DELETE FROM events
WHERE category NOT IN (
  SELECT category FROM events2 WHERE date > '2001-01-01'
);
```

^[delete-from-databricks-on-aws.md]

## Subquery Support

The `WHERE` predicate in a `DELETE FROM` statement supports several types of subqueries, including:
- `IN`
- `NOT IN`
- `EXISTS`
- `NOT EXISTS`
- Scalar subqueries

However, the following types of subqueries are not supported:
- **Nested subqueries** — a subquery inside another subquery
- **`NOT IN` subquery inside an `OR`** — for example, `a = 3 OR b NOT IN (SELECT c FROM t)`

^[delete-from-databricks-on-aws.md]

## Why NOT EXISTS Is Faster

The performance difference arises from how Databricks optimizes and executes these queries against Delta Lake tables:

- **`NOT EXISTS`** can be optimized into an anti-join operation, which Delta Lake's query engine can execute efficiently, especially when the subquery returns a large result set.
- **`NOT IN`** may require checking every value from the subquery against every row in the target table, and must also handle `NULL` values in the subquery result. If the subquery result contains `NULL`, the entire `NOT IN` condition evaluates to `UNKNOWN` (effectively `FALSE`) for all rows, which can lead to unexpected results or degraded performance.

## Best Practices

- **Prefer `NOT EXISTS` over `NOT IN`** for `DELETE` statements whenever the logic allows.
- **Avoid `NOT IN` subqueries inside `OR` clauses**, as these are not supported by Databricks SQL.
- **Avoid nested subqueries** in `DELETE` statements, as these are also unsupported.
- When you cannot avoid `NOT IN` — for example, when the subquery is part of a complex expression — consider breaking the operation into multiple steps, such as identifying the rows to delete in a temporary table first, then performing the `DELETE`.

## Related Concepts

- [DELETE FROM](/concepts/delete-from-delta-lake.md) — The full syntax reference for the `DELETE FROM` statement in Databricks SQL
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that supports `DELETE` operations
- Anti-Join — The query execution strategy used for `NOT EXISTS` optimization
- [Delta MERGE INTO](/concepts/delta-lake-merge-into-upsert.md) — An alternative to `DELETE` for upsert and conditional row removal
- [Common Table Expressions (CTE)](/concepts/common-table-expressions-cte-in-dml.md) — A feature that can help restructure complex `DELETE` queries

## Sources

- delete-from-databricks-on-aws.md

# Citations

1. [delete-from-databricks-on-aws.md](/references/delete-from-databricks-on-aws-ab1d0768.md)
