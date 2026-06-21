---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3390bced97c3230176da993623ada22bd9cbbd62c56063c7ab4aac2eedb4a425
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-table-features-and-icebergcompat-dependencies
    - IcebergCompat dependencies and Delta Table Features
    - DTFAID
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: Delta Table Features and IcebergCompat dependencies
description: IcebergCompatV requires specific Delta table features to be enabled and supported, and prevents dropping required features or enabling incompatible features simultaneously.
tags:
  - delta-lake
  - table-features
  - apache-iceberg
  - compatibility
timestamp: "2026-06-18T11:54:33.271Z"
---

# Delta Table Features and IcebergCompat Dependencies

**Delta Table Features and IcebergCompat dependencies** describes the relationship between [Delta Lake](/concepts/delta-lake.md) table features and the IcebergCompatV1/V2 compatibility modes. When enabling IcebergCompat on a Delta table, certain table features are required, while others are incompatible or must be disabled first.

## Overview

IcebergCompatV1 and IcebergCompatV2 are [Delta Lake](/concepts/delta-lake.md) table features that enable compatibility with [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) readers. Enabling these modes imposes specific requirements on the table's existing features and configuration. Violations of these requirements result in a `DELTA_ICEBERG_COMPAT_VIOLATION` error. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Required Table Features

IcebergCompatV`<version>` requires certain table features to be supported and enabled on the table. If a required feature is missing, the error `MISSING_REQUIRED_TABLE_FEATURE` is raised. If a required feature is present but disabled, the error `DISABLING_REQUIRED_TABLE_FEATURE` is raised — you cannot drop the feature from the table without first disabling IcebergCompat. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Incompatible Table Features

Some table features are incompatible with IcebergCompat. If an incompatible feature is enabled on the table, the error `INCOMPATIBLE_TABLE_FEATURE` is raised. You must disable or remove the incompatible feature before enabling IcebergCompat. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Deletion Vectors

IcebergCompatV`<version>` has specific requirements regarding [Deletion Vectors](/concepts/deletion-vectors.md):

- **Deletion Vectors must be disabled first.** If Deletion Vectors are currently enabled, the error `DELETION_VECTORS_SHOULD_BE_DISABLED` is raised. You must disable Deletion Vectors on the table, then run `REORG TABLE APPLY (PURGE)` to purge existing Deletion Vectors. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]
- **Deletion Vectors must be completely purged.** Even after disabling, any remaining Deletion Vectors in the table cause the error `DELETION_VECTORS_NOT_PURGED`. Run `REORG TABLE APPLY (PURGE)` to remove them. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Type Widening

IcebergCompatV`<version>` is incompatible with type changes applied to the table. If a column's data type has been widened (for example, from `INT` to `BIGINT`), the error `UNSUPPORTED_TYPE_WIDENING` is raised, indicating the field path and the previous and new types. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Unsupported Data Types

IcebergCompatV`<version>` does not support certain data types in the table schema or in partition columns. If an unsupported data type is found in the schema, the error `UNSUPPORTED_DATA_TYPE` is raised. If found in partition columns, the error `UNSUPPORTED_PARTITION_DATA_TYPE` is raised. Both errors include the full schema for reference. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Table Property Requirements

IcebergCompatV`<version>` requires specific table properties to be set to specific values. If a required property has an incorrect value, the error `WRONG_REQUIRED_TABLE_PROPERTY` is raised, indicating the property key, the required value, and the current value. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Version Mutual Exclusivity

Only one IcebergCompat version can be enabled at a time. If you attempt to enable a second version while another is already active, the error `VERSION_MUTUAL_EXCLUSIVE` is raised. You must explicitly disable all other IcebergCompat versions that are not needed. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Managed Table Requirement

IcebergCompat can only be enabled on [managed tables](/concepts/managed-tables-in-databricks.md). If you attempt to enable it on an external table, the error `REQUIRE_MANAGED_TABLE` is raised. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## File Compatibility

Enabling IcebergCompat requires all existing files in the table to be Apache Iceberg compatible. If concurrent writes have produced incompatible files, the error `FILES_NOT_ICEBERG_COMPAT` is raised, indicating the number of incompatible files and the table version. Running `REORG TABLE APPLY (UPGRADE UNIFORM (ICEBERG_COMPAT_VERSION=<version>))` again may resolve this. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Partition Spec Changes

