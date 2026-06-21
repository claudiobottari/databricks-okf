---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 22a21657486edec06fb5d4977155bba57b5e4061abf4403d335a084e9cb89ddb
  pageDirectory: concepts
  sources:
    - update-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - update-statement-delta-lake
    - US(L
    - UPDATE (Delta Lake)
    - UPDATE (Delta)
    - UPDATE Statement
    - UPDATE statement
  citations:
    - file: update-databricks-on-aws.md
title: UPDATE Statement (Delta Lake)
description: SQL statement to update column values in Delta Lake tables, optionally filtered by a predicate using WHERE clause.
tags:
  - delta-lake
  - sql
  - dml
timestamp: "2026-06-19T23:15:49.204Z"
---

# UPDATE Statement ([Delta Lake](/concepts/delta-lake.md))

The **`UPDATE` statement** in [Delta Lake](/concepts/delta-lake.md) modifies column values for rows that match a specified predicate. When no predicate is provided, the statement updates column values for all rows. This statement is supported only for [Delta Lake](/concepts/delta-lake.md) tables. ^[update-databricks-on-aws.md]

## Syntax

```sql
[ common_table_expression ]
UPDATE table_name [table_alias]
    SET { { column_name | field_name } = [ expr | DEFAULT } [, ...]
    [WHERE clause]
```

The `UPDATE` statement may be preceded by one or more common table expressions (CTEs), allowing named subqueries to be reused within the main query. ^[update-databricks-on-aws.md]

## Parameters

- **common_table_expression**  
  One or more named queries defined using the `WITH` clause. CTEs improve readability and avoid repeated computation in complex queries. ^[update-databricks-on-aws.md]

- **table_name**  
  Identifies the Delta table to be updated. The table name must not include a temporal or options specification. `table_name` must not be a foreign table. ^[update-databricks-on-aws.md]

- **table_alias**  
  An alias for the table, without a column list. ^[update-databricks-on-aws.md]

- **column_name**  
  A reference to a column in the table. Each column may be referenced at most once. ^[update-databricks-on-aws.md]

- **field_name**  
  A reference to a field within a column of type `STRUCT`. Each field may be referenced at most once. ^[update-databricks-on-aws.md]

- **expr**  
  An arbitrary expression. If the expression references columns of the table, they represent the state of each row prior to the update. ^[update-databricks-on-aws.md]

- **DEFAULT**  
  Applies to Databricks SQL and Databricks Runtime 11.3 LTS and above. Uses the column’s default value if one is defined, otherwise `NULL`. ^[update-databricks-on-aws.md]

- **WHERE clause**  
  Filters rows by a predicate. The predicate may include subqueries, with the following restrictions:  
  - Nested subqueries (a subquery inside another subquery) are not allowed.  
  - A `NOT IN` subquery inside an `OR` condition is not allowed (for example, `a = 3 OR b NOT IN (SELECT c FROM t)`).  

  In most cases, `NOT IN` subqueries can be rewritten using `NOT EXISTS`. Databricks recommends using `NOT EXISTS` wherever possible, as `UPDATE` with `NOT IN` subqueries can be slow. ^[update-databricks-on-aws.md]

## Updating from Another Table or Join

Databricks SQL does not support the `UPDATE ... FROM ... JOIN` syntax found in some other SQL dialects. To update a table based on a join with another table or subquery, use [MERGE INTO|MERGE INTO](/concepts/merge-into-delta-lake.md) instead. ^[update-databricks-on-aws.md]

### Equivalent MERGE example

```sql
-- Instead of (unsupported): UPDATE t1 SET t1.c1 = t2.c1 FROM t1 INNER JOIN t2 ON t1.c2 = t2.c2

MERGE INTO t1
USING t2 ON t1.c2 = t2.c2
WHEN MATCHED THEN UPDATE SET t1.c1 = t2.c1;
```

## Examples

Update a single column based on a condition:

```sql
UPDATE events SET eventType = 'click' WHERE eventType = 'clk';
```

Update multiple columns using a subquery:

```sql
UPDATE all_events
    SET session_time = 0, ignored = true
  WHERE session_time < (SELECT min(session_time) FROM good_events);
```

Update using `EXISTS`:

```sql
UPDATE orders AS t1
    SET order_status = 'returned'
  WHERE EXISTS (SELECT oid FROM returned_orders WHERE t1.oid = oid);
```

Update using `NOT IN` (note the performance concern):

```sql
UPDATE events
    SET category = 'undefined'
  WHERE category NOT IN (SELECT category FROM events2 WHERE date > '2001-01-01');
```

Update using `DEFAULT`:

```sql
UPDATE events
    SET ignored = DEFAULT
  WHERE eventType = 'unknown';
```

## Related Concepts

- [MERGE INTO](/concepts/merge-into-delta-lake.md) — The recommended way to perform updates based on joins or from another table.
- DELETE Statement (Delta Lake)
- INSERT INTO
- [Common Table Expression (CTE)](/concepts/common-table-expressions-cte-in-dml.md)
- Delta Lake SQL Reference
- [Delta Lake Transactions](/concepts/delta-acid-transactions.md)

## Sources

- update-databricks-on-aws.md

# Citations

1. [update-databricks-on-aws.md](/references/update-databricks-on-aws-8f0bcd2b.md)
