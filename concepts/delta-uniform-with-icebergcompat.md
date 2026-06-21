---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 15328d9565509d20b01eded81dddd7add9f8abbe8ac29f6dbf25315f2207131f
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-uniform-with-icebergcompat
    - DUWI
    - Delta-Uniform (IcebergCompat)
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: Delta Uniform with IcebergCompat
description: The Uniform feature in Delta Lake enables Apache Iceberg compatibility, and upgrading or enabling it requires all existing files to be Iceberg-compatible, enforced via IcebergCompatV.
tags:
  - delta-lake
  - apache-iceberg
  - uniform
  - compatibility
timestamp: "2026-06-18T11:54:32.938Z"
---

# Delta Uniform with IcebergCompat

**Delta Uniform with IcebergCompat** is a feature that enables Delta Lake tables to be read by Apache Iceberg readers by maintaining an Iceberg-compatible metadata layer on top of Delta Lake data files. The `IcebergCompatV` property enforces that all writes to the table produce files that are compatible with the Apache Iceberg format, ensuring seamless interoperability.

## Overview

Delta Uniform provides a bridge between Delta Lake and Apache Iceberg ecosystems. When you enable `IcebergCompatV<version>` on a Delta table, the table becomes readable as an Iceberg table without requiring data duplication or conversion. This is useful in multi-engine environments where different teams or pipelines use different table formats. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

IcebergCompatVersion values are between 1 and the maximum supported version (`<maxVersion>`). Only one IcebergCompat version can be enabled at a time on any given table. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Enabling IcebergCompat

You enable IcebergCompat by setting the table property when creating or altering a Delta table. The feature requires that all table files are Apache Iceberg compatible and that the table meets certain structural requirements.

To upgrade an existing table to a new IcebergCompat version, use the `REORG TABLE` command:

```sql
REORG TABLE table_name APPLY (UPGRADE UNIFORM ('ICEBERG_COMPAT_VERSION = <newVersion>'))
```

This command re-writes the table's metadata and enables the new IcebergCompat version. Note that after upgrading, Databricks runtime versions without support for the new IcebergCompat version may not be able to write to the table. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Requirements and Constraints

### Table Type

IcebergCompat can only be enabled on [Managed Tables](/concepts/managed-tables-in-databricks.md). External tables are not supported. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Deletion Vectors

IcebergCompat requires Deletion Vectors to be completely purged from the table. If Deletion Vectors are present, you must first disable them and then run `REORG PURGE`:

1. Disable Deletion Vectors on the table.
2. Run `REORG TABLE APPLY (PURGE)` to purge existing Deletion Vectors. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Schema and Data Types

The table schema must be compatible with Apache Iceberg. IcebergCompat does not support certain data types:

- **Unsupported data types** in the schema: `IcebergCompatV<version> does not support the data type <dataType> in your schema.`
- **Unsupported partition column data types**: `IcebergCompatV<version> does not support the data type <dataType> for partition columns in your schema.` ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Type Widening

IcebergCompat is incompatible with type changes (type widening) applied to the table. If a field was changed from one type to another, the table cannot have IcebergCompat enabled. The error message specifies which field was changed and the old and new types. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Partition Spec Changes

IcebergCompat does not support replacing partitioned tables with a differently-named partition spec, because Iceberg-Spark 1.1.0 does not support this operation. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Table Features

IcebergCompatV`<version>` requires certain table features to be supported and enabled. You cannot disable a required feature without first disabling IcebergCompat. Conversely, IcebergCompat is incompatible with certain table features — attempting to enable both will result in an error. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Error Conditions

The `DELTA_ICEBERG_COMPAT_VIOLATION` error class is raised when validation of IcebergCompat fails. The error includes specific sub-conditions that identify the exact issue. Common error conditions include:

| Error Condition | Description |
|-----------------|-------------|
| `CHANGE_VERSION_NEED_REWRITE` | Changing to a new IcebergCompat version requires rewriting the table using `REORG TABLE APPLY (UPGRADE UNIFORM (...))`. |
| `COMPAT_VERSION_NOT_SUPPORTED` | The specified IcebergCompat version is not supported. Supported versions are between 1 and the maximum supported version. |
| `DELETION_VECTORS_NOT_PURGED` | Deletion Vectors must be completely purged using `REORG TABLE APPLY (PURGE)`. |
| `DELETION_VECTORS_SHOULD_BE_DISABLED` | Deletion Vectors must first be disabled, then purged. |
| `FILES_NOT_ICEBERG_COMPAT` | Some files in the table are not Apache Iceberg compatible, usually due to concurrent writes. Re-run the upgrade command. |
| `UNSUPPORTED_DATA_TYPE` | The schema contains a data type not supported by the IcebergCompat version. |
| `UNSUPPORTED_PARTITION_DATA_TYPE` | A partition column uses a data type not supported by the IcebergCompat version. |
| `UNSUPPORTED_TYPE_WIDENING` | A type change has been applied to the table that is incompatible with IcebergCompat. |
| `VERSION_MUTUAL_EXCLUSIVE` | Only one IcebergCompat version can be enabled at a time. |
| `WRONG_REQUIRED_TABLE_PROPERTY` | A required table property is set to the wrong value. |

^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Troubleshooting

If you encounter `FILES_NOT_ICEBERG_COMPAT`, run the `REORG TABLE APPLY (UPGRADE UNIFORM (...))` command again. This condition usually results from concurrent writes to the table during the initial upgrade attempt. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

If you need to change the IcebergCompat version, first disable the current version before enabling the new one, or use `REORG TABLE APPLY (UPGRADE UNIFORM (...))` to migrate directly. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The underlying table format that supports Iceberg compatibility
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The open table format that Delta Uniform targets for compatibility
- [Managed Tables](/concepts/managed-tables-in-databricks.md) — The only table type that supports IcebergCompat
- [Deletion Vectors](/concepts/deletion-vectors.md) — A Delta Lake feature that must be disabled and purged for IcebergCompat
- [REORG TABLE](/concepts/reorg-table.md) — The command used to upgrade, purge, and manage Uniform compatibility

## Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
