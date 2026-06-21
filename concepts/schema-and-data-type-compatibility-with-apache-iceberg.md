---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5f44ad96bd7a54b6d28b75edfea137eca462435d9aa35f554f68ca74c689e3f0
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - schema-and-data-type-compatibility-with-apache-iceberg
    - Data Type Compatibility with Apache Iceberg and Schema
    - SADTCWAI
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: Schema and Data Type Compatibility with Apache Iceberg
description: IcebergCompatV imposes restrictions on supported data types and schema changes, including unsupported data types, partition data types, and type widening that are incompatible with Apache Iceberg.
tags:
  - delta-lake
  - apache-iceberg
  - schema-evolution
  - data-types
timestamp: "2026-06-18T11:54:17.933Z"
---

# Schema and Data Type Compatibility with Apache Iceberg

Enabling **IcebergCompatV** on a Delta table requires the table’s schema and data types to satisfy Apache Iceberg’s compatibility rules. When a schema change or type configuration violates those rules, Databricks raises a `DELTA_ICEBERG_COMPAT_VIOLATION` error with a specific sub‑condition. Understanding these constraints helps you plan schema evolution and table conversions to [Uniform Apache Iceberg](/concepts/uniform-apache-iceberg-format.md).

## Schema Compatibility Check

During table creation or conversion to an Iceberg‑compatible format, Databricks performs an Apache Iceberg schema compatibility check. If the Delta schema cannot be represented in Iceberg’s type system, the operation fails with:

`SCHEMA_COMPATIBILITY_CHECK_FAILED` — reason: `<reason>`. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Unsupported Data Types

Not all Delta data types are supported by Apache Iceberg. If a column in the table schema uses a type that Iceberg does not support, the error includes the `UNSUPPORTED_DATA_TYPE` sub‑condition. The error message lists the offending type and the full schema. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

Similarly, partition columns that use an unsupported data type trigger `UNSUPPORTED_PARTITION_DATA_TYPE`, which reports the partition schema and the unsupported type. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Unsupported Type Widening

IcebergCompatV is incompatible with certain type changes (widening) that are allowed in Delta Lake. If a field’s data type was changed from a narrower type to a wider type—for example, from `INT` to `BIGINT`—and that change is not supported by Iceberg, the `UNSUPPORTED_TYPE_WIDENING` sub‑condition is raised. The error identifies the field path and the old and new types. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Additional Schema‑Related Constraints

- **Deletion Vectors**: IcebergCompatV requires Deletion Vectors to be purged or disabled. The sub‑conditions `DELETION_VECTORS_NOT_PURGED` and `DELETION_VECTORS_SHOULD_BE_DISABLED` guide the remediation steps. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]
- **Required table features**: Enabling IcebergCompatV may require certain table features (e.g., `DELETION_VECTORS` must be disabled). The `MISSING_REQUIRED_TABLE_FEATURE` and `DISABLING_REQUIRED_TABLE_FEATURE` conditions indicate when a required feature is missing or must be prevented from being dropped. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]
- **Incompatible table features**: If the table already has a feature that conflicts with IcebergCompatV, `INCOMPATIBLE_TABLE_FEATURE` is raised. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]
- **Replacing partitioned tables**: IcebergCompatV does not support replacing a partitioned table with a differently‑named partition spec (due to Iceberg‑Spark 1.1.0 limitations). The `REPLACE_TABLE_CHANGE_PARTITION_NAMES` sub‑condition applies. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]
- **Managed tables only**: IcebergCompatV can only be enabled on managed Delta tables. External tables trigger `REQUIRE_MANAGED_TABLE`. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]
- **Required table property**: A specific table property may need to be set to a required value. The `WRONG_REQUIRED_TABLE_PROPERTY` sub‑condition identifies the property and the required value. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Remediation

Most schema‑related errors are resolved by either adjusting the Delta schema to meet Iceberg’s requirements or by running a `REORG TABLE APPLY (UPGRADE UNIFORM ...)` command. Consult the specific sub‑condition’s error message for the exact steps. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [IcebergCompatV](/concepts/icebergcompatv.md) — The compatibility version enforced during conversion
- [Uniform Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The feature that makes Delta tables readable as Iceberg tables
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format
- [REORG TABLE](/concepts/reorg-table.md) — The command used to upgrade Uniform format and purge incompatible features
- [Deletion Vectors](/concepts/deletion-vectors.md) — A Delta feature that must be handled before enabling IcebergCompatV

## Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
