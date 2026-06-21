---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b82bf679f9a517fd622ae2c3dfbaf12d0b7bd45f80a1517458af7f4585393d3a
  pageDirectory: concepts
  sources:
    - object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - storage-billing-after-object-deletion
    - SBAOD
  citations:
    - file: object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md
title: Storage Billing After Object Deletion
description: Databricks bills for default storage only during the 7-day recovery window; for customer-provided storage the cloud provider bills directly and charges may persist based on bucket policies.
tags:
  - unity-catalog
  - billing
  - storage
timestamp: "2026-06-19T19:49:26.835Z"
---

# Storage Billing After Object Deletion

**Storage Billing After Object Deletion** describes how Databricks and cloud providers charge for storage when a Unity Catalog securable object (table, volume, catalog, schema, etc.) is deleted. The billing behavior depends on the object type (managed or external), the storage type (Databricks default or customer‑provided), and the phase of the data lifecycle at the time of deletion. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Overview

When a Unity Catalog object is deleted, the underlying data files are handled according to the object’s storage type. Billing for that storage follows from the storage type and the object’s lifecycle phase. The two principal phases are the **recovery window** (7 days after deletion) and the **purge** (within 48 hours after the recovery window ends). ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Billing by Storage Type

### Managed objects on Databricks default storage

Databricks controls the storage location and data lifecycle. During the 7‑day recovery window, Databricks continues to bill for the storage of the soft‑deleted data. Once the recovery window ends and the data is purged (within 48 hours), Databricks storage billing stops. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

### Managed objects on customer‑provided managed storage

The data lifecycle is the same as for Databricks default storage (recovery window, then purge), but the billing differs. Databricks does not bill for storage on customer‑provided managed storage. Your cloud provider bills you directly for the underlying cloud storage. After deletion, you might still see storage charges from your cloud provider; these depend on the bucket’s object versioning, soft‑delete, and lifecycle policies. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

### External tables and volumes

When you delete an external table or external volume, Unity Catalog removes only the metadata from the [Metastore](/concepts/metastore.md). The data files remain in your cloud storage location and are **not** deleted by Databricks. Your cloud provider continues to bill you for the storage according to your bucket’s policies. To stop billing, you must delete the files directly from cloud storage. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

### Foreign and federated catalogs

A foreign catalog holds only connection metadata to an external data source (such as a federated database or Hive [Metastore](/concepts/metastore.md)). Deleting a foreign catalog removes only the connection metadata; the data in the source system is unaffected. Databricks does not bill for storage in the source system — the source system’s own billing applies. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Recovery Window and Purge Impact

For managed objects, the 7‑day recovery window is the only period during which Databricks default storage billing is active. After the recovery window expires, data is purged within 48 hours, and storage billing from Databricks stops. During the recovery window, you can use the UNDROP SQL command to recover the object. Storage billing continues during that window because the data files are still retained. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Workspace Deletion

By default, deleting a workspace does **not** automatically delete the workspace’s default Unity Catalog catalog. If the catalog is retained, its managed tables and volumes remain, and storage billing continues until the catalog is dropped manually from another workspace in the same [Metastore](/concepts/metastore.md). ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Summary Table

The source includes a summary table that cross‑references each phase and storage type. Key takeaways:
- Databricks bills for storage only on Databricks default storage and only during the recovery window.
- For customer‑provided managed storage and external storage, the cloud provider bills directly.
- After the recovery window, Databricks storage billing ends.

## Related Concepts

- [Managed vs External Assets in Unity Catalog](/concepts/managed-vs-external-assets-in-unity-catalog.md)
- Default storage in Databricks
- UNDROP
- [Recovery window](/concepts/recovery-window-and-undrop.md)
- Lifecycle of managed data after deletion
- Delete a workspace

## Sources

- object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md

# Citations

1. [object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md](/references/object-storage-lifecycle-in-unity-catalog-databricks-on-aws-112fa332.md)
