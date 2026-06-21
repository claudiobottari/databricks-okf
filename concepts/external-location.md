---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dd3bbe6871833cca1302887bbc1b4e101e3f94ace92c7a09cefce58603a84a33
  pageDirectory: concepts
  sources:
    - resolve-storage-path-conflicts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-location
    - External Locations
    - External Use Location
    - External locations
    - S3 External Location
    - external locations
    - Assign an external location to specific workspaces
    - Cloudflare R2 external location setup
    - Create an external location
    - External Location Binding
  citations:
    - file: resolve-storage-path-conflicts-databricks-on-aws.md
title: External location
description: A Unity Catalog object that defines a cloud storage path and its access credentials, which must not overlap with any workspace's default storage path in the same account.
tags:
  - unity-catalog
  - storage
  - data-governance
timestamp: "2026-06-19T20:14:04.239Z"
---

# External Location

An **external location** is a [Unity Catalog](/concepts/unity-catalog.md) object that registers a cloud storage path (e.g., an Amazon S3 bucket or prefix) for data access within a Databricks workspace. It defines a root path that can be used to create external tables, manages data governance, and controls access to that storage.

## Storage Path Conflicts

A storage path conflict occurs when an external location overlaps with the default Unity Catalog storage path of any workspace in your Databricks account. The default workspace storage path is configured during workspace deployment via a storage configuration object (e.g., `s3://<your-bucket>/<region>/`). If an external location is created or updated at a broader path (e.g., `s3://<your-bucket>/`), it overlaps with the internal workspace storage location. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

Such an overlap interferes with Unity Catalog internal processing, blocks certain functionality, and weakens data governance because internal workspace data could be exposed by the external location. Unity Catalog validates external locations against every storage configuration registered to the account, not just the workspace where the location was created. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

However, creating an external location on *more specific* paths *under* a workspace default storage path (such as a [DBFS root location](/concepts/dbfs-root-location.md)) is allowed because those paths are siblings of the workspace’s internal storage path and do not create a conflict. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

## How to Resolve

If a conflict exists, the external location configuration must be updated. Two common scenarios are described in the source material.

### Scenario A: External location updates without moving data

If an external location is defined at a broad path (e.g., `s3://<customer-bucket>/`) but only needs to access data in a more specific sibling folder (e.g., legacy DBFS data at `s3://<customer-bucket>/<region>/<workspace-id>/`), the recommended action is to update the external location to the more specific path. This resolves the conflict while continuing to allow access to all required data and prevents accidental leakage of workspace internal data. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

### Scenario B: Managed tables stored at the root bucket location

If managed tables have been created directly under the root bucket (e.g., `s3://<your-bucket>/__unity_storage/...`) via the broad external location, the path cannot be changed without moving the data. In this case, the user must open a support ticket with Databricks Support so the support team can migrate the managed data to a new location and restore the [Metastore](/concepts/metastore.md) to a non‑conflicting state. ^[resolve-storage-path-conflicts-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) and governance layer for Databricks data assets.
- Storage configuration – The object that defines the default storage path for a workspace.
- [DBFS root location](/concepts/dbfs-root-location.md) – A legacy Databricks File System location that is a sibling of internal workspace storage.
- Cloud storage – The underlying S3 bucket or blob store where data resides.
- External table – A table whose data resides in an external location.

## Sources

- resolve-storage-path-conflicts-databricks-on-aws.md

# Citations

1. [resolve-storage-path-conflicts-databricks-on-aws.md](/references/resolve-storage-path-conflicts-databricks-on-aws-74a353cf.md)
