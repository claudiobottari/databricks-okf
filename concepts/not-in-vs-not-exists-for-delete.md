---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a309fd0288bb66c491a3d05d7fd6dc1fcd0b3cdc2602beeb6055538c943edd84
  pageDirectory: concepts
  sources:
    - delete-from-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - not-in-vs-not-exists-for-delete
    - NIVNEFD
    - NOT IN vs NOT EXISTS
  citations:
    - file: delete-from-databricks-on-aws.md
title: NOT IN vs NOT EXISTS for DELETE
description: Preference for NOT EXISTS over NOT IN subqueries in DELETE statements due to performance considerations
tags:
  - sql
  - performance
  - best-practices
  - dml
timestamp: "2026-06-19T18:19:46.219Z"
---

# NOT IN vs NOT EXISTS for DELETE

When deleting rows from a [Delta Lake](/concepts/delta-lake.md) table using `DELETE FROM`, the `WHERE` predicate can include subqueries with `IN`, `NOT IN`, `EXISTS`, and `NOT EXISTS`. While both `NOT IN` and `NOT EXISTS` can express the same logical condition — “delete rows that do not match a set of values” — they differ significantly in performance and compatibility within the `DELETE` statement. ^[delete-from-databricks-on-aws.md]

## Performance Considerations

The Databricks documentation explicitly recommends using `NOT EXISTS` over `NOT IN` for `DELETE` operations, because `DELETE` with `NOT IN` subqueries can be slow. In most cases, a `NOT IN` subquery can be rewritten as an equivalent `NOT EXISTS` subquery. ^[delete-from-databricks-on-aws.md]

For example, the following two statements are logically equivalent, but the `NOT EXISTS` version is preferred:

```sql
-- NOT IN (slower)
DELETE FROM events
WHERE category NOT IN (SELECT category FROM events2 WHERE date > '2001-01-01');

-- NOT EXISTS (recommended)
DELETE FROM events e
WHERE NOT EXISTS (SELECT 1 FROM events2 e2 WHERE e2.date > '2001-01-01' AND e2.category = e.category);
```

^[delete-from-databricks-on-aws.md]

## Restrictions on Subquery Placement

The `WHERE` predicate of a `DELETE` statement supports `NOT IN` subqueries only under specific conditions. **`NOT IN` subquery inside an `OR` is not supported.** For example, the following construct is invalid:

```sql
-- NOT allowed: NOT IN inside OR
DELETE FROM t WHERE a = 3 OR b NOT IN (SELECT c FROM s);
```

Additionally, nested subqueries (a subquery inside another subquery) are not supported for any of the allowed subquery types (`IN`, `NOT IN`, `EXISTS`, `NOT EXISTS`, and scalar subqueries). ^[delete-from-databricks-on-aws.md]

## Recommendation

Whenever possible, rewrite `NOT IN` subqueries as `NOT EXISTS` subqueries in `DELETE` statements. This rewrite avoids the performance penalty associated with `NOT IN` and sidesteps the restriction on using `NOT IN` within `OR` conditions. ^[delete-from-databricks-on-aws.md]

## Related Concepts

- [DELETE FROM](/concepts/delete-from-delta-lake.md) — The DML statement that removes rows from a Delta table.
- Subqueries in WHERE clause — General patterns for using subqueries in DML predicates.
- Delta Lake DML — Overview of insert, update, merge, and delete operations on Delta tables.
- SQL performance optimization — Best practices for efficient query execution on Databricks.

## Sources

- delete-from-databricks-on-aws.md

# Citations

1. [delete-from-databricks-on-aws.md](/references/delete-from-databricks-on-aws-ab1d0768.md)
