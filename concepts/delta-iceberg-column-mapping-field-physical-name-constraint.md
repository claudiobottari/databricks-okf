---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ef8671fb6231101371b272862b493deeb114363a18b21b8d026cbf0bcf1a2cb9
  pageDirectory: concepts
  sources:
    - delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-iceberg-column-mapping-field-physical-name-constraint
    - DCMFPNC
  citations:
    - file: delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
title: Delta-Iceberg Column Mapping Field Physical Name Constraint
description: A requirement of IcebergWriterCompatV that column mapping field physical names must follow the pattern 'col-[fieldId]' for Iceberg-compatible Delta writes.
tags:
  - delta-lake
  - apache-iceberg
  - column-mapping
  - schema
timestamp: "2026-06-18T15:20:46.114Z"
---



# Delta-Iceberg Column Mapping Field Physical Name Constraint

## Overview

The **Delta-Iceberg Column Mapping Field Physical Name Constraint** is a validation rule enforced by Delta Lake's IcebergWriterCompatV protocol that requires column mapping field physical names to follow a specific pattern. When this constraint is violated, Delta Lake returns the `FIELD_ID_DOES_NOT_MATCH_PHYSICAL_NAME` error. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Error Condition

This error belongs to the `DELTA_ICEBERG_WRITER_COMPAT_VIOLATION` error class with SQLSTATE `KD00E`. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

### Error Message

```
IcebergWriterCompatV<version> requires column mapping field physical names be equal to 'col-[fieldId]', but this is not true for fields: <field_names>, physical names: <physical_names>.
```

^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Requirement

The IcebergWriterCompatV protocol mandates that column mapping field physical names must follow the naming convention `col-[fieldId]`, where `fieldId` is the assigned field identifier. This ensures compatibility with Apache Iceberg's column mapping system, which uses a predictable naming scheme based on field IDs. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Common Causes

The constraint is violated when Delta tables have column mapping physical names that do not match the expected `col-[fieldId]` pattern. This typically occurs when:

- Existing tables have Delta-Iceberg column mapping configured with custom or non-standard physical names
- Tables are migrated from other formats that use different naming conventions
- Column mapping is manually modified to use names not following the field ID pattern

## Resolution

To resolve this error, ensure that all column mapping field physical names conform to the `col-[fieldId]` naming convention. This may involve:

1. Recreating the table with [Delta Lake column mapping](/concepts/delta-table-column-mapping.md) using the correct naming scheme
2. Adjusting any existing [Delta Lake table features](/concepts/delta-lake-reader-table-features.md) to match Iceberg compatibility requirements
3. Modifying column definitions to use field ID-based physical names

## Related Concepts

- DELTA_ICEBERG_WRITER_COMPAT_VIOLATION|Delta-Iceberg Writer Compat Violation — The parent error class for Iceberg compatibility issues
- [IcebergWriterCompatV](/concepts/icebergwritercompatv.md) — The protocol version enforcing this constraint
- [Delta Lake column mapping](/concepts/delta-table-column-mapping.md) — The feature that maps Delta column names to physical storage names
- Apache Iceberg compatibility — Delta Lake's support for reading and writing Iceberg tables
- [Delta Lake table features](/concepts/delta-lake-reader-table-features.md) — Configurable features affecting table behavior and compatibility

## Sources

- delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws-02e8eab9.md)
