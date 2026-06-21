---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4f6ed7438a21b5b579a80e146c73b18cfcf937978e00f68b6673b3e1ff268a53
  pageDirectory: concepts
  sources:
    - delete-from-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-on-databricks-sql
    - DLODS
  citations:
    - file: delete-from-databricks-on-aws.md
title: Delta Lake on Databricks SQL
description: Databricks SQL and Databricks Runtime support for Delta Lake DELETE operations with full SQL DML semantics.
tags:
  - databricks
  - sql
  - delta-lake
timestamp: "2026-06-19T14:59:01.115Z"
---

# Delta Lake on Databricks SQL

**Delta Lake on Databricks SQL** refers to the ability to use standard SQL DML statements to manipulate data stored in Delta Lake tables. Databricks SQL natively supports Delta Lake as its storage format, providing ACID transactions, schema enforcement, and time travel capabilities through familiar SQL syntax. ^[delete-from-databricks-on-aws.md]

## DELETE FROM Statement

One of the core DML operations supported for Delta Lake tables is the `DELETE FROM` statement. This statement deletes rows that match a predicate. When no predicate is provided, it deletes all rows. The statement is **only supported for Delta Lake tables**; it cannot be used on foreign tables or other storage formats directly. ^[delete-from-databricks-on-aws.md]

### Syntax

```sql
[ common_table_expression ]
DELETE FROM table_name [table_alias] [WHERE predicate]
```

^[delete-from-databricks-on-aws.md]

### Parameters

- **common table expression (CTE):** One or more named queries that can be reused multiple times within the main query block. CTEs help avoid repeated computations and improve readability of complex, nested queries. ^[delete-from-databricks-on-aws.md]
- **table_name:** Identifies an existing [Delta Lake Table](/concepts/delta-lake-table.md). The name must not include a temporal specification. It must not be a foreign table. ^[delete-from-databricks-on-aws.md]
- **table_alias:** Defines an alias for the table. The alias must not include a column list. ^[delete-from-databricks-on-aws.md]
- **WHERE predicate:** Filters rows by a predicate. The predicate supports subqueries, including `IN`, `NOT IN`, `EXISTS`, `NOT EXISTS`, and scalar subqueries. The following types of subqueries are **not supported**:
  - Nested subqueries (a subquery inside another subquery)
  - A `NOT IN` subquery inside an `OR` clause (e.g., `a = 3 OR b NOT IN (SELECT c from t)`)
  - In most cases, you can rewrite `NOT IN` subqueries using `NOT EXISTS`. Databricks recommends using `NOT EXISTS` whenever possible, as `DELETE` with `NOT IN` subqueries can be slow. ^[delete-from-databricks-on-aws.md]

### Examples

```sql
-- Delete all events before 2017-01-01
DELETE FROM events WHERE date < '2017-01-01';

-- Delete all events whose session_time is less than the minimum session_time in good_events
DELETE FROM all_events
  WHERE session_time < (SELECT min(session_time) FROM good_events);

-- Use EXISTS to delete orders that have a matching returned order
DELETE FROM orders AS t1
  WHERE EXISTS (SELECT oid FROM returned_orders WHERE t1.oid = oid);

-- Use NOT IN with a correlated subquery (consider rewriting with NOT EXISTS)
DELETE FROM events
  WHERE category NOT IN (SELECT category FROM events2 WHERE date > '2001-01-01');
```

^[delete-from-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The underlying storage layer providing ACID transactions and scalable metadata handling.
- Databricks SQL – The SQL analytics environment that supports Delta Lake tables.
- [MERGE INTO](/concepts/merge-into-delta-lake.md) – Another DML statement that can perform upserts and deletes conditionally.
- INSERT INTO – DML statement to add rows to Delta Lake tables.
- UPDATE – DML statement to modify existing rows in Delta Lake tables.
- [Common Table Expression (CTE)](/concepts/common-table-expressions-cte-in-dml.md) – Reusable named queries in SQL.

## Sources

- delete-from-databricks-on-aws.md

# Citations

1. [delete-from-databricks-on-aws.md](/references/delete-from-databricks-on-aws-ab1d0768.md)
