---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 72d59eb9003f184794e0dc02f6bcf40919a03846f5db9f173bc638cf4f3b9f0e
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - icebergcompatv-versioning-in-delta-lake
    - IVIDL
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
      start: 24
      end: 25
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
      start: 5
      end: 6
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
      start: 2
      end: 4
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
      start: 18
      end: 19
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
      start: 27
      end: 28
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
      start: 10
      end: 11
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
      start: 14
      end: 15
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
      start: 7
      end: 9
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
      start: 12
      end: 13
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
      start: 22
      end: 23
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
      start: 26
      end: 27
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
      start: 20
      end: 21
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
      start: 16
      end: 17
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
      start: 1
      end: 28
title: IcebergCompatV versioning in Delta Lake
description: A versioned compatibility feature in Databricks Delta Lake that enforces Apache Iceberg compatibility rules; only one version can be enabled at a time and versions range from 1 to a configurable maxVersion.
tags:
  - delta-lake
  - iceberg
  - compatibility
  - databricks
timestamp: "2026-06-19T18:25:27.404Z"
---

# IcebergCompatV Versioning in Delta Lake

**IcebergCompatV versioning** is a mechanism in Delta Lake that ensures a Delta table is compatible with the [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) format. Each version of IcebergCompat imposes specific requirements on table properties, supported data types, and enabled table features.

## Overview

When a Delta table has the [IcebergCompatV](/concepts/icebergcompatv.md) feature enabled (e.g., `IcebergCompatV1`, `IcebergCompatV2`), the table can be read by Iceberg readers. The version number determines which set of compatibility rules apply. Only one IcebergCompat version can be active on a table at any time. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md:24-25] (from `VERSION_MUTUAL_EXCLUSIVE`)

## Versioning Rules

- **Supported version range**: The version must be an integer between 1 and the maximum supported version for the Databricks runtime. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md:5-6] (from `COMPAT_VERSION_NOT_SUPPORTED`)
- **Single active version**: You cannot enable multiple IcebergCompat versions simultaneously. Before changing versions, you must disable all other IcebergCompat versions. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md:24-25]
- **Version upgrade requires rewrite**: Changing to a different IcebergCompat version requires rewriting the table using `REORG TABLE APPLY (UPGRADE UNIFORM ('ICEBERG_COMPAT_VERSION = <newVersion>'))`. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md:2-4] (from `CHANGE_VERSION_NEED_REWRITE`)

## Requirements and Constraints

- **Managed tables only**: The IcebergCompatV feature can only be enabled on managed (not external) tables. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md:18-19] (from `REQUIRE_MANAGED_TABLE`)
- **Required table properties**: Certain table properties must have specific values when an IcebergCompat version is enabled. If a property is incorrect, the error `WRONG_REQUIRED_TABLE_PROPERTY` occurs. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md:27-28] (from that section)
- **Required table features**: Each IcebergCompat version may require specific Delta table features (e.g., `AppendOnly`, `Invariants`). You cannot drop a feature that is required by the active IcebergCompat version. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md:10-11] (from `DISABLING_REQUIRED_TABLE_FEATURE`)
- **Incompatible features**: Some table features are incompatible with IcebergCompatV. If they are enabled on the table, the error `INCOMPATIBLE_TABLE_FEATURE` is raised. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md:14-15] (from that section)
- **Deletion Vectors must be purged**: Before enabling IcebergCompatV, any existing [Deletion Vectors](/concepts/deletion-vectors.md) must be purged from the table using `REORG TABLE APPLY (PURGE)`. If Deletion Vectors are still enabled, you must disable them first. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md:7-9] (from `DELETION_VECTORS_NOT_PURGED` and `DELETION_VECTORS_SHOULD_BE_DISABLED`)
- **File-level compatibility**: All existing data files must be Apache Iceberg compatible. If concurrent writes create files without the required Iceberg tags, the table must be rewritten using `REORG TABLE APPLY (UPGRADE UNIFORM ...)`. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md:12-13] (from `FILES_NOT_ICEBERG_COMPAT`)

## Data Type and Schema Constraints

- **Unsupported data types**: Some Delta data types cannot be used in tables with IcebergCompatV enabled, both for regular columns and for partition columns. If an unsupported type is present, the errors `UNSUPPORTED_DATA_TYPE` or `UNSUPPORTED_PARTITION_DATA_TYPE` are raised. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md:22-23] (from those sections)
- **Type widening incompatibility**: IcebergCompatV is incompatible with type changes (type widening) applied to the table’s schema. The error `UNSUPPORTED_TYPE_WIDENING` is returned when a field’s type has been changed. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md:26-27] (from that section)
- **Schema compatibility check**: When creating a new table or converting an existing one to use IcebergCompatV, the Iceberg schema compatibility check must pass. If it fails, the reason is provided in the `SCHEMA_COMPATIBILITY_CHECK_FAILED` error. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md:20-21] (from that section)
- **Partition spec restrictions**: Replacing a partitioned table with a differently-named partition spec is not supported because Iceberg-Spark 1.1.0 does not support it. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md:16-17] (from `REPLACE_TABLE_CHANGE_PARTITION_NAMES`)

## Error Handling

All violations of IcebergCompatV versioning rules raise the error class `DELTA_ICEBERG_COMPAT_VIOLATION` with a sub‑error providing more detail. Common sub‑errors include `VERSION_MUTUAL_EXCLUSIVE`, `COMPAT_VERSION_NOT_SUPPORTED`, `DELETION_VECTORS_NOT_PURGED`, `FILES_NOT_ICEBERG_COMPAT`, and `WRONG_REQUIRED_TABLE_PROPERTY`. Most errors suggest rerunning `REORG TABLE` with the appropriate options to fix the issue. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md:1-28]

## Related Concepts

- [Uniform (Apache Iceberg)](/concepts/uniform-apache-iceberg-format.md) — The broader feature that makes Delta tables readable as Iceberg tables.
- [REORG TABLE](/concepts/reorg-table.md) — The command used to upgrade, purge, or rewrite tables for Iceberg compatibility.
- [Deletion Vectors](/concepts/deletion-vectors.md) — A Delta table feature that must be disabled or purged before enabling IcebergCompatV.
- [Delta Lake table features](/concepts/delta-lake-reader-table-features.md) — The system of optional features that IcebergCompatV may require or conflict with.
- [Managed tables](/concepts/managed-tables-in-databricks.md) — The only table type that can have IcebergCompatV enabled.

## Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md:24-25](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
2. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md:5-6](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
3. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md:2-4](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
4. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md:18-19](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
5. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md:27-28](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
6. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md:10-11](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
7. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md:14-15](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
8. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md:7-9](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
9. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md:12-13](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
10. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md:22-23](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
11. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md:26-27](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
12. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md:20-21](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
13. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md:16-17](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
14. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md:1-28](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
