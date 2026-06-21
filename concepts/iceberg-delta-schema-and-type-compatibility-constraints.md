---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ab819d4fecc38f863208cfc205acf04485975260b766d92a1a7d54eff10dea9b
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - iceberg-delta-schema-and-type-compatibility-constraints
    - type compatibility constraints and Iceberg-Delta schema
    - ISATCC
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: Iceberg-Delta schema and type compatibility constraints
description: IcebergCompatV imposes restrictions on schema changes, including unsupported data types for columns and partition columns, incompatibility with type widening, and a requirement that partition specs cannot be renamed during REPLACE TABLE operations.
tags:
  - delta-lake
  - iceberg
  - schema
  - databricks
  - data-types
timestamp: "2026-06-19T18:25:41.827Z"
---

# Iceberg-Delta Schema and Type Compatibility Constraints

**Iceberg-Delta schema and type compatibility constraints** are a set of validation rules enforced when enabling the `IcebergCompatV<version>` table feature on a [Delta Lake Table](/concepts/delta-lake-table.md). These constraints ensure that the Delta table's schema, data types, partition columns, and type evolution history are compatible with the target Apache Iceberg format. Violations result in a `DELTA_ICEBERG_COMPAT_VIOLATION` error with a specific sub‑condition. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Schema Compatibility

When creating a table with IcebergCompat enabled, or when converting an existing Delta table to a Uniform Iceberg table, the schema must pass an Apache Iceberg compatibility check. The error condition `SCHEMA_COMPATIBILITY_CHECK_FAILED` indicates that the schema, in its current form, is not representable in Iceberg. The error includes a `<reason>` message explaining the failure. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Unsupported Data Types

`IcebergCompatV<version>` does not accept every data type that Delta Lake supports. Two error sub‑conditions cover this:

- **`UNSUPPORTED_DATA_TYPE`** – The schema contains a `<dataType>` that is not supported by the target Iceberg version. The full table schema is included in the error message. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

- **`UNSUPPORTED_PARTITION_DATA_TYPE`** – A column used in the partition schema has an unsupported `<dataType>`. The partition schema is shown in the error. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Type Widening Restrictions

IcebergCompat is incompatible with certain type‑evolution operations. The error `UNSUPPORTED_TYPE_WIDENING` occurs when a field has undergone a type change (for example, from `<prevType>` to `<newType>`) that is not allowed under the Iceberg compatibility version. This constraint prevents the table from being enabled for Uniform Iceberg until the type change is resolved. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Partition Spec Renaming

`IcebergCompatV<version>` does not support replacing an existing partitioned table with a differently named partition spec. This limitation stems from Iceberg‑Spark 1.1.0, which does not handle renamed partition specifications. The error `REPLACE_TABLE_CHANGE_PARTITION_NAMES` is raised when a `REPLACE TABLE` operation attempts to change partition column names on a table that has IcebergCompat enabled. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- IcebergCompat – The table feature that enables Delta tables to be read as Apache Iceberg tables.
- [Uniform Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) – The overall feature that provides Iceberg compatibility through the Delta `uniform` table property.
- [Delta Lake schema enforcement](/concepts/delta-table-schema-requirements.md) – Delta’s native schema validation, which interacts with these Iceberg compatibility checks.
- [Deletion Vectors](/concepts/deletion-vectors.md) – A related feature that must be purged or disabled before enabling certain IcebergCompat versions.
- [REORG TABLE](/concepts/reorg-table.md) – The command used to upgrade Uniform Iceberg compatibility or purge incompatible data.

## Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
