---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ca9fb19e21c43d1103497be33c29fda047ed49122008414c7db2ef98ce0392c3
  pageDirectory: concepts
  sources:
    - delete-from-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - subquery-restrictions-in-dml-statements
    - SRIDS
    - Subqueries in DML
  citations:
    - file: delete-from-databricks-on-aws.md
title: Subquery Restrictions in DML Statements
description: DELETE and other DML statements in Databricks SQL forbid nested subqueries and NOT IN subqueries inside OR expressions.
tags:
  - sql
  - subqueries
  - dml
  - limitations
timestamp: "2026-06-18T11:48:01.845Z"
---

# Subquery Restrictions in DML Statements

**Subquery Restrictions in DML Statements** refers to the limitations on which types of subqueries can be used within `DELETE`, `UPDATE`, and `MERGE` statements on Delta Lake tables in Databricks. Understanding these restrictions is essential for writing valid and performant data modification queries.

## Supported Subquery Types

DML statements support the following subquery types in the `WHERE` predicate:

- `IN` subqueries
- `NOT IN` subqueries
- `EXISTS` subqueries
- `NOT EXISTS` subqueries
- Scalar subqueries

^[delete-from-databricks-on-aws.md]

## Unsupported Subquery Types

### Nested Subqueries

Subqueries inside another subquery are not supported in DML statements. For example, the following pattern is not allowed:

```sql
DELETE FROM table1
WHERE column1 IN (SELECT column2 FROM table2 WHERE column3 IN (SELECT column4 FROM table3));
```

^[delete-from-databricks-on-aws.md]

### NOT IN Subquery Inside an OR Condition

A `NOT IN` subquery cannot appear inside an `OR` expression. The following pattern is not supported:

```sql
DELETE FROM table1
WHERE a = 3 OR b NOT IN (SELECT c FROM table2);
```

^[delete-from-databricks-on-aws.md]

## Performance Considerations

When using `NOT IN` subqueries in `DELETE` statements, performance can be slow. In most cases, you can rewrite `NOT IN` subqueries using `NOT EXISTS`, which is the recommended approach for better performance. ^[delete-from-databricks-on-aws.md]

### Example: Rewriting NOT IN as NOT EXISTS

Instead of:

```sql
DELETE FROM events
WHERE category NOT IN (SELECT category FROM events2 WHERE date > '2001-01-01');
```

Use:

```sql
DELETE FROM events AS t1
WHERE NOT EXISTS (SELECT 1 FROM events2 WHERE t1.category = events2.category AND events2.date > '2001-01-01');
```

^[delete-from-databricks-on-aws.md]

## Examples of Valid Subquery Usage

The following examples demonstrate supported subquery patterns in `DELETE` statements:

```sql
-- Scalar subquery
DELETE FROM all_events
WHERE session_time < (SELECT min(session_time) FROM good_events);

-- EXISTS subquery
DELETE FROM orders AS t1
WHERE EXISTS (SELECT oid FROM returned_orders WHERE t1.oid = oid);

-- NOT EXISTS subquery (recommended over NOT IN)
DELETE FROM events AS t1
WHERE NOT EXISTS (SELECT 1 FROM events2 WHERE t1.category = events2.category AND events2.date > '2001-01-01');

-- IN subquery
DELETE FROM events WHERE category IN (SELECT category FROM events2 WHERE date > '2001-01-01');
```

^[delete-from-databricks-on-aws.md]

## Scope

These restrictions apply to all DML statements on Delta Lake tables, including:

- [DELETE FROM](/concepts/delete-from-delta-lake.md)
- UPDATE
- [MERGE INTO](/concepts/merge-into-delta-lake.md)

The restrictions are specific to the `WHERE` predicate of these statements and do not apply to general `SELECT` queries. ^[delete-from-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer that supports these DML operations
- [DELETE FROM](/concepts/delete-from-delta-lake.md) — The DML statement for removing rows
- UPDATE — The DML statement for modifying rows
- [MERGE INTO](/concepts/merge-into-delta-lake.md) — The DML statement for upsert operations
- Subqueries — General subquery syntax and usage
- [Common Table Expressions (CTEs)](/concepts/common-table-expressions-ctes-in-dml.md) — Named queries that can be used in DML statements

## Sources

- delete-from-databricks-on-aws.md

# Citations

1. [delete-from-databricks-on-aws.md](/references/delete-from-databricks-on-aws-ab1d0768.md)
