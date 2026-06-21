---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1b7535c1abc7f150825c61210f5f771a16afa8242779e4c8e01f0777a26abc75
  pageDirectory: concepts
  sources:
    - delete-from-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-dml-restrictions
    - DLDR
  citations:
    - file: delete-from-databricks-on-aws.md
    - file: update-databricks-on-aws.md
    - file: merge-into-databricks-on-aws.md
title: Delta Lake DML Restrictions
description: Constraints on Delta Lake DML operations including DELETE restrictions on temporal specifications, foreign tables, and subquery nesting.
tags:
  - delta-lake
  - sql
  - limitations
timestamp: "2026-06-19T14:58:56.884Z"
---

# Delta Lake DML Restrictions

**Delta Lake DML Restrictions** refer to limitations on Data Manipulation Language (DML) operations — specifically `DELETE`, `UPDATE`, and `MERGE` — when applied to Delta Lake tables on Databricks. These restrictions affect which tables can be modified and which subquery patterns are supported in the `WHERE` clause. ^[delete-from-databricks-on-aws.md, update-databricks-on-aws.md, merge-into-databricks-on-aws.md]

## Overview

Delta Lake supports standard DML statements for modifying data, but imposes certain restrictions to ensure transactional consistency, performance, and compatibility with the [Delta Lake](/concepts/delta-lake.md) protocol. The restrictions primarily concern the target table type and the complexity of subqueries used in filtering conditions. ^[delete-from-databricks-on-aws.md]

## Table Type Restrictions

The target table in a `DELETE`, `UPDATE`, or `MERGE` statement must be a [Delta Lake](/concepts/delta-lake.md) table. ^[delete-from-databricks-on-aws.md]

- The table name must not include a temporal specification, such as a time-travel version or timestamp. ^[delete-from-databricks-on-aws.md]
- The table must not be a **foreign table** (an external table managed by another system like Hive or a JDBC source). ^[delete-from-databricks-on-aws.md]

These restrictions apply to all three DML statements. ^[delete-from-databricks-on-aws.md, update-databricks-on-aws.md, merge-into-databricks-on-aws.md]

## Subquery Restrictions in the WHERE Clause

The `WHERE` predicate in `DELETE` and `UPDATE` statements supports subqueries, including `IN`, `NOT IN`, `EXISTS`, `NOT EXISTS`, and scalar subqueries. However, two types of subqueries are **not supported**: ^[delete-from-databricks-on-aws.md, update-databricks-on-aws.md]

- **Nested subqueries**: A subquery inside another subquery is not allowed. ^[delete-from-databricks-on-aws.md, update-databricks-on-aws.md]
- **`NOT IN` subquery inside an `OR`**: For example, `a = 3 OR b NOT IN (SELECT c FROM t)` is not supported. ^[delete-from-databricks-on-aws.md, update-databricks-on-aws.md]

In most cases, `NOT IN` subqueries can be rewritten using `NOT EXISTS`. Databricks recommends using `NOT EXISTS` whenever possible, as `DELETE` and `UPDATE` with `NOT IN` subqueries can be significantly slower. ^[delete-from-databricks-on-aws.md, update-databricks-on-aws.md]

Unsupported subquery patterns may result in an error and should be restructured to use equivalent supported patterns. ^[delete-from-databricks-on-aws.md, update-databricks-on-aws.md]

## MERGE-Specific Restrictions

The [MERGE INTO](/concepts/merge-into-delta-lake.md) statement has additional restrictions beyond those shared with `DELETE` and `UPDATE`. For complete details on MERGE-specific limitations, see the [MERGE INTO](/concepts/merge-into-delta-lake.md) documentation. ^[merge-into-databricks-on-aws.md]

## Common Table Expressions (CTEs)

DML statements on Delta Lake tables can include [Common Table Expressions (CTEs)](/concepts/common-table-expressions-ctes-in-dml.md) at the beginning of the statement. CTEs define named queries that can be reused multiple times within the main query block. This feature is supported for all Delta Lake DML statements to improve readability and avoid repeated computations. ^[delete-from-databricks-on-aws.md, update-databricks-on-aws.md, merge-into-databricks-on-aws.md]

## Best Practices

- Use `NOT EXISTS` instead of `NOT IN` in subqueries within `DELETE` and `UPDATE` statements for better performance. ^[delete-from-databricks-on-aws.md, update-databricks-on-aws.md]
- Ensure all DML target tables are [Delta Lake](/concepts/delta-lake.md) tables, not foreign tables. ^[delete-from-databricks-on-aws.md]
- Avoid temporal specifications (time-travel) on the target table name in DML statements. ^[delete-from-databricks-on-aws.md]
- Use CTEs to simplify complex DML statements without nesting subqueries. ^[delete-from-databricks-on-aws.md, update-databricks-on-aws.md, merge-into-databricks-on-aws.md]

## Related Concepts

- [DELETE FROM](/concepts/delete-from-delta-lake.md) – Syntax and usage for deleting rows from Delta tables.
- UPDATE – Syntax and usage for updating rows in Delta tables.
- [MERGE INTO](/concepts/merge-into-delta-lake.md) – Syntax and usage for upsert operations on Delta tables.
- [Delta Lake](/concepts/delta-lake.md) – The underlying storage layer that supports these DML operations.
- [Common Table Expressions (CTEs)](/concepts/common-table-expressions-ctes-in-dml.md) – Named subqueries supported in DML statements.
- Databricks SQL – The SQL environment where these restrictions apply.

## Sources

- delete-from-databricks-on-aws.md
- update-databricks-on-aws.md
- merge-into-databricks-on-aws.md

# Citations

1. [delete-from-databricks-on-aws.md](/references/delete-from-databricks-on-aws-ab1d0768.md)
2. [update-databricks-on-aws.md](/references/update-databricks-on-aws-8f0bcd2b.md)
3. [merge-into-databricks-on-aws.md](/references/merge-into-databricks-on-aws-b9eee097.md)
