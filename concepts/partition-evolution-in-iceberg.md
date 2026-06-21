---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2a31a5eb1289e97f5c30ad141cd14ecfa740d43b756124f1669f03e3ca1eba4d
  pageDirectory: concepts
  sources:
    - delta_clone_incompatible_source-error-condition-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - partition-evolution-in-iceberg
    - PEII
    - Partition evolution
    - partition evolution
  citations:
    - file: delta_clone_incompatible_source-error-condition-databricks-on-aws.md
title: Partition Evolution in Iceberg
description: A feature of Apache Iceberg tables where the partitioning scheme can change over time; tables that have undergone partition evolution are incompatible as sources for Delta clone operations.
tags:
  - iceberg
  - partitioning
  - delta-lake
  - compatibility
timestamp: "2026-06-18T11:50:31.589Z"
---

# Partition Evolution in Iceberg

**Partition Evolution** is a feature in Apache Iceberg that allows a table's partitioning scheme to be changed after the table has been created and data has been written to it. Unlike some other table formats that require rewriting the entire table or dropping and recreating it to change partitioning, Iceberg supports evolving the partition specification over time without invalidating existing data files.

## Overview

In Apache Iceberg, partition evolution enables users to modify how data is physically organized in a table without rewriting existing data. When a partition specification is changed, new data is written using the new partitioning scheme, while existing data files remain in their original layout. Iceberg tracks multiple partition specifications within the table metadata, allowing queries to correctly read data written under any previous or current partition scheme. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## How Partition Evolution Works

Iceberg stores partition specifications as part of the table metadata. Each partition specification has a unique ID, and every data file is associated with the partition specification that was active when the file was written. When a query reads the table, Iceberg uses the appropriate partition specification for each file to correctly interpret the partition data.

When a partition evolution occurs:

1. A new partition specification is added to the table metadata with a new ID.
2. New data files are written using the new partition specification.
3. Existing data files remain unchanged and continue to use their original partition specification.
4. Queries automatically handle data written under different partition specifications.

## Partition Evolution and Cloning

When cloning an Iceberg table that has undergone partition evolution, the clone operation may fail with the error condition `ICEBERG_UNDERGONE_PARTITION_EVOLUTION`. This error occurs because the clone source has valid format but has an unsupported feature — specifically, the table has multiple partition specifications due to partition evolution. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

### Error Message

```
Source Apache Iceberg table has undergone partition evolution.
```

^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

### Resolution

To clone an Iceberg table that has undergone partition evolution, you must first resolve the incompatible partition specifications. Options include:

- **Rewriting the table** to consolidate all data under a single partition specification before cloning.
- **Using an alternative approach** such as reading the data with a query and writing it to a new table with a single partition specification.
- **Checking for updates** to the cloning tool or platform that may add support for cloning tables with partition evolution.

## Related Concepts

- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The open table format that supports partition evolution
- [Delta Lake](/concepts/delta-lake.md) — Another table format that handles partitioning differently
- [Table Cloning](/concepts/delta-table-cloning.md) — The operation that may be affected by partition evolution
- Partitioning Strategies — Best practices for choosing partition schemes
- [Table Metadata](/concepts/trace-metadata.md) — Where partition specifications are stored in Iceberg

## Sources

- delta_clone_incompatible_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_incompatible_source-error-condition-databricks-on-aws.md](/references/delta_clone_incompatible_source-error-condition-databricks-on-aws-b63ca67d.md)
