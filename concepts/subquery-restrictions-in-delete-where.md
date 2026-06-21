---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e1a2d143cc33c6bd6cd386e937d0d1bd4bd012579b1c54d4a4067468f4c275e7
  pageDirectory: concepts
  sources:
    - delete-from-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - subquery-restrictions-in-delete-where
    - SRIDW
  citations:
    - file: delete-from-databricks-on-aws.md
title: Subquery Restrictions in DELETE WHERE
description: Restrictions on subquery types within DELETE WHERE predicates, including nested subqueries and NOT IN within OR
tags:
  - sql
  - subqueries
  - dml
timestamp: "2026-06-19T18:19:47.732Z"
---

# Subquery Restrictions in DELETE WHERE

The `DELETE FROM` statement in Databricks SQL supports filtering rows with a `WHERE` predicate that can include subqueries. However, certain subquery patterns are not allowed and others may have performance implications. This page documents the supported and unsupported subquery types for the `DELETE` command on Delta Lake tables. ^[delete-from-databricks-on-aws.md]

## Supported Subqueries

The `WHERE` predicate in a `DELETE` statement can contain the following types of subqueries:

- `IN` subqueries
- `NOT IN` subqueries
- `EXISTS` subqueries
- `NOT EXISTS` subqueries
- Scalar subqueries (subqueries that return a single value)

^[delete-from-databricks-on-aws.md]

## Unsupported Subquery Types

The following subquery patterns are **not supported** in a `DELETE WHERE` clause:

- **Nested subqueries** – a subquery placed inside another subquery. For example, `DELETE FROM t1 WHERE x IN (SELECT y FROM t2 WHERE y IN (SELECT z FROM t3))` would be invalid because the inner `SELECT ... FROM t3` is nested inside the first subquery. ^[delete-from-databricks-on-aws.md]
- `NOT IN` subquery used inside an `OR` expression. For example, `a = 3 OR b NOT IN (SELECT c FROM t)` is not supported. ^[delete-from-databricks-on-aws.md]

## Performance Considerations for `NOT IN` Subqueries

In most cases, you can rewrite a `NOT IN` subquery using `NOT EXISTS`. Databricks recommends using `NOT EXISTS` whenever possible, because `DELETE` statements that use `NOT IN` subqueries can be **slow**. ^[delete-from-databricks-on-aws.md]

## Valid Subquery Examples

The following examples show valid subquery usage in `DELETE FROM` statements:

```sql
-- Scalar subquery
DELETE FROM all_events
  WHERE session_time < (SELECT min(session_time) FROM good_events);

-- EXISTS subquery
DELETE FROM orders AS t1
  WHERE EXISTS (SELECT oid FROM returned_orders WHERE t1.oid = oid);

-- NOT IN subquery (allowed, but may be slow)
DELETE FROM events
  WHERE category NOT IN (SELECT category FROM events2 WHERE date > '2001-01-01');
```

^[delete-from-databricks-on-aws.md]

## Related Concepts

- [DELETE FROM](/concepts/delete-from-delta-lake.md) – Full syntax and parameters for the `DELETE` statement.
- [Delta Lake](/concepts/delta-lake.md) – The table format for which `DELETE` is supported.
- [MERGE INTO](/concepts/merge-into-delta-lake.md) – An alternative DML statement that can perform conditional deletes.
- Subqueries – General guide to using subqueries in Databricks SQL.
- WHERE Clause – Filtering rows with predicates.

## Sources

- delete-from-databricks-on-aws.md

# Citations

1. [delete-from-databricks-on-aws.md](/references/delete-from-databricks-on-aws-ab1d0768.md)
