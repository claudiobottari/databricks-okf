---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bbac51dbd29e54d0357d68cb95b23cad8142630f3bab14e531c082403ca0b1bf
  pageDirectory: concepts
  sources:
    - delete-from-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - common-table-expressions-with-delete-from
    - CTEWDF
  citations:
    - file: delete-from-databricks-on-aws.md
title: Common Table Expressions with DELETE FROM
description: Databricks SQL allows using common table expressions (CTEs) as named queries that can be reused within the DELETE FROM statement to improve readability or avoid repeated computations.
tags:
  - cte
  - dml
  - databricks-sql
timestamp: "2026-06-19T09:59:32.269Z"
---

# Common Table Expressions with DELETE FROM

**Common Table Expressions (CTEs) with DELETE FROM** allow you to define named temporary result sets that can be referenced within a `DELETE` statement's `WHERE` clause. This enables more readable and maintainable deletion logic by breaking complex filtering conditions into reusable query blocks. ^[delete-from-databricks-on-aws.md]

## Syntax

A CTE can be placed before a `DELETE FROM` statement to compute intermediate results that are then used by the deletion predicate. The full syntax is:

```sql
[ common_table_expression ]
DELETE FROM table_name [table_alias]
[WHERE predicate]
```

^[delete-from-databricks-on-aws.md]

The CTE must appear immediately before the `DELETE FROM` keyword, with no intervening statements. The `DELETE FROM` clause specifies the target table and an optional alias. The `WHERE` clause, which is also optional, provides the filtering predicate that determines which rows to delete. ^[delete-from-databricks-on-aws.md]

## Purpose

CTEs serve two primary purposes in this context:

- **Reusability:** A named query defined in the CTE can be referenced multiple times within the `WHERE` predicate, avoiding repeated computation of the same subquery. ^[delete-from-databricks-on-aws.md]
- **Readability:** Breaking a deeply nested or complex filtering condition into a CTE makes the overall `DELETE` statement easier to understand and maintain. ^[delete-from-databricks-on-aws.md]

## Requirements

- This statement is only supported for [Delta Lake](/concepts/delta-lake.md) tables. It does not apply to foreign tables or other table formats. ^[delete-from-databricks-on-aws.md]
- The table name must not include a temporal specification. ^[delete-from-databricks-on-aws.md]

## Supported Subqueries in WHERE

The `WHERE` predicate within a CTE-backed `DELETE FROM` supports several subquery types:

- `IN` and `NOT IN`
- `EXISTS` and `NOT EXISTS`
- Scalar subqueries

^[delete-from-databricks-on-aws.md]

## Unsupported Subquery Patterns

The following subquery patterns are **not** supported when used with `DELETE FROM`:

- **Nested subqueries** — a subquery placed inside another subquery. ^[delete-from-databricks-on-aws.md]
- **`NOT IN` subquery inside an `OR`** — for example, `a = 3 OR b NOT IN (SELECT c FROM t)`. ^[delete-from-databricks-on-aws.md]

In most cases, a `NOT IN` subquery can be rewritten as a `NOT EXISTS` subquery. Databricks recommends using `NOT EXISTS` whenever possible, because `DELETE` with `NOT IN` subqueries can be slow. ^[delete-from-databricks-on-aws.md]

## Examples

### Using a CTE to identify stale records

The following example uses a CTE to define "good" sessions, then deletes all events that fall outside that time window: ^[delete-from-databricks-on-aws.md]

```sql
WITH good_sessions AS (
  SELECT min(session_time) AS min_time
  FROM good_events
)
DELETE FROM all_events
WHERE session_time < (SELECT min_time FROM good_sessions)
```

### Filtering with EXISTS

Delete rows from `orders` where a matching `oid` is found in `returned_orders`: ^[delete-from-databricks-on-aws.md]

```sql
WITH returned AS (
  SELECT oid FROM returned_orders
)
DELETE FROM orders AS t1
WHERE EXISTS (SELECT 1 FROM returned WHERE returned.oid = t1.oid)
```

### Deleting without a CTE (direct predicate)

When no CTE is needed, the `DELETE FROM` statement can use a simple `WHERE` clause: ^[delete-from-databricks-on-aws.md]

```sql
DELETE FROM events WHERE date < '2017-01-01'
```

## Related Concepts

- [Common Table Expressions (CTE)](/concepts/common-table-expressions-cte-in-dml.md) — General syntax and usage for CTEs in Databricks SQL
- [DELETE FROM (Delta Lake)](/concepts/delete-from-delta-lake.md) — The base `DELETE FROM` statement without CTE support
- WHERE clause — Filtering predicate for row selection
- Subqueries — Supported subquery types in Databricks SQL
- NOT EXISTS — Recommended alternative to `NOT IN` for better performance

## Sources

- delete-from-databricks-on-aws.md

# Citations

1. [delete-from-databricks-on-aws.md](/references/delete-from-databricks-on-aws-ab1d0768.md)
