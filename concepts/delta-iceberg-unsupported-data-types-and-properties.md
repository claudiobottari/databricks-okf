---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7a9aa5b4b2a8a44ed3ba7258732ab21cc470914960d9f253ddeff2d1c775ab41
  pageDirectory: concepts
  sources:
    - delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-iceberg-unsupported-data-types-and-properties
    - Properties and Delta-Iceberg Unsupported Data Types
    - DUDTAP
  citations:
    - file: delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
title: Delta-Iceberg Unsupported Data Types and Properties
description: The set of data types and Apache Iceberg table properties that IcebergWriterCompatV rejects, ensuring only Iceberg-compatible schema types and table configurations are used in Delta tables.
tags:
  - delta-lake
  - apache-iceberg
  - data-types
  - table-properties
timestamp: "2026-06-18T15:21:27.407Z"
---

# Delta-Iceberg Unsupported Data Types and Properties

**Delta-Iceberg Unsupported Data Types and Properties** refers to specific error conditions that occur when a [Delta Lake Table](/concepts/delta-lake-table.md) configured with IcebergWriterCompatV compatibility contains schema elements, table features, or properties that are incompatible with the Apache Iceberg specification.

## Overview

When using IcebergWriterCompatV`<version>`, Delta Lake enforces compatibility constraints to ensure tables can be correctly read by Apache Iceberg readers. Violations of these constraints result in `DELTA_ICEBERG_WRITER_COMPAT_VIOLATION` errors with a SQLSTATE of KD00E. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Unsupported Data Types

### UNSUPPORTED_DATA_TYPE

The `UNSUPPORTED_DATA_TYPE` error occurs when a table schema contains a data type that is not supported by the specified IcebergWriterCompatV version. The error message includes both the unsupported data type and the full schema for debugging purposes. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

To resolve this error, modify the schema to use data types that are compatible with Apache Iceberg. The specific unsupported data types depend on the IcebergWriterCompatV version in use.

### CANNOT_CHANGE_MAP_STRUCT_KEY

This error occurs when a transaction attempts to change map keys that are structs. IcebergWriterCompatV disallows modifying struct-typed keys in map columns. The error message lists the affected map column names. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Unsupported Properties

### UNSUPPORTED_ICEBERG_TABLE_PROPERTY

This error occurs when a table is configured with an Apache Iceberg table property that is not supported by the current IcebergWriterCompatV version. The error message identifies the unsupported property key. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

To fix this, remove or replace the unsupported table property with one that is compatible.

### WRONG_REQUIRED_TABLE_PROPERTY

Occurs when a required table property is set to an incorrect value. The error message specifies the property key, the required value, and the current value. Update the property to match the required value to resolve this error. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Configuration and Feature Errors

### CONFIG_NOT_ENABLED

Occurs when a required configuration is not enabled for the table. The error message specifies which config needs to be enabled to satisfy IcebergWriterCompatV requirements. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### DISABLING_REQUIRED_TABLE_FEATURE

Occurs when attempting to drop a table feature that is required by IcebergWriterCompatV. The required feature cannot be removed from the table as long as compatibility is enforced. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### INCOMPATIBLE_TABLE_FEATURE

Occurs when the table has a feature enabled that is incompatible with the current IcebergWriterCompatV version. Disable or remove the incompatible feature to resolve this error. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### MISSING_REQUIRED_TABLE_FEATURE

Occurs when a required table feature is not supported or enabled. Enable the specified feature to satisfy IcebergWriterCompatV requirements. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Column Mapping Errors

### FIELD_ID_DOES_NOT_MATCH_PHYSICAL_NAME

Occurs when column mapping field physical names do not follow the required format `col-[fieldId]`. The error message lists the affected field names and their current physical names. Update the physical names to match the required pattern to resolve this error. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake and Apache Iceberg Compatibility](/concepts/delta-lake-table-features-and-iceberg-compatibility.md)
- [IcebergWriterCompatV](/concepts/icebergwritercompatv.md)
- [Delta Lake Schema Evolution](/concepts/delta-lake-schema-migration.md)
- [Column mapping in Delta Lake](/concepts/column-mapping-in-delta-lake.md)
- Apache Iceberg Specification
- Delta Lake Table Features

## Sources

- delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws-02e8eab9.md)
