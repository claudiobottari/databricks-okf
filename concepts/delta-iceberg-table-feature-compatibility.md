---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8fbf6df6b3d5c2177798351b66f29096760752b5512263608f17501f915238a0
  pageDirectory: concepts
  sources:
    - delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-iceberg-table-feature-compatibility
    - DTFC
    - Delta Iceberg Compatibility
    - Delta-Iceberg Compatibility
  citations:
    - file: delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
title: Delta-Iceberg Table Feature Compatibility
description: Constraints enforced by IcebergWriterCompatV requiring specific table features to be enabled or disabled, and preventing incompatible features from coexisting on a Delta table intended for Iceberg compatibility.
tags:
  - delta-lake
  - apache-iceberg
  - table-features
  - compatibility
timestamp: "2026-06-18T15:21:11.187Z"
---

# Delta-Iceberg Table Feature Compatibility

**Delta-Iceberg Table Feature Compatibility** refers to the set of constraints enforced by the `DELTA_ICEBERG_WRITER_COMPAT_VIOLATION` error class in Databricks. This error class is raised when a write operation to a Delta table violates the requirements of the Iceberg writer compatibility version (`IcebergWriterCompatV<version>`) configured on the table. The compatibility version ensures that Delta tables written with the specified constraints can be read natively by Apache Iceberg readers without data loss or semantic mismatch.

^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Error Overview

The full error class appears as:

```
DELTA_ICEBERG_WRITER_COMPAT_VIOLATION
```

It is associated with SQLSTATE `KD00E`, which falls under the `KD` class for datasource-specific errors.

^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

The validation is invoked when a Delta table has an `IcebergWriterCompatV` property set (e.g., `delta.icebergWriterCompatV`). The table’s schema, column mapping, table properties, and enabled table features must all conform to the rules required by that version. Any write operation that violates these rules triggers one of the specific sub‑error conditions listed below.

## Sub‑Error Conditions

All sub‑errors are children of the `DELTA_ICEBERG_WRITER_COMPAT_VIOLATION` error class. Each describes a particular kind of incompatibility.

### CANNOT_CHANGE_MAP_STRUCT_KEY

This error occurs when a transaction attempts to change the key type of a map column while the key is a struct type. IcebergWriterCompatV disallows changing map keys that are structs. The error message lists the names of the affected map columns (`<map_names>`).

^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### CONFIG_NOT_ENABLED

The compatibility version requires a specific Delta configuration key (`<config>`) to be enabled. If that configuration is not set, the write operation is rejected.

^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### DISABLING_REQUIRED_TABLE_FEATURE

IcebergWriterCompatV requires a particular Delta table feature (e.g., `changeDataFeed`, `columnMapping`) to be supported and enabled on the table. Attempting to drop that feature from the table (by removing the table property that controls it) raises this error.

^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### FIELD_ID_DOES_NOT_MATCH_PHYSICAL_NAME

When [Delta column mapping](/concepts/delta-table-column-mapping.md) is enabled, Iceberg compatibility requires that physical column names follow the pattern `col-<fieldId>`. If any field’s physical name does not match that pattern, this error is raised. The message lists the field names and their current physical names.

^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### INCOMPATIBLE_TABLE_FEATURE

This error indicates that a feature enabled on the table is fundamentally incompatible with the configured IcebergWriterCompatV version. The incompatible feature name is provided in the message.

^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### MISSING_REQUIRED_TABLE_FEATURE

IcebergWriterCompatV requires a specific table feature (`<feature>`) to be supported and enabled, but that feature is missing. This is similar to `DISABLING_REQUIRED_TABLE_FEATURE` but occurs when the feature was never present or was already dropped, not when a drop is attempted.

^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### UNSUPPORTED_DATA_TYPE

The schema contains a data type that is not supported by the Iceberg compatibility version. The error shows the unsupported data type and the full schema that triggered the violation.

^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### UNSUPPORTED_ICEBERG_TABLE_PROPERTY

The table has an Apache Iceberg table property (a property prefixed with `iceberg.`) that the compatibility version does not support. The property key is provided in the message.

^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### WRONG_REQUIRED_TABLE_PROPERTY

IcebergWriterCompatV requires a specific table property (`<key>`) to be set to a specific value (`<requiredValue>`), but the actual value (`<actualValue>`) differs.

^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Resolving Violations

Each sub‑error points to the exact constraint that must be satisfied. Common remediation steps include:

- Enabling the required Delta configurations or table features.
- Adjusting column mapping physical names to the `col-<fieldId>` format.
- Removing unsupported data types or table properties.
- Setting the required table property to the expected value.
- Avoiding schema changes that alter map struct keys.

For a full reference on Iceberg writer compatibility versions, see [Delta Lake and Iceberg integration](https://docs.delta.io/latest/delta-iceberg.html) (external to Databricks).

## Related Concepts

- [Delta Lake table features](/concepts/delta-lake-reader-table-features.md) – The `delta.feature.*` properties that control table capabilities.
- [Column mapping in Delta Lake](/concepts/column-mapping-in-delta-lake.md) – Physical column naming required for Iceberg compatibility.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – The open table format that Delta tables are being made compatible with.
- Delta table properties – Configuration keys such as `delta.icebergWriterCompatV`.
- DELTA_ICEBERG_WRITER_COMPAT_VIOLATION|error class DELTA_ICEBERG_WRITER_COMPAT_VIOLATION – Detailed Databricks error documentation.

## Sources

- delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws-02e8eab9.md)
