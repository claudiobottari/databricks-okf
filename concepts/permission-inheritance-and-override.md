---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: df20f0565393ba99ee02135850e80169d590cb60ba8c802e9cf3e9aa1fb0b388
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - permission-inheritance-and-override
    - Override and Permission Inheritance
    - PIAO
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: Permission Inheritance and Override
description: Feature store-wide permissions are inherited by individual feature tables and can only be removed at the store level; per-table settings can add more permissive rules but cannot override inherited restrictions.
tags:
  - databricks
  - feature-store
  - access-control
timestamp: "2026-06-19T13:50:55.203Z"
---

# Permission Inheritance and Override

**Permission Inheritance and Override** is a security model in Databricks Feature Store that allows permissions to be set at both the Feature Store level and the individual feature table level. Permissions set at the Feature Store level apply to all feature tables (including future ones), while individual feature table permissions can add additional access beyond the inherited baseline.

## Overview

Workspace administrators and users with CAN MANAGE permission for the Feature Store can set permission levels on all feature tables for specific users or groups from the Feature Store page. These inherited permissions then apply to all existing and future feature tables. ^[access-control-legacy-databricks-on-aws.md]

## Inheritance Behavior

When permissions are set from the Feature Store page:

- The permissions apply to all current and future feature tables.
- On a specific feature table page, inherited permissions are marked with the note: "Some permissions cannot be removed because they are inherited."
- Inherited permissions can only be removed from the Feature Store page, not from individual feature table pages. ^[access-control-legacy-databricks-on-aws.md]

## Override Rules

Override behavior follows these rules:

- **Adding permissions:** On a feature table page, you can override settings from the Feature Store page to add permissions for additional users or groups.
- **Restricting permissions:** You cannot set more restrictive permissions on a feature table than what is inherited from the Feature Store level. Overrides can only expand access, not contract it. ^[access-control-legacy-databricks-on-aws.md]

## Permission Levels

The Feature Store supports three permission levels:

| Permission Level | Description |
|-----------------|-------------|
| CAN VIEW METADATA | View a feature table in the UI |
| CAN EDIT METADATA | Edit a feature table's description |
| CAN MANAGE | Manage other users' permissions on the table, and delete the table |

Any user can create a new feature table. ^[access-control-legacy-databricks-on-aws.md]

## Default Permissions

By default, when a feature table is created:

- The creator has CAN MANAGE permission
- Workspace admins have CAN MANAGE permission
- All other users have NO PERMISSIONS

^[access-control-legacy-databricks-on-aws.md]

## Configuring Permissions

### At the Feature Store Level

Workspace administrators and users with CAN MANAGE permission for the Feature Store can configure inherited permissions:

1. On the feature store page, click **Permissions**.
2. Edit the permissions and click **Save**.

Permissions set here apply to all feature tables. ^[access-control-legacy-databricks-on-aws.md]

### At the Feature Table Level

Users with CAN MANAGE permission on a specific feature table can override inherited permissions:

1. On the feature table page, click the arrow to the right of the name and select **Permissions**.
2. Edit the permissions and click **Save**.

Only additions to the inherited permissions are possible at this level. ^[access-control-legacy-databricks-on-aws.md]

## Important Notes

- If you do not have CAN MANAGE permission for a feature table, you will not see the **Permissions** option on that table's page.
- Permissions set on the Feature Store page can only be removed from that page. ^[access-control-legacy-databricks-on-aws.md]

## Related Concepts

- [Workspace Feature Store](/concepts/workspace-feature-store-ui.md) — The Feature Store environment where permissions are managed
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — Alternative permission model for workspaces enabled for Unity Catalog
- [Feature Table Management](/concepts/feature-tables.md) — Creating, editing, and deleting feature tables
- [Access Control Models](/concepts/unity-catalog-access-control-models.md) — Comparison of legacy and Unity Catalog access control approaches

## Sources

- access-control-legacy-databricks-on-aws.md

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
