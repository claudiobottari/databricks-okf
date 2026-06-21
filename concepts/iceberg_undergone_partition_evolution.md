---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9ec1f6535890b341bc4082c3817d07001cd8faec0fc6d84b222092b0e2a29d2c
  pageDirectory: concepts
  sources:
    - delta_clone_incompatible_source-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - iceberg_undergone_partition_evolution
    - ICEBERG_UNDERGONE_PARTITION_EVOLUTION
    - Iceberg Partition Evolution
    - iceberg_undergone_partition_evolution-delta-clone-sub-error
    - I(CS
    - ICEBERG_UNDERGONE_PARTITION_EVOLUTION (Delta Clone sub-error)
    - iceberg_undergone_partition_evolution-error-condition
    - IEC
    - iceberg_undergone_partition_evolution-sub-error
    - ICEBERG_UNDERGONE_PARTITION_EVOLUTION sub-error
  citations:
    - file: delta_clone_incompatible_source-error-condition-databricks-on-aws.md
title: ICEBERG_UNDERGONE_PARTITION_EVOLUTION
description: A subclass of DELTA_CLONE_INCOMPATIBLE_SOURCE error indicating the source Apache Iceberg table has undergone partition evolution, making it incompatible for cloning.
tags:
  - databricks
  - iceberg
  - partition-evolution
  - error-handling
timestamp: "2026-06-19T18:22:21.431Z"
---

# ICEBERG_UNDERGONE_PARTITION_EVOLUTION

**ICEBERG_UNDERGONE_PARTITION_EVOLUTION** is an error condition that occurs when attempting to clone an [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) table that has undergone partition evolution into a [Delta Lake](/concepts/delta-lake.md) table. This error is classified under the `DELTA_CLONE_INCOMPATIBLE_SOURCE` error class (SQLSTATE: 0AKDC). ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Error Message

The error message is:

```
Source Apache Iceberg table has undergone partition evolution.
```

^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Cause

The clone source (an Apache Iceberg table) has a valid format but contains an unsupported feature for Delta Lake. Specifically, the source Iceberg table has experienced partition evolution — meaning its partitioning scheme has changed over time through operations like adding, removing, or redefining partition columns. Delta Lake's cloning operation cannot handle Iceberg tables with evolved partition schemes. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Solution

To resolve this error, you must ensure the source Iceberg table has a consistent, non-evolved partition specification before cloning. This may involve:

- Creating a new Iceberg table with a single, stable partition scheme
- Restructuring the data into a table that has not undergone partition evolution
- Using an alternative data migration strategy that does not rely on cloning

## Related Concepts

- DELTA_CLONE_INCOMPATIBLE_SOURCE Error|DELTA_CLONE_INCOMPATIBLE_SOURCE error condition — The parent error class for this and similar errors
- [Delta Lake cloning](/concepts/delta-table-cloning.md) — The operation that triggers this error
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The source table format
- HAS_INDEXES — Another error under the same error class (table has indexes)
- ICEBERG_MISSING_PARTITION_SPECS — Another error under the same error class (table has no partition specs)

## Sources

- delta_clone_incompatible_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_incompatible_source-error-condition-databricks-on-aws.md](/references/delta_clone_incompatible_source-error-condition-databricks-on-aws-b63ca67d.md)
