---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 077c61a0300834fd8631cab7c4e0f8a8d4c5fa1fdbe11a70025ec6811c1b91ed
  pageDirectory: concepts
  sources:
    - admin-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automatic-unity-catalog-enablement
    - AUCE
    - AUC
    - automatic-unity-catalog-enablement-and-workspace-admin-default-privileges
    - Workspace Admin Default Privileges and Automatic Unity Catalog Enablement
    - AUCEAWADP
  citations:
    - file: admin-privileges-in-unity-catalog-databricks-on-aws.md
    - file: enable-a-workspace-for-unity-catalog-databricks-on-aws.md
    - file: create-a-unity-catalog-metastore-databricks-on-aws.md
    - file: what-is-unity-catalog-databricks-on-aws.md
title: Automatic Unity Catalog Enablement
description: For workspaces created after November 8, 2023, Unity Catalog is auto-enabled with a metastore, eliminating the need for a separate metastore admin by granting workspace admins sufficient metastore-level privileges.
tags:
  - unity-catalog
  - workspace-setup
  - databricks
timestamp: "2026-06-19T21:59:54.795Z"
---

# Automatic Unity Catalog Enablement

**Automatic Unity Catalog enablement** is a Databricks feature that automatically provisions and attaches a Unity Catalog [Metastore](/concepts/metastore.md) to newly created workspaces, eliminating the need for manual configuration by an account admin. This feature began rolling out on November 8, 2023, and applies to all workspaces created after that date.^[admin-privileges-in-unity-catalog-databricks-on-aws.md, enable-a-workspace-for-unity-catalog-databricks-on-aws.md]

## Overview

When a workspace is automatically enabled for Unity Catalog, it is attached to a [Metastore](/concepts/metastore.md) by default, significantly simplifying the setup process. Prior to this feature, account admins were required to manually create or assign a [Metastore](/concepts/metastore.md) to each workspace after creation.^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md, create-a-unity-catalog-metastore-databricks-on-aws.md]

Unity Catalog is the unified governance layer built into Databricks that operates beneath every data interaction in workspaces, enforcing access control, tracking lineage, and logging activity.^[what-is-unity-catalog-databricks-on-aws.md]

## Workspace admin privileges with automatic enablement

In workspaces automatically enabled for Unity Catalog, workspace admins receive additional privileges on the attached [Metastore](/concepts/metastore.md) by default. These privileges include the ability to perform the following actions:^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

- `CREATE CATALOG`
- `CREATE CLEAN ROOM`
- `CREATE EXTERNAL LOCATION`
- `CREATE SERVICE CREDENTIAL`
- `CREATE STORAGE CREDENTIAL`
- `CREATE CONNECTION`
- `CREATE SHARE`
- `CREATE RECIPIENT`
- `CREATE PROVIDER`
- `CREATE MATERIALIZED VIEW`

Databricks represents these privilege grants with an auto-generated system group named `_workspace_admins_databricks_<account_id>_workspace_<workspace_id>`. These grants are visible in the [Metastore](/concepts/metastore.md)'s **Permissions** tab in the account console.^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

Additionally, workspace admins are the default owners of the workspace catalog, if a workspace catalog was provisioned for their workspace. Ownership of this catalog grants the ability to manage privileges for or transfer ownership of any object within the workspace catalog, including granting themselves read and write access to all data in the catalog (with granting permissions being audit-logged). Workspace admins can also transfer ownership of the workspace catalog itself.^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

All workspace users receive the `USE CATALOG` privilege on the workspace catalog. Workspace users also receive `USE SCHEMA`, `CREATE TABLE`, `CREATE VOLUME`, `CREATE MODEL`, `CREATE FUNCTION`, and `CREATE MATERIALIZED VIEW` privileges on the `default` schema in the catalog.^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## [Metastore](/concepts/metastore.md) admin role in automatically enabled workspaces

When the [Metastore](/concepts/metastore.md) is provisioned as part of automatic Unity Catalog enablement, it is created without a [Metastore](/concepts/metastore.md) admin. Because workspace admins receive sufficient metastore-level privileges by default, the [Metastore](/concepts/metastore.md) admin role becomes optional for these workspaces.^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

### When a [Metastore](/concepts/metastore.md) admin is needed

However, an account admin must assign a [Metastore](/concepts/metastore.md) admin if any of the following actions are needed:^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

- Changing ownership of objects or granting privileges on objects that the workspace admin does not own.
- Removing default workspace admin permissions.
- Adding managed storage to the [Metastore](/concepts/metastore.md), if it has none.
- Enabling default access request destinations for objects that don't have destinations explicitly set.

