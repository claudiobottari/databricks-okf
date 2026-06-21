---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7439db10693121e8901b2256ad45f1ea81d436bb31fb0dfc64e3f217eb19d733
  pageDirectory: concepts
  sources:
    - delete-from-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - subquery-support-in-delete-where-clause
    - SSIDWC
  citations:
    - file: delete-from-databricks-on-aws.md
title: Subquery Support in DELETE WHERE Clause
description: Types of subqueries allowed (IN, NOT IN, EXISTS, NOT EXISTS, scalar) and not allowed (nested, NOT IN inside OR) in Delta Lake DELETE statements.
tags:
  - sql
  - subqueries
  - delta-lake
timestamp: "2026-06-19T14:58:52.087Z"
---

# Subquery Support in DELETE WHERE Clause

**Subquery support in the `DELETE FROM` WHERE clause** allows you to conditionally delete rows from a [Delta Lake](/concepts/delta-lake.md) table based on the results of a nested query. Databricks SQL and Databricks Runtime support several standard subquery forms within the `WHERE` predicate of a `DELETE` statement. ^[delete-from-databricks-on-aws.md]

## Supported Subquery Types

The `WHERE` predicate in `DELETE FROM` supports the following subquery types: ^[delete-from-databricks-on-aws.md]

- `IN` – delete rows where a column value matches any value returned by the subquery.
- `NOT IN` – delete rows where a column value does **not** match any value in the subquery result.
- `EXISTS` – delete rows for which the subquery returns at least one row.
- `NOT EXISTS` – delete rows for which the subquery returns no rows.
- **Scalar subqueries** – subqueries that return a single value (a single row and column) can be used in comparisons or as expressions within the `WHERE` clause.

## Unsupported Subquery Patterns

The following subquery patterns are **not** supported in a `DELETE` statement: ^[delete-from-databricks-on-aws.md]

- **Nested subqueries** – a subquery that itself contains another subquery (i.e., a subquery inside a subquery).
- **`NOT IN` subquery inside an `OR` expression** – for example, `a = 3 OR b NOT IN (SELECT c FROM t)`. This combination is not allowed.

In most cases, you can rewrite a `NOT IN` subquery as a `NOT EXISTS` subquery to avoid this limitation. ^[delete-from-databricks-on-aws.md]

## Performance Considerations

Databricks recommends using `NOT EXISTS` instead of `NOT IN` whenever possible, because `DELETE` operations with `NOT IN` subqueries can be **slow**. ^[delete-from-databricks-on-aws.md]

## Examples

The following examples illustrate supported subquery usage:

```sql
-- Delete rows from 'events' that have a date before '2017-01-01'
DELETE FROM events WHERE date < '2017-01-01';

-- Delete orders whose session_time is less than the minimum from good_events
DELETE FROM all_events
  WHERE session_time < (SELECT min(session_time) FROM good_events);

-- Delete orders that have a matching oid in returned_orders
DELETE FROM orders AS t1
  WHERE EXISTS (SELECT oid FROM returned_orders WHERE t1.oid = oid);

-- Delete events whose category is not present in events2 after a certain date
DELETE FROM events
  WHERE category NOT IN (SELECT category FROM events2 WHERE date > '2001-01-01');
```

^[delete-from-databricks-on-aws.md]

The fourth example uses `NOT IN`; for improved performance with large tables, consider rewriting it using `NOT EXISTS`.

## Applicability

The `DELETE FROM` statement with subquery support is **only supported for Delta Lake tables**. The `table_name` in the `DELETE` statement must not be a foreign table. ^[delete-from-databricks-on-aws.md]

## Related Concepts

- [DELETE FROM](/concepts/delete-from-delta-lake.md) – Base statement syntax and parameters
- [Delta Lake](/concepts/delta-lake.md) – The storage format required for `DELETE`
- [Common Table Expressions (CTE)](/concepts/common-table-expressions-cte-in-dml.md) – Can be used with `DELETE FROM` to simplify complex subqueries
- WHERE clause – General filtering and subquery semantics
- Subqueries in Databricks SQL – Broader subquery capabilities in the SELECT statement
- NOT EXISTS vs NOT IN – Performance guidance for correlated subqueries

## Sources

- delete-from-databricks-on-aws.md

# Citations

1. [delete-from-databricks-on-aws.md](/references/delete-from-databricks-on-aws-ab1d0768.md)
