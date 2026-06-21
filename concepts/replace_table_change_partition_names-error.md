---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d7afaa0d15c871a443ea9b4c7447b9ad2392e09e1ff62b818d13df4bf0606347
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - replace_table_change_partition_names-error
  citations:
    - file: delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
title: REPLACE_TABLE_CHANGE_PARTITION_NAMES error
description: A sub-error of DELTA_ICEBERG_COMPAT_V1_VIOLATION triggered when replacing a partitioned table with a differently-named partition spec, mirroring a limitation in Iceberg-Spark 1.1.0.
tags:
  - delta-lake
  - partitioning
  - error-handling
  - iceberg-compatibility
timestamp: "2026-06-18T11:54:05.331Z"
---

# REPLACE\_TABLE\_CHANGE\_PARTITION\_NAMES Error

The **REPLACE\_TABLE\_CHANGE\_PARTITION\_NAMES** error occurs when using [IcebergCompatV1](/concepts/icebergcompatv1.md) on a Delta table and attempting to replace a partitioned table with a differently-named partition specification. This operation is not supported because the underlying Iceberg-Spark 1.1.0 library does not support partition spec renaming. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Error Message

When this error occurs, Delta Lake returns the following message:

```
IcebergCompatV1 doesn't support replacing partitioned tables with a differently-named partition spec, because Iceberg-Spark 1.1.0 doesn't.

Prev Partition Spec: <prevPartitionSpec>

New Partition Spec: <newPartitionSpec>
```

^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

The error message includes both the previous partition specification and the new partition specification that was attempted, helping you identify the naming change that caused the conflict. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Cause

The error is triggered when you attempt to replace a table's partition specification with one that has different partition column names while IcebergCompatV1 is enabled on the table. The compatibility layer between Delta Lake and Apache Iceberg, specifically through Iceberg-Spark 1.1.0, does not support the operation of changing partition column names during a `REPLACE TABLE` operation. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Solution

To resolve this error, you have the following options:

- **Disable IcebergCompatV1** on the table before performing the partition spec rename. After the rename is complete, you can re-enable IcebergCompatV1 if needed. Use `ALTER TABLE ... SET TBLPROPERTIES` to modify the `delta.enableIcebergCompatV1` property. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

- **Keep the same partition column names** in your new partition specification. If you only need to change how data is organized within existing partition columns (for example, changing partitioning strategy without renaming columns), the operation may succeed. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

- **Create a new table** with the desired partition specification and copy data from the original table. This approach avoids the `REPLACE TABLE` operation entirely. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Related Error Subtypes

This error is part of the `DELTA_ICEBERG_COMPAT_V1_VIOLATION` error class, which includes other validation failures related to IcebergCompatV1: ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

- `DISABLING_REQUIRED_TABLE_FEATURE` — Attempting to drop a feature required by IcebergCompatV1
- `INCOMPATIBLE_TABLE_FEATURE` — Using a feature incompatible with IcebergCompatV1
- `MISSING_REQUIRED_TABLE_FEATURE` — Missing a table feature required by IcebergCompatV1
- `UNSUPPORTED_DATA_TYPE` — Using MapType, ArrayType, or NullType in the schema
- `WRONG_REQUIRED_TABLE_PROPERTY` — A required property is set to an incorrect value

## Related Concepts

- [IcebergCompatV1](/concepts/icebergcompatv1.md) — The Delta Lake compatibility mode for Apache Iceberg
- [Delta Lake Partitioning](/concepts/delta-lake-partitioning-constraints.md) — How Delta Lake organizes data across partitions
- REPLACE TABLE — The SQL command for replacing table definitions
- Delta Lake Table Properties — Configuration properties for Delta tables

## Sources

- delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md](/references/delta_iceberg_compat_v1_violation-error-class-databricks-on-aws-da04bc25.md)
