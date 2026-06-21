---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eb68fdd13da0b6f83eb6e64c85eaf9487bef3ae31a3dc6e2decf7b3a86f1fd88
  pageDirectory: concepts
  sources:
    - fsck-repair-table-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - missing-data-files-and-deletion-vectors
    - deletion vectors and Missing data files
    - MDFADV
  citations:
    - file: fsck-repair-table-databricks-on-aws.md
title: Missing data files and deletion vectors
description: Detection of referenced data files or deletion vectors that are missing from storage in Delta Lake tables
tags:
  - delta-lake
  - databricks
  - data-loss
  - storage
timestamp: "2026-06-19T10:40:31.542Z"
---

#Missing Data Files and Deletion Vectors

**Missing data files and deletion vectors** refer to integrity issues within a [Delta Lake](/concepts/delta-lake.md) table where underlying data files or their associated [deletion vector](/concepts/deletion-vectors.md) binary files are absent from storage. These inconsistencies are detected and reported by the [FSCK REPAIR TABLE](/concepts/fsck-repair-table.md) command during validation scans.

## Overview

In Delta Lake, a table consists of data files (Parquet) and optional deletion vectors that track which rows have been logically deleted without rewriting the data file. If a data file referenced in the transaction log is no longer present on disk, it is considered a missing data file. Similarly, if a deletion vector file (`dv1.bin`, `dv2.bin`, etc.) is referenced by the log but cannot be found, it is a missing deletion vector file. ^[fsck-repair-table-databricks-on-aws.md]

## Detection

The `FSCK REPAIR TABLE` command with different modes can detect missing files. The output includes columns that flag the state of each file:

- `dataFileMissing` — indicates whether a data file listed in the table metadata is absent from the file system.
- `deletionVectorFileMissing` — indicates whether a deletion vector file that the metadata depends on is absent.
- `deletionVectorCorrupt` — when the deletion vector file is present but its contents are corrupt or unreadable.

^[fsck-repair-table-databricks-on-aws.md]

For example, running `FSCK REPAIR TABLE t DRY RUN` on a table where `file1.parquet` is missing and its deletion vector `dv1.bin` is also missing produces output showing both flags as `true`: ^[fsck-repair-table-databricks-on-aws.md]

```
dataFilePath  dataFileMissing deletionVectorPath deletionVectorFileMissing ...
------------  --------------- ------------------ -------------------------
file2.parquet true            dv1.bin            true
```

In contrast, a corrupt deletion vector (e.g., `dv2.bin` that is present but corrupted) is flagged by `deletionVectorCorrupt = true` rather than `deletionVectorFileMissing`. ^[fsck-repair-table-databricks-on-aws.md]

## Resolution

The primary tool for resolving missing data files and deletion vectors is `FSCK REPAIR TABLE`. The command can be run with `DRY RUN` to preview issues without making changes, or without `DRY RUN` to attempt automatic repair. Additional verification checks are provided by the `VERIFY ALL FILES` option, which reads data files to confirm they are readable and checks CRC integrity. ^[fsck-repair-table-databricks-on-aws.md]

Scenarios addressed:

- **Missing data file** — The file is absent; repair may remove the reference from the transaction log or recreate the file from other sources.
- **Missing deletion vector file** — The deletion vector is absent; repair may ignore the deletion mappings or regenerate the vector.
- **Corrupt deletion vector** — The file exists but cannot be parsed; repair may discard the corrupt vector and rebuild it.

## Related Concepts

- [FSCK REPAIR TABLE](/concepts/fsck-repair-table.md) — The SQL command used to detect and fix table integrity issues.
- [Deletion Vectors](/concepts/deletion-vectors.md) — Delta Lake mechanism for marking rows as deleted without rewriting data files.
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format for tables on Databricks.
- Table Maintenance — Regular operations (OPTIMIZE, VACUUM, FSCK) to keep tables performant and consistent.

## Sources

- fsck-repair-table-databricks-on-aws.md

# Citations

1. [fsck-repair-table-databricks-on-aws.md](/references/fsck-repair-table-databricks-on-aws-0ce9a31c.md)
