---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 41ce67600928f206ea5a5352af8f21a9abf5db0d1f8a6e3c670d6bbd8602842e
  pageDirectory: concepts
  sources:
    - copy-into-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - copy-into-file-selection-files-and-pattern
    - PATTERN) and COPY INTO File Selection (FILES
    - CIFS(AP
  citations:
    - file: copy-into-databricks-on-aws.md
title: COPY INTO File Selection (FILES and PATTERN)
description: "Two mutually exclusive mechanisms for selecting which files to ingest: listing specific file names (FILES, up to 1000) or using a glob pattern (PATTERN)."
tags:
  - sql
  - file-selection
  - data-ingestion
timestamp: "2026-06-19T14:27:45.660Z"
---

# COPY INTO File Selection (FILES and PATTERN)

**COPY INTO File Selection** refers to the two mutually exclusive mechanisms for specifying which files to load from a source directory when using the `COPY INTO` command in Databricks SQL and Databricks Runtime. These mechanisms are the `FILES` parameter, which accepts an explicit list of file names, and the `PATTERN` parameter, which uses a glob pattern to match files.

## Overview

The `COPY INTO` command loads data from a file location into a Delta table. To control which files are ingested from the source directory, you can use either `FILES` or `PATTERN`, but not both. Each provides a different way to target specific files for loading. ^[copy-into-databricks-on-aws.md]

## FILES Parameter

The `FILES` parameter takes a list of file names to load from the source directory. This is useful when you know the exact filenames you want to ingest and want to load only those specific files.

```sql
COPY INTO my_table
FROM 's3://my-bucket/data/'
FILEFORMAT = JSON
FILES = ('file1.json', 'file2.json', 'file3.json')
```

### Limitations

- The list is limited to **1000 files**. ^[copy-into-databricks-on-aws.md]
- Cannot be specified together with `PATTERN`. ^[copy-into-databricks-on-aws.md]

## PATTERN Parameter

The `PATTERN` parameter accepts a glob pattern that identifies which files to load from the source directory. This is useful when you want to load files that match a naming convention without listing each file individually.

```sql
COPY INTO my_table
FROM 's3://my-bucket/data/'
FILEFORMAT = JSON
PATTERN = '*.json'
```

### Glob Pattern Syntax

The glob pattern follows standard glob syntax, where:
- `*` matches any sequence of characters (except `/`)
- `?` matches any single character (except `/`)
- `[abc]` matches any character in the set
- `[a-z]` matches any character in the range

### Limitations

- Cannot be specified together with `FILES`. ^[copy-into-databricks-on-aws.md]

## Choosing Between FILES and PATTERN

| Scenario | Recommended Parameter |
|----------|----------------------|
| You know the exact filenames to load (up to 1000) | `FILES` |
| You want to load files matching a naming pattern (e.g., all `.csv` files, files starting with `2024-`) | `PATTERN` |
| You need to load more than 1000 specific files | Use `PATTERN` with an appropriate glob, or use Auto Loader |

### Example: Loading files for a specific date

```sql
-- Using PATTERN to load files from a specific date
COPY INTO daily_sales
FROM 's3://my-bucket/sales/'
FILEFORMAT = PARQUET
PATTERN = '2024-01-15_*.parquet'
```

### Example: Loading specific files by name

```sql
-- Using FILES to load only the files you need
COPY INTO archive
FROM 's3://my-bucket/exports/'
FILEFORMAT = CSV
FILES = ('export_2024_Q1.csv', 'export_2024_Q2.csv')
```

## Idempotency and File Selection

`COPY INTO` is a retryable and idempotent operation — files in the source location that have already been loaded are skipped. This behavior applies regardless of whether you use `FILES` or `PATTERN`. If a file has been previously loaded by a `COPY INTO` statement against the same table, it will not be loaded again, even if the file has been modified. ^[copy-into-databricks-on-aws.md]

If you need to reload files that were previously ingested, set the `COPY_OPTIONS` parameter `force` to `true`:

```sql
COPY INTO my_table
FROM 's3://my-bucket/data/'
FILEFORMAT = PARQUET
PATTERN = '*.parquet'
COPY_OPTIONS ('force' = 'true')
```

## Related Concepts

- [COPY INTO](/concepts/copy-into-command.md) — The overall command for loading data into Delta tables
- Auto Loader — Recommended alternative for ingesting directories with very large numbers of files
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format for tables loaded by COPY INTO
- File Metadata Column — Accessing metadata for file-based data sources
- Cloud Object Storage — Managing external data sources for ingestion

## Sources

- copy-into-databricks-on-aws.md

# Citations

1. [copy-into-databricks-on-aws.md](/references/copy-into-databricks-on-aws-02102312.md)
