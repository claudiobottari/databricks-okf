---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7a53c16a836a11109372b8380cb4adcc34b2a21a9d65e5d4937fa3cd145f11b8
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - wrong_required_table_property-delta-iceberg-error
    - W(IE
  citations:
    - file: delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
title: WRONG_REQUIRED_TABLE_PROPERTY (Delta Iceberg error)
description: A sub-error of DELTA_ICEBERG_COMPAT_V1_VIOLATION that occurs when a required table property for IcebergCompatV1 is set to an incorrect value
tags:
  - delta-lake
  - error-subtype
  - table-properties
  - iceberg-compatibility
timestamp: "2026-06-19T15:05:26.626Z"
---

Here is the wiki page for "WRONG_REQUIRED_TABLE_PROPERTY (Delta Iceberg error)".

# WRONG_REQUIRED_TABLE_PROPERTY (Delta Iceberg error)

**WRONG_REQUIRED_TABLE_PROPERTY** is a subtype of the DELTA_ICEBERG_COMPAT_V1_VIOLATION error class. It occurs when a [Delta Lake](/concepts/delta-lake.md) table has the [IcebergCompatV1](/concepts/icebergcompatv1.md) writer feature enabled but a required table property is not set to the expected value. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Error Message

When this error is raised, the system returns a message in the following format:

```
IcebergCompatV1 requires table property '<key>' to be set to '<requiredValue>'. Current value: '<actualValue>'.
```

^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Cause

This error occurs during validation of IcebergCompatV1 when a table property that is mandatory for compatibility with the Apache Iceberg format has been set to an incorrect value. The error identifies the specific property key, the value that is required, and the current (incorrect) value found on the table. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Resolution

To resolve this error, update the specified table property to the required value. The exact property and required value are provided in the error message. After updating the property, the IcebergCompatV1 validation will pass. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Related Concepts

- [IcebergCompatV1](/concepts/icebergcompatv1.md) – The Delta Lake writer feature that enables compatibility with Apache Iceberg readers.
- DELTA_ICEBERG_COMPAT_V1_VIOLATION error class – The parent error class containing related validation failures.
- Table Properties in Delta Lake – Configuration settings that control [Delta Lake Table](/concepts/delta-lake-table.md) behavior.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – The open table format that Delta Lake’s IcebergCompatV1 writer feature aims to be compatible with.
- MISSING_REQUIRED_TABLE_FEATURE – Another validation error in the same error class, indicating a missing feature rather than a wrong property value.
- DISABLING_REQUIRED_TABLE_FEATURE – An error that occurs when attempting to drop a required table feature while IcebergCompatV1 is enabled.

## Sources

- delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md](/references/delta_iceberg_compat_v1_violation-error-class-databricks-on-aws-da04bc25.md)
