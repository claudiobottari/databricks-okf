---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 67322c3400026dfe8d39649017f10c05610a657f2651c8a4fee7689ecfcaa9df
  pageDirectory: concepts
  sources:
    - admin-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metastore-admins-unity-catalog
    - MA(C
  citations:
    - file: admin-privileges-in-unity-catalog-databricks-on-aws.md
title: Metastore admins (Unity Catalog)
description: Optional but highly privileged role governing data access, ownership, and top-level Unity Catalog securable objects within a single metastore.
tags:
  - unity-catalog
  - admin-roles
  - databricks
timestamp: "2026-06-18T14:20:22.701Z"
---

# [Metastore](/concepts/metastore.md) admins (Unity Catalog)

**Metastore admins** are an optional but highly privileged role in [Unity Catalog](/concepts/unity-catalog.md) that governs data access, ownership, and top-level Unity Catalog securable objects within a single [Metastore](/concepts/metastore.md). Unlike [account admins](/concepts/account-admins-unity-catalog.md) and [workspace admins](/concepts/workspace-admins-unity-catalog.md), the [Metastore](/concepts/metastore.md) admin role is not required for all deployments. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Role Overview

From a Unity Catalog permissions perspective, the three most important administrator roles are account admins, workspace admins, and [Metastore](/concepts/metastore.md) admins. Account admins and workspace admins are required for all deployments, while the [Metastore](/concepts/metastore.md) admin role is optional. Understanding each role's responsibilities helps you assign admins with the right scope. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

- **Account admins** operate at the Databricks account level. They create and link metastores and workspaces, and can assign admin roles.
- **Workspace admins** operate within a single workspace. They manage workspace membership, jobs, and workspace objects.
- **Metastore admins** operate within a single Unity Catalog [Metastore](/concepts/metastore.md). They govern data access, ownership, and top-level Unity Catalog securable objects.

^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## When to Assign a [Metastore](/concepts/metastore.md) Admin

For workspaces created after November 8, 2023, the [Metastore](/concepts/metastore.md) admin role is optional. This is because workspace admins receive sufficient metastore-level privileges by default. However, you must assign a [Metastore](/concepts/metastore.md) admin if you need to perform the following actions: ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

- Change ownership of objects or grant privileges on objects that you do not own. For example, this is required when taking over a catalog after the original owning account is removed. Workspace admins can create objects but cannot make grants on or change ownership of existing objects they do not own.
- Remove default workspace admin permissions.
- Add managed storage to the [Metastore](/concepts/metastore.md), if it has none. This requires an account admin to add the storage location to the [Metastore](/concepts/metastore.md) definition.
- Enable default access request destinations for objects that don't have destinations explicitly set.

^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Default [Metastore](/concepts/metastore.md) Admin Privileges

[Metastore](/concepts/metastore.md) admins have privileges from two sources: default privileges granted by the role, and ownership privileges because they are the owners of the [Metastore](/concepts/metastore.md). ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

The default privileges assigned to [Metastore](/concepts/metastore.md) admins on the [Metastore](/concepts/metastore.md) include ownership-level capabilities such as managing permissions, transferring ownership, and controlling top-level securable objects. As owners of the [Metastore](/concepts/metastore.md), [Metastore](/concepts/metastore.md) admins have full control over the [Metastore](/concepts/metastore.md)'s configuration and the objects within it. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Initial [Metastore](/concepts/metastore.md) Admin Assignment

The initial [Metastore](/concepts/metastore.md) admin depends on how the [Metastore](/concepts/metastore.md) was created: ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

- **Manual creation by account admin:** If an account admin creates the [Metastore](/concepts/metastore.md) manually, that account admin is the [Metastore](/concepts/metastore.md)'s initial owner and [Metastore](/concepts/metastore.md) admin. All metastores created before November 8, 2023 were created manually by an account admin.
- **Automatic Unity Catalog enablement:** If the [Metastore](/concepts/metastore.md) was provisioned as part of automatic Unity Catalog enablement, the [Metastore](/concepts/metastore.md) was created without a [Metastore](/concepts/metastore.md) admin. Workspace admins in that case are automatically granted privileges that make the [Metastore](/concepts/metastore.md) admin optional. If needed, account admins can assign the [Metastore](/concepts/metastore.md) admin role to a user, service principal, or group.

^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Assigning a [Metastore](/concepts/metastore.md) Admin

[Metastore](/concepts/metastore.md) admin is a highly privileged role that should be distributed carefully. Account admins can assign the [Metastore](/concepts/metastore.md) admin role. Databricks recommends nominating a group as the [Metastore](/concepts/metastore.md) admin, so any member of the group is automatically a [Metastore](/concepts/metastore.md) admin. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

To assign the [Metastore](/concepts/metastore.md) admin role to a group: ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

1. As an account admin, log in to the [account console](https://accounts.cloud.databricks.com/).
2. Click **Catalog**.
3. Click the name of a [Metastore](/concepts/metastore.md) to open its properties.
4. Under **Metastore Admin**, click **Edit**.
5. Select a group from the drop-down. You can enter text in the field to search for options.
6. Click **Save**.

It can take up to 30 seconds for a [Metastore](/concepts/metastore.md) admin assignment change to be reflected in your account, and it may take longer to take effect in some workspaces than others due to caching protocols. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Separation from Account Admins

Account admins and [Metastore](/concepts/metastore.md) admins are separate roles. When an account admin creates a [Metastore](/concepts/metastore.md), they become its initial [Metastore](/concepts/metastore.md) admin by default. They can then assign the [Metastore](/concepts/metastore.md) admin role to a different user, group, or service principal and relinquish it themselves. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that uses [Metastore](/concepts/metastore.md) admins
- [Account admins](/concepts/account-admins-unity-catalog.md) — The account-level admin role that can assign [Metastore](/concepts/metastore.md) admins
- [Workspace admins](/concepts/workspace-admins-unity-catalog.md) — The workspace-level admin role with default [Metastore](/concepts/metastore.md) privileges
- [Metastore](/concepts/metastore.md) — The Unity Catalog container that [Metastore](/concepts/metastore.md) admins govern
- [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md) — The permission system managed by [Metastore](/concepts/metastore.md) admins

## Sources

- admin-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [admin-privileges-in-unity-catalog-databricks-on-aws.md](/references/admin-privileges-in-unity-catalog-databricks-on-aws-a7ab7fd7.md)
