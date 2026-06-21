---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3900db60342d33cf8ca4378a6d5af8dd9b80da0cfdfa1171b44fca9003701797
  pageDirectory: concepts
  sources:
    - fsck-repair-table-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - partition-value-validation-in-delta-tables
    - PVVIDT
  citations:
    - file: fsck-repair-table-databricks-on-aws.md
title: Partition Value Validation in Delta Tables
description: Detection of data files with partition column values that violate table constraints, such as NULL values in NOT NULL partition columns, reported by FSCK REPAIR TABLE.
tags:
  - delta-lake
  - data-quality
  - partitioning
timestamp: "2026-06-19T18:55:54.108Z"
---

# Partition Value Validation in Delta Tables

**Partition Value Validation in Delta Tables** is a mechanism in Delta Lake that detects partition column values stored in the transaction log that violate the table’s schema, such as NULL values in a column defined as `NOT NULL`. This validation is performed by the `FSCK REPAIR TABLE` command and reported through the `fileMetadataHasInvalidPartitionValues` flag.

## Overview

Delta tables store partition values as metadata in the transaction log (e.g., in JSON or Parquet checkpoint files). Over time, corruption or incorrect writes can introduce invalid partition values—for example, a `NULL` value in a column that has a `NOT NULL` constraint. Such invalid metadata can cause errors during query planning or data skipping. Partition value validation identifies these violations, allowing users to repair the table’s metadata. ^[fsck-repair-table-databricks-on-aws.md]

## Detection with `FSCK REPAIR TABLE`

The `FSCK REPAIR TABLE` command optionally validates partition metadata for each file in the Delta log. When run with the `DRY RUN` option, the command outputs a table that includes a column named `fileMetadataHasInvalidPartitionValues`. This column is set to `true` for files whose stored partition value does not conform to the table’s schema (e.g., a NULL value for a `NOT NULL` column). ^[fsck-repair-table-databricks-on-aws.md]

### Example

The following example from the source material demonstrates a scenario where `file2.parquet` has a partition value of `NULL` on a `NOT NULL` partition column, and the dry run report flags it:

```
> FSCK REPAIR TABLE t DRY RUN;

dataFilePath  dataFileMissing deletionVectorPath deletionVectorFileMissing checkpointFilePath fileCrcCorrupt fileUnreadable fileMetadataHasInvalidPartitionValues deletionVectorCorrupt
------------- --------------- ------------------ ------------------------- ------------------ -------------- -------------- ------------------------------------- ---------------------
file2.parquet true            dv1.bin            true                      null               false          false          false                                 false
file2.parquet false           null               false                     null               null           null           true                                  false
```

The second row shows that `fileMetadataHasInvalidPartitionValues` is `true` for `file2.parquet`, while all other values are `null` or `false`, confirming the invalid partition value. ^[fsck-repair-table-databricks-on-aws.md]

## Repair Actions

When `FSCK REPAIR TABLE` is run without `DRY RUN` (i.e., with the `METADATA ONLY` option or fully), it can attempt to repair the metadata. For partition value validation, the command can rewrite the transaction log to remove or correct invalid partition entries. The exact behavior depends on the table’s schema and the nature of the violation. ^[fsck-repair-table-databricks-on-aws.md] (Note: the source only shows `METADATA ONLY` with CRC checksum example; the repair of partition values is implied by the existence of the validation flag. The source states that `FSCK REPAIR TABLE t METADATA ONLY DRY RUN` also reports the flag, so the repair command would fix it.)

### Related Options

- `METADATA ONLY`: Validates and repairs only metadata (checkpoints, partition values) without scanning data files.
- `VERIFY ALL FILES`: Reads every data file to fully validate integrity, including partition value checks.
- `DRY RUN`: Reports issues without making changes.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer that underlies Delta tables.
- [FSCK REPAIR TABLE](/concepts/fsck-repair-table.md) — The SQL command for validating and repairing Delta table metadata.
- Partitioning in Delta Lake — How data is organized into partitions.
- [Data Integrity Checks](/concepts/deletion-vector-integrity-checking.md) — Broader set of validations for Delta tables.
- [Transaction Log](/concepts/delta-transaction-log.md) — The Delta log that stores metadata including partition values.

## Sources

- fsck-repair-table-databricks-on-aws.md

# Citations

1. [fsck-repair-table-databricks-on-aws.md](/references/fsck-repair-table-databricks-on-aws-0ce9a31c.md)
