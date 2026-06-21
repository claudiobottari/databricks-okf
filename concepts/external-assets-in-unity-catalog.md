---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 79ade204b7fc0df7ecd8daa7f08ec9ed8d275bed0ee8da6ef74359899788817d
  pageDirectory: concepts
  sources:
    - managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-assets-in-unity-catalog
    - EAIUC
    - External Locations in Unity Catalog
    - External locations in Unity Catalog
  citations:
    - file: managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md
title: External assets in Unity Catalog
description: Data assets (tables and volumes) where Unity Catalog controls governance only and the file storage lifecycle is controlled by the user
tags:
  - unity-catalog
  - data-governance
  - databricks
timestamp: "2026-06-19T19:29:05.783Z"
---

# External assets in Unity Catalog

**External assets** are data assets (tables and volumes) registered in Unity Catalog where Unity Catalog controls governance (access control, auditing, and lineage), but the storage location and lifecycle of the underlying data files are managed by you or an external system. This contrasts with [managed assets](/concepts/managed-assets-in-unity-catalog.md), where Unity Catalog also controls the file storage lifecycle. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

## Key characteristics

- Unity Catalog governs the object’s metadata but does **not** manage the physical storage or file lifecycle.
- You specify the storage location for the underlying data files (for external tables) or must choose a path covered by a Unity Catalog external location (for external volumes).
- When you drop an external asset, Unity Catalog removes the object’s metadata from the [Metastore](/concepts/metastore.md), but the underlying data files **remain in place** in your cloud account. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]
- External assets support multiple formats, including Delta, CSV, JSON, Avro, Parquet, and ORC (for tables). ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

## External tables

An **external table** in Unity Catalog is a table where you explicitly specify the storage location for the underlying data files. You retain full control over those files. When the external table is dropped, only the table metadata is deleted; the data files remain. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

External tables can use a variety of file formats (e.g., Delta, CSV, JSON, Avro, Parquet, ORC). For more information about table types, see Unity Catalog table types. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

## External volumes

An **external volume** is a volume where you specify the storage location. The location must be a path covered by a Unity Catalog [External location](/concepts/external-location.md). When the external volume is dropped, Unity Catalog removes the volume definition, but the underlying data files remain. For more information about volumes, see Unity Catalog volumes. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

## Comparison with managed assets

| Aspect | Managed assets | External assets |
|--------|----------------|-----------------|
| Governance (access, audit, lineage) | Controlled by Unity Catalog | Controlled by Unity Catalog |
| File storage location | Determined by Unity Catalog (managed storage location) | Specified by you |
| File lifecycle (optimization, organization, deletion) | Controlled by Unity Catalog | Controlled by you or external system |
| Behavior when dropped | Unity Catalog deletes the underlying data files | Unity Catalog removes metadata only; data files remain |

The distinction between managed and external applies only to **tables and volumes**. Other Unity Catalog securable objects (views, models, functions) do not have managed and external variants. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

## The word "manage" in different contexts

The word *manage* has multiple meanings across Unity Catalog:

- **Governance manage**: All registered objects, including external assets, are *managed by Unity Catalog* in the sense that Unity Catalog governs access to them.
- **Storage lifecycle manage**: *Managed tables* and *managed volumes* have the specific meaning that Unity Catalog determines where the underlying data files are stored and controls their lifecycle. External assets do **not** have this property.
- **`MANAGE` privilege**: A permission level (`MANAGE`) that allows a user to assign or revoke privileges, transfer ownership, or delete an object without being the owner. This is unrelated to external assets. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

## Access from external engines

Both managed and external tables support read, write, and create access from external engines via open APIs such as the Unity REST API and the Iceberg REST Catalog (IRC). External assets do not cause vendor lock-in. See Access Databricks data using external systems. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

## Related concepts

- [Managed assets in Unity Catalog](/concepts/managed-assets-in-unity-catalog.md)
- Unity Catalog table types
- [External location](/concepts/external-location.md)
- Unity Catalog volumes
- [Securable objects in Unity Catalog](/concepts/securable-objects-in-unity-catalog.md)
- [Unity Catalog governance](/concepts/unity-catalog-governance.md)

## Sources

- managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md

# Citations

1. [managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md](/references/managed-versus-external-assets-in-unity-catalog-databricks-on-aws-581e1fb1.md)
