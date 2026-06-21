---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6c1c015b2cfaf430b9445d0ee89fb2099730457d50512dea96b1c2ef29544bf4
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - configuring-permissions-across-all-feature-tables
    - CPAAFT
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: Configuring Permissions Across All Feature Tables
description: Workspace admins and Feature Store CAN MANAGE holders can set base permissions for all current and future feature tables from the Feature Store page
tags:
  - configuration
  - permissions
  - feature-store
  - administration
timestamp: "2026-06-18T14:16:39.385Z"
---

# Configuring Permissions Across All Feature Tables

**Configuring Permissions Across All Feature Tables** allows workspace administrators and users with `CAN MANAGE` permission on the Feature Store to set a common permission level for all existing and future [feature tables](/concepts/feature-table.md) at once, rather than editing each table individually.

## Permission Levels

The Feature Store supports three permission levels for feature table metadata: `CAN VIEW METADATA`, `CAN EDIT METETADATA`, and `CAN MANAGE`. By default, when a feature table is created, the creator and workspace administrators receive `CAN MANAGE`, and all other users have no permissions. ^[access-control-legacy-databricks-on-aws.md]

## Bulk Permission Configuration

Workspace administrators and any user who holds `CAN MANAGE` on the Feature Store itself can change the default permissions for all feature tables — both currently existing and those created in the future — from the Feature Store page. A user with `CAN MANAGE` on the Feature Store can change these global permissions for all other users. ^[access-control-legacy-databricks-on-aws.md]

### Steps

1. On the Feature Store page, click **Permissions**.  
   This button appears only for workspace administrators and users who have `CAN MANAGE` permission on the Feature Store. ^[access-control-legacy-databricks-on-aws.md]
2. Edit the permission assignments for users or groups, then click **Save**. ^[access-control-legacy-databricks-on-aws.md]

## Important Behavior

- Permissions set from the Feature Store page can **only be removed** from that same page. ^[access-control-legacy-databricks-on-aws.md]
- On individual feature table pages, you may **add** permissions beyond those inherited from the Feature Store level, but you **cannot** set more restrictive permissions than what the Feature Store page defines. When you view a specific feature table’s permissions, inherited settings are marked with the note “Some permissions cannot be removed because they are inherited”. ^[access-control-legacy-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md)
- [Feature table permissions](/concepts/feature-table-permission-levels.md)
- [CAN MANAGE Permission](/concepts/can-manage-permission.md)
- [Workspace administrator](/concepts/workspace-admin-unity-catalog.md)

## Sources

- access-control-legacy-databricks-on-aws.md

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
