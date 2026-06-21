---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2668e0c458f9926cc80dae7de1fc9e6a3de5b3c7156794a51f856e8d2815a887
  pageDirectory: concepts
  sources:
    - managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - managed-assets-in-unity-catalog
    - MAIUC
  citations:
    - file: managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md
title: Managed assets in Unity Catalog
description: Data assets (tables and volumes) where Unity Catalog controls both governance and the underlying file storage lifecycle
tags:
  - unity-catalog
  - data-governance
  - databricks
timestamp: "2026-06-19T19:30:50.635Z"
---

# Managed assets in Unity Catalog

**Managed assets** in [Unity Catalog] are data objects — specifically tables and volumes — where the catalog controls both governance (access control, auditing, lineage) and the lifecycle of the underlying data files (storage location, organization, optimization, and deletion). This is distinct from external assets, where Unity Catalog governs only the metadata while the file lifecycle remains under external control. The managed-versus-external distinction applies only to tables and volumes; other securable objects such as views, models, and functions do not have managed and external variants. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

## Overview

When you register a managed asset in Unity Catalog, you retain full ownership of your data. The data files always remain in your cloud account — Databricks does not transfer them to its own infrastructure or own them. Unity Catalog determines where within your account the files are stored (the *managed storage location*), but the data stays under your control at all times. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

The term *managed* has multiple meanings in the Unity Catalog context:

- **Governance-managed**: All registered objects are "managed by Unity Catalog" in the sense that Unity Catalog governs access to them. This applies to both managed and external tables/volumes, as well as to views, models, and functions.
- **Lifecycle-managed**: Managed tables and volumes have a specific meaning: Unity Catalog determines where in your cloud account the underlying data files are stored and controls the file lifecycle (optimization, organization, and deletion). This is what the product documentation calls the *managed storage location*.
- **`MANAGE` privilege**: `MANAGE` is also a privilege that can be assigned to any Unity Catalog securable object. It allows a user to assign or revoke privileges, transfer ownership, and delete an object without being the owner.

^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

## Managed tables

A **Unity Catalog managed table** is a table where Unity Catalog determines the storage location for the underlying data files. Managed tables are stored in the managed storage location defined on the containing schema, catalog, or [Metastore](/concepts/metastore.md). When you drop a managed table, Unity Catalog deletes the underlying data files. Managed tables use the Delta or Apache Iceberg format. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

By contrast, an **external table** requires you to specify the storage location. Dropping an external table removes only the metadata; the data files remain in place. External tables support multiple formats, including Delta, CSV, JSON, Avro, Parquet, and ORC. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

Both managed and external tables support read, write, and create access from external engines via open APIs, including the Unity REST API and the Iceberg REST Catalog (IRC). This means that managed tables do not cause vendor lock-in — any engine that supports these APIs can access them. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

For more detail on table types, see Databricks Unity Catalog table types.

## Managed volumes

A **Unity Catalog managed volume** is a volume where Unity Catalog determines the storage location. Unity Catalog automatically stores managed volumes in the managed storage location of the containing schema within your cloud account. As with managed tables, you retain full ownership of the underlying data. When you drop a managed volume, Unity Catalog deletes the underlying data files. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

An **external volume** requires you to specify a storage location that is covered by a Unity Catalog [External location](/concepts/external-location.md). Dropping an external volume removes only the volume definition; the underlying data files remain in place. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

For more information about volumes, see [What are Unity Catalog volumes?](/concepts/databricks-utilities-with-unity-catalog-volumes.md).

## Key differences: managed vs. external

| Property | Managed | External |
|----------|---------|----------|
| Governance (access, audit, lineage) | Unity Catalog | Unity Catalog |
| File storage location | Determined by Unity Catalog (managed storage location on the schema, catalog, or [Metastore](/concepts/metastore.md)) | Specified by the user |
| File lifecycle (optimization, organization, deletion) | Unity Catalog controls | User or external system controls |
| Data ownership | Remains in the user's cloud account | Remains in the user's cloud account |
| When dropped | Data files are deleted | Data files remain in place |
| Supported formats (tables) | Delta, Apache Iceberg | Delta, CSV, JSON, Avro, Parquet, ORC |
| Applicable to | Tables and volumes only | Tables and volumes only |

^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

## Related concepts

- [External assets in Unity Catalog](/concepts/external-assets-in-unity-catalog.md) — The complement to managed assets
- [Managed storage location](/concepts/managed-storage-location.md) — Where Unity Catalog places managed asset data files
- [Unity Catalog Securable Objects](/concepts/unity-catalog-securable-objects.md) — The complete set of objects governed by Unity Catalog
- [External location](/concepts/external-location.md) — A cloud storage path registered as a security boundary for external assets
- Databricks Unity Catalog table types — Detailed documentation on managed and external tables
- [What are Unity Catalog volumes?](/concepts/databricks-utilities-with-unity-catalog-volumes.md) — Overview of the volumes feature

## Sources

- managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md

# Citations

1. [managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md](/references/managed-versus-external-assets-in-unity-catalog-databricks-on-aws-581e1fb1.md)
