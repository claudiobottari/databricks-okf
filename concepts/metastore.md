---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8d07b06150e774a3dcd7f3d6e42be0afcf5be104075fa69bf34d33e37901b1d3
  pageDirectory: concepts
  sources:
    - unity-catalog-securable-objects-reference-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metastore
    - metastores
    - Metastore catalog
    - restore
  citations:
    - file: unity-catalog-securable-objects-reference-databricks-on-aws.md
title: Metastore
description: The top-level securable object in Unity Catalog that contains all registered objects (catalogs, credentials, shares, connections, etc.) within a single cloud region.
tags:
  - unity-catalog
  - architecture
  - governance
timestamp: "2026-06-19T23:15:27.317Z"
---

# Metastore

The **metastore** is the top-level securable object in [Unity Catalog](/concepts/unity-catalog.md). It represents the container for all objects registered in [Unity Catalog](/concepts/unity-catalog.md) within a single cloud region. This includes not only the Catalog|catalogs that organize data assets, but also objects that control how data is accessed and shared, such as Storage Credential|storage credentials, [external locations](/concepts/external-location.md), Service Credential|service credentials, Connection|connections, Share|shares, [Recipient|recipients](/concepts/recipient-and-share-model.md), Provider|providers, and [Clean Room|clean rooms](/concepts/databricks-clean-rooms.md). ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

## Role in the Object Hierarchy

[Securable objects in Unity Catalog](/concepts/securable-objects-in-unity-catalog.md) follow a hierarchical structure, with the metastore as the root. Below the metastore, data assets are organized in a [Three-Level Namespace](/concepts/three-level-namespace.md): **catalog**, **schema**, and the asset type (such as Table|table, View|view, Volume|volume, or Function|function). This hierarchical structure provides the foundation for access control in [Unity Catalog](/concepts/unity-catalog.md), where privileges can be granted to principals (users, service principals, or groups) on any securable object in the hierarchy. ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

## Securable Objects within the Metastore

All other [Securable objects in Unity Catalog](/concepts/securable-objects-in-unity-catalog.md) exist directly under the metastore. These can be broadly categorized into two groups:

1. **Data and AI assets** organized within catalogs and schemas:
   - Table
   - View (including Materialized View|materialized views and Metric View|metric views)
   - Volume
   - Function (including user-defined functions, stored procedures, and [Model|registered models](/concepts/model-registration-methods.md))

2. **Access and sharing objects** that exist directly under the metastore:
   - [Storage Credential](/concepts/storage-credential-iam-role-for-unity-catalog.md) — authentication information for cloud storage access
   - [External location](/concepts/external-location.md) — a specific cloud storage path paired with a storage credential
   - Service Credential — authentication for accessing external cloud services
   - Connection — endpoint and credentials for accessing external systems
   - Share — a logical grouping of data assets for sharing
   - Provider — an external organization that has shared data with your organization
   - [Recipient](/concepts/data-recipient.md) — an external organization that receives shared data
   - [Clean Room](/concepts/databricks-clean-rooms.md) — a secure environment for multi-party collaboration ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

## Privileges and Access Control

As the top-level securable object, the metastore is the entry point for granting broad privileges across the entire [Unity Catalog](/concepts/unity-catalog.md) deployment. Many creation privileges on other securable objects must be granted at the metastore level. For example, creating a storage credential requires the `CREATE STORAGE CREDENTIAL` privilege on the metastore, and creating a connection requires the `CREATE CONNECTION` privilege on the metastore. ^[unity-catalog-securable-objects-reference-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Securable Object](/concepts/unity-catalog-securable-objects.md)
- [Catalog](/concepts/unity-catalog.md)
- Schema
- Table
- Access Control in Unity Catalog

## Sources

- unity-catalog-securable-objects-reference-databricks-on-aws.md

# Citations

1. [unity-catalog-securable-objects-reference-databricks-on-aws.md](/references/unity-catalog-securable-objects-reference-databricks-on-aws-c3527d93.md)
