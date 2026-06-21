---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1789de8bc9a0e1dc30427fe74fa7bb4f474d38585df05314dce59eb1d253ef04
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - per-table-access-control-configuration
    - PACC
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: Per-Table Access Control Configuration
description: Users with CAN MANAGE permission can configure permissions on an individual feature table via the table's drop-down menu in the Databricks Feature Store UI.
tags:
  - databricks
  - feature-store
  - access-control
timestamp: "2026-06-19T13:50:54.659Z"
---

# Per-Table Access Control Configuration

**Per-Table Access Control Configuration** refers to the ability to grant fine-grained permissions on individual feature table metadata within the [Feature Store](/concepts/feature-store.md) (legacy), for workspaces that are not enabled for [Unity Catalog](/concepts/unity-catalog.md). This allows administrators to control who can view, edit, or manage each feature table independently. ^[access-control-legacy-databricks-on-aws.md]

## Permission Levels

Feature table metadata supports three hierarchical permission levels: ^[access-control-legacy-databricks-on-aws.md]

| Permission Level | Abilities |
|------------------|-----------|
| `CAN VIEW METADATA` | View the feature table in the UI and see its metadata. |
| `CAN EDIT METADATA` | Edit the feature table’s description and other metadata. |
| `CAN MANAGE` | Change permissions for other users on the table, and delete the table. |

Any user can create a new feature table; the creator automatically receives `CAN MANAGE` permission on that table. ^[access-control-legacy-databricks-on-aws.md]

## Default Permissions

When a feature table is first created, the following default permissions apply: ^[access-control-legacy-databricks-on-aws.md]

- The creator has `CAN MANAGE` permission.
- Workspace admins have `CAN MANAGE` permission.
- All other users have `NO PERMISSIONS`.

## Configuring Permissions for a Single Feature Table

To configure permissions on a specific feature table: ^[access-control-legacy-databricks-on-aws.md]

1. Navigate to the feature table’s page in the Feature Store UI.
2. Click the arrow to the right of the feature table name and select **Permissions**.
3. If you do not have `CAN MANAGE` permission, this option is not visible.
4. Edit the permissions as needed and click **Save**.

## Configuring Permissions for All Feature Tables

Workspace administrators – or any user with `CAN MANAGE` permission at the Feature Store level – can set baseline permissions that apply to all current and future feature tables. ^[access-control-legacy-databricks-on-aws.md]

1. On the **Feature Store** page, click **Permissions**.
2. Edit the permissions and click **Save**.

Permissions set at the Feature Store level can only be removed from that same page. Individual feature table pages can add additional permissions (broadening access) but cannot remove the inherited permissions or make them more restrictive. Inherited permissions are marked with the note: “Some permissions cannot be removed because they are inherited.” ^[access-control-legacy-databricks-on-aws.md]

## Important Notes

- This legacy access control mechanism applies only to workspaces **not** enabled for Unity Catalog. If your workspace uses Unity Catalog, use [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md) instead. ^[access-control-legacy-databricks-on-aws.md]
- Permissions set at the Feature Store level apply to all future feature tables created after the settings are saved. ^[access-control-legacy-databricks-on-aws.md]
- To change permissions for a feature table, you must have `CAN MANAGE` on that table. To change permissions for all tables at the Feature Store level, you must have `CAN MANAGE` on the Feature Store itself (or be a workspace admin). ^[access-control-legacy-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md) — The repository for feature tables.
- [Unity Catalog](/concepts/unity-catalog.md) — The modern data governance solution that supersedes this legacy access control.
- [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md) — How to manage access control when Unity Catalog is enabled.
- Workspace admin — Role that inherits `CAN MANAGE` on all feature tables.
- [Feature table metadata](/concepts/feature-table.md) — The metadata governed by these permission levels.

## Sources

- access-control-legacy-databricks-on-aws.md

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
