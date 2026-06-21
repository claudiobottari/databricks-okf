---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3487e4b2856f7c10f7e89c276cc720d3ed91b586a902445e80c09ea4073f6047
  pageDirectory: concepts
  sources:
    - merge-into-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - when-not-matched-insert-clause
    - WNM(C
    - WHEN NOT MATCHED Clause
  citations:
    - file: merge-into-databricks-on-aws.md
title: WHEN NOT MATCHED (INSERT) Clause
description: Inserts a new row into the target Delta table when a source row does not match any target row, supporting INSERT * (all columns), INSERT with specific columns, and optional EXCEPT clause.
tags:
  - delta-lake
  - sql
  - merge
timestamp: "2026-06-19T19:31:49.888Z"
---

# WHEN NOT MATCHED (INSERT) Clause

The **WHEN NOT MATCHED** clause (also written as `WHEN NOT MATCHED BY TARGET`) is a component of the [MERGE INTO](/concepts/merge-into-delta-lake.md) statement used with [Delta Lake](/concepts/delta-lake.md) tables. It defines the action to take when a row from the source table does not have a matching row in the target table based on the merge condition. ^[merge-into-databricks-on-aws.md]

## Syntax

```sql
WHEN NOT MATCHED [BY TARGET] [ AND not_matched_condition ] THEN not_matched_action
```

Where `not_matched_action` is one of:

- `INSERT * [ EXCEPT ( column [, ...] ) ]` – inserts all columns from the source row into the target table. Equivalent to listing every column in the target table with the corresponding source column value.
- `INSERT (column1 [, ...] ) VALUES ( expr | DEFAULT [, ...] )` – inserts a new row with explicit column mapping and expressions. Columns not specified receive their column default or `NULL`. ^[merge-into-databricks-on-aws.md]

## Behavior

The `WHEN NOT MATCHED` clause is evaluated for each source row that does not satisfy the `merge_condition` with any target row. The optional `not_matched_condition` further filters which unmatched source rows are inserted. ^[merge-into-databricks-on-aws.md]

Multiple `WHEN NOT MATCHED` clauses can be specified, and they are evaluated in order. All but the last clause must have a `not_matched_condition`; otherwise, the statement returns a `NON_LAST_NOT_MATCHED_CLAUSE_OMIT_CONDITION` error. ^[merge-into-databricks-on-aws.md]

When using `INSERT *`, the source table must have the same columns as the target table. The optional `EXCEPT` clause explicitly excludes certain columns from the insert; excluded target columns are set to `NULL`. If schema evolution is enabled, `EXCEPT` columns refer to source columns and are excluded from schema evolution. ^[merge-into-databricks-on-aws.md]

`DEFAULT` can be used as an expression in the `VALUES` list to explicitly insert the column default value. ^[merge-into-databricks-on-aws.md]

## Examples

```sql
-- Insert all source rows that have no match in the target.
MERGE INTO target USING source
  ON target.key = source.key
  WHEN NOT MATCHED THEN INSERT *;

-- Conditionally insert only source rows created within the last day.
MERGE INTO target USING source
  ON target.key = source.key
  WHEN NOT MATCHED BY TARGET AND source.created_at > now() - INTERVAL '1' DAY
    THEN INSERT (created_at, value) VALUES (source.created_at, DEFAULT);

-- Insert all columns except `last_updated`, which is set to null in target.
MERGE INTO target USING source
  ON target.key = source.key
  WHEN NOT MATCHED THEN INSERT * EXCEPT (last_updated);
```

^[merge-into-databricks-on-aws.md]

## Applicability

The `WHEN NOT MATCHED` clause is supported in Databricks SQL and Databricks Runtime 12.2 LTS and above. `INSERT *` and `INSERT (columns) VALUES` are available from Databricks Runtime 11.3 LTS and above. ^[merge-into-databricks-on-aws.md]

## Related Concepts

- [MERGE INTO](/concepts/merge-into-delta-lake.md) – The parent statement that combines insert, update, and delete logic.
- [WHEN MATCHED (UPDATE/DELETE) Clause](/concepts/when-matched-clause.md) – Actions for rows that have a match in the target.
- [WHEN NOT MATCHED BY SOURCE (UPDATE/DELETE) Clause](/concepts/when-not-matched-by-source-clause.md) – Actions for target rows without a source match.
- [Delta Lake](/concepts/delta-lake.md) – The storage layer that supports the MERGE operation.
- Schema Evolution – Automatic adjustment of target table schema during MERGE.

## Sources

- merge-into-databricks-on-aws.md

# Citations

1. [merge-into-databricks-on-aws.md](/references/merge-into-databricks-on-aws-b9eee097.md)
