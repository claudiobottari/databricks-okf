---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a44b2be4119b9a4da940bd35c8d2c521c473048a4c0f966db3ce5cf438f46612
  pageDirectory: concepts
  sources:
    - delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - delta-lake-table-features-and-iceberg-compatibility
    - Iceberg compatibility and Delta Lake table features
    - DLTFAIC
    - Apache Iceberg compatibility in Delta Lake
    - Delta Lake Iceberg Compatibility
    - Delta Lake and Apache Iceberg Compatibility
    - Delta Lake and Iceberg interoperability
    - Delta Lake to Iceberg compatibility
    - Delta Lake-Iceberg Compatibility
    - Delta Lake-Iceberg interoperability
    - Delta table Iceberg compatibility
    - Iceberg and Delta Lake interoperability
  citations:
    - file: delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
title: Delta Lake table features and Iceberg compatibility
description: IcebergWriterCompatV requires specific Delta Lake table features to be enabled and supported, and is incompatible with certain features
tags:
  - table-features
  - delta-lake
  - compatibility
timestamp: "2026-06-18T11:54:52.767Z"
---

# [Delta Lake Table](/concepts/delta-lake-table.md) features and Iceberg compatibility

**Delta Lake table features** are optional capabilities that can be enabled on a Delta table. They enable incremental new functionality, such as support for specific writer protocols. **Iceberg compatibility** refers to Delta Lake’s ability to produce data that can be read by [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) readers. This is governed by the `IcebergWriterCompatV` table feature, which enforces a set of constraints on the table layout, schema, and properties. Violating those constraints produces the `DELTA_ICEBERG_WRITER_COMPAT_VIOLATION` error. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## The IcebergWriterCompatV table feature

`IcebergWriterCompatV` (with a version number) is a Delta table feature that, when enabled, requires the table to conform to rules that make its underlying Parquet files compatible with Iceberg readers. The version indicates the specific set of rules. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Compatibility constraints enforced by the feature

The following table lists the constraints that `IcebergWriterCompatV<version>` imposes. If a table transaction violates any of them, the `DELTA_ICEBERG_WRITER_COMPAT_VIOLATION` error is raised with one of the sub‑error codes shown. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

| Sub‑error code | Condition violated | Description |
|----------------|-------------------|-------------|
| `CANNOT_CHANGE_MAP_STRUCT_KEY` | Changing struct‑typed map keys | The feature disallows altering the key type of a map if the key is a struct. |
| `CONFIG_NOT_ENABLED` | Missing required configuration | A specific Delta‑level config must be enabled. |
| `DISABLING_REQUIRED_TABLE_FEATURE` | Dropping a required feature | The table feature required by `IcebergWriterCompatV` cannot be removed. |
| `FIELD_ID_DOES_NOT_MATCH_PHYSICAL_NAME` | Column‑mapping physical names | Column mapping must use physical names equal to `col-[fieldId]`. |
| `INCOMPATIBLE_TABLE_FEATURE` | Incompatible feature present | Another enabled table feature conflicts with `IcebergWriterCompatV`. |
| `MISSING_REQUIRED_TABLE_FEATURE` | Missing required feature | A prerequisite table feature is not enabled. |
| `UNSUPPORTED_DATA_TYPE` | Data type not supported | The table schema contains a data type that Iceberg does not support. |
| `UNSUPPORTED_ICEBERG_TABLE_PROPERTY` | Unsupported Iceberg property | A table property set on the Delta table is not recognized by Iceberg. |
| `WRONG_REQUIRED_TABLE_PROPERTY` | Incorrect required property | A required table property has a value that does not match the expected value. |

## Key requirements

- **Column mapping physical names**: When `IcebergWriterCompatV` is enabled, column mapping must follow the Iceberg convention: physical names must equal `col-<fieldId>`. Any deviation triggers `FIELD_ID_DOES_NOT_MATCH_PHYSICAL_NAME`. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]
- **Data type support**: The feature does not support all Delta data types. Including an unsupported type (e.g., certain nested or complex types) raises `UNSUPPORTED_DATA_TYPE`, which includes the offending schema for debugging. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]
- **Required table properties**: For a given version, specific table properties must be set to exact values. For example, `delta.columnMapping.mode` might need a particular setting (`WRONG_REQUIRED_TABLE_PROPERTY`). ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]
- **Supported and unsupported table features**: `IcebergWriterCompatV` requires some features (like [column mapping](/concepts/column-mapping-in-delta-lake.md) or [Deletion Vectors](/concepts/deletion-vectors.md)) to be already enabled (`MISSING_REQUIRED_TABLE_FEATURE`), and forbids others (`INCOMPATIBLE_TABLE_FEATURE`). It also prevents the removal of any feature it depends on (`DISABLING_REQUIRED_TABLE_FEATURE`). ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]
- **Map key restrictions**: Changing struct keys of map columns is forbidden (`CANNOT_CHANGE_MAP_STRUCT_KEY`). ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]
- **Iceberg table properties**: The feature rejects any Delta table property that is not supported by Apache Iceberg (`UNSUPPORTED_ICEBERG_TABLE_PROPERTY`). ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Enabling IcebergWriterCompatV

To enable the feature, you typically set the table property `delta.enableIcebergWriterCompatV` to `true` (or the appropriate version). The exact property name and version may vary; the error `CONFIG_NOT_ENABLED` indicates that the required config has not been turned on. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Related concepts

- [Delta Lake table features](/concepts/delta-lake-reader-table-features.md) – The general mechanism for optional capabilities.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – The open table format that Delta aims to be compatible with.
- [Column mapping](/concepts/column-mapping-in-delta-lake.md) – A Delta feature that is often required for Iceberg compatibility.
- Delta table properties – Configuration keys that control table behaviour.
- DELTA_ICEBERG_WRITER_COMPAT_VIOLATION – The error class raised when constraints are violated.

## Sources

- delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws-02e8eab9.md)
