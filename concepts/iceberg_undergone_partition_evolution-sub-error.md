---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9a8906620e81f6809b2ed6233dac734b27b9f932ca4444365d3bd6fda2a278ae
  pageDirectory: concepts
  sources:
    - delta_clone_incompatible_source-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - iceberg_undergone_partition_evolution-sub-error
    - ICEBERG_UNDERGONE_PARTITION_EVOLUTION sub-error
  citations:
    - file: delta_clone_incompatible_source-error-condition-databricks-on-aws.md
title: ICEBERG_UNDERGONE_PARTITION_EVOLUTION sub-error
description: A specific error under DELTA_CLONE_INCOMPATIBLE_SOURCE indicating the source Apache Iceberg table has undergone partition evolution, which is unsupported for Delta cloning.
tags:
  - error
  - delta-lake
  - iceberg
  - partition-evolution
timestamp: "2026-06-19T15:01:59.381Z"
---

---
title: ICEBERG_UNDERGONE_PARTITION_EVOLUTION sub-error
summary: A specific sub-error of DELTA_CLONE_INCOMPATIBLE_SOURCE indicating the source Iceberg table has undergone partition evolution, which is unsupported for Delta cloning
sources:
  - delta_clone_incompatible_source-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T15:17:20.684Z"
updatedAt: "2026-06-18T15:17:20.684Z"
tags:
  - databricks
  - delta-lake
  - iceberg
  - partition-evolution
aliases:
  - iceberg_undergone_partition_evolution-sub-error
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# ICEBERG_UNDERGONE_PARTITION_EVOLUTION sub-error

**ICEBERG_UNDERGONE_PARTITION_EVOLUTION** is a sub-error of the `DELTA_CLONE_INCOMPATIBLE_SOURCE` error class (SQLSTATE: `0AKDC`) that occurs when attempting to clone an Apache Iceberg table into a Delta table, but the source Iceberg table has undergone [partition evolution](/concepts/partition-evolution-in-iceberg.md). The Delta clone operation does not support sources with evolved partition schemes. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Error Details

- **Error Class:** `DELTA_CLONE_INCOMPATIBLE_SOURCE` ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]
- **SQLSTATE:** `0AKDC` (Feature Not Supported) ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]
- **Sub-error:** `ICEBERG_UNDERGONE_PARTITION_EVOLUTION` ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Error Message

When this sub-error occurs, the system returns the following message:

```
Source Apache Iceberg table has undergone partition evolution.
```

^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Cause

Partition evolution in Iceberg refers to the process where a table's partitioning scheme changes over time (e.g., adding, removing, or modifying partition columns after data has been written). Delta Lake’s current Iceberg compatibility layer cannot safely convert such tables during a `CLONE` operation, as the evolved partition structure introduces complexities beyond what is supported. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Related Sub-errors

The `DELTA_CLONE_INCOMPATIBLE_SOURCE` error class includes other sub-errors that may appear in similar scenarios: ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

| Sub-error | Description |
|-----------|-------------|
| `HAS_INDEXES` | The source table has indexes that must be dropped before cloning |
| `ICEBERG_MISSING_PARTITION_SPECS` | The source Iceberg table has no partition specs in the table metadata |

## Related Concepts

- [Delta CLONE command](/concepts/delta-clone.md) — The SQL command used to clone tables
- [Delta Lake](/concepts/delta-lake.md) — The storage layer used for Delta tables
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The open table format of the source table
- DELTA_CLONE_INCOMPATIBLE_SOURCE — The parent error class
- [Partition evolution](/concepts/partition-evolution-in-iceberg.md) — The concept of changing a table’s partitioning scheme over time

## Sources

- delta_clone_incompatible_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_incompatible_source-error-condition-databricks-on-aws.md](/references/delta_clone_incompatible_source-error-condition-databricks-on-aws-b63ca67d.md)
