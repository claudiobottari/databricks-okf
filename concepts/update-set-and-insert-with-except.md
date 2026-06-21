---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ee13190f8d0405fa14590cba2eea6f57054f6f032c588891084a308613f506f0
  pageDirectory: concepts
  sources:
    - merge-into-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - update-set-and-insert-with-except
    - INSERT * with EXCEPT and UPDATE SET *
    - US*AI*WE
    - UPDATE and MERGE
  citations:
    - file: merge-into-databricks-on-aws.md
title: UPDATE SET * and INSERT * with EXCEPT
description: Shorthand syntax to update all target columns from corresponding source columns (or insert all source columns), with the ability to exclude specific columns using the EXCEPT clause (Databricks Runtime 12.2 LTS+).
tags:
  - delta-lake
  - sql
  - syntax
timestamp: "2026-06-19T19:31:41.624Z"
---

# UPDATE SET * and INSERT * with EXCEPT

**UPDATE SET \* and INSERT \* with EXCEPT** are shorthand notations used in `MERGE INTO` statements on Delta Lake tables. They allow updating or inserting all columns from a source table into a target table in one expression, with the option to exclude specific columns using the `EXCEPT` clause. ^[merge-into-databricks-on-aws.md]

## Syntax

The relevant syntax within a `MERGE INTO` statement is:

```sql
matched_action {
  UPDATE SET * [ EXCEPT ( column [, ...] ) ] |
  ...
}
not_matched_action {
  INSERT * [ EXCEPT ( column [, ...] ) ] |
  ...
}
```

^[merge-into-databricks-on-aws.md]

## UPDATE SET *

`UPDATE SET *` updates all columns of the matched target row with the corresponding columns from the source dataset. It is equivalent to writing `UPDATE SET col1 = source.col1 [, col2 = source.col2 ...]` for every column in the target table. This action requires that the source table has the same columns as the target table; otherwise, the query raises an analysis error. ^[merge-into-databricks-on-aws.md]

### Using EXCEPT with UPDATE SET *

The `EXCEPT` clause allows you to exclude specific columns from the update. The excluded target columns are set to `NULL` after the update. ^[merge-into-databricks-on-aws.md]

When schema evolution is enabled (`MERGE WITH SCHEMA EVOLUTION`), the columns listed in `EXCEPT` refer to source columns, and those source columns are excluded from schema evolution. This means the target schema will not be extended with the excluded source columns. ^[merge-into-databricks-on-aws.md]

**Applies to:** Databricks SQL and Databricks Runtime 12.2 LTS or above. ^[merge-into-databricks-on-aws.md]

> **Note:** The `UPDATE SET *` shorthand (without `EXCEPT`) is available in earlier versions, but the `EXCEPT` clause itself requires Databricks Runtime 12.2 LTS or above for both `UPDATE` and `INSERT` actions.

## INSERT *

`INSERT *` inserts all columns from a source row that does not match any target row into the target table. It is equivalent to writing `INSERT (col1 [, col2 ...]) VALUES (source.col1 [, source.col2 ...])` for every column in the target table. This action also requires the source table to have the same columns as the target table. ^[merge-into-databricks-on-aws.md]

### Using EXCEPT with INSERT *

Similar to `UPDATE SET *`, the `EXCEPT` clause can be used with `INSERT *` to exclude specific columns from the insert operation. Excluded target columns are set to `NULL` in the inserted rows. ^[merge-into-databricks-on-aws.md]

When schema evolution is enabled, the `EXCEPT` columns refer to source columns and are excluded from schema evolution. ^[merge-into-databricks-on-aws.md]

**Applies to:** Databricks SQL and Databricks Runtime 12.2 LTS or above. ^[merge-into-databricks-on-aws.md]

## Examples

The following examples are taken from the Delta Lake `MERGE INTO` documentation:

```sql
-- Insert all columns from the source except `last_updated`, which is set to null in the target.
MERGE INTO target USING source
  ON target.key = source.key
  WHEN NOT MATCHED THEN INSERT * EXCEPT (last_updated)
```

^[merge-into-databricks-on-aws.md]

```sql
-- Update all matching target rows using all source columns except `last_updated`.
MERGE INTO target USING source
  ON target.key = source.key
  WHEN MATCHED THEN UPDATE SET * EXCEPT (last_updated)
```

(Similar pattern can be used for `UPDATE SET * EXCEPT`; the source provides an example only for `INSERT * EXCEPT`, but the syntax is symmetrical.)

## Important Considerations

- The `EXCEPT` clause is only supported when the `UPDATE SET *` or `INSERT *` shorthand is used. It is not available with explicit column lists. ^[merge-into-databricks-on-aws.md]
- Columns excluded via `EXCEPT` are set to `NULL` in the target table; no default value is applied. ^[merge-into-databricks-on-aws.md]
- With schema evolution, `EXCEPT` prevents the excluded source columns from being added to the target schema. ^[merge-into-databricks-on-aws.md]
- The source and target tables must have the same column structure for the shorthand to work without errors. ^[merge-into-databricks-on-aws.md]

## Related Concepts

- [MERGE INTO](/concepts/merge-into-delta-lake.md) – The complete statement syntax and semantics.
- [Delta Lake](/concepts/delta-lake.md) – The storage layer that supports `MERGE` operations.
- Schema Evolution – Automatic schema updates during `MERGE` operations.
- [Upsert into Delta Lake using merge](/concepts/merge-into-delta-lake.md) – Practical guidance on using `MERGE` for upserts.

## Sources

- merge-into-databricks-on-aws.md

# Citations

1. [merge-into-databricks-on-aws.md](/references/merge-into-databricks-on-aws-b9eee097.md)
