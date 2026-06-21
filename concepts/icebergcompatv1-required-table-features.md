---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5667b0f7ddd3a04befed4c3b7e5eac62125468feb3e8e8c79fd90c66715e6157
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - icebergcompatv1-required-table-features
    - IRTF
    - IcebergCompatV1 table feature
  citations:
    - file: delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
title: IcebergCompatV1 Required Table Features
description: Certain Delta table features must be enabled and cannot be dropped while IcebergCompatV1 is active; disabling the compatibility mode is required first.
tags:
  - table-features
  - delta-lake
  - iceberg
  - constraints
timestamp: "2026-06-18T15:19:38.120Z"
---

# IcebergCompatV1 Required Table Features

**IcebergCompatV1 Required Table Features** refers to the specific table features and properties that must be enabled or configured for a [Delta Lake](/concepts/delta-lake.md) table to be compatible with Apache Iceberg's V1 compatibility mode. These requirements ensure that the table can be properly read by Iceberg readers and maintain consistency across formats.

## Overview

IcebergCompatV1 imposes strict validation on Delta tables to ensure compatibility with the Iceberg format. When this compatibility mode is enabled, certain table features become mandatory, while others become incompatible. Violations result in a `DELTA_ICEBERG_COMPAT_V1_VIOLATION` error, which carries SQLSTATE `KD00E`.^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Required Table Features

### Features That Must Be Enabled

IcebergCompatV1 requires that specific table features be both supported and enabled on the table. These features are essential for Iceberg compatibility and cannot be dropped while IcebergCompatV1 is active.^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

If a required table feature is missing or disabled, the system raises the `MISSING_REQUIRED_TABLE_FEATURE` or `DISABLING_REQUIRED_TABLE_FEATURE` error, respectively. To remove such a feature, users must first disable IcebergCompatV1 on the table.^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

### Required Table Properties

IcebergCompatV1 requires certain table properties to be set to specific values. If a required property has an incorrect value, the system raises the `WRONG_REQUIRED_TABLE_PROPERTY` error, which indicates the required key, the required value, and the actual current value.^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Incompatible Features

Some table features are incompatible with IcebergCompatV1. If an incompatible feature is enabled on a table with IcebergCompatV1 active, the system raises the `INCOMPATIBLE_TABLE_FEATURE` error. Users must remove or disable the incompatible feature before using IcebergCompatV1.^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Unsupported Data Types

IcebergCompatV1 does not support schemas containing `MapType`, `ArrayType`, or `NullType` columns. If the table schema includes any of these data types, the system raises the `UNSUPPORTED_DATA_TYPE` error. This restriction applies because the Iceberg format does not have direct equivalents for these Delta data types.^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Partitioning Constraints

IcebergCompatV1 does not support replacing partitioned tables with a differently-named partition specification. This limitation exists because Iceberg-Spark 1.1.0 does not support renaming partition specs during a table replacement operation. If a `REPLACE TABLE` operation attempts to change partition column names, the system raises the `REPLACE_TABLE_CHANGE_PARTITION_NAMES` error.^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Error Summary

| Error Subtype | Cause |
|---------------|-------|
| `DISABLING_REQUIRED_TABLE_FEATURE` | Attempting to drop a feature that IcebergCompatV1 requires |
| `INCOMPATIBLE_TABLE_FEATURE` | An incompatible feature is enabled |
| `MISSING_REQUIRED_TABLE_FEATURE` | A required feature is not enabled |
| `REPLACE_TABLE_CHANGE_PARTITION_NAMES` | Trying to rename partition specs during table replacement |
| `UNSUPPORTED_DATA_TYPE` | Schema contains MapType, ArrayType, or NullType |
| `WRONG_REQUIRED_TABLE_PROPERTY` | A required table property has an incorrect value |

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage format underlying Iceberg compatibility
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The open table format for which compatibility is provided
- Table Features in Delta Lake — The feature system that enables format-specific capabilities
- Delta Table Properties — Configuration properties for Delta tables
- [IcebergCompatV1](/concepts/icebergcompatv.md) — The broader compatibility mode setting

## Sources

- delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md](/references/delta_iceberg_compat_v1_violation-error-class-databricks-on-aws-da04bc25.md)
