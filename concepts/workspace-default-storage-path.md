---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0a87e603276fc2bbb51b5c7a2e3f75913c7fbf51c9235e93c473f21c75e8ed2e
  pageDirectory: concepts
  sources:
    - resolve-storage-path-conflicts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workspace-default-storage-path
    - WDSP
    - Default Storage
    - Default storage
    - default storage
  citations:
    - file: resolve-storage-path-conflicts-databricks-on-aws.md
title: Workspace default storage path
description: The default storage path configured for a Databricks workspace during deployment using a storage configuration object, used for internal Unity Catalog processing.
tags:
  - unity-catalog
  - workspace-configuration
  - storage
timestamp: "2026-06-19T20:14:02.856Z"
---

# Workspace default storage path

The **workspace default storage path** is the root cloud storage location that a Databricks workspace uses as its default [Unity Catalog](/concepts/unity-catalog.md) managed storage. It is configured during classic workspace deployment by creating a *storage configuration* object that points to a cloud bucket (for example, `s3://<your-bucket>/<region>/`). ^[resolve-storage-path-conflicts-databricks-on-aws.md]

## Relation to external locations

Unity Catalog validates [external locations](/concepts/external-location.md) against every storage configuration registered to the Databricks account, not just the workspace where the location was created. A **storage path conflict** occurs when an external location path overlaps with (is broader than or equal to) the workspace default storage path of any workspace in the same account. For example:

- **Workspace default storage path:** `s3://<your-bucket>/<region>/`
- **Conflicting external location:** `s3://<your-bucket>/`

This overlap interferes with Unity Catalog’s internal processing and weakens data governance because internal workspace data stored under the default path could be exposed through the external location. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

## Non-conflicting paths

An external location can be created on **more specific paths** under a workspace’s default storage path without causing a conflict, provided those paths do not overlap with the internal Unity Catalog storage structure. For instance, the [DBFS root location](/concepts/dbfs-root-location.md) is a sibling of the workspace’s internal storage path and does not create a conflict. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

## Resolving conflicts

When a conflict exists, you must update the external location configuration. Two common scenarios are described in the source:

1. **External location at a broad path (e.g., `s3://<bucket>/`) but data is in a specific sibling folder** – Update the external location to a more specific sibling path (e.g., `s3://<bucket>/<region>/<workspace-id>/`). This resolves the conflict without moving data and also prevents accidental leakage of workspace internal data. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

2. **Managed tables stored directly under the root bucket path** – If the external location is at the root and managed tables already exist under it (e.g., `s3://<bucket>/__unity_storage/...`), you cannot simply change the path. You must open a support ticket with Databricks Support to migrate the managed data to a new location and restore the [Metastore](/concepts/metastore.md) to a non-conflicting state. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

## Related concepts

- [External location](/concepts/external-location.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [DBFS root location](/concepts/dbfs-root-location.md)
- Storage configuration object
- Classic workspace deployment

## Sources

- resolve-storage-path-conflicts-databricks-on-aws.md

# Citations

1. [resolve-storage-path-conflicts-databricks-on-aws.md](/references/resolve-storage-path-conflicts-databricks-on-aws-74a353cf.md)
