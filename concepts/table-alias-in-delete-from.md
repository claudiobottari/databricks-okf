---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 648bd0f5d6331a0cce8036eea8e8f5253715c117d84d2fb84eda6d1970502298
  pageDirectory: concepts
  sources:
    - delete-from-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - table-alias-in-delete-from
    - TAIDF
  citations:
    - file: delete-from-databricks-on-aws.md
title: Table Alias in DELETE FROM
description: Using table aliases in DELETE FROM statements to simplify references in subqueries
tags:
  - sql
  - syntax
  - dml
timestamp: "2026-06-19T18:20:21.770Z"
---

# Table Alias in DELETE FROM

**Table Alias in DELETE FROM** refers to the ability to assign a temporary name (alias) to a target table within a `DELETE FROM` statement on Delta Lake tables. This alias can then be used to refer to the table in subqueries, particularly in the `WHERE` clause when joining against other tables or subqueries. ^[delete-from-databricks-on-aws.md]

## Syntax

The optional `table_alias` is specified immediately after the `table_name` in the `DELETE FROM` statement:

```sql
DELETE FROM table_name [table_alias] [WHERE predicate]
```

^[delete-from-databricks-on-aws.md]

## Requirements

- The `table_alias` must not include a column list — only a simple alias name is permitted. ^[delete-from-databricks-on-aws.md]
- The statement is supported only for [Delta Lake](/concepts/delta-lake.md) tables. ^[delete-from-databricks-on-aws.md]
- The `table_name` must not include a temporal specification. ^[delete-from-databricks-on-aws.md]

## Purpose and Use Cases

The table alias is primarily useful when the `WHERE` predicate contains subqueries that need to reference the target table. Without an alias, it can be ambiguous or more verbose to refer to the table being deleted from within a correlated subquery. ^[delete-from-databricks-on-aws.md]

Common patterns include:

- **Correlated subqueries with `EXISTS`**: The alias allows the subquery to reference columns from the target table.
- **Correlated subqueries with `IN` or `NOT IN`**: The alias disambiguates column references when the subquery involves the same table or tables with overlapping column names.
- **Common table expressions (CTEs)**: When used with a [common table expression](/concepts/common-table-expressions-cte-in-dml.md), the alias helps clarify which table is being deleted.

## Examples

The following example uses a table alias `t1` in combination with an `EXISTS` subquery to delete rows from `orders` that have matching entries in a `returned_orders` table:

```sql
DELETE FROM orders AS t1
  WHERE EXISTS (SELECT oid FROM returned_orders WHERE t1.oid = oid)
```

^[delete-from-databricks-on-aws.md]

In this example, `t1.oid` explicitly refers to the `oid` column of the `orders` table being deleted, while `oid` alone refers to the column in `returned_orders`.

## Comparison with Other DML Statements

The ability to use a table alias in a `DELETE FROM` statement follows similar conventions to other Delta Lake DML statements:

- UPDATE — Supports table aliases for the target table.
- MERGE — Supports aliases for both the target and source tables.
- INSERT — Does not typically require a table alias for the target table.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer that supports `DELETE FROM` with table aliases.
- [Common Table Expression (CTE)](/concepts/common-table-expressions-cte-in-dml.md) — Named subqueries that can precede `DELETE FROM` statements.
- Subqueries in WHERE Clause — The primary use case for table aliases in delete operations.
- [DELETE FROM](/concepts/delete-from-delta-lake.md) — The full statement syntax and parameter documentation.
- UPDATE — Similar alias support for update operations.
- MERGE — Upsert operations with alias support.

## Sources

- delete-from-databricks-on-aws.md

# Citations

1. [delete-from-databricks-on-aws.md](/references/delete-from-databricks-on-aws-ab1d0768.md)
