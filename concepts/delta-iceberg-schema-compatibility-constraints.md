---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c7f7076af31eae380e3dfd2803ae00d9736c1bdb137f5699331f99eda8d66c6d
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-iceberg-schema-compatibility-constraints
    - DSCC
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: Delta-Iceberg Schema Compatibility Constraints
description: A set of restrictions on Delta table schemas when using IcebergCompatV, including unsupported data types, partition column types, and schema evolution rules.
tags:
  - delta-lake
  - apache-iceberg
  - schema
  - compatibility
timestamp: "2026-06-18T15:20:15.669Z"
---

# Delta-Iceberg Schema Compatibility Constraints

**Delta-Iceberg Schema Compatibility Constraints** are the structural and type-level rules that [Delta Lake](/concepts/delta-lake.md) enforces when a table has the `IcebergCompatV<version>` table feature enabled (commonly used with [Uniform Apache Iceberg](/concepts/uniform-apache-iceberg-format.md)). These constraints ensure that the Delta table’s schema remains compatible with Apache Iceberg’s stricter type system and partition semantics, preventing silent data corruption or read failures in Iceberg readers. When a constraint is violated, Delta Lake raises a `DELTA_ICEBERG_COMPAT_VIOLATION` error (SQLSTATE KD00E). ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Why Schema Constraints Are Needed

Apache Iceberg does not support every data type or schema evolution operation that Delta Lake allows. For example, Iceberg has a narrower set of supported column types and stricter rules about type widening. When `IcebergCompatV<version>` is enabled, Delta Lake must reject write or conversion operations that would produce a schema that Iceberg cannot represent – otherwise, downstream Iceberg readers would encounter failures or undefined behavior. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Schema-Related Constraint Violations

The following subsections describe the schema-specific error conditions that fall under `DELTA_ICEBERG_COMPAT_VIOLATION`. Each condition is triggered by a specific incompatibility between the Delta table’s schema and Iceberg’s requirements.

### Unsupported Data Types (`UNSUPPORTED_DATA_TYPE`)

`IcebergCompatV<version>` does not support certain Delta data types. If the table schema contains an unsupported type, enabling the feature or writing to the table fails. The error message includes the offending type and the full schema. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Unsupported Partition Data Types (`UNSUPPORTED_PARTITION_DATA_TYPE`)

Even if a column type is supported as a regular column, it may be unsupported as a partition column in Iceberg. This constraint checks that all partition columns in the table use types that Iceberg can handle. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Unsupported Type Widening (`UNSUPPORTED_TYPE_WIDENING`)

Schema evolution that widens a column’s type (e.g., `INT` → `LONG`) must be compatible with Iceberg’s type promotion rules. If a type change violates Iceberg’s allowed widening paths, Delta Lake rejects the change and reports the field path, previous type, and new type. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Schema Compatibility Check Failed (`SCHEMA_COMPATIBILITY_CHECK_FAILED`)

During table creation or conversion (e.g., `REORG TABLE APPLY (UPGRADE UNIFORM ...)`), Delta Lake runs a full schema compatibility check against Iceberg’s rules. If the check fails, the operation is blocked and the reason is provided. This is a catch-all for structural incompatibilities that are not captured by the more specific errors above. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Replace Table Change Partition Names (`REPLACE_TABLE_CHANGE_PARTITION_NAMES`)

IcebergCompatV does not support replacing a partitioned table with a differently‑named partition spec, because the underlying Iceberg-Spark library (version 1.1.0) does not support this operation. The error includes the previous and new partition specifications. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Other Non-Schema Constraints

While the focus of this page is schema compatibility, `IcebergCompatV<version>` also enforces non‑schema constraints that can cause `DELTA_ICEBERG_COMPAT_VIOLATION` errors. These include:

- **Deletion Vectors** must be disabled and purged before enabling the feature.^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

- **Required table features** (e.g., `DELETION_VECTORS`, `ROW_LEVEL_SECURITY`) must either be enabled or absent, depending on the IcebergCompat version.^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

- The table must be a **managed table** (`REQUIRE_MANAGED_TABLE`).^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

- Only one IcebergCompat version can be enabled at a time (`VERSION_MUTUAL_EXCLUSIVE`).^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

- Certain table properties must be set to specific values (`WRONG_REQUIRED_TABLE_PROPERTY`).^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Resolution

Most schema-related violations are resolved by either:

1. **Modifying the schema** to remove unsupported types or undo incompatible type widenings.
2. **Running `REORG TABLE APPLY (UPGRADE UNIFORM ('ICEBERG_COMPAT_VERSION = <version>'))`** after the schema is made compatible. This command rewrites the table metadata and enables the required table features.

For the full list of `DELTA_ICEBERG_COMPAT_VIOLATION` sub‑conditions and their exact error messages, refer to the official error class documentation.^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Uniform Apache Iceberg](/concepts/uniform-apache-iceberg-format.md)
- [IcebergCompatV2](/concepts/icebergcompatv2.md)
- [Delta Lake Schema Evolution](/concepts/delta-lake-schema-migration.md)
- [REORG TABLE](/concepts/reorg-table.md)
- DELTA_ICEBERG_COMPAT_VIOLATION error class|DELTA_ICEBERG_COMPAT_VIOLATION Error Class

## Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
