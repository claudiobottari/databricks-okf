---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b205be8afae4f60cf7a7045a29c4be3d04f149de3e9c209960c404350844b8bc
  pageDirectory: concepts
  sources:
    - admin-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metastore-admin-unity-catalog
    - MA(C
  citations:
    - file: admin-privileges-in-unity-catalog-databricks-on-aws.md
title: Metastore Admin (Unity Catalog)
description: An optional role governing data access, ownership, and top-level Unity Catalog securable objects within a single metastore, with privileges from both the role and ownership of the metastore.
tags:
  - unity-catalog
  - admin-roles
  - databricks
timestamp: "2026-06-19T22:00:31.571Z"
---

# [Metastore](/concepts/metastore.md) Admin (Unity Catalog)

**Metastore admin** is an optional but highly privileged role in Unity Catalog that governs data access, ownership, and top-level Unity Catalog securable objects within a single [Metastore](/concepts/metastore.md). Unlike account admins and workspace admins, the [Metastore](/concepts/metastore.md) admin role is not required for all deployments, but it becomes necessary for specific administrative actions. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

The role sits alongside two other critical admin roles in Databricks: **account admins** (who operate at the account level, creating and linking metastores and workspaces) and **workspace admins** (who manage a single workspace). Understanding the boundaries between these roles helps organizations assign admins with the right scope. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## When to assign a [Metastore](/concepts/metastore.md) admin

For workspaces created after November 8, 2023, the [Metastore](/concepts/metastore.md) admin role is optional because workspace admins receive sufficient metastore-level privileges by default (see [Workspace Admin (Unity Catalog)](/concepts/workspace-admin-unity-catalog.md)). However, you must assign a [Metastore](/concepts/metastore.md) admin if you need to perform any of the following actions: ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

- Change ownership of objects or grant privileges on objects that you do not own. For example, this is required when taking over a catalog after the original owning account is removed. Workspace admins can create objects but cannot make grants on or change ownership of existing objects they do not own. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]
- Remove default workspace admin privileges on the [Metastore](/concepts/metastore.md). ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]
- Add managed storage to the [Metastore](/concepts/metastore.md) if it has none (this also requires an account admin to add the storage location to the [Metastore](/concepts/metastore.md) definition). ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]
- Enable default access request destinations for objects that don't have destinations explicitly set. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Default [Metastore](/concepts/metastore.md) admin privileges

[Metastore](/concepts/metastore.md) admins receive a set of default privileges on the [Metastore](/concepts/metastore.md) itself. These include all capabilities necessary to manage the [Metastore](/concepts/metastore.md)'s securable objects, such as creating catalogs, managing external locations, and governing permissions. The source document lists these privileges in a table, but the exact list is omitted here for brevity — consult the Databricks documentation for the full set. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Ownership privileges

Because the [Metastore](/concepts/metastore.md) admin is the owner of the [Metastore](/concepts/metastore.md), they also possess all ownership privileges on the [Metastore](/concepts/metastore.md) object. Ownership grants the ability to transfer ownership, manage permissions on the [Metastore](/concepts/metastore.md), and perform any action that the owner of a securable object can perform. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Who has initial [Metastore](/concepts/metastore.md) admin privileges?

If an account admin manually creates the [Metastore](/concepts/metastore.md), that account admin becomes the [Metastore](/concepts/metastore.md)'s initial owner and [Metastore](/concepts/metastore.md) admin. All metastores created before November 8, 2023 were created manually by an account admin. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

If the [Metastore](/concepts/metastore.md) was provisioned as part of automatic Unity Catalog enablement (applies to workspaces created after November 8, 2023), the [Metastore](/concepts/metastore.md) was created without a [Metastore](/concepts/metastore.md) admin. In that case, workspace admins are automatically granted privileges that make the [Metastore](/concepts/metastore.md) admin optional. If needed, account admins can assign the [Metastore](/concepts/metastore.md) admin role to a user, service principal, or group (groups are strongly recommended). ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Assign a [Metastore](/concepts/metastore.md) admin

The [Metastore](/concepts/metastore.md) admin role is highly privileged and should be distributed carefully. Databricks recommends nominating a **group** as the [Metastore](/concepts/metastore.md) admin rather than an individual, so that any member of the group automatically becomes a [Metastore](/concepts/metastore.md) admin. Only account admins can assign the [Metastore](/concepts/metastore.md) admin role. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

To assign the [Metastore](/concepts/metastore.md) admin role to a group:

1. As an account admin, log in to the [account console](https://accounts.cloud.databricks.com/).
2. Click **Catalog**.
3. Click the name of a [Metastore](/concepts/metastore.md) to open its properties.
4. Under **Metastore Admin**, click **Edit**.
5. Select a group from the drop-down. You can enter text in the field to search for options.
6. Click **Save**.

It can take up to 30 seconds for a [Metastore](/concepts/metastore.md) admin assignment change to be reflected in your account, and it may take longer to take effect in some workspaces than others due to caching protocols. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Related concepts

- [Account admin](/concepts/account-admin-unity-catalog.md) — The role that creates and links metastores, and assigns the [Metastore](/concepts/metastore.md) admin role.
- [Workspace Admin (Unity Catalog)](/concepts/workspace-admin-unity-catalog.md) — The role that receives default [Metastore](/concepts/metastore.md) privileges on automatically enabled workspaces.
- [Unity Catalog](/concepts/unity-catalog.md) — The metastore-based governance solution.
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — The full permission model for securable objects.

## Sources

- admin-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [admin-privileges-in-unity-catalog-databricks-on-aws.md](/references/admin-privileges-in-unity-catalog-databricks-on-aws-a7ab7fd7.md)
