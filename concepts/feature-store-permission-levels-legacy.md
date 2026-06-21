---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 74bac440a99d6af6da647d417c229eada27ff8fff337f4f6721958a0d8ffdfc8
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-store-permission-levels-legacy
    - FSPL(
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: Feature Store Permission Levels (Legacy)
description: "Three permission levels for feature table metadata in Databricks Feature Store: CAN VIEW METADATA, CAN EDIT METADATA, and CAN MANAGE."
tags:
  - databricks
  - access-control
  - feature-store
timestamp: "2026-06-19T08:48:59.120Z"
---

# Feature Store Permission Levels (Legacy)

**Feature Store Permission Levels (Legacy)** define the access control model for [Feature Store](/concepts/feature-store.md) feature tables in Databricks workspaces that are **not** enabled for [Unity Catalog](/concepts/unity-catalog.md). Workspaces that use Unity Catalog should instead manage access via [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md). This legacy system controls a user’s ability to view feature table metadata, edit descriptions, manage permissions for other users, and delete a table. ^[access-control-legacy-databricks-on-aws.md]

## Permission Levels

Three permission levels are available for feature table metadata:

| Permission Level | Abilities |
|------------------|-----------|
| **CAN VIEW METADATA** | View the feature table's metadata in the UI. |
| **CAN EDIT METADATA** | Edit the feature table's description and other metadata. |
| **CAN MANAGE** | Manage permissions for other users on the table, edit metadata, and delete the table. |

Any user can create a new feature table. Upon creation, the table is automatically owned by the creator with CAN MANAGE permission. ^[access-control-legacy-databricks-on-aws.md]

## Default Permissions

When a feature table is created, the following defaults apply:

- The creator receives **CAN MANAGE** permission.
- Workspace administrators receive **CAN MANAGE** permission.
- All other users receive **NO PERMISSIONS** (no access at all).

^[access-control-legacy-databricks-on-aws.md]

## Configuring Permissions for a Specific Feature Table

1. On the feature table page, click the arrow to the right of the table name and select **Permissions**. This option is only visible if you have **CAN MANAGE** permission for that table.
2. In the permissions dialog, edit the users or groups and their assigned permission level.
3. Click **Save**.

^[access-control-legacy-databricks-on-aws.md]

## Configuring Permissions for All Feature Tables

Workspace administrators (or any user with **CAN MANAGE** permission for the entire Feature Store) can set default permission levels that apply to **all existing and future** feature tables.

1. On the Feature Store (main) page, click **Permissions** (only available to workspace admins or users with Feature Store–level CAN MANAGE).
2. Edit the permissions and click **Save**.

Permissions set at the Feature Store level are inherited by individual tables. On a specific table’s permission page, you can add permissions that are **more permissive** than the inherited ones, but you cannot set **more restrictive** permissions than those inherited from the Feature Store level. Inherited permissions are marked with the note: “Some permissions cannot be removed because they are inherited.” ^[access-control-legacy-databricks-on-aws.md]

## Limitations

- This access control model applies only to the legacy (non–Unity Catalog) Feature Store. If your workspace is enabled for Unity Catalog, use the Unity Catalog privilege model instead. ^[access-control-legacy-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — The recommended access control model for Unity Catalog–enabled workspaces.
- [Feature Store](/concepts/feature-store.md) — The repository for feature tables.
- [CAN MANAGE](/concepts/can-manage-permission.md) — The highest permission level, granting full administrative control over a feature table.

## Sources

- access-control-legacy-databricks-on-aws.md

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
