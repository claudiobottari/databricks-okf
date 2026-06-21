---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b86d6120f4a4c8ccf3994e4f17e02de696b9471274c0b2a79ec7cbea6c678bda
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - wrong_required_table_property
    - WRONG_REQUIRED_TABLE_PROPERTY
    - wrong_required_table_property-delta-iceberg-error
    - W(IE
  citations:
    - file: delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
    - file: inferred
title: WRONG_REQUIRED_TABLE_PROPERTY
description: Error sub-type indicating a required table property for IcebergCompatV1 is set to an incorrect value
tags:
  - error-messages
  - table-properties
  - delta-lake
timestamp: "2026-06-19T18:25:13.622Z"
---

# WRONG_REQUIRED_TABLE_PROPERTY

The **WRONG_REQUIRED_TABLE_PROPERTY** sub-error occurs when a Delta table with the [IcebergCompatV1](/concepts/icebergcompatv.md) feature enabled does not have a required table property set to the correct value. This is part of the broader DELTA_ICEBERG_COMPAT_V1_VIOLATION error class, which validates compatibility between Delta Lake and Iceberg. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Error Message

```
IcebergCompatV1 requires table property '<key>' to be set to '<requiredValue>'.
Current value: '<actualValue>'.
```

^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Cause

IcebergCompatV1 enforces specific Delta table properties that are necessary for interoperability with Apache Iceberg readers. When the table property `<key>` exists but holds a value (`<actualValue>`) that differs from the required value (`<requiredValue>`), the validation fails. This typically happens when attempting to modify a critical property or when the table was created with non‑compliant settings. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Resolution

To resolve the error, set the identified table property to the required value:

```sql
ALTER TABLE <table_name> SET TBLPROPERTIES ('<key>' = '<requiredValue>');
```

If the property cannot be changed without breaking existing workloads, consider disabling IcebergCompatV1 first by removing it from the table features, then adjusting the property as needed. ^[inferred] ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md] *(The source states you can disable IcebergCompatV1 first when dealing with incompatible changes, as noted in the DISABLING_REQUIRED_TABLE_FEATURE sub‑error.)*

## Related Concepts

- DELTA_ICEBERG_COMPAT_V1_VIOLATION — The parent error class containing other validation failures such as MISSING_REQUIRED_TABLE_FEATURE, INCOMPATIBLE_TABLE_FEATURE, and UNSUPPORTED_DATA_TYPE.
- [IcebergCompatV1](/concepts/icebergcompatv.md) — A Delta table compatibility mode for Apache Iceberg.
- Delta table properties — Metadata properties that control table behavior.
- Iceberg-Spark integration — The underlying integration that imposes these property requirements.

## Sources

- delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md](/references/delta_iceberg_compat_v1_violation-error-class-databricks-on-aws-da04bc25.md)
2. inferred
