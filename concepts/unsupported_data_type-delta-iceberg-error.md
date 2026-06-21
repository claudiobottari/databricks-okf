---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 31f43a39f007807112429724ae0a897743d878e3051f2124777503a09ef5ccbb
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unsupported_data_type-delta-iceberg-error
    - U(IE
  citations:
    - file: delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
title: UNSUPPORTED_DATA_TYPE (Delta Iceberg error)
description: A sub-error of DELTA_ICEBERG_COMPAT_V1_VIOLATION that occurs when a table schema contains MapType, ArrayType, or NullType, which are unsupported by IcebergCompatV1
tags:
  - delta-lake
  - error-subtype
  - data-types
  - iceberg-compatibility
timestamp: "2026-06-19T15:05:17.377Z"
---

# UNSUPPORTED_DATA_TYPE (Delta Iceberg error)

The **UNSUPPORTED_DATA_TYPE** error occurs when attempting to apply the `IcebergCompatV1` table feature to a Delta table that contains columns with MapType, ArrayType, or NullType in its schema. IcebergCompatV1 does not support these data types. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Error Message

The error returns the following message:

```
IcebergCompatV1 doesn't support schema with MapType or ArrayType or NullType. Your schema:
<schema>
```

^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Cause

The `IcebergCompatV1` table feature imposes restrictions on the schema of a Delta table. If the table's schema contains any column of type `MapType`, `ArrayType`, or `NullType`, validation fails with this error. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Solutions

To resolve this error, you must modify the table schema to remove or replace the unsupported column types:

- Convert `MapType` columns to an alternative representation compatible with Iceberg, such as using `StructType` with key-value pairs or storing data as JSON strings in a `StringType` column.
- Convert `ArrayType` columns to a compatible representation, such as a `StringType` column containing serialized arrays, or restructure into separate rows.
- Remove columns of type `NullType`, or replace them with a concrete data type.

After modifying the schema, you can then enable `IcebergCompatV1` on the table.

## Related Concepts

- IcebergCompatV1 table feature — The Delta table feature that enables Iceberg compatibility, which enforces these schema restrictions.
- UNSUPPORTED_DATA_TYPE — The specific error subclass within the DELTA_ICEBERG_COMPAT_V1_VIOLATION error class.
- DELTA_ICEBERG_COMPAT_V1_VIOLATION error class — The parent error class containing all IcebergCompatV1 validation failures.
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format that supports Iceberg compatibility features.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The compatible table format that IcebergCompatV1 enables interoperability with.

## Sources

- delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md](/references/delta_iceberg_compat_v1_violation-error-class-databricks-on-aws-da04bc25.md)
