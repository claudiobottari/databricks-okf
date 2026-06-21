---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5de43ac3f0dc3dd7e5bf0d7ad9859f35e85f32a81cefa393208b3273c6710306
  pageDirectory: concepts
  sources:
    - admin-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - account-admin-role-in-unity-catalog
    - AARIUC
    - Admin Roles in Unity Catalog
    - Admin roles in Unity Catalog
  citations:
    - file: admin-privileges-in-unity-catalog-databricks-on-aws.md
title: Account Admin Role in Unity Catalog
description: A highly privileged role operating at the Databricks account level, responsible for creating and linking metastores and workspaces, and assigning admin roles.
tags:
  - unity-catalog
  - account-admin
  - admin-roles
timestamp: "2026-06-19T17:28:49.471Z"
---

# Account Admin Role in Unity Catalog

The **Account Admin Role in Unity Catalog** is a highly privileged role that operates at the Databricks account level, with authority over the entire Databricks account rather than individual workspaces. Account admins are one of three key administrative roles in Unity Catalog, alongside workspace admins and [Metastore](/concepts/metastore.md) admins. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Overview

Account admins are required for all Databricks deployments. They have privileges that span the entire account, including the ability to create and link metastores and workspaces, and to assign admin roles to other users. Due to the broad scope of their permissions, this role should be distributed carefully. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

The three most important administrative roles in Unity Catalog from a permissions perspective are:
- **Account admins** — operate at the account level
- **[Workspace admin privileges|Workspace admins](/concepts/workspace-admin-privileges-in-unity-catalog.md)** — operate within a single workspace
- **[Metastore admin privileges|Metastore admins (optional)](/concepts/metastore-admin-ownership-privileges.md)** — operate within a single Unity Catalog [Metastore](/concepts/metastore.md) ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Key Capabilities

Account admins have the following critical capabilities:

- Create and manage metastores
- Link metastores to workspaces
- Create and manage workspaces
- Assign admin roles to users, groups, or service principals
- Restrict workspace admin privileges using the `RestrictWorkspaceAdmins` setting ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Relationship to [Metastore](/concepts/metastore.md) Admin Role

Account admins and [Metastore](/concepts/metastore.md) admins are separate roles. However, there is an important default behavior: when an account admin creates a [Metastore](/concepts/metastore.md), they become its initial [Metastore](/concepts/metastore.md) admin by default. The account admin can then assign the [Metastore](/concepts/metastore.md) admin role to a different user, group, or service principal and relinquish the [Metastore](/concepts/metastore.md) admin role themselves. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## [Metastore](/concepts/metastore.md) Creation and Initial Admin

### Manual Creation
If an account admin creates a [Metastore](/concepts/metastore.md) manually, that account admin becomes the [Metastore](/concepts/metastore.md)'s initial owner and [Metastore](/concepts/metastore.md) admin. All metastores created before November 8, 2023 were created manually by an account admin. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

### Automatic Provisioning
If the [Metastore](/concepts/metastore.md) was provisioned as part of automatic Unity Catalog enablement (applicable to all workspaces created after November 8, 2023), the [Metastore](/concepts/metastore.md) was created without a [Metastore](/concepts/metastore.md) admin. In this case, workspace admins are automatically granted privileges that make the [Metastore](/concepts/metastore.md) admin optional. If needed, account admins can assign the [Metastore](/concepts/metastore.md) admin role to a user, service principal, or group. Databricks strongly recommends using groups. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Assigning the [Metastore](/concepts/metastore.md) Admin Role

Account admins have the authority to assign the [Metastore](/concepts/metastore.md) admin role. Databricks recommends nominating a group as the [Metastore](/concepts/metastore.md) admin, as any member of the group automatically becomes a [Metastore](/concepts/metastore.md) admin. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

To assign the [Metastore](/concepts/metastore.md) admin role to a group:
1. As an account admin, log in to the [account console](https://accounts.cloud.databricks.com/).
2. Click the **Catalog** icon.
3. Click the name of a [Metastore](/concepts/metastore.md) to open its properties.
4. Under **Metastore Admin**, click **Edit**.
5. Select a group from the drop-down field.
6. Click **Save**. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

> **Important:** It can take up to 30 seconds for a [Metastore](/concepts/metastore.md) admin assignment change to be reflected in your account, and it may take longer to take effect in some workspaces than others. This delay is due to caching protocols. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Best Practices

- Distribute the account admin role carefully due to its high privilege level
- Use groups rather than individual users for admin role assignments when possible
- Consider transferring the [Metastore](/concepts/metastore.md) admin role from the account admin to a dedicated group after initial [Metastore](/concepts/metastore.md) setup
- Use the `RestrictWorkspaceAdmins` setting to limit workspace admin privileges when needed ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Metastore admin privileges](/concepts/metastore-admin-ownership-privileges.md) — The optional role that governs data access and ownership within a [Metastore](/concepts/metastore.md)
- [Workspace admin privileges](/concepts/restricting-workspace-admin-privileges.md) — Admin privileges scoped to a single workspace
- [Metastore](/concepts/metastore.md) — The top-level container for data governance in Unity Catalog
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution for Databricks
- Account Console — The management interface for account-level operations

## Sources

- admin-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [admin-privileges-in-unity-catalog-databricks-on-aws.md](/references/admin-privileges-in-unity-catalog-databricks-on-aws-a7ab7fd7.md)
