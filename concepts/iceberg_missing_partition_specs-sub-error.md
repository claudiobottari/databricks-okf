---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 022a27a9a72bff9d0443cf4f3e8c1608750dd38a7429e367019ca3f0f94528e7
  pageDirectory: concepts
  sources:
    - delta_clone_incompatible_source-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - iceberg_missing_partition_specs-sub-error
    - ICEBERG_MISSING_PARTITION_SPECS error
    - ICEBERG_MISSING_PARTITION_SPECS sub-error
  citations:
    - file: delta_clone_incompatible_source-error-condition-databricks-on-aws.md
title: ICEBERG_MISSING_PARTITION_SPECS sub-error
description: A specific error under DELTA_CLONE_INCOMPATIBLE_SOURCE indicating the source Apache Iceberg table has no partition specs, making it incompatible for Delta cloning.
tags:
  - error
  - delta-lake
  - iceberg
  - partitioning
timestamp: "2026-06-19T15:02:00.440Z"
---

# ICEBERG_MISSING_PARTITION_SPECS Sub-Error

**ICEBERG_MISSING_PARTITION_SPECS** is a sub-error of the `DELTA_CLONE_INCOMPATIBLE_SOURCE` error class (SQLSTATE 0AKDC). It occurs when a CLONE command or equivalent operation attempts to clone a source [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) table that has no partition specifications defined. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Error Message

The error message returned is:

```
Source Apache Iceberg table has no partition specs in table.
```

^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Description

The `DELTA_CLONE_INCOMPATIBLE_SOURCE` error is raised when the clone source has a valid format but uses a feature that is unsupported by [Delta Lake](/concepts/delta-lake.md). The `ICEBERG_MISSING_PARTITION_SPECS` variant specifically indicates that the source Iceberg table does not contain any partition specs. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

Partition specs define how data is physically organized in an Iceberg table. Without partition specs, the table structure is incompatible with Delta Lake’s cloning operation, and the clone cannot proceed. *(Inferred)*

## Related Concepts

- [Delta Clone](/concepts/delta-clone.md) — The operation that triggers this error.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The source table format.
- DELTA_CLONE_INCOMPATIBLE_SOURCE — The parent error class.
- ICEBERG_UNDERGONE_PARTITION_EVOLUTION — Another related sub-error for Iceberg tables that have undergone partition evolution.

## Sources

- delta_clone_incompatible_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_incompatible_source-error-condition-databricks-on-aws.md](/references/delta_clone_incompatible_source-error-condition-databricks-on-aws-b63ca67d.md)