Account admins can assign the [Metastore](/concepts/metastore.md) admin role to a user, service principal, or group. Databricks strongly recommends nominating a group as the [Metastore](/concepts/metastore.md) admin.^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Creating a [Metastore](/concepts/metastore.md) manually

For workspaces that were not automatically enabled, an account admin must manually create a Unity Catalog [Metastore](/concepts/metastore.md). The manual process involves:^[create-a-unity-catalog-metastore-databricks-on-aws.md]

1. (Optional) Creating an S3 bucket for metastore-level storage of managed tables and volumes in your AWS account.
2. (Optional) Creating an IAM role that provides access to that storage location.
3. Creating the [Metastore](/concepts/metastore.md) in the Databricks account console, attaching the storage location, and assigning workspaces to it.

The user who creates a [Metastore](/concepts/metastore.md) manually becomes its owner and initial [Metastore](/concepts/metastore.md) admin. Databricks recommends reassigning the [Metastore](/concepts/metastore.md) admin role to a group.^[create-a-unity-catalog-metastore-databricks-on-aws.md]

## Comparison with manual enablement

| Aspect | Automatic enablement | Manual enablement |
|---|---|---|
| Workspace creation | Post-November 8, 2023 | Before November 8, 2023 |
| Setup effort | No action required | Account admin must create/assign [Metastore](/concepts/metastore.md) |
| [Metastore](/concepts/metastore.md) admin | Optional (not assigned by default) | Account admin is initial [Metastore](/concepts/metastore.md) admin and owner |
| Workspace admin privileges | Additional default privileges on [Metastore](/concepts/metastore.md) | No additional Unity Catalog privileges by default |
| User management | Must use account-level interfaces | May use workspace-level interfaces until migration |

^[admin-privileges-in-unity-catalog-databricks-on-aws.md, enable-a-workspace-for-unity-catalog-databricks-on-aws.md, create-a-unity-catalog-metastore-databricks-on-aws.md]

## Key considerations

- Automatic Unity Catalog enablement cannot be reversed. Once enabled, users, groups, and service principals must be managed using account-level interfaces, not workspace-level interfaces.^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md]
- The default privileges granted on the attached [Metastore](/concepts/metastore.md) and workspace catalog are not maintained across workspaces (if the workspace catalog is also bound to another workspace).^[admin-privileges-in-unity-catalog-databricks-on-aws.md]
- If your workspace was enabled for Unity Catalog automatically, the article on manually enabling workspaces and creating metastores does not apply.^[enable-a-workspace-for-unity-catalog-databricks-on-aws.md, create-a-unity-catalog-metastore-databricks-on-aws.md]
- Account admins can restrict workspace admin privileges using the `RestrictWorkspaceAdmins` setting.^[admin-privileges-in-unity-catalog-databricks-on-aws.md]

## Verification

To check if Unity Catalog is already enabled for your workspace, see the [Get started with Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/get-started) guide. Users must be on a workspace that is attached to a [Metastore](/concepts/metastore.md) in their region to work with Unity Catalog.^[what-is-unity-catalog-databricks-on-aws.md, create-a-unity-catalog-metastore-databricks-on-aws.md]

## Related concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The unified data governance layer that automatic enablement configures.
- [Metastore](/concepts/metastore.md) — The top-level container for Unity Catalog data and metadata.
- [Account Admin (Unity Catalog)](/concepts/account-admin-unity-catalog.md) — The role that manages metastores and workspaces at the account level.
- Workspace admin — The role that manages individual workspaces.
- [Metastore admin](/concepts/metastore-admin-role.md) — An optional role for managing Unity Catalog metadata permissions.
- [Catalog Explorer](/concepts/catalog-explorer.md) — The Databricks UI for discovering and managing data and AI assets.

## Sources

- admin-privileges-in-unity-catalog-databricks-on-aws.md
- enable-a-workspace-for-unity-catalog-databricks-on-aws.md
- create-a-unity-catalog-metastore-databricks-on-aws.md
- what-is-unity-catalog-databricks-on-aws.md

# Citations

1. [admin-privileges-in-unity-catalog-databricks-on-aws.md](/references/admin-privileges-in-unity-catalog-databricks-on-aws-a7ab7fd7.md)
2. [enable-a-workspace-for-unity-catalog-databricks-on-aws.md](/references/enable-a-workspace-for-unity-catalog-databricks-on-aws-e9f0e09a.md)
3. [create-a-unity-catalog-metastore-databricks-on-aws.md](/references/create-a-unity-catalog-metastore-databricks-on-aws-f0a3d0e9.md)
4. [what-is-unity-catalog-databricks-on-aws.md](/references/what-is-unity-catalog-databricks-on-aws-ea58b0e9.md)
