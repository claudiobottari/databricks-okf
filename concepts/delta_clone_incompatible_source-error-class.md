---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e85549d4d16c204fd93bef53c53d8311964f55edd0bea51046f83c537a0406d8
  pageDirectory: concepts
  sources:
    - delta_clone_incompatible_source-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_clone_incompatible_source-error-class
    - DEC
    - DELTA_CLONE_INCOMPATIBLE_SOURCE error class
  citations:
    - file: delta_clone_incompatible_source-error-condition-databricks-on-aws.md
title: DELTA_CLONE_INCOMPATIBLE_SOURCE error class
description: A Databricks error condition raised when a Delta clone operation fails because the source table has a valid format but uses unsupported features.
tags:
  - error
  - delta-lake
  - databricks
timestamp: "2026-06-19T15:01:50.909Z"
---

# DELTA_CLONE_INCOMPATIBLE_SOURCE error class

**DELTA_CLONE_INCOMPATIBLE_SOURCE** is an error class that occurs when attempting to [Deep Clone a Delta Table|clone a Delta table](/concepts/deep-clone-delta-table.md), but the source table, while having a valid format, includes an unsupported feature that is incompatible with Delta Lake's cloning operation. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

The error belongs to the SQLSTATE class `0AKDC` (Feature not supported). ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Sub-Errors

This error class includes three specific sub‑errors, each describing a distinct incompatibility.

### HAS_INDEXES

The source table has indexes, which Delta Lake does not support for cloning. The error message includes the table name and the list of index names. Drop the indexes from the source table before retrying the clone operation. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

```
Table <tableName> has indexes: <indexNames>. Drop the indexes before cloning.
```

### ICEBERG_MISSING_PARTITION_SPECS

The source Apache Iceberg table has no partition specifications in its metadata. Delta Lake requires partition spec information to correctly clone an Iceberg table. Verify that the Iceberg table has at least one partition spec defined. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

### ICEBERG_UNDERGONE_PARTITION_EVOLUTION

The source Apache Iceberg table has undergone partition evolution — meaning its partition scheme has changed over time. Delta Lake currently does not support cloning an Iceberg table that has evolved its partitions. Consider using an alternative method to migrate such a table. ^[delta_clone_incompatible_source-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The storage layer that provides ACID transactions and scalable metadata handling.
- [Deep Clone a Delta Table](/concepts/deep-clone-delta-table.md) – The operation that creates a full copy of a Delta table.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – Another open table format that can be used as a source for cloning.
- Delta Lake Indexes – Unsupported feature on Delta tables; dropping indexes resolves the HAS_INDEXES error.
- SQLSTATE – Standard error codes used in SQL diagnostic messages.
- Partition Evolution – A feature in Iceberg that changes partitioning over time; currently incompatible with Delta cloning.

## Sources

- delta_clone_incompatible_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_clone_incompatible_source-error-condition-databricks-on-aws.md](/references/delta_clone_incompatible_source-error-condition-databricks-on-aws-b63ca67d.md)
