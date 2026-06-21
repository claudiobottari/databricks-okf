---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 82dff197d0c11b4d75149d6a22c21e14dc2d5003ed7684bc35e01731f0450784
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - configuring-feature-table-permissions-via-ui
    - CFTPVU
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: Configuring Feature Table Permissions via UI
description: Users with CAN MANAGE permission can configure permissions on individual feature tables through a drop-down menu on the feature table page in the Databricks UI.
tags:
  - databricks
  - feature-store
  - user-interface
timestamp: "2026-06-18T10:36:59.728Z"
---

# Configuring Feature Table Permissions via UI

This page describes how to configure permissions on feature tables using the Databricks Feature Store UI. These instructions apply to workspaces that are **not** enabled for Unity Catalog. If your workspace is enabled for Unity Catalog, use [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) instead. ^[access-control-legacy-databricks-on-aws.md]

## Overview

You can configure Feature Store access control to grant fine-grained permissions on feature table metadata. This controls a user's ability to view a feature table in the UI, edit its description, manage other users' permissions on the table, and delete the table. ^[access-control-legacy-databricks-on-aws.md]

Three permission levels are available for feature table metadata:

| Permission Level | Abilities |
|---|---|
| **CAN VIEW METADATA** | View the feature table and its metadata in the UI |
| **CAN EDIT METADATA** | Edit the feature table's description and metadata |
| **CAN MANAGE** | Manage other users' permissions on the table, edit metadata, and delete the table |

Any user can create a new feature table. ^[access-control-legacy-databricks-on-aws.md]

## Default Permissions

When a feature table is created, the following default permissions apply:

- The creator has **CAN MANAGE** permission
- Workspace admins have **CAN MANAGE** permission
- All other users have **NO PERMISSIONS**

^[access-control-legacy-databricks-on-aws.md]

## Configuring Permissions for a Single Feature Table

To configure permissions for an individual feature table:

1. Navigate to the feature table page in the Feature Store UI.
2. Click the arrow to the right of the feature table's name and select **Permissions** from the dropdown menu.
3. Edit the permissions for users or groups as needed.
4. Click **Save** to apply the changes.

> **Note:** If you do not have **CAN MANAGE** permission for the feature table, the **Permissions** option will not appear in the dropdown menu. ^[access-control-legacy-databricks-on-aws.md]

## Configuring Permissions for All Feature Tables

Workspace administrators and users with **CAN MANAGE** permission for the Feature Store can set permission levels on all feature tables for specific users or groups from the Feature Store page.

To configure permissions globally:

1. Navigate to the Feature Store page.
2. Click the **Permissions** button at the top of the page.
3. Edit the permissions for users or groups as needed.
4. Click **Save** to apply the changes.

> **Important:** Permissions set from the Feature Store page apply to all current and future feature tables. These permissions can only be removed from the Feature Store page, not from individual feature table pages. ^[access-control-legacy-databricks-on-aws.md]

## Inheritance and Override Behavior

When permissions are set at the Feature Store level, they are inherited by all individual feature tables. The following rules apply:

- On an individual feature table page, you can **add** permissions beyond those inherited from the Feature Store level.
- You **cannot** set more restrictive permissions on an individual feature table than those inherited from the Feature Store level.
- When viewing permissions on a specific feature table page, inherited permissions are marked with the note: "Some permissions cannot be removed because they are inherited."

^[access-control-legacy-databricks-on-aws.md]

## Best Practices

- **Use groups rather than individual users** when assigning permissions to simplify management.
- **Set broad permissions at the Feature Store level** and refine them on individual tables as needed.
- **Audit permissions regularly** to ensure users have appropriate access levels.
- **Grant CAN MANAGE sparingly** as it allows users to manage other users' permissions and delete feature tables.

## Related Concepts

- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — The permission model for workspaces enabled for Unity Catalog
- [Feature Store](/concepts/feature-store.md) — The Databricks feature management platform
- [Feature Tables](/concepts/feature-table.md) — The core data objects managed in the Feature Store
- Access Control in Unity Catalog — Modern access control for Unity Catalog-enabled workspaces

## Sources

- access-control-legacy-databricks-on-aws.md

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
