---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e07156c258f5ec17627a2053d5ab0d00c57b7fd32002cc2bc981d1a243af652a
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - schema-and-type-compatibility-between-delta-and-iceberg
    - Type Compatibility Between Delta and Iceberg and Schema
    - SATCBDAI
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: Schema and Type Compatibility Between Delta and Iceberg
description: Constraints on schema changes and data types when enabling IcebergCompatV, including unsupported data types, unsupported partition data types, and incompatibility with type widening.
tags:
  - delta-lake
  - apache-iceberg
  - schema-evolution
  - data-types
timestamp: "2026-06-19T15:05:56.992Z"
---

---
title: Schema and Type Compatibility Between Delta and Iceberg
summary: Constraints and error conditions for schema and data type compatibility when using Delta Lake with Apache Iceberg via IcebergCompatV
sources:
  - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T15:00:00.000Z"
updatedAt: "2026-06-19T15:00:00.000Z"
tags:
  - delta-lake
  - apache-iceberg
  - schema-compatibility
  - data-types
  - error-conditions
aliases:
  - delta-iceberg-schema-compatibility
  - iceberg-type-compatibility
  - delta-iceberg-type-widening
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Schema and Type Compatibility Between Delta and Iceberg

When enabling [Uniform Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) on a [Delta Lake](/concepts/delta-lake.md) table via `IcebergCompatV<version>`, Databricks validates that the Delta schema and data types are compatible with Apache Iceberg’s type system. If the validation fails, the `DELTA_ICEBERG_COMPAT_VIOLATION` error class is raised with a specific sub‑error. This page documents the schema‑ and type‑related sub‑errors that can occur.

## Schema Compatibility Check

During table creation or conversion to an Iceberg‑compatible format, Apache Iceberg performs its own schema compatibility check. If that check fails, the system returns the sub‑error `SCHEMA_COMPATIBILITY_CHECK_FAILED` with the reason provided by Iceberg. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Unsupported Data Types

IcebergCompatV`<version>` does not support all Delta data types. If the table schema contains a data type that is not supported by the target Iceberg version, the `UNSUPPORTED_DATA_TYPE` sub‑error is raised, listing the offending data type and the full schema. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Unsupported Partition Column Data Types

Partition columns are also subject to type restrictions. If a partition column uses a data type that IcebergCompatV`<version>` cannot handle, the `UNSUPPORTED_PARTITION_DATA_TYPE` sub‑error is raised with the partition schema. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Type Widening Incompatibility

IcebergCompatV`<version>` is incompatible with **type widening** — a schema evolution operation that changes a column’s data type to a wider type (e.g., `INT` to `BIGINT`). If such a change has been applied to the table, the `UNSUPPORTED_TYPE_WIDENING` sub‑error is raised, identifying the field path and the previous and new data types. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Partition Name Changes

Replacing a partitioned table with a differently‑named partition spec is not supported because Iceberg‑Spark 1.1.0 does not allow it. The `REPLACE_TABLE_CHANGE_PARTITION_NAMES` sub‑error is raised, showing the previous and new partition specs. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Related Error Conditions

Other `DELTA_ICEBERG_COMPAT_VIOLATION` sub‑errors address non‑schema issues that can arise during Iceberg compatibility validation:

- `MISSING_REQUIRED_TABLE_FEATURE` – a required table feature (e.g., [Deletion Vectors](/concepts/deletion-vectors.md)) is not enabled.
- `INCOMPATIBLE_TABLE_FEATURE` – a table feature is incompatible with IcebergCompatV.
- `DISABLING_REQUIRED_TABLE_FEATURE` – attempting to drop a feature that IcebergCompatV requires to be enabled.
- `WRONG_REQUIRED_TABLE_PROPERTY` – a table property must be set to a specific value.
- `FILES_NOT_ICEBERG_COMPAT` – some data files are not Iceberg‑compatible.
- `CHANGE_VERSION_NEED_REWRITE` – upgrading to a new IcebergCompat version requires rewriting the table.

For a full list of sub‑errors and recommended recovery steps (such as `REORG TABLE APPLY (UPGRADE UNIFORM …)` or `REORG TABLE APPLY (PURGE)`), see the DELTA_ICEBERG_COMPAT_V1_VIOLATION|DELTA_ICEBERG_COMPAT_VIOLATION error class reference. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md)
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md)
- [IcebergCompatV](/concepts/icebergcompatv.md)
- [Uniform Apache Iceberg](/concepts/uniform-apache-iceberg-format.md)
- Schema Evolution
- [Deletion Vectors](/concepts/deletion-vectors.md)
- Table Features
- [REORG TABLE](/concepts/reorg-table.md)

## Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
