---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0d120bf30485edc30d88973dd1230281db568d68b88b5506137b773513ac22fb
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_iceberg_compat_v1_violation
    - DELTA_ICEBERG_COMPAT_V1_VIOLATION
    - DELTA_ICEBERG_COMPAT_VIOLATION
    - delta_iceberg_compat_v1_violation-error-class
    - DEC
    - DELTA_ICEBERG_COMPAT_V1_VIOLATION error class
    - IcebergCompatV1 error class
    - delta_iceberg_compat_violation-error-class
    - DELTA_ICEBERG_COMPAT_VIOLATION Error Class
    - DELTA_ICEBERG_COMPAT_VIOLATION error class
  citations:
    - file: delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
title: DELTA_ICEBERG_COMPAT_V1_VIOLATION
description: A Delta Lake error class indicating that validation of IcebergCompatV1 has failed on a table operation
tags:
  - delta-lake
  - error-class
  - iceberg-compatibility
timestamp: "2026-06-19T15:05:14.761Z"
---

# DELTA_ICEBERG_COMPAT_V1_VIOLATION Error Class

## Overview

The `DELTA_ICEBERG_COMPAT_V1_VIOLATION` error class (SQLSTATE `KD00E`) occurs when a [Delta Lake](/concepts/delta-lake.md) table operation violates the requirements of [IcebergCompatV1](/concepts/icebergcompatv.md), a compatibility mode that allows Delta tables to be read by Apache Iceberg readers. The validation failure prevents the operation from completing. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

This error class includes several specific subtypes, each corresponding to a different type of violation.

## Error Subtypes

### DISABLING_REQUIRED_TABLE_FEATURE

IcebergCompatV1 requires a specific table feature to be supported and enabled. This error occurs when an attempt is made to drop that feature from the table. To resolve, disable IcebergCompatV1 first before removing the required feature. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

- **Error message:** `IcebergCompatV1 requires feature <feature> to be supported and enabled. You cannot drop it from the table. Instead, please disable IcebergCompatV1 first.`

### INCOMPATIBLE_TABLE_FEATURE

The table has a feature enabled that is incompatible with IcebergCompatV1. The operation is blocked because IcebergCompatV1 cannot coexist with the conflicting feature. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

- **Error message:** `IcebergCompatV1 is incompatible with feature <feature>.`

### MISSING_REQUIRED_TABLE_FEATURE

IcebergCompatV1 requires a particular table feature to be present and enabled, but it is missing. The operation cannot proceed until the required feature is added. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

- **Error message:** `IcebergCompatV1 requires feature <feature> to be supported and enabled.`

### REPLACE_TABLE_CHANGE_PARTITION_NAMES

IcebergCompatV1 does not support replacing a partitioned table with a differently-named partition specification, because Apache Iceberg-Spark 1.1.0 lacks this capability. The error includes the previous and new partition specs. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

- **Error message:** `IcebergCompatV1 doesn't support replacing partitioned tables with a differently-named partition spec, because Iceberg-Spark 1.1.0 doesn't. Prev Partition Spec: <prevPartitionSpec> New Partition Spec: <newPartitionSpec>`

### UNSUPPORTED_DATA_TYPE

The table schema contains data types that are not supported by IcebergCompatV1. Specifically, `MapType`, `ArrayType`, and `NullType` are not allowed. The error includes the full schema. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

- **Error message:** `IcebergCompatV1 doesn't support schema with MapType or ArrayType or NullType. Your schema: <schema>`

### WRONG_REQUIRED_TABLE_PROPERTY

IcebergCompatV1 requires a specific table property to be set to a particular value. This error occurs when the property exists but has an incorrect value. The error includes the property key, the required value, and the current value. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

- **Error message:** `IcebergCompatV1 requires table property '<key>' to be set to '<requiredValue>'. Current value: '<actualValue>'.`

## Related Concepts

- [IcebergCompatV1](/concepts/icebergcompatv.md) – The compatibility mode that enforces these validation rules.
- Delta Lake Table Features – The mechanism for enabling/disabling capabilities that may conflict with IcebergCompatV1.
- Partition Specifications – Rules for how table data is partitioned; changing partition names is restricted under IcebergCompatV1.
- Delta Lake Data Types – Supported column types; MapType, ArrayType, and NullType are incompatible with IcebergCompatV1.

## Sources

- delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md](/references/delta_iceberg_compat_v1_violation-error-class-databricks-on-aws-da04bc25.md)
