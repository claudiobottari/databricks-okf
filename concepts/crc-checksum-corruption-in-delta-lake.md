---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d4320807dbfa92eaa3112d509886e9d89ed640f2f542da7104d93f00c9a6c8cf
  pageDirectory: concepts
  sources:
    - fsck-repair-table-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - crc-checksum-corruption-in-delta-lake
    - CCCIDL
  citations:
    - file: fsck-repair-table-databricks-on-aws.md
title: CRC checksum corruption in Delta Lake
description: Corruption of CRC checksum in Delta Lake checkpoint files detected by FSCK REPAIR TABLE
tags:
  - delta-lake
  - corruption
  - checksum
  - integrity
timestamp: "2026-06-19T10:40:18.729Z"
---

# CRC Checksum Corruption in Delta Lake

**CRC checksum corruption** in [Delta Lake](/concepts/delta-lake.md) refers to an inconsistency between the stored cyclic redundancy check (CRC) value of a checkpoint file and the file’s actual content. When a checkpoint’s CRC checksum is corrupted, Delta Lake cannot verify the integrity of that checkpoint, which can lead to failures when reading the transaction log. ^[fsck-repair-table-databricks-on-aws.md]

## How CRC Corruption Occurs

CRC checksum corruption most often affects `_delta_log/*.checkpoint.parquet` files. It can arise from storage‑layer bit rot, incomplete writes, or other data integrity issues. The corruption is distinct from a file being unreadable or missing — the file may exist and be readable, but its CRC value no longer matches its contents. ^[fsck-repair-table-databricks-on-aws.md]

## Detection with `FSCK REPAIR TABLE`

The `FSCK REPAIR TABLE` command with the `METADATA ONLY` option or the `DRY RUN` option can identify checkpoint files whose CRC checksum is corrupted. The command reports the result in the `fileCrcCorrupt` column of its output. ^[fsck-repair-table-databricks-on-aws.md]

### Example Output

```sql
> FSCK REPAIR TABLE t METADATA ONLY DRY RUN;

 dataFilePath | dataFileMissing | deletionVectorPath | deletionVectorFileMissing | checkpointFilePath                | fileCrcCorrupt | fileUnreadable | ...
--------------|-----------------|--------------------|---------------------------|-----------------------------------|----------------|----------------|-----
 null         | false           | null               | false                     | _delta_log/005.checkpoint.parquet | true           | false          | false
```

In this example the checkpoint file `005.checkpoint.parquet` has its CRC checksum flagged as corrupt (`fileCrcCorrupt = true`), while the file itself remains readable (`fileUnreadable = false`). ^[fsck-repair-table-databricks-on-aws.md]

The `FSCK REPAIR TABLE` output includes the following columns relevant to CRC checksum inspection:

- `checkpointFilePath` – the path of the checkpoint file examined.
- `fileCrcCorrupt` – `true` if the CRC checksum is corrupted; `false` if it is valid; `null` if the row does not pertain to a checkpoint (e.g., when scanning data files).
- `fileUnreadable` – `true` if the file cannot be read; `false` otherwise. CRC corruption and unreadability are independent checks. ^[fsck-repair-table-databricks-on-aws.md]

## Resolution

When a CRC‑corrupted checkpoint is identified, the recommended approach is to **repair** it by running `FSCK REPAIR TABLE` without the `DRY RUN` modifier. This operation regenerates the checkpoint’s metadata from the delta log entries, replacing the corrupted file with a correct version. ^[fsck-repair-table-databricks-on-aws.md]

```sql
FSCK REPAIR TABLE t METADATA ONLY;
```

The `METADATA ONLY` variant limits repair to checkpoint and metadata files, ignoring data files. For a full repair that also handles missing data files, deletion vectors, and unreadable files, omit the `METADATA ONLY` clause. ^[fsck-repair-table-databricks-on-aws.md]

## Related Concepts

- [Delta Lake Transaction Log](/concepts/delta-lake-transaction-log.md) – The underlying structure that checkpoints compact.
- Checkpoint Files – Parquet snapshots of the delta log that can suffer CRC corruption.
- [FSCK REPAIR TABLE](/concepts/fsck-repair-table.md) – The command used to detect and fix corruption.
- [Deletion Vector Corruption](/concepts/deletion-vector-corruption-detection.md) – Another type of corruption that can be detected alongside CRC issues.
- Delta Lake File Integrity – Broader topic of ensuring data files and log files are consistent.

## Sources

- fsck-repair-table-databricks-on-aws.md

# Citations

1. [fsck-repair-table-databricks-on-aws.md](/references/fsck-repair-table-databricks-on-aws-0ce9a31c.md)
