---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 725dbf2ec71e06b59e3a8bd0ddc9bb99ba3521e4f24af57bd1e4f9add001451e
  pageDirectory: concepts
  sources:
    - merge-into-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - default-keyword-in-merge-actions
    - DKIMA
  citations:
    - file: merge-into-databricks-on-aws.md
title: DEFAULT Keyword in MERGE Actions
description: The DEFAULT keyword can be used as an expression in UPDATE SET and INSERT VALUES clauses to explicitly set a column to its default value (Databricks Runtime 11.3 LTS+).
tags:
  - delta-lake
  - sql
  - default-values
timestamp: "2026-06-19T19:31:55.110Z"
---

---
title: DEFAULT Keyword in MERGE Actions
summary: The `DEFAULT` keyword can be used as a value expression in `UPDATE SET` and `INSERT ... VALUES` clauses within `MERGE INTO` statements on Delta tables to explicitly set a column to its defined default value.
sources:
  - merge-into-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T18:07:30.341Z"
updatedAt: "2026-06-19T18:07:30.341Z"
tags:
  - sql
  - delta-lake
  - merge
  - default
aliases:
  - default-keyword-in-merge-actions
  - default-merge
confidence: 0.99
provenanceState: extracted
inferredParagraphs: 0
---

# DEFAULT Keyword in MERGE Actions

The **`DEFAULT` keyword** is a SQL expression that can be used in `MERGE INTO` statements on [Delta Lake](/concepts/delta-lake.md) tables to explicitly set a target column to its defined default value. It is supported in `UPDATE SET` and `INSERT ... VALUES` clauses within the `WHEN MATCHED`, `WHEN NOT MATCHED`, and `WHEN NOT MATCHED BY SOURCE` actions.

## Syntax

The `DEFAULT` keyword appears in three action types in the `MERGE` syntax:

- **`UPDATE SET`**:  
  `UPDATE SET { column = { expr | DEFAULT } } [, ...]`  
  Specifying `DEFAULT` as the expression updates the column to its default value. ^[merge-into-databricks-on-aws.md]

- **`INSERT ... VALUES`**:  
  `INSERT (column1 [, ...] ) VALUES ( expr | DEFAULT ] [, ...] )`  
  Specifying `DEFAULT` as the value inserts the column’s default value. ^[merge-into-databricks-on-aws.md]

- **`WHEN NOT MATCHED BY SOURCE` `UPDATE SET`**:  
  `UPDATE SET { column = { expr | DEFAULT } } [, ...]`  
  The same syntax applies when updating target rows that have no match in the source. ^[merge-into-databricks-on-aws.md]

## Usage Details

- **`WHEN MATCHED` – `UPDATE SET`**:  
  In a matched action, you can use `DEFAULT` in place of an explicit expression to reset a column to its default value. For example:  
  ```sql
  MERGE INTO target USING source
  ON target.key = source.key
  WHEN MATCHED THEN UPDATE SET target.value = DEFAULT
  ```  
  This sets `target.value` to the column’s default. ^[merge-into-databricks-on-aws.md]

- **`WHEN NOT MATCHED` – `INSERT ... VALUES`**:  
  When inserting a new row, you can use `DEFAULT` for any listed column. For example:  
  ```sql
  MERGE INTO target USING source
  ON target.key = source.key
  WHEN NOT MATCHED THEN INSERT (created_at, value) VALUES (source.created_at, DEFAULT)
  ```  
  The `value` column receives its default value. ^[merge-into-databricks-on-aws.md]

- **`WHEN NOT MATCHED BY SOURCE` – `UPDATE SET`**:  
  The same `<code>DEFAULT</code> usage applies when updating target rows that are not matched by the source. For example:  
  ```sql
  MERGE INTO target USING source
  ON target.key = source.key
  WHEN NOT MATCHED BY SOURCE THEN UPDATE SET target.value = DEFAULT
  ```  

- **Column Defaults**:  
  A column’s default value is defined at table creation or via `ALTER TABLE … ALTER COLUMN … SET DEFAULT`. If no default is defined, `DEFAULT` resolves to `NULL`. ^[merge-into-databricks-on-aws.md]

- **Applicable Types**:  
  The `DEFAULT` keyword is supported in:
  - `WHEN MATCHED THEN UPDATE SET` (since Databricks Runtime 11.3 LTS)
  - `WHEN NOT MATCHED THEN INSERT ... VALUES` (since Databricks Runtime 11.3 LTS)
  - `WHEN NOT MATCHED BY SOURCE THEN UPDATE SET` (since Databricks Runtime 11.3 LTS)

  See the official [MERGE INTO](/concepts/merge-into-delta-lake.md) documentation for version-specific availability.

## Notes

- `DEFAULT` cannot be used in `UPDATE SET *` or `INSERT *` forms; it is only valid in the explicit column‑list syntax.
- Using `DEFAULT` in an `UPDATE SET` for a column that has no default value does not cause an error; it sets the column to `NULL`.
- The `DEFAULT` keyword is a SQL standard expression, not a Databricks extension.

## Related Concepts

- [MERGE INTO](/concepts/merge-into-delta-lake.md) – The full command syntax and usage.
- [Delta Lake](/concepts/delta-lake.md) – The storage layer that supports `MERGE` operations.
- [Column Default Values](/concepts/featurespec-default-values.md) – How to define and alter default values on Delta table columns.
- UPDATE – The standalone update statement (also supports `DEFAULT`).
- INSERT INTO – The standalone insert statement (also supports `DEFAULT`).

## Sources

- merge-into-databricks-on-aws.md

# Citations

1. [merge-into-databricks-on-aws.md](/references/merge-into-databricks-on-aws-b9eee097.md)
