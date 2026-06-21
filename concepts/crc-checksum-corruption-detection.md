---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8e85dfda56d3cd7cfdce578488f1832308d3af4a05fba2a51daa6413dd7a5ab2
  pageDirectory: concepts
  sources:
    - fsck-repair-table-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - crc-checksum-corruption-detection
    - CCCD
  citations:
    - file: fsck-repair-table-databricks-on-aws.md
title: CRC Checksum Corruption Detection
description: The ability of FSCK REPAIR TABLE to detect CRC (Cyclic Redundancy Check) checksum corruption in Delta Lake checkpoint files (.checkpoint.parquet).
tags:
  - delta-lake
  - corruption
  - checksum
timestamp: "2026-06-18T12:26:51.826Z"
---

#CRC Checksum Corruption Detection

**CRC Checksum Corruption Detection** refers to the process of identifying Data Lake checkpoint files whose Cyclic Redundancy Check (CRC) checksum — a mathematical fingerprint that verifies file integrity — has become corrupt. In [Delta Lake](/concepts/delta-lake.md), CRC corruption can occur when a checkpoint `.parquet` file is written or stored incorrectly, making its contents unusable. Detecting and repairing such corruption is critical to maintaining metadata consistency and preventing query failures. ^[fsck-repair-table-databricks-on-aws.md]

## Detection via FSCK REPAIR TABLE

The `FSCK REPAIR TABLE` command in Delta Lake can scan checkpoint files for CRC checksum corruption. When invoked with the `DRY RUN` option, the command reports issues without making changes. The output includes a dedicated column `fileCrcCorrupt` that indicates whether a checkpoint file’s CRC checksum is corrupted. ^[fsck-repair-table-databricks-on-aws.md]

### Example: Detecting a CRC‑corrupt checkpoint file

The source material demonstrates a scenario in which a checkpoint file (`005.checkpoint.parquet`) is assumed to have CRC checksum corruption. Running `FSCK REPAIR TABLE t METADATA ONLY DRY RUN` produces output where `checkpointFilePath` points to the corrupt file and `fileCrcCorrupt` is `true`:

```
> FSCK REPAIR TABLE t METADATA ONLY DRY RUN;
dataFilePath | dataFileMissing | deletionVectorPath | deletionVectorFileMissing | checkpointFilePath                | fileCrcCorrupt | fileUnreadable | fileMetadataHasInvalidPartitionValues | deletionVectorCorrupt
-------------|-----------------|--------------------|---------------------------|------------------------------------|----------------|----------------|----------------------------------------|-----------------------
null         | false           | null               | false                     | _delta_log/005.checkpoint.parquet  | true           | false          | false                                 | false
```

^[fsck-repair-table-databricks-on-aws.md]

In this example, the only reported issue is CRC corruption of the checkpoint file; the data files, deletion vectors, and other metadata are intact.

## Other Detection Options

- **`VERIFY ALL FILES`** — In addition to CRC checks, this option also reads every data file and deletion vector to detect unreadable content or corrupt deletion vectors. The `fileCrcCorrupt` column remains part of the output but will be `null` for data files (CRC corruption is relevant only for checkpoint files). ^[fsck-repair-table-databricks-on-aws.md]

- **`METADATA ONLY`** — This mode checks only the transaction log metadata (including CRC integrity of checkpoint files) without verifying data files. It is faster and sufficient for detecting checkpoint CRC corruption. ^[fsck-repair-table-databricks-on-aws.md]

## What to Do After Detection

Once CRC corruption in a checkpoint file is confirmed, you can run `FSCK REPAIR TABLE` **without** `DRY RUN` to attempt a repair. The command will rewrite the corrupt checkpoint from the preceding transaction log entries, restoring metadata integrity. After repair, the table’s metadata is again consistent and queries can proceed normally.

> ⚠️ CRC corruption in a checkpoint does **not** necessarily mean data loss — only that the metadata snapshot is damaged. The underlying data files and earlier transaction log entries may still be intact.

## Related Concepts

- [FSCK REPAIR TABLE](/concepts/fsck-repair-table.md) — The Delta Lake command for detecting and repairing table metadata issues
- [Delta Lake](/concepts/delta-lake.md) — The open‑source storage layer providing ACID transactions and metadata verification
- Checkpoint files — Periodic snapshots of Delta table metadata stored as Parquet files in `_delta_log`
- CRC Checksum — A cyclic redundancy check used to detect accidental changes to raw data
- [Data Corruption](/concepts/deletion-vector-corruption-detection.md) — Broader concept of file integrity loss in data lakes

## Sources

- fsck-repair-table-databricks-on-aws.md

# Citations

1. [fsck-repair-table-databricks-on-aws.md](/references/fsck-repair-table-databricks-on-aws-0ce9a31c.md)
