---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eaee083c5b6a7edf97d8c7a5c5030ada0800a57cedcb89d14281d60f83c6e035
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - default-feature-table-permissions
    - DFTP
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: Default Feature Table Permissions
description: Upon creation, the creator and workspace admins automatically receive CAN MANAGE permission on a feature table, while all other users have NO PERMISSIONS.
tags:
  - databricks
  - feature-store
  - access-control
timestamp: "2026-06-19T13:50:44.260Z"
---

# Default Feature Table Permissions

**Default Feature Table Permissions** refers to the baseline access control settings automatically applied to feature tables in Databricks Feature Store workspaces that are not enabled for Unity Catalog. These defaults determine who can view, edit, or manage feature table metadata upon creation.

## Overview

When a new feature table is created in a workspace without Unity Catalog, the system assigns the following default permissions:

- **The creator** receives CAN MANAGE permission
- **Workspace admins** receive CAN MANAGE permission
- **All other users** receive NO PERMISSIONS

^[access-control-legacy-databricks-on-aws.md]

This means that by default, only the table creator and workspace administrators can view the feature table's metadata, edit its description, manage permissions, or delete the table. Other users cannot see the feature table in the UI or interact with it in any way until explicit permissions are granted. ^[access-control-legacy-databricks-on-aws.md]

## Permission Levels

Three permission levels are available for feature table metadata:

| Permission Level | Abilities |
|-----------------|-----------|
| CAN VIEW METADATA | View the feature table in the UI |
| CAN EDIT METADATA | Edit the feature table's description |
| CAN MANAGE | Manage other users' permissions and delete the table |

Any user can create a new feature table, but the default permissions restrict access to the creator and workspace admins. ^[access-control-legacy-databricks-on-aws.md]

## Configuring Permissions

### Per-Table Permissions

To change permissions on a specific feature table, navigate to the feature table page, click the arrow to the right of the table name, and select **Permissions**. This option is only available if you have CAN MANAGE permission for that feature table. ^[access-control-legacy-databricks-on-aws.md]

### Global Feature Store Permissions

Workspace administrators can set permission levels on all feature tables (including future tables) from the Feature Store UI. On the feature store page, click **Permissions**. This button is only available for workspace administrators and users with CAN MANAGE permission for the Feature Store. ^[access-control-legacy-databricks-on-aws.md]

Permissions set at the Feature Store level apply to all future feature tables. On individual feature table pages, you can add permissions beyond what is set at the Feature Store level, but you cannot set more restrictive permissions. Permissions inherited from the Feature Store level are marked as "Some permissions cannot be removed because they are inherited." ^[access-control-legacy-databricks-on-aws.md]

## Unity Catalog Workspaces

If your workspace is enabled for Unity Catalog, use [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md) instead of these legacy access controls. Unity Catalog provides a more comprehensive and centralized approach to data governance. ^[access-control-legacy-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md) — The central repository for feature tables
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — Modern access control for Unity Catalog-enabled workspaces
- [Feature Table Metadata](/concepts/feature-table.md) — The descriptive information controlled by these permissions
- Workspace Admin Permissions — Administrative access levels in Databricks

## Sources

- access-control-legacy-databricks-on-aws.md

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
