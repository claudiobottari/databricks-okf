---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3848e5cb72902f24f3c5eafbff014694645fa9faa24e5a4356bd9a35a99ca551
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-table-features-compatibility
    - DLTFC
    - Delta Lake feature compatibility matrix
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: Delta Lake Table Features Compatibility
description: The set of table features that are required, incompatible, or must be enabled/disabled for IcebergCompatV to function correctly.
tags:
  - delta-lake
  - apache-iceberg
  - table-features
timestamp: "2026-06-19T15:05:42.497Z"
---

# [Delta Lake Table](/concepts/delta-lake-table.md) Features Compatibility

**Delta Lake Table Features Compatibility** refers to the constraints and requirements that enforce interoperability between [Delta Lake Table](/concepts/delta-lake-table.md) features and the Apache Iceberg compatibility modes (IcebergCompatV1, V2, etc.). When a table operation violates these compatibility rules, Delta Lake raises a `DELTA_ICEBERG_COMPAT_VIOLATION` error condition. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Overview

IcerbergCompatV`<version>` (e.g., `IcebergCompatV2`) is a table feature that enables a Delta table to be read by Apache Iceberg readers. Enabling this feature imposes restrictions on other table features, schema changes, and data file formats. The `DELTA_ICEBERG_COMPAT_VIOLATION` error class captures all cases where a requested operation would break Iceberg compatibility. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Version Management

- **Version Range**: Only IcebergCompat versions between 1 and a server-defined maximum (`<maxVersion>`) are supported. Selecting an unsupported version yields the `COMPAT_VERSION_NOT_SUPPORTED` sub-error. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]
- **Mutual Exclusivity**: Only one IcebergCompat version can be enabled on a table at a time. Attempting to enable a second version without disabling the first raises the `VERSION_MUTUAL_EXCLUSIVE` error. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]
- **Upgrading**: To move from one version to another, you must rewrite the table using `REORG TABLE APPLY (UPGRADE UNIFORM ('ICEBERG_COMPAT_VERSION = <newVersion>'))`. The error string `CHANGE_VERSION_NEED_REWRITE` directs users to this command. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Required and Incompatible Table Features

- **Required Features**: IcebergCompatV`<version>` mandates that certain Delta table features be supported and enabled. The `MISSING_REQUIRED_TABLE_FEATURE` error indicates a feature is absent; the `DISABLING_REQUIRED_TABLE_FEATURE` error indicates an attempt to drop a required feature. To disable a required feature, IcebergCompat itself must be disabled first. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]
- **Incompatible Features**: Some table features conflict with Iceberg compatibility. The `INCOMPATIBLE_TABLE_FEATURE` error names the conflicting feature. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Deletion Vectors

Deletion Vectors are a Delta Lake feature for efficient delete operations. IcebergCompatV`<version>` may require Deletion Vectors to be completely purged or disabled:

- `DELETION_VECTORS_NOT_PURGED`: Deletion Vectors exist and must be purged from the table via `REORG TABLE APPLY (PURGE)`. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]
- `DELETION_VECTORS_SHOULD_BE_DISABLED`: Deletion Vectors must be disabled on the table first, and then purged. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## File Compatibility

All data files in the table must be Apache Iceberg compatible when IcebergCompat is enabled. The `FILES_NOT_ICEBERG_COMPAT` error reports the count of files that are not compatible, usually caused by a concurrent write. The resolution is to re-run the `REORG TABLE APPLY (UPGRADE UNIFORM ...)` command. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Schema and Type Constraints

Iceberg compatibility imposes restrictions on schema evolution:

- **Unsupported Data Types**: Certain data types (`<dataType>`) in the schema, including partition columns, are not supported by IcebergCompatV`<version>`. This includes both regular column types and partition column types. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]
- **Unsupported Type Widening**: Once IcebergCompat is enabled, type widening changes (e.g., changing a field from `<prevType>` to `<newType>`) are incompatible and raise `UNSUPPORTED_TYPE_WIDENING`. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]
- **Schema Compatibility Check**: During table creation or conversion, an Iceberg schema compatibility check is performed. Failure produces the `SCHEMA_COMPATIBILITY_CHECK_FAILED` error with a reason. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Partitioning Constraints

- **Partition Name Changes**: IcebergCompatV`<version>` does not support replacing a partitioned table with a differently-named partition spec, because Iceberg-Spark 1.1.0 does not allow it. The `REPLACE_TABLE_CHANGE_PARTITION_NAMES` error includes both the previous and new partition specs. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]
- **Unsupported Partition Data Types**: Partition columns may not use data types that Iceberg does not support. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Table Management Requirements

- **Managed Tables Only**: IcebergCompatV`<version>` can be enabled only on [Managed Tables](/concepts/managed-tables-in-databricks.md). External tables are not eligible. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]
- **Required Table Properties**: Certain table properties must be set to exact values. The `WRONG_REQUIRED_TABLE_PROPERTY` error lists the key, required value, and current value. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]
- **Configuration**: IcerbergCompatV`<version>` must be enabled in the runtime environment. If not, the `CONFIG_NOT_ENABLED` error is raised. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Recovering from Violations

Most compatibility violations can be resolved by:

1. Running `REORG TABLE APPLY (UPGRADE UNIFORM ('ICEBERG_COMPAT_VERSION = <version>'))` to re-apply the upgrade after fixing the underlying issue.
2. Disabling Deletion Vectors or purging them if required.
3. Changing the schema to avoid unsupported types or reverting type widenings.
4. Disabling the offending IcebergCompat version if the table feature or operation cannot be changed.

The `REWRITE_DATA_FAILED` error indicates that rewriting data to IcebergCompatV`<version>` failed, and users should re-run the `REORG` command. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) – Open-source storage layer for data lakes.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – Open table format for large analytic datasets.
- [IcebergCompatV](/concepts/icebergcompatv.md) – The versioned compatibility feature between Delta Lake and Iceberg.
- [Deletion Vectors](/concepts/deletion-vectors.md) – Delta Lake feature for soft deletes.
- [REORG TABLE](/concepts/reorg-table.md) – Delta command for rewriting table data and upgrading Uniform.
- [Managed Tables](/concepts/managed-tables-in-databricks.md) – Delta tables whose metadata and data are managed by the [Metastore](/concepts/metastore.md).
- Schema Evolution – Delta Lake's ability to change table schema over time.
- Partitioning – Organizing table data by partition columns.

## Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
