---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9d56674fb9351584f11610483aa64cd2e3920cf8d1adf770d70847c6557e40da
  pageDirectory: concepts
  sources:
    - update-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - subquery-restrictions-in-update-where-clause
    - SRIUWC
  citations:
    - file: update-databricks-on-aws.md
title: Subquery Restrictions in UPDATE WHERE Clause
description: "Limitations on subqueries in UPDATE WHERE clauses: nested subqueries and NOT IN subqueries inside OR are not allowed; NOT IN can be rewritten as NOT EXISTS for better performance."
tags:
  - sql
  - subqueries
  - restrictions
timestamp: "2026-06-19T23:16:35.527Z"
---

# Subquery Restrictions in UPDATE WHERE Clause

The **Subquery Restrictions in UPDATE WHERE Clause** define which types of subqueries are permitted in the `WHERE` clause of an `UPDATE` statement on Databricks. These restrictions apply only to [Delta Lake](/concepts/delta-lake.md) tables, as the `UPDATE` statement is supported exclusively for [Delta Lake](/concepts/delta-lake.md). ^[update-databricks-on-aws.md]

## Allowed and Prohibited Subquery Patterns

The `WHERE` clause in an `UPDATE` statement may include subqueries, but two patterns are explicitly prohibited: ^[update-databricks-on-aws.md]

- **Nested subqueries** – a subquery placed inside another subquery is not allowed. ^[update-databricks-on-aws.md]
- **A `NOT IN` subquery inside an `OR`** – for example, `a = 3 OR b NOT IN (SELECT c FROM t)`. ^[update-databricks-on-aws.md]

These restrictions prevent ambiguous or inefficient evaluation of the update predicate.

## Performance Considerations for NOT IN

Using `NOT IN` subqueries in an `UPDATE` statement can be slow. Databricks recommends rewriting `NOT IN` subqueries as `NOT EXISTS` whenever possible. The `NOT EXISTS` form is not only exempt from the restriction above but also typically performs better. ^[update-databricks-on-aws.md]

## Rewriting NOT IN as NOT EXISTS

In most cases, a `NOT IN` subquery can be rewritten using `NOT EXISTS`. This rewrite avoids both the restriction on `NOT IN` inside `OR` and the performance penalty. The following example from the Databricks documentation illustrates a valid `NOT IN` subquery in an `UPDATE`: ^[update-databricks-on-aws.md]

```sql
UPDATE events
  SET category = 'undefined'
  WHERE category NOT IN (SELECT category FROM events2 WHERE date > '2001-01-01')
```

While the above is allowed (it does not contain an `OR`), Databricks still suggests rewriting it with `NOT EXISTS` for better performance. The equivalent form would be: ^[update-databricks-on-aws.md]

```sql
UPDATE events AS t1
  SET category = 'undefined'
  WHERE NOT EXISTS (SELECT 1 FROM events2 WHERE events2.category = t1.category AND events2.date > '2001-01-01')
```

## Alternative to JOIN-Based Updates

Databricks SQL does not support `UPDATE ... FROM ... JOIN` syntax. To update a table based on a join, use [MERGE INTO](/concepts/merge-into-delta-lake.md) instead. For example, a `MERGE` statement can replace a hypothetical `UPDATE ... FROM ... JOIN` where you want to set column values from another table. ^[update-databricks-on-aws.md]

## Related Concepts

- UPDATE – The statement that applies these restrictions.
- WHERE clause – The predicate clause that governs which rows are updated.
- NOT IN – The operator subject to performance and syntactic restrictions.
- NOT EXISTS – The recommended alternative for `NOT IN` subqueries.
- [MERGE INTO](/concepts/merge-into-delta-lake.md) – The syntax to use when updating from a join.
- [Delta Lake](/concepts/delta-lake.md) – The storage format that supports the `UPDATE` statement.
- Subqueries – General use of subqueries in SQL.

## Sources

- update-databricks-on-aws.md

# Citations

1. [update-databricks-on-aws.md](/references/update-databricks-on-aws-8f0bcd2b.md)
