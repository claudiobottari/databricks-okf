---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8dd96596bedf67392066c809f05497e93e5e2d32dfbad398b2d35374f399900b
  pageDirectory: concepts
  sources:
    - delete-from-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - table-aliases-in-databricks-dml-statements
    - TAIDDS
    - Databricks DML statements
  citations:
    - file: delete-from-databricks-on-aws.md
title: Table aliases in Databricks DML statements
description: Databricks SQL allows defining a table alias in DELETE FROM statements, but the alias must not include a column list, enabling clearer references in subqueries and complex predicates.
tags:
  - syntax
  - dml
  - databricks-sql
timestamp: "2026-06-19T09:59:15.985Z"
---

# Table aliases in Databricks DML statements

**Table aliases** in [Databricks DML statements](/concepts/table-aliases-in-databricks-dml-statements.md) provide a shorthand name for a table within a Data Manipulation Language (DML) statement. They are particularly useful in subqueries, self-joins, and correlated subqueries to avoid ambiguity and improve readability. ^[delete-from-databricks-on-aws.md]

## Syntax in DELETE FROM

Table aliases are supported in the `DELETE FROM` statement. The alias is placed directly after the table name, optionally preceded by the `AS` keyword. ^[delete-from-databricks-on-aws.md]

```sql
DELETE FROM table_name [table_alias] [WHERE predicate]
DELETE FROM table_name [AS] table_alias [WHERE predicate]
```

## Parameters

- **table_alias**: A temporary name assigned to the table for the duration of the statement. The alias must not include a column list. ^[delete-from-databricks-on-aws.md]

## Usage examples

The following examples from the Databricks documentation demonstrate table aliases in `DELETE FROM`: ^[delete-from-databricks-on-aws.md]

```sql
-- Simple deletion with alias
DELETE FROM events AS e WHERE e.date < '2017-01-01';

-- Using alias in a correlated subquery
DELETE FROM orders AS t1
  WHERE EXISTS (SELECT oid FROM returned_orders WHERE t1.oid = oid);

-- Deletion with a subquery (no alias necessary)
DELETE FROM all_events
  WHERE session_time < (SELECT min(session_time) FROM good_events);
```

## Related Concepts

- [DELETE FROM](/concepts/delete-from-delta-lake.md) – The DML statement that supports table aliases.
- [DML Statements](/concepts/delta-lake-dml-statements.md) – Overview of Data Manipulation Language in Databricks.
- Table Alias – General SQL concept.
- [Subqueries in DML](/concepts/subquery-restrictions-in-dml-statements.md) – Using subqueries with `WHERE` predicates.
- [UPDATE and MERGE](/concepts/update-set-and-insert-with-except.md) – Other DML statements that may support aliases (check individual documentation).

## Sources

- delete-from-databricks-on-aws.md

# Citations

1. [delete-from-databricks-on-aws.md](/references/delete-from-databricks-on-aws-ab1d0768.md)
