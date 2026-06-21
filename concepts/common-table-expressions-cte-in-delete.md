---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ad3c2890af78d5c96ba7b09ba90e789087e834b63b4e4cb6a6e5c17b9779e4b0
  pageDirectory: concepts
  sources:
    - delete-from-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - common-table-expressions-cte-in-delete
    - CTE(ID
    - Common Table Expression (CTE) in SELECT
  citations:
    - file: delete-from-databricks-on-aws.md
title: Common Table Expressions (CTE) in DELETE
description: Optional use of CTEs with DELETE FROM to reuse named queries and improve complex deletion logic
tags:
  - sql
  - cte
  - dml
timestamp: "2026-06-19T18:19:49.717Z"
---

# Common Table Expressions (CTE) in DELETE

**Common Table Expressions (CTE) in DELETE** refers to the use of named temporary result sets within a `DELETE` statement on [Delta Lake](/concepts/delta-lake.md) tables. A CTE allows you to define one or more named queries that can be referenced multiple times within the main `DELETE` operation, improving readability and avoiding repeated computations in complex deletion logic. ^[delete-from-databricks-on-aws.md]

## Syntax

The CTE is placed before the `DELETE FROM` clause in the statement:

```sql
[ common_table_expression ]
DELETE FROM table_name [table_alias] [WHERE predicate]
```

^[delete-from-databricks-on-aws.md]

## Parameters

- **common_table_expression**: One or more named queries that can be reused within the main query block. CTEs help simplify complex, nested queries by breaking them into manageable parts. ^[delete-from-databricks-on-aws.md]
- **table_name**: Identifies an existing [Delta Lake](/concepts/delta-lake.md) table. The name must not include a temporal specification and must not be a foreign table. ^[delete-from-databricks-on-aws.md]
- **table_alias**: Defines an alias for the table. The alias must not include a column list. ^[delete-from-databricks-on-aws.md]
- **WHERE predicate**: Filters rows to delete. Supports subqueries including `IN`, `NOT IN`, `EXISTS`, `NOT EXISTS`, and scalar subqueries. ^[delete-from-databricks-on-aws.md]

## Supported Subqueries

The `WHERE` predicate in a CTE-based `DELETE` supports the following subquery types:

- `IN` subqueries
- `NOT IN` subqueries
- `EXISTS` subqueries
- `NOT EXISTS` subqueries
- Scalar subqueries

The following subquery types are **not supported**:

- Nested subqueries (a subquery inside another subquery)
- `NOT IN` subquery inside an `OR` condition (e.g., `a = 3 OR b NOT IN (SELECT c FROM t)`)

In most cases, `NOT IN` subqueries can be rewritten using `NOT EXISTS`. Using `NOT EXISTS` is recommended whenever possible, as `DELETE` with `NOT IN` subqueries can be slow. ^[delete-from-databricks-on-aws.md]

## Examples

### Basic DELETE with CTE

```sql
WITH recent_events AS (
  SELECT * FROM events WHERE date >= '2017-01-01'
)
DELETE FROM events
WHERE date < (SELECT MIN(date) FROM recent_events);
```

### DELETE with EXISTS and CTE

```sql
WITH returned_orders AS (
  SELECT oid FROM returned_orders WHERE return_date > '2024-01-01'
)
DELETE FROM orders AS t1
WHERE EXISTS (SELECT oid FROM returned_orders WHERE t1.oid = oid);
```

### DELETE with NOT EXISTS

```sql
WITH valid_categories AS (
  SELECT category FROM events2 WHERE date > '2001-01-01'
)
DELETE FROM events
WHERE category NOT IN (SELECT category FROM valid_categories);
```

## Related Concepts

- [DELETE FROM](/concepts/delete-from-delta-lake.md) — The base statement for deleting rows from Delta Lake tables
- [Common Table Expression (CTE)](/concepts/common-table-expressions-cte-in-dml.md) — General CTE syntax and usage in SQL
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that supports this statement
- [MERGE INTO](/concepts/merge-into-delta-lake.md) — An alternative for conditional row deletion
- [UPDATE Statement](/concepts/update-statement-delta-lake.md) — Related DML operation for modifying rows
- Subqueries — Nested queries used within WHERE predicates

## Sources

- delete-from-databricks-on-aws.md

# Citations

1. [delete-from-databricks-on-aws.md](/references/delete-from-databricks-on-aws-ab1d0768.md)
