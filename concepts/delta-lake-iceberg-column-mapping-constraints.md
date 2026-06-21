---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 620f255e87947cf44b622a319df850ba8612ad84928db02064984a1d607ca293
  pageDirectory: concepts
  sources:
    - delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-iceberg-column-mapping-constraints
    - DLCMC
  citations:
    - file: delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
title: Delta Lake-Iceberg column mapping constraints
description: IcebergWriterCompatV requires column mapping physical names to follow the 'col-[fieldId]' convention, enforced via the FIELD_ID_DOES_NOT_MATCH_PHYSICAL_NAME condition
tags:
  - column-mapping
  - schema
  - compatibility
timestamp: "2026-06-18T11:54:26.623Z"
---

# Delta Lake-Iceberg Column Mapping Constraints

**Delta Lake-Iceberg column mapping constraints** are validation rules enforced when a Delta table is configured with `IcebergWriterCompatV<version>` settings. These constraints ensure that the table's schema and properties remain compatible with Apache Iceberg's column mapping requirements, enabling interoperability between [Delta Lake](/concepts/delta-lake.md) and [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md).

## Overview

When a Delta table has `IcebergWriterCompatV<version>` enabled, certain schema modifications and table configurations are restricted to maintain compatibility with Iceberg's column mapping conventions. Violations trigger a `DELTA_ICEBERG_WRITER_COMPAT_VIOLATION` error (SQLSTATE: KD00E) during write operations or schema evolution attempts. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Constraint Types

### CANNOT_CHANGE_MAP_STRUCT_KEY

This constraint prevents changing map keys that are structs. IcebergWriterCompatV`<version>` disallows transactions that alter the key type for maps containing struct keys. The error identifies the affected map column names. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### CONFIG_NOT_ENABLED

The table must have a required configuration parameter enabled. IcebergWriterCompatV`<version>` specifies which config must be active for the table to be Iceberg-compatible. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### DISABLING_REQUIRED_TABLE_FEATURE

A table feature required by IcebergWriterCompatV`<version>` cannot be dropped from the table. The constraint ensures that necessary features remain supported and enabled. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### FIELD_ID_DOES_NOT_MATCH_PHYSICAL_NAME

IcebergWriterCompatV`<version>` requires that column mapping field physical names follow the pattern `col-[fieldId]`. This constraint validates that all fields adhere to this naming convention. Fields that do not match are reported with their actual physical names. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### INCOMPATIBLE_TABLE_FEATURE

An existing table feature is incompatible with IcebergWriterCompatV`<version>`. The table cannot simultaneously enable the specified Iceberg compatibility version and the conflicting feature. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### MISSING_REQUIRED_TABLE_FEATURE

A table feature required by IcebergWriterCompatV`<version>` is not supported or enabled on the table. The constraint identifies which feature must be added. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### UNSUPPORTED_DATA_TYPE

IcebergWriterCompatV`<version>` does not support specific data types in the table's schema. When a schema contains an unsupported data type, the constraint reports the type and the full schema. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### UNSUPPORTED_ICEBERG_TABLE_PROPERTY

An Apache Iceberg table property set on the Delta table is not supported by IcebergWriterCompatV`<version>`. The error identifies the unsupported property key. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### WRONG_REQUIRED_TABLE_PROPERTY

A required table property must be set to a specific value. IcebergWriterCompatV`<version>` specifies both the property key and its required value. The error reports the current value alongside the required value. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Error Message Format

All constraint violations follow this pattern:

```
DELTA_ICEBERG_WRITER_COMPAT_VIOLATION.ERROR_TYPE: Description of the violation
```

Each constraint type has a distinct error code prefix (e.g., `CANNOT_CHANGE_MAP_STRUCT_KEY`, `CONFIG_NOT_ENABLED`) that identifies the specific validation failure. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Resolution

To resolve a `DELTA_ICEBERG_WRITER_COMPAT_VIOLATION` error:

1. **Identify the constraint type** from the error code prefix in the error message.
2. **Review the specific violation details** — the error message includes the affected fields, features, or property values.
3. **Adjust the table schema or configuration** to comply with IcebergWriterCompatV`<version>` requirements, such as:
   - Changing physical column names to match the `col-[fieldId]` pattern.
   - Enabling required table features or configuration parameters.
   - Removing incompatible table features or unsupported data types.
   - Removing unsupported Iceberg table properties.
   - Setting required table properties to the correct value.

## Related Concepts

- [IcebergWriterCompatV](/concepts/icebergwritercompatv.md) — The compatibility version setting that enforces these constraints
- [Delta Lake table features](/concepts/delta-lake-reader-table-features.md) — Features that may be required or incompatible
- [Column mapping in Delta Lake](/concepts/column-mapping-in-delta-lake.md) — The physical column naming conventions enforced by this constraint
- [Delta Lake-Iceberg interoperability](/concepts/delta-lake-table-features-and-iceberg-compatibility.md) — The broader framework for cross-format compatibility
- DELTA_ICEBERG_WRITER_COMPAT_VIOLATION — The error class for all constraint violations

## Sources

- delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws-02e8eab9.md)
