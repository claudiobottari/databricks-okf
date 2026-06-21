---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: db9cf3e115976825f7a44c851e4a82810f3585756338748d1d1992f9901c27e2
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-store-access-control-permissions-legacy
    - FSACP(
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: Feature Store Access Control Permissions (Legacy)
description: Three permission levels (CAN VIEW METADATA, CAN EDIT METADATA, CAN MANAGE) that control granular access to feature table metadata in Databricks Feature Store workspaces not using Unity Catalog.
tags:
  - databricks
  - access-control
  - feature-store
timestamp: "2026-06-18T10:36:50.193Z"
---

# Feature Store Access Control Permissions (Legacy)

**Feature Store Access Control Permissions (Legacy)** describes how to manage permissions on feature tables in Databricks workspaces that are **not** enabled for [Unity Catalog](/concepts/unity-catalog.md). For workspaces that are Unity Catalog-enabled, use [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md) instead. ^[access-control-legacy-databricks-on-aws.md]

## Permission Levels

Three permission levels control access to feature table metadata. Any user can create a new feature table, but the creator is automatically assigned the highest level. The table below summarises the abilities granted at each level:

| Permission Level | Abilities |
|---|---|
| **CAN VIEW METADATA** | View the feature table in the UI. |
| **CAN EDIT METADATA** | View and edit the feature table description and other metadata. |
| **CAN MANAGE** | View, edit, and delete the feature table; manage other users' permissions on the table. |

^[access-control-legacy-databricks-on-aws.md]

## Default Permissions

When a feature table is created:

- The creator receives **CAN MANAGE** permission.
- Workspace admins receive **CAN MANAGE** permission.
- All other users receive **NO PERMISSIONS**.

^[access-control-legacy-databricks-on-aws.md]

## Configuring Permissions

### For a Single Feature Table

1. On the feature table page, click the arrow to the right of the feature table name and select **Permissions**. (This option is visible only if you have **CAN MANAGE** permission on that feature table.)
2. Edit the permissions as desired.
3. Click **Save**.

![Select permissions from drop-down menu](https://docs.databricks.com/aws/en/assets/images/feature-store-permissions-840e0dfb9dce73d02e7e520219a4b652.png)

^[access-control-legacy-databricks-on-aws.md]

### For All Feature Tables at the Feature Store Level

Workspace administrators (and any user with **CAN MANAGE** permission for the Feature Store) can set a default permission level that applies to all existing and future feature tables.

1. On the Feature Store (home) page, click **Permissions**.
2. Edit the permissions and click **Save**.

![Permissions button on Feature Store page](https://docs.databricks.com/aws/en/assets/images/feature-store-wide-permissions-65c0edf83a192ef0b3b1adf7395003e8.png)

Permissions set from the Feature Store page can only be removed from that page. On an individual feature table page, you can add further permissions on top of the inherited settings, but you **cannot** set more restrictive permissions than those inherited. Inherited permissions are marked with the note “Some permissions cannot be removed because they are inherited.” ^[access-control-legacy-databricks-on-aws.md]

## Important Notes

- A user with **CAN MANAGE** permission for the Feature Store can change permissions for all other users from the Feature Store page.
- Workspace administrators can always access the Feature Store permissions page regardless of their individual feature table permissions. ^[access-control-legacy-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md) – The workspace-level feature store that this access control applies to.
- [Unity Catalog](/concepts/unity-catalog.md) – The modern data governance solution that replaces legacy access control for feature tables.
- Workspace admin – Role with full management capabilities over the Feature Store.

## Sources

- access-control-legacy-databricks-on-aws.md

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
