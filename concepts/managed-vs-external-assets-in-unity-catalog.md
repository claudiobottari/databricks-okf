---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e3ae3ccb1d02e3c0c72d799091ffd4bcacf3eaff34194019c8985004b5597bc2
  pageDirectory: concepts
  sources:
    - object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - managed-vs-external-assets-in-unity-catalog
    - MVEAIUC
    - Managed versus external assets
    - Managed vs External Assets
  citations:
    - file: object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md
title: Managed vs External Assets in Unity Catalog
description: Fundamental distinction between managed objects (Unity Catalog controls storage lifecycle) and external objects (user controls storage and lifecycle) in Unity Catalog.
tags:
  - unity-catalog
  - storage
  - data-governance
timestamp: "2026-06-19T19:49:11.449Z"
---

# Managed vs External Assets in Unity Catalog

**Managed vs External Assets in Unity Catalog** describes how [Unity Catalog](/concepts/unity-catalog.md) handles the storage location and data file lifecycle for tables and [volume|volumes](/concepts/ucvolumedataset-and-ucvolumewriter.md), based on whether the asset is classified as *managed* or *external*. The distinction determines what happens to the underlying data files when the asset is deleted, how storage is billed, and who controls the storage location. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Overview

For tables and volumes, the storage type (managed vs external) governs the behavior of the underlying data files upon deletion. All other securable objects (catalogs, schemas, views, functions, models) contain only metadata – deletion removes the metadata with no associated data files to manage. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Managed Assets

A **managed table** or **managed volume** exists in a storage location that Unity Catalog controls. The data files reside in the managed storage location defined at the [Metastore](/concepts/metastore.md), catalog, or schema level. When you delete a managed table or volume, Unity Catalog removes the underlying data files through a multi-phase lifecycle (recovery window then purge). ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

Managed storage comes in two flavors:

- **Databricks default storage**: Object storage that Databricks provisions and manages in your Databricks account.
- **Customer-provided managed storage**: A cloud storage location in your cloud account, configured at the [Metastore](/concepts/metastore.md), catalog, or schema level, that Databricks writes and manages data to.

Both flavors share the same data file lifecycle, but billing and post‑deletion file retention differ. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## External Assets

An **external table** or **external volume** is backed by a storage location that you control. Unity Catalog holds only the metadata (schema, location pointer). When you delete an external table or volume, Unity Catalog removes the metadata from the [Metastore](/concepts/metastore.md), but the data files remain untouched in your cloud storage location. You are responsible for deleting those files directly using your cloud provider's tools. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Foreign and Federated Catalogs

[Foreign catalog|Foreign](/concepts/foreign-iceberg-table-sharing.md) and federated catalog|federated catalogs store data in an external data source (e.g., a federated database through Lakehouse Federation, or a Hive [Metastore](/concepts/metastore.md) through [Hive Metastore Federation](/concepts/hive-metastore-federation.md)). Unity Catalog holds only the connection metadata. Deleting the foreign catalog removes that metadata; data in the source system is unaffected. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Lifecycle After Deletion

### Managed Assets

Deleting a managed table or volume triggers a two‑phase lifecycle:

1. **Recovery window (7 days)**: Unity Catalog retains the soft‑deleted data. You can recover the object using the `UNDROP` SQL command (for tables, materialized views, and streaming tables). Storage billing continues during this window.
2. **Purge (within 48 hours after the recovery window ends)**: Unity Catalog permanently deletes the data files. The object can no longer be recovered.

^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

### External Assets

No data lifecycle applies. Delete removes only the metadata. The data files persist in your storage bucket and continue to accrue cloud provider charges according to the bucket’s policies. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Storage Billing

| Scenario | Billing during recovery window | Billing after purge/delete |
|---|---|---|
| Managed – Databricks default storage | Databricks bills for storage | Databricks stops billing |
| Managed – Customer-provided storage | Your cloud provider bills you | Your cloud provider may still bill if files remain (e.g., due to versioning or lifecycle policies) |
| External table/volume | Your cloud provider bills you | Your cloud provider continues to bill for the data files |

^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Recovering Deleted Objects

- **Managed table, materialized view, streaming table**: Use `UNDROP` within the 7‑day recovery window.
- **External table/volume**: Recovery is not possible through Unity Catalog because the metadata was removed. You can re‑register the files as a new external table if the data still exists in storage.
- **Catalog or schema dropped with `CASCADE`**: The contained objects follow their own managed‑or‑external behavior. Recovery is best‑effort and time‑limited.

^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Managed storage location](/concepts/managed-storage-location.md)
- External Table
- Volume
- Foreign Catalog
- Federated Catalog
- UNDROP
- DROP TABLE
- DROP VOLUME
- Data Billing in Unity Catalog

## Sources

- object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md

# Citations

1. [object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md](/references/object-storage-lifecycle-in-unity-catalog-databricks-on-aws-112fa332.md)
