---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c9788d477c4c196454f1bed6cfa3d344a0ecaca077ab76e334974e17bc725d25
  pageDirectory: concepts
  sources:
    - delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-iceberg-writer-compatibility-constraints
    - DWCC
  citations:
    - file: delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
title: Delta-Iceberg writer compatibility constraints
description: The set of specific schema and table property constraints enforced by IcebergWriterCompatV, including field naming, data types, table features, and configuration requirements.
tags:
  - delta-lake
  - iceberg
  - compatibility
  - constraints
timestamp: "2026-06-19T18:26:00.309Z"
---

```markdown
---
title: Delta-Iceberg Writer Compatibility Constraints
summary: The set of nine specific validation rules enforced by IcebergWriterCompatV, covering schema types, table features, configuration, column mapping, and table properties
sources:
  - delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-20T10:00:00.000Z"
updatedAt: "2026-06-20T10:00:00.000Z"
tags:
  - delta-lake
  - iceberg
  - compatibility
  - validation
aliases:
  - delta-iceberg-writer-compatibility-constraints
  - DWCC
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 3
---

# Delta-Iceberg Writer Compatibility Constraints

**Delta-Iceberg Writer Compatibility Constraints** are a set of validation rules enforced by Databricks to ensure that Delta Lake tables written with IcebergWriterCompatV`<version>` remain compatible with Apache Iceberg readers. These constraints prevent schema, configuration, and feature mismatches that would break interoperability. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Overview

When a Delta table is configured with the IcebergWriterCompatV setting, write operations are validated against a defined set of compatibility rules. If a transaction violates any of these rules, the system raises a `DELTA_ICEBERG_WRITER_COMPAT_VIOLATION` error with SQLSTATE `KD00E`, which falls under the datasource-specific error class `KD`. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

Each error sub-type includes the version identifier of the IcebergWriterCompatV constraint being applied.

## Error Sub-Types

### CANNOT_CHANGE_MAP_STRUCT_KEY

IcebergWriterCompatV`<version>` disallows changing map keys that are structs. This error occurs when a transaction attempts to modify the key type for maps — the error message lists the affected map names. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### CONFIG_NOT_ENABLED

IcebergWriterCompatV`<version>` requires a specific configuration parameter `<config>` to be enabled on the table. If the required config is not set, this error is raised. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### DISABLING_REQUIRED_TABLE_FEATURE

IcebergWriterCompatV`<version>` requires a particular table feature `<feature>` to be both supported and enabled. This error occurs when an attempt is made to drop that feature from the table. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### FIELD_ID_DOES_NOT_MATCH_PHYSICAL_NAME

IcebergWriterCompatV`<version>` requires that column mapping field physical names follow the pattern `col-[fieldId]`. This error is raised when one or more fields deviate from that naming convention — the error message provides the field names and their actual physical names. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### INCOMPATIBLE_TABLE_FEATURE

IcebergWriterCompatV`<version>` is incompatible with a particular table feature `<feature>`. If a table has that feature enabled, this error prevents the write operation. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### MISSING_REQUIRED_TABLE_FEATURE

IcebergWriterCompatV`<version>` requires a specific table feature `<feature>` to be supported and enabled. If that feature is missing from the table, this error is raised. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### UNSUPPORTED_DATA_TYPE

IcebergWriterCompatV`<version>` does not support a particular data type `<dataType>` present in the table schema. The error message includes the full schema for context. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### UNSUPPORTED_ICEBERG_TABLE_PROPERTY

IcebergWriterCompatV`<version>` does not support a specific Apache Iceberg table property `<key>`. This error is raised when an unsupported Iceberg property is set on the table. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### WRONG_REQUIRED_TABLE_PROPERTY

IcebergWriterCompatV`<version>` requires a table property `<key>` to be set to a specific required value `<requiredValue>`. This error is raised when the property currently has a different value `<actualValue>`. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [[Delta Lake]] — The underlying storage format enabling Iceberg compatibility
- [[Uniform (Apache Iceberg) Format|Apache Iceberg]] — The open table format that Delta tables target for interoperability
- [[Delta-Iceberg Table Feature Compatibility|Delta-Iceberg Compatibility]] — The broader framework for cross-format interoperability
- [[Column Mapping in Delta Lake]] — The feature governing physical-to-logical column name mapping
- Delta Table Features — The feature flags that control Delta Lake capabilities
- Delta Lake Table Properties — Configuration options for Delta tables

## Sources

- delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
```

# Citations

1. [delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws-02e8eab9.md)
