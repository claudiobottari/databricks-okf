---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 281feafc7b80571e812da684a8c7f5fe9835b1906973e2e80bdabdd3d0b55b89
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unsupported_data_type-in-icebergcompatv1
    - UII
    - unsupported_data_type-delta-iceberg-error
    - U(IE
  citations:
    - file: delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
title: UNSUPPORTED_DATA_TYPE in IcebergCompatV1
description: Error sub-type indicating IcebergCompatV1 does not support schemas containing MapType, ArrayType, or NullType columns
tags:
  - error-messages
  - data-types
  - schema
  - delta-lake
timestamp: "2026-06-19T18:25:31.639Z"
---

# UNSUPPORTED_DATA_TYPE in IcebergCompatV1

**UNSUPPORTED_DATA_TYPE** is an error that occurs when attempting to use [IcebergCompatV1](/concepts/icebergcompatv.md) on a Delta table whose schema contains `MapType`, `ArrayType`, or `NullType` columns. IcebergCompatV1 does not support these data types, and the operation fails with a descriptive error message. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Error Message

When this error occurs, Databricks returns the following message:

```
IcebergCompatV1 doesn't support schema with MapType or ArrayType or NullType. Your schema:
<schema>
```

^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

The `<schema>` placeholder is replaced with the actual schema of the table that triggered the error.

## Cause

IcebergCompatV1 enforces compatibility with the Apache Iceberg specification, which does not support the following Delta data types: ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

- **MapType** — Key-value map structures
- **ArrayType** — Array or list structures
- **NullType** — Columns with null-only data

If a table enabled with IcebergCompatV1 contains any column of these types, any operation that validates Iceberg compatibility will fail with this error.

## Affected Operations

The error can occur during any operation that triggers IcebergCompatV1 validation, including: ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

- Enabling IcebergCompatV1 on an existing table
- Writing data to a table with IcebergCompatV1 enabled
- Reading or querying a table with IcebergCompatV1 enabled
- Altering the schema of a table with IcebergCompatV1 enabled

## Resolution

To resolve this error, you must remove or replace the unsupported data types from the table schema before using IcebergCompatV1. Options include: ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

1. **Restructure the schema** — Convert `MapType` and `ArrayType` columns to supported types such as `StructType` or individual columns.
2. **Drop unsupported columns** — Remove columns with unsupported types if they are not needed.
3. **Use a different compatibility mode** — Consider using [IcebergCompatV2](/concepts/icebergcompatv2.md) if it supports the required data types, or disable Iceberg compatibility entirely.

## Related Errors

UNSUPPORTED_DATA_TYPE is one of several errors in the DELTA_ICEBERG_COMPAT_V1_VIOLATION error class. Related errors include: ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

- DISABLING_REQUIRED_TABLE_FEATURE — Attempting to drop a feature required by IcebergCompatV1
- INCOMPATIBLE_TABLE_FEATURE — A table feature that conflicts with IcebergCompatV1
- MISSING_REQUIRED_TABLE_FEATURE — A required feature is not enabled
- REPLACE_TABLE_CHANGE_PARTITION_NAMES — Renaming partitions in a partitioned table
- WRONG_REQUIRED_TABLE_PROPERTY — A required table property has an incorrect value

## Related Concepts

- [IcebergCompatV1](/concepts/icebergcompatv.md) — The Delta table compatibility mode for Apache Iceberg
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The open table format that IcebergCompatV1 targets
- Delta table features — Features that IcebergCompatV1 requires or is incompatible with

## Sources

- delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md](/references/delta_iceberg_compat_v1_violation-error-class-databricks-on-aws-da04bc25.md)
