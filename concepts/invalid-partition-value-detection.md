---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 33eb4b5268c3482f391b8652ef9a791e67250bdbff98a5ce6bf39fd9f4855cea
  pageDirectory: concepts
  sources:
    - fsck-repair-table-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - invalid-partition-value-detection
    - IPVD
  citations:
    - file: fsck-repair-table-databricks-on-aws.md
title: Invalid Partition Value Detection
description: The ability of FSCK REPAIR TABLE to detect data files with partition column values that violate NOT NULL constraints, such as NULL values in non-nullable partition columns.
tags:
  - delta-lake
  - partitioning
  - validation
timestamp: "2026-06-18T12:26:52.589Z"
---

# Invalid Partition Value Detection

**Invalid Partition Value Detection** is a feature of Delta Lake's `FSCK REPAIR TABLE` command that identifies data files whose partition column metadata contains values that violate the table's partition schema. The most common scenario is a `NULL` value in a partition column that is defined as `NOT NULL`. Such inconsistencies can arise from manual file operations, direct file writes bypassing Delta Lake constraints, or external data ingestion.^[fsck-repair-table-databricks-on-aws.md]

## How Detection Works

When you run `FSCK REPAIR TABLE` with the `DRY RUN` option, Delta Lake inspects the metadata of each data file and checks whether the stored partition values match the table's schema constraints. Files with invalid partition metadata are reported with the column `fileMetadataHasInvalidPartitionValues` set to `true`.^[fsck-repair-table-databricks-on-aws.md]

The detection is available in two modes:

- **Standard `DRY RUN`** — Reports invalid partition values among other file-level inconsistencies.
- **`VERIFY ALL FILES DRY RUN`** — Performs additional checks including file readability and [deletion vector](/concepts/deletion-vectors.md) integrity, and also reports invalid partition values.

## Examples

### Standard Dry Run

Given a table `t` where partition column `p` is defined as `NOT NULL`, and a file `file2.parquet` has a `NULL` partition value:

```sql
> FSCK REPAIR TABLE t DRY RUN;
```

| dataFilePath | dataFileMissing | deletionVectorPath | deletionVectorFileMissing | checkpointFilePath | fileCrcCorrupt | fileUnreadable | fileMetadataHasInvalidPartitionValues | deletionVectorCorrupt |
|---|---|---|---|---|---|---|---|---|
| file2.parquet | true | dv1.bin | true | null | false | false | false | false |
| file2.parquet | false | null | false | null | null | null | **true** | false |

The second row shows that `file2.parquet` has `fileMetadataHasInvalidPartitionValues = true`, indicating that its partition metadata is inconsistent with the table schema.^[fsck-repair-table-databricks-on-aws.md]

### Dry Run with Metadata-Only Scan

A metadata-only scan (`METADATA ONLY DRY RUN`) checks [checkpoint](/concepts/checkpoint-v2-requirement.md) files for CRC corruption and file existence, but **does not** inspect partition values in individual data files. Invalid partition values are only detected when the full scan is performed.^[fsck-repair-table-databricks-on-aws.md]

## Repairing Invalid Partition Values

To repair the detected inconsistencies, run `FSCK REPAIR TABLE` without the `DRY RUN` clause. Delta Lake will attempt to fix or remove the files with invalid partition metadata, restoring the table's consistency. After the repair, a subsequent `DRY RUN` should no longer report those files as invalid.^[fsck-repair-table-databricks-on-aws.md]

## Relationship to Other Checks

The `fileMetadataHasInvalidPartitionValues` column is one of several integrity flags reported by `FSCK REPAIR TABLE`. Others include `dataFileMissing`, `fileCrcCorrupt`, `fileUnreadable`, and `deletionVectorCorrupt`. This detection is part of Delta Lake File Integrity Validation.^[fsck-repair-table-databricks-on-aws.md]

## Best Practices

- Run `FSCK REPAIR TABLE t DRY RUN` regularly on tables that receive external data writes to catch partition metadata issues early.
- Define partition columns as `NOT NULL` whenever possible to prevent accidental insertion of invalid values.
- Use the `VERIFY ALL FILES` option less frequently (e.g., after known data corruption events) because it performs more I/O-intensive checks.

## Related Concepts

- [FSCK REPAIR TABLE](/concepts/fsck-repair-table.md) — The command used for detecting and repairing table inconsistencies
- [Delta Lake Partitioning](/concepts/delta-lake-partitioning-constraints.md) — How Delta Lake organizes data by partition columns
- [Delta Lake Constraints](/concepts/delta-lake-partitioning-constraints.md) — Schema constraints including `NOT NULL` on partition columns
- Data Corruption Detection — Broader topic of integrity checks in Delta Lake
- [Deletion Vector](/concepts/deletion-vectors.md) — Associated metadata that can also be checked for corruption

## Sources

- fsck-repair-table-databricks-on-aws.md

# Citations

1. [fsck-repair-table-databricks-on-aws.md](/references/fsck-repair-table-databricks-on-aws-0ce9a31c.md)
