---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a56b0d590e495f4c300e4687088ba536ecedf265e65617a44c6220a5ced6a227
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-store-access-control-legacy
    - FSAC(
    - Feature Store Access Control
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: Feature Store Access Control (Legacy)
description: A permission system for controlling access to feature table metadata in Databricks workspaces not enabled for Unity Catalog
tags:
  - access-control
  - feature-store
  - databricks
timestamp: "2026-06-19T21:55:21.708Z"
---

# Feature Store Access Control (Legacy)

**Feature Store Access Control (Legacy)** governs permissions on [Feature Tables](/concepts/feature-tables.md) in Databricks workspaces that are **not** enabled for [Unity Catalog](/concepts/unity-catalog.md). Workspaces that are enabled for Unity Catalog should use [Unity Catalog privileges](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/) instead. ^[access-control-legacy-databricks-on-aws.md]

This legacy system allows fine-grained control over metadata access: who can view a feature table in the UI, edit its description, manage permissions for others, or delete the table. ^[access-control-legacy-databricks-on-aws.md]

## Permission Levels

The following three permission levels can be assigned to feature table metadata: ^[access-control-legacy-databricks-on-aws.md]

| Permission Level | Abilities |
|------------------|-----------|
| **CAN VIEW METADATA** | View the feature table in the UI. |
| **CAN EDIT METADATA** | Edit the feature table description and other metadata. |
| **CAN MANAGE** | Manage permissions for other users on the feature table, and delete the table. |

Any user can create a new feature table. ^[access-control-legacy-databricks-on-aws.md]

## Default Permissions

When a feature table is created, the following defaults apply: ^[access-control-legacy-databricks-on-aws.md]

- The creator is granted **CAN MANAGE** permission.
- Workspace admins are granted **CAN MANAGE** permission.
- All other users have **NO PERMISSIONS**.

## Configuring Permissions

### For a Single Feature Table

Only users with **CAN MANAGE** permission on the feature table can change its permissions. To do so: ^[access-control-legacy-databricks-on-aws.md]

1. On the feature table page, click the arrow to the right of the table name and select **Permissions**.
2. Edit the permissions and click **Save**.

If you do not have CAN MANAGE permission, the **Permissions** option is not visible. ^[access-control-legacy-databricks-on-aws.md]

### For All Feature Tables (Feature Store Level)

Workspace admins and any user with **CAN MANAGE** permission for the Feature Store itself can set permission levels that apply to **all** feature tables (current and future). To do so: ^[access-control-legacy-databricks-on-aws.md]

1. On the Feature Store page, click **Permissions**. (This button is only available to workspace admins and users with CAN MANAGE on the Feature Store.)
2. Edit the permissions and click **Save**.

Permissions set at the Feature Store level **apply to all future feature tables**. ^[access-control-legacy-databricks-on-aws.md]

## Inheritance and Override

Permissions configured from the Feature Store page are **inherited** by individual feature tables. When viewing a specific feature table’s permissions, these inherited permissions are labeled “Some permissions cannot be removed because they are inherited.” ^[access-control-legacy-databricks-on-aws.md]

- Permissions set at the Feature Store level **cannot be removed** from a single feature table page.
- On the individual feature table page, you **can override** the inherited settings to **add** more permissions (i.e., grant additional access), but you **cannot** set more restrictive permissions than those inherited.

Feature Store–level permissions can only be removed from the Feature Store permissions page. ^[access-control-legacy-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md) – Overview of Databricks Feature Store.
- [Unity Catalog](/concepts/unity-catalog.md) – The modern data governance model; workspaces enabled for Unity Catalog use a different privilege system.
- [Workspace Admin](/concepts/workspace-admin-unity-catalog.md) – Administrators who have CAN MANAGE on all feature tables by default.
- Access Control – General concept of permissions in Databricks.

## Sources

- access-control-legacy-databricks-on-aws.md

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
