---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 17f458d55ca869c6b7f657f6a52b75b78493dfe19cdf5384deec3729b2995907
  pageDirectory: concepts
  sources:
    - delete-from-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - table-aliases-in-delete-statements
    - TAIDS
  citations:
    - file: delete-from-databricks-on-aws.md
title: Table Aliases in DELETE Statements
description: Databricks SQL allows optional table aliasing in DELETE FROM syntax but the alias must not include a column list.
tags:
  - sql
  - syntax
  - dml
timestamp: "2026-06-18T11:48:12.274Z"
---

# Table Aliases in DELETE Statements

**Table Aliases in DELETE Statements** allow you to assign a temporary name to the target table within a `DELETE` command. This is useful when the `WHERE` clause contains subqueries that need to reference the table being deleted from, particularly correlated subqueries. Table aliases in `DELETE` are supported only for [Delta Lake](/concepts/delta-lake.md) tables. ^[delete-from-databricks-on-aws.md]

## Syntax

The alias is placed immediately after the table name, optionally preceded by `AS`. The alias must not include a column list. ^[delete-from-databricks-on-aws.md]

```sql
DELETE FROM table_name [table_alias] [WHERE predicate]
```

## Parameters

- **table_alias** – A temporary name for the table. The alias must not include a column list. It can be used within the `WHERE` predicate to refer to the target table, for example in subqueries. ^[delete-from-databricks-on-aws.md]

## Examples

Delete rows from `orders` where a matching order ID exists in the `returned_orders` table:

```sql
DELETE FROM orders AS t1
  WHERE EXISTS (SELECT oid FROM returned_orders WHERE t1.oid = oid);
```

^[delete-from-databricks-on-aws.md]

In this example, the alias `t1` lets the subquery unambiguously reference the `orders` table’s `oid` column.

## Use Cases

- **Correlated subqueries** – When the `WHERE` condition depends on a subquery that refers back to the table being deleted, an alias provides a clear way to qualify the column reference. ^[delete-from-databricks-on-aws.md]
- **Readability** – Shorter aliases can make complex delete statements easier to read, especially when the table name is long.

## Best Practices

- Always use an alias if the `WHERE` clause contains a subquery that references the target table. Without an alias, the column reference may be ambiguous or cause a parsing error.
- Avoid aliases that include column lists; the syntax does not permit them. ^[delete-from-databricks-on-aws.md]

## Limitations

- Table aliases in `DELETE` are only valid for [Delta Lake](/concepts/delta-lake.md) tables. ^[delete-from-databricks-on-aws.md]
- The alias cannot be used in a `FROM` clause outside of the `DELETE` itself; it only applies within the `DELETE` statement’s scope.

## Related Concepts

- [DELETE FROM](/concepts/delete-from-delta-lake.md) – The full statement syntax and supported subquery types
- [MERGE INTO](/concepts/merge-into-delta-lake.md) – Another DML statement that supports table aliases
- UPDATE – Table aliases are also used in `UPDATE` statements
- [Common Table Expressions](/concepts/common-table-expressions-cte-in-dml.md) – Can be used with `DELETE` to improve query structure
- Subqueries – How subqueries interact with `DELETE` and aliases

## Sources

- delete-from-databricks-on-aws.md

# Citations

1. [delete-from-databricks-on-aws.md](/references/delete-from-databricks-on-aws-ab1d0768.md)
