---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c8708bed5be5f9a6f8ae786d07883f399cf992adf22cfddb0c2f0f8fe708d0c5
  pageDirectory: concepts
  sources:
    - fsck-repair-table-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - invalid-partition-values-detection
    - IPVD
  citations:
    - file: fsck-repair-table-databricks-on-aws.md
title: Invalid partition values detection
description: Detection of data files with partition values that violate the table's NOT NULL partition column constraints
tags:
  - delta-lake
  - databricks
  - partitioning
  - data-quality
timestamp: "2026-06-19T10:40:25.049Z"
---

# Invalid Partition Values Detection

**Invalid partition values detection** refers to the identification of partition column values in a [Delta Lake](/concepts/delta-lake.md) table that violate the table’s schema constraints. A common case is a partition column that is defined as `NOT NULL` but contains a `NULL` value in one or more data files. The detection is performed using the `FSCK REPAIR TABLE` command. ^[fsck-repair-table-databricks-on-aws.md]

## Detection with FSCK REPAIR TABLE

The `FSCK REPAIR TABLE` command with the `DRY RUN` option reports files that have invalid partition values. The output includes a `fileMetadataHasInvalidPartitionValues` column, which is set to `true` when a data file’s partition metadata violates the table’s partition column constraints. ^[fsck-repair-table-databricks-on-aws.md]

### Example

Consider a table `t` where a partition column is defined as `NOT NULL`. If a data file `file2.parquet` has a `NULL` value for that partition column, running the following command will flag it:

```sql
FSCK REPAIR TABLE t DRY RUN;
```

The output includes a row for `file2.parquet` with `fileMetadataHasInvalidPartitionValues` set to `true` and the other diagnostic columns set to `null` or `false`:

| dataFilePath  | dataFileMissing | deletionVectorPath | deletionVectorFileMissing | checkpointFilePath | fileCrcCorrupt | fileUnreadable | fileMetadataHasInvalidPartitionValues | deletionVectorCorrupt |
|---------------|-----------------|--------------------|---------------------------|--------------------|----------------|----------------|----------------------------------------|-----------------------|
| file2.parquet | false           | null               | false                     | null               | null           | null           | true                                   | false                 |

^[fsck-repair-table-databricks-on-aws.md]

## Use Cases

- **Schema enforcement**: Detecting `NULL` values in partition columns that were expected to be `NOT NULL`.
- **Data quality**: Identifying corrupt or improperly written metadata that can affect query results.
- **Table repair**: The `FSCK REPAIR TABLE` command (without `DRY RUN`) can repair such issues, though the source material focuses on the detection phase. ^[fsck-repair-table-databricks-on-aws.md]

## Related Concepts

- [FSCK REPAIR TABLE](/concepts/fsck-repair-table.md) – The command used to detect and repair table inconsistencies.
- [Delta Lake](/concepts/delta-lake.md) – The storage layer that provides ACID transactions and schema enforcement.
- Partition Columns – Columns used to physically organize data in a Delta table.
- Table Constraints – Rules like `NOT NULL` that can be defined on partition columns.

## Sources

- fsck-repair-table-databricks-on-aws.md

# Citations

1. [fsck-repair-table-databricks-on-aws.md](/references/fsck-repair-table-databricks-on-aws-0ce9a31c.md)
