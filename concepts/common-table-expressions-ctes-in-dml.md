---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0254ae2618f6df3f7a8d7babb29db8d428994c2211c56da9843657411dfdc415
  pageDirectory: concepts
  sources:
    - delete-from-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - common-table-expressions-ctes-in-dml
    - CTE(ID
    - Common Table Expressions (CTEs)
    - common table expressions (CTEs)
    - common-table-expressions-cte-in-delete
    - Common Table Expression (CTE) in SELECT
  citations:
    - file: delete-from-databricks-on-aws.md
title: Common Table Expressions (CTEs) in DML
description: CTEs can be used with DELETE FROM statements to reuse named subqueries for improved readability and performance.
tags:
  - sql
  - cte
  - dml
timestamp: "2026-06-18T11:48:15.685Z"
---

# Common Table Expressions (CTEs) in DML

**Common Table Expressions (CTEs)** are one or more named queries that can be reused multiple times within the main block of a Data Manipulation Language (DML) statement. They help avoid repeated computations and improve the readability of complex, nested queries. ^[delete-from-databricks-on-aws.md]

## Syntax

When used in a DML statement, the CTE clause appears before the DML command itself. The following example shows the syntax for a `DELETE FROM` statement:

```
[ common_table_expression ]
DELETE FROM table_name [table_alias] [WHERE predicate]
```

^[delete-from-databricks-on-aws.md]

The `common_table_expression` is defined using the standard SQL `WITH` clause, which declares one or more named subqueries that can be referenced by name in the subsequent DML operation.

## Benefits

- **Reusability:** The same named query can be referenced multiple times within the DML statement without rewriting the subquery.
- **Performance:** The query engine may materialize the CTE result once, avoiding repeated execution of the same logic.
- **Readability:** Breaking complex logic into named steps makes the DML statement easier to understand and maintain.

## Example

The following example uses a CTE to compute the minimum session time from `good_events` and then deletes rows from `all_events` that have an earlier session time:

```sql
WITH min_good_session AS (
  SELECT min(session_time) AS min_time FROM good_events
)
DELETE FROM all_events
WHERE session_time < (SELECT min_time FROM min_good_session);
```

^[delete-from-databricks-on-aws.md]

In this example, the CTE `min_good_session` is defined once and then used inside the `WHERE` predicate of the `DELETE` statement.

## Usage in DML Statements

The source material provides documentation for CTEs in the context of the `DELETE FROM` statement. The same principle applies to other DML statements that support subqueries, though the source does not explicitly cover `INSERT`, `UPDATE`, or `MERGE` with CTEs.

## Related Concepts

- [DELETE FROM](/concepts/delete-from-delta-lake.md) — The DML statement in which CTEs are documented for Delta Lake tables.
- SELECT — CTEs are most commonly used with `SELECT` queries; the same `WITH` syntax is used for DML.
- Subqueries — CTEs provide an alternative to inline subqueries in DML predicates.
- [Delta Lake](/concepts/delta-lake.md) — The storage format for which `DELETE FROM` with CTEs is supported.
- [MERGE INTO](/concepts/merge-into-delta-lake.md) — Another DML statement that may support CTEs (not covered in source).

## Sources

- delete-from-databricks-on-aws.md

# Citations

1. [delete-from-databricks-on-aws.md](/references/delete-from-databricks-on-aws-ab1d0768.md)
