---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2773c0fe5ea3e5dca6014f63022c67181a657cf2529b7db67c87c5b8dddf7d4b
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - incompatible_table_feature-delta-iceberg-error
    - I(IE
  citations:
    - file: delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
title: INCOMPATIBLE_TABLE_FEATURE (Delta Iceberg error)
description: A sub-error of DELTA_ICEBERG_COMPAT_V1_VIOLATION that occurs when a table has a feature incompatible with IcebergCompatV1
tags:
  - delta-lake
  - error-subtype
  - iceberg-compatibility
timestamp: "2026-06-19T15:05:07.073Z"
---

# INCOMPATIBLE_TABLE_FEATURE (Delta Iceberg error)

**INCOMPATIBLE_TABLE_FEATURE** is an error class under the `DELTA_ICEBERG_COMPAT_V1_VIOLATION` error group. It occurs when attempting to use IcebergCompatV1 on a Delta table that has an enabled table feature that is incompatible with the Iceberg compatibility layer. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Overview

The `DELTA_ICEBERG_COMPAT_V1_VIOLATION` error class indicates that validation of the IcebergCompatV1 setting has failed. The specific `INCOMPATIBLE_TABLE_FEATURE` sub-error is raised when one or more enabled [Delta Lake table features](/concepts/delta-lake-reader-table-features.md) conflict with the requirements of IcebergCompatV1. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Error Message

The error message has the following structure:

```
IcebergCompatV1 is incompatible with feature <feature>.
```

Where `<feature>` is replaced with the name of the incompatible table feature. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Related Errors

The `DELTA_ICEBERG_COMPAT_V1_VIOLATION` error class contains several related sub-errors that may arise during IcebergCompatV1 validation:

- **DISABLING_REQUIRED_TABLE_FEATURE** – Occurs when attempting to drop a table feature that IcebergCompatV1 requires. The error advises disabling IcebergCompatV1 first before dropping the feature. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]
- **MISSING_REQUIRED_TABLE_FEATURE** – Occurs when a required table feature is not supported or enabled. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]
- **REPLACE_TABLE_CHANGE_PARTITION_NAMES** – Occurs when attempting to replace a partitioned table with a differently-named partition spec, which IcebergCompatV1 does not support. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]
- **UNSUPPORTED_DATA_TYPE** – Occurs when the schema contains MapType, ArrayType, or NullType, which IcebergCompatV1 does not support. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]
- **WRONG_REQUIRED_TABLE_PROPERTY** – Occurs when a required table property is not set to the expected value. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Resolution

To resolve the `INCOMPATIBLE_TABLE_FEATURE` error, identify the incompatible feature reported in the error message and either:

1. Disable the incompatible table feature from the table, or
2. Disable IcebergCompatV1 on the table if the incompatible feature is required for your use case.

Consult the Delta Lake table features documentation for guidance on enabling and disabling specific features. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Related Concepts

- [IcebergCompatV1](/concepts/icebergcompatv1.md) — The Delta Lake compatibility layer for Apache Iceberg that requires specific table features
- [Delta Lake table features](/concepts/delta-lake-reader-table-features.md) — The mechanism for enabling and disabling Delta Lake capabilities
- DELTA_ICEBERG_COMPAT_V1_VIOLATION error class — The parent error class containing this and related sub-errors
- [Delta Lake and Iceberg interoperability](/concepts/delta-lake-table-features-and-iceberg-compatibility.md) — Broader context for using Delta tables with Iceberg-based tools

## Sources

- delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md](/references/delta_iceberg_compat_v1_violation-error-class-databricks-on-aws-da04bc25.md)
