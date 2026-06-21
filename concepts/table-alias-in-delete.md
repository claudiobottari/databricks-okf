---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d94b1a435e17e2689ea00d6fb9f2c74982379116d9684b4399e571f70494729d
  pageDirectory: concepts
  sources:
    - delete-from-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - table-alias-in-delete
    - TAID
  citations:
    - file: delete-from-databricks-on-aws.md
title: Table alias in DELETE
description: DELETE FROM supports an optional table alias that must not include a column list, used to reference the target table in subqueries.
tags:
  - delta-lake
  - sql-syntax
timestamp: "2026-06-18T15:14:47.913Z"
---

# Table alias in DELETE

A **table alias in DELETE** is a temporary name assigned to the target table of a `DELETE FROM` statement. It allows the statement to refer to the table by a short or disambiguating name, particularly when the `WHERE` clause contains correlated subqueries.

## Syntax

```
DELETE FROM table_name [table_alias] [WHERE predicate]
```

The alias, if supplied, follows the table name and may be introduced by the optional `AS` keyword. ^[delete-from-databricks-on-aws.md]

## Parameters

### table_alias

Defines an alias for the table. The alias must not include a column list. ^[delete-from-databricks-on-aws.md]

- When present, the alias can be used to reference the target table inside the `WHERE` predicate, including in correlated subqueries.
- The alias is optional; if omitted, the table’s original name is used throughout the statement.

## Usage

The table alias is most useful when the `WHERE` clause contains a subquery that references the same table as the `DELETE` target. Without an alias, the subquery might become ambiguous or self-referential. For example, the following uses the alias `t1` to link the subquery’s `oid` column with the target table’s `oid` column:

```sql
DELETE FROM orders AS t1
  WHERE EXISTS (SELECT oid FROM returned_orders WHERE t1.oid = oid);
```

This statement deletes rows from `orders` where a matching `oid` exists in `returned_orders`. The alias `t1` makes the correlation explicit. ^[delete-from-databricks-on-aws.md]

The alias is also supported in the standard `DELETE` syntax for Delta Lake tables, alongside common table expressions (CTEs) and any valid `WHERE` predicate (including `IN`, `NOT IN`, `EXISTS`, `NOT EXISTS`, and scalar subqueries). ^[delete-from-databricks-on-aws.md]

## Restrictions

- The alias must not contain a column list (e.g., `t1(c1, c2)` is not allowed).
- The table name must not include a temporal specification (time travel syntax).
- The statement is only supported for [Delta Lake](/concepts/delta-lake.md) tables; foreign tables are not allowed. ^[delete-from-databricks-on-aws.md]

## Examples

Delete all rows from an aliased table (no predicate):

```sql
DELETE FROM events AS e;
```

Delete rows using a correlated `EXISTS` subquery:

```sql
DELETE FROM orders AS t1
  WHERE EXISTS (SELECT oid FROM returned_orders WHERE t1.oid = oid);
```

Delete rows using a `NOT IN` subquery:

```sql
DELETE FROM events
  WHERE category NOT IN (SELECT category FROM events2 WHERE date > '2001-01-01');
```

(The last example does not use an alias because the subquery references a different table; an alias is optional when no self‑reference is needed.) ^[delete-from-databricks-on-aws.md]

## Related Concepts

- [DELETE FROM](/concepts/delete-from-delta-lake.md) — The full statement syntax and parameters.
- [Delta Lake](/concepts/delta-lake.md) — The storage engine that supports the `DELETE` statement.
- Correlated Subquery — A pattern where the table alias is commonly used.
- Table Alias — General use of aliases in SQL queries.

## Sources

- delete-from-databricks-on-aws.md

# Citations

1. [delete-from-databricks-on-aws.md](/references/delete-from-databricks-on-aws-ab1d0768.md)
