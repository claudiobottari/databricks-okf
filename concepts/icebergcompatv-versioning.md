---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 27c83020e300495fa86a4e50d1809da6d84498a7cccb3f085182f078ceeff2d1
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - icebergcompatv-versioning
    - Iceberg Compat Version
    - IcebergCompatV1 configuration
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: IcebergCompatV versioning
description: Delta Lake table property controlling Uniform Iceberg compatibility level (versions 1 to maxVersion), where only one version can be enabled at a time and upgrading requires REORG TABLE.
tags:
  - delta-lake
  - iceberg-compatibility
  - versioning
timestamp: "2026-06-19T10:06:33.521Z"
---

# IcebergCompatV Versioning

**IcebergCompatV versioning** refers to the mechanism by which [Delta Lake](/concepts/delta-lake.md) tables enable compatibility with [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) through the Uniform Iceberg feature. The version of IcebergCompatV (e.g., `IcebergCompatV1`, `IcebergCompatV2`) determines the specific set of table features, data types, and schema constraints that the table must satisfy in order to remain readable by Iceberg readers. Only one IcebergCompat version can be enabled on a table at a time. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Version Range and Mutual Exclusivity

IcebergCompatV supports versions between 1 and a system-defined maximum (<maxVersion>). If an attempt is made to set an unsupported version, the error `COMPAT_VERSION_NOT_SUPPORTED` is raised. The versions are mutually exclusive: enabling a new version requires explicitly disabling any other IcebergCompat version that is already active (`VERSION_MUTUAL_EXCLUSIVE`). ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Enabling and Upgrading Versions

Changing the IcebergCompat version of a table requires rewriting the table’s data to conform to the new version’s requirements. This is accomplished by running:
```sql
REORG TABLE APPLY (UPGRADE UNIFORM ('ICEBERG_COMPAT_VERSION = <newVersion>'));
```
When the upgrade is triggered, Databricks enables the table feature `IcebergCompatV<newVersion>`. After the upgrade, older Databricks runtime versions that do not support that table feature may be unable to write to the table. If the rewrite fails (`REWRITE_DATA_FAILED`), the command should be re-run. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Requirements and Constraints

### Table Type
IcebergCompatV can be enabled only on [managed tables](/concepts/managed-tables-in-databricks.md) (`REQUIRE_MANAGED_TABLE`). ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Deletion Vectors
The table must not have any [Deletion Vectors](/concepts/deletion-vectors.md) present. Two distinct error conditions apply:
- If deletion vectors are still enabled, they must first be disabled (`DELETION_VECTORS_SHOULD_BE_DISABLED`), after which a `REORG PURGE` command must be run to purge them.
- If deletion vectors are disabled but not yet purged, the purge must be completed (`DELETION_VECTORS_NOT_PURGED`), again using `REORG TABLE APPLY (PURGE)`. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Table Features
IcebergCompatV requires that certain Delta table features be both supported and enabled (`MISSING_REQUIRED_TABLE_FEATURE`). Conversely, it is incompatible with other features (`INCOMPATIBLE_TABLE_FEATURE`), and those incompatible features must not be present. A required feature cannot be dropped while IcebergCompatV is active (`DISABLING_REQUIRED_TABLE_FEATURE`); the IcebergCompat version must be disabled first. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Data Types
The schema of the table must not contain data types that are unsupported by the target IcebergCompat version. This applies both to regular columns (`UNSUPPORTED_DATA_TYPE`) and to partition columns (`UNSUPPORTED_PARTITION_DATA_TYPE`). ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Type Widening
A type change that widens an existing column (e.g., changing a field from `INT` to `BIGINT`) is incompatible with IcebergCompatV (`UNSUPPORTED_TYPE_WIDENING`). Such type changes must be reverted before the version can be enabled. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Schema Compatibility
When a table is created or converted to use IcebergCompatV, an Apache Iceberg schema compatibility check is performed. If the check fails, the error `SCHEMA_COMPATIBILITY_CHECK_FAILED` is raised with a specific reason. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Partition Spec Renaming
Replacing a partitioned table with a differently named partition spec is not allowed under IcebergCompatV, because Iceberg-Spark 1.1.0 does not support this operation (`REPLACE_TABLE_CHANGE_PARTITION_NAMES`). ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Required Table Properties
Certain table properties must have specific values. If a required property is set to a different value, the error `WRONG_REQUIRED_TABLE_PROPERTY` is raised, indicating the expected and current values. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### File-Level Compatibility
Enabling Uniform Iceberg with IcebergCompatV requires that all existing data files in the table be Apache Iceberg compatible. If concurrent writes have created incompatible files, the error `FILES_NOT_ICEBERG_COMPAT` appears. The remedy is to re-run the `REORG TABLE APPLY (UPGRADE UNIFORM)` command, which will rewrite the incompatible files. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Environment Support
The feature must be enabled in the current environment (`CONFIG_NOT_ENABLED`). ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Error Reference

The following table summarises the error subconditions for the `DELTA_ICEBERG_COMPAT_VIOLATION` error class (SQLSTATE KD00E):

| Error Subtype | Meaning |
|---------------|---------|
| `CHANGE_VERSION_NEED_REWRITE` | Changing to a different IcebergCompat version requires a table rewrite via `REORG`. |
| `COMPAT_VERSION_NOT_SUPPORTED` | The specified version is outside the supported range (1 to <maxVersion>). |
| `CONFIG_NOT_ENABLED` | IcebergCompatV<version> is not enabled in the environment. |
| `DELETION_VECTORS_NOT_PURGED` | Deletion vectors are disabled but not yet purged; run `REORG PURGE`. |
| `DELETION_VECTORS_SHOULD_BE_DISABLED` | Deletion vectors are still enabled; disable them first, then run `REORG PURGE`. |
| `DISABLING_REQUIRED_TABLE_FEATURE` | Cannot drop a required table feature; disable IcebergCompatV first. |
| `FILES_NOT_ICEBERG_COMPAT` | Some files are not Iceberg compatible; re-run the upgrade command. |
| `INCOMPATIBLE_TABLE_FEATURE` | A table feature is incompatible with IcebergCompatV. |
| `MISSING_REQUIRED_TABLE_FEATURE` | A required table feature is not enabled. |
| `REPLACE_TABLE_CHANGE_PARTITION_NAMES` | Cannot replace a partitioned table with a differently named partition spec. |
| `REQUIRE_MANAGED_TABLE` | IcebergCompatV is allowed only on managed tables. |
| `REWRITE_DATA_FAILED` | Data rewrite failed; re-run the upgrade command. |
| `SCHEMA_COMPATIBILITY_CHECK_FAILED` | Schema compatibility check with Iceberg failed. |
| `UNSUPPORTED_DATA_TYPE` | Unsupported data type in the column schema. |
| `UNSUPPORTED_PARTITION_DATA_TYPE` | Unsupported data type in partition columns. |
| `UNSUPPORTED_TYPE_WIDENING` | A type widening change is incompatible. |
| `VERSION_MUTUAL_EXCLUSIVE` | Only one IcebergCompat version can be enabled at a time. |
| `WRONG_REQUIRED_TABLE_PROPERTY` | A required table property has an incorrect value. |

^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Uniform Apache Iceberg](/concepts/uniform-apache-iceberg-format.md)
- Delta Lake Table Features
- [Deletion Vectors](/concepts/deletion-vectors.md)
- [Managed Tables](/concepts/managed-tables-in-databricks.md)
- [REORG TABLE](/concepts/reorg-table.md) (for upgrade and purge operations)

## Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
