---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1eb6a34732e89998b5fc99a34c03cba4f04d6906a9bb091a19db1bf915a4ed37
  pageDirectory: concepts
  sources:
    - managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - managed-vs-external-volumes-in-unity-catalog
    - MVEVIUC
  citations:
    - file: managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md
    - file: managed-versous-external-assets-in-unity-catalog-databricks-on-aws.md
title: Managed vs External volumes in Unity Catalog
description: Distinction between volumes where Unity Catalog determines the storage location and manages file lifecycle versus volumes where the user specifies the storage location
tags:
  - unity-catalog
  - volumes
  - databricks
timestamp: "2026-06-19T19:29:42.161Z"
---

# Managed vs External Volumes in Unity Catalog

In Unity Catalog, all registered securable objects are centrally governed. For data assets such as tables and volumes, Unity Catalog can additionally control the storage location and lifecycle of the underlying data files in your cloud account. This distinction defines **managed** vs **external** assets. The following focuses on volumes, but the same principles apply to tables. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

## Key Distinction

- **Managed volume**: Unity Catalog controls both governance (access control, auditing, lineage) and the underlying file storage lifecycle (file organization, optimization, and deletion). The storage location is automatically determined by the managed storage location defined on the containing schema, catalog, or [Metastore](/concepts/metastore.md). ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

- **External volume**: Unity Catalog controls governance only. You specify the storage location, which must be a path covered by a Unity Catalog [External location](/concepts/external-location.md). The underlying file lifecycle is controlled by you or an external system. When the volume is dropped, Unity Catalog removes the volume definition but the underlying data files remain in place. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

## Managed Volumes

A Unity Catalog managed volume is stored in the managed storage location of its containing schema within your cloud account. You retain full ownership of the underlying data at all times — the data always remains in your cloud account and is never transferred to Databricks. When you drop a managed volume, Unity Catalog deletes the underlying data files. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

## External Volumes

An external volume is created by specifying a storage location that is covered by a Unity Catalog external location. You control the file lifecycle (optimization, organization, deletion). Dropping an external volume removes only the metadata from the [Metastore](/concepts/metastore.md); the data files at the specified location are not touched. ^[managed-versous-external-assets-in-unity-catalog-databricks-on-aws.md]

## Summary Table

| Aspect | Managed Volume | External Volume |
|--------|----------------|----------------|
| Governance (access, audit, lineage) | Unity Catalog | Unity Catalog |
| Storage location determined by | Unity Catalog (managed storage location of schema/catalog/[Metastore](/concepts/metastore.md)) | You (must be a path covered by an external location) |
| File lifecycle (optimization, organization, deletion) | Unity Catalog | You or external system |
| Data dropped with volume? | Yes – data files are deleted | No – only metadata is removed; data files remain |

*Source: This table synthesizes information from the source document.* ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

## Uses of the Word "Manage"

The word *manage* appears in three distinct contexts across Unity Catalog:

1. **Governance**: When an object is said to be "managed by Unity Catalog," it means Unity Catalog governs its access. This applies to all registered objects, including external volumes.
2. **Managed vs External**: The specific term *managed volume* means Unity Catalog determines the storage location and controls the file lifecycle.
3. **`MANAGE` privilege**: A permission level that allows a user to assign or revoke privileges, transfer ownership, or delete an object without being the owner. This is unrelated to managed storage.

^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Securable Objects](/concepts/unity-catalog-securable-objects.md)
- External locations in Unity Catalog
- [Managed vs External tables in Unity Catalog](/concepts/managed-vs-external-tables-in-unity-catalog.md)
- [What are Unity Catalog volumes?](/concepts/databricks-utilities-with-unity-catalog-volumes.md)
- Databricks cloud account storage
- [MANAGE Privilege](/concepts/manage-privilege.md)

## Sources

- managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md

# Citations

1. [managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md](/references/managed-versus-external-assets-in-unity-catalog-databricks-on-aws-581e1fb1.md)
2. managed-versous-external-assets-in-unity-catalog-databricks-on-aws.md
