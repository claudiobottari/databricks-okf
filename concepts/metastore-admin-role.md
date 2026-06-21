---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d358c10769163370b20a5a390bafc3627c3d439f45ecf7aa905308b798d541b2
  pageDirectory: concepts
  sources:
    - admin-privileges-in-unity-catalog-databricks-on-aws.md
    - create-a-unity-catalog-metastore-databricks-on-aws.md
    - manage-unity-catalog-metastores-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - metastore-admin-role
    - MAR
    - Metastore Admin
    - Metastore Admins
    - Metastore admin
    - metastore admin
    - metastore admins
    - Metastore Administration
    - Metastore admin|metastore admins
    - metastore-admin-role-unity-catalog
    - MAR(C
    - metastore-admin-unity-catalog
    - MA(C
    - metastore-admins-in-unity-catalog
    - MAIUC
    - metastore-admins-unity-catalog
  citations:
    - file: create-a-unity-catalog-metastore-databricks-on-aws.md
    - file: admin-privileges-in-unity-catalog-databricks-on-aws.md
title: Metastore Admin Role
description: An optional, highly privileged Unity Catalog role that governs data access, ownership, and top-level securable objects; required for specific actions like changing ownership or removing default workspace admin permissions.
tags:
  - unity-catalog
  - metastore-admin
  - admin-roles
timestamp: "2026-06-19T17:28:20.562Z"
---

# [Metastore](/concepts/metastore.md) Admin Role

The **Metastore Admin** is the owner and highest-level administrator of a Unity Catalog [Metastore](/concepts/metastore.md). This role is automatically assigned to the user who creates the [Metastore](/concepts/metastore.md) — typically a Databricks account admin — and carries full privileges to manage the [Metastore](/concepts/metastore.md), its objects, and data-access permissions.^[create-a-unity-catalog-metastore-databricks-on-aws.md] The [Metastore](/concepts/metastore.md) admin is an optional role; for workspaces created after November 8, 2023, workspace admins receive sufficient metastore-level privileges by default, making the [Metastore](/concepts/metastore.md) admin role unnecessary in many deployments.^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Responsibilities and Privileges

[Metastore](/concepts/metastore.md) admins have privileges from two sources: **default privileges** granted by the role and **ownership privileges** because they are the owners of the [Metastore](/concepts/metastore.md).^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

- **Default privileges** include the ability to create top‑level objects such as [catalogs](/concepts/unity-catalog.md), schemas, [external locations](/concepts/external-location.md), and storage credentials, as well as manage access to tables and other securable objects.
- **Ownership privileges** grant full control over the [Metastore](/concepts/metastore.md) itself, including the ability to transfer ownership, change object owners, and grant or revoke privileges on any object in the [Metastore](/concepts/metastore.md).

Because of these broad powers, Databricks recommends that the [Metastore](/concepts/metastore.md) admin role be assigned to a group rather than an individual user, ensuring continuity and simplifying privilege management.^[create-a-unity-catalog-metastore-databricks-on-aws.md, admin-privileges-in-unity-catalog-databricks-on-aws.md]

## When to Assign a [Metastore](/concepts/metastore.md) Admin

For workspaces that were enabled for Unity Catalog automatically (all workspaces created after November 8, 2023), the [Metastore](/concepts/metastore.md) admin role is optional because workspace admins already have privileges to create catalogs, external locations, and other metastore‑level objects. However, a [Metastore](/concepts/metastore.md) admin **must** be assigned in the following situations:^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

- Changing ownership of objects or granting privileges on objects that the current user does not own (e.g., taking over a catalog after the original owning account is removed).
- Removing the default workspace admin permissions on the [Metastore](/concepts/metastore.md).
- Adding managed storage to a [Metastore](/concepts/metastore.md) that has none (requires an account admin to add the storage location).
- Enabling default access request destinations for objects that do not have destinations explicitly set.

## Who Has Initial [Metastore](/concepts/metastore.md) Admin Privileges?

If an account admin creates the [Metastore](/concepts/metastore.md) manually, that account admin becomes the metastore’s initial owner and [Metastore](/concepts/metastore.md) admin. All metastores created before November 8, 2023 were created manually by an account admin. If the [Metastore](/concepts/metastore.md) was provisioned automatically as part of Unity Catalog’s automatic enablement, it is created without a [Metastore](/concepts/metastore.md) admin. In that case, an account admin can assign the role to a user, service principal, or group as needed.^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Assigning the [Metastore](/concepts/metastore.md) Admin Role

Account admins can assign the [Metastore](/concepts/metastore.md) admin role through the Databricks account console. Databricks strongly recommends nominating a group rather than an individual. To assign:^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

1. As an account admin, log in to the [account console](https://accounts.cloud.databricks.com/).
2. Click **Catalog**.
3. Click the name of the [Metastore](/concepts/metastore.md) to open its properties.
4. Under **Metastore Admin**, click **Edit**.
5. Select a group (or user) from the drop‑down.
6. Click **Save**.

It can take up to 30 seconds for the change to be reflected in the account, and slightly longer to take effect in some workspaces due to caching protocols.^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Account Admin](/concepts/account-admin-unity-catalog.md) — The role that creates metastores and can assign the [Metastore](/concepts/metastore.md) admin.
- [Workspace Admin](/concepts/workspace-admin-unity-catalog.md) — A separate role that, in automatically‑enabled workspaces, receives many [Metastore](/concepts/metastore.md) privileges by default.
- [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) — The top‑level container for data governance in Unity Catalog.
- Group — Recommended principal type for holding the [Metastore](/concepts/metastore.md) admin role.
- [Manage Unity Catalog Metastores](/concepts/unity-catalog-metastore.md) — How to update, delete, and configure metastores.

## Sources

- create-a-unity-catalog-metastore-databricks-on-aws.md
- admin-privileges-in-unity-catalog-databricks-on-aws.md
- manage-unity-catalog-metastores-databricks-on-aws.md (referenced for the optional nature of the role)

# Citations

1. [create-a-unity-catalog-metastore-databricks-on-aws.md](/references/create-a-unity-catalog-metastore-databricks-on-aws-f0a3d0e9.md)
2. [admin-privileges-in-unity-catalog-databricks-on-aws.md](/references/admin-privileges-in-unity-catalog-databricks-on-aws-a7ab7fd7.md)
