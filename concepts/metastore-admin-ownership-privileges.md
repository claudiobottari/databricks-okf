---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 29b2bb72b851e54044bce549dc5dc9fdefdc72da48043067cd903de1ce118ead
  pageDirectory: concepts
  sources:
    - admin-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metastore-admin-ownership-privileges
    - MAOP
    - Metastore admin privileges
    - Metastore admin privileges|Metastore admins (optional)
  citations:
    - file: admin-privileges-in-unity-catalog-databricks-on-aws.md
title: Metastore admin ownership privileges
description: Default and ownership-based privileges granted to metastore admins as owners of the metastore, including the ability to manage any object in the metastore.
tags:
  - unity-catalog
  - admin-roles
  - databricks
timestamp: "2026-06-18T14:20:33.895Z"
---

# [Metastore](/concepts/metastore.md) admin ownership privileges

**Metastore admin ownership privileges** refers to the two categories of [Unity Catalog](/concepts/unity-catalog.md) permissions that a [Metastore](/concepts/metastore.md) admin holds by virtue of their role: default privileges granted automatically to the role, and ownership privileges that come from being the owner of the [Metastore](/concepts/metastore.md). The [Metastore](/concepts/metastore.md) admin is an optional but highly privileged user, group, or service principal that governs data access, ownership, and top-level Unity Catalog securable objects within a single [Metastore](/concepts/metastore.md). ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Default [Metastore](/concepts/metastore.md) admin privileges

[Metastore](/concepts/metastore.md) admins receive a set of default privileges on the [Metastore](/concepts/metastore.md) itself. These privileges are automatically granted when the role is assigned and cover operations that affect the entire [Metastore](/concepts/metastore.md), such as managing catalogs, external locations, and other global objects. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Ownership privileges

Because the [Metastore](/concepts/metastore.md) admin is the owner of the [Metastore](/concepts/metastore.md), they also hold ownership-level privileges. Ownership allows the [Metastore](/concepts/metastore.md) admin to change ownership of any object in the [Metastore](/concepts/metastore.md), grant or revoke privileges on objects they do not otherwise own, and transfer ownership of the [Metastore](/concepts/metastore.md) itself. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## When a [Metastore](/concepts/metastore.md) admin is needed

The [Metastore](/concepts/metastore.md) admin role is optional for workspaces created after November 8, 2023, which are automatically enabled for Unity Catalog. In those workspaces, [workspace admin](/concepts/workspace-admin-unity-catalog.md)s already receive sufficient metastore-level privileges by default, including `CREATE CATALOG` and other top-level permissions. However, a [Metastore](/concepts/metastore.md) admin must be assigned for the following actions: ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

- Changing ownership of objects or granting privileges on objects that the requesting user does not own.
- Removing default workspace admin permissions on the [Metastore](/concepts/metastore.md).
- Adding managed storage to the [Metastore](/concepts/metastore.md) when it has none (requires an account admin to add the storage location to the [Metastore](/concepts/metastore.md) definition).
- Enabling default access request destinations for objects that do not have destinations explicitly set. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Initial [Metastore](/concepts/metastore.md) admin assignment

If an [account admin](/concepts/account-admin-unity-catalog.md) creates the [Metastore](/concepts/metastore.md) manually, that account admin becomes the [Metastore](/concepts/metastore.md)'s initial owner and [Metastore](/concepts/metastore.md) admin. Metastores provisioned as part of automatic Unity Catalog enablement are created without any [Metastore](/concepts/metastore.md) admin; workspace admins in that case automatically receive privileges that make a dedicated [Metastore](/concepts/metastore.md) admin optional. If needed, account admins may later assign a [Metastore](/concepts/metastore.md) admin to a user, service principal, or group. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Assigning a [Metastore](/concepts/metastore.md) admin

Only account admins can assign the [Metastore](/concepts/metastore.md) admin role. Databricks recommends using a group as the [Metastore](/concepts/metastore.md) admin so that any member of the group automatically holds the role. To assign the role: ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

1. Log in to the account console as an account admin.
2. Click **Catalog**.
3. Select the [Metastore](/concepts/metastore.md).
4. Under **Metastore Admin**, click **Edit**.
5. Choose a group from the drop-down (search is available).
6. Click **Save**.

Changes can take up to 30 seconds to be reflected in the account and may take longer to propagate across workspaces due to caching. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Related concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [account admin](/concepts/account-admin-unity-catalog.md)
- [workspace admin](/concepts/workspace-admin-unity-catalog.md)
- [Metastore](/concepts/metastore.md)
- privileges in Unity Catalog

## Sources

- admin-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [admin-privileges-in-unity-catalog-databricks-on-aws.md](/references/admin-privileges-in-unity-catalog-databricks-on-aws-a7ab7fd7.md)
