---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e4893c97ba0091ced52407e26e2af2ef077b236aea090223b719dac649cc6da7
  pageDirectory: concepts
  sources:
    - delete-from-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - predicate-based-row-deletion
    - PRD
  citations:
    - file: delete-from-databricks-on-aws.md
title: Predicate-based row deletion
description: Core mechanism of DELETE FROM that filters which rows to remove using a WHERE predicate; deleting all rows when no predicate is provided.
tags:
  - delta-lake
  - sql-pattern
timestamp: "2026-06-18T15:14:31.717Z"
---

# Predicate-based Row Deletion

**Predicate-based row deletion** is a data manipulation operation that removes rows from a [Delta Lake](/concepts/delta-lake.md) table when they satisfy a specified filtering condition (predicate). When no predicate is provided, the statement deletes all rows in the table. ^[delete-from-databricks-on-aws.md]

## Syntax

The basic syntax for predicate-based deletion follows this structure:

```
[ common_table_expression ]
DELETE FROM table_name [table_alias] [WHERE predicate]
```

^[delete-from-databricks-on-aws.md]

## Parameters

- **table_name**: Identifies an existing [Delta Lake Table](/concepts/delta-lake-table.md). The name must not include a temporal specification and must not be a foreign table. ^[delete-from-databricks-on-aws.md]
- **table_alias**: Defines an alias for the table, which cannot include a column list. ^[delete-from-databricks-on-aws.md]
- **WHERE predicate**: Filters rows to determine which ones should be deleted. The predicate supports subqueries, including `IN`, `NOT IN`, `EXISTS`, `NOT EXISTS`, and scalar subqueries. ^[delete-from-databricks-on-aws.md]

## WHERE Predicate Support

The `WHERE` clause supports several types of subqueries for complex filtering:

- `IN` and `NOT IN` subqueries
- `EXISTS` and `NOT EXISTS` subqueries
- Scalar subqueries

However, certain subquery patterns are not supported:
- Nested subqueries (a subquery inside another subquery)
- `NOT IN` subqueries within an `OR` expression (e.g., `a = 3 OR b NOT IN (SELECT c from t)`)

In most cases, `NOT IN` subqueries can be rewritten using `NOT EXISTS`. Using `NOT EXISTS` is recommended when possible, as `DELETE` operations with `NOT IN` subqueries can be slow. ^[delete-from-databricks-on-aws.md]

## Common Table Expressions

Common table expressions (CTEs) can be used as part of the delete statement. CTEs are one or more named queries that can be reused multiple times within the main query block to:
- Avoid repeated computations
- Improve readability of complex, nested queries ^[delete-from-databricks-on-aws.md]

## Examples

### Simple Predicate Deletion
```sql
> DELETE FROM events WHERE date < '2017-01-01'
```
^[delete-from-databricks-on-aws.md]

### Subquery-based Deletion
```sql
> DELETE FROM all_events
  WHERE session_time < (
    SELECT min(session_time) FROM good_events
  )
```
^[delete-from-databricks-on-aws.md]

### EXISTS-based Deletion
```sql
> DELETE FROM orders AS t1
  WHERE EXISTS (
    SELECT oid FROM returned_orders WHERE t1.oid = oid
  )
```
^[delete-from-databricks-on-aws.md]

### NOT IN Subquery Deletion
```sql
> DELETE FROM events
  WHERE category NOT IN (
    SELECT category FROM events2 WHERE date > '2001-01-01'
  )
```
^[delete-from-databricks-on-aws.md]

## Related Concepts

- Delta DELETE — The companion operation for updating data in Delta tables
- Delta MERGE — Upsert operation combining insert, update, and delete logic
- Delta UPDATE — Row-level modification without full table replacement
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format supporting these operations
- Delta COPY INTO — Alternative data loading mechanism for bulk ingestion
- INSERT — Adding new rows to a table
- PARTITION — Query optimization for partitioned data
- WHERE Clause — The filtering mechanism used in predicate definitions
- [Common Table Expressions](/concepts/common-table-expressions-cte-in-dml.md) — Named subqueries for complex queries

## Sources

- delete-from-databricks-on-aws.md

# Citations

1. [delete-from-databricks-on-aws.md](/references/delete-from-databricks-on-aws-ab1d0768.md)
