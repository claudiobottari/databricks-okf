---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d306d9a93c7de1bba0ba67e3caffa26c26a08b6d1d2da1091bfe8ad0f80d67d1
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - uniform-apache-iceberg-format
    - U(IF
    - Uniform (Apache Iceberg)
    - Uniform Apache Iceberg
    - Apache Iceberg
    - Apache Iceberg writer
    - IcebergCompat (Uniform Apache Iceberg)
    - Uniform (Iceberg)
    - Uniform Iceberg
    - managed Apache Iceberg
    - uniform-apache-iceberg-format-in-databricks
    - U(IFID
    - Apache Iceberg on Databricks
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: Uniform (Apache Iceberg) Format
description: A Databricks feature that makes Delta tables readable as Apache Iceberg tables, requiring all files to be Iceberg-compatible and enforced via IcebergCompatV.
tags:
  - delta-lake
  - apache-iceberg
  - databricks
  - format-interoperability
timestamp: "2026-06-19T15:06:14.730Z"
---

# Uniform (Apache Iceberg) Format

**Uniform (Apache Iceberg) Format** is a Databricks table format that enables [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) compatibility for [Delta Lake](/concepts/delta-lake.md) tables. It allows Delta tables to be read and written by Iceberg-compatible engines, providing interoperability between the two formats.

## Overview

The Uniform format is implemented through the `ICEBERG_COMPAT_VERSION` table feature, which enables Apache Iceberg compatibility on Delta tables. This feature allows Delta tables to be accessed by Iceberg readers while maintaining Delta Lake's native capabilities.^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Version Support

The Uniform format supports multiple compatibility versions, with valid versions ranging from 1 to the maximum supported version in the current environment. Only one `ICEBERG_COMPAT_VERSION` can be enabled at a time; all other versions must be explicitly disabled.^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Enabling Uniform Format

To enable or upgrade the Uniform format, use the `REORG TABLE APPLY (UPGRADE UNIFORM)` command:

```sql
REORG TABLE table APPLY (UPGRADE UNIFORM ('ICEBERG_COMPAT_VERSION = <newVersion>'));
```

This command rewrites the table to make it Iceberg-compatible and enables the specified compatibility version. After execution, other Databricks runtime versions that don't support that table feature may not be able to write to the table.^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Requirements and Constraints

### Managed Tables Only
The Uniform format can only be enabled on [Managed Tables](/concepts/managed-tables-in-databricks.md). External tables are not supported for this feature.^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### File Compatibility
Enabling Uniform format requires all existing files to be Apache Iceberg compatible. If some files are not compatible—typically due to concurrent writes—the `REORG TABLE` command must be run again to complete the upgrade.^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Deletion Vectors
The Uniform format requires [Deletion Vectors](/concepts/deletion-vectors.md) to be completely purged from the table. Use the `REORG TABLE APPLY (PURGE)` command to remove them before enabling Iceberg compatibility.^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Required Table Features
The feature requires specific table features to be supported and enabled. You cannot drop required features while Uniform format is active; instead, disable the Uniform format first.^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Unsupported Operations
- **Partition renaming**: The format doesn't support replacing partitioned tables with differently-named partition specs, due to Iceberg-Spark 1.1.0 limitations.^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]
- **Type widening**: Schema changes that widen data types are incompatible with the Uniform format.^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Error Conditions

The `DELTA_ICEBERG_COMPAT_VIOLATION` error class (SQLSTATE: KD00E) is raised when validation of Iceberg compatibility fails. Common error conditions include:

| Error | Description |
|-------|-------------|
| `CHANGE_VERSION_NEED_REWRITE` | Changing to a new compatibility version requires table rewrite |
| `COMPAT_VERSION_NOT_SUPPORTED` | Specified version is outside the supported range (1 to max) |
| `CONFIG_NOT_ENABLED` | Iceberg compatibility is not enabled in the environment |
| `DELETION_VECTORS_NOT_PURGED` | Deletion vectors must be purged before enabling |
| `DELETION_VECTORS_SHOULD_BE_DISABLED` | Deletion vectors must be disabled first |
| `FILES_NOT_ICEBERG_COMPAT` | Some files are not Iceberg-compatible |
| `INCOMPATIBLE_TABLE_FEATURE` | The feature conflicts with other table features |
| `SCHEMA_COMPATIBILITY_CHECK_FAILED` | Schema compatibility check failed |
| `UNSUPPORTED_DATA_TYPE` | Data type not supported in the schema |
| `UNSUPPORTED_PARTITION_DATA_TYPE` | Partition column data type not supported |

^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – The native table format that Uniform format extends
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – The open table format for interoperability
- [Managed Tables](/concepts/managed-tables-in-databricks.md) – Required table type for Uniform format
- [Deletion Vectors](/concepts/deletion-vectors.md) – Must be purged for Iceberg compatibility
- [REORG Command](/concepts/reorg-table.md) – Used to upgrade and maintain Uniform format tables
- Table Features – Enables specific capabilities in Delta Lake

## Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
