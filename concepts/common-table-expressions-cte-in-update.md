---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ce17ee2099e56aef1cc1ed75629ad26b8d6dc3f448822accd41b9982fd45dbe9
  pageDirectory: concepts
  sources:
    - update-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - common-table-expressions-cte-in-update
    - CTE(IU
  citations:
    - file: update-databricks-on-aws.md
title: Common Table Expressions (CTE) in UPDATE
description: Named queries that can be reused within the UPDATE statement to avoid repeated computations or improve readability.
tags:
  - sql
  - cte
  - query-optimization
timestamp: "2026-06-19T23:16:23.568Z"
---

# Common Table Expressions (CTE) in UPDATE

**Common Table Expressions (CTE) in UPDATE** allow you to define one or more named subqueries that can be reused within the `UPDATE` statement, simplifying complex update logic and avoiding repeated computation. Databricks SQL and Databricks Runtime support CTEs in the `UPDATE` statement for [Delta Lake](/concepts/delta-lake.md) tables. ^[update-databricks-on-aws.md]

## Syntax[​](#syntax "Direct link to Syntax")

```sql
[ common_table_expression ]  UPDATE table_name [table_alias]
    SET  { { column_name | field_name }  = [ expr | DEFAULT } [, ...]
    [WHERE clause]
```

The `common_table_expression` clause is optional and appears before the `UPDATE` keyword. ^[update-databricks-on-aws.md]

## Parameters[​](#parameters "Direct link to Parameters")

- **common_table_expression**  
  One or more named queries that can be referenced by name within the `UPDATE`, `SET`, or `WHERE` clauses. CTEs improve readability and performance when the same subquery result is needed multiple times. ^[update-databricks-on-aws.md]

- **table_name**  
  The Delta table to update. Must not include a temporal or options specification, and must not be a foreign table. ^[update-databricks-on-aws.md]

- **table_alias**  
  An alias for the table. Must not include a column list. ^[update-databricks-on-aws.md]

- **column_name / field_name**  
  Columns or fields (of type `STRUCT`) to update. Each can appear only once in the `SET` clause. ^[update-databricks-on-aws.md]

- **expr**  
  An arbitrary expression; references to the table’s columns represent the row state prior to the update. ^[update-databricks-on-aws.md]

- **DEFAULT**  
  Sets the column to its default value (if defined) or `NULL`. Supported in Databricks Runtime 11.3 LTS and above. ^[update-databricks-on-aws.md]

- **WHERE clause**  
  Filters rows by predicate. Supports subqueries but not nested subqueries, `NOT IN` inside an `OR`, or `NOT IN` subqueries (which can often be rewritten with `NOT EXISTS` for better performance). ^[update-databricks-on-aws.md]

## Usage[​](#usage "Direct link to Usage")

CTEs are defined using the `WITH` keyword (standard SQL) and can be placed directly before the `UPDATE` statement. For example:

```sql
WITH cte AS (
  SELECT oid, status FROM returned_orders WHERE status = 'approved'
)
UPDATE orders AS t1
SET order_status = 'returned'
WHERE EXISTS (SELECT 1 FROM cte WHERE t1.oid = cte.oid);
```

CTEs are especially useful when the same subquery is referenced multiple times in the `WHERE` clause or when building complex update logic that would otherwise require nested subqueries. ^[update-databricks-on-aws.md]

## Limitations[​](#limitations "Direct link to Limitations")

- The `UPDATE` statement is only supported for [Delta Lake](/concepts/delta-lake.md) tables. ^[update-databricks-on-aws.md]
- `UPDATE ... FROM ... JOIN` syntax is not supported; use [MERGE INTO](/concepts/merge-into-delta-lake.md) instead for updates based on joins with other tables or subqueries. ^[update-databricks-on-aws.md]
- Subqueries in the `WHERE` clause have restrictions on nesting and `NOT IN` usage (see Parameters above). ^[update-databricks-on-aws.md]

## Related Concepts[​](#related-concepts "Direct link to Related Concepts")

- [Common Table Expression (CTE)](/concepts/common-table-expressions-cte-in-dml.md) – General SQL CTE syntax and behavior.
- [MERGE INTO](/concepts/merge-into-delta-lake.md) – Recommended alternative for updating from a join.
- DELETE – Deleting rows with CTE support.
- INSERT – Inserting data with CTE support.
- [Delta Lake](/concepts/delta-lake.md) – The storage layer that supports this `UPDATE` syntax.
- Databricks SQL – Execution environment for CTE‑based `UPDATE`.

## Sources[​](#sources "Direct link to Sources")

- update-databricks-on-aws.md

# Citations

1. [update-databricks-on-aws.md](/references/update-databricks-on-aws-8f0bcd2b.md)
