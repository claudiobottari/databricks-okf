---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: af7212c9b0eeba6e8c227f3c658f54f16a82eb5ab0e1d34cef6c5b933df94383
  pageDirectory: concepts
  sources:
    - resolve-storage-path-conflicts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - conflict-resolution-by-data-migration
    - CRBDM
  citations:
    - file: resolve-storage-path-conflicts-databricks-on-aws.md
title: Conflict resolution by data migration
description: Resolution strategy for storage path conflicts where data must be physically moved because managed tables exist directly under the root bucket path that conflicts with the workspace default storage path.
tags:
  - unity-catalog
  - troubleshooting
  - storage
  - data-migration
timestamp: "2026-06-19T20:14:44.789Z"
---

# Conflict Resolution by Data Migration

**Conflict resolution by data migration** refers to the process of resolving [storage path conflicts](/concepts/storage-path-conflict.md) in [Unity Catalog](/concepts/unity-catalog.md) by moving managed data to a new, non-conflicting storage location. This approach is required when an external location path overlaps with a workspace's default Unity Catalog storage path and the conflict cannot be resolved by simply updating the external location path. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

## When Data Migration Is Required

A storage path conflict occurs when an external location overlaps with the default Unity Catalog storage path of any workspace in your Databricks account. This overlap interferes with the internal processing of certain Unity Catalog features. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

Data migration is specifically required in **Scenario B**, where managed tables are stored directly at the root bucket location that conflicts with a workspace default storage path. For example:

- **Workspace default storage path:** `s3://<your-bucket>/<region>/`
- **Overlapping external location:** `s3://<your-bucket>/`
- **Managed table location (under conflict):** `s3://<your-bucket>/__unity_storage/catalogs/<catalog_id>/tables/<table_id>`

In this scenario, updating the external location path is not possible because the managed data already exists at the root bucket level. The data must be moved to a new location. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

## The Migration Process

When data migration is required, you must open a support ticket with Databricks Support. The support team can help you:

1. Migrate your managed data to a new storage location that does not conflict with any workspace default storage path.
2. Restore your [Metastore](/concepts/metastore.md) to a non-conflicting state.

^[resolve-storage-path-conflicts-databricks-on-aws.md]

## Comparison with Alternative Resolution

| Resolution Method | When Applicable | Action |
|---|---|---|
| **Path update (no data move)** | External location can be narrowed to a more specific path that does not overlap. Data is accessed from a sibling folder. | Update the external location to a more specific path (e.g., from `s3://<your-bucket>/` to `s3://<your-bucket>/<region>/<workspace-id>/`). |
| **Data migration** | Managed tables are stored at the root bucket location that conflicts. Path update is not possible. | Open a support ticket with Databricks Support to migrate managed data and restore the [Metastore](/concepts/metastore.md). |

^[resolve-storage-path-conflicts-databricks-on-aws.md]

## Why Migration Is Necessary

A storage path conflict prevents Unity Catalog from using the workspace storage location for internal processing and blocks certain Unity Catalog functionality. Additionally, the overlap weakens data governance because internal workspace data could be exposed by the external location. Consequently, external location paths must not overlap with any workspace default Unity Catalog storage path in your account. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

## Related Concepts

- [Storage path conflict](/concepts/storage-path-conflict.md) — The underlying issue that may require resolution by data migration.
- [External location](/concepts/external-location.md) — The Unity Catalog object that can cause conflicts with workspace storage paths.
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that validates external locations against workspace storage configurations.
- [Managed Tables](/concepts/managed-tables-in-databricks.md) — Tables whose data may need to be migrated to resolve path conflicts.
- Workspace Storage Configuration — The default storage path assigned during workspace deployment.

## Sources

- resolve-storage-path-conflicts-databricks-on-aws.md

# Citations

1. [resolve-storage-path-conflicts-databricks-on-aws.md](/references/resolve-storage-path-conflicts-databricks-on-aws-74a353cf.md)
