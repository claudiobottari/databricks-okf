---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 22330c123f0699935b5dd62a9191eeae53f95770cc62bfcc34513d113abe1e75
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_iceberg_compat_v1_violation-error-class
    - DEC
    - DELTA_ICEBERG_COMPAT_V1_VIOLATION error class
    - IcebergCompatV1 error class
  citations:
    - file: delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
title: DELTA_ICEBERG_COMPAT_V1_VIOLATION error class
description: A Delta Lake error class raised when IcebergCompatV1 validation fails on a table operation
tags:
  - error-messages
  - delta-lake
  - databricks
timestamp: "2026-06-19T18:25:24.719Z"
---

# DELTA_ICEBERG_COMPAT_V1_VIOLATION Error Class

The `DELTA_ICEBERG_COMPAT_V1_VIOLATION` error class occurs when a Delta table operation violates the constraints required by [IcebergCompatV1](/concepts/icebergcompatv1.md), a compatibility mode that ensures Delta tables can be read by Apache Iceberg. This error is raised during validation checks on Delta Lake tables and includes several sub-errors that identify the specific type of violation. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## SQLSTATE

This error class maps to SQLSTATE `KD00E`, which falls under the KD class (datasource-specific errors) in Databricks error classification. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Sub-Errors

The `DELTA_ICEBERG_COMPAT_V1_VIOLATION` error class encompasses several distinct sub-error types, each addressing a specific validation failure:

### DISABLING_REQUIRED_TABLE_FEATURE

IcebergCompatV1 requires a specific table feature `<feature>` to be supported and enabled on the Delta table. This error occurs when attempting to drop or disable that required feature. To resolve this, disable IcebergCompatV1 first rather than removing the required table feature. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

### INCOMPATIBLE_TABLE_FEATURE

IcebergCompatV1 is incompatible with the table feature `<feature>`. This error indicates that the specified table feature cannot coexist with IcebergCompatV1, and using both simultaneously is not permitted. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

### MISSING_REQUIRED_TABLE_FEATURE

IcebergCompatV1 requires the table feature `<feature>` to be both supported and enabled, but it is currently missing from the table configuration. The table must have this feature present to maintain Iceberg compatibility. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

### REPLACE_TABLE_CHANGE_PARTITION_NAMES

IcebergCompatV1 does not support replacing a partitioned table with a differently-named partition spec, because [Iceberg-Spark](/concepts/icebergcompatv2.md) 1.1.0 lacks this capability. The error message displays both the previous partition spec and the new partition spec for reference. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

### UNSUPPORTED_DATA_TYPE

IcebergCompatV1 does not support schemas that contain `MapType`, `ArrayType`, or `NullType` data types. When this error occurs, it includes the offending schema that triggered the violation. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

### WRONG_REQUIRED_TABLE_PROPERTY

IcebergCompatV1 requires a specific table property `<key>` to be set to a required value `<requiredValue>`. This error occurs when the current value `<actualValue>` does not match the required value, indicating a misconfigured table property. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The storage layer that provides IcebergCompatV1 compatibility mode
- [IcebergCompatV1](/concepts/icebergcompatv1.md) – The specific compatibility mode enabling Delta tables to be read by Apache Iceberg
- Table features – Delta Lake protocol features that can be enabled or disabled
- Partition spec – The definition of how a table is partitioned
- [Databricks error messages](/concepts/databricks-error-message-reference.md) – General guidance on interpreting Databricks error classes and SQLSTATE codes

## Sources

- delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md](/references/delta_iceberg_compat_v1_violation-error-class-databricks-on-aws-da04bc25.md)
