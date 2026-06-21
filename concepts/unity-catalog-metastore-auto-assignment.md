---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aa280457efeeddf27c673881eaeb12ea32678333f7f3d8132996b4f4ad497e6e
  pageDirectory: concepts
  sources:
    - manage-unity-catalog-metastores-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-metastore-auto-assignment
    - UCMA
    - Metastore auto-assignment
  citations:
    - file: manage-unity-catalog-metastores-databricks-on-aws.md
title: Unity Catalog Metastore Auto-Assignment
description: An account admin setting that automatically assigns an existing Unity Catalog metastore to new workspaces created in the same AWS region, eliminating the need for manual workspace-to-metastore assignment.
tags:
  - unity-catalog
  - metastore
  - workspace-management
timestamp: "2026-06-19T19:28:51.810Z"
---

## Unity Catalog [Metastore](/concepts/metastore.md) Auto-Assignment

**Unity Catalog [Metastore](/concepts/metastore.md) Auto-Assignment** is a configuration setting that allows an account admin to automatically assign an existing Unity Catalog [Metastore](/concepts/metastore.md) to new workspaces created in the same cloud region as the [Metastore](/concepts/metastore.md). When enabled, the [Metastore](/concepts/metastore.md) is attached to the workspace without requiring a manual selection during workspace creation. ^[manage-unity-catalog-metastores-databricks-on-aws.md]

### Impacts on New Workspaces

Before enabling auto-assignment, account admins should understand the following consequences for every workspace that is subsequently created in the region:

- A **workspace catalog** is automatically created, and all workspace users receive the privileges needed to create objects inside it. ^[manage-unity-catalog-metastores-databricks-on-aws.md]
- Workspace admins obtain the permissions required to create metastore-level securable objects such as catalogs and external locations. ^[manage-unity-catalog-metastores-databricks-on-aws.md]
- If metastore-level managed storage has been configured, the workspace can use that storage location. ^[manage-unity-catalog-metastores-databricks-on-aws.md]
- If a [Metastore](/concepts/metastore.md) admin is defined, that admin can manage access to all securable objects across every workspace attached to the [Metastore](/concepts/metastore.md). ^[manage-unity-catalog-metastores-databricks-on-aws.md]
- The OpenSharing setting (enabled or disabled) of the [Metastore](/concepts/metastore.md) applies uniformly to all attached workspaces. ^[manage-unity-catalog-metastores-databricks-on-aws.md]

### How to Enable Auto-Assignment

1. Log in to the Databricks account console as an account admin.
2. Click the **Catalog** icon.
3. Select the [Metastore](/concepts/metastore.md) you want to configure.
4. On the **Configuration** tab, under **Workspace assignment**, select **Automatically assign new workspaces in `<region>` to this metastore**.
5. Confirm by clicking **Enable auto-assignment** on the dialog.

^[manage-unity-catalog-metastores-databricks-on-aws.md]

If auto-assignment is not enabled, the admin who creates a workspace in the same region must manually attach the workspace to the [Metastore](/concepts/metastore.md) by choosing it from a drop-down list.

### Related Concepts

- [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) — The top-level container for Unity Catalog metadata and data assets.
- [Workspace catalog](/concepts/workspace-catalog-binding.md) — The default catalog created for a workspace when it is attached to a [Metastore](/concepts/metastore.md).
- [Metastore admin](/concepts/metastore-admin-role.md) — A principal with administrative privileges over all objects in the [Metastore](/concepts/metastore.md).
- [Metastore-level managed storage](/concepts/metastore-level-managed-storage.md) — A cloud storage location used for managing Unity Catalog tables and volumes.
- [OpenSharing](/concepts/opensharing.md) — A Delta Sharing feature that allows sharing data with external organizations.

### Sources

- manage-unity-catalog-metastores-databricks-on-aws.md

# Citations

1. [manage-unity-catalog-metastores-databricks-on-aws.md](/references/manage-unity-catalog-metastores-databricks-on-aws-6a5c164f.md)
