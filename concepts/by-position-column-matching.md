---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 07db68d36e1470d37c0a764ac944f9c9e4811c323aa524cf470831993a515311
  pageDirectory: concepts
  sources:
    - copy-into-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - by-position-column-matching
    - BPCM
  citations:
    - file: copy-into-databricks-on-aws.md
title: BY POSITION Column Matching
description: A syntax option for matching source columns to target table columns by ordinal position, supporting headerless CSV files
tags:
  - databricks
  - sql
  - csv-ingestion
timestamp: "2026-06-19T09:25:17.467Z"
---

# BY POSITION Column Matching

BY POSITION column matching is a syntax variant of the [COPY INTO](/concepts/copy-into-command.md) command that matches source columns to target table columns by ordinal position rather than by name. When this matching mode is used, Databricks SQL automatically casts the data types of the matched columns. ^[copy-into-databricks-on-aws.md]

## Requirements

BY POSITION column matching is only supported for headerless CSV files. The command must specify `FILEFORMAT = CSV` and `FORMAT_OPTIONS ("headers" = "false")` (which is the default for CSV). ^[copy-into-databricks-on-aws.md]

## Syntax Options

Two syntax forms are available:

### 1. `BY POSITION` (automatic matching)

```sql
COPY INTO target_table
FROM source
FILEFORMAT = CSV
FORMAT_OPTIONS ("headers" = "false")
BY POSITION
```

In this form, source columns are matched to target table columns automatically by their ordinal position in the input file and the table schema. The default name matching is not used. `IDENTITY` columns and `GENERATED` columns of the target table are ignored when matching the source columns. If the number of source columns does not equal the number of filtered target table columns (excluding identity and generated columns), `COPY INTO` raises an error. ^[copy-into-databricks-on-aws.md]

### 2. `( col_name [, col_name ...] )` (explicit column list)

```sql
COPY INTO target_table (col1, col2, col3)
FROM source
FILEFORMAT = CSV
FORMAT_OPTIONS ("headers" = "false")
```

With this syntax, source columns are matched to the specified target table columns by relative ordinal position using a parenthesized list of column names. The original table column order and column names are not used for matching. `IDENTITY` columns and `GENERATED` columns cannot appear in this list; if they do, `COPY INTO` raises an error. The specified columns cannot be duplicated. If the number of source columns does not equal the number of specified table columns, an error is raised. For columns that are not specified in the list, `COPY INTO` assigns default values if any exist, or `NULL` otherwise. If any such column is not nullable, an error is raised. ^[copy-into-databricks-on-aws.md]

## Behavior Summary

- **Ordinal matching**: Source columns are matched to target columns based on their order in the file and table, not by name.
- **Type casting**: Automatic type casting is applied to matched columns.
- **Identity and generated columns**: Ignored in the automatic `BY POSITION` form; cannot appear in the column list form.
- **Error conditions**: Mismatched column counts cause the command to fail.
- **Schema evolution**: Can be combined with `COPY_OPTIONS ("mergeSchema" = "true")` to evolve the target schema as needed.

## Related Concepts

- [COPY INTO](/concepts/copy-into-command.md) — The parent command that supports BY POSITION matching.
- [Delta table](/concepts/delta-lake-table.md) — The target for COPY INTO operations.
- CSV file format — The required source format for BY POSITION matching.
- IDENTITY columns — Automatically populated columns skipped during positional matching.
- GENERATED columns — Computed columns skipped during positional matching.
- Column matching — General concept of matching source fields to target columns.
- Headerless CSV — CSV files without a header row, required for this feature.

## Sources

- copy-into-databricks-on-aws.md

# Citations

1. [copy-into-databricks-on-aws.md](/references/copy-into-databricks-on-aws-02102312.md)
