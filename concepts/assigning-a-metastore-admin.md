---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 10294315b378bd1a33fbbf8d00fe9a820ea9db9236edfc719fd7e3bc8d627963
  pageDirectory: concepts
  sources:
    - admin-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - assigning-a-metastore-admin
    - AAMA
    - Assign a metastore admin
  citations:
    - file: admin-privileges-in-unity-catalog-databricks-on-aws.md
    - file: |-
        admin-privileges-in-unity-catalog-databricks-on-aws.md>

        ### Propagation Delay

        It can take up to 30 seconds for a metastore admin assignment change to be reflected in your account
    - file: and it may take longer to take effect in some workspaces than others. This delay is due to caching protocols. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md
title: Assigning a Metastore Admin
description: The process by which account admins assign the metastore admin role to a user, service principal, or group (groups recommended), with changes taking up to 30 seconds plus caching delays.
tags:
  - unity-catalog
  - admin-roles
  - databricks
timestamp: "2026-06-19T22:00:51.993Z"
---

# Assigning a [Metastore](/concepts/metastore.md) Admin

A **metastore admin** is an optional but highly privileged role in [Unity Catalog](/concepts/unity-catalog.md) that governs data access, ownership, and top-level securable objects within a single [Metastore](/concepts/metastore.md). Understanding how to assign this role is critical for managing permissions across your Databricks deployment. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## When to Assign a [Metastore](/concepts/metastore.md) Admin

For workspaces created after November 8, 2023, the [Metastore](/concepts/metastore.md) admin role is optional because [workspace admins](/concepts/workspace-admins-unity-catalog.md) receive sufficient metastore-level privileges by default. However, a [Metastore](/concepts/metastore.md) admin is required in the following situations: ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

- **Changing ownership** of objects or granting privileges on objects you do not own. For example, this is needed when taking over a catalog after the original owning account is removed. Workspace admins can create objects but cannot make grants on or change ownership of existing objects they do not own. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]
- **Removing** default workspace admin permissions. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]
- **Adding managed storage** to the [Metastore](/concepts/metastore.md) if it has none. This also requires an account admin to add the storage location to the [Metastore](/concepts/metastore.md) definition. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]
- **Enabling default access request destinations** for objects that don't have destinations explicitly set. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Initial [Metastore](/concepts/metastore.md) Admin

Who holds the initial [Metastore](/concepts/metastore.md) admin privileges depends on how the [Metastore](/concepts/metastore.md) was created: ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

- **Manual creation by an account admin**: The creating account admin becomes the [Metastore](/concepts/metastore.md)'s initial owner and [Metastore](/concepts/metastore.md) admin. All metastores created before November 8, 2023 were created manually. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]
- **Automatic Unity Catalog enablement**: The [Metastore](/concepts/metastore.md) is created without a [Metastore](/concepts/metastore.md) admin. Workspace admins are automatically granted privileges that make the [Metastore](/concepts/metastore.md) admin role optional. Account admins can assign the role if needed. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## How to Assign a [Metastore](/concepts/metastore.md) Admin

Only [account admins](/concepts/account-admin-unity-catalog.md) can assign the [Metastore](/concepts/metastore.md) admin role. Databricks recommends nominating a **group** as the [Metastore](/concepts/metastore.md) admin. By doing this, any member of the group is automatically a [Metastore](/concepts/metastore.md) admin. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

To assign the [Metastore](/concepts/metastore.md) admin role to a group:

1. As an account admin, log in to the [account console](https://accounts.cloud.databricks.com/). ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]
2. Click **Catalog**. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]
3. Click the name of a [Metastore](/concepts/metastore.md) to open its properties. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]
4. Under **Metastore Admin**, click **Edit**. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]
5. Select a group from the drop-down. You can enter text in the field to search for options. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]
6. Click **Save**. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md>

### Propagation Delay

It can take up to 30 seconds for a metastore admin assignment change to be reflected in your account, and it may take longer to take effect in some workspaces than others. This delay is due to caching protocols. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## [Metastore](/concepts/metastore.md) Admin Privileges

[Metastore](/concepts/metastore.md) admins have privileges from two sources: default privileges granted by the role, and ownership privileges because they are the owners of the [Metastore](/concepts/metastore.md). Specific privilege details are documented in the relevant [Unity Catalog permissions](/concepts/unity-catalog-permissions-model.md) guides. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution for managing metastores and permissions.
- [Account admins](/concepts/account-admin-unity-catalog.md) — The only role that can assign [Metastore](/concepts/metastore.md) admins.
- [Workspace admins](/concepts/workspace-admins-unity-catalog.md) — Receive default privileges that may make the [Metastore](/concepts/metastore.md) admin role optional.
- [Unity Catalog permissions](/concepts/unity-catalog-permissions-model.md) — Detailed management of privileges across securable objects.
- [Metastore](/concepts/metastore.md) — The top-level container for all Unity Catalog metadata.

## Sources

- admin-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [admin-privileges-in-unity-catalog-databricks-on-aws.md](/references/admin-privileges-in-unity-catalog-databricks-on-aws-a7ab7fd7.md)
2. admin-privileges-in-unity-catalog-databricks-on-aws.md>

### Propagation Delay

It can take up to 30 seconds for a metastore admin assignment change to be reflected in your account
3. and it may take longer to take effect in some workspaces than others. This delay is due to caching protocols. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md
