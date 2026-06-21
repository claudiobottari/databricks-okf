---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9d54c420c2d872240e3dc4c3d35bacfcf309b82a7fc291144aef43fa57a23617
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - required-table-features-and-properties-for-iceberg-compat
    - properties for Iceberg compat and Required table features
    - RTFAPFIC
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: Required table features and properties for Iceberg compat
description: IcebergCompatV requires specific table features to be enabled and specific table properties to be set to particular values; disabling required features or misconfiguring properties triggers violation errors.
tags:
  - delta-lake
  - iceberg-compatibility
  - table-properties
timestamp: "2026-06-19T10:06:42.935Z"
---

# Required Table Features and Properties for Iceberg Compat

**Required Table Features and Properties for Iceberg Compat** refers to the set of constraints that a [Delta Lake](/concepts/delta-lake.md) table must satisfy when enabling or operating with [IcebergCompatV](/concepts/icebergcompatv.md) (e.g., `IcebergCompatV1`, `IcebergCompatV2`). These requirements are enforced by Databricks to ensure interoperability with [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) via the Uniform Iceberg format, and violations produce the `DELTA_ICEBERG_COMPAT_VIOLATION` error. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Required Table Features

IcebergCompat requires that certain Delta table features are **enabled** and **cannot be dropped**. If a required feature is missing, the error `MISSING_REQUIRED_TABLE_FEATURE` is raised; if an attempt is made to disable a required feature, the error `DISABLING_REQUIRED_TABLE_FEATURE` is raised. Conversely, some features are **incompatible** with IcebergCompat and must be absent (error `INCOMPATIBLE_TABLE_FEATURE`). ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

The source material lists the following specific feature-related errors:

| Error Subclass | Meaning |
|----------------|---------|
| `MISSING_REQUIRED_TABLE_FEATURE` | IcebergCompat requires feature `<feature>` to be supported and enabled. |
| `DISABLING_REQUIRED_TABLE_FEATURE` | The user tried to drop a feature that IcebergCompat depends on; disable IcebergCompat first. |
| `INCOMPATIBLE_TABLE_FEATURE` | IcebergCompatV`<version>` is incompatible with feature `<feature>`. |

### Deletion Vectors

[Deletion Vectors](/concepts/deletion-vectors.md) are a table feature that may need to be **disabled and purged** depending on the IcebergCompat version. Specifically:

- `DELETION_VECTORS_NOT_PURGED`: IcebergCompatV`<version>` requires Deletion Vectors to be completely purged from the table. Run `REORG TABLE APPLY (PURGE)`. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]
- `DELETION_VECTORS_SHOULD_BE_DISABLED`: IcebergCompatV`<version>` requires Deletion Vectors to be disabled on the table first, then purge with `REORG PURGE`. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Required Table Properties

IcebergCompat enforces specific values for certain table properties. The error `WRONG_REQUIRED_TABLE_PROPERTY` indicates that a property must be set to a specific value:

```
IcebergCompatV<version> requires table property '<key>' to be set to '<requiredValue>'. Current value: '<actualValue>'.
```

^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

This means that when enabling IcebergCompat, the table must have the correct configuration for properties such as `delta.icebergCompatVersion` or related settings. The exact key-value pairs depend on the target version. Failure to match them will prevent the operation.

## Managed Table Requirement

IcebergCompat can only be enabled on [Managed Tables](/concepts/managed-tables-in-databricks.md) in Unity Catalog or the Hive [Metastore](/concepts/metastore.md). The error `REQUIRE_MANAGED_TABLE` states: "The feature can be enabled only on Managed Tables." External tables or tables backed by external locations are not supported for IcebergCompat. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Schema Compatibility

The source material lists several schema-related constraints that IcebergCompat imposes:

- **Unsupported data types**: `UNSUPPORTED_DATA_TYPE` — IcebergCompat does not support the data type `<dataType>` in the table schema. All columns must use types that are compatible with Apache Iceberg. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]
- **Unsupported partition data types**: `UNSUPPORTED_PARTITION_DATA_TYPE` — Partition columns must also use supported types. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]
- **Type widening forbidden**: `UNSUPPORTED_TYPE_WIDENING` — IcebergCompat is incompatible with type changes that widen an existing column (e.g., from `<prevType>` to `<newType>`). ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]
- **Schema compatibility check fails**: `SCHEMA_COMPATIBILITY_CHECK_FAILED` — The Apache Iceberg schema compatibility check failed during table creation or conversion, with a provided reason. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### File-Level Compatibility

When enabling Uniform Apache Iceberg with IcebergCompat, all existing data files must be Apache Iceberg compatible. The error `FILES_NOT_ICEBERG_COMPAT` indicates that some files are not compatible, often due to concurrent writes. Running `REORG TABLE APPLY (UPGRADE UNIFORM ...)` again is recommended. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Version Management

Only one IcebergCompat version can be enabled at a time. The error `VERSION_MUTUAL_EXCLUSIVE` states: "Only one IcebergCompat version can be enabled, please explicitly disable all other IcebergCompat versions that are not needed." ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

If an attempt is made to change the version, the error `CHANGE_VERSION_NEED_REWRITE` requires rewriting the table using `REORG TABLE APPLY (UPGRADE UNIFORM ('ICEBERG_COMPAT_VERSION = <newVersion>'))`. Note that the new version may not be supported by all Databricks runtime versions for writing. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

Additionally, `COMPAT_VERSION_NOT_SUPPORTED` indicates that the specified IcebergCompatVersion is outside the supported range (between 1 and `<maxVersion>`). ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Resolving Violations

Most violations are resolved by running the appropriate `REORG TABLE` command. The source material suggests:

- `REORG TABLE APPLY (PURGE)` — to purge Deletion Vectors.
- `REORG TABLE APPLY (UPGRADE UNIFORM (ICEBERG_COMPAT_VERSION=<version>))` — to upgrade the table to the desired IcebergCompat version.
- For missing required features, enable the feature explicitly before enabling IcebergCompat.
- For incompatible features, disable those features or consider a different IcebergCompat version.
- For unsupported data types or type widening, revise the table schema to be Iceberg-compatible.

## Related Concepts

- [IcebergCompatV](/concepts/icebergcompatv.md) – The table feature that enables Uniform Iceberg format.
- [Deletion Vectors](/concepts/deletion-vectors.md) – A Delta table feature that may need to be manipulated.
- [Uniform Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – The interoperability layer between Delta and Iceberg.
- [Managed Tables](/concepts/managed-tables-in-databricks.md) – The required table type for IcebergCompat.
- [REORG TABLE](/concepts/reorg-table.md) – The command used to resolve many compat violations.
- Delta Table Properties – Configure table behavior.
- Schema Evolution – Limitations on type changes when IcebergCompat is on.
- DELTA_ICEBERG_COMPAT_V1_VIOLATION|DELTA_ICEBERG_COMPAT_VIOLATION – The error class covering all these subclasses.

## Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
