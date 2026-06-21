---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aebbf3fab3e98a2dfb53d313a754cd0c38c228ef62c0830d147a6553f137dde5
  pageDirectory: concepts
  sources:
    - managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-governance
    - UCG
    - Unity Catalog Data Governance
    - Unity Catalog – Data Governance
  citations:
    - file: managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md
title: Unity Catalog governance
description: Central management of metadata, access control, auditing, and lineage for all registered securable objects
tags:
  - unity-catalog
  - data-governance
  - security
timestamp: "2026-06-19T19:29:20.755Z"
---

# Unity Catalog governance

**Unity Catalog governance** refers to the centralized management, access control, auditing, and lineage tracking that Unity Catalog applies to every [securable object](/concepts/unity-catalog-securable-objects.md) registered in it. Governance covers all objects—tables, volumes, views, models, functions, and others—whether they are managed or external. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

For data assets like tables and volumes, Unity Catalog can additionally control the storage location and lifecycle of the underlying data files in your cloud account. This distinction creates two categories: **managed assets** and **external assets**. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

## Managed vs. external assets

- **Managed assets** – Unity Catalog governs both (a) access, auditing, and lineage, and (b) the underlying file storage lifecycle (how files are organized, optimized, and when they are deleted). ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]
- **External assets** – Unity Catalog governs access, auditing, and lineage only. The underlying file storage lifecycle is controlled by you or an external system. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

When you register a managed asset, your data files remain in your cloud account at all times. Unity Catalog determines where within your account they are stored but does not transfer them to Databricks or own them. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

The managed/external distinction applies only to tables and volumes. Other Unity Catalog securable objects—such as views, models, and functions—do not have managed and external variants. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

## Managed and external tables

A **[managed table](/concepts/unity-catalog-managed-tables.md)** is a table where Unity Catalog determines the storage location for the underlying data files. Unity Catalog stores managed tables in the managed storage location defined on the containing schema, catalog, or [Metastore](/concepts/metastore.md). When you drop a managed table, Unity Catalog deletes the underlying data files. Managed tables use the Delta or [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) format. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

An **external table** is a table where you specify the storage location for the underlying data files. When you drop an external table, Unity Catalog removes the table metadata from the [Metastore](/concepts/metastore.md), but the underlying data files remain. External tables support multiple formats, including Delta, CSV, JSON, Avro, Parquet, and ORC. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

Both managed and external tables support read, write, and create access from external engines via open APIs, such as the Unity REST API and the [Iceberg REST Catalog](/concepts/iceberg-rest-catalog-irc-protocol.md). This means managed tables do not cause vendor lock-in; any engine that supports these APIs can access them. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

## Managed and external volumes

A **managed volume** is a volume where Unity Catalog determines the storage location. Unity Catalog automatically stores managed volumes in the managed storage location of the containing schema within your cloud account. As with managed tables, you retain full ownership of the underlying data. When you drop a managed volume, Unity Catalog deletes the underlying data files. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

An **external volume** is a volume where you specify the storage location. The location must be a path covered by a Unity Catalog [External location](/concepts/external-location.md). When you drop an external volume, Unity Catalog removes the volume definition, but the underlying data files remain in place. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

## Uses of the word “manage” across Unity Catalog

The word _manage_ has multiple meanings in Unity Catalog:

1. **Governance** – When people say an object is “managed by Unity Catalog,” they typically mean that Unity Catalog governs access to it. This applies to all registered objects, including external tables and volumes. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

2. **Managed tables/volumes** – The word _managed_ in “managed table” or “managed volume” has a more specific meaning: Unity Catalog determines where in your cloud account the underlying data files are stored and controls the file lifecycle (optimization, organization, and deletion). This is referred to as the _managed storage location_. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

3. **`MANAGE` privilege** – The word `MANAGE` also appears as a privilege that can be assigned to Unity Catalog objects. Generally, `MANAGE` allows a user to assign or revoke privileges on, transfer ownership of, and delete an object without being the owner. ^[managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md]

## Related concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Securable object](/concepts/unity-catalog-securable-objects.md)
- Access control in Unity Catalog
- Auditing in Unity Catalog
- [Lineage in Unity Catalog](/concepts/data-lineage-in-unity-catalog.md)
- [Managed storage location](/concepts/managed-storage-location.md)
- [External location](/concepts/external-location.md)
- [Delta table](/concepts/delta-lake-table.md)
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md)

## Sources

- managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md

# Citations

1. [managed-versus-external-assets-in-unity-catalog-databricks-on-aws.md](/references/managed-versus-external-assets-in-unity-catalog-databricks-on-aws-581e1fb1.md)
