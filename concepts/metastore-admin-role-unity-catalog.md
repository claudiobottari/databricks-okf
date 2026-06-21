---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 42afca4a306e7b4bbfa01c788af09218e1e20f6f8b8f02fd3ca4320fd454d97b
  pageDirectory: concepts
  sources:
    - admin-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metastore-admin-role-unity-catalog
    - MAR(C
  citations:
    - file: admin-privileges-in-unity-catalog-databricks-on-aws.md
title: Metastore Admin Role (Unity Catalog)
description: An optional but highly privileged Unity Catalog role that governs data access, ownership, and top-level securable objects within a metastore.
tags:
  - unity-catalog
  - admin-roles
  - data-governance
timestamp: "2026-06-19T08:53:49.923Z"
---

# [Metastore](/concepts/metastore.md) Admin Role (Unity Catalog)

The **Metastore Admin** is an optional but highly privileged role in [Unity Catalog](/concepts/unity-catalog.md) that governs data access, ownership, and top-level Unity Catalog securable objects within a single [Metastore](/concepts/metastore.md). [Metastore](/concepts/metastore.md) admins are distinct from [Account admin](/concepts/account-admin-unity-catalog.md) and Workspace admin roles. Understanding when to assign a [Metastore](/concepts/metastore.md) admin is critical for managing data governance and object ownership at the [Metastore](/concepts/metastore.md) level. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Default [Metastore](/concepts/metastore.md) Admin Privileges

[Metastore](/concepts/metastore.md) admins receive privileges from two sources: **default privileges granted by the role** and **ownership privileges** because they are the default owners of the [Metastore](/concepts/metastore.md). The default privileges include the ability to perform administrative actions on the [Metastore](/concepts/metastore.md), such as managing grants and ownership of objects across all catalogs and schemas within the [Metastore](/concepts/metastore.md). ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

As **owners** of the [Metastore](/concepts/metastore.md), [Metastore](/concepts/metastore.md) admins have full control over the [Metastore](/concepts/metastore.md) itself, including the ability to change ownership of the [Metastore](/concepts/metastore.md) and grant or revoke privileges on the [Metastore](/concepts/metastore.md). This ownership also confers the privileges to manage any securable object in the [Metastore](/concepts/metastore.md) that does not have an explicit owner. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## When to Assign a [Metastore](/concepts/metastore.md) Admin

For workspaces created after November 8, 2023, the [Metastore](/concepts/metastore.md) admin role is **optional** because workspace admins receive sufficient metastore-level privileges by default (see [Workspace Admin Privileges in Unity Catalog](/concepts/workspace-admin-privileges-in-unity-catalog.md)). However, you must assign a [Metastore](/concepts/metastore.md) admin if you need to perform any of the following actions: ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

- **Change ownership** of objects or grant privileges on objects that you do not own. For example, this is required when taking over a catalog after the original owning account is removed. Workspace admins can create objects but cannot make grants on or change ownership of existing objects they do not own. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]
- **Remove default workspace admin permissions** that were automatically granted when the workspace was enabled for Unity Catalog. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]
- **Add managed storage to the metastore**, if it has none. (This requires an account admin to add the storage location to the [Metastore](/concepts/metastore.md) definition.) ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]
- **Enable default access request destinations** for objects that don't have destinations explicitly set. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Initial [Metastore](/concepts/metastore.md) Admin Assignment

If an account admin **manually creates** the [Metastore](/concepts/metastore.md), that account admin becomes the [Metastore](/concepts/metastore.md)'s initial owner and [Metastore](/concepts/metastore.md) admin. All metastores created before November 8, 2023 were created manually by an account admin. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

If the [Metastore](/concepts/metastore.md) was **provisioned as part of automatic Unity Catalog enablement**, the [Metastore](/concepts/metastore.md) was created without a [Metastore](/concepts/metastore.md) admin. Workspace admins in that case are automatically granted privileges that make the [Metastore](/concepts/metastore.md) admin optional. If needed, account admins can assign the [Metastore](/concepts/metastore.md) admin role to a user, service principal, or group. Groups are strongly recommended. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Assigning a [Metastore](/concepts/metastore.md) Admin

Only **account admins** can assign the [Metastore](/concepts/metastore.md) admin role. Databricks recommends nominating a **group** as the [Metastore](/concepts/metastore.md) admin. By doing this, any member of the group is automatically a [Metastore](/concepts/metastore.md) admin. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

To assign the [Metastore](/concepts/metastore.md) admin role to a group:

1. As an account admin, log in to the [account console](https://accounts.cloud.databricks.com/).
2. Click **Catalog**.
3. Click the name of a [Metastore](/concepts/metastore.md) to open its properties.
4. Under **Metastore Admin**, click **Edit**.
5. Select a group from the drop-down. You can enter text in the field to search for options.
6. Click **Save**.

^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

### Caching Delay

It can take up to 30 seconds for a [Metastore](/concepts/metastore.md) admin assignment change to be reflected in your account, and it may take longer to take effect in some workspaces than others. This delay is due to caching protocols. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Account admin](/concepts/account-admin-unity-catalog.md) – Higher-level role that manages the entire Databricks account.
- Workspace admin – Role that manages a single workspace, with default privileges on the attached [Metastore](/concepts/metastore.md).
- [Unity Catalog](/concepts/unity-catalog.md) – The data governance catalog system.
- [Metastore](/concepts/metastore.md) – The top-level container for Unity Catalog objects.
- Privilege management in Unity Catalog – How grants and ownership are handled.

## Sources

- admin-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [admin-privileges-in-unity-catalog-databricks-on-aws.md](/references/admin-privileges-in-unity-catalog-databricks-on-aws-a7ab7fd7.md)
