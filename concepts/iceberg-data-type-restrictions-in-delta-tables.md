---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a35c098cfee590ecf883fcfbd0d37d8bf8f305bc9ac1bec64954d0bcb62db0e7
  pageDirectory: concepts
  sources:
    - delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - iceberg-data-type-restrictions-in-delta-tables
    - IDTRIDT
  citations:
    - file: delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
title: Iceberg data type restrictions in Delta tables
description: The constraint that IcebergWriterCompatV rejects Delta schemas containing data types not supported by Apache Iceberg
tags:
  - databricks
  - delta-lake
  - iceberg
  - data-types
timestamp: "2026-06-19T10:07:02.061Z"
---

# Iceberg Data Type Restrictions in Delta Tables

**Iceberg data type restrictions in Delta tables** refer to the constraints enforced by the `IcebergWriterCompatV`<version>` compatibility mode when [Delta tables](/concepts/delta-lake-table.md) are written in a format compatible with [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md). These restrictions ensure that Delta table schemas and features align with Iceberg’s requirements, preventing writes or schema changes that would produce incompatible data.

## Overview

When a Delta table is configured with `IcebergWriterCompatV`<version>`, the writer validates that every transaction — schema evolution, property changes, and data writes — complies with Iceberg’s data type and feature model. If validation fails, a `DELTA_ICEBERG_WRITER_COMPAT_VIOLATION` error (SQLSTATE: KD00E) is raised. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

The restrictions cover unsupported data types, incompatible table features, required table properties, column mapping conventions, and structural rules for complex types like maps.

## Specific Restrictions

### Unsupported Data Types

`UNSUPPORTED_DATA_TYPE` occurs when the schema contains a data type that IcebergWriterCompatV<version> does not support. The full schema is reported in the error message. To resolve, replace the unsupported type with an Iceberg-compatible alternative. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### Struct Keys in Maps

`CANNOT_CHANGE_MAP_STRUCT_KEY` prevents using structs as map keys. Iceberg requires map keys to be primitive types; any transaction that introduces or modifies a map with a struct key is rejected. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### Column Mapping Field Names

`FIELD_ID_DOES_NOT_MATCH_PHYSICAL_NAME` enforces that column mapping physical names must follow the pattern `col-[fieldId]`. If a Delta table uses a different physical naming convention, changes are blocked. This ensures interoperability with Iceberg’s field ID system. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### Required Table Features and Properties

- **`MISSING_REQUIRED_TABLE_FEATURE`** and **`DISABLING_REQUIRED_TABLE_FEATURE`** indicate that a Delta table feature is either missing or being dropped, but Iceberg compatibility requires it to be present. Examples include `columnMapping`, `deletionVectors`, or `changeDataFeed`. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]
- **`WRONG_REQUIRED_TABLE_PROPERTY`** occurs when a Delta table property must be set to a specific value for Iceberg compatibility (e.g., `delta.columnMapping.mode = 'name'`), but it is set to a different value. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]
- **`CONFIG_NOT_ENABLED`** appears when a required configuration (e.g., `spark.databricks.delta.icebergWriters.compatible.enabled`) is not enabled. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### Incompatible Table Features

`INCOMPATIBLE_TABLE_FEATURE` is raised when a Delta table feature (such as `generationExpression` or `checkConstraints`) is incompatible with the Iceberg writer compatibility version. The feature must be removed or the compatibility level adjusted. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### Unsupported Iceberg Table Properties

`UNSUPPORTED_ICEBERG_TABLE_PROPERTY` prevents setting an Apache Iceberg table property that is not recognized or supported by the current Delta writer compatibility version. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Error Class and Sub‑errors

All violations share the error class `DELTA_ICEBERG_WRITER_COMPAT_VIOLATION`. The sub‑error messages listed above identify the specific cause. Each sub‑error includes placeholders that are replaced with context‑specific values at runtime. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Resolving Violations

To resolve a restriction:

1. Identify the sub‑error and its details from the error message.
2. Modify the Delta table schema, properties, or configuration to satisfy Iceberg compatibility requirements.
3. Disable `IcebergWriterCompatV<version>` if Iceberg compatibility is not needed.

For example, to fix `UNSUPPORTED_DATA_TYPE`, change the offending column’s type to a supported Iceberg type (such as `TIMESTAMP` instead of `TIMESTAMP_NTZ`, or `STRUCT` with only primitive fields). For `CANNOT_CHANGE_MAP_STRUCT_KEY`, restructure the schema to use primitive map keys. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta table Iceberg compatibility](/concepts/delta-lake-table-features-and-iceberg-compatibility.md) – Overview of the compatibility mode and its configuration.
- [Delta Table Column Mapping](/concepts/delta-table-column-mapping.md) – Requires specific physical naming for Iceberg writes.
- Supported Iceberg data types – Reference of types accepted by Iceberg.
- Delta table features – List of features that may conflict with Iceberg.
- Apache Iceberg specification – Full data type and schema requirements.

## Sources

- delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws-02e8eab9.md)
