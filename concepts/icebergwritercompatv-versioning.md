---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2c75e302a8a02191fc74e7385d26a9f7137505bd7688e69cb081631224deed92
  pageDirectory: concepts
  sources:
    - delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - icebergwritercompatv-versioning
  citations:
    - file: delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
title: IcebergWriterCompatV versioning
description: A Databricks compatibility mechanism that enforces Delta table schemas and properties conform to Apache Iceberg writer expectations at a given version level
tags:
  - databricks
  - delta-lake
  - iceberg
  - compatibility
timestamp: "2026-06-19T10:06:42.936Z"
---

---
title: IcebergWriterCompatV Versioning
summary: The versioned validation framework that enforces Delta table writer compatibility with Apache Iceberg, with specific constraints per version.
sources:
  - delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:00:00.000Z"
updatedAt: "2026-06-19T10:00:00.000Z"
tags:
  - delta-lake
  - iceberg
  - compatibility
aliases:
  - iceberg-writer-compat-v-versioning
  - IWCVV
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# IcebergWriterCompatV Versioning

**IcebergWriterCompatV** is a versioned validation framework in [Delta Lake](/concepts/delta-lake.md) that enforces writer compatibility with [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md). Each version (e.g., `V2`, `V3`) defines a set of constraints that Delta table metadata and operations must satisfy to produce files readable by Iceberg clients. When a write operation violates the constraints of the active version, the `DELTA_ICEBERG_WRITER_COMPAT_VIOLATION` error is raised. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Version Rules

Each version of `IcebergWriterCompatV` enforces the following categories of rules. The error sub‑types below describe the specific violations that can occur.

### `CANNOT_CHANGE_MAP_STRUCT_KEY`
> IcebergWriterCompatV`<version>` disallows changing map keys that are structs. This transaction changes the key for maps: `<map_names>`. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### `CONFIG_NOT_ENABLED`
> IcebergWriterCompatV`<version>` requires the config `<config>` to be enabled. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### `DISABLING_REQUIRED_TABLE_FEATURE`
> IcebergWriterCompatV`<version>` requires feature `<feature>` to be supported and enabled. You cannot drop it from the table. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### `FIELD_ID_DOES_NOT_MATCH_PHYSICAL_NAME`
> IcebergWriterCompatV`<version>` requires column mapping field physical names be equal to 'col-\[fieldId\]', but this is not true for fields: `<field_names>`, physical names: `<physical_names>`. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### `INCOMPATIBLE_TABLE_FEATURE`
> IcebergWriterCompatV`<version>` is incompatible with feature `<feature>`. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### `MISSING_REQUIRED_TABLE_FEATURE`
> IcebergWriterCompatV`<version>` requires feature `<feature>` to be supported and enabled. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### `UNSUPPORTED_DATA_TYPE`
> IcebergWriterCompatV`<version>` does not support the data type `<dataType>` in your schema. Your schema:
> `<schema>` ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### `UNSUPPORTED_ICEBERG_TABLE_PROPERTY`
> IcebergWriterCompatV`<version>` does not support Apache Iceberg table property '`<key>`'. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### `WRONG_REQUIRED_TABLE_PROPERTY`
> IcebergWriterCompatV`<version>` requires table property '`<key>`' to be set to '`<requiredValue>`'. Current value: '`<actualValue>`'. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Usage

The active `IcebergWriterCompatV` version is controlled by a Delta table property (e.g., `delta.icebergWriterCompatVersion`). Setting this property to a specific version causes all subsequent write operations on the table to be validated against that version’s rules. If the operation violates any rule, the transaction is rejected with the appropriate sub‑error. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta-Iceberg Compatibility](/concepts/delta-iceberg-table-feature-compatibility.md) – The broader effort to enable reader and writer compatibility between Delta Lake and Apache Iceberg.
- Delta Table Features – The feature flags that must be enabled for Iceberg compatibility.
- [Column Mapping](/concepts/delta-table-column-mapping.md) – The mapping of logical column names to physical storage names, which is constrained by `FIELD_ID_DOES_NOT_MATCH_PHYSICAL_NAME`.
- [Apache Iceberg Table Properties](/concepts/icebergcompatv1-required-table-properties.md) – Iceberg‑specific properties that may conflict with Delta’s writer compatibility rules.

## Sources

- [delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md](https://docs.databricks.com/aws/en/error-messages/delta-iceberg-writer-compat-violation-error-class)

# Citations

1. [delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws-02e8eab9.md)
