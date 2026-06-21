---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ca3bb5eede4e9034c9975c8c0602ab6f42c8b94ae8db2dac634e1bf35d9ce124
  pageDirectory: concepts
  sources:
    - delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-iceberg-column-mapping-field-physical-name-convention
    - DCMFPNC
  citations:
    - file: delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md
title: Delta-Iceberg column mapping field physical name convention
description: The requirement enforced by IcebergWriterCompatV that column mapping field physical names follow the pattern 'col-[fieldId]'
tags:
  - databricks
  - delta-lake
  - iceberg
  - schema
timestamp: "2026-06-19T10:06:39.834Z"
---

# Delta-Iceberg Column Mapping Field Physical Name Convention

The **Delta-Iceberg column mapping field physical name convention** is a requirement enforced by IcebergWriterCompatV that mandates column mapping field physical names follow the format `col-[fieldId]`. When this convention is violated, the system raises a `FIELD_ID_DOES_NOT_MATCH_PHYSICAL_NAME` error. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Error Condition

The validation occurs as part of the IcebergWriterCompatV checks. The error message is:

```
IcebergWriterCompatV<version> requires column mapping field physical names be 
equal to 'col-[fieldId]', but this is not true for fields: <field_names>, 
physical names: <physical_names>.
```

^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Requirements

The physical name for each column in the table's column mapping must be formatted as `col-<fieldId>` where `<fieldId>` is the numeric identifier assigned to that column in the Delta Lake protocol. This format matches the convention used by [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) for column mapping. ^[delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md]

## Impact

Tables that have column mapping field physical names that do not conform to this convention cannot be written to when IcebergWriterCompatV is enabled. To resolve the issue, you must either:

- Update the column mapping physical names to follow the `col-[fieldId]` convention.
- Disable or remove the IcebergWriterCompatV requirement.

## Related Concepts

- [IcebergWriterCompatV](/concepts/icebergwritercompatv.md) — The validation version that enforces this requirement
- [Delta Lake column mapping](/concepts/delta-table-column-mapping.md) — The feature that maps logical column names to physical storage names
- FIELD_ID_DOES_NOT_MATCH_PHYSICAL_NAME — The specific error subcondition
- Delta Lake protocol — The underlying protocol governing Delta table structure
- Apache Iceberg compatibility — The broader compatibilty framework between Delta Lake and Iceberg formats

## Sources

- delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_writer_compat_violation-error-condition-databricks-on-aws-02e8eab9.md)
