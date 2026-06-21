---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4d80cca1f9892462c7208dbe48050b33716b340d3160807227ee4ae4a3c21b72
  pageDirectory: concepts
  sources:
    - fsck-repair-table-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - verify-all-files-mode
    - VAFM
  citations:
    - file: fsck-repair-table-databricks-on-aws.md
title: VERIFY ALL FILES mode
description: FSCK REPAIR TABLE mode that checks all files by reading their contents, including data files and deletion vectors
tags:
  - delta-lake
  - databricks
  - verification
  - integrity
timestamp: "2026-06-19T10:40:25.207Z"
---

# VERIFY ALL FILES mode

**VERIFY ALL FILES mode** is a flag used with the `FSCK REPAIR TABLE` command in [Delta Lake](/concepts/delta-lake.md) that extends the repair check to perform a full content-level verification of every data file and deletion vector, rather than relying solely on metadata or CRC checksums. ^[fsck-repair-table-databricks-on-aws.md]

## How It Works

When `VERIFY ALL FILES` is specified, Databricks reads each data file and its associated deletion vector (if any) to determine:

- Whether the data file is **unreadable** (e.g., corrupt or truncated). ^[fsck-repair-table-databricks-on-aws.md]
- Whether the deletion vector itself is **corrupt** (e.g., internal consistency failures). ^[fsck-repair-table-databricks-on-aws.md]

This is a significantly more thorough check than the default `DRY RUN` mode, which only determines whether files are missing from the file system or partition values are invalid. ^[fsck-repair-table-databricks-on-aws.md]

## Comparison with Other Modes

The following table (based on the source material) summarises what each mode detects:

| Check type                                  | `DRY RUN` (no flag) | `METADATA ONLY DRY RUN` | `VERIFY ALL FILES DRY RUN` |
|---------------------------------------------|---------------------|--------------------------|----------------------------|
| Missing data files                          | ✓                   | ✗                        | ✓                          |
| Missing deletion vectors                     | ✓                   | ✗                        | ✓                          |
| CRC checksum corruption (checkpoint files)  | ✗                   | ✓                        | ✓                          |
| Invalid partition values                    | ✓                   | ✗                        | ✓                          |
| Data file unreadable (content corruption)    | ✗                   | ✗                        | ✓                          |
| Deletion vector corruption (content issue)   | ✗                   | ✗                        | ✓                          |

^[fsck-repair-table-databricks-on-aws.md]

- **`DRY RUN` (default)**: Only detects missing files and invalid partition values. It does not open files to verify their content. ^[fsck-repair-table-databricks-on-aws.md]
- **`METADATA ONLY DRY RUN`**: Checks CRC checksum corruption in checkpoint files without scanning the table’s data files. ^[fsck-repair-table-databricks-on-aws.md]
- **`VERIFY ALL FILES DRY RUN`**: Includes all the checks of `DRY RUN` and `METADATA ONLY`, and additionally verifies that every data file is readable and that every deletion vector is internally consistent. ^[fsck-repair-table-databricks-on-aws.md]

## Example Output

The source material shows the following results for a `VERIFY ALL FILES DRY RUN` on a table with two problematic files:

```
dataFilePath  dataFileMissing deletionVectorPath deletionVectorFileMissing checkpointFilePath fileCrcCorrupt fileUnreadable fileMetadataHasInvalidPartitionValues deletionVectorCorrupt
------------- --------------- ------------------ ------------------------- ------------------ -------------- -------------- ------------------------------------- ---------------------
file1.parquet false           null               false                     null               false          true           false                                 false
file2.parquet false           dv2.bin            false                     null               null           null           false                                 true
```

^[fsck-repair-table-databricks-on-aws.md]

In this example:
- `file1.parquet` exists (`dataFileMissing = false`) but is **unreadable** (`fileUnreadable = true`).
- `file2.parquet` exists and is readable, but its deletion vector `dv2.bin` is **corrupt** (`deletionVectorCorrupt = true`).

## When to Use

Use `VERIFY ALL FILES` when you suspect data corruption that is not merely a missing file or a CRC mismatch—for example, after disk failures, interrupted writes, or storage-level anomalies. Because it reads every data file, it is slower and more expensive than other modes, so it should be used sparingly, typically for troubleshooting or after an incident. ^[fsck-repair-table-databricks-on-aws.md]

## Related Concepts

- [FSCK REPAIR TABLE](/concepts/fsck-repair-table.md) – The command that this mode modifies.
- [DRY RUN](/concepts/dry-run-mode.md) – The safe execution mode that reports issues without attempting repairs.
- [Deletion Vectors](/concepts/deletion-vectors.md) – The mechanism that tracks soft-deleted rows; corruption here can cause incorrect query results.
- Delta Lake Maintenance – Broader set of commands for keeping Delta tables healthy.
- Checkpoint Files – Used for fast table state recovery; CRC corruption may affect reliability.

## Sources

- fsck-repair-table-databricks-on-aws.md

# Citations

1. [fsck-repair-table-databricks-on-aws.md](/references/fsck-repair-table-databricks-on-aws-0ce9a31c.md)
