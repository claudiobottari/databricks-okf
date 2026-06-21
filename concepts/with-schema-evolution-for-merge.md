---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d02a5bc5dcfa1f3ad4ec2298abcd299b80468c542d732cfcee580929acca07e8
  pageDirectory: concepts
  sources:
    - merge-into-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - with-schema-evolution-for-merge
    - WSEFM
    - Automatic schema evolution with merge
  citations:
    - file: merge-into-databricks-on-aws.md
    - file: lines 47-60
    - file: lines 48-49
    - file: lines 49-50
    - file: lines 69-70
    - file: lines 112-113
title: WITH SCHEMA EVOLUTION for MERGE
description: A modifier that automatically updates the target Delta table schema to match the source table schema during a MERGE operation (Databricks Runtime 15.2+).
tags:
  - delta-lake
  - schema-evolution
  - sql
timestamp: "2026-06-19T19:31:36.785Z"
---

# `WITH SCHEMA EVOLUTION` for MERGE

The `WITH SCHEMA EVOLUTION` clause is an optional modifier for the `MERGE INTO` statement in Databricks SQL and Databricks Runtime. When specified, it enables automatic schema evolution on the target Delta table, allowing the table’s schema to be updated to match the source table’s schema during the merge operation. ^[merge-into-databricks-on-aws.md]

## Syntax

The clause is placed immediately after the `MERGE` keyword and before `INTO`:

```sql
MERGE WITH SCHEMA EVOLUTION INTO target_table_name [target_alias]
USING source_table_reference [source_alias]
ON merge_condition
{ WHEN MATCHED [ AND matched_condition ] THEN matched_action |
  WHEN NOT MATCHED [BY TARGET] [ AND not_matched_condition ] THEN not_matched_action |
  WHEN NOT MATCHED BY SOURCE [ AND not_matched_by_source_condition ] THEN not_matched_by_source_action }
[...]
```

^[merge-into-databricks-on-aws.md, lines 47-60]

## Requirements

`WITH SCHEMA EVOLUTION` is available in **Databricks Runtime 15.2 or above**. It applies to both Databricks SQL and Databricks Runtime. ^[merge-into-databricks-on-aws.md, lines 48-49]

## Behavior

When `WITH SCHEMA EVOLUTION` is enabled, the target Delta table’s schema is automatically updated to match the schema of the source table. This includes adding new columns that exist in the source but not in the target, and widening data types as needed (subject to Delta Lake schema evolution rules). ^[merge-into-databricks-on-aws.md, lines 49-50]

### Interaction with `EXCEPT` in `UPDATE SET *` and `INSERT *`

The `EXCEPT` clause can be used with `UPDATE SET *` or `INSERT *` to exclude specific columns from the operation. When schema evolution is active, the `EXCEPT` columns refer to **source columns** and are also excluded from schema evolution – meaning those columns will not be added to the target table even if they exist in the source. ^[merge-into-databricks-on-aws.md, lines 69-70]

### Effect on matched and unmatched actions

Schema evolution affects the resolution of column references in `UPDATE SET *` and `INSERT *`. For example, if the source has a new column `new_col` not present in the target:
- `UPDATE SET *` would add `new_col` to the target and set its value from the source.
- `INSERT *` would similarly include `new_col`.
- Explicit column lists (e.g., `INSERT (col1, col2) VALUES (...))` do not trigger schema evolution for columns not listed.

The `WHEN NOT MATCHED BY SOURCE` clause does not involve source columns for the action, so it does not directly cause schema evolution, but the overall merge may still evolve the schema based on other clauses.

## Example

The following example merges source data into a target Delta table with schema evolution enabled, performing updates, inserts, and deletions:

```sql
MERGE WITH SCHEMA EVOLUTION INTO target USING source
ON source.key = target.key
WHEN MATCHED THEN UPDATE SET *
WHEN NOT MATCHED THEN INSERT *
WHEN NOT MATCHED BY SOURCE THEN DELETE
```

^[merge-into-databricks-on-aws.md, lines 112-113]

If the source table contains columns that the target table does not, they will be automatically added to the target schema. Existing columns in the target that are not present in the source are not dropped.

## Related Concepts

- [MERGE INTO](/concepts/merge-into-delta-lake.md) — The base statement for upserting data into Delta tables.
- Schema Evolution — General concept of automatically evolving table schemas.
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that supports schema evolution.
- [Upsert into a Delta Lake table using merge](/concepts/delta-lake-table.md) — Practical guide for merge operations.
- EXCEPT clause in MERGE — Excluding specific columns from update/insert wildcards.

## Sources

- merge-into-databricks-on-aws.md

# Citations

1. [merge-into-databricks-on-aws.md](/references/merge-into-databricks-on-aws-b9eee097.md)
2. lines 47-60
3. lines 48-49
4. lines 49-50
5. lines 69-70
6. lines 112-113
