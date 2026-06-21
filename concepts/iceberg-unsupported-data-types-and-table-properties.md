---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7f99d1461360d943a59192a2164eeb980a3b1a7edd053a3793f3367354ead09d
  pageDirectory: concepts
  sources:
    - delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - iceberg-unsupported-data-types-and-table-properties
    - table properties and Iceberg unsupported data types
    - IUDTATP
    - Iceberg-unsupported data types
  citations:
    - file: delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
title: Iceberg unsupported data types and table properties
description: IcebergWriterCompatV restricts which data types and Iceberg table properties are allowed in the Delta table schema and configuration
tags:
  - data-types
  - table-properties
  - schema-validation
timestamp: "2026-06-18T11:54:45.507Z"
---

---
title: Iceberg Unsupported Data Types and Table Properties
summary: A description of the compatibility requirements enforced by IcebergWriterCompatV, covering the `UNSUPPORTED_DATA_TYPE` and `UNSUPPORTED_ICEBERG_TABLE_PROPERTY` error conditions.
sources:
  - delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-22T15:30:00.000Z"
updatedAt: "2026-06-22T15:30:00.000Z"
tags:
  - apache-iceberg
  - compatibility
  - errors
  - delta-lake
aliases:
  - iceberg-unsupported-data-types-and-table-properties
  - IUDTATP
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Iceberg Unsupported Data Types and Table Properties

**IcebergWriterCompatV** is a validation layer in Delta Lake that enforces compatibility rules when a Delta table is written in a mode that targets [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) readers. When a schema or table-level configuration violates one of these rules, the system raises a `DELTA_ICEBERG_WRITER_COMPAT_VIOLATION` error (SQLSTATE `KD00E`). Two specific sub-conditions — `UNSUPPORTED_DATA_TYPE` and `UNSUPPORTED_ICEBERG_TABLE_PROPERTY` — cover cases where the table's schema or table properties are incompatible with the targeted Iceberg version. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## UNSUPPORTED_DATA_TYPE

IcebergWriterCompatV`<version>` does not support the data type `<dataType>` in your schema. An error of this type is raised when one or more columns in the Delta table use a data type that the targeted Iceberg specification version does not recognize. The full schema that triggered the conflict is included in the error message as `<schema>`. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### Common Triggers

- VoidType|VoidType columns not representable in Iceberg.
- MapType|Map types whose key is itself a struct (separately reported as `CANNOT_CHANGE_MAP_STRUCT_KEY`).
- Any Spark SQL data type that lacks a direct Iceberg analog in the targeted version.

To resolve, remove or remap the unsupported column type before writing, or use an Iceberg-compatible schema that maps every Delta column type to an Iceberg equivalent.

## UNSUPPORTED_ICEBERG_TABLE_PROPERTY

IcebergWriterCompatV`<version>` does not support Apache Iceberg table property '`<key>`'. This error is raised when the Delta table carries a table property that Iceberg does not recognize or whose value is outside the allowed set for the targeted Iceberg version. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### Common Triggers

- Proprietary [Delta Lake table properties](/concepts/delta-lake-reader-table-features.md) (for example, `delta.enableChangeDataFeed`, `delta.minReaderVersion`) that have no Iceberg counterpart.
- Iceberg table properties with values outside the version's specification.
- A table property that conflicts with an IcebergWriterCompatV requirement (for example, setting a property that is already required to be a specific value by `WRONG_REQUIRED_TABLE_PROPERTY`).

To resolve, remove or alter the unsupported property. Review the Apache Iceberg table property specification for the version you are targeting.

## Related Error Conditions

IcebergWriterCompatV validation includes several other checks that may surface alongside or instead of the unsupported-type and unsupported-property errors:

| Error Sub-Condition | Description |
|---|---|
| `CANNOT_CHANGE_MAP_STRUCT_KEY` | Disallows changing map keys that are structs |
| `CONFIG_NOT_ENABLED` | A required configuration is not enabled |
| `DISABLING_REQUIRED_TABLE_FEATURE` | An attempt to drop a feature that IcebergWriterCompatV requires |
| `FIELD_ID_DOES_NOT_MATCH_PHYSICAL_NAME` | Column mapping physical names must follow the `col-[fieldId]` convention |
| `INCOMPATIBLE_TABLE_FEATURE` | A table feature conflicts with the targeted Iceberg version |
| `MISSING_REQUIRED_TABLE_FEATURE` | A required table feature is not enabled |
| `WRONG_REQUIRED_TABLE_PROPERTY` | A table property must be set to a specific value |

## Best Practices

- Before enabling IcebergWriterCompatV on a Delta table, audit the schema for [Iceberg-unsupported data types](/concepts/iceberg-unsupported-data-types-and-table-properties.md) and remove or remap them.
- Use `DESCRIBE DETAIL` to review the table's current properties and identify any that lack an Iceberg analog.
- Apply an explicit set of [Iceberg-compatible table properties](/concepts/icebergcompatv1-required-table-properties.md) at table creation time to avoid conflicts later.
- Test schema and property changes on a copy of the table before applying them to production data.

## Related Concepts

- [IcebergWriterCompatV](/concepts/icebergwritercompatv.md) — The Delta Lake compatibility layer for Iceberg readers
- Delta Lake to Iceberg Migration — General strategies for making Delta tables Iceberg-readable
- Delta Lake Table Features — Features that Iceberg compatibility may require or exclude
- Apache Iceberg Specification — The authoritative reference for supported types and properties
- [Column mapping in Delta Lake](/concepts/column-mapping-in-delta-lake.md) — How column mapping physical names interact with Iceberg requirements

## Sources

- delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws-02e8eab9.md)
