---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bf660cfa1dc1f8dd43ab732857ce798477b4dc732511e3c74790a77cc976168c
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
  confidence: 0.94
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - icebergcompatv1-required-table-properties
    - IRTP
    - Apache Iceberg Table Properties
    - Iceberg-compatible table properties
  citations:
    - file: delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
title: IcebergCompatV1 Required Table Properties
description: The requirement that certain table properties must be set to specific values for IcebergCompatV1 to be valid, and violations raise the WRONG_REQUIRED_TABLE_PROPERTY sub-error.
tags:
  - delta-lake
  - table-properties
  - iceberg
timestamp: "2026-06-19T10:06:00.849Z"
---

# IcebergCompatV1 Required Table Properties

**IcebergCompatV1 Required Table Properties** refers to the set of table properties and features that must be correctly configured and enabled for IcebergCompatV1 validation to succeed. When these requirements are not met, Delta Lake raises the `DELTA_ICEBERG_COMPAT_V1_VIOLATION` error.

## Overview

IcebergCompatV1 enforces strict validation on Delta tables to ensure compatibility with Apache Iceberg readers. This validation checks that specific table features and properties are present and correctly configured. Any violation produces an error within the `DELTA_ICEBERG_COMPAT_V1_VIOLATION` error class. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Required Table Properties

### WRONG_REQUIRED_TABLE_PROPERTY

IcebergCompatV1 requires a table property `<key>` to be set to `<requiredValue>`. If the current value differs from the required value, the error reports both the required and actual values. This error occurs when a mandatory table property has been set to an incorrect value. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Required Table Features

### MISSING_REQUIRED_TABLE_FEATURE

IcebergCompatV1 requires feature `<feature>` to be supported and enabled, but it is missing from the table. You must enable the required feature to satisfy IcebergCompatV1 validation. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

### DISABLING_REQUIRED_TABLE_FEATURE

IcebergCompatV1 requires feature `<feature>` to be supported and enabled. You cannot drop this feature from the table while IcebergCompatV1 is active. To remove the feature, you must first disable IcebergCompatV1. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Other Validation Violations

### INCOMPATIBLE_TABLE_FEATURE

IcebergCompatV1 is incompatible with feature `<feature>`. The presence of an incompatible feature prevents IcebergCompatV1 from being used on the table. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

### UNSUPPORTED_DATA_TYPE

IcebergCompatV1 does not support schemas that contain `MapType`, `ArrayType`, or `NullType` columns. The error message includes the full schema that contains the unsupported types. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

### REPLACE_TABLE_CHANGE_PARTITION_NAMES

IcebergCompatV1 does not support replacing partitioned tables with a differently-named partition spec, because Iceberg-Spark 1.1.0 does not support this operation. The error includes both the previous and new partition specifications. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Best Practices

- Enable all required table features before enabling IcebergCompatV1
- Verify that table properties are set to the exact required values
- Avoid schemas containing `MapType`, `ArrayType`, or `NullType`
- Disable IcebergCompatV1 before making structural changes that would violate its requirements

## Related Concepts

- [Delta Lake Iceberg Compatibility](/concepts/delta-lake-table-features-and-iceberg-compatibility.md)
- Iceberg Table Format
- Delta Table Properties
- Delta Table Features
- [IcebergCompatV1](/concepts/icebergcompatv1.md)

## Sources

- delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md](/references/delta_iceberg_compat_v1_violation-error-class-databricks-on-aws-da04bc25.md)
