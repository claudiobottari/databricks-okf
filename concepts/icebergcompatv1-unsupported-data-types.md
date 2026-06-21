---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1130e5cc4e57e0944e45e66d31c9a9acc352308d683160974f06d24d6230c976
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - icebergcompatv1-unsupported-data-types
    - IUDT
    - Iceberg-unsupported data types
  citations:
    - file: delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
title: IcebergCompatV1 Unsupported Data Types
description: Schemas containing MapType, ArrayType, or NullType are rejected under IcebergCompatV1 because Iceberg does not support these types.
tags:
  - schema
  - data-types
  - delta-lake
  - iceberg
timestamp: "2026-06-18T15:20:00.355Z"
---

# IcebergCompatV1 Unsupported Data Types

**IcebergCompatV1 Unsupported Data Types** refers to a specific validation failure that occurs when attempting to create or modify a [Delta Lake](/concepts/delta-lake.md) table with IcebergCompatV1 enabled that contains certain unsupported column types.

## Error Overview

When IcebergCompatV1 compatibility mode is enabled for a Delta table, the schema cannot contain `MapType`, `ArrayType`, or `NullType` columns. If a table schema includes these types, the operation fails with the `UNSUPPORTED_DATA_TYPE` error. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Error Message

The error appears as follows:

```
UNSUPPORTED_DATA_TYPE
IcebergCompatV1 doesn't support schema with MapType or ArrayType or NullType. Your schema: <schema>
```

The `<schema>` placeholder shows the full table schema, including the unsupported column type that caused the validation failure. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Unsupported Data Types

The following column types are incompatible with IcebergCompatV1:

- **MapType** — Columns that store key-value pairs (e.g., `MAP<STRING, INT>`)
- **ArrayType** — Columns that store lists or arrays of elements (e.g., `ARRAY<STRING>`)
- **NullType** — Columns with no defined type (typically used for `NULL` literals)

^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Why These Types Are Unsupported

IcebergCompatV1 maps Delta Lake schemas to [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) format specifications. The Iceberg-Spark 1.1.0 compatibility layer that IcebergCompatV1 relies on does not support MapType or ArrayType at the schema level. NullType represents untyped data that cannot be meaningfully translated between the two formats. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## How to Resolve

### Option 1: Restructure the Schema

Replace unsupported column types with Iceberg-compatible alternatives:

- **ArrayType** → Use a separate child table with a foreign key relationship, or store as a serialized string (e.g., JSON) using `STRING` type
- **MapType** → Flatten into separate columns or store as a serialized string using `STRING` type
- **NullType** → Define an explicit data type for the column instead of leaving it untyped

### Option 2: Disable IcebergCompatV1

If the table fundamentally requires these data types, disable IcebergCompatV1 and use standard Delta Lake format instead. See DELTA_ICEBERG_COMPAT_V1_VIOLATION error class|IcebergCompatV1 error class for related error handling.

## Related Concepts

- DELTA_ICEBERG_COMPAT_V1_VIOLATION error class|IcebergCompatV1 error class — Full list of IcebergCompatV1 validation errors
- [Delta Lake to Iceberg compatibility](/concepts/delta-lake-table-features-compatibility.md) — Overview of format interoperability
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — Target format for IcebergCompatV1
- Delta Lake data types — Supported column types in Delta Lake
- Schema evolution in Delta Lake — How schemas can be modified over time

## Sources

- delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md](/references/delta_iceberg_compat_v1_violation-error-class-databricks-on-aws-da04bc25.md)
