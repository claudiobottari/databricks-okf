---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cdc84851ec7ccabf7e64c24e3d11b31a7e0b5e81ccf2bdc418cc39580fdcae05
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-uniform-managed-table-requirement
    - DMTR
    - icebergcompatv-managed-table-requirement
    - IMR
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: Delta-Uniform Managed Table Requirement
description: The IcebergCompatV feature can only be enabled on managed Delta tables, not external or unmanaged tables.
tags:
  - delta-lake
  - databricks
  - table-management
timestamp: "2026-06-18T15:20:29.211Z"
---

# Delta-Uniform Managed Table Requirement

**Delta-Uniform Managed Table Requirement** refers to the constraint that the [Delta Uniform](/concepts/delta-uniform.md) (IcebergCompatV`<version>`) feature can be enabled only on [managed tables](/concepts/managed-tables-in-databricks.md) in Unity Catalog. This requirement is enforced by Databricks at creation time or when converting an existing table.

## Overview

Delta-Uniform (also known as Uniform or IcebergCompat) allows Delta tables to be read by Apache Iceberg clients by publishing Iceberg metadata. To activate this feature using the `ALTER TABLE ... SET TBLPROPERTIES` command or the `REORG TABLE APPLY (UPGRADE UNIFORM ...)` command, the target table must be a managed table. External tables (tables whose data is stored in a location not managed by Unity Catalog) cannot have Delta-Uniform enabled. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## Enforcement

When a user attempts to enable `IcebergCompatVersion` on a table that is not managed, Databricks raises the `DELTA_ICEBERG_COMPAT_VIOLATION` error class with the sub‑condition `REQUIRE_MANAGED_TABLE`. The error message states: ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

> The feature can be enabled only on Managed Tables.

## Related Requirements

In addition to the managed‑table requirement, Delta-Uniform activation imposes other conditions that are validated collectively. The `DELTA_ICEBERG_COMPAT_VIOLATION` error class includes sub‑conditions for:

- `DELETION_VECTORS_NOT_PURGED` – Deletion vectors must be purged before activation.
- `FILES_NOT_ICEBERG_COMPAT` – All existing files must be Iceberg‑compatible.
- `SCHEMA_COMPATIBILITY_CHECK_FAILED` – The table schema must satisfy Iceberg compatibility rules.
- `UNSUPPORTED_DATA_TYPE` – Certain Delta data types are not supported.
- `UNSUPPORTED_TYPE_WIDENING` – Type widening after table creation may block activation.
- `VERSION_MUTUAL_EXCLUSIVE` – Only one IcebergCompat version can be enabled at a time.
- `WRONG_REQUIRED_TABLE_PROPERTY` – Specific table properties must have the correct values.

These requirements are checked during `SET TBLPROPERTIES` or `REORG` operations and each generates the corresponding sub‑error if violated. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

## How to Satisfy the Managed Table Requirement

To enable Delta-Uniform on a table, ensure the table is managed. Managed tables are defined with the `MANAGED LOCATION` clause (or implicitly created in the metastore’s root location) and are fully governed by Unity Catalog. If the target table is currently an external table, it must be converted to a managed table (e.g., by using `ALTER TABLE ... SET TBLPROPERTIES` to change the table type) before Delta-Uniform can be enabled.

For the full set of steps to activate Delta-Uniform, see the documentation on Enabling Uniform on Delta tables.

## Related Concepts

- [Delta-Uniform (IcebergCompat)](/concepts/delta-uniform-with-icebergcompat.md)
- [Managed tables vs external tables](/concepts/managed-vs-external-tables-in-unity-catalog.md)
- DELTA_ICEBERG_COMPAT_VIOLATION error class
- [REORG TABLE - UPGRADE UNIFORM](/concepts/reorg-table-apply-upgrade-uniform.md)
- IcebergCompatV1 and V2

## Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
