---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 83473d16c669e76d1e9bf643689d5f342fdf127d3d6a56be06264935a804e347
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-store-wide-permission-configuration
    - FSPC
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: Feature Store-Wide Permission Configuration
description: Workspace administrators and users with CAN MANAGE on the Feature Store can set default permission levels on all current and future feature tables from the Feature Store page.
tags:
  - databricks
  - feature-store
  - access-control
timestamp: "2026-06-19T13:51:06.896Z"
---

# Feature Store-Wide Permission Configuration

**Feature Store-Wide Permission Configuration** allows workspace administrators to set permission levels on all [Feature Tables](/concepts/feature-tables.md) in a Feature Store for specific users or groups. This configuration is applied at the Feature Store level rather than on individual feature tables, providing centralized access control for metadata operations.

## Overview

Feature Store-Wide Permission Configuration applies to workspaces that are **not** enabled for [Unity Catalog](/concepts/unity-catalog.md). If your workspace is enabled for Unity Catalog, use [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md) instead. ^[access-control-legacy-databricks-on-aws.md]

Permission levels control a user's ability to view a feature table in the UI, edit its description, manage other users' permissions, and delete the table. ^[access-control-legacy-databricks-on-aws.md]

## Permission Levels

Three permission levels can be assigned to feature table metadata:

- **CAN VIEW METADATA**: Can view the feature table in the UI
- **CAN EDIT METADATA**: Can edit the feature table's description
- **CAN MANAGE**: Can manage other users' permissions on the table and delete the table

Any user can create a new feature table. ^[access-control-legacy-databricks-on-aws.md]

## Default Permissions

By default, when a feature table is created:

- The creator has **CAN MANAGE** permission
- Workspace admins have **CAN MANAGE** permission
- Other users have **NO PERMISSIONS**

^[access-control-legacy-databricks-on-aws.md]

## Configuring Feature Store-Wide Permissions

Workspace administrators can configure permissions for **all** feature tables in the Feature Store using the UI. Permissions set from the Feature Store page also apply to all future feature tables. ^[access-control-legacy-databricks-on-aws.md]

### Prerequisites

- You must be a workspace administrator or have **CAN MANAGE** permission for the Feature Store
- The **Permissions** button on the feature store page is only available for these users

### Steps

1. On the **feature store** page, click **Permissions**.
   ![Drop-down menu where you select permissions](https://docs.databricks.com/aws/en/assets/images/feature-store-wide-permissions-65c0edf83a192ef0b3b1adf7395003e8.png)
2. Edit the permissions and click **Save**.

### Inheritance Rules

- Permissions set on the Feature Store page can **only be removed** from that page
- On the feature table page, you can override settings from the Feature Store page to **add** permissions, but you **cannot** set more restrictive permissions
- When navigating to a specific feature table page, permissions set from the Feature Store page are marked **"Some permissions cannot be removed because they are inherited"**

## Related Concepts

- [Feature Store Access Control](/concepts/feature-store-access-control-legacy.md) — Fine-grained permissions on individual feature tables
- [Unity Catalog](/concepts/unity-catalog.md) — Modern access control for Unity Catalog-enabled workspaces
- [Feature Table](/concepts/feature-table.md) — The metadata object managed by the Feature Store
- [Workspace Administration](/concepts/workspace-admin-unity-catalog.md) — Role-based access control for Datab workspaces

## Sources

- access-control-legacy-databricks-on-aws.md

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
