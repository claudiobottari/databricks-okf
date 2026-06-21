---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bbe2b7fb4b68f4c093b3c3fed03d5a798b066f6894f4836525d1134d61a6fe2a
  pageDirectory: concepts
  sources:
    - admin-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metastore-admin-role-assignment
    - MARA
    - Metastore auto-assign
  citations:
    - file: admin-privileges-in-unity-catalog-databricks-on-aws.md
title: Metastore admin role assignment
description: Process and considerations for assigning the metastore admin role via the account console, with recommendations to use groups and awareness of caching delays.
tags:
  - unity-catalog
  - admin-roles
  - databricks
timestamp: "2026-06-18T14:20:11.051Z"
---

# [Metastore](/concepts/metastore.md) admin role assignment

**Metastore admin role assignment** refers to the process of designating a user, group, or service principal as the [Metastore](/concepts/metastore.md) administrator for a [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md). The [Metastore](/concepts/metastore.md) admin is an optional but highly privileged role in Unity Catalog that grants default administrative privileges on the [Metastore](/concepts/metastore.md) and ownership over it. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## When to assign

For workspaces created after November 8, 2023 (which are auto‑enabled for Unity Catalog), the [Metastore](/concepts/metastore.md) admin role is optional because workspace admins already receive sufficient metastore-level privileges by default. However, you must assign a [Metastore](/concepts/metastore.md) admin if you need to perform any of the following actions:

- Change ownership of objects or grant privileges on objects that you do not own (for example, taking over a catalog after the original owning account is removed). Workspace admins can create objects but cannot make grants on or change ownership of existing objects they do not own.
- Remove default workspace admin permissions.
- Add managed storage to the [Metastore](/concepts/metastore.md) (this also requires an account admin to add the storage location to the [Metastore](/concepts/metastore.md) definition).
- Enable default access request destinations for objects that lack explicit destinations.

^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Default privileges

[Metastore](/concepts/metastore.md) admins receive default privileges on the [Metastore](/concepts/metastore.md) by virtue of the role. Additionally, because the [Metastore](/concepts/metastore.md) admin is the owner of the [Metastore](/concepts/metastore.md), they also inherit ownership privileges. The source document enumerates these default privileges (not repeated here to avoid verbatim copying) — they include the ability to govern top‑level Unity Catalog securable objects, manage data access, and transfer ownership. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Initial assignment

If an account admin manually creates the [Metastore](/concepts/metastore.md), that account admin becomes the metastore’s initial owner and [Metastore](/concepts/metastore.md) admin. This applies to all metastores created before November 8, 2023.

If the [Metastore](/concepts/metastore.md) was provisioned as part of automatic Unity Catalog enablement (workspaces created after November 8, 2023), the [Metastore](/concepts/metastore.md) was created without a [Metastore](/concepts/metastore.md) admin. In this case, workspace admins receive automatic privileges that make the [Metastore](/concepts/metastore.md) admin optional. If needed, account admins can later assign the [Metastore](/concepts/metastore.md) admin role to a user, service principal, or group — Databricks strongly recommends using a group. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## How to assign

Only **account admins** can assign the [Metastore](/concepts/metastore.md) admin role. The recommended practice is to nominate a **group** as the [Metastore](/concepts/metastore.md) admin so that any member of the group automatically becomes a [Metastore](/concepts/metastore.md) admin.

To assign the [Metastore](/concepts/metastore.md) admin role to a group:

1. Log in to the [account console](https://accounts.cloud.databricks.com/) as an account admin.
2. Click the **Catalog** icon.
3. Click the name of the [Metastore](/concepts/metastore.md) to open its properties.
4. Under **Metastore Admin**, click **Edit**.
5. Select a group from the drop-down (you can type to search).
6. Click **Save**.

^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Caching considerations

It can take up to 30 seconds for a [Metastore](/concepts/metastore.md) admin assignment change to be reflected in your account, and it may take longer to take effect in some workspaces than others. This delay is due to caching protocols. ^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Related concepts

- [Account admin](/concepts/account-admin-unity-catalog.md) — The role that assigns [Metastore](/concepts/metastore.md) admins
- Workspace admin — Workspace-level admin with related privileges
- [Unity Catalog](/concepts/unity-catalog.md) — The governance solution that uses metastores
- [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md) — The permission model for securable objects
- [Metastore admin](/concepts/metastore-admin-role.md) — The role itself

## Sources

- admin-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [admin-privileges-in-unity-catalog-databricks-on-aws.md](/references/admin-privileges-in-unity-catalog-databricks-on-aws-a7ab7fd7.md)
