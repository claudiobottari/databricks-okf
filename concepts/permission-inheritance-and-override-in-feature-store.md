---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ef7d74bd41a0da5bfa1dd23ebf8e030ec02a150978cc63305f9db85f04638779
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - permission-inheritance-and-override-in-feature-store
    - Override in Feature Store and Permission Inheritance
    - PIAOIFS
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: Permission Inheritance and Override in Feature Store
description: Permissions set at the Feature Store level apply to all tables and can only be overridden to add more permissive access, not remove; inherited permissions are marked as such
tags:
  - inheritance
  - permissions
  - feature-store
timestamp: "2026-06-18T14:16:56.119Z"
---

# Permission Inheritance and Override in Feature Store

**Permission Inheritance and Override in Feature Store** describes how access control permissions flow from the workspace-level Feature Store to individual feature tables, and the rules for overriding those inherited permissions at the table level.

## Overview

In Databricks Feature Store workspaces that are not enabled for [Unity Catalog](/concepts/unity-catalog.md), permissions can be set at two levels: on the Feature Store itself (applying to all current and future feature tables) and on individual feature tables. Permissions set at the Feature Store level are inherited by all feature tables, but can be overridden on a per-table basis with certain constraints.^[access-control-legacy-databricks-on-aws.md]

## Permission Inheritance

When a workspace administrator or a user with `CAN MANAGE` permission for the Feature Store sets permissions on the Feature Store page, those permissions apply to all existing feature tables. They also automatically apply to any new feature tables created in the future.^[access-control-legacy-databricks-on-aws.md]

Inherited permissions are visible on individual feature table pages, where they are marked with the notice: "Some permissions cannot be removed because they are inherited."^[access-control-legacy-databricks-on-aws.md]

## Override Rules

Permissions set on the Feature Store page can only be removed from that page. On the individual feature table page, you can override settings from the Feature Store page to **add** permissions, but you **cannot set more restrictive permissions** than those inherited from the Feature Store level.^[access-control-legacy-databricks-on-aws.md]

This means:

- **Adding permissions at the table level is allowed.** You can grant a user or group additional access on a specific feature table beyond what they receive from the Feature Store-wide setting.
- **Restricting permissions at the table level is not allowed.** You cannot reduce a user's or group's access below what they inherit from the Feature Store. Attempting to do so would conflict with the inheritance rule.

## Permission Levels

The Feature Store supports three permission levels for feature table metadata:^[access-control-legacy-databricks-on-aws.md]

| Permission Level | Capabilities |
|-----------------|--------------|
| `CAN VIEW METADATA` | View the feature table in the UI |
| `CAN EDIT METADATA` | View and edit the feature table's description and metadata |
| `CAN MANAGE` | Full control, including managing other users' permissions and deleting the table |

## Default Permissions

When a feature table is created, the following default permissions apply:^[access-control-legacy-databricks-on-aws.md]

- The creator receives `CAN MANAGE` permission
- Workspace administrators receive `CAN MANAGE` permission
- All other users receive `NO PERMISSIONS`

## Managing Permissions

### Feature Store Level

Workspace administrators and users with `CAN MANAGE` permission for the Feature Store can configure permissions for all feature tables by navigating to the Feature Store page and clicking **Permissions**. This button is only available to authorized users.^[access-control-legacy-databricks-on-aws.md]

### Individual Feature Table Level

On a feature table's page, click the arrow next to the table name and select **Permissions**. This option is available only to users with `CAN MANAGE` permission on that specific feature table.^[access-control-legacy-databricks-on-aws.md]

## Related Concepts

- [Feature Store Access Control](/concepts/feature-store-access-control-legacy.md) — Overview of permission management for feature tables
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — Modern access control approach for Unity Catalog-enabled workspaces
- [CAN MANAGE Permission](/concepts/can-manage-permission.md) — The administrative permission level for feature tables

## Sources

- access-control-legacy-databricks-on-aws.md

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
