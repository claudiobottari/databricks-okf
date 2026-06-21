---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 22fbd53371271d5cc0c325c2eab790baba4158591581fca3b70673043b84464f
  pageDirectory: concepts
  sources:
    - delta_clone_incompatible_source-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - iceberg_missing_partition_specs-error-condition
    - IEC
  citations:
    - file: delta_clone_incompatible_source-error-condition-databricks-on-aws.md
title: ICEBERG_MISSING_PARTITION_SPECS error condition
description: A sub-error of DELTA_CLONE_INCOMPATIBLE_SOURCE raised when cloning an Apache Iceberg table that has no partition specs defined.
tags:
  - databricks
  - iceberg
  - error-message
  - partitioning
timestamp: "2026-06-18T11:50:22.497Z"
---

# ICEBERG_MISSING_PARTITION_SPECS Error Condition

The **ICEBERG_MISSING_PARTITION_SPECS** error condition occurs when attempting to clone a source Apache Iceberg table that has no partition specifications defined in its table metadata. This is a subclass of the `DELTA_CLONE_INCOMPATIBLE_SOURCE` error class. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Error Details

| Property | Value |
|----------|-------|
| SQLSTATE | 0AKDC |
| Error Class | `DELTA_CLONE_INCOMPATIBLE_SOURCE` |
| Subclass | `ICEBERG_MISSING_PARTITION_SPECS` |

## Error Message

```
ICEBERG_MISSING_PARTITION_SPECS
```

The full error message indicates: *Source Apache Iceberg table has no partition specs in table.* ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Cause

This error is raised when a `CLONE` operation targets an Apache Iceberg table that is missing partition specifications entirely. While the source table has valid format and is otherwise readable, the Delta clone operation requires partition metadata from the source Iceberg table. Without any partition specs, the clone operation cannot proceed. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Related Error Conditions

### ICEBERG_UNDERGONE_PARTITION_EVOLUTION

A similar error condition, `ICEBERG_UNDERGONE_PARTITION_EVOLUTION`, occurs when the source Iceberg table has undergone [partition evolution](/concepts/partition-evolution-in-iceberg.md) — meaning its partition scheme has changed over time. This is distinct from having no partition specs at all. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

### HAS_INDEXES

Another subclass of `DELTA_CLONE_INCOMPATIBLE_SOURCE` is `HAS_INDEXES`, which occurs when the source table has indexes that must be dropped before cloning. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Troubleshooting

To resolve this error, ensure the source Iceberg table has at least one partition specification defined. This may require modifying the source table in Iceberg to add a partition spec before attempting the clone operation to Delta.

## Related Concepts

- [Delta Lake CLONE](/concepts/delta-clone.md) — The operation that triggers this error
- Apache Iceberg Tables — Source format for the clone operation
- DELTA_CLONE_INCOMPATIBLE_SOURCE — The parent error class
- ICEBERG_UNDERGONE_PARTITION_EVOLUTION — Related error for partition-evolved Iceberg tables
- [Delta Lake](/concepts/delta-lake.md) — The target format for the clone operation

## Sources

- delta_clone_incompatible_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_incompatible_source-error-condition-databricks-on-aws.md](/references/delta_clone_incompatible_source-error-condition-databricks-on-aws-b63ca67d.md)
