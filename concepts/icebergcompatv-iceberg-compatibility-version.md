---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5b9e93c3011614b1cb1896cea70572f6ef45993b6dc59d12e5e1060207f2cda6
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - icebergcompatv-iceberg-compatibility-version
    - I(CV
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: IcebergCompatV (Iceberg Compatibility Version)
description: A Delta Lake table setting that enforces compatibility with Apache Iceberg format, with version constraints between 1 and a maximum supported version.
tags:
  - delta-lake
  - apache-iceberg
  - databricks
  - table-properties
timestamp: "2026-06-19T15:05:43.998Z"
---

# IcebergCompatV (Iceberg Compatibility Version)

**IcebergCompatV** refers to a versioned compatibility layer in [Unity Catalog](/concepts/unity-catalog.md) that enables [Delta Lake](/concepts/delta-lake.md) tables to interoperate with [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) readers and writers. Each version (e.g., IcebergCompatV1, IcebergCompatV2) defines a specific set of required table features, behaviors, and constraints that must be met for the table to be considered Iceberg-compatible. When a table operation violates these requirements, Databricks raises a `DELTA_ICEBERG_COMPAT_VIOLATION` error with a detailed subreason.

## Overview

IcebergCompatV is part of the [Uniform](/concepts/delta-uniform.md) format conversion framework in [Delta Lake](/concepts/delta-lake.md). When a table declares an IcebergCompat version, all files in the table must be written in a format that Apache Iceberg can read. Databricks uses `REORG TABLE APPLY (UPGRADE UNIFORM)` commands to rewrite table data into the required Iceberg-compatible format. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Supported Versions

IcebergCompat supports versions 1 through `<maxVersion>`. Each version imposes stricter requirements on table metadata and file format. The specific version number is embedded in the error message as `IcebergCompatV<version>`. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Common Violations

### CHANGE_VERSION_NEED_REWRITE

Changing from one IcebergCompat version to another requires rewriting the table. Run:
```sql
REORG TABLE APPLY (UPGRADE UNIFORM ('ICEBERG_COMPAT_VERSION = <newVersion>'));
```
This command enables the new table feature and may prevent older Databricks runtimes from writing to the table. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### COMPAT_VERSION_NOT_SUPPORTED

The requested IcebergCompat version is outside the supported range (1 to `<maxVersion>`). ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### CONFIG_NOT_ENABLED

The IcebergCompat version is not enabled in the current environment. This typically means the Databricks runtime or cluster configuration does not support the specified version. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### DELETION_VECTORS_NOT_PURGED

IcebergCompat requires [Deletion Vectors](/concepts/deletion-vectors.md) to be completely purged from the table before conversion. Run `REORG TABLE APPLY (PURGE)` to remove them. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### DELETION_VECTORS_SHOULD_BE_DISABLED

Deletion Vectors must be disabled on the table first, then purged with `REORG PURGE`. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### DISABLING_REQUIRED_TABLE_FEATURE

A required table feature (e.g., Deletion Vectors) cannot be dropped while IcebergCompat is enabled. Disable IcebergCompat first, then remove the feature. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### FILES_NOT_ICEBERG_COMPAT

Some files in the table are not written in Iceberg-compatible format. This usually happens due to concurrent writes. Run `REORG TABLE APPLY (UPGRADE UNIFORM)` again to rewrite the incompatible files. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### INCOMPATIBLE_TABLE_FEATURE

The requested IcebergCompat version conflicts with an existing table feature. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### MISSING_REQUIRED_TABLE_FEATURE

A table feature required by IcebergCompat is not enabled. Enable the feature before upgrading. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### REPLACE_TABLE_CHANGE_PARTITION_NAMES

IcebergCompat does not support replacing a partitioned table with a differently-named partition spec (Iceberg-Spark limitation). ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### REQUIRE_MANAGED_TABLE

IcebergCompat can only be enabled on [Managed Tables](/concepts/managed-tables-in-databricks.md) in Unity Catalog. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### REWRITE_DATA_FAILED

Data rewriting failed. Retry the `REORG TABLE` command. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### SCHEMA_COMPATIBILITY_CHECK_FAILED

The table schema is incompatible with Apache Iceberg. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### UNSUPPORTED_DATA_TYPE

An unsupported data type in the schema prevents IcebergCompat conversion. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### UNSUPPORTED_PARTITION_DATA_TYPE

An unsupported data type in partition columns prevents conversion. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### UNSUPPORTED_TYPE_WIDENING

A type change (widening) applied to the table is incompatible with IcebergCompat. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### VERSION_MUTUAL_EXCLUSIVE

Only one IcebergCompat version can be enabled. Disable all other versions before enabling a new one. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### WRONG_REQUIRED_TABLE_PROPERTY

A required table property has an incorrect value. Set the property to the required value before upgrading. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Uniform](/concepts/delta-uniform.md) – The format conversion framework for Delta Lake to Iceberg
- [Deletion Vectors](/concepts/deletion-vectors.md) – A Delta Lake feature that must be purged before Iceberg conversion
- [Managed Tables](/concepts/managed-tables-in-databricks.md) – Tables that support IcebergCompat in Unity Catalog
- [Delta Lake](/concepts/delta-lake.md) – The underlying table format being converted
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – The target format for compatibility
- [REORG TABLE](/concepts/reorg-table.md) – The command used to rewrite and upgrade table format
- Table Features – Features that must be enabled or disabled for compatibility

## Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
