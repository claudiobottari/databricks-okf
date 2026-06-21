---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dd3ddf918f1434a16a15c84ce2e814ce3971e719b05596cdd036a0ae5a552625
  pageDirectory: concepts
  sources:
    - admin-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - assigning-the-metastore-admin-role
    - ATMAR
    - Assign admin roles
  citations:
    - file: admin-privileges-in-unity-catalog-databricks-on-aws.md
title: Assigning the Metastore Admin Role
description: Process by which account admins assign the metastore admin role to a user, service principal, or group in the account console; Databricks recommends using a group. Changes may take up to 30 seconds to propagate due to caching.
tags:
  - unity-catalog
  - metastore-admin
  - administration
timestamp: "2026-06-19T13:54:47.188Z"
---

# Assigning the [Metastore](/concepts/metastore.md) Admin Role

The **metastore admin** is an optional but highly privileged role in [Unity Catalog](/concepts/unity-catalog.md). [Metastore](/concepts/metastore.md) admins operate within a single [Metastore](/concepts/metastore.md) and govern data access, ownership, and top-level Unity Catalog securable objects. Their privileges come from two sources: default grants that arrive with the role and ownership privileges derived from being the owners of the [Metastore](/concepts/metastore.md). ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## When to Assign a [Metastore](/concepts/metastore.md) Admin

For workspaces created after November 8, 2023, the [Metastore](/concepts/metastore.md) admin role is optional because workspace admins receive sufficient metastore-level privileges by default. However, you must assign a [Metastore](/concepts/metastore.md) admin if you need to perform any of the following actions: ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

- Change ownership of objects or grant privileges on objects you do not own (for example, when taking over a catalog after the original owning account is removed).
- Remove the default workspace admin permissions.
- Add managed storage to the [Metastore](/concepts/metastore.md) if it has none (this also requires an account admin to add the storage location to the [Metastore](/concepts/metastore.md) definition).
- Enable default access request destinations for objects that do not have destinations explicitly set. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Initial [Metastore](/concepts/metastore.md) Admin Assignment

If an account admin creates the [Metastore](/concepts/metastore.md) manually, that account admin becomes the metastore’s initial owner and [Metastore](/concepts/metastore.md) admin. All metastores created before November 8, 2023 were created manually by an account admin. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

If the [Metastore](/concepts/metastore.md) was provisioned as part of automatic Unity Catalog enablement (applies to all workspaces created after November 8, 2023), the [Metastore](/concepts/metastore.md) was created without a [Metastore](/concepts/metastore.md) admin. In that case, workspace admins are automatically granted sufficient privileges to make the [Metastore](/concepts/metastore.md) admin optional. When needed, account admins can later assign the [Metastore](/concepts/metastore.md) admin role to a user, service principal, or group. **Groups are strongly recommended.** ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## How to Assign a [Metastore](/concepts/metastore.md) Admin

Only account admins can assign the [Metastore](/concepts/metastore.md) admin role. Databricks recommends nominating a **group** as the [Metastore](/concepts/metastore.md) admin so that any member of the group automatically becomes a [Metastore](/concepts/metastore.md) admin. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

To assign the [Metastore](/concepts/metastore.md) admin role: ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

1.  As an account admin, log in to the [account console](https://accounts.cloud.databricks.com/).
2.  Click the **Catalog** icon.
3.  Click the name of the [Metastore](/concepts/metastore.md) to open its properties.
4.  Under **Metastore Admin**, click **Edit**.
5.  Select a group from the drop-down. You can type in the field to search for options.
6.  Click **Save**.

> **Important:** It can take up to 30 seconds for a [Metastore](/concepts/metastore.md) admin assignment change to be reflected in your account, and it may take longer to take effect in some workspaces than others. This delay is due to caching protocols. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Account Admins](/concepts/account-admins-unity-catalog.md) – The role that can assign [Metastore](/concepts/metastore.md) admins.
- Workspace Admins – A separate admin role that operates within a single workspace.
- [Unity Catalog](/concepts/unity-catalog.md) – The data governance platform where [Metastore](/concepts/metastore.md) admins operate.
- Managing Privileges in Unity Catalog – Broader topic on privilege management.
- [Metastore Administration](/concepts/metastore-admin-role.md) – General overview of [Metastore](/concepts/metastore.md) admin responsibilities.

## Sources

- admin-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [admin-privileges-in-unity-catalog-databricks-on-aws.md](/references/admin-privileges-in-unity-catalog-databricks-on-aws-a7ab7fd7.md)
