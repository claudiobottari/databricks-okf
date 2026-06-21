---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a339221ba20a19bda8377bb79b7b767b380887c21b0fe0c966fd250595bc3699
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta_iceberg_compat_violation-error-class
    - DEC
    - DELTA_ICEBERG_COMPAT_VIOLATION Error Class
    - DELTA_ICEBERG_COMPAT_VIOLATION error class
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: DELTA_ICEBERG_COMPAT_VIOLATION error class
description: A Databricks Delta Lake error class (SQLSTATE KD00E) raised when IcebergCompatV validation fails during table operations.
tags:
  - error-messages
  - delta-lake
  - databricks
timestamp: "2026-06-19T18:25:24.101Z"
---

# DELTA_ICEBERG_COMPAT_VIOLATION error class

The `DELTA_ICEBERG_COMPAT_VIOLATION` error class (SQLSTATE: **KD00E**) indicates that validation of [IcebergCompatV](/concepts/icebergcompatv.md)`<version>` has failed on a Delta table. This error occurs when an operation violates the requirements for enabling or maintaining Uniform Apache Iceberg compatibility at a given compatibility version. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

The error is raised in a variety of situations, from configuration mismatches and missing table features to incompatible schema changes and data layout issues. Each sub-error provides a specific reason and a recommended remediation step.

## CHANGE_VERSION_NEED_REWRITE

Changing the table's `IcebergCompatVersion` from one version to another requires rewriting the table to apply the new compatibility features. The recommended action is to run `REORG TABLE APPLY (UPGRADE UNIFORM ('ICEBERG_COMPAT_VERSION = <newVersion>'))`. Note that after this operation, Databricks runtime versions that do not support the new IcebergCompat version may not be able to write to the table. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## COMPAT_VERSION_NOT_SUPPORTED

The specified `IcebergCompatVersion` is outside the supported range. Supported versions are between `1` and `<maxVersion>`. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## CONFIG_NOT_ENABLED

The requested IcebergCompat version is not enabled in the current environment. Enable it before attempting operations that depend on it. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## DELETION_VECTORS_NOT_PURGED

IcebergCompatV`<version>` requires that all [Deletion Vectors](/concepts/deletion-vectors.md) be completely purged from the table. Run `REORG TABLE APPLY (PURGE)` to remove them. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## DELETION_VECTORS_SHOULD_BE_DISABLED

Deletion Vectors must first be disabled on the table before upgrading to the specified IcebergCompat version. After disabling, run `REORG PURGE` to purge any remaining Deletion Vectors. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## DISABLING_REQUIRED_TABLE_FEATURE

The specified IcebergCompat version requires a certain table feature to be supported and enabled. You cannot drop that feature from the table. If you need to remove it, disable IcebergCompatV`<version>` first. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## FILES_NOT_ICEBERG_COMPAT

Enabling Uniform Apache Iceberg with the given IcebergCompat version requires that all data files in the table are Apache Iceberg compatible. The error reports how many files are incompatible, usually as a result of concurrent writes. Re-run `REORG TABLE APPLY (UPGRADE UNIFORM (ICEBERG_COMPAT_VERSION=<version>))` to retry. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## INCOMPATIBLE_TABLE_FEATURE

The specified IcebergCompat version is incompatible with another table feature that is currently enabled on the table. You must resolve the incompatibility (typically by disabling the conflicting feature) before proceeding. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## MISSING_REQUIRED_TABLE_FEATURE

The table is missing a table feature that is required by the target IcebergCompat version. Enable the missing feature before retrying the operation. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## REPLACE_TABLE_CHANGE_PARTITION_NAMES

IcebergCompatV`<version>` does not support replacing a partitioned table with a differently-named partition spec, because Iceberg-Spark 1.1.0 does not allow it. The error provides the previous and new partition specs for reference. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## REQUIRE_MANAGED_TABLE

This feature can be enabled only on [Managed Tables|managed tables](/concepts/managed-tables-in-databricks.md) in Unity Catalog. External tables or unmanaged tables are not supported. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## REWRITE_DATA_FAILED

Rewriting the table's data to the target IcebergCompat version failed. Run `REORG TABLE APPLY (UPGRADE UNIFORM (ICEBERG_COMPAT_VERSION=<version>))` again to retry. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## SCHEMA_COMPATIBILITY_CHECK_FAILED

An Apache Iceberg schema compatibility check failed during table creation or conversion. The error message includes the reason for the failure. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## UNSUPPORTED_DATA_TYPE

The table schema contains a data type (`<dataType>`) that is not supported by the target IcebergCompat version. The full schema is included in the error message. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## UNSUPPORTED_PARTITION_DATA_TYPE

The partition columns in the table schema use a data type (`<dataType>`) that is not supported by the target IcebergCompat version. The partition schema is included in the error message. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## UNSUPPORTED_TYPE_WIDENING

A type change applied to a column (e.g., widening from `<prevType>` to `<newType>`) is incompatible with the target IcebergCompat version. The error identifies the field path and the old and new types. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## VERSION_MUTUAL_EXCLUSIVE

Only one IcebergCompat version can be enabled on a table at a time. You must explicitly disable all other IcebergCompat versions that are not needed before enabling a new one. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## WRONG_REQUIRED_TABLE_PROPERTY

The table property `<key>` must be set to a specific value (`<requiredValue>`) for the target IcebergCompat version. The current value is `<actualValue>`. Update the table property to the required value. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Related concepts

- [IcebergCompatV](/concepts/icebergcompatv.md) – The compatibility version that triggered the violation.
- [Uniform](/concepts/delta-uniform.md) – The feature set enabling Apache Iceberg compatibility on Delta tables.
- [REORG TABLE](/concepts/reorg-table.md) – The command used to rewrite, purge, or upgrade tables to resolve compatibility issues.
- [Deletion Vectors](/concepts/deletion-vectors.md) – A Delta Lake feature that must be managed for some IcebergCompat versions.
- [Managed Tables](/concepts/managed-tables-in-databricks.md) – The only table type eligible for certain IcebergCompat features.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – The open table format for which compatibility is being enforced.
- Table Features – The feature flags that must be enabled or disabled for compatibility.

## Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
