---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 44918846f5f26e1fb5bb21ab08e4d09e228d648e5477217da054eb633ebc3a13
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - default-permissions-for-feature-tables
    - DPFFT
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: Default Permissions for Feature Tables
description: By default, the creator and workspace admins get CAN MANAGE permission while all other users have no permissions on a new feature table
tags:
  - access-control
  - permissions
  - feature-store
timestamp: "2026-06-19T21:55:28.980Z"
---

# Default Permissions for Feature Tables

**Default Permissions for Feature Tables** define the initial access control levels automatically assigned when a new feature table is created in Databricks Feature Store (workspaces not enabled for Unity Catalog). These defaults determine who can view, edit, manage, or delete feature table metadata.

## Default Permission Levels

When a feature table is created, the following default permissions are applied:

- **The creator** receives CAN MANAGE permission
- **Workspace admins** receive CAN MANAGE permission
- **All other users** receive NO PERMISSIONS

^[access-control-legacy-databricks-on-aws.md]

## Permission Levels

Feature Store supports three permission levels for feature table metadata:

| Permission Level | Abilities |
|-----------------|-----------|
| **CAN VIEW METADATA** | View the feature table in the UI |
| **CAN EDIT METADATA** | Edit the feature table description |
| **CAN MANAGE** | Manage other users' permissions on the table and delete the table |

Any user can create a new feature table, regardless of their existing permissions. ^[access-control-legacy-databricks-on-aws.md]

## Configuring Permissions

### Per-Table Permissions

To configure permissions for a specific feature table:

1. On the feature table page, click the arrow to the right of the table name and select **Permissions**.
2. Edit the permissions and click **Save**.

The **Permissions** option is only visible to users with CAN MANAGE permission for that feature table. ^[access-control-legacy-databricks-on-aws.md]

### Global Feature Store Permissions

Workspace administrators can set permission levels on all feature tables (current and future) from the Feature Store UI:

1. On the feature store page, click **Permissions**.
2. Edit the permissions and click **Save**.

This button is only available for workspace administrators and users with CAN MANAGE permission for the Feature Store. ^[access-control-legacy-databricks-on-aws.md]

Permissions set from the Feature Store page can only be removed from that page. On individual feature table pages, you can add permissions beyond the global settings, but you cannot set more restrictive permissions than those inherited from the Feature Store level. When viewing a specific feature table, inherited permissions are marked as "Some permissions cannot be removed because they are inherited." ^[access-control-legacy-databricks-on-aws.md]

## Unity Catalog Workspaces

If your workspace is enabled for Unity Catalog, use [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) instead of these legacy access controls. ^[access-control-legacy-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md) — The centralized repository for feature tables
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — Access control for Unity Catalog-enabled workspaces
- [Feature Table Metadata](/concepts/feature-table.md) — The descriptive information about feature tables
- [Workspace Administration](/concepts/workspace-admin-unity-catalog.md) — Managing user permissions and access

## Sources

- access-control-legacy-databricks-on-aws.md

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
