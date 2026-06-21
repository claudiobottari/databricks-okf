---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e128eaacab9e46f2210a0603dc759760f264eebb17f21742434770569a7748f6
  pageDirectory: concepts
  sources:
    - object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-and-foreign-object-deletion-behavior
    - Foreign Object Deletion Behavior and External
    - EAFODB
  citations:
    - file: object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md
title: External and Foreign Object Deletion Behavior
description: Deleting external tables/volumes removes metadata but leaves data files intact in cloud storage; deleting foreign/federated catalogs removes connection metadata without affecting source data.
tags:
  - unity-catalog
  - deletion
  - external-data
timestamp: "2026-06-19T19:49:17.291Z"
---

# External and Foreign Object Deletion Behavior

**External and Foreign Object Deletion Behavior** describes what happens to the underlying data when you delete externals tables, external volumes, foreign catalogs, or federated catalogs in Unity Catalog. Unlike managed objects, Deleting these objects removes only the metadata from the [Metastore](/concepts/metastore.md); the actual data in the source system is unaffected. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## External Tables and Volumes

When you delete an external table or an external volume, Unity Catalog removes the metadata from the [Metastore](/concepts/metastore.md). The data files in your cloud storage location are **not** deleted. Your cloud provider continues to bill you for that storage according to your bucket’s policies. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

If you wish to free that storage, you must delete the files directly from your cloud storage location (e.g., using your cloud provider’s console or CLI). ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Foreign and Federated Catalogs

A foreign catalog contains metadata that references an external data source (such as a federated database through Lakehouse Federation, or a Hive [Metastore](/concepts/metastore.md) through [Hive Metastore Federation](/concepts/hive-metastore-federation.md)). Unity Catalog holds only the connection metadata for these catalogs. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

When you delete a foreign catalog, Unity Catalog removes the connection metadata. The data in the source system is unaffected. Databricks does not bill you for storage in the source system; the source system’s own billing applies. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Recovery

Recovery of a deleted object is time-limited and best-effort, and the approach depends on the object type. For external tables, volumes, and foreign catalogs, the data remains in the external source, so you could re-register it by creating a new external table or catalog pointing to the same location. The source documentation does not describe a specific `UNDROP` command for external or foreign objects. ^[object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Managed vs External Assets in Unity Catalog](/concepts/managed-vs-external-assets-in-unity-catalog.md)
- Managed table deletion behavior
- [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md)
- [Hive Metastore Federation](/concepts/hive-metastore-federation.md)
- UNDROP command
- [Catalog Explorer](/concepts/catalog-explorer.md)

## Sources

- object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md

# Citations

1. [object-storage-lifecycle-in-unity-catalog-databricks-on-aws.md](/references/object-storage-lifecycle-in-unity-catalog-databricks-on-aws-112fa332.md)
