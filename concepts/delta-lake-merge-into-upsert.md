---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1aeb960f681fc24bf7a03a5ada68bf625e817caee4c5ad3b3d04b3e33d62d09a
  pageDirectory: concepts
  sources:
    - merge-into-databricks-on-aws.md
    - tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - delta-lake-merge-into-upsert
    - DLMI(
    - Delta Lake Merge Schema
    - Delta MERGE INTO
  citations:
    - file: merge-into-databricks-on-aws.md
    - file: tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md
title: Delta Lake MERGE INTO (Upsert)
description: A SQL statement that merges updates, insertions, and deletions from a source table into a target Delta table, supporting WHEN MATCHED, WHEN NOT MATCHED, and WHEN NOT MATCHED BY SOURCE clauses.
tags:
  - delta-lake
  - sql
  - data-manipulation
timestamp: "2026-06-19T19:31:39.566Z"
---

# Delta Lake MERGE INTO (Upsert)

**Delta Lake MERGE INTO (Upsert)** is a SQL statement that merges a set of updates, insertions, and deletions from a source table into a target [Delta Lake Table](/concepts/delta-lake-table.md). It is the primary mechanism for performing upsert operations — updating existing records and inserting new records in a single atomic operation. ^[merge-into-databricks-on-aws.md]

## Overview

The `MERGE INTO` statement is supported only for [Delta Lake](/concepts/delta-lake.md) tables on Databricks. It combines data from a source table reference with a target Delta table based on a merge condition, then executes specified actions for matched and unmatched rows. ^[merge-into-databricks-on-aws.md]

The statement is available in Databricks SQL and Databricks Runtime. ^[merge-into-databricks-on-aws.md]

## Syntax

```sql
[ common_table_expression ]
MERGE [ WITH SCHEMA EVOLUTION ] INTO target_table_name [target_alias]
  USING source_table_reference [source_alias]
  ON merge_condition
  { WHEN MATCHED [ AND matched_condition ] THEN matched_action |
    WHEN NOT MATCHED [BY TARGET] [ AND not_matched_condition ] THEN not_matched_action |
    WHEN NOT MATCHED BY SOURCE [ AND not_matched_by_source_condition ] THEN not_matched_by_source_action } [...]
```

^[merge-into-databricks-on-aws.md]

## Parameters

### Common Table Expressions

Common table expressions (CTEs) are one or more named queries that can be reused multiple times within the main query block to avoid repeated computations or to improve readability of complex, nested queries. ^[merge-into-databricks-on-aws.md]

### WITH SCHEMA EVOLUTION

**Applies to:** Databricks Runtime 15.2 or above

Enables automatic schema evolution for the `MERGE` operation. When enabled, the schema of the target Delta table is automatically updated to match the schema of the source table. ^[merge-into-databricks-on-aws.md]

### Target and Source References

- **target_table_name**: Identifies the Delta table being modified. The name must not include an options specification, and the table must not be a foreign table. ^[merge-into-databricks-on-aws.md]
- **target_alias**: An optional alias for the target table. The alias must not include a column list. ^[merge-into-databricks-on-aws.md]
- **source_table_reference**: Identifies the source table to be merged into the target table. ^[merge-into-databricks-on-aws.md]
- **source_alias**: An optional alias for the source table. The alias must not include a column list. ^[merge-into-databricks-on-aws.md]

### ON merge_condition

An expression with a return type of Boolean that determines how rows from one relation are combined with rows of another relation. ^[merge-into-databricks-on-aws.md]

### WHEN MATCHED

`WHEN MATCHED` clauses are executed when a source row matches a target table row based on the `merge_condition` and the optional `match_condition`. ^[merge-into-databricks-on-aws.md]

**Matched actions:**

- **DELETE**: Deletes the matching target table row. Databricks allows multiple matches when matches are unconditionally deleted, as an unconditional delete is not ambiguous even with multiple matches. ^[merge-into-databricks-on-aws.md]
- **UPDATE**: Updates the matched target table row. Use `UPDATE SET *` to update all columns of the target Delta table with corresponding columns of the source dataset. This assumes the source table has the same columns as the target table; otherwise, the query throws an analysis error. ^[merge-into-databricks-on-aws.md]
  - **Applies to:** Databricks Runtime 12.2 LTS or above for `UPDATE SET *` with `EXCEPT` clause
  - **Applies to:** Databricks Runtime 11.3 LTS or above for `DEFAULT` as expression

To exclude specific columns from `UPDATE SET *`, use the `EXCEPT` clause. Excluded target columns are set to `null`. With schema evolution enabled, the `EXCEPT` columns refer to source columns and are excluded from schema evolution. ^[merge-into-databricks-on-aws.md]

If there are multiple `WHEN MATCHED` clauses, they are evaluated in the order specified. Each `WHEN MATCHED` clause except the last must have a `matched_condition`. If none of the conditions evaluate to true for a matching pair, the target row is left unchanged. ^[merge-into-databricks-on-aws.md]

### WHEN NOT MATCHED [BY TARGET]

`WHEN NOT MATCHED` clauses insert a row when a source row does not match any target row based on the `merge_condition` and the optional `not_matched_condition`. ^[merge-into-databricks-on-aws.md]

**Applies to:** Databricks SQL and Databricks Runtime 12.2 LTS or above

`WHEN NOT MATCHED BY TARGET` can be used as an alias for `WHEN NOT MATCHED`. ^[merge-into-databricks-on-aws.md]

**Not matched actions:**

- **INSERT \***: Inserts all columns of the target Delta table with corresponding columns of the source dataset. This requires the source table to have the same columns as the target table. ^[merge-into-databricks-on-aws.md]
  - **Applies to:** Databricks SQL and Databricks Runtime 12.2 LTS or above for `INSERT *` with `EXCEPT` clause
- **INSERT (column1 [, ...]) VALUES (expr | DEFAULT [, ...])**: Generates a new row based on specified column and corresponding expressions. Unspecified target columns receive their column default, or `NULL` if none exists. ^[merge-into-databricks-on-aws.md]
  - **Applies to:** Databricks SQL and Databricks Runtime 11.3 LTS or above for `DEFAULT` as expression

If there are multiple `WHEN NOT MATCHED` clauses, they are evaluated in order. All except the last must have `not_matched_condition`s. ^[merge-into-databricks-on-aws.md]

### WHEN NOT MATCHED BY SOURCE

**Applies to:** Databricks SQL and Databricks Runtime 12.2 LTS or above

`WHEN NOT MATCHED BY SOURCE` clauses are executed when a target row does not match any rows in the source table based on the `merge_condition` and the optional `not_match_by_source_condition` evaluates to true. The condition must be a Boolean expression that only references columns from the target table. ^[merge-into-databricks-on-aws.md]

**Not matched by source actions:**

- **DELETE**: Deletes the target table row. ^[merge-into-databricks-on-aws.md]
- **UPDATE**: Updates the target table row. `expr` may only reference columns from the target table, otherwise the query throws an analysis error. ^[merge-into-databricks-on-aws.md]
  - **Applies to:** Databricks SQL and Databricks Runtime 11.3 LTS or above for `DEFAULT` as expression

Adding a `WHEN NOT MATCHED BY SOURCE` clause can lead to a large number of target rows being modified. For best performance, apply `not_matched_by_source_condition`s to limit the number of target rows updated or deleted. ^[merge-into-databricks-on-aws.md]

If there are multiple `WHEN NOT MATCHED BY SOURCE` clauses, they are evaluated in order. Each except the last must have a `not_matched_by_source_condition`. If none of the conditions evaluate to true for an unmatched target row, the target row is left unchanged. ^[merge-into-databricks-on-aws.md]

## Important Considerations

`MERGE` operations fail with a `DELTA_MULTIPLE_SOURCE_ROW_MATCHING_TARGET_ROW_IN_MERGE` error if more than one row in the source table matches the same row in the target table based on the conditions specified in the `ON` and `WHEN MATCHED` clauses. According to SQL semantics of merge, this type of update operation is ambiguous because it is unclear which source row should be used to update the matched target row. You can preprocess the source table to eliminate the possibility of multiple matches. ^[merge-into-databricks-on-aws.md]

In Databricks Runtime 15.4 LTS and below, `MERGE` only considers conditions in the `ON` clause before evaluating multiple matches. ^[merge-into-databricks-on-aws.md]

## Examples

### WHEN MATCHED

```sql
-- Delete all target rows that have a match in the source table.
MERGE INTO target USING source
  ON target.key = source.key
  WHEN MATCHED THEN DELETE

-- Conditionally update target rows that have a match in the source table using the source value.
MERGE INTO target USING source
  ON target.key = source.key
  WHEN MATCHED AND target.updated_at < source.updated_at THEN UPDATE SET *

-- Multiple MATCHED clauses conditionally deleting matched target rows and updating two columns for all other matched rows.
MERGE INTO target USING source
  ON target.key = source.key
  WHEN MATCHED AND target.marked_for_deletion THEN DELETE
  WHEN MATCHED THEN UPDATE SET target.updated_at = source.updated_at, target.value = DEFAULT
```

^[merge-into-databricks-on-aws.md]

### WHEN NOT MATCHED [BY TARGET]

```sql
-- Insert all rows from the source that are not already in the target table.
MERGE INTO target USING source
  ON target.key = source.key
  WHEN NOT MATCHED THEN INSERT *

-- Conditionally insert new rows in the target table using unmatched rows from the source table.
MERGE INTO target USING source
  ON target.key = source.key
  WHEN NOT MATCHED BY TARGET AND source.created_at > now() - INTERVAL "1" DAY
    THEN INSERT (created_at, value) VALUES (source.created_at, DEFAULT)

-- Insert all columns from the source except `last_updated`, which is set to null in the target.
MERGE INTO target USING source
  ON target.key = source.key
  WHEN NOT MATCHED THEN INSERT * EXCEPT (last_updated)
```

^[merge-into-databricks-on-aws.md]

### WHEN NOT MATCHED BY SOURCE

```sql
-- Delete all target rows that have no matches in the source table.
MERGE INTO target USING source
  ON target.key = source.key
  WHEN NOT MATCHED BY SOURCE THEN DELETE

-- Multiple NOT MATCHED BY SOURCE clauses conditionally deleting unmatched target rows and updating two columns for all other matched rows.
MERGE INTO target USING source
  ON target.key = source.key
  WHEN NOT MATCHED BY SOURCE AND target.marked_for_deletion THEN DELETE
  WHEN NOT MATCHED BY SOURCE THEN UPDATE SET target.value = DEFAULT
```

^[merge-into-databricks-on-aws.md]

### WITH SCHEMA EVOLUTION

```sql
-- Multiple MATCHED and NOT MATCHED clauses with schema evolution enabled.
MERGE WITH SCHEMA EVOLUTION INTO target USING source
  ON source.key = target.key
  WHEN MATCHED THEN UPDATE SET *
  WHEN NOT MATCHED THEN INSERT *
  WHEN NOT MATCHED BY SOURCE THEN DELETE
```

^[merge-into-databricks-on-aws.md]

## Using MERGE for Upsert Operations

The `MERGE INTO` statement is the standard way to perform upsert operations on Delta Lake tables. The tutorial on creating and managing Delta Lake tables demonstrates a common upsert pattern: ^[tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md]

```python
from delta.tables import *

deltaTable = DeltaTable.forName(spark, 'workspace.default.people_10k')

(deltaTable.alias("people_10k")
  .merge(
    people_10k_updates.alias("people_10k_updates"),
    "people_10k.id = people_10k_updates.id")
  .whenMatchedUpdateAll()
  .whenNotMatchedInsertAll()
  .execute())
```

^[tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md]

In this pattern, when there is a matching row in both tables, Delta Lake updates the data column using the given expression. When there is no matching row, Delta Lake adds a new row. ^[tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The optimized storage layer that provides the foundation for tables on Databricks
- [Upsert into a Delta Lake table using merge](/concepts/delta-lake-table.md) — Guidance on how to use MERGE operations to manage data
- [Automatic schema evolution with merge](/concepts/with-schema-evolution-for-merge.md) — Details on schema evolution behavior during MERGE operations
- [DeltaTable API](/concepts/delta-lake-api.md) — Python and Scala APIs for programmatic merge operations
- Change Data Capture (CDC) — Common use case for MERGE operations
- [Time Travel](/concepts/delta-lake-time-travel.md) — Querying earlier versions of Delta tables
- OPTIMIZE — Compacting small files created by multiple MERGE operations
- VACUUM — Cleaning up old snapshots after MERGE operations

## Sources

- merge-into-databricks-on-aws.md
- tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md

# Citations

1. [merge-into-databricks-on-aws.md](/references/merge-into-databricks-on-aws-b9eee097.md)
2. [tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md](/references/tutorial-create-and-manage-delta-lake-tables-databricks-on-aws-481179d7.md)
