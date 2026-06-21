---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 011439ff963e1d122165950e74f6933edfa7ac04be07b64c1105e80ed409e430
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-iceberg-partition-spec-constraints
    - DIPSC
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: Delta Iceberg Partition Spec Constraints
description: A restriction that replacing partitioned tables with differently-named partition specs is not supported under IcebergCompatV due to Iceberg-Spark 1.1.0 limitations.
tags:
  - delta-lake
  - apache-iceberg
  - partitioning
timestamp: "2026-06-19T15:06:50.305Z"
---

# Delta Iceberg Partition Spec Constraints

**Delta Iceberg Partition Spec Constraints** refer to limitations imposed by the [IcebergCompatV](/concepts/icebergcompatv2.md) protocol on Delta Lake tables when partitioning is modified. These constraints arise from compatibility requirements with the [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) metadata layer and the Iceberg-Spark connector.

## Overview

When a Delta table has [IcebergCompatV](/concepts/icebergcompatv2.md) enabled, the partition specification is governed by Iceberg's metadata model. This creates specific restrictions on partition-related operations that would otherwise be permissible in standard Delta Lake tables. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Partition Rename Restrictions

IcebergCompatV does not support replacing partitioned tables with a differently-named partition spec. This is because Iceberg-Spark 1.1.0 does not support partition rename operations. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Error: REPLACE_TABLE_CHANGE_PARTITION_NAMES

If you attempt to replace a partitioned table with a new partition spec that uses different column names, the operation fails with the `REPLACE_TABLE_CHANGE_PARTITION_NAMES` error. The error message includes both the previous and the new partition specifications:

- **Prev Partition Spec**: `<prevPartitionSpec>`
- **New Partition Spec**: `<newPartitionSpec>`

^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Unsupported Partition Data Types

IcebergCompatV imposes restrictions on the data types that can be used for partition columns. Not all Delta-supported data types are compatible with Iceberg's partition model. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Error: UNSUPPORTED_PARTITION_DATA_TYPE

When attempting to create or convert a table with an unsupported data type in a partition column, the `UNSUPPORTED_PARTITION_DATA_TYPE` error is raised:

```
IcebergCompatV<version> does not support the data type <dataType> for partition columns in your schema.
Your partition schema:
<schema>
```

^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Related Constraints

Several other partition-related constraints apply under IcebergCompatV:

- **Unsupported data types in schema**: The `UNSUPPORTED_DATA_TYPE` error occurs when any column (not just partition columns) uses a data type not supported by IcebergCompatV. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

- **Iceberg version mutual exclusivity**: Only one IcebergCompat version can be enabled at a time. All other IcebergCompat versions must be explicitly disabled (`VERSION_MUTUAL_EXCLUSIVE`). ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

- **Schema compatibility checks**: During table creation or conversion, Iceberg performs schema compatibility validation that may fail (`SCHEMA_COMPATIBILITY_CHECK_FAILED`). ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

- **Type widening conflicts**: IcebergCompatV is incompatible with type changes applied to fields after table creation (`UNSUPPORTED_TYPE_WIDENING`). This includes type widening on partition columns. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Best Practices

To avoid partition spec constraint violations when using IcebergCompatV:

- Design partition schemas with Iceberg-compatible data types before enabling IcebergCompatV.
- Avoid changing partition column names after the table has been created with IcebergCompatV enabled.
- Run `REORG TABLE APPLY (UPGRADE UNIFORM ('ICEBERG_COMPAT_VERSION = <newVersion>'))` when upgrading to a new IcebergCompat version, as recommended in the `CHANGE_VERSION_NEED_REWRITE` error. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]
- Disable all other IcebergCompat versions before enabling a new one.
- Avoid type widening operations on existing columns while IcebergCompatV is active.

## Related Concepts

- [IcebergCompatV](/concepts/icebergcompatv2.md) – The compatibility version that enforces these partition constraints.
- [Delta Lake Partitioning](/concepts/delta-lake-partitioning-constraints.md) – General partitioning concepts in Delta Lake.
- [Uniform Format](/concepts/delta-uniform-uniform.md) – The unified format that bridges Delta and Iceberg metadata.
- Delta Lake Table Features – The features system that enables IcebergCompatV.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – The open table format that defines the compatibility constraints.
- [REORG TABLE command](/concepts/reorg-table-command.md) – The command used to upgrade uniform format and resolve compatibility violations.
- [Deletion Vectors](/concepts/deletion-vectors.md) – Table feature that must be purged or disabled before enabling IcebergCompatV.

## Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
