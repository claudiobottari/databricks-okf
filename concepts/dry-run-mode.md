---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c5e6770f2ac7360c516f49b3a8872c3e53e5715f80e2365d190d08815d06f624
  pageDirectory: concepts
  sources:
    - fsck-repair-table-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dry-run-mode
    - DRM
    - DRY RUN
  citations:
    - file: fsck-repair-table-databricks-on-aws.md
title: DRY RUN mode
description: Preview mode for FSCK REPAIR TABLE that reports detected issues without making any changes
tags:
  - delta-lake
  - databricks
  - safety
  - verification
timestamp: "2026-06-19T10:40:21.835Z"
---

# DRY RUN Mode

**DRY RUN mode** is an option available with the `FSCK REPAIR TABLE` command in [Delta Lake](/concepts/delta-lake.md) that reports detected issues in a table's metadata or underlying files without performing any repairs. It provides a safe, read-only way to inspect data integrity problems before deciding whether to apply fixes. ^[fsck-repair-table-databricks-on-aws.md]

## Overview

The `DRY RUN` clause is appended to `FSCK REPAIR TABLE` to simulate what the repair operation would correct. No changes are made to the table; instead, the command outputs a result set listing each file or checkpoint that has an anomaly. This allows administrators to assess the scope of corruption or missing files before committing to a repair. ^[fsck-repair-table-databricks-on-aws.md]

## Supported Variants

| Command | Behavior |
|---------|----------|
| `FSCK REPAIR TABLE <name> DRY RUN` | Reports missing data files, missing deletion vector files, invalid partition values, and other file-level issues. |
| `FSCK REPAIR TABLE <name> METADATA ONLY DRY RUN` | Checks only the Delta transaction log metadata (e.g., checkpoint CRC integrity) without scanning data files or deletion vectors. |
| `FSCK REPAIR TABLE <name> VERIFY ALL FILES DRY RUN` | Performs a more thorough check that also validates file contents (e.g., detects unreadable data files and corrupt deletion vectors). |

All variants are read-only. ^[fsck-repair-table-databricks-on-aws.md]

## Output Columns

The result of a `DRY RUN` is a table with the following columns:

| Column | Type | Description |
|--------|------|-------------|
| `dataFilePath` | string | Path to a data file (Parquet) that was checked. |
| `dataFileMissing` | boolean | `true` if the data file is referenced in the log but does not exist on storage. |
| `deletionVectorPath` | string | Path to the deletion vector file associated with the data file, if any. |
| `deletionVectorFileMissing` | boolean | `true` if the deletion vector file is referenced but does not exist. |
| `checkpointFilePath` | string | Path to a checkpoint file that was checked (only in `METADATA ONLY` mode). |
| `fileCrcCorrupt` | boolean | `true` if the CRC checksum of the checkpoint file is invalid. |
| `fileUnreadable` | boolean | `true` if the data file exists but cannot be read (e.g., corrupt format). |
| `fileMetadataHasInvalidPartitionValues` | boolean | `true` if the file’s partition column value violates the table’s schema (e.g., `NULL` in a `NOT NULL` partition column). |
| `deletionVectorCorrupt` | boolean | `true` if the deletion vector file is present but its contents are corrupt. |

Each row represents one file or checkpoint that failed one or more checks. ^[fsck-repair-table-databricks-on-aws.md]

## Usage Recommendations

- Run `DRY RUN` before any repair operation to understand what changes will be made.
- Use `METADATA ONLY DRY RUN` to quickly check transaction log integrity without scanning all data files.
- Use `VERIFY ALL FILES DRY RUN` for a comprehensive health check, especially if you suspect file-level corruption.
- The `DRY RUN` results can be saved or queried further (e.g., export to a table) for reporting and monitoring.

## Related Concepts

- [FSCK REPAIR TABLE](/concepts/fsck-repair-table.md) — The parent command for repairing Delta table metadata.
- [Delta Lake](/concepts/delta-lake.md) — The storage layer that provides ACID transactions and time travel.
- [Deletion Vectors](/concepts/deletion-vectors.md) — Files that mark logically deleted rows in a data file.
- [Delta transaction log](/concepts/delta-transaction-log.md) — The ordered record of all changes to a Delta table.
- Checkpoint Integrity — Validation of CRC checksums in checkpoint files.

## Sources

- fsck-repair-table-databricks-on-aws.md

# Citations

1. [fsck-repair-table-databricks-on-aws.md](/references/fsck-repair-table-databricks-on-aws-0ce9a31c.md)
