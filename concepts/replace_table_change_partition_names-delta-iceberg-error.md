---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3f4425240de6b3201a6e6e1acd2b1bb292c62cc091a89791be72fe1520f541f1
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - replace_table_change_partition_names-delta-iceberg-error
    - R(IE
  citations:
    - file: delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
title: REPLACE_TABLE_CHANGE_PARTITION_NAMES (Delta Iceberg error)
description: A sub-error of DELTA_ICEBERG_COMPAT_V1_VIOLATION that occurs when replacing a partitioned table with a differently-named partition spec, unsupported by IcebergCompatV1 due to Iceberg-Spark 1.1.0 limitations
tags:
  - delta-lake
  - error-subtype
  - partitioning
  - iceberg-compatibility
timestamp: "2026-06-19T15:05:17.085Z"
---

# REPLACE_TABLE_CHANGE_PARTITION_NAMES (Delta Iceberg error)

**REPLACE_TABLE_CHANGE_PARTITION_NAMES** is an error subclass of the DELTA_ICEBERG_COMPAT_V1_VIOLATION error class that occurs when attempting to replace a partitioned table with a differently-named partition specification while [IcebergCompatV1](/concepts/icebergcompatv1.md) is enabled. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Error Message

The error reports both the previous and new partition specifications:

```
IcebergCompatV1 doesn't support replacing partitioned tables with a differently-named partition spec, because Iceberg-Spark 1.1.0 doesn't.

Prev Partition Spec: <prevPartitionSpec>
New Partition Spec: <newPartitionSpec>
```

^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Cause

This error is triggered when a `REPLACE TABLE` operation changes the partition column names of an existing table that has IcebergCompatV1 enabled. The restriction exists because Iceberg-Spark 1.1.0 does not support modifying partition column names in a table replacement. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Workaround

To replace a table with a different partition specification, you must first disable IcebergCompatV1 on the table. Once the compatibility mode is removed, the table replacement operation can proceed with the new partition column names. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Related Concepts

- DELTA_ICEBERG_COMPAT_V1_VIOLATION error class – The parent error class containing all IcebergCompatV1 validation failures
- [IcebergCompatV1](/concepts/icebergcompatv1.md) – The Delta Lake compatibility mode that enforces Apache Iceberg compatibility
- Iceberg-Spark 1.1.0 – The Iceberg-Spark connector version that imposes this partition naming limitation
- [Delta Lake table features](/concepts/delta-lake-reader-table-features.md) – Features that may conflict with or be required by IcebergCompatV1

## Sources

- delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md](/references/delta_iceberg_compat_v1_violation-error-class-databricks-on-aws-da04bc25.md)
