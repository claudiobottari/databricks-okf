---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9c2150bc4acb643b31268a0515819cc3bfb17264b6adba185446f99c7e3a4949
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - icebergcompatv1-partition-spec-constraint
    - IPSC
  citations:
    - file: delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
title: IcebergCompatV1 Partition Spec Constraint
description: IcebergCompatV1 does not support replacing a partitioned table with a differently-named partition spec, mirroring a limitation in Iceberg-Spark 1.1.0.
tags:
  - partitioning
  - delta-lake
  - iceberg
  - limitations
timestamp: "2026-06-18T15:19:43.926Z"
---

# IcebergCompatV1 Partition Spec Constraint

**IcebergCompatV1 Partition Spec Constraint** is a validation rule enforced by the IcebergCompatV1 table feature in Delta Lake that prevents replacing a partitioned table's partition specification with a differently-named partition spec. This constraint exists because Iceberg-Spark 1.1.0 does not support such operations. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Overview

When a Delta table has IcebergCompatV1 enabled, the system validates all operations against compatibility requirements with Apache Iceberg. One specific constraint governs how partition specifications can be modified. If an operation attempts to replace a partitioned table with a new partition spec that has different column names, the operation fails with the `REPLACE_TABLE_CHANGE_PARTITION_NAMES` error. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Error Details

The error is part of the `DELTA_ICEBERG_COMPAT_V1_VIOLATION` error class with SQLSTATE `KD00E`. When triggered, the error message includes both the previous and new partition specifications for debugging: ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

```
IcebergCompatV1 doesn't support replacing partitioned tables with a differently-named partition spec, because Iceberg-Spark 1.1.0 doesn't.

Prev Partition Spec: <prevPartitionSpec>
New Partition Spec: <newPartitionSpec>
```

## Root Cause

The constraint stems from a limitation in Iceberg-Spark version 1.1.0, which does not support altering partition column names during a table replacement operation. Since IcebergCompatV1 ensures compatibility with this version of Iceberg, Delta Lake enforces the same restriction. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Workarounds

To change partition column names on a table with IcebergCompatV1 enabled, you must first disable IcebergCompatV1, perform the partition spec change, and then re-enable IcebergCompatV1. Note that disabling IcebergCompatV1 may require dropping other dependent table features first. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Related Constraints

IcebergCompatV1 enforces several other validation rules that may be relevant:

- **DISABLING_REQUIRED_TABLE_FEATURE**: Prevents dropping features that IcebergCompatV1 requires. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]
- **INCOMPATIBLE_TABLE_FEATURE**: Prevents enabling features incompatible with IcebergCompatV1. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]
- **MISSING_REQUIRED_TABLE_FEATURE**: Requires certain table features to be enabled. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]
- **UNSUPPORTED_DATA_TYPE**: Restricts schema types (MapType, ArrayType, NullType are not allowed). ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]
- **WRONG_REQUIRED_TABLE_PROPERTY**: Enforces specific table property values. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Related Concepts

- [IcebergCompatV1](/concepts/icebergcompatv1.md) — The table compatibility feature that enforces these constraints
- [Delta Lake Partitioning](/concepts/delta-lake-partitioning-constraints.md) — How Delta Lake organizes data into partitions
- Apache Iceberg Compatibility — Broader compatibility features between Delta Lake and Iceberg
- Delta Table Features — The feature system that governs table capabilities

## Sources

- delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md](/references/delta_iceberg_compat_v1_violation-error-class-databricks-on-aws-da04bc25.md)
