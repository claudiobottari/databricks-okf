---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 522f483cf2ba2020918d41eb13b97ed0209cc79476ad5dce17f70b5a5c665a9c
  pageDirectory: concepts
  sources:
    - delete-from-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delete-from-for-delta-lake
    - DFFDL
  citations:
    - file: delete-from-databricks-on-aws.md
title: DELETE FROM for Delta Lake
description: The DELETE FROM statement in Databricks SQL is used to delete rows from Delta Lake tables, with optional predicate filtering and support for subqueries in the WHERE clause.
tags:
  - delta-lake
  - dml
  - databricks-sql
timestamp: "2026-06-19T09:59:27.939Z"
---

# DELETE FROM for Delta Lake

**DELETE FROM** is a SQL statement that removes rows from a [Delta Lake](/concepts/delta-lake.md) table based on a specified predicate condition. When no predicate is provided, the statement deletes all rows from the table. This statement is only supported for Delta Lake tables. ^[delete-from-databricks-on-aws.md]

## Syntax

```sql
[ common_table_expression ]
DELETE FROM table_name [table_alias] [WHERE predicate]
```

^[delete-from-databricks-on-aws.md]

### Common Table Expression

The optional [common_table_expression](/concepts/common-table-expressions-cte-in-dml.md) (CTE) clause allows defining one or more named queries that can be reused multiple times within the main query block. CTEs help avoid repeated computations and improve the readability of complex, nested queries. ^[delete-from-databricks-on-aws.md]

### Table Name

The `table_name` parameter identifies an existing [Delta Lake Table](/concepts/delta-lake-table.md). The name must not include a temporal specification. The table must be a [Delta Lake Table](/concepts/delta-lake-table.md), not a foreign table. ^[delete-from-databricks-on-aws.md]

### Table Alias

The optional `table_alias` parameter defines an alias for the table. The alias must not include a column list. ^[delete-from-databricks-on-aws.md]

### WHERE Predicate

The `WHERE` clause filters rows by predicate. When omitted, all rows are deleted. ^[delete-from-databricks-on-aws.md]

The `WHERE` predicate supports the following types of subqueries:
- `IN`
- `NOT IN`
- `EXISTS`
- `NOT EXISTS`
- Scalar subqueries

The following types of subqueries are **not** supported:
- Nested subqueries (a subquery inside another subquery)
- `NOT IN` subqueries inside an `OR` expression (for example, `a = 3 OR b NOT IN (SELECT c from t)`)

^[delete-from-databricks-on-aws.md]

## Performance Considerations

In most cases, `NOT IN` subqueries can be rewritten using `NOT EXISTS`. Using `NOT EXISTS` is recommended whenever possible, as `DELETE` with `NOT IN` subqueries can be slow. ^[delete-from-databricks-on-aws.md]

## Examples

### Delete by date condition

```sql
DELETE FROM events WHERE date < '2017-01-01';
```
^[delete-from-databricks-on-aws.md]

### Delete using a subquery

```sql
DELETE FROM all_events
  WHERE session_time < (SELECT min(session_time) FROM good_events);
```
^[delete-from-databricks-on-aws.md]

### Delete using EXISTS

```sql
DELETE FROM orders AS t1
  WHERE EXISTS (SELECT oid FROM returned_orders WHERE t1.oid = oid);
```
^[delete-from-databricks-on-aws.md]

### Delete using NOT IN

```sql
DELETE FROM events
  WHERE category NOT IN (SELECT category FROM events2 WHERE date > '2001-01-01');
```
^[delete-from-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The storage layer that supports this statement
- [MERGE INTO](/concepts/merge-into-delta-lake.md) – An alternative DML statement for upserting data
- UPDATE – A related DML statement for modifying existing rows
- INSERT – A DML statement for adding new rows
- [COPY INTO](/concepts/copy-into-command.md) – A data ingestion command for Delta Lake
- [Common Table Expression](/concepts/common-table-expressions-cte-in-dml.md) – Reusable named queries within a statement
- Partition – Data organization in Delta Lake tables

## Sources

- delete-from-databricks-on-aws.md

# Citations

1. [delete-from-databricks-on-aws.md](/references/delete-from-databricks-on-aws-ab1d0768.md)
