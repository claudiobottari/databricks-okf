---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3c38d966ebe9bd7da9ded57fcebaf8a48a24872ee25e992b6e3efe24807c85d5
  pageDirectory: concepts
  sources:
    - fsck-repair-table-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - fsck-repair-table
    - FRT
    - MSCK REPAIR TABLE
    - REPAIR TABLE
    - Delta Lake FSCK REPAIR TABLE
  citations:
    - file: fsck-repair-table-databricks-on-aws.md
title: FSCK REPAIR TABLE
description: Command to detect and repair metadata inconsistencies in Delta Lake tables on Databricks
tags:
  - delta-lake
  - databricks
  - sql-command
  - maintenance
timestamp: "2026-06-19T10:40:02.863Z"
---

# FSCK REPAIR TABLE

**FSCK REPAIR TABLE** is a SQL command in Databricks that checks Delta tables for metadata inconsistencies. The command can detect missing data files, deletion vector files, checkpoint corruption, unreadable files, invalid partition values, and CRC checksum corruption. The examples below demonstrate the command’s output with the `DRY RUN` option, which reports issues without making repairs. ^[fsck-repair-table-databricks-on-aws.md]

## Syntax

```sql
FSCK REPAIR TABLE table_name
[ METADATA ONLY ]
[ VERIFY ALL FILES ]
[ DRY RUN ]
```

## Output Columns

When run with `DRY RUN`, the command returns a table with the following columns: ^[fsck-repair-table-databricks-on-aws.md]

| Column | Description |
|--------|-------------|
| `dataFilePath` | Path to a data file with issues |
| `dataFileMissing` | Whether the data file is missing from storage |
| `deletionVectorPath` | Path to a deletion vector file with issues |
| `deletionVectorFileMissing` | Whether the deletion vector file is missing |
| `checkpointFilePath` | Path to a checkpoint file with issues |
| `fileCrcCorrupt` | Whether the file has CRC checksum corruption |
| `fileUnreadable` | Whether the file exists but cannot be read |
| `fileMetadataHasInvalidPartitionValues` | Whether the file has partition values that violate the table schema |
| `deletionVectorCorrupt` | Whether a deletion vector file is corrupted |

## Examples

### Detecting checkpoint CRC corruption (METADATA ONLY)

```sql
FSCK REPAIR TABLE t METADATA ONLY DRY RUN;
```

**Assumes** `005.checkpoint.parquet` has CRC checksum corruption.  
**Sample output:** ^[fsck-repair-table-databricks-on-aws.md]

| dataFilePath | dataFileMissing | deletionVectorPath | deletionVectorFileMissing | checkpointFilePath                | fileCrcCorrupt | fileUnreadable | fileMetadataHasInvalidPartitionValues | deletionVectorCorrupt |
|--------------|-----------------|--------------------|---------------------------|-----------------------------------|----------------|----------------|---------------------------------------|-----------------------|
| null         | false           | null               | false                     | _delta_log/005.checkpoint.parquet | true           | false          | false                                 | false                 |

### Detecting missing files and invalid partition values

```sql
FSCK REPAIR TABLE t DRY RUN;
```

**Assumes** `file1.parquet` is missing, whose deletion vector `dv1.bin` is also missing; `file2.parquet` has a null partition value where the partition column is `NOT NULL`.  
**Sample output:** ^[fsck-repair-table-databricks-on-aws.md]

| dataFilePath  | dataFileMissing | deletionVectorPath | deletionVectorFileMissing | checkpointFilePath | fileCrcCorrupt | fileUnreadable | fileMetadataHasInvalidPartitionValues | deletionVectorCorrupt |
|---------------|-----------------|--------------------|---------------------------|--------------------|----------------|----------------|---------------------------------------|-----------------------|
| file2.parquet | true            | dv1.bin            | true                      | null               | false          | false          | false                                 | false                 |
| file2.parquet | false           | null               | false                     | null               | null           | null           | true                                  | false                 |

### Detecting unreadable files and corrupt deletion vectors (VERIFY ALL FILES)

```sql
FSCK REPAIR TABLE t VERIFY ALL FILES DRY RUN;
```

**Assumes** `file1.parquet` is corrupt and unreadable; `file2.parquet` has a corrupt deletion vector `dv2.bin`.  
**Sample output:** ^[fsck-repair-table-databricks-on-aws.md]

| dataFilePath  | dataFileMissing | deletionVectorPath | deletionVectorFileMissing | checkpointFilePath | fileCrcCorrupt | fileUnreadable | fileMetadataHasInvalidPartitionValues | deletionVectorCorrupt |
|---------------|-----------------|--------------------|---------------------------|--------------------|----------------|----------------|---------------------------------------|-----------------------|
| file1.parquet | false           | null               | false                     | null               | false          | true           | false                                 | false                 |
| file2.parquet | false           | dv2.bin            | false                     | null               | null           | null           | false                                 | true                  |

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md)
- Delta Table Maintenance

## Sources

- fsck-repair-table-databricks-on-aws.md

# Citations

1. [fsck-repair-table-databricks-on-aws.md](/references/fsck-repair-table-databricks-on-aws-0ce9a31c.md)
