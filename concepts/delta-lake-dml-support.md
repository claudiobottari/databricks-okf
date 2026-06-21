---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8d7c16a075f7f09a5b9df04ba7af9ee117e9bbb8319cdde7f6ddf8b64bee6ad9
  pageDirectory: concepts
  sources:
    - delete-from-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-dml-support
    - DLDS
  citations:
    - file: delete-from-databricks-on-aws.md
title: Delta Lake DML Support
description: DELETE FROM is only supported for Delta Lake tables in Databricks, not other table formats
tags:
  - delta-lake
  - dml
  - databricks
timestamp: "2026-06-19T18:19:51.959Z"
---

# Delta Lake DML Support

**Delta Lake DML Support** refers to the ability to execute standard Data Manipulation Language (DML) operations — `DELETE`, `UPDATE`, `MERGE`, and `INSERT` — against [Delta Lake](/concepts/delta-lake.md) tables on Databricks. These operations enable row-level modifications while maintaining Delta Lake's transactional guarantees, including atomicity, versioning, and [time travel](/concepts/delta-lake-time-travel.md) capabilities.

## Overview

Delta Lake supports the standard [SQL DML statements](/concepts/delta-lake-dml-statements.md) (`DELETE`, `UPDATE`, `MERGE`, and `INSERT`) for modifying data in Delta tables. These operations are fully transactional: each DML statement creates a new version of the table, allowing users to roll back changes or query historical snapshots of the data. ^[delete-from-databricks-on-aws.md]

## Supported DML Statements

### DELETE FROM

The `DELETE FROM` statement removes rows that match a given predicate from a Delta table. If no predicate is provided, the statement deletes all rows in the table. The syntax is:

```sql
DELETE FROM table_name [table_alias] [WHERE predicate]
```

^[delete-from-databricks-on-aws.md]

The `WHERE` clause supports subqueries, including `IN`, `NOT IN`, `EXISTS`, `NOT EXISTS`, and scalar subqueries. However, the following subquery types are not supported:

- Nested subqueries (a subquery inside another subquery)
- `NOT IN` subquery inside an `OR` clause (e.g., `a = 3 OR b NOT IN (SELECT c FROM t)`)

In most cases, `NOT IN` subqueries can be rewritten using `NOT EXISTS`. Using `NOT EXISTS` is recommended whenever possible, as `DELETE` with `NOT IN` subqueries can be slow.

Common table expressions ([CTE](/concepts/common-table-expressions-cte-with-delete.md)) can precede the `DELETE FROM` statement to define named queries that can be reused within the main query block. ^[delete-from-databricks-on-aws.md]

The `table_name` must identify an existing [Delta table](/concepts/delta-lake-table.md) and must not include a temporal specification. It must not be a foreign table. An optional table alias can be provided without a column list. ^[delete-from-databricks-on-aws.md]

**Examples:**

```sql
-- Delete all events before 2017
DELETE FROM events WHERE date < '2017-01-01';

-- Delete using a scalar subquery
DELETE FROM all_events
  WHERE session_time < (SELECT min(session_time) FROM good_events);

-- Delete using EXISTS
DELETE FROM orders AS t1
  WHERE EXISTS (SELECT oid FROM returned_orders WHERE t1.oid = oid);

-- Delete using NOT IN (slower, use NOT EXISTS instead)
DELETE FROM events
  WHERE category NOT IN (SELECT category FROM events2 WHERE date > '2001-01-01');
```

^[delete-from-databricks-on-aws.md]

### Other DML Statements

In addition to `DELETE FROM`, Delta Lake supports the following DML operations:

- **INSERT INTO**: Adds new rows to a table.
- **UPDATE**: Modifies existing rows that match a predicate.
- **[MERGE INTO](/concepts/merge-into-delta-lake.md)**: Performs upsert operations (insert, update, or delete based on a source-target match condition), also known as upsert.

These statements are documented separately on the Databricks SQL language reference. ^[delete-from-databricks-on-aws.md]

## Partition Support

DML operations can leverage table [partitioning](/concepts/delta-table-partitioning-mismatch.md) to improve performance. When a `WHERE` predicate matches partition columns, Delta Lake can prune partitions, reducing the amount of data scanned during the operation. ^[delete-from-databricks-on-aws.md]

## Transactional Guarantees

Every DML operation on a Delta table is executed as an [ACID transaction](/concepts/delta-acid-transactions.md). This ensures:

- **Atomicity**: The operation either fully succeeds or has no effect.
- **Consistency**: The table remains in a valid state before and after the operation.
- **Isolation**: Concurrent operations can proceed without interference.
- **Durability**: Committed changes persist and can be recovered even after system failures.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer providing ACID transactions and versioning.
- [Time Travel](/concepts/delta-lake-time-travel.md) — Querying historical versions of a Delta table.
- Partition Pruning — Optimization for partition-based filtering.
- [CTE (Common Table Expressions)](/concepts/common-table-expressions-cte-in-dml.md) — Named subqueries used in DML statements.
- Upsert — A combination of insert and update logic, typically implemented via `MERGE INTO`.

## Sources

- delete-from-databricks-on-aws.md

# Citations

1. [delete-from-databricks-on-aws.md](/references/delete-from-databricks-on-aws-ab1d0768.md)
