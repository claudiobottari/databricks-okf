---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c17f45a236eabaac595e39f6d1fb06f4a7abdfc9cbcb7ff3dfef06c9ec64db51
  pageDirectory: concepts
  sources:
    - delta_clone_incompatible_source-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - iceberg_undergone_partition_evolution-error-condition
    - IEC
  citations:
    - file: delta_clone_incompatible_source-error-condition-databricks-on-aws.md
title: ICEBERG_UNDERGONE_PARTITION_EVOLUTION error condition
description: A sub-error of DELTA_CLONE_INCOMPATIBLE_SOURCE raised when cloning an Apache Iceberg table that has undergone partition evolution (changed partitioning over time).
tags:
  - databricks
  - iceberg
  - error-message
  - partition-evolution
timestamp: "2026-06-18T11:50:46.719Z"
---

# ICEBERG_UNDERGONE_PARTITION_EVOLUTION Error Condition

**ICEBERG_UNDERGONE_PARTITION_EVOLUTION** is an error condition that occurs when attempting to clone an Apache Iceberg table that has undergone partition evolution into a [Delta Lake Table](/concepts/delta-lake-table.md). The error is part of the `DELTA_CLONE_INCOMPATIBLE_SOURCE` error class (SQLSTATE: 0AKDC). ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Error Message

The error is reported as:

```
Source Apache Iceberg table has undergone partition evolution.
```

^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Explanation

Partition evolution refers to the ability in [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) to change a table's partitioning scheme over time without rewriting existing data files. When an Iceberg table has undergone partition evolution — meaning its partitioning strategy has been modified at least once since creation — the clone operation to [Delta Lake](/concepts/delta-lake.md) cannot proceed because the current version of Delta Lake does not support cloning tables with multiple partitioning schemes. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Cause

This error is triggered when: ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

- The source Iceberg table has valid format and is recognized as a valid Iceberg table.
- However, the table has experienced partition evolution during its lifecycle.
- Delta's clone functionality for Iceberg sources does not support tables with evolved partitions.

## Related Error Subtypes

The `DELTA_CLONE_INCOMPATIBLE_SOURCE` error class includes two other related subtypes: ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

| Subtype | Description |
|---------|-------------|
| `HAS_INDEXES` | Table has indexes that must be dropped before cloning |
| `ICEBERG_MISSING_PARTITION_SPECS` | Source Iceberg table has no partition specs |

## Workarounds and Solutions

### Option 1: Recreate the Source Table Without Partition Evolution

If you control the source Iceberg table, recreate it with a single, stable partitioning strategy and load the data without performing partition evolution. After recreating the table, attempt the clone operation again. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

### Option 2: Use Alternative Migration Methods

Instead of cloning, consider: ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

- Using Parquet as an intermediate format — export the Iceberg table to Parquet and then load the Parquet files into a new Delta table.
- Using Spark SQL `INSERT OVERWRITE` or `CREATE TABLE AS SELECT` to copy data from the Iceberg source to a Delta target without the clone command.
- Using external data ingestion tools that can read Iceberg tables with evolved partitions and write to Delta format.

### Option 3: Manual Data Reload

As a manual workaround: ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

1. Read the Iceberg source table using Spark.
2. Write the data to a new Delta table using `df.write.format("delta").save()`.
3. Apply the desired partitioning on the new Delta table.

## Best Practices

- **Plan partitioning before data ingestion.** Determine your partitioning strategy for Iceberg tables before loading data to avoid needing partition evolution later. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]
- **Test clone operations.** Before committing to a clone workflow, test the operation on a sample Iceberg table that has undergone no partition changes. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]
- **Consider Delta Lake natively.** If you anticipate needing to clone tables across platforms, consider using [Delta Lake](/concepts/delta-lake.md) as the primary storage format to avoid compatibility issues with Iceberg partition evolution. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage format and engine for the clone target
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The source table format with partition evolution capabilities
- DELTA_CLONE_INCOMPATIBLE_SOURCE — The parent error class for Iceberg incompatibility issues
- HAS_INDEXES|HAS_INDEXES error — Related subtype for tables with indexes
- ICEBERG_MISSING_PARTITION_SPECS|ICEBERG_MISSING_PARTITION_SPECS error — Related subtype for tables without partition specs
- Parquet — Intermediate format for data migration workarounds

## Sources

- delta_clone_incompatible_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_incompatible_source-error-condition-databricks-on-aws.md](/references/delta_clone_incompatible_source-error-condition-databricks-on-aws-b63ca67d.md)
