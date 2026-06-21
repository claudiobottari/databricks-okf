---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e9405df02b6241bb4a1aed61464f64e4d432370832fcf206c930fcbd5f07831a
  pageDirectory: concepts
  sources:
    - manage-unity-catalog-metastores-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metastore-storage-root-removal
    - MSRR
    - Metastore Storage Root
  citations:
    - file: manage-unity-catalog-metastores-databricks-on-aws.md
title: Metastore Storage Root Removal
description: The process of removing the metastore-level storage root to enforce catalog- or schema-level data isolation, which pushes the root location down to existing catalogs and requires new catalogs to specify their own storage location.
tags:
  - unity-catalog
  - storage
  - data-isolation
timestamp: "2026-06-19T19:28:56.759Z"
---

# [Metastore](/concepts/metastore.md) Storage Root Removal

**Metastore Storage Root Removal** is the process of removing the metastore-level managed storage location from a [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md). This operation enforces data storage isolation at the catalog or schema level, requiring each new catalog to provide its own dedicated storage location.

## Overview

Metastore-level managed storage (the [Metastore](/concepts/metastore.md) storage root) is an optional configuration that stores managed table and volume data in a central S3 bucket for all workspaces attached to the [Metastore](/concepts/metastore.md). When a [Metastore](/concepts/metastore.md) is created automatically, this storage root is not included. An account admin can later add it, but removing it is a deliberate choice to enforce stricter data isolation. ^[manage-unity-catalog-metastores-databricks-on-aws.md]

## Effects of Removal

When you remove the [Metastore](/concepts/metastore.md) storage root, the following consequences apply:

- **Existing catalogs without a storage root**: These catalogs are automatically assigned the former [Metastore](/concepts/metastore.md) storage root’s cloud storage location as their catalog-level managed storage location. Access to data in these catalogs continues without interruption. ^[manage-unity-catalog-metastores-databricks-on-aws.md]
- **External location creation**: If no external location securable object was defined in Unity Catalog for the [Metastore](/concepts/metastore.md) storage root, a new external location and associated storage credential are created automatically. The new external location is named `prior_metastore_root_location` by default. ^[manage-unity-catalog-metastores-databricks-on-aws.md]
- **Future catalogs**: Every time a user creates a new catalog, they **must** provide a dedicated storage location that is registered in Unity Catalog as an [External location](/concepts/external-location.md). ^[manage-unity-catalog-metastores-databricks-on-aws.md]

### OpenSharing Notebook Consideration

If you use [OpenSharing](/concepts/opensharing.md) (via [Delta Sharing](/concepts/delta-sharing.md)) to share notebooks and you previously used the [Metastore](/concepts/metastore.md) root as shared notebook storage, you must take the following steps **before** removing the [Metastore](/concepts/metastore.md) root:

1. Remove the notebook from the share.
2. Re-add the notebook using a dedicated storage location.

^[manage-unity-catalog-metastores-databricks-on-aws.md]

## Procedure

To remove the [Metastore](/concepts/metastore.md) storage root:

1. As an account admin, log in to the [account console](https://accounts.cloud.databricks.com/).
2. Click the **Catalog** icon.
3. Click the [Metastore](/concepts/metastore.md) name.
4. On the **Configuration** tab, under **S3 bucket path**, click the **Remove** button.
5. On the confirmation dialog, click **Remove**.

^[manage-unity-catalog-metastores-databricks-on-aws.md]

> **Note:** The S3 bucket path cannot be modified once set, but you can remove it and add a new path if necessary. ^[manage-unity-catalog-metastores-databricks-on-aws.md]

## Related Concepts

- [Metastore Storage Root](/concepts/metastore-storage-root-removal.md) — The optional central storage location for managed tables and volumes in a [Metastore](/concepts/metastore.md).
- [Managed storage location](/concepts/managed-storage-location.md) — Storage configured at the [Metastore](/concepts/metastore.md), catalog, or schema level for managed objects.
- [External location](/concepts/external-location.md) — A securable object in Unity Catalog representing a cloud storage path.
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution on Databricks.
- [Catalog](/concepts/unity-catalog.md) — A top-level container in Unity Catalog’s three-level namespace.
- Schema — The second level in the three-level namespace.
- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for sharing data across platforms.

## Sources

- manage-unity-catalog-metastores-databricks-on-aws.md

# Citations

1. [manage-unity-catalog-metastores-databricks-on-aws.md](/references/manage-unity-catalog-metastores-databricks-on-aws-6a5c164f.md)
