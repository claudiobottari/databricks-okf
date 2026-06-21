---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a51bd88075f1eb551a3cf041094dee2dc0f4ed850771f83972452959fe8dccbd
  pageDirectory: concepts
  sources:
    - delete-from-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - delta-lake-dml-statements
    - DLDS
    - Delta Lake statements
    - DELETE FROM statement
    - DML Statements
    - Delta Lake`s `OVERWRITE` semantics
    - MERGE Statement
    - SQL DML statements
  citations:
    - file: delete-from-databricks-on-aws.md
title: Delta Lake DML statements
description: Set of data modification operations supported on Delta Lake tables, including DELETE, INSERT, MERGE, UPDATE, and COPY INTO.
tags:
  - delta-lake
  - dml
timestamp: "2026-06-18T15:14:34.331Z"
---

# Delta Lake DML Statements

**Delta Lake DML statements** are SQL commands used to modify data stored in [Delta Lake](/concepts/delta-lake.md) tables. Delta Lake supports standard data manipulation language (DML) operations such as `DELETE`, `UPDATE`, `INSERT`, and `MERGE`. This page documents the `DELETE FROM` statement. For other DML statements, see the linked pages.

## DELETE FROM

The `DELETE FROM` statement deletes rows from a [Delta Lake Table](/concepts/delta-lake-table.md) that match an optional predicate. When no predicate is provided, all rows are deleted. This statement is only supported for Delta Lake tables. ^[delete-from-databricks-on-aws.md]

### Syntax

```
[ common_table_expression ]
DELETE FROM table_name [table_alias] [WHERE predicate]
```

^[delete-from-databricks-on-aws.md]

### Parameters

- **common_table_expression** – One or more named queries that can be reused within the main query block to simplify complex logic. ^[delete-from-databricks-on-aws.md]
- **table_name** – Identifies an existing [Delta Lake Table](/concepts/delta-lake-table.md). The name must not include a temporal specification, and the table must not be a foreign table. ^[delete-from-databricks-on-aws.md]
- **table_alias** – An optional alias for the table. The alias must not include a column list. ^[delete-from-databricks-on-aws.md]
- **WHERE** – A predicate that filters which rows to delete. The predicate supports subqueries, including `IN`, `NOT IN`, `EXISTS`, `NOT EXISTS`, and scalar subqueries. ^[delete-from-databricks-on-aws.md]

> **Subquery restrictions:** Nested subqueries (a subquery inside another subquery) and `NOT IN` subqueries inside an `OR` condition are not supported. `NOT IN` subqueries can be slower; using `NOT EXISTS` is recommended when possible. ^[delete-from-databricks-on-aws.md]

### Examples

```sql
-- Delete all rows where date is before 2017-01-01
DELETE FROM events WHERE date < '2017-01-01';

-- Delete rows using a correlated subquery
DELETE FROM all_events
  WHERE session_time < (SELECT min(session_time) FROM good_events);

-- Delete rows using EXISTS
DELETE FROM orders AS t1
  WHERE EXISTS (SELECT oid FROM returned_orders WHERE t1.oid = oid);

-- Delete rows using NOT IN (slower, but acceptable for small datasets)
DELETE FROM events
  WHERE category NOT IN (SELECT category FROM events2 WHERE date > '2001-01-01');
```

^[delete-from-databricks-on-aws.md]

## Related Statements

For other Delta Lake DML operations, see:

- INSERT INTO – Adds new rows to a table.
- UPDATE – Modifies existing rows.
- [MERGE INTO](/concepts/merge-into-delta-lake.md) – Upserts (inserts or updates) rows based on a source.

These statements share the same Delta Lake support and transactional guarantees.

## Sources

- delete-from-databricks-on-aws.md

# Citations

1. [delete-from-databricks-on-aws.md](/references/delete-from-databricks-on-aws-ab1d0768.md)
