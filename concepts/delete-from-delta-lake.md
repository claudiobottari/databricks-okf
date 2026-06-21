---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ec425fd9968a6250c2a281958faaa4418971cec48b4c214291b798f266b7d724
  pageDirectory: concepts
  sources:
    - delete-from-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delete-from-delta-lake
    - DF(L
    - DELETE (Delta Lake)
    - DELETE (Delta)
    - DELETE FROM
  citations:
    - file: delete-from-databricks-on-aws.md
title: DELETE FROM (Delta Lake)
description: SQL statement to delete rows from Delta Lake tables, optionally filtered by a predicate
tags:
  - sql
  - delta-lake
  - dml
timestamp: "2026-06-19T18:19:37.561Z"
---

```markdown
---
title: DELETE FROM (Delta Lake)
summary: A DML statement for deleting rows from Delta Lake tables, optionally filtered by a predicate.
sources:
  - delete-from-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:47:53.191Z"
updatedAt: "2026-06-18T11:47:53.191Z"
tags:
  - delta-lake
  - dml
  - sql
aliases:
  - delete-from-delta-lake
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# DELETE FROM (Delta Lake)

**DELETE FROM** is a DML statement that removes rows from a [[Delta Lake]] table based on an optional predicate. When no predicate is provided, the statement deletes all rows. This statement is only supported for Delta Lake tables. ^[delete-from-databricks-on-aws.md]

## Syntax

```sql
[ common_table_expression ]
DELETE FROM table_name [table_alias] [WHERE predicate]
```

^[delete-from-databricks-on-aws.md]

## Parameters

### common_table_expression

One or more named queries ([Common Table Expressions](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-qry-select-cte)) that can be reused multiple times within the main query block. CTEs improve readability and avoid repeated computations in complex, nested queries. They must be defined before the `DELETE FROM` clause. ^[delete-from-databricks-on-aws.md]

### table_name

Identifies an existing [[delta-lake-table|Delta Lake Table]]. The name must not include a temporal specification, and it must not be a foreign table. ^[delete-from-databricks-on-aws.md]

### table_alias

Defines an alias for the table. The alias must not include a column list. ^[delete-from-databricks-on-aws.md]

### WHERE predicate

Filters rows to delete. The predicate supports subqueries, including `IN`, `NOT IN`, `EXISTS`, `NOT EXISTS`, and scalar subqueries. The following types of subqueries are **not** supported: ^[delete-from-databricks-on-aws.md]

- Nested subqueries – a subquery inside another subquery.
- `NOT IN` subquery inside an `OR` expression – for example, `a = 3 OR b NOT IN (SELECT c FROM t)`.

In most cases, you can rewrite `NOT IN` subqueries using `NOT EXISTS`. Databricks recommends using `NOT EXISTS` whenever possible, as `DELETE` with `NOT IN` subqueries can be slow. ^[delete-from-databricks-on-aws.md]

## Examples

### Delete all rows older than a date

```sql
DELETE FROM events WHERE date < '2017-01-01';
```

^[delete-from-databricks-on-aws.md]

### Delete rows based on a scalar subquery

```sql
DELETE FROM all_events
  WHERE session_time < (SELECT min(session_time) FROM good_events);
```

^[delete-from-databricks-on-aws.md]

### Delete rows using EXISTS

```sql
DELETE FROM orders AS t1
  WHERE EXISTS (SELECT oid FROM returned_orders WHERE t1.oid = oid);
```

^[delete-from-databricks-on-aws.md]

### Delete rows using NOT IN

```sql
DELETE FROM events
  WHERE category NOT IN (SELECT category FROM events2 WHERE date > '2001-01-01');
```

^[delete-from-databricks-on-aws.md]

## Related Concepts

- [[Delta Lake]] – The storage layer that supports `DELETE FROM`.
- [[MERGE INTO (Delta Lake)]] – Combines insert, update, and delete in one operation.
- [[UPDATE Statement (Delta Lake)|UPDATE (Delta Lake)]] – Updates rows in a Delta table.
- INSERT INTO (Delta Lake) – Adds new rows.
- [[Common Table Expressions (CTE) in DML|Common Table Expression (CTE)]] – Reusable named queries.
- Temporal Table Specification – Not allowed in the table name for `DELETE`.

## Sources

- delete-from-databricks-on-aws.md
```

# Citations

1. [delete-from-databricks-on-aws.md](/references/delete-from-databricks-on-aws-ab1d0768.md)
