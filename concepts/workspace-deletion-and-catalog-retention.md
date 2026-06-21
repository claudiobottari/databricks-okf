---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2e49dd75cd492d7160b8d4d3c11401b9111259aeb8d36725a24dd3ee972eac0d
  pageDirectory: concepts
  sources:
    - object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workspace-deletion-and-catalog-retention
    - Catalog Retention and Workspace Deletion
    - WDACR
  citations:
    - file: object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md
title: Workspace Deletion and Catalog Retention
description: Deleting a Databricks workspace does not automatically delete its default Unity Catalog catalog; the catalog must be dropped manually from another workspace assigned to the same metastore.
tags:
  - unity-catalog
  - workspace
  - deletion
timestamp: "2026-06-19T19:49:21.818Z"
---

# Workspace Deletion and Catalog Retention

**Workspace Deletion and Catalog Retention** describes the default behavior when a Databricks workspace is deleted: the workspace's default Unity Catalog catalog is **not** automatically deleted. This retention behavior has implications for data lifecycle management, storage billing, and ongoing governance responsibilities.

## Default Behavior

By default, deleting a workspace does **not** automatically delete the workspace's default Unity Catalog catalog. If the catalog is retained, its managed tables and volumes remain in place. Storage billing for those objects continues until the catalog is explicitly dropped.^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Manual Cleanup Required

Because the catalog is not removed with the workspace, it must be dropped manually after workspace deletion. To drop the catalog, a user must do so from another workspace that is assigned to the same [Metastore](/concepts/metastore.md).^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

For more details about the workspace deletion process itself, see Delete a workspace.

## Data Lifecycle After Catalog Deletion

When the retained catalog is eventually dropped (either manually or through a `DROP CATALOG` statement), the contained objects are handled according to their type:

- **Managed tables and volumes**: Follow the standard multi-phase lifecycle: a 7-day recovery window during which `UNDROP` is possible, followed by permanent deletion of data files.
- **External tables and volumes**: Only metadata is removed; data files remain in the customer's cloud storage.
- **Foreign and federated catalogs**: Only connection metadata is removed; data in the source system is unaffected.^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Storage Billing Implications

- **Databricks default storage**: Storage billing continues for managed objects on Databricks default storage as long as the catalog is retained. Billing stops only after the 7-day recovery window following a `DROP` passes.
- **Customer-provided managed storage**: Your cloud provider continues to bill you directly for managed storage until the data files are deleted (either through the Unity Catalog lifecycle or by your own bucket policies).^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Securable Objects](/concepts/unity-catalog-securable-objects.md)
- [Managed versus external assets](/concepts/managed-vs-external-assets-in-unity-catalog.md)
- Object storage lifecycle in Unity Catalog
- UNDROP command
- DROP CATALOG
- Delete a workspace
- Default storage in Databricks

## Sources

- object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md

# Citations

1. [object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md](/references/object-storage-lifecycle-in-unity-catalog-databricks-on-aws-112fa332.md)
