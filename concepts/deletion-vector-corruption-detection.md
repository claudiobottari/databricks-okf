---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8b159edb8d3a142af4e7e4222e1df32a07a961ca23cbda0156ccec1a96e70a3b
  pageDirectory: concepts
  sources:
    - fsck-repair-table-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deletion-vector-corruption-detection
    - DVCD
    - Deletion Vector Corruption
    - Data Corruption
    - Data File Corruption
  citations:
    - file: fsck-repair-table-databricks-on-aws.md
title: Deletion Vector corruption detection
description: Capability of FSCK REPAIR TABLE to detect corruption in deletion vectors of Delta Lake tables
tags:
  - delta-lake
  - databricks
  - deletion-vectors
  - corruption
timestamp: "2026-06-19T10:40:21.034Z"
---

# Deletion Vector Corruption Detection

**Deletion Vector Corruption Detection** is a feature of the `FSCK REPAIR TABLE` command in Delta Lake that identifies deletion vectors whose contents are corrupted or unreadable. Deletion vectors are auxiliary files that track which rows in a data file have been logically deleted without rewriting the file. When a deletion vector becomes corrupt, query results may be incorrect because the Delta engine cannot determine which rows should be excluded. ^[fsck-repair-table-databricks-on-aws.md]

## Detection Mechanism

The `FSCK REPAIR TABLE` command detects deletion vector corruption when run with the `VERIFY ALL FILES` option. This option performs a full content verification of all files referenced in the Delta table's transaction log, including deletion vectors. ^[fsck-repair-table-databricks-on-aws.md]

### Command Syntax

```sql
FSCK REPAIR TABLE table_name VERIFY ALL FILES [DRY RUN]
```

The `DRY RUN` modifier reports issues without attempting repairs. ^[fsck-repair-table-databricks-on-aws.md]

## Output Columns

When deletion vector corruption is detected, the command reports it in the `deletionVectorCorrupt` column of the output. The output includes the following relevant columns: ^[fsck-repair-table-databricks-on-aws.md]

| Column | Description |
|--------|-------------|
| `deletionVectorPath` | Path to the deletion vector file |
| `deletionVectorFileMissing` | Whether the deletion vector file is missing |
| `deletionVectorCorrupt` | Whether the deletion vector content is corrupt or unreadable |

## Example

The following example shows a table where `file2.parquet` has a corrupt deletion vector `dv2.bin`: ^[fsck-repair-table-databricks-on-aws.md]

```sql
FSCK REPAIR TABLE t VERIFY ALL FILES DRY RUN;
```

| dataFilePath | dataFileMissing | deletionVectorPath | deletionVectorFileMissing | deletionVectorCorrupt |
|---|---|---|---|---|
| file1.parquet | false | null | false | false |
| file2.parquet | false | dv2.bin | false | true |

In this output, `file2.parquet` exists and is readable, but its associated deletion vector `dv2.bin` has corrupt content. The `deletionVectorCorrupt` column shows `true` for this file. ^[fsck-repair-table-databricks-on-aws.md]

## Related Issues

Deletion vector corruption is distinct from other file integrity issues that `FSCK REPAIR TABLE` can detect: ^[fsck-repair-table-databricks-on-aws.md]

- **Missing deletion vectors** — The deletion vector file does not exist at the expected path (reported as `deletionVectorFileMissing = true`).
- **Data file corruption** — The data file itself is corrupt or unreadable (reported as `fileUnreadable = true`).
- **CRC checksum corruption** — A checkpoint file has CRC checksum corruption (reported as `fileCrcCorrupt = true`).
- **Invalid partition values** — A data file has partition values that violate the table schema (reported as `fileMetadataHasInvalidPartitionValues = true`).

## Impact

A corrupt deletion vector can cause the Delta engine to incorrectly include or exclude rows during queries, leading to inaccurate results. The corruption affects all operations that read the affected data file, including `SELECT`, `UPDATE`, `DELETE`, and `MERGE` statements. ^[fsck-repair-table-databricks-on-aws.md]

## Related Concepts

- [FSCK REPAIR TABLE](/concepts/fsck-repair-table.md) — The command used to detect and repair Delta table metadata issues
- [Deletion Vectors](/concepts/deletion-vectors.md) — Auxiliary files that track logically deleted rows in Delta tables
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that provides ACID transactions and file management
- Data File Corruption Detection — Detection of unreadable data files
- [Checkpoint CRC Corruption Detection](/concepts/checkpoint-crc-corruption-detection.md) — Detection of checksum corruption in checkpoint files
- Missing File Detection — Detection of missing data or deletion vector files

## Sources

- fsck-repair-table-databricks-on-aws.md

# Citations

1. [fsck-repair-table-databricks-on-aws.md](/references/fsck-repair-table-databricks-on-aws-0ce9a31c.md)
