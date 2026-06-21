---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6fb243855d8ba9cb47a2f0ae9be43b55e3ba1286b9576d62eaa930f4ad9644ff
  pageDirectory: concepts
  sources:
    - create-a-unity-catalog-metastore-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workspace-metastore-linking
    - workspace-metastore-attachment
  citations:
    - file: create-a-unity-catalog-metastore-databricks-on-aws.md
title: Workspace-Metastore Linking
description: The process of attaching a Databricks workspace to a Unity Catalog metastore, allowing multiple workspaces in the same region to share the same view of data with unified access control.
tags:
  - unity-catalog
  - workspace
  - databricks
timestamp: "2026-06-18T11:15:55.142Z"
---

# Workspace-Metastore Linking

**Workspace-Metastore Linking** is the process of attaching a [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) to a Databricks workspace so that users in that workspace can access data governed by the [Metastore](/concepts/metastore.md). A [Metastore](/concepts/metastore.md) is the top-level container for metadata about securable objects (such as tables, volumes, external locations, and shares) and the permissions that control access to them. Each [Metastore](/concepts/metastore.md) exposes a three-level namespace (`catalog.schema.table`) for organizing data. To work with Unity Catalog, users must be on a workspace that is attached to a [Metastore](/concepts/metastore.md) in their region. Databricks began automatically enabling new workspaces for Unity Catalog on November 8, 2023, so the manual linking steps described below are only necessary for existing workspaces or for workspaces in a region that does not yet have a [Metastore](/concepts/metastore.md). ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Prerequisites

- You must be a Databricks **account admin**.
- Your Databricks account must be on the **Premium plan or above**.
- Each region requires its own Unity Catalog [Metastore](/concepts/metastore.md). The [Metastore](/concepts/metastore.md) must be deployed in the same AWS region as the workspaces you want to link to it. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## The Linking Process

Linking is performed as part of the [Metastore](/concepts/metastore.md) creation workflow in the Databricks account console:

1. Log in to the [account console](https://accounts.cloud.databricks.com/).
2. Navigate to **Catalog** and click **Create metastore**.
3. Enter a name for the [Metastore](/concepts/metastore.md) and select the region (must match the region of your workspaces and, if applicable, the S3 storage bucket).
4. (Optional) Provide an S3 bucket path and an IAM role name if you have chosen to set up metastore-level managed storage.
5. Click **Create**. When prompted, select the workspaces to link to the [Metastore](/concepts/metastore.md).
6. After creation, transfer the [Metastore](/concepts/metastore.md) admin role to a group (recommended). The original creator is the owner. Reassigning to a group ensures continuity. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

A single [Metastore](/concepts/metastore.md) can be linked to any number of workspaces in the same region. Each linked workspace sees the same data and permissions as defined in the [Metastore](/concepts/metastore.md), enabling cross-workspace data access control. You can access data in other metastores using [Delta Sharing](/concepts/delta-sharing.md). ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Regional Constraints

Each [Metastore](/concepts/metastore.md) is tied to one AWS region. If your organization operates in multiple regions, you must create a separate [Metastore](/concepts/metastore.md) per region. Workspaces can only be linked to a [Metastore](/concepts/metastore.md) in the same region. The S3 bucket used for metastore-level managed storage must also reside in that same region. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Post-Linking Configuration

After linking, Databricks recommends enabling CORS on the S3 bucket used for managed storage to allow uploads to managed volumes. The CORS configuration must allow `PUT` requests from `https://*.databricks.com`. ^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Next Steps

- Create catalogs to organize data into logical containers.
- Create schemas within catalogs.
- Manage Unity Catalog metastores for ongoing administration.
- [Assign a metastore admin](/concepts/assigning-a-metastore-admin.md) to delegate ownership.

## Sources

- create-a-unity-catalog-metastore-databricks-on-aws.md

# Citations

1. [create-a-unity-catalog-metastore-databricks-on-aws.md](/references/create-a-unity-catalog-metastore-databricks-on-aws-f0a3d0e9.md)
