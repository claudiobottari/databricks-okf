---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5fd5339f3d9d2de7eb940b227353b189cf35fcd556c22ce774f4733591e824dd
  pageDirectory: concepts
  sources:
    - delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - delta-lake-universal-format-deltauniversalformatenabledformats
    - DLUF(
  citations:
    - file: delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md
title: Delta Lake Universal Format (delta.universalFormat.enabledFormats)
description: A Delta Lake table property that enables multi-format support, requiring explicit opt-in for features like SYNC UNIFORM
tags:
  - delta-lake
  - table-property
  - format-interoperability
  - databricks
timestamp: "2026-06-18T15:24:31.036Z"
---



# Delta Lake Universal Format (delta.universalFormat.enabledFormats)

**Delta Lake Universal Format** is a configuration property (`delta.universalFormat.enabledFormats`) that controls which reader formats are permitted when using the `REFRESH SYNC UNIFORM` operation on Delta tables. This setting determines the compatibility requirements for synchronizing [Delta Lake](/concepts/delta-lake.md) tables with external formats like Apache Iceberg, Apache Hudi, or Apache XTable.

## Overview

The `delta.universalFormat.enabledFormats` property specifies which [Uniform Format](/concepts/delta-uniform.md) readers are enabled for a Delta table. When using `REFRESH SYNC UNIFORM`, the system checks that the enabled formats are compatible with the table's existing features and configuration. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Compatibility Requirements

For `REFRESH SYNC UNIFORM` to work successfully, the `delta.universalFormat.enabledFormats` must include the necessary format compatibility settings. Without proper configuration, the operation will fail with a `COMPATIBILITY_NOT_ENABLED` error. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Supported Formats

The `delta.universalFormat.enabledFormats` property can be configured to support various external table formats, including:

- Apache Iceberg
- Apache Hudi
- Apache XTable
- Other compatible formats

## Error Conditions

When `delta.universalFormat.enabledFormats` is not properly configured, the following error conditions can occur:

- **COMPATIBILITY_NOT_ENABLED**: The `REFRESH SYNC UNIFORM` operation requires compatibility to be included in `delta.universalFormat.enabledFormats`. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

- **UNSUPPORTED_READER_FEATURES**: The reader table features specified are not supported by `REFRESH SYNC UNIFORM`. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

- **COLUMN_MASK**: Column masks are not supported by the `REFRESH SYNC UNIFORM` operation. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

- **ROW_LEVEL_SECURITY**: Row-level security is not supported by the `REFRESH SYNC UNIFORM` operation. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

- **UNSUPPORTED_TYPE**: The source type specified is not supported by `REFRESH SYNC UNIFORM`. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

- **WRONG_TYPE**: The `REFRESH` keyword identifier `SYNC UNIFORM` cannot be used for the specified source type. ^[delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md]

## Configuration

To enable universal format support, configure the table property:

```sql
ALTER TABLE <table_name> 
SET TBLPROPERTIES (
  'delta.universalFormat.enabledFormats' = '<format1>,<format2>'
);
```

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) - The foundational data lake storage layer
- [Uniform Format](/concepts/delta-uniform.md) - Multi-format compatibility for Delta tables
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) - An open table format for large analytic datasets
- Apache Hudi - A data lake platform that brings database capabilities
- Table Features - [Delta Lake Table](/concepts/delta-lake-table.md) features and capabilities
- [REFRESH SYNC UNIFORM](/concepts/refresh-sync-uniform.md) - The sync operation for maintaining format consistency

## Sources

- delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md

# Citations

1. [delta_uniform_refresh_not_supported-error-condition-databricks-on-aws.md](/references/delta_uniform_refresh_not_supported-error-condition-databricks-on-aws-9dd3f333.md)
