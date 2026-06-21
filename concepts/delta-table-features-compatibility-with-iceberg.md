---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e92c0f1c23b8f6ee623550cc7565b38f762547537be8bd6f5155c06bec13c9c7
  pageDirectory: concepts
  sources:
    - delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
  confidence: 0.92
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-table-features-compatibility-with-iceberg
    - DTFCWI
    - Delta Lake compatibility with Iceberg
  citations:
    - file: delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
    - file: delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
      start: 9
      end: 10
    - file: delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
      start: 12
      end: 13
    - file: delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
      start: 15
      end: 16
    - file: delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
      start: 25
      end: 26
    - file: delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
      start: 18
      end: 20
    - file: delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
      start: 22
      end: 23
    - file: delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
      start: 28
      end: 31
    - file: delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
      start: 33
      end: 34
    - file: delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
      start: 36
      end: 38
title: Delta table features compatibility with Iceberg
description: Constraints enforced by IcebergWriterCompatV that require specific Delta table features to be enabled and prohibit incompatible features
tags:
  - databricks
  - delta-lake
  - iceberg
  - table-features
timestamp: "2026-06-19T10:07:07.168Z"
---

# Delta Table Features Compatibility with Iceberg

**Delta Table Features Compatibility with Iceberg** refers to the set of constraints that [Delta tables](/concepts/delta-lake-table.md) must satisfy when written with an Iceberg-compatible writer mode (`IcebergWriterCompatV`). These constraints ensure the Delta table can be read by [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) readers. Violating any constraint raises the `DELTA_ICEBERG_WRITER_COMPAT_VIOLATION` error. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Overview

The `IcebergWriterCompatV` protocol imposes restrictions on Delta table schema, table features, configurations, and properties. The version number (`V<version>`) indicates which set of compatibility rules apply. When a write operation violates a rule, Databricks returns the error with a specific sub‑reason. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Constraint Categories

### Map Key Type Restrictions

`IcebergWriterCompatV` disallows changing map keys that are structs. Iceberg does not support struct keys in maps, so any transaction that alters the key type of a `MapType` column where the key is a struct triggers this error. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md#L9-L10]

### Required Spark Configuration

A specific Spark configuration must be enabled for the compatibility mode. The error message identifies which configuration (`<config>`) is missing. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md#L12-L13]

### Required Table Features

`IcebergWriterCompatV` requires certain Delta table features to be both supported and enabled. Attempting to **disable** a required feature (e.g., column mapping, deletion vectors) or finding it **missing** from the table will raise the error. The error names the feature (`<feature>`) and, in the disabling case, confirms it cannot be dropped. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md#L15-L16] ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md#L25-L26]

### Column Mapping Physical Names

When column mapping is enabled, physical column names must follow the pattern `col-[fieldId]`. If any field deviates from this pattern, the error lists the field names and their current physical names. This mapping ensures Iceberg can correctly identify columns. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md#L18-L20]

### Incompatible Table Features

Some Delta table features are fundamentally incompatible with `IcebergWriterCompatV`. If such a feature (`<feature>`) is enabled on the table, the write operation fails. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md#L22-L23]

### Unsupported Data Types

The compatibility mode restricts the table schema to data types that Iceberg supports. If a column uses an unsupported type (`<dataType>`), the error shows the full schema. Examples of unsupported types include `MapType` with non‑string keys or `VoidType`. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md#L28-L31]

### Unsupported Iceberg Table Properties

Any Delta table property that is not recognized by Apache Iceberg will cause the verification to fail. The error identifies the offending property key (`<key>`). ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md#L33-L34]

### Wrong Required Table Property

Certain Delta table properties must be set to a specific value for Iceberg compatibility. For example, a property like `delta.enableDeletionVectors` might need to be `false`. The error reports the required value (`<requiredValue>`) and the current value (`<actualValue>`). ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md#L36-L38]

## Responding to the Error

When you encounter a `DELTA_ICEBERG_WRITER_COMPAT_VIOLATION`, examine the sub‑reason to identify which constraint is broken. Common fixes include:

- Changing Spark configs (e.g., `spark.databricks.delta.write.icebergWriterCompatV2Enabled`).
- Adding or enabling required table features (e.g., `delta.feature.columnMapping`).
- Adjusting column mapping physical names to match the `col-[fieldId]` format.
- Changing column data types to Iceberg‑supported equivalents.
- Removing unsupported table properties or setting properties to the required values.
- Disabling incompatible table features.

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md)
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md)
- [Column mapping](/concepts/column-mapping-in-delta-lake.md)
- Delta table features
- [IcebergWriterCompatV](/concepts/icebergwritercompatv.md)
- Table properties
- Error handling

## Sources

- delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws-02e8eab9.md)
2. [delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md:9-10](/references/delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws-02e8eab9.md)
3. [delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md:12-13](/references/delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws-02e8eab9.md)
4. [delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md:15-16](/references/delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws-02e8eab9.md)
5. [delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md:25-26](/references/delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws-02e8eab9.md)
6. [delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md:18-20](/references/delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws-02e8eab9.md)
7. [delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md:22-23](/references/delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws-02e8eab9.md)
8. [delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md:28-31](/references/delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws-02e8eab9.md)
9. [delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md:33-34](/references/delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws-02e8eab9.md)
10. [delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md:36-38](/references/delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws-02e8eab9.md)
