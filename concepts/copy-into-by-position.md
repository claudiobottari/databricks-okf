---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fb08734021361590846f1f1e0654ff20a9823f0a99a90a9a35ec76f556a0b195
  pageDirectory: concepts
  sources:
    - copy-into-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - copy-into-by-position
    - CIBP
  citations:
    - file: copy-into-databricks-on-aws.md
title: COPY INTO BY POSITION
description: A syntax option for matching source columns to target Delta table columns by ordinal position rather than by name, only supported for headerless CSV files.
tags:
  - sql
  - csv
  - data-ingestion
timestamp: "2026-06-19T14:26:44.666Z"
---

# COPY INTO BY POSITION

**COPY INTO BY POSITION** is a variant of the `COPY INTO` SQL command in Databricks that loads data from headerless CSV files into a Delta table by matching source columns to target table columns based on their ordinal position (column order) rather than by name. This syntax is designed for scenarios where CSV files lack column headers and the schema must be inferred from the file’s column order. ^[copy-into-databricks-on-aws.md]

## Syntax

The command supports two syntax forms:

**Form 1 – `BY POSITION` keyword:**

```sql
COPY INTO target_table
  BY POSITION
  FROM source_clause
  FILEFORMAT = CSV
  [ FORMAT_OPTIONS ("headers" = "false") ]
  ...
```

**Form 2 – Explicit column list:**

```sql
COPY INTO target_table ( col_name [, col_name ...] )
  FROM source_clause
  FILEFORMAT = CSV
  ...
```

Both forms require `FILEFORMAT = CSV`. The `FORMAT_OPTIONS` setting `"headers" = "false"` is the default and may be omitted. ^[copy-into-databricks-on-aws.md]

## How `BY POSITION` matching works

When `BY POSITION` is specified, source columns are matched to target table columns by their ordinal position in the file, not by name. Type casting of the matched columns is performed automatically. ^[copy-into-databricks-on-aws.md]

Key behaviors:

- The default name‑based matching is **not** used. Column names in the source file are ignored.
- IDENTITY columns and GENERATED columns in the target table are skipped during matching — they are not included in the positional comparison.
- If the number of source columns does not equal the number of filtered target table columns (after excluding identity and generated columns), `COPY INTO` raises an error.

^[copy-into-databricks-on-aws.md]

## Explicit column list matching

When an explicit column list is provided in parentheses (e.g., `(col_name1, col_name2)`), matching works as follows: ^[copy-into-databricks-on-aws.md]

- Source columns are matched to the **specified** target table columns by relative ordinal position using the column name list. The original table column order and column names are **not** used for matching.
- IDENTITY columns and GENERATED columns cannot appear in the column name list; including them causes `COPY INTO` to raise an error.
- The specified columns cannot be duplicated.
- When the number of source columns does not equal the number of specified table columns, `COPY INTO` raises an error.
- For columns **not** specified in the column name list, `COPY INTO` assigns default values (if any exist) or assigns `NULL`. If any unspecified column is not nullable, `COPY INTO` raises an error.

^[copy-into-databricks-on-aws.md]

## Supported file format

`COPY INTO BY POSITION` is **only** supported for headerless CSV files. You must specify `FILEFORMAT = CSV`. The `FORMAT_OPTIONS` must include `("headers" = "false")`, though this is the default setting. ^[copy-into-databricks-on-aws.md]

## Common use cases

This syntax is useful when:

- You have CSV files without column headers and need to load data into a Delta table with a predefined schema.
- The source file column order is known and matches the target table column order (excluding identity and generated columns).
- You want to load only specific columns from a source file by explicitly naming the target columns, leaving other columns to receive default values.

## Related concepts

- [COPY INTO](/concepts/copy-into-command.md) — The general data loading command for Delta tables.
- [Delta tables](/concepts/delta-lake-table.md) — The target storage format for `COPY INTO` operations.
- CSV file format — The source file format for `BY POSITION` matching.
- IDENTITY columns — Auto‑incrementing columns that are skipped in positional matching.
- GENERATED columns — Computed columns that are skipped in positional matching.
- Auto Loader — An alternative ingestion mechanism for cloud object storage.
- File metadata column — Metadata access for file‑based data sources.

## Sources

- copy-into-databricks-on-aws.md

# Citations

1. [copy-into-databricks-on-aws.md](/references/copy-into-databricks-on-aws-02102312.md)
