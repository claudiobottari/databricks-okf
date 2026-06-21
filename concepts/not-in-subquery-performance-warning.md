---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 52d090073a3ebbc11cebb91ae3d04152bd897a399cf0cb4274613638717892f5
  pageDirectory: concepts
  sources:
    - delete-from-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - not-in-subquery-performance-warning
    - NISPW
  citations:
    - file: delete-from-databricks-on-aws.md
title: NOT IN subquery performance warning
description: DELETE with NOT IN subqueries can be slow; Databricks recommends using NOT EXISTS instead whenever possible.
tags:
  - delta-lake
  - performance
  - optimization
timestamp: "2026-06-18T15:14:50.516Z"
---

# NOT IN Subquery Performance Warning

The **NOT IN subquery performance warning** advises against using `NOT IN` subqueries in `DELETE FROM` statements on [Delta Lake](/concepts/delta-lake.md) tables. Although `NOT IN` is syntactically supported, it can lead to slow query execution. The recommended alternative is to rewrite such subqueries using `NOT EXISTS`. ^[delete-from-databricks-on-aws.md]

## Why NOT IN Is Slow in DELETE

When a `DELETE` statement includes a `WHERE` clause with a `NOT IN` subquery, the query optimizer often struggles to generate an efficient execution plan. This is especially true when the subquery involves large tables or complex joins. The performance impact is significant enough that Databricks explicitly recommends avoiding `NOT IN` in `DELETE` operations. ^[delete-from-databricks-on-aws.md]

## Supported Subqueries in DELETE

The documentation notes that `DELETE FROM` supports several subquery types in the `WHERE` predicate, including:

- `IN`
- `NOT IN`
- `EXISTS`
- `NOT EXISTS`
- Scalar subqueries

However, two important restrictions apply:

1. Nested subqueries (a subquery inside another subquery) are **not supported**.
2. A `NOT IN` subquery inside an `OR` clause is **not supported** (e.g., `a = 3 OR b NOT IN (SELECT c FROM t)`).

The performance warning is separate from these syntax restrictions but applies to all `NOT IN` subqueries in `DELETE`. ^[delete-from-databricks-on-aws.md]

## Recommended Rewrite: Use NOT EXISTS

The guidance is clear:

> "In most cases, you can rewrite NOT IN subqueries using NOT EXISTS. We recommend using NOT EXISTS whenever possible, as DELETE with NOT IN subqueries can be slow."

For example, instead of:

```sql
DELETE FROM events
WHERE category NOT IN (SELECT category FROM events2 WHERE date > '2001-01-01');
```

Rewrite as:

```sql
DELETE FROM events AS e
WHERE NOT EXISTS (SELECT 1 FROM events2 AS e2
                  WHERE e2.date > '2001-01-01' AND e2.category = e.category);
```

The `NOT EXISTS` version is typically more efficient because it can leverage anti-join execution strategies, while `NOT IN` often requires scanning and comparing all values from the subquery. ^[delete-from-databricks-on-aws.md]

## When the Warning Applies

The performance warning applies specifically to `DELETE` statements on [Delta Lake](/concepts/delta-lake.md) tables. While `NOT IN` may perform acceptably in other contexts (e.g., `SELECT` queries), the recommendation is strongest for `DELETE` because the operation is already I/O-intensive and a slow subquery can severely degrade performance.

## Related Concepts

- [DELETE FROM](/concepts/delete-from-delta-lake.md) – Syntax and usage for Delta Lake
- Subqueries in SQL – Types and performance considerations
- NOT EXISTS – Alternative to NOT IN
- Anti-join – Execution strategy used for NOT EXISTS
- Delta Lake Performance Tuning – General optimization techniques

## Sources

- delete-from-databricks-on-aws.md

# Citations

1. [delete-from-databricks-on-aws.md](/references/delete-from-databricks-on-aws-ab1d0768.md)
