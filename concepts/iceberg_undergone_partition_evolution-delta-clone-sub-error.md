---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d96a3463cd1c987930edd98d6b1b8eaedf54d664e27e53440e03c07aab685316
  pageDirectory: concepts
  sources:
    - delta_clone_incompatible_source-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - iceberg_undergone_partition_evolution-delta-clone-sub-error
    - I(CS
    - ICEBERG_UNDERGONE_PARTITION_EVOLUTION (Delta Clone sub-error)
  citations:
    - file: delta_clone_incompatible_source-error-condition-databricks-on-aws.md
title: ICEBERG_UNDERGONE_PARTITION_EVOLUTION (Delta Clone sub-error)
description: A specific DELTA_CLONE_INCOMPATIBLE_SOURCE sub-error indicating the source Iceberg table has undergone partition evolution, which is incompatible with cloning.
tags:
  - error-message
  - delta-lake
  - iceberg
  - partition-evolution
timestamp: "2026-06-19T10:02:37.624Z"
---

# ICEBERG_UNDERGONE_PARTITION_EVOLUTION (Delta Clone sub-error)

**ICEBERG_UNDERGONE_PARTITION_EVOLUTION** is a sub-error of the `DELTA_CLONE_INCOMPATIBLE_SOURCE` error class that occurs when attempting to clone an Apache Iceberg table into a Delta table, but the source Iceberg table has undergone partition evolution. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Error Message

The error message returned is:

```
Source Apache Iceberg table has undergone partition evolution.
```

^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Cause

This error occurs when the source [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) table has had its partitioning scheme changed over time through partition evolution. Delta Lake's clone operation from an Iceberg source cannot handle tables that have undergone partition evolution, as the cloning process expects a consistent partition specification throughout the table's history. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Solution

To resolve this error, you must first recreate the source Iceberg table without partition evolution. This means recreating the table with a single, consistent partition specification that does not change over time. Once the table has a stable partition scheme, the clone operation to [Delta Lake](/concepts/delta-lake.md) should succeed. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Clone](/concepts/delta-clone.md) — The cloning operation that produces this error
- DELTA_CLONE_INCOMPATIBLE_SOURCE — The parent error class containing this sub-error
- ICEBERG_MISSING_PARTITION_SPECS — Another sub-error in the same class, where the source Iceberg table has no partition specs
- HAS_INDEXES — Another sub-error where the source table has indexes that must be dropped before cloning

# Citations

1. [delta_clone_incompatible_source-error-condition-databricks-on-aws.md](/references/delta_clone_incompatible_source-error-condition-databricks-on-aws-b63ca67d.md)
