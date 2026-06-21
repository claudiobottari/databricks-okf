---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c932a1482c431964822043b054cd3c7edbdb7ec60ff797ae7a46447ba9dd8b29
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - disabling_required_table_feature-error
  citations:
    - file: delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
title: DISABLING_REQUIRED_TABLE_FEATURE error
description: A sub-error of DELTA_ICEBERG_COMPAT_V1_VIOLATION indicating an attempt to drop a table feature that IcebergCompatV1 requires.
tags:
  - delta-lake
  - error-handling
  - table-features
timestamp: "2026-06-18T11:53:40.259Z"
---

# DISABLING_REQUIRED_TABLE_FEATURE Error

The **DISABLING_REQUIRED_TABLE_FEATURE** error occurs when attempting to drop a table feature that [IcebergCompatV1](/concepts/icebergcompatv1.md) requires to be supported and enabled. This is a validation error within the `DELTA_ICEBERG_COMPAT_V1_VIOLATION` error class (SQLSTATE: KD00E).

## Error Message

```
IcebergCompatV1 requires feature <feature> to be supported and enabled. You cannot drop it from the table. Instead, please disable IcebergCompatV1 first.
```

^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Cause

[IcebergCompatV1](/concepts/icebergcompatv1.md) requires specific table features to be supported and enabled on the table for compatibility with Apache Iceberg. When you attempt to disable or drop a required feature from the table, the system detects the violation and prevents the operation. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Solution

To resolve this error, you must first disable [IcebergCompatV1](/concepts/icebergcompatv1.md) on the table before you can drop or remove the required table feature. The error message explicitly states: "You cannot drop it from the table. Instead, please disable IcebergCompatV1 first." ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

### Steps to Disable IcebergCompatV1

1. **Alter the table** to remove the IcebergCompatV1 setting.
2. **Remove the property** that enables IcebergCompatV1 compatibility.
3. **Drop or modify** the previously required feature as needed.

## Related Errors

The `DELTA_ICEBERG_COMPAT_V1_VIOLATION` error class includes several related error conditions:

- MISSING_REQUIRED_TABLE_FEATURE — IcebergCompatV1 requires a feature to be supported and enabled
- INCOMPATIBLE_TABLE_FEATURE — IcebergCompatV1 is incompatible with a specific feature
- UNSUPPORTED_DATA_TYPE — IcebergCompatV1 doesn't support certain data types (MapType, ArrayType, NullType)
- WRONG_REQUIRED_TABLE_PROPERTY — A table property must be set to a specific value for IcebergCompatV1

## Related Concepts

- [IcebergCompatV1](/concepts/icebergcompatv1.md) — The compatibility mode for Apache Iceberg integration
- [Delta Lake table features](/concepts/delta-lake-reader-table-features.md) — Features that enable specific Delta Lake capabilities
- Table properties — Configuration settings for Delta tables

# Citations

1. [delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md](/references/delta_iceberg_compat_v1_violation-error-class-databricks-on-aws-da04bc25.md)
