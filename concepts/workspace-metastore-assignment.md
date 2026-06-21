---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1f6539d9d820b4a2e7b080dae5f49dff357c1a47ae05194fe2de1a82393838a3
  pageDirectory: concepts
  sources:
    - enable-a-workspace-for-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workspace-metastore-assignment
    - Workspace assignment
  citations:
    - file: enable-a-workspace-for-unity-catalog-databricks-on-aws.md
title: Workspace-Metastore Assignment
description: The process of enabling a Databricks workspace for Unity Catalog by assigning it to a Unity Catalog metastore, either during workspace creation or later via the account console.
tags:
  - unity-catalog
  - workspace-setup
  - databricks
timestamp: "2026-06-19T18:39:51.492Z"
---

# Workspace-Metastore Assignment

**Workspace-Metastore Assignment** is the process of linking a Databricks workspace to a [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md), which enables the workspace for Unity Catalog. This assignment determines which metastore’s data catalog, access controls, and governance policies apply to users and workloads in that workspace. Once assigned, the workspace cannot be unlinked, and user and group management moves to account-level interfaces. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

## Overview

Enabling Unity Catalog for a workspace means that users in that workspace can potentially access the same data as users in other workspaces linked to the same [Metastore](/concepts/metastore.md), and data stewards can manage data access centrally across workspaces. Data access is audited automatically, and identity federation is enabled, allowing admins to manage identities centrally using the account console. A [Metastore](/concepts/metastore.md) is the top-level container for data in Unity Catalog, exposing a three-level namespace (`catalog.schema.table`) by which data can be organized. You can share a single [Metastore](/concepts/metastore.md) across multiple Databricks workspaces in an account, giving each linked workspace the same view of the data. You can create one [Metastore](/concepts/metastore.md) per region and attach it to any number of workspaces in that region. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

## Automatic vs. Manual Enablement

On November 8, 2023, Databricks started to enable new workspaces for Unity Catalog automatically, with a rollout proceeding gradually. If your workspace was enabled automatically, the manual assignment process described in this article does not apply. To determine if your workspace is already enabled for Unity Catalog, see the setup documentation for confirming Unity Catalog enablement. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

## Considerations Before Enabling

### Workspace Admin Privileges

Workspace admin is a privileged role that should be distributed carefully. Workspace admins can manage operations for their workspace, including adding users and service principals, creating clusters, and delegating other users to be workspace admins. If your workspace was enabled for Unity Catalog automatically, the workspace admin also has a number of additional privileges by default, including the ability to create most Unity Catalog object types and grant access to the ones they create. If your workspace was not enabled automatically, workspace admins have no more access to Unity Catalog objects by default than any other user, but they do have the ability to perform workspace management tasks such as managing job ownership and viewing notebooks, which may give indirect access to data registered in Unity Catalog. Account admins can restrict workspace admin privileges using the `RestrictWorkspaceAdmins` setting. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

### Workspace-Catalog Bindings

If you use workspaces to isolate user data access, you might want to use workspace-catalog bindings. These bindings enable you to limit catalog access by workspace boundaries. For example, you can ensure that workspace admins and users can only access production data in `prod_catalog` from a production workspace environment, `prod_workspace`. The default is to share the catalog with all workspaces attached to the current [Metastore](/concepts/metastore.md). Likewise, you can bind access to external locations such that they are accessible only from specified workspaces. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

### Automation and SCIM Provisioning

Update any automation configured to manage users, groups, and service principals — such as SCIM provisioning connectors and Terraform automation — so that they refer to account endpoints instead of workspace endpoints. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

### Irreversibility

Enabling a workspace for Unity Catalog cannot be reversed. Once you enable the workspace, you will manage users, groups, and service principals for this workspace using account-level interfaces. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

## Requirements

Before you can enable your workspace for Unity Catalog, you must have a [Metastore](/concepts/metastore.md) configured for your Databricks account. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

## How to Assign a Workspace to a [Metastore](/concepts/metastore.md)

### Assigning an Existing Workspace

To enable an existing workspace for Unity Catalog using the account console:

1. As an account admin, log in to the [account console](https://accounts.cloud.databricks.com/).
2. Click **Catalog**.
3. Click the [Metastore](/concepts/metastore.md) name.
4. Click the **Workspaces** tab.
5. Click **Assign to workspace**.
6. Select one or more workspaces. You can type part of the workspace name to filter the list.
7. Scroll to the bottom of the dialog, and click **Assign**.
8. On the confirmation dialog, click **Enable**.

^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

### Enabling Unity Catalog When Creating a Workspace

To enable Unity Catalog when you create a workspace using the account console:

1. As an account admin, log in to the account console.
2. Click **Workspaces**.
3. Click **Create workspace**.
4. On the Create workspace page, click the **Enable Unity Catalog** toggle.
5. On the confirmation dialog, click **Enable**.
6. Select the **Metastore**.
7. Complete the workspace creation configuration and click **Save**.

^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

When the assignment is complete, the workspace appears in the metastore’s **Workspaces** tab, and the [Metastore](/concepts/metastore.md) appears on the workspace’s **Configuration** tab. ^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The data governance solution that provides [Metastore](/concepts/metastore.md) capabilities.
- [Metastore](/concepts/metastore.md) – The top-level container for data in Unity Catalog.
- [Workspace-Catalog Binding](/concepts/workspace-catalog-binding.md) – Limiting catalog access by workspace boundaries.
- [External Location Workspace Binding](/concepts/unity-catalog-workspace-bindings.md) – Restricting external location access to specific workspaces.
- [Account-Level SCIM Provisioning](/concepts/account-level-identity-provisioning-for-unity-catalog.md) – Managing identities at the account level after Unity Catalog enablement.
- Admin Privileges in Unity Catalog – Understanding workspace admin capabilities in Unity Catalog‑enabled workspaces.
- [Restrict Workspace Admins](/concepts/restrictworkspaceadmins-setting.md) – Account-level setting to limit workspace admin power.

## Sources

- enable-a-workspace-for-unity-catalog-databricks-on-aws.md

# Citations

1. [enable-a-workspace-for-unity-catalog-databricks-on-aws.md](/references/enable-a-workspace-for-unity-catalog-databricks-on-aws-e9f0e09a.md)