IcebergCompatV`<version>` does not support replacing partitioned tables with a differently-named partition spec, due to limitations in Iceberg-Spark 1.1.0. Attempting this raises the error `REPLACE_TABLE_CHANGE_PARTITION_NAMES`, showing both the previous and new partition specs. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Schema Compatibility

During table creation or conversion to IcebergCompat, an Apache Iceberg schema compatibility check is performed. If this check fails, the error `SCHEMA_COMPATIBILITY_CHECK_FAILED` is raised with the reason for the failure. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Rewriting Data

When upgrading to a new IcebergCompat version, data may need to be rewritten. If the rewrite fails, the error `REWRITE_DATA_FAILED` is raised. Running `REORG TABLE APPLY (UPGRADE UNIFORM (ICEBERG_COMPAT_VERSION=<version>))` again may resolve this. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Version Upgrade Path

To change to a newer IcebergCompat version, the error `CHANGE_VERSION_NEED_REWRITE` indicates that rewriting the table is required. Run `REORG TABLE APPLY (UPGRADE UNIFORM ('ICEBERG_COMPAT_VERSION = <newVersion>'))`. Note that after the upgrade, Databricks runtime versions without support for the new IcebergCompat version may not be able to write to the table. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Environment Support

IcebergCompatV`<version>` must be enabled in the current environment. If it is not, the error `CONFIG_NOT_ENABLED` is raised. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Version Support Range

IcebergCompatVersion must be within the supported range. If an unsupported version is specified, the error `COMPAT_VERSION_NOT_SUPPORTED` is raised, indicating the supported range (1 to `<maxVersion>`). ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Summary of Dependencies

| Dependency Type | Condition | Error |
|----------------|-----------|-------|
| Required table features | Missing | `MISSING_REQUIRED_TABLE_FEATURE` |
| Required table features | Disabled | `DISABLING_REQUIRED_TABLE_FEATURE` |
| Incompatible table features | Present | `INCOMPATIBLE_TABLE_FEATURE` |
| Deletion Vectors | Enabled | `DELETION_VECTORS_SHOULD_BE_DISABLED` |
| Deletion Vectors | Not purged | `DELETION_VECTORS_NOT_PURGED` |
| Type widening | Applied | `UNSUPPORTED_TYPE_WIDENING` |
| Unsupported data types | In schema | `UNSUPPORTED_DATA_TYPE` |
| Unsupported partition types | In partition spec | `UNSUPPORTED_PARTITION_DATA_TYPE` |
| Table properties | Incorrect value | `WRONG_REQUIRED_TABLE_PROPERTY` |
| Version exclusivity | Multiple versions | `VERSION_MUTUAL_EXCLUSIVE` |
| Table type | External | `REQUIRE_MANAGED_TABLE` |
| File compatibility | Incompatible files | `FILES_NOT_ICEBERG_COMPAT` |
| Partition spec | Renamed | `REPLACE_TABLE_CHANGE_PARTITION_NAMES` |
| Schema compatibility | Check failed | `SCHEMA_COMPATIBILITY_CHECK_FAILED` |
| Data rewrite | Failed | `REWRITE_DATA_FAILED` |
| Version upgrade | Needs rewrite | `CHANGE_VERSION_NEED_REWRITE` |
| Environment | Not enabled | `CONFIG_NOT_ENABLED` |
| Version range | Out of range | `COMPAT_VERSION_NOT_SUPPORTED` |

## Related Concepts

- Delta Lake Table Features — The feature system that IcebergCompat depends on
- [Uniform Iceberg](/concepts/uniform-apache-iceberg-format.md) — The broader compatibility feature for Apache Iceberg
- [Deletion Vectors](/concepts/deletion-vectors.md) — A Delta feature that must be disabled for IcebergCompat
- [Managed Tables](/concepts/managed-tables-in-databricks.md) — The only table type that supports IcebergCompat
- [REORG TABLE](/concepts/reorg-table.md) — The command used to upgrade or repair IcebergCompat
- Delta Table Properties — Configuration properties that IcebergCompat may require

## Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
