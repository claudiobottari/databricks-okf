---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 63e082ed761d2a20c0bd8a9769c4dce4a0a066b81bc489480023bb8e235a5b4b
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - incompatible_table_feature
    - INCOMPATIBLE_TABLE_FEATURE
  citations:
    - file: delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md
title: INCOMPATIBLE_TABLE_FEATURE
description: Error sub-type indicating a table feature is incompatible with IcebergCompatV1
tags:
  - error-messages
  - table-features
  - compatibility
timestamp: "2026-06-19T18:24:59.767Z"
---

# INCOMPATIBLE_TABLE_FEATURE

The **INCOMPATIBLE_TABLE_FEATURE** error is a subcategory of the DELTA_ICEBERG_COMPAT_V1_VIOLATION error class that occurs when a table has a feature enabled that is incompatible with IcebergCompatV1. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Error Details

This error triggers the SQLSTATE KD00E (datasource-specific error). The full error message is:

> IcebergCompatV1 is incompatible with feature `<feature>`.

where `<feature>` is replaced with the name of the incompatible table feature. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Cause

[IcebergCompatV1](/concepts/icebergcompatv1.md) requires that certain table features are either not present or are explicitly compatible. When a table has a feature enabled that IcebergCompatV1 cannot work with, this error is raised. The incompatible feature must be removed or disabled before IcebergCompatV1 can be applied to the table. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Related Errors

The DELTA_ICEBERG_COMPAT_V1_VIOLATION error class includes several other related sub-errors:

- DISABLING_REQUIRED_TABLE_FEATURE — Raised when trying to drop a feature that IcebergCompatV1 requires
- MISSING_REQUIRED_TABLE_FEATURE — Raised when a required feature is not enabled
- REPLACE_TABLE_CHANGE_PARTITION_NAMES — Raised when partition spec names are changed incompatibly
- UNSUPPORTED_DATA_TYPE — Raised when the schema contains unsupported types (MapType, ArrayType, NullType)
- WRONG_REQUIRED_TABLE_PROPERTY — Raised when a required table property has an incorrect value

## Resolution

To resolve this error, identify the incompatible feature and either:

1. Drop or disable the incompatible feature from the table
2. Remove the IcebergCompatV1 setting if the incompatible feature is required

The specific steps depend on which feature is conflicting and whether that feature is necessary for your workload. ^[delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md]

## Related Concepts

- [Delta Lake table features](/concepts/delta-lake-reader-table-features.md)
- [Delta Lake compatibility with Iceberg](/concepts/delta-table-features-compatibility-with-iceberg.md)
- Table properties in Delta Lake

## Sources

- delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_v1_violation-error-class-databricks-on-aws.md](/references/delta_iceberg_compat_v1_violation-error-class-databricks-on-aws-da04bc25.md)
