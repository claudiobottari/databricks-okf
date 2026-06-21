---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8b330b108614ffa869dfcdfc93202091e0235ce24fa0d860809a908ce442462b
  pageDirectory: concepts
  sources:
    - update-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - default-expression-in-update
    - DEIU
  citations:
    - file: update-databricks-on-aws.md
title: DEFAULT Expression in UPDATE
description: Sets a column to its defined default value (or NULL if no default is defined) during an UPDATE operation. Available in Databricks Runtime 11.3 LTS and above.
tags:
  - delta-lake
  - sql
  - default-values
timestamp: "2026-06-19T23:16:41.781Z"
---

# DEFAULT Expression in UPDATE

The **DEFAULT Expression in UPDATE** is a syntax option in Databricks SQL and Databricks Runtime that allows you to reset a column to its default value during an update operation on [Delta Lake](/concepts/delta-lake.md) tables. Instead of specifying an explicit expression for a column, you use the `DEFAULT` keyword to assign the column's predefined default value. ^[update-databricks-on-aws.md]

## Syntax

The `DEFAULT` expression can be used in the `SET` clause of an UPDATE statement in place of a standard expression:

```sql
UPDATE table_name
SET column_name = DEFAULT
[WHERE clause]
```

^[update-databricks-on-aws.md]

## Behavior

When `DEFAULT` is specified, the column is set to its default value if one is defined in the table schema. If no default value is defined for the column, `DEFAULT` resolves to `NULL`. ^[update-databricks-on-aws.md]

This feature is available in Databricks Runtime 11.3 LTS and above, as well as in Databricks SQL. ^[update-databricks-on-aws.md]

## Example

The following example updates the `category` column in the `events` table, setting it to its default value (`NULL` if no default is defined) for rows where `eventType` is `'unknown'`:

```sql
UPDATE events
SET category = DEFAULT
WHERE eventType = 'unknown'
```

^[update-databricks-on-aws.md]

## Usage Notes

- The `DEFAULT` expression is only supported for [Delta Lake](/concepts/delta-lake.md) tables. ^[update-databricks-on-aws.md]
- Multiple columns can be updated in a single `UPDATE` statement, with any combination of explicit expressions and `DEFAULT` values. ^[update-databricks-on-aws.md]
- The `WHERE` clause filters which rows are affected. Without a `WHERE` clause, the default value is applied to all rows. ^[update-databricks-on-aws.md]

## Related Concepts

- UPDATE — The overall statement that supports the `DEFAULT` expression.
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that supports this operation.
- [MERGE INTO](/concepts/merge-into-delta-lake.md) — An alternative for updating from a join with another table.
- Databricks SQL — The SQL interface where this feature is available.
- Databricks Runtime 11.3 LTS — The minimum Runtime version supporting `DEFAULT` in `UPDATE`.

## Sources

- update-databricks-on-aws.md

# Citations

1. [update-databricks-on-aws.md](/references/update-databricks-on-aws-8f0bcd2b.md)
