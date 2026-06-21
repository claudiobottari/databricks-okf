---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ab1526832de01094ce17ed930f623a1481340f56c588db21461ba0a6e7bc700d
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - can-manage-permission
    - CMP
    - CAN MANAGE
    - Compute Permissions
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: CAN MANAGE Permission
description: The highest permission level for feature tables, allowing management of other users' permissions and deletion of the table
tags:
  - access-control
  - permissions
  - feature-store
timestamp: "2026-06-19T21:55:25.513Z"
---

# CAN MANAGE Permission

**CAN MANAGE Permission** is the highest permission level that can be assigned to a [Feature Table](/concepts/feature-table.md) in Databricks Feature Store workspaces that are not enabled for [Unity Catalog](/concepts/unity-catalog.md). It grants full administrative control over a feature table's metadata, including the ability to view metadata, edit descriptions, manage other users' permissions, and delete the table. ^[access-control-legacy-databricks-on-aws.md]

## Overview

In the Feature Store access control model, three permission levels are available for feature table metadata: CAN VIEW METADATA, CAN EDIT METADATA, and CAN MANAGE. CAN MANAGE is the most permissive level, encompassing all capabilities of the lower levels plus additional administrative functions. ^[access-control-legacy-databricks-on-aws.md]

## Default Assignment

When a new feature table is created, the following default permissions are applied:

- The **creator** of the feature table automatically receives CAN MANAGE permission.
- **Workspace administrators** automatically receive CAN MANAGE permission.
- All other users receive **NO PERMISSIONS** by default.

^[access-control-legacy-databricks-on-aws.md]

## Capabilities

Users with CAN MANAGE permission can perform the following actions on a feature table:

- View the feature table in the UI
- Edit the feature table's description
- Manage permissions for other users on the feature table
- Delete the feature table

These capabilities include all actions available at the CAN VIEW METADATA and CAN EDIT METADATA levels. ^[access-control-legacy-databricks-on-aws.md]

## Managing Permissions

### On a Specific Feature Table

To configure permissions for an individual feature table:

1. Navigate to the feature table page.
2. Click the arrow to the right of the feature table name and select **Permissions**.
3. Edit the permissions and click **Save**.

Only users with CAN MANAGE permission for the feature table will see the **Permissions** option in the dropdown menu. ^[access-control-legacy-databricks-on-aws.md]

### On All Feature Tables

Workspace administrators and users with CAN MANAGE permission for the entire Feature Store can set permission levels on all feature tables for specific users or groups:

1. On the Feature Store page, click **Permissions**.
2. Edit the permissions and click **Save**.

Permissions set at the Feature Store level apply to all current and future feature tables. These permissions can only be removed from the Feature Store page. On individual feature table pages, users can add additional permissions but cannot set more restrictive permissions than those inherited from the Feature Store level. Inherited permissions are marked with the message "Some permissions cannot be removed because they are inherited." ^[access-control-legacy-databricks-on-aws.md]

## Related Concepts

- [Feature Table](/concepts/feature-table.md) — The data object that CAN MANAGE permission controls access to.
- [CAN VIEW METADATA Permission](/concepts/can-view-metadata-permission.md) — The lowest permission level for feature tables.
- [CAN EDIT METADATA Permission](/concepts/can-edit-metadata-permission.md) — The intermediate permission level for feature tables.
- [Unity Catalog](/concepts/unity-catalog.md) — The recommended governance solution for workspaces enabled for Unity Catalog.
- [Feature Store](/concepts/feature-store.md) — The workspace-level feature store where permissions can be set globally.

## Sources

- access-control-legacy-databricks-on-aws.md

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
