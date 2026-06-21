---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4868bc86476427f2d08c7eb192e52c3e55ac541792fa91ddef0e90d6dcdc5562
  pageDirectory: concepts
  sources:
    - delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - kd00e-sqlstate
  citations:
    - file: delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
title: KD00E SQLSTATE
description: A Databricks-specific SQLSTATE code (KD00E) under the KD class for datasource-specific errors, used by the DELTA_ICEBERG_WRITER_COMPAT_VIOLATION error condition.
tags:
  - sqlstate
  - error-handling
  - databricks
timestamp: "2026-06-19T18:25:52.599Z"
---

# KD00E SQLSTATE

**KD00E** is a SQLSTATE class code in the KD range (Datasource-Specific Errors) that indicates a validation failure of the IcebergWriterCompatV`<version>` specification. This error occurs when an operation on a Delta table violates the compatibility requirements imposed by the Iceberg-compatible writer version configured for that table. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Overview

The KD00E SQLSTATE covers a family of specific error conditions related to [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) write compatibility validation. When a Delta table has IcebergWriterCompatV`<version>` enabled, certain schema changes, table features, configurations, and data types are restricted to ensure the table can be read correctly by Iceberg readers. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Error Sub-Conditions

Each sub-condition of KD00E describes a specific violation:

### CANNOT_CHANGE_MAP_STRUCT_KEY

IcebergWriterCompatV`<version>` disallows changing map keys that are structs. This error is raised when a transaction attempts to modify the key of a map whose key type is a struct. The error message includes the names of the affected maps. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### CONFIG_NOT_ENABLED

IcebergWriterCompatV`<version>` requires a specific configuration parameter (`<config>`) to be enabled. This error occurs when that required configuration is not set in the table properties. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### DISABLING_REQUIRED_TABLE_FEATURE

IcebergWriterCompatV`<version>` requires a particular table feature (`<feature>`) to be supported and enabled. This error is raised when an attempt is made to drop or disable that required feature from the table. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### FIELD_ID_DOES_NOT_MATCH_PHYSICAL_NAME

IcebergWriterCompatV`<version>` requires column mapping field physical names to follow the pattern `col-<fieldId>`. This error occurs when one or more fields have physical names that do not match this required convention. The error message lists the offending field names and their actual physical names. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### INCOMPATIBLE_TABLE_FEATURE

IcebergWriterCompatV`<version>` is incompatible with certain table features. This error is raised when a table has a feature (`<feature>`) enabled that conflicts with the Iceberg compatibility requirements. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### MISSING_REQUIRED_TABLE_FEATURE

IcebergWriterCompatV`<version>` requires a specific table feature (`<feature>`) to be supported and enabled. This error occurs when that required feature is not present on the table. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### UNSUPPORTED_DATA_TYPE

IcebergWriterCompatV`<version>` does not support certain data types. This error is raised when the table schema contains a data type (`<dataType>`) that is not supported. The error message includes the full schema for reference. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### UNSUPPORTED_ICEBERG_TABLE_PROPERTY

IcebergWriterCompatV`<version>` does not support a specific Apache Iceberg table property. This error occurs when a table has an Iceberg table property (`<key>`) that is incompatible with the specified compatibility version. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### WRONG_REQUIRED_TABLE_PROPERTY

IcebergWriterCompatV`<version>` requires a specific table property to be set to a particular value. This error is raised when the table property (`<key>`) is set to a value (`<actualValue>`) that differs from the required value (`<requiredValue>`). ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- SQLSTATE — The standard SQL error code system used by Databricks
- KD Class Datasource-Specific Errors — The broader error class containing KD00E
- [Delta Lake Iceberg Compatibility](/concepts/delta-lake-table-features-and-iceberg-compatibility.md) — The feature enabling Iceberg read compatibility for Delta tables
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The open table format that Delta tables can be made compatible with
- Delta Table Features — Table capabilities that may conflict with Iceberg compatibility
- [Column mapping in Delta Lake](/concepts/column-mapping-in-delta-lake.md) — The feature affected by the FIELD_ID_DOES_NOT_MATCH_PHYSICAL_NAME error

## Sources

- delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws-02e8eab9.md)
