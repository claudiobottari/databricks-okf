---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cf968bd4de8a7c861b4b507c3c6ac96cf06ad6b21f37c29c64452c657468de24
  pageDirectory: concepts
  sources:
    - create-a-unity-catalog-metastore-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workspace-metastore-attachment
  citations:
    - file: create-a-unity-catalog-metastore-databricks-on-aws.md
title: Workspace-Metastore Attachment
description: The process of linking a Unity Catalog metastore to Databricks workspaces in the same region, giving all linked workspaces a unified view of metastore data.
tags:
  - unity-catalog
  - workspaces
  - databricks
timestamp: "2026-06-19T09:30:37.022Z"
---

# Workspace-Metastore Attachment

**Workspace-Metastore Attachment** is the process of linking a Databricks workspace to a [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) in the same region. This attachment enables the workspace to use Unity Catalog for data governance, providing a three-level namespace (`catalog.schema.table`) and centralized access control across multiple workspaces. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Overview

Each Databricks region requires its own Unity Catalog [Metastore](/concepts/metastore.md). You can link each regional [Metastore](/concepts/metastore.md) to any number of workspaces in that region. After attachment, each linked workspace has the same view of the data in the [Metastore](/concepts/metastore.md), and data access control can be managed across workspaces. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

To work with Unity Catalog, users must be on a workspace that is attached to a [Metastore](/concepts/metastore.md) in their region. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Process

Workspace-metastore attachment is performed when creating a [Metastore](/concepts/metastore.md) in the Databricks account console. After creating the [Metastore](/concepts/metastore.md) and specifying its region, you are prompted to select workspaces to link to the [Metastore](/concepts/metastore.md). ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

### Requirements

- You must be a Databricks account admin. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]
- Your Databricks account must be on the Premium plan or above. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]
- The workspace must be in the same region as the [Metastore](/concepts/metastore.md). ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

### Automatic Attachment

For workspaces enabled for Unity Catalog automatically (starting November 8, 2023), the attachment process is handled by Databricks and does not require manual configuration. You only need to follow the manual instructions if your workspace does not already have a [Metastore](/concepts/metastore.md) in its region. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## After Attachment

After attaching a workspace to a [Metastore](/concepts/metastore.md), Databricks recommends:

1. **Transferring the [Metastore](/concepts/metastore.md) admin role** to a group rather than keeping it assigned to an individual user. The [Metastore](/concepts/metastore.md) admin can create top-level objects such as catalogs and manage access to tables and other objects. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]
2. **Enabling CORS configuration** on the S3 bucket used for [Metastore](/concepts/metastore.md) storage to allow Databricks management of uploads to managed volumes. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) — The top-level container for data in Unity Catalog
- Create a Unity Catalog Metastore — Full instructions for creating a [Metastore](/concepts/metastore.md) and attaching workspaces
- [Managed Storage in Unity Catalog](/concepts/managed-storage-in-unity-catalog.md) — Storage locations for managed tables and volumes
- [OpenSharing](/concepts/opensharing.md) — Accessing data in other metastores
- [Metastore Admin](/concepts/metastore-admin-role.md) — The role responsible for managing the [Metastore](/concepts/metastore.md)

## Sources

- create-a-unity-catalog-metastore-databricks-on-aws.md

# Citations

1. [create-a-unity-catalog-metastore-databricks-on-aws.md](/references/create-a-unity-catalog-metastore-databricks-on-aws-f0a3d0e9.md)
