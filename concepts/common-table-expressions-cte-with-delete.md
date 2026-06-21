---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 504b3eb7a40a9e995c35c73fb8062caf30d4b97ae719859b6440004666ee9cfb
  pageDirectory: concepts
  sources:
    - delete-from-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - common-table-expressions-cte-with-delete
    - CTE(WD
    - CTE
  citations:
    - file: delete-from-databricks-on-aws.md
title: Common Table Expressions (CTE) with DELETE
description: A CTE can optionally prefix a DELETE FROM statement to define named subqueries that improve readability and avoid repeated computation.
tags:
  - delta-lake
  - sql-cte
timestamp: "2026-06-18T15:14:54.696Z"
---

# Common Table Expressions (CTE) with DELETE

**Common Table Expressions (CTE) with DELETE** refers to the use of named, temporary result sets within a `DELETE FROM` statement to improve query readability, avoid repeated subquery computations, and simplify complex deletion logic in [Delta Lake](/concepts/delta-lake.md) tables.

## Overview

In Databricks SQL, a CTE can be used as an optional prefix to a `DELETE FROM` statement. The CTE defines one or more named queries that can then be referenced multiple times within the main `DELETE` query block. This enables you to write cleaner, more maintainable deletion logic by breaking complex operations into named, reusable components. ^[delete-from-databricks-on-aws.md]

## Syntax

The CTE precedes the `DELETE FROM` clause in the statement:

```
[ common_table_expression ]
DELETE FROM table_name [table_alias] [WHERE predicate]
```

^[delete-from-databricks-on-aws.md]

## How It Works

A CTE acts as a temporary named query that exists only for the duration of the `DELETE` statement. You can reference the CTE name in the `WHERE` predicate of the `DELETE` — for example, within `IN`, `NOT IN`, `EXISTS`, `NOT EXISTS`, or scalar subqueries. Note that the source material does not provide concrete examples showing CTEs specifically with DELETE, but the syntax definition confirms their availability. ^[delete-from-databricks-on-aws.md]

## Benefits

- **Avoids repeated computations.** Define complex filtering logic once in the CTE and reference it multiple times without recalculating. ^[delete-from-databricks-on-aws.md]
- **Improves readability.** Break nested or multi-step deletion logic into named, sequential steps. ^[delete-from-databricks-on-aws.md]
- **Simplifies maintenance.** Changes to the filtering logic need to be made in only one place (the CTE definition). ^[delete-from-databricks-on-aws.md]

## Supported Predicate Types

The `WHERE` predicate in a `DELETE` statement supports subqueries, including:

- `IN`
- `NOT IN`
- `EXISTS`
- `NOT EXISTS`
- Scalar subqueries

The following types of subqueries are **not** supported:
- Nested subqueries (a subquery inside another subquery)
- `NOT IN` subquery inside an `OR` condition, for example `a = 3 OR b NOT IN (SELECT c FROM t)`

In most cases, `NOT IN` subqueries can be rewritten using `NOT EXISTS`. Using `NOT EXISTS` is recommended whenever possible, as `DELETE` with `NOT IN` subqueries can be slow. ^[delete-from-databricks-on-aws.md]

## Example (Conceptual)

While the source material does not include a specific CTE-with-DELETE example, the following demonstrates the general pattern:

```sql
WITH outdated_orders AS (
  SELECT order_id
  FROM orders
  WHERE order_date < '2020-01-01'
    AND status = 'completed'
)
DELETE FROM order_archive AS oa
WHERE EXISTS (
  SELECT 1 FROM outdated_orders oo WHERE oa.order_id = oo.order_id
);
```

In this example:
- The CTE `outdated_orders` identifies stale orders.
- The `DELETE` statement references that CTE in its `WHERE` clause.
- The statement deletes only the rows in `order_archive` that match the CTE's results.

## Limitations

- The `DELETE` statement is only supported for [Delta Lake](/concepts/delta-lake.md) tables. ^[delete-from-databricks-on-aws.md]
- `table_name` must not include a temporal specification and must not be a foreign table. ^[delete-from-databricks-on-aws.md]
- Nested subqueries and NOT IN with OR conditions are not supported within the predicate. ^[delete-from-databricks-on-aws.md]

## Related Concepts

- [DELETE FROM](/concepts/delete-from-delta-lake.md) — The full statement syntax and usage for Delta Lake
- [Common Table Expressions (CTE)](/concepts/common-table-expressions-cte-in-dml.md) — General CTE syntax in Databricks SQL
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that supports this operation
- [Subqueries in DML](/concepts/subquery-restrictions-in-dml-statements.md) — How subqueries work in DELETE, UPDATE, and MERGE
- [NOT IN vs NOT EXISTS](/concepts/not-in-vs-not-exists-for-delete.md) — Performance considerations for deletion predicates

## Sources

- delete-from-databricks-on-aws.md

# Citations

1. [delete-from-databricks-on-aws.md](/references/delete-from-databricks-on-aws-ab1d0768.md)
