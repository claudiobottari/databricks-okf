---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 76286b711b0deddb964f8b65e5321285eaf4c3a5839c6a6f05bb33932169837e
  pageDirectory: concepts
  sources:
    - delete-from-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - subquery-support-in-databricks-delete-where-clause
    - SSIDDWC
  citations:
    - file: delete-from-databricks-on-aws.md
title: Subquery support in Databricks DELETE WHERE clause
description: The WHERE predicate in DELETE FROM supports subqueries including IN, NOT IN, EXISTS, NOT EXISTS, and scalar subqueries, with specific restrictions on nested subqueries and NOT IN inside OR expressions.
tags:
  - subqueries
  - dml
  - databricks-sql
timestamp: "2026-06-19T09:58:54.926Z"
---

# Subquery support in Databricks DELETE WHERE clause

**Subquery support in Databricks DELETE WHERE clause** refers to the ability to use subqueries within the `WHERE` predicate of a `DELETE FROM` statement on [Delta Lake](/concepts/delta-lake.md) tables. This enables conditional row deletion based on data in other tables or aggregated results, rather than only simple column comparisons.

## Supported Subquery Types

The `WHERE` predicate in a `DELETE FROM` statement supports the following subquery types: ^[delete-from-databricks-on-aws.md]

- `IN` subqueries
- `NOT IN` subqueries
- `EXISTS` subqueries
- `NOT EXISTS` subqueries
- Scalar subqueries (subqueries that return a single value)

## Unsupported Subquery Patterns

Two types of subqueries are **not supported** in the `DELETE WHERE` clause: ^[delete-from-databricks-on-aws.md]

1. **Nested subqueries** — a subquery inside another subquery.
2. **`NOT IN` subquery inside an `OR`** — for example, `a = 3 OR b NOT IN (SELECT c from t)`.

## Performance Considerations

In most cases, `NOT IN` subqueries can be rewritten using `NOT EXISTS`. Databricks recommends using `NOT EXISTS` whenever possible, as `DELETE` with `NOT IN` subqueries can be slow. ^[delete-from-databricks-on-aws.md]

## Examples

### Delete rows matching a condition from another table

```sql
DELETE FROM all_events
  WHERE session_time < (SELECT min(session_time) FROM good_events);
```

This uses a scalar subquery to find the minimum session time from `good_events` and deletes all rows in `all_events` with an earlier session time. ^[delete-from-databricks-on-aws.md]

### Delete rows using EXISTS

```sql
DELETE FROM orders AS t1
  WHERE EXISTS (SELECT oid FROM returned_orders WHERE t1.oid = oid);
```

This deletes all orders that have a matching entry in the `returned_orders` table. ^[delete-from-databricks-on-aws.md]

### Delete rows using NOT IN

```sql
DELETE FROM events
  WHERE category NOT IN (SELECT category FROM events2 WHERE date > '2001-01-01');
```

This deletes events whose category does not appear in the set of categories from `events2` after a certain date. ^[delete-from-databricks-on-aws.md]

### Delete rows with a simple predicate

```sql
DELETE FROM events WHERE date < '2017-01-01';
```

While this example does not use a subquery, it shows the basic `DELETE FROM` syntax. ^[delete-from-databricks-on-aws.md]

## Syntax

```sql
[ common_table_expression ]
DELETE FROM table_name [table_alias] [WHERE predicate]
```

The `WHERE` predicate is optional. When omitted, all rows are deleted. The `table_name` must identify an existing [Delta Lake](/concepts/delta-lake.md) table and must not include a temporal specification. The optional `table_alias` provides an alias for the table but must not include a column list. ^[delete-from-databricks-on-aws.md]

## Related Concepts

- [DELETE FROM statement](/concepts/delta-lake-dml-operations.md) — Full syntax and usage for the `DELETE FROM` command
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that supports this statement
- [MERGE INTO](/concepts/merge-into-delta-lake.md) — An alternative for conditional updates, inserts, and deletes
- [UPDATE statement](/concepts/update-statement-delta-lake.md) — For modifying existing rows rather than deleting them
- [Common Table Expressions (CTEs)](/concepts/common-table-expressions-ctes-in-dml.md) — Can be used with `DELETE FROM` for complex queries
- Subqueries in Databricks SQL — General subquery support across SQL statements

## Sources

- delete-from-databricks-on-aws.md

# Citations

1. [delete-from-databricks-on-aws.md](/references/delete-from-databricks-on-aws-ab1d0768.md)
