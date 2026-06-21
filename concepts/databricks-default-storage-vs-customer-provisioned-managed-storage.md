---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9298a1c5f7ffa1a75b26da86b2c0b1fe08a84d9ea0e332f96cf989316a09fc02
  pageDirectory: concepts
  sources:
    - object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-default-storage-vs-customer-provisioned-managed-storage
    - DDSVCMS
    - Customer-Provided Managed Storage
  citations:
    - file: object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md
title: Databricks Default Storage vs Customer-Provisioned Managed Storage
description: "Two flavors of managed storage: Databricks-provisioned default storage and customer-provided cloud storage; same lifecycle but different billing and post-purge retention behavior."
tags:
  - unity-catalog
  - storage
  - billing
timestamp: "2026-06-19T19:49:08.262Z"
---

# Databricks Default Storage vs Customer-Provisioned Managed Storage

**Databricks Default Storage** and **Customer-Provisioned Managed Storage** are the two flavors of managed storage available for [Unity Catalog](/concepts/unity-catalog.md) managed tables and volumes. Both are controlled by Unity Catalog and share the same data file lifecycle after deletion, but they differ in billing responsibility and post-purge file retention. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Overview

Managed storage is storage that Unity Catalog provisions and manages. For managed tables and volumes (as opposed to external tables/volumes), the storage location is defined at the [Metastore](/concepts/metastore.md), catalog, or schema level. The two flavors are:

- **Databricks default storage**: Object storage that Databricks provisions and manages within your Databricks account.
- **Customer-provided managed storage**: A cloud storage location in your own cloud account (AWS, Azure, GCP), configured as a managed storage location in Unity Catalog. Databricks writes and manages data to this location.

Both types follow the same multi-phase lifecycle when a managed object is deleted, but billing and file retention after the purge phase differ. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Key Differences

| Aspect | Databricks Default Storage | Customer-Provisioned Managed Storage |
|--------|----------------------------|--------------------------------------|
| **Billing during recovery window (7 days)** | Databricks bills for storage. | Your cloud provider bills you directly. |
| **Billing after purge** | Databricks stops billing once the 7-day recovery window ends. | Your cloud provider may continue to bill you until you delete the files or adjust bucket lifecycle policies. |
| **Post-purge file retention** | Databricks permanently deletes the data files within 48 hours after the recovery window. | After the purge, the files remain in your cloud storage bucket unless your cloud provider’s versioning or soft-delete policies retain them. You are responsible for any ongoing charges. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md] |

## Shared Lifecycle After Deletion

When a managed table or volume is deleted (via Catalog Explorer or `DROP`), Unity Catalog does not immediately remove data files. The lifecycle has two phases:

1. **Recovery window (7 days)**: During this period, you can recover the object using the `UNDROP` SQL command. Databricks retains the soft-deleted metadata and data files, and storage billing (per the flavor above) continues. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]
2. **Purge (within 48 hours after the window ends)**: Unity Catalog permanently deletes the data files from cloud storage. For customer-provided storage, the deletion is performed by Databricks, but your cloud provider’s bucket policies (e.g., versioning, soft-delete) may keep copies that cause continued billing. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## External Tables and Volumes

This comparison applies only to *managed* objects. For external tables and volumes, you control the storage location and lifecycle. When you delete an external object, Unity Catalog removes only the metadata; the data files remain in your cloud storage and are not billed by Databricks. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that manages storage locations.
- [Managed vs External Assets](/concepts/managed-vs-external-assets-in-unity-catalog.md) – How managed and external objects differ in storage control.
- Default Storage in Databricks – What Databricks provisions as default storage.
- [Specify a Managed Storage Location](/concepts/managed-storage-location.md) – How to configure customer-provided managed storage.
- UNDROP – SQL command to recover deleted managed objects.

## Sources

- object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md

# Citations

1. [object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md](/references/object-storage-lifecycle-in-unity-catalog-databricks-on-aws-112fa332.md)
