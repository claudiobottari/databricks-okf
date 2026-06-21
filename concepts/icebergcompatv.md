---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 60836e722e254294e5ac103abbef4efc39064bb138b62a56b45ac26ee5f8865e
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - icebergcompatv
    - IcebergCompat
    - Iceberg compatibility
    - icebergcompatv-iceberg-compatibility-version
    - I(CV
    - icebergcompatv1
    - IcebergCompatV1 protocol
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: IcebergCompatV
description: A Delta Lake table setting in Databricks that enables compatibility with Apache Iceberg readers, subject to version-specific validation rules.
tags:
  - delta-lake
  - apache-iceberg
  - databricks
  - table-format
timestamp: "2026-06-18T15:20:03.287Z"
---

# IcebergCompatV

**IcebergCompatV** is a versioned table feature in [Delta Lake](/concepts/delta-lake.md) that enables compatibility with [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) readers. By enabling IcebergCompatV on a Delta table, the table becomes readable by Iceberg clients without requiring additional conversion steps. The feature is part of Databricks' **Uniform** format offering, which allows a single table to be accessed as both Delta and Iceberg. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## DELTA_ICEBERG_COMPAT_VIOLATION Error

The `DELTA_ICEBERG_COMPAT_VIOLATION` error class is raised when validation of an IcebergCompatV setting fails. The error provides a SQLSTATE of `KD00E` and includes a sub‑error that identifies the specific violation. Databricks returns one of the following sub‑errors to help diagnose and resolve the issue. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### CHANGE_VERSION_NEED_REWRITE

Attempting to change from one IcebergCompat version to another (e.g., from V1 to V2) without rewriting the table triggers this error. The fix is to run:
```sql
REORG TABLE APPLY (UPGRADE UNIFORM ('ICEBERG_COMPAT_VERSION = <newVersion>'));
```
Note that after the upgrade, older Databricks runtimes without support for the new version may not be able to write to the table. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### COMPAT_VERSION_NOT_SUPPORTED

The specified IcebergCompatVersion number is outside the supported range. Supported versions are between 1 and `<maxVersion>`. Use a version within that range to resolve the error. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### CONFIG_NOT_ENABLED

IcebergCompatV`<version>` is not enabled in the current environment. This indicates that the runtime or workspace configuration does not support the feature. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### DELETION_VECTORS_NOT_PURGED

IcebergCompatV requires that [Deletion Vectors](/concepts/deletion-vectors.md) be fully purged from the table. Run `REORG TABLE APPLY (PURGE)` to remove all deletion vectors before enabling IcebergCompatV. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### DELETION_VECTORS_SHOULD_BE_DISABLED

Deletion Vectors are enabled on the table and must be disabled first. After disabling them, run `REORG PURGE` to purge the remaining deletion vectors. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### DISABLING_REQUIRED_TABLE_FEATURE

IcebergCompatV requires a certain table feature (e.g., `deletionVectors` or another feature) to be supported and enabled. You cannot drop that required feature; instead, disable IcebergCompatV first if you want to remove the feature. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### FILES_NOT_ICEBERG_COMPAT

When enabling Uniform Apache Iceberg with IcebergCompatV, all files must be Iceberg‑compatible. This error indicates that some files are not compatible, usually because of concurrent writes. Re‑run the `REORG TABLE APPLY (UPGRADE UNIFORM ...)` command to retry the conversion. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### INCOMPATIBLE_TABLE_FEATURE

IcebergCompatV is incompatible with another enabled table feature. Identify the conflicting feature and disable or remove it before enabling IcebergCompatV. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### MISSING_REQUIRED_TABLE_FEATURE

IcebergCompatV requires a specific table feature to be supported and enabled. Enable the missing feature before proceeding. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### REPLACE_TABLE_CHANGE_PARTITION_NAMES

IcebergCompatV does not support replacing a partitioned table with a differently‑named partition spec (limitation inherited from Iceberg‑Spark 1.1.0). Use the same partition column names when replacing the table. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### REQUIRE_MANAGED_TABLE

IcebergCompatV can only be enabled on [Managed Tables](/concepts/managed-tables-in-databricks.md). Convert the table to a managed table (managed by Unity Catalog or the [Metastore](/concepts/metastore.md)) before enabling the feature. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### REWRITE_DATA_FAILED

The data rewrite process for IcebergCompatV failed. Re‑run the `REORG TABLE APPLY (UPGRADE UNIFORM...)` command to retry the upgrade. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### SCHEMA_COMPATIBILITY_CHECK_FAILED

An Apache Iceberg schema compatibility check failed during table creation or conversion. The error includes a `<reason>` that details the incompatibility. Adjust the schema accordingly. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### UNSUPPORTED_DATA_TYPE

IcebergCompatV does not support the specified data type in the table schema. Review the schema and replace unsupported types with compatible alternatives. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### UNSUPPORTED_PARTITION_DATA_TYPE

The data type used in a partition column is not supported by IcebergCompatV. Change the partition column to a supported type. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### UNSUPPORTED_TYPE_WIDENING

A type change (widening) applied to a field is incompatible with IcebergCompatV. For example, changing a column from `<prevType>` to `<newType>` is not allowed while IcebergCompatV is enabled. Either revert the type change or disable IcebergCompatV. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### VERSION_MUTUAL_EXCLUSIVE

Only one IcebergCompat version can be enabled at a time. Explicitly disable any other IcebergCompat versions that are not needed before enabling a new one. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### WRONG_REQUIRED_TABLE_PROPERTY

IcebergCompatV requires a specific table property to be set to a required value. The error message shows the key, required value, and the current value. Set the property to the required value. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Uniform Apache Iceberg](/concepts/uniform-apache-iceberg-format.md)
- [Deletion Vectors](/concepts/deletion-vectors.md)
- [Managed Tables](/concepts/managed-tables-in-databricks.md)
- [REORG Command](/concepts/reorg-table.md)
- Delta Lake Table Features
- [Iceberg Compat Version](/concepts/icebergcompatv-versioning.md)

## Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
