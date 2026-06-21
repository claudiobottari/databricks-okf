---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 97832c2061bf91c3a8ce7548dfeecc4b1a94dc84fa59929868288462090b1b5c
  pageDirectory: concepts
  sources:
    - manage-unity-catalog-metastores-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workspace-catalog-in-unity-catalog
    - WCIUC
  citations:
    - file: manage-unity-catalog-metastores-databricks-on-aws.md
title: Workspace Catalog in Unity Catalog
description: An automatically created catalog that is provisioned for each new workspace when metastore auto-assignment is enabled, giving all workspace users privileges to create objects within it.
tags:
  - unity-catalog
  - workspace
  - catalog
timestamp: "2026-06-19T19:30:48.743Z"
---

# Workspace Catalog in Unity Catalog

The **Workspace Catalog** is a special catalog that is automatically created in a [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) when workspace auto-assignment is enabled for a [Metastore](/concepts/metastore.md). When an account admin enables automatic [Metastore](/concepts/metastore.md) assignment for new workspaces, the system creates a workspace catalog and grants all workspace users the privileges required to create objects within it. ^[manage-unity-catalog-metastores-databricks-on-aws.md]

## Overview

Workspace catalogs are created as part of the onboarding process when a workspace is automatically assigned to a Unity Catalog [Metastore](/concepts/metastore.md). This automatic creation simplifies data governance by ensuring that every workspace has immediate access to a catalog where users can create and manage data objects without requiring additional administrative setup. ^[manage-unity-catalog-metastores-databricks-on-aws.md]

## Creation Prerequisites

Workspace catalogs are only created when an account admin enables the workspace auto-assignment setting for a [Metastore](/concepts/metastore.md). Before enabling this setting, administrators should understand the following implications for new workspaces:

- A workspace catalog will be created, and all workspace users will have the privileges required to create objects in it.
- Workspace admins will have the permissions required to create metastore-level securable objects, such as catalogs and external locations.
- If metastore-level storage is already enabled for the [Metastore](/concepts/metastore.md), the workspace will be able to use that storage.
- If a [Metastore](/concepts/metastore.md) admin is defined, they will be able to manage access to all securable objects in all workspaces attached to the [Metastore](/concepts/metastore.md).
- The OpenSharing setting for the [Metastore](/concepts/metastore.md) will apply to all workspaces attached to the [Metastore](/concepts/metastore.md).

^[manage-unity-catalog-metastores-databricks-on-aws.md]

## How to Enable Auto-Assignment

To enable automatic workspace assignment (and thus the creation of a workspace catalog), an account admin must perform the following steps:

1. Navigate to the Databricks account console.
2. Click the **Catalog** icon.
3. Select the [Metastore](/concepts/metastore.md).
4. On the **Configuration** tab, under **Workspace assignment**, select **Automatically assign new workspaces in `<region>` to this metastore**.
5. On the confirmation dialog, click **Enable auto-assignment**.

^[manage-unity-catalog-metastores-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) — The top-level container for data governance in Unity Catalog.
- [Metastore auto-assignment](/concepts/unity-catalog-metastore-auto-assignment.md) — The setting that triggers automatic workspace catalog creation.
- [Catalog](/concepts/unity-catalog.md) — The first-level container in the [Unity Catalog Object Hierarchy](/concepts/unity-catalog-object-hierarchy.md).
- [Unity Catalog permissions](/concepts/unity-catalog-permissions-model.md) — Access control for objects within Unity Catalog, including workspace catalogs.
- [Workspace admin privileges](/concepts/restricting-workspace-admin-privileges.md) — Permissions granted to workspace admins when workspaces are auto-enabled for Unity Catalog.

## Sources

- manage-unity-catalog-metastores-databricks-on-aws.md

# Citations

1. [manage-unity-catalog-metastores-databricks-on-aws.md](/references/manage-unity-catalog-metastores-databricks-on-aws-6a5c164f.md)
