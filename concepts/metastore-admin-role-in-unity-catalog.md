---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1ffe8da896fe577dc92fed80d9363f757fa99298e28645f21c4969d21f259044
  pageDirectory: concepts
  sources:
    - create-a-unity-catalog-metastore-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metastore-admin-role-in-unity-catalog
    - MARIUC
  citations:
    - file: create-a-unity-catalog-metastore-databricks-on-aws.md
title: Metastore Admin Role in Unity Catalog
description: The administrative role automatically assigned to the creator of a metastore, with privileges to create catalogs and manage access, and a recommendation to reassign it to a group.
tags:
  - unity-catalog
  - administration
  - security
  - databricks
timestamp: "2026-06-18T14:49:11.611Z"
---

# [Metastore](/concepts/metastore.md) Admin Role in Unity Catalog

The **Metastore Admin** is the owner of a Unity Catalog [Metastore](/concepts/metastore.md), with full administrative privileges over the [Metastore](/concepts/metastore.md) and all objects within it. This role is automatically assigned to the user who creates the [Metastore](/concepts/metastore.md).^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Responsibilities

The [Metastore](/concepts/metastore.md) admin can:

- Create top-level objects in the [Metastore](/concepts/metastore.md), such as [catalogs](/concepts/unity-catalog.md) and schemas.
- Manage access to tables, [volumes](/concepts/ucvolumedataset.md), and other securable objects registered in the [Metastore](/concepts/metastore.md).
- Link or unlink workspaces to the [Metastore](/concepts/metastore.md).
- Assign other users, service principals, or groups as additional [Metastore](/concepts/metastore.md) admins (see [Assign a metastore admin](/concepts/assigning-a-metastore-admin.md)).^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Best Practices

Databricks **strongly recommends** that you reassign the [Metastore](/concepts/metastore.md) admin role to a group rather than keeping it assigned to an individual user. This ensures that administrative access is not lost when a person leaves the organization or changes roles. The group can contain multiple users or service principals as needed.^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Transferring the Role

To transfer the [Metastore](/concepts/metastore.md) admin role to a group after the [Metastore](/concepts/metastore.md) is created, follow the instructions in the documentation on Manage Unity Catalog metastores and [Assign a metastore admin](/concepts/assigning-a-metastore-admin.md).^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) – The top-level container for data governance.
- [Catalogs](/concepts/unity-catalog.md) – First-level namespace in Unity Catalog.
- Manage Unity Catalog metastores – Administration of [Metastore](/concepts/metastore.md) settings and assignments.
- [Assign a metastore admin](/concepts/assigning-a-metastore-admin.md) – How to grant or transfer the admin role.
- [Managed Storage in Unity Catalog](/concepts/managed-storage-in-unity-catalog.md) – Storage locations owned by the [Metastore](/concepts/metastore.md).

## Sources

- create-a-unity-catalog-metastore-databricks-on-aws.md

# Citations

1. [create-a-unity-catalog-metastore-databricks-on-aws.md](/references/create-a-unity-catalog-metastore-databricks-on-aws-f0a3d0e9.md)
