---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 241ef09f7829e885a5ab88132463fea0403db2dd250ada82878214dd42bb41b9
  pageDirectory: concepts
  sources:
    - copy-into-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - by-position-column-mapping
    - BPCM
  citations:
    - file: copy-into-databricks-on-aws.md
title: BY POSITION Column Mapping
description: Syntax for matching source columns to target Delta table columns by ordinal position, primarily for headerless CSV files.
tags:
  - databricks
  - sql
  - csv
  - schema-mapping
timestamp: "2026-06-18T14:45:21.108Z"
---

# BY POSITION Column Mapping

**BY POSITION Column Mapping** is a syntax option in the [COPY INTO](/concepts/copy-into-command.md) command that matches source columns to target [Delta table](/concepts/delta-lake-table.md) columns by ordinal position rather than by name. It is designed specifically for **headerless CSV** files and is only supported when `FILEFORMAT = CSV` and `FORMAT_OPTIONS ("headers" = "false")` (the default for CSV). ^[copy-into-databricks-on-aws.md]

## Overview

When loading data from a CSV file that lacks a header row, `COPY INTO` must know how to align the positional columns in the file with the columns of the target table. The `BY POSITION` clause provides two ways to specify that alignment:

- **Automatic mapping** by ordinal position.
- **Explicit column list** using target table column names in parentheses.

Both approaches bypass the default name-based matching and require that the number of source columns equals the number of relevant target columns. ^[copy-into-databricks-on-aws.md]

## Syntax Options

### Option 1: `BY POSITION`

When `BY POSITION` is used alone (without a column list), source columns are automatically matched to target table columns by their ordinal position:

- The original table column order and column names are ignored for matching.
- `IDENTITY` columns and `GENERATED` columns in the target table are **skipped** during matching.
- If the number of source columns does not equal the number of filtered target columns (i.e., total columns minus `IDENTITY` and `GENERATED` columns), `COPY INTO` raises an error.
- Type casting of the matched columns is performed automatically. ^[copy-into-databricks-on-aws.md]

```sql
COPY INTO target_table
FROM '/path/to/headerless.csv'
FILEFORMAT = CSV
BY POSITION
FORMAT_OPTIONS ("headers" = "false")
```

### Option 2: `( col_name [, col_name ...] )`

An explicit column name list specifies which target columns should receive the source data, in the order they appear in the file:

- Source columns are matched to the listed target columns by relative ordinal position (first source column → first listed column, etc.).
- `IDENTITY` columns and `GENERATED` columns **cannot** appear in the column list; if they are included, `COPY INTO` raises an error.
- Column names in the list must not be duplicated.
- The number of source columns must equal the number of listed columns.
- Columns not listed receive their default value, or `NULL` if no default exists. If an unlisted column is not nullable, `COPY INTO` raises an error. ^[copy-into-databricks-on-aws.md]

```sql
COPY INTO target_table (col1, col3, col2)
FROM '/path/to/headerless.csv'
FILEFORMAT = CSV
FORMAT_OPTIONS ("headers" = "false")
```

## Key Considerations

- `BY POSITION` is only valid for CSV files with `"headers" = "false"`. It does not apply to other file formats. ^[copy-into-databricks-on-aws.md]
- The automatic `BY POSITION` variant ignores `IDENTITY` and `GENERATED` columns, making it suitable for tables that auto-generate primary keys or timestamps.
- The explicit column list variant gives precise control over column mapping and default value assignment for unmapped columns.
- Both options raise errors if the number of source columns does not match the expected number of target columns, ensuring data integrity.

## Related Concepts

- [COPY INTO](/concepts/copy-into-command.md) — The broader command for loading data into Delta tables.
- CSV File Format Options — Configuration for reading CSV files.
- Delta Table Schema — How table schemas interact with data ingestion.
- IDENTITY Column — Auto‑generated column that is automatically skipped by `BY POSITION`.
- GENERATED Column — Computed column that is automatically skipped by `BY POSITION`.

## Sources

- copy-into-databricks-on-aws.md

# Citations

1. [copy-into-databricks-on-aws.md](/references/copy-into-databricks-on-aws-02102312.md)
