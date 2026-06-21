---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6b182f2acef47f7dfe2b7de65eac9b707b2744472155353e00f00ad3a93e5500
  pageDirectory: concepts
  sources:
    - admin-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metastore-admins-in-unity-catalog
    - MAIUC
  citations:
    - file: admin-privileges-in-unity-catalog-databricks-on-aws.md
title: Metastore Admins in Unity Catalog
description: Optional but highly privileged role governing data access, ownership, and top-level Unity Catalog securable objects within a single metastore; needed for operations like changing ownership or removing default workspace admin permissions.
tags:
  - unity-catalog
  - admin-roles
  - databricks
timestamp: "2026-06-19T13:54:33.127Z"
---

# [Metastore](/concepts/metastore.md) Admins in Unity Catalog

**Metastore Admin** is an optional, highly privileged role within a single [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md). Although account admins and workspace admins are required for all deployments, the [Metastore](/concepts/metastore.md) admin role is needed only for specific governance actions such as changing ownership of objects that the current owner cannot manage, removing default workspace admin permissions, or enabling default access request destinations. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Overview

From a Unity Catalog permissions perspective, the three most important admin roles are account admins, workspace admins, and [Metastore](/concepts/metastore.md) admins. [Metastore](/concepts/metastore.md) admins operate within a single [Metastore](/concepts/metastore.md), governing data access, ownership, and top-level Unity Catalog securable objects. Unlike account and workspace admins, the [Metastore](/concepts/metastore.md) admin role is optional—especially for workspaces created after November 8, 2023, where workspace admins receive sufficient metastore-level privileges by default. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## When to assign a [Metastore](/concepts/metastore.md) admin

For workspaces created after November 8, 2023, you must assign a [Metastore](/concepts/metastore.md) admin only if you need to perform the following actions:

- **Change ownership** of objects or grant privileges on objects that you do not own (for example, taking over a catalog after the original owning account is removed). Workspace admins can create objects but cannot make grants on or change ownership of existing objects they do not own.
- **Remove** default workspace admin permissions.
- **Add managed storage** to the [Metastore](/concepts/metastore.md) if it has none (this action also requires an account admin to add the storage location to the [Metastore](/concepts/metastore.md) definition).
- **Enable default access request destinations** for objects that don't have destinations explicitly set.

^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Default [Metastore](/concepts/metastore.md) admin privileges

[Metastore](/concepts/metastore.md) admins receive privileges from two sources: default privileges granted by the role and ownership privileges because they are the owners of the [Metastore](/concepts/metastore.md).

The default privileges on the [Metastore](/concepts/metastore.md) include all permissions necessary to manage data access and ownership at the [Metastore](/concepts/metastore.md) level. (The source document lists these privileges but does not enumerate them individually in an accessible format; it states that [Metastore](/concepts/metastore.md) admins have these privileges by virtue of the role.) ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Ownership privileges

As owners of the [Metastore](/concepts/metastore.md), [Metastore](/concepts/metastore.md) admins have the following privileges:

- **Manage privileges** for or transfer ownership of any object within the [Metastore](/concepts/metastore.md), including the ability to grant themselves read and write access to all data in the [Metastore](/concepts/metastore.md) (granting permissions is audit-logged).
- **Transfer ownership** of the [Metastore](/concepts/metastore.md) itself.

^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Initial [Metastore](/concepts/metastore.md) admin

If an account admin creates the [Metastore](/concepts/metastore.md) manually, that account admin becomes the [Metastore](/concepts/metastore.md)'s initial owner and [Metastore](/concepts/metastore.md) admin. All metastores created before November 8, 2023, were created manually by an account admin. If the [Metastore](/concepts/metastore.md) was provisioned as part of automatic Unity Catalog enablement (workspaces created after November 8, 2023), the [Metastore](/concepts/metastore.md) was created without a [Metastore](/concepts/metastore.md) admin. In that case, workspace admins are automatically granted privileges that make the [Metastore](/concepts/metastore.md) admin role optional. Account admins can later assign the [Metastore](/concepts/metastore.md) admin role to a user, service principal, or group (groups are strongly recommended). ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Assigning a [Metastore](/concepts/metastore.md) admin

[Metastore](/concepts/metastore.md) admin is a highly privileged role that should be distributed carefully. Only account admins can assign the [Metastore](/concepts/metastore.md) admin role. Databricks recommends nominating a **group** as the [Metastore](/concepts/metastore.md) admin so that any member of the group automatically becomes a [Metastore](/concepts/metastore.md) admin.

To assign the [Metastore](/concepts/metastore.md) admin role to a group:

1. As an account admin, log in to the [account console](https://accounts.cloud.databricks.com/).
2. Click **Catalog**.
3. Click the name of a [Metastore](/concepts/metastore.md) to open its properties.
4. Under **Metastore Admin**, click **Edit**.
5. Select a group from the drop-down (you can type to search).
6. Click **Save**.

It can take up to 30 seconds for the assignment change to be reflected in your account, and longer to take effect in some workspaces due to caching protocols. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Related concepts

- [Account admins](/concepts/account-admin-unity-catalog.md)
- [Workspace admins](/concepts/workspace-admins-unity-catalog.md)
- [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Managing privileges in Unity Catalog](/concepts/manage-privilege-in-unity-catalog.md)

## Sources

- admin-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [admin-privileges-in-unity-catalog-databricks-on-aws.md](/references/admin-privileges-in-unity-catalog-databricks-on-aws-a7ab7fd7.md)
