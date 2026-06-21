---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 589dc99d3ef7433abb8dbdb019658f409f4ce44314abea00d74006cc28efc63d
  pageDirectory: concepts
  sources:
    - delete-from-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-dml-operations
    - DLDO
    - Delta Lake DDL Operations
    - Delta Lake MERGE Operation
    - Delta Lake Operations
    - Delta Lake table operations
    - Delta Lake write operations
    - Delta Merge Operations
    - MERGE Operations
  citations:
    - file: delete-from-databricks-on-aws.md
title: Delta Lake DML Operations
description: Delta Lake supports standard DML operations including DELETE, INSERT, MERGE, and UPDATE with SQL syntax.
tags:
  - delta-lake
  - dml
  - sql
timestamp: "2026-06-18T11:48:04.144Z"
---

# Delta Lake DML Operations

Delta Lake supports standard data manipulation language (DML) statements to modify data stored in Delta tables. The core DML operations include `DELETE`, `UPDATE`, `MERGE`, and `INSERT`. This page documents the `DELETE FROM` statement in detail; see the linked pages for other operations.

## DELETE FROM

The `DELETE FROM` statement deletes rows that match a predicate. When no predicate is provided, it deletes all rows. This statement is only supported for Delta Lake tables. ^[delete-from-databricks-on-aws.md]

### Syntax

```
[ common_table_expression ]
DELETE FROM table_name [table_alias] [WHERE predicate]
```

^[delete-from-databricks-on-aws.md]

#### Parameters

- **[common table expression (CTE)](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-qry-select-cte)**  
  One or more named queries that can be reused multiple times within the main query block to avoid repeated computations or improve readability of complex, nested queries. ^[delete-from-databricks-on-aws.md]

- **table_name**  
  Identifies an existing Delta table. The name must not include a temporal specification. `table_name` must not be a foreign table. ^[delete-from-databricks-on-aws.md]

- **table_alias**  
  Defines an alias for the table. The alias must not include a column list. ^[delete-from-databricks-on-aws.md]

- **WHERE predicate**  
  Filters rows by predicate. The `WHERE` predicate supports subqueries, including `IN`, `NOT IN`, `EXISTS`, `NOT EXISTS`, and scalar subqueries. The following types of subqueries are *not* supported: ^[delete-from-databricks-on-aws.md]
  - Nested subqueries (a subquery inside another subquery)
  - `NOT IN` subquery inside an `OR`, for example, `a = 3 OR b NOT IN (SELECT c from t)`

In most cases, you can rewrite `NOT IN` subqueries using `NOT EXISTS`. Databricks recommends using `NOT EXISTS` whenever possible, as `DELETE` with `NOT IN` subqueries can be slow. ^[delete-from-databricks-on-aws.md]

### Examples

```sql
-- Delete all events before 2017-01-01
DELETE FROM events WHERE date < '2017-01-01';

-- Delete rows based on a scalar subquery
DELETE FROM all_events
  WHERE session_time < (SELECT min(session_time) FROM good_events);

-- Delete using EXISTS
DELETE FROM orders AS t1
  WHERE EXISTS (SELECT oid FROM returned_orders WHERE t1.oid = oid);

-- Delete using NOT IN (slower than NOT EXISTS)
DELETE FROM events
  WHERE category NOT IN (SELECT category FROM events2 WHERE date > '2001-01-01');
```

^[delete-from-databricks-on-aws.md]

### Notes

- `DELETE FROM` is a Delta Lake–only operation; it does not apply to foreign tables or non-Delta tables.
- The `WHERE` predicate can reference subqueries from other tables, enabling complex row deletions.
- For performance reasons, avoid `NOT IN` subqueries in `DELETE` statements and prefer `NOT EXISTS`.

## Related DML Statements

Delta Lake also supports the following DML operations, each described in its own page:

- UPDATE – Modify existing rows.
- [MERGE INTO](/concepts/merge-into-delta-lake.md) – Upsert data (insert or update) based on a condition.
- INSERT INTO – Add new rows to a table.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The storage layer that provides ACID transactions and scalable metadata handling.
- Temporal Specification – Used to query table snapshots at specific points in time.
- [Common Table Expression (CTE)](/concepts/common-table-expressions-cte-in-dml.md) – Named subqueries that improve readability and reuse.

## Sources

- delete-from-databricks-on-aws.md

# Citations

1. [delete-from-databricks-on-aws.md](/references/delete-from-databricks-on-aws-ab1d0768.md)
