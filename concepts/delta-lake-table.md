---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9251be6ee3d75a98084f516818235d4d11b9d810383f878f91c77a4399a268f7
  pageDirectory: concepts
  sources:
    - update-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-table
    - DLT
    - Delta Lake Table State
    - Delta Lake table properties|table property
    - Delta Table
    - Delta Tables
    - Delta table
    - Delta tables
    - Delta tables for traces
    - Delta table|Delta format
    - Upsert into a Delta Lake table using merge
  citations:
    - file: update-databricks-on-aws.md
title: Delta Lake Table
description: The storage format required for UPDATE, DELETE, and MERGE operations in Databricks; standard tables do not support UPDATE.
tags:
  - delta-lake
  - storage-format
timestamp: "2026-06-19T23:16:09.855Z"
---

# [Delta Lake](/concepts/delta-lake.md) Table

A **Delta Lake table** is the only table type in Databricks that supports the `UPDATE` data modification statement. All `UPDATE` operations require the target table to be a [Delta Lake](/concepts/delta-lake.md) table. ^[update-databricks-on-aws.md]

## Characteristics

- [Delta Lake](/concepts/delta-lake.md) tables allow updating column values for rows that match a predicate. When no predicate is provided, all rows in the table are updated. ^[update-databricks-on-aws.md]
- The `UPDATE` statement supports `SET` clauses that assign expressions or the `DEFAULT` value to columns or struct fields. The `DEFAULT` keyword (available in Databricks SQL and Databricks Runtime 11.3 LTS and above) inserts the column’s default value if defined, otherwise `NULL`. ^[update-databricks-on-aws.md]
- A `WHERE` clause can filter rows by predicate and may include subqueries, with the restriction that nested subqueries are not allowed and `NOT IN` subqueries cannot appear inside an `OR` condition. Using `NOT EXISTS` is recommended over `NOT IN` for better performance. ^[update-databricks-on-aws.md]
- [Delta Lake](/concepts/delta-lake.md) tables support [common table expressions (CTEs)](/concepts/common-table-expressions-ctes-in-dml.md) within the `UPDATE` statement for reusable named queries. ^[update-databricks-on-aws.md]

## Limitations

- The table name in an `UPDATE` statement must not use a `temporal specification` or `options specification`, and the table must not be a foreign table. ^[update-databricks-on-aws.md]
- Databricks SQL does **not** support the `UPDATE ... FROM ... JOIN` syntax used in some other SQL dialects. To update a [Delta Lake](/concepts/delta-lake.md) table based on a join with another table or subquery, use [MERGE INTO](/concepts/merge-into-delta-lake.md) instead. ^[update-databricks-on-aws.md]

## Examples

The following examples update a [Delta Lake](/concepts/delta-lake.md) table named `events`:

```sql
-- Update all rows with a simple condition
UPDATE events SET eventType = 'click' WHERE eventType = 'clk';

-- Update using a subquery
UPDATE all_events
  SET session_time = 0, ignored = true
WHERE session_time < (SELECT min(session_time) FROM good_events);

-- Update using EXISTS subquery
UPDATE orders AS t1
  SET order_status = 'returned'
WHERE EXISTS (SELECT oid FROM returned_orders WHERE t1.oid = oid);

-- Update using NOT IN (prefer NOT EXISTS)
UPDATE events
  SET category = 'undefined'
WHERE category NOT IN (SELECT category FROM events2 WHERE date > '2001-01-01');

-- Set column to its default value
UPDATE events
  SET ignored = DEFAULT
WHERE eventType = 'unknown';
```

To update a table from a join, use `MERGE INTO` instead of the unsupported `UPDATE ... FROM ... JOIN`:

```sql
MERGE INTO t1
USING t2 ON t1.c2 = t2.c2
WHEN MATCHED THEN UPDATE SET t1.c1 = t2.c1;
```

^[update-databricks-on-aws.md]

## Related Concepts

- UPDATE – The SQL statement supported only on [Delta Lake](/concepts/delta-lake.md) tables.
- [MERGE INTO](/concepts/merge-into-delta-lake.md) – The recommended alternative for updating via joins.
- DELETE – Another DML operation supported on [Delta Lake](/concepts/delta-lake.md) tables.
- INSERT – Data insertion into [Delta Lake](/concepts/delta-lake.md) tables.
- [Common Table Expressions](/concepts/common-table-expressions-cte-in-dml.md) – Reusable named queries usable in UPDATE statements.
- [Delta Lake](/concepts/delta-lake.md) – The underlying open‑source storage layer that provides ACID transactions and schema enforcement.

## Sources

- update-databricks-on-aws.md

# Citations

1. [update-databricks-on-aws.md](/references/update-databricks-on-aws-8f0bcd2b.md)
