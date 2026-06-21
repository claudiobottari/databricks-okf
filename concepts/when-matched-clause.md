---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 423904d1b0a0268f4323f8fb3b9b915d1ca2b8f84d8d048935db89f02cf1592a
  pageDirectory: concepts
  sources:
    - merge-into-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - when-matched-clause
    - WMC
    - WHEN NOT MATCHED Clause
    - WHEN MATCHED (UPDATE/DELETE) Clause
    - WHERE clauses
  citations:
    - file: merge-into-databricks-on-aws.md
title: WHEN MATCHED Clause
description: Specifies actions (DELETE or UPDATE) to perform when a source row matches a target table row based on the merge condition, with optional conditional evaluation and ordering of multiple clauses.
tags:
  - delta-lake
  - sql
  - merge
timestamp: "2026-06-19T19:31:28.057Z"
---

# WHEN MATCHED Clause

The **`WHEN MATCHED` Clause** is a component of the `MERGE INTO` statement in Databricks SQL that specifies the action to take when a source row matches a target table row based on the merge condition. It is part of the Delta Lake `MERGE` operation for upserting, updating, or deleting data.

## Syntax

The `WHEN MATCHED` clause appears after the `ON` condition in a `MERGE INTO` statement and can include an optional `AND matched_condition` for conditional matching. The syntax is:

```
WHEN MATCHED [ AND matched_condition ] THEN matched_action
```

Where `matched_action` can be one of:

- `DELETE`
- `UPDATE SET * [ EXCEPT ( column [, ...] ) ]`
- `UPDATE SET { column = { expr | DEFAULT } } [, ...]`

^[merge-into-databricks-on-aws.md]

## Behavior

`WHEN MATCHED` clauses are executed when a source row matches a target table row based on the `merge_condition` defined in the `ON` clause. Databricks allows multiple `WHEN MATCHED` clauses, evaluated in the order they are specified. Each `WHEN MATCHED` clause, except the last one, must have a `matched_condition`. If any clause lacks a condition when it is not the last, the query returns a `NON_LAST_MATCHED_CLAUSE_OMIT_CONDITION` error. ^[merge-into-databricks-on-aws.md]

If none of the `WHEN MATCHED` conditions evaluate to true for a source and target row pair that matches the `merge_condition`, the target row is left unchanged. ^[merge-into-databricks-on-aws.md]

## Actions

### DELETE
Deletes the matching target table row. Databricks allows multiple matches when matches are unconditionally deleted, as an unconditional delete is not ambiguous even with multiple matches. ^[merge-into-databricks-on-aws.md]

### UPDATE SET *
Updates all columns of the target Delta table with the corresponding columns of the source dataset. This is equivalent to `UPDATE SET col1 = source.col1 [, col2 = source.col2 ...]` for all target columns. This action requires the source table to have the same columns as the target table; otherwise, the query throws an analysis error. ^[merge-into-databricks-on-aws.md]

To exclude specific columns from `UPDATE SET *`, use the `EXCEPT` clause. Excluded target columns are set to `null`. With schema evolution enabled, the `EXCEPT` columns refer to source columns and are excluded from schema evolution. ^[merge-into-databricks-on-aws.md]

### UPDATE SET specific columns
Updates specified target columns using expressions. You can specify `DEFAULT` as an expression to explicitly update the column to its default value. ^[merge-into-databricks-on-aws.md]

## Multiple Matches Handling

`MERGE` operations fail with a `DELTA_MULTIPLE_SOURCE_ROW_MATCHING_TARGET_ROW_IN_MERGE` error if more than one row in the source table matches the same row in the target table based on conditions in the `ON` and `WHEN MATCHED` clauses. This is because the update becomes ambiguous — it is unclear which source row should update the matched target row. To avoid this, preprocess the source table to eliminate multiple matches. ^[merge-into-databricks-on-aws.md]

## Examples

Delete all target rows that have a match in the source table:
```sql
MERGE INTO target USING source
  ON target.key = source.key
  WHEN MATCHED THEN DELETE
```
^[merge-into-databricks-on-aws.md]

Conditionally update target rows that have a match using the source value:
```sql
MERGE INTO target USING source
  ON target.key = source.key
  WHEN MATCHED AND target.updated_at < source.updated_at THEN UPDATE SET *
```
^[merge-into-databricks-on-aws.md]

Multiple `MATCHED` clauses conditionally deleting and updating:
```sql
MERGE INTO target USING source
  ON target.key = source.key
  WHEN MATCHED AND target.marked_for_deletion THEN DELETE
  WHEN MATCHED THEN UPDATE SET target.updated_at = source.updated_at, target.value = DEFAULT
```
^[merge-into-databricks-on-aws.md]

## Related Concepts

- [MERGE INTO](/concepts/merge-into-delta-lake.md) — The parent statement containing `WHEN MATCHED`
- [WHEN NOT MATCHED Clause](/concepts/when-not-matched-insert-clause.md) — Action for source rows without a target match
- [WHEN NOT MATCHED BY SOURCE Clause](/concepts/when-not-matched-by-source-clause.md) — Action for target rows without a source match
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that supports the `MERGE` operation
- Schema Evolution — Automatic schema updates during merge operations

## Sources

- merge-into-databricks-on-aws.md

# Citations

1. [merge-into-databricks-on-aws.md](/references/merge-into-databricks-on-aws-b9eee097.md)
