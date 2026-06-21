---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0b97c329a5b81d3e415453ec82e792752f1b6e5f94d0c9609d279d96aa3bc4fc
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - schema-and-data-type-constraints-for-iceberg-compat
    - data type constraints for Iceberg compat and Schema
    - SADTCFIC
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: Schema and data type constraints for Iceberg compat
description: IcebergCompatV imposes restrictions on schema changes and data types, including unsupported data types, unsupported partition data types, type widening incompatibility, and partition spec rename restrictions.
tags:
  - delta-lake
  - iceberg-compatibility
  - schema-evolution
timestamp: "2026-06-19T10:06:24.519Z"
---

---
title: Schema and data type constraints for Iceberg compat
summary: IcebergCompatV imposes restrictions on the schema and data types of Delta tables, including unsupported types, partition column types, type widening, and schema compatibility checks.
sources:
  - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T12:00:00.000Z"
updatedAt: "2026-06-19T12:00:00.000Z"
tags:
  - iceberg
  - delta-lake
  - schema
  - data-type
aliases:
  - schema-and-data-type-constraints-for-iceberg-compat
  - SDTCIC
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Schema and data type constraints for Iceberg compat

**Schema and data type constraints for Iceberg compat** refer to the restrictions that [IcebergCompatV2](/concepts/icebergcompatv2.md) (and future versions) place on the schema and data types of a Delta table. When a table is configured with IcebergCompat, certain data types, partition column types, schema changes, and overall compatibility with the Apache Iceberg specification are validated. If a constraint is violated, a `DELTA_ICEBERG_COMPAT_VIOLATION` error is raised. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Unsupported data types

IcebergCompat does not support all data types that Delta supports. If a table schema contains a data type that is not supported by the target IcebergCompat version, the error `UNSUPPORTED_DATA_TYPE` is returned. The error includes the offending data type and the full schema. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Unsupported partition data types

Similarly, partition columns have their own restriction: IcebergCompat does not support certain data types for partition columns. The error `UNSUPPORTED_PARTITION_DATA_TYPE` identifies the unsupported type and the partition schema. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Type widening incompatibility

IcebergCompat is incompatible with type changes applied to the table after IcebergCompat was enabled. Specifically, the error `UNSUPPORTED_TYPE_WIDENING` occurs when a field has been changed from a narrower type (`<prevType>`) to a wider type (`<newType>`). This is because Iceberg does not allow such type widening without a full rewrite. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Schema compatibility check failure

When creating a table or converting an existing table to use IcebergCompat, a schema compatibility check against the Apache Iceberg specification is performed. If this check fails, the error `SCHEMA_COMPATIBILITY_CHECK_FAILED` is raised with a reason explaining the failure. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Related constraints

Additional non‑schema constraints that may appear alongside data‑type issues include:

- **Required table features**: IcebergCompat requires certain table features (e.g., `Deletion Vectors` disabled, `Managed Table` only). Errors like `REQUIRE_MANAGED_TABLE` and `MISSING_REQUIRED_TABLE_FEATURE` can block enabling IcebergCompat. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]
- **Deletion Vectors**: If Deletion Vectors are present, the errors `DELETION_VECTORS_NOT_PURGED` or `DELETION_VECTORS_SHOULD_BE_DISABLED` must be resolved by disabling and purging Deletion Vectors before enabling IcebergCompat. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]
- **Table property requirements**: Certain table properties must be set to specific values; otherwise, `WRONG_REQUIRED_TABLE_PROPERTY` is raised. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Resolution steps

When a schema or data‑type constraint is violated, the recommended action depends on the error:

- For `UNSUPPORTED_DATA_TYPE` or `UNSUPPORTED_PARTITION_DATA_TYPE`, alter the schema to remove or replace the unsupported type.
- For `UNSUPPORTED_TYPE_WIDENING`, revert the type change or rewrite the table using `REORG TABLE APPLY (UPGRADE UNIFORM ...)`.
- For `SCHEMA_COMPATIBILITY_CHECK_FAILED`, adjust the schema to match the Iceberg specification based on the reason provided.
- For issues that require rewriting data, run `REORG TABLE APPLY (UPGRADE UNIFORM (ICEBERG_COMPAT_VERSION=<version>))` again after fixing the underlying problem. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Related concepts

- [Delta Uniform](/concepts/delta-uniform.md) – The feature that provides Iceberg compatibility.
- [IcebergCompatV2](/concepts/icebergcompatv2.md) – Specific version of Iceberg compatibility.
- DELTA_ICEBERG_COMPAT_V1_VIOLATION|DELTA_ICEBERG_COMPAT_VIOLATION – Full list of error sub‑conditions.
- [REORG TABLE](/concepts/reorg-table.md) – Command used to upgrade Uniform and purge Deletion Vectors.
- [Deletion Vectors](/concepts/deletion-vectors.md) – A Delta table feature that must be disabled/purged for IcebergCompat.

## Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
