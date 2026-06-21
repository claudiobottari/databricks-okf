---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 09a4fe8c02338939cefb2b1a4d3246d4d485ea5ef2cf14426ea36ad67a0f45e8
  pageDirectory: concepts
  sources:
    - delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - icebergwritercompatv
    - IcebergWriterCompat
    - IcebergWriterCompatV2
  citations:
    - file: delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
title: IcebergWriterCompatV
description: A versioned validation mechanism in Databricks Delta Lake that enforces compatibility constraints so Delta tables can be read by Apache Iceberg writers.
tags:
  - delta-lake
  - iceberg
  - compatibility
  - databricks
timestamp: "2026-06-19T18:25:42.421Z"
---

# IcebergWriterCompatV

**IcebergWriterCompatV** is a versioned compatibility validation mechanism in [Delta Lake](/concepts/delta-lake.md) that enforces constraints on write operations to ensure compatibility with [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md). When a Delta table is configured with a specific IcebergWriterCompatV version, Delta Lake checks every write transaction against that version's rules and raises a `DELTA_ICEBERG_WRITER_COMPAT_VIOLATION` error if any constraint is violated. The error has SQLSTATE `KD00E`. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Error Conditions

Each sub-error within `DELTA_ICEBERG_WRITER_COMPAT_VIOLATION` describes a specific type of violation that can occur during a write to a Delta table that has IcebergWriterCompatV enabled.

### CANNOT_CHANGE_MAP_STRUCT_KEY

IcebergWriterCompatV disallows changing map keys that are structs. This error occurs when a transaction attempts to modify the key of a map column where the key type is a struct. The error message lists the affected map names. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### CONFIG_NOT_ENABLED

IcebergWriterCompatV requires a specific configuration to be enabled on the table. This error occurs when that required configuration is not set, and the error message identifies the configuration key. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### DISABLING_REQUIRED_TABLE_FEATURE

IcebergWriterCompatV requires a specific [Delta Lake Table Features|table feature](/concepts/delta-lake-reader-table-features.md) to be supported and enabled. This error occurs when an operation attempts to drop that feature from the table, and the error message names the required feature. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### FIELD_ID_DOES_NOT_MATCH_PHYSICAL_NAME

IcebergWriterCompatV requires [column mapping](/concepts/column-mapping-in-delta-lake.md) field physical names to follow the pattern `col-[fieldId]`. This error occurs when one or more fields have physical names that do not conform to that convention. The error message lists the affected field names and their current physical names. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### INCOMPATIBLE_TABLE_FEATURE

IcebergWriterCompatV is incompatible with a specific table feature that is currently enabled on the table. This error occurs when a table has a feature enabled that conflicts with the requirements of the IcebergWriterCompatV version. The error message identifies the incompatible feature. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### MISSING_REQUIRED_TABLE_FEATURE

IcebergWriterCompatV requires a specific table feature to be supported and enabled, but that feature is not present on the table. The error message identifies which required feature is missing. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### UNSUPPORTED_DATA_TYPE

IcebergWriterCompatV does not support certain data types in the table schema. This error occurs when the schema contains a data type that is not supported by the specified compatibility version. The error message includes the unsupported data type and the full schema. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### UNSUPPORTED_ICEBERG_TABLE_PROPERTY

IcebergWriterCompatV does not support a specific Apache Iceberg table property that is set on the table. The error message identifies the unsupported property key. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### WRONG_REQUIRED_TABLE_PROPERTY

IcebergWriterCompatV requires a specific table property to be set to a particular value. This error occurs when the property is set to a different value than required. The error message includes the property key, the required value, and the current actual value. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer that enforces IcebergWriterCompatV validation
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The open table format that the compatibility mode targets
- Delta Lake Table Features — Features that may be required or incompatible with IcebergWriterCompatV
- [Column Mapping](/concepts/delta-table-column-mapping.md) — The feature that requires physical names to follow the `col-[fieldId]` pattern
- Delta Lake Configuration Properties — Table properties that may need specific values for Iceberg compatibility

## Sources

- delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws-02e8eab9.md)
