---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b1db8bca0b79a1c1ca92796e00675a139b71ac792356502faf35d6937c45cbaf
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - replace_table_change_partition_names
    - REPLACE_TABLE_CHANGE_PARTITION_NAMES
    - replace_table_change_partition_names-delta-iceberg-error
    - R(IE
    - replace_table_change_partition_names-error
  citations:
    - file: delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
title: REPLACE_TABLE_CHANGE_PARTITION_NAMES
description: Error sub-type indicating IcebergCompatV1 does not support replacing partitioned tables with a differently-named partition spec
tags:
  - error-messages
  - partitioning
  - iceberg
  - delta-lake
timestamp: "2026-06-19T18:25:09.772Z"
---

## REPLACE_TABLE_CHANGE_PARTITION_NAMES

The **REPLACE_TABLE_CHANGE_PARTITION_NAMES** error is a sub‑class of the DELTA_ICEBERG_COMPAT_V1_VIOLATION error class. It occurs when an attempt is made to replace a partitioned Delta table while changing the names of the partition columns, but the table has the `IcebergCompatV1` table property enabled. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

### Error Details

IcebergCompatV1 does not support replacing a partitioned table with a differently‑named partition specification. This limitation exists because the underlying Iceberg‑Spark 1.1.0 connector itself does not support renaming partition columns when replacing a table. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

The error message includes both the **previous partition spec** and the **new partition spec** for reference:

```
Prev Partition Spec: <prevPartitionSpec>
New Partition Spec: <newPartitionSpec>
```

^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

### Cause

The `REPLACE TABLE` command was issued against a table that has `IcebergCompatV1` enabled, and the new partition specification uses column names that differ from the existing partition columns. The compatibility layer rejects the operation because Iceberg‑Spark cannot handle the change.

### Suggested Actions

To perform the partition rename, you must first disable `IcebergCompatV1` on the table. After disabling the compatibility property, the `REPLACE TABLE` command with a differently‑named partition spec can proceed without the error. Alternatively, avoid renaming partition columns while `IcebergCompatV1` remains active.

### Related Concepts

- DELTA_ICEBERG_COMPAT_V1_VIOLATION – The parent error class for IcebergCompatV1 validation failures
- [IcebergCompatV1](/concepts/icebergcompatv.md) – The Delta table property that enforces Iceberg compatibility
- REPLACE TABLE – The SQL command that triggers this error when used with partition renaming
- Delta table partitioning – Partitioning strategies for Delta Lake tables
- [Iceberg‑Spark connector](/concepts/opensharing-apache-spark-connector.md) – The underlying library that imposes the limitation

### Sources

- delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md](/references/delta_iceberg_compat_v1_violation-error-class-databricks-on-aws-da04bc25.md)
