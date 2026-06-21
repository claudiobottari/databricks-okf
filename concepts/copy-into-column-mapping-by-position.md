---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e7b14a19f841e63efeace33010722e91a462c57f81a0da7ee9f04ed9a6129b6c
  pageDirectory: concepts
  sources:
    - copy-into-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - copy-into-column-mapping-by-position
    - CICM(P
  citations:
    - file: copy-into-databricks-on-aws.md
title: COPY INTO Column Mapping (BY POSITION)
description: Syntax for matching source columns to target Delta table columns by ordinal position, supporting headerless CSV and explicit column name lists.
tags:
  - databricks
  - sql
  - csv
  - schema-mapping
timestamp: "2026-06-19T17:53:28.631Z"
---

# COPY INTO Column Mapping (BY POSITION)

**COPY INTO Column Mapping (BY POSITION)** is a syntax option for the [COPY INTO](/concepts/copy-into-command.md) command in Databricks SQL and Databricks Runtime that matches source columns to target table columns by their ordinal position in the file rather than by column name. This is useful for loading data from files that lack headers or where the column order differs from the target table schema. ^[copy-into-databricks-on-aws.md]

## Overview

The `BY POSITION` clause tells `COPY INTO` to map columns based on their sequential position in the source file to the corresponding position in the target Delta table. Type casting of the matched columns is handled automatically. ^[copy-into-databricks-on-aws.md]

## Syntax

```sql
COPY INTO target_table BY POSITION
FROM source_clause
FILEFORMAT = CSV
FORMAT_OPTIONS ("headers" = "false")
```

## Requirements

`BY POSITION` is **only supported for headerless CSV files**. You must specify `FILEFORMAT = CSV` and either explicitly set `FORMAT_OPTIONS ("headers" = "false")` or rely on the default behavior (headerless CSV is the default). ^[copy-into-databricks-on-aws.md]

## Behavior

When using `BY POSITION`:

- The default name-based column matching is **not used**. Columns are matched solely by position. ^[copy-into-databricks-on-aws.md]
- Identity Column (Databricks)|IDENTITY columns and Generated Column (Databricks)|GENERATED columns in the target table are **ignored** when matching source columns. ^[copy-into-databricks-on-aws.md]
- If the number of source columns does not equal the number of filtered target columns (excluding `IDENTITY` and `GENERATED` columns), `COPY INTO` raises an error. ^[copy-into-databricks-on-aws.md]

## Alternative: Named Column List

Instead of `BY POSITION`, you can explicitly specify a list of target column names in parentheses:

```sql
COPY INTO target_table (col1, col2, col3)
FROM ...
```

This also matches by relative ordinal position but uses your specified column list rather than the table's natural column order. ^[copy-into-databricks-on-aws.md]

When using a named column list:
- The original table column order and column names are not used for matching. ^[copy-into-databricks-on-aws.md]
- `IDENTITY` and `GENERATED` columns **cannot** be specified in the column name list, or `COPY INTO` raises an error. ^[copy-into-databricks-on-aws.md]
- Specified columns cannot be duplicated. ^[copy-into-databricks-on-aws.md]
- When the number of source columns does not equal the specified table columns, `COPY INTO` raises an error. ^[copy-into-databricks-on-aws.md]
- For columns not specified in the list, `COPY INTO` assigns default values (if any) or `NULL`. If any unspecified column is not nullable, `COPY INTO` raises an error. ^[copy-into-databricks-on-aws.md]

## Comparison: Default Name Matching vs. BY POSITION vs. Column Name List

| Feature | Default (Name Matching) | BY POSITION | Column Name List |
|---|---|---|---|
| Matching method | By column name | By ordinal position | By ordinal position relative to specified list |
| File format | Any supported format | CSV only (headerless) | CSV only (headerless) |
| Headers required | Yes (or schema inference) | No | No |
| IDENTITY/GENERATED columns | Matched by name | Ignored in matching | Cannot be specified |
| Error on column count mismatch | No (uses schema evolution or projection) | Yes | Yes |

## Related Concepts

- [COPY INTO](/concepts/copy-into-command.md) – The parent command for incremental data loading into Delta tables.
- COPY INTO Column Mapping (Name) – The default name-based column mapping approach.
- [Delta Table](/concepts/delta-lake-table.md) – The target table type for `COPY INTO` operations.
- Identity Column (Databricks) – Auto-incrementing columns that are special-cased during position-based loading.
- Generated Column (Databricks) – Computed columns that are excluded from source matching.
- CSV File Loading on Databricks – General considerations for loading CSV data.
- Format Options for COPY INTO – Additional `FORMAT_OPTIONS` that can be used with `BY POSITION`.

## Sources

- copy-into-databricks-on-aws.md

# Citations

1. [copy-into-databricks-on-aws.md](/references/copy-into-databricks-on-aws-02102312.md)
