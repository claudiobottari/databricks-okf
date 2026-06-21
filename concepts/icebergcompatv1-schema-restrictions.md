---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 29cf1792d0e4031bb15ae8a1bfc660b39c34c03625fbc6aa718a86933bf79efe
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - icebergcompatv1-schema-restrictions
    - ISR
  citations:
    - file: delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
title: IcebergCompatV1 Schema Restrictions
description: The constraint that IcebergCompatV1 does not support tables with MapType, ArrayType, or NullType columns in their schema, due to limitations in the Iceberg format.
tags:
  - delta-lake
  - iceberg
  - schema
  - data-types
timestamp: "2026-06-19T10:06:02.621Z"
---

# IcebergCompatV1 Schema Restrictions

**IcebergCompatV1 Schema Restrictions** define the structural and type constraints that Delta Lake tables must satisfy to be compatible with Iceberg V1 format. When a table violates these restrictions, Databricks raises the `DELTA_ICEBERG_COMPAT_V1_VIOLATION` error class (SQLSTATE: KD00E) during validation. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Overview

IcebergCompatV1 imposes specific schema requirements to ensure Delta tables can be read by Apache Iceberg V1-compatible readers. These restrictions cover data types, partitioning behavior, table features, and table properties. Violations prevent operations that would create an incompatible table state. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Unsupported Data Types

IcebergCompatV1 does **not** support schemas that contain the following column data types:^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

- `MapType` — Map columns are not allowed
- `ArrayType` — Array columns are not allowed
- `NullType` — Columns of type NULL are not allowed

If a table's schema includes any of these types, the system returns the `UNSUPPORTED_DATA_TYPE` error with the offending schema. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Partitioning Restrictions

IcebergCompatV1 does not support replacing a partitioned table with a differently-named partition specification. This is because Iceberg-Spark 1.1.0 does not support partition spec renaming. If you attempt to `REPLACE TABLE` with a partition spec whose column names differ from the previous spec, the system returns the `REPLACE_TABLE_CHANGE_PARTITION_NAMES` error. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

The error message includes both the previous and new partition specs for reference. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Required Table Features

IcebergCompatV1 requires certain Delta table features to be both supported and enabled on the table:^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

- If a required feature is missing, the system returns `MISSING_REQUIRED_TABLE_FEATURE`, identifying which feature is required.
- If an attempt is made to drop a required feature, the system returns `DISABLING_REQUIRED_TABLE_FEATURE`. The feature must remain enabled; the only way to remove it is to disable IcebergCompatV1 first.

## Incompatible Table Features

Some table features are inherently incompatible with IcebergCompatV1. If such a feature is present and enabled on the table, the system returns the `INCOMPATIBLE_TABLE_FEATURE` error. You must remove or disable the incompatible feature before enabling IcebergCompatV1. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Required Table Properties

IcebergCompatV1 mandates that specific table properties be set to exact values. If a property is missing or set to an incorrect value, the system returns the `WRONG_REQUIRED_TABLE_PROPERTY` error, which indicates:^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

- The property key (`<key>`)
- The required value (`<requiredValue>`)
- The current actual value (`<actualValue>`)

To resolve this error, update the table property to match the required value.

## Error Subtypes Summary

| Error Subtype | Cause |
|---|---|
| `UNSUPPORTED_DATA_TYPE` | Schema contains MapType, ArrayType, or NullType |
| `REPLACE_TABLE_CHANGE_PARTITION_NAMES` | Attempt to rename partition columns in REPLACE TABLE |
| `MISSING_REQUIRED_TABLE_FEATURE` | Required table feature is not enabled |
| `DISABLING_REQUIRED_TABLE_FEATURE` | Attempt to drop a required table feature |
| `INCOMPATIBLE_TABLE_FEATURE` | An incompatible feature is enabled on the table |
| `WRONG_REQUIRED_TABLE_PROPERTY` | A required table property is missing or incorrect |

## Related Concepts

- [Delta-Iceberg Compatibility](/concepts/delta-iceberg-table-feature-compatibility.md) — General compatibility between Delta Lake and Apache Iceberg
- Delta Table Features — The feature system that governs table capabilities
- [IcebergCompatV1](/concepts/icebergcompatv1.md) — The compatibility mode that enforces these restrictions
- Delta Table Properties — Configuration properties for Delta tables

## Sources

- delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md](/references/delta_iceberg_compat_v1_violation-error-class-databricks-on-aws-da04bc25.md)
