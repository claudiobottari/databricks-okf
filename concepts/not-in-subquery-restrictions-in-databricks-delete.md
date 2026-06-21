---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 42462eddd1eb8b15c08326a203c32fe6bb00a442b548e3bc0a64209deadfd98e
  pageDirectory: concepts
  sources:
    - delete-from-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - not-in-subquery-restrictions-in-databricks-delete
    - NISRIDD
  citations:
    - file: delete-from-databricks-on-aws.md
title: NOT IN subquery restrictions in Databricks DELETE
description: In Databricks SQL DELETE FROM statements, NOT IN subqueries are not supported when nested inside an OR expression, and can be slow; NOT EXISTS is recommended as a faster alternative.
tags:
  - subqueries
  - performance
  - databricks-sql
  - dml
timestamp: "2026-06-19T09:59:04.613Z"
---

# NOT IN Subquery Restrictions in Databricks DELETE

**NOT IN subquery restrictions in Databricks DELETE** refers to the limitations and best practices when using a `NOT IN` subquery inside the `WHERE` clause of a `DELETE FROM` statement on Delta Lake tables. While Databricks SQL supports several subquery types in `DELETE`, `NOT IN` subqueries are subject to specific restrictions and performance considerations.

## Supported Subqueries in DELETE

The `WHERE` predicate of a `DELETE FROM` statement supports subqueries, including `IN`, `NOT IN`, `EXISTS`, `NOT EXISTS`, and scalar subqueries. ^[delete-from-databricks-on-aws.md]

## Restrictions

The following types of subqueries are **not supported** in a `DELETE` statement:

1. **Nested subqueries** — a subquery inside another subquery. ^[delete-from-databricks-on-aws.md]
2. **`NOT IN` subquery inside an `OR`** — for example, `a = 3 OR b NOT IN (SELECT c FROM t)`. ^[delete-from-databricks-on-aws.md]

These restrictions apply only to subqueries in the `DELETE` context. The `NOT IN` subquery is allowed when used alone (i.e., not nested and not combined with `OR`), as shown in the example:

```sql
DELETE FROM events
  WHERE category NOT IN (SELECT category FROM events2 WHERE date > '2001-01-01');
```

^[delete-from-databricks-on-aws.md]

## Performance Considerations

Even when a `NOT IN` subquery is syntactically allowed, Databricks recommends using `NOT EXISTS` instead. `DELETE` with `NOT IN` subqueries can be slow. In most cases, a `NOT IN` query can be rewritten as a `NOT EXISTS` query, which often performs better. ^[delete-from-databricks-on-aws.md]

## Best Practice: Use NOT EXISTS

Because `NOT IN` subqueries are slow and subject to restrictions, Databricks recommends using `NOT EXISTS` whenever possible. The following example rewrites the earlier `NOT IN` query using `NOT EXISTS`:

```sql
DELETE FROM events AS t1
  WHERE NOT EXISTS (SELECT 1 FROM events2 t2 WHERE t2.category = t1.category AND t2.date > '2001-01-01');
```

^[delete-from-databricks-on-aws.md]

## Related Concepts

- [DELETE FROM](/concepts/delete-from-delta-lake.md) — The full syntax and semantics of the `DELETE` statement.
- WHERE clause — How predicates filter rows in DML statements.
- Subqueries — General subquery support in Databricks SQL.
- NOT EXISTS — The recommended alternative to `NOT IN`.
- NO_HINT Sub-Error|IN subquery — Supported subquery forms without the same restrictions.
- [Delta Lake](/concepts/delta-lake.md) — The storage layer underlying this operation.

## Sources

- delete-from-databricks-on-aws.md

# Citations

1. [delete-from-databricks-on-aws.md](/references/delete-from-databricks-on-aws-ab1d0768.md)
