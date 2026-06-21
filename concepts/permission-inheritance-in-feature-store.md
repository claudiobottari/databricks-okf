---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 05d472b715f857ac6e735c3c59239024cd830daa2afe809fbac91f9eabb5e017
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - permission-inheritance-in-feature-store
    - PIIFS
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: Permission Inheritance in Feature Store
description: Permissions set at the Feature Store level are inherited by individual feature tables; they can be overridden to add permissions but not to remove inherited permissions.
tags:
  - access-control
  - feature-store
  - inheritance
timestamp: "2026-06-19T17:24:25.417Z"
---

# Permission Inheritance in Feature Store

**Permission Inheritance in Feature Store** describes how access control permissions for individual feature tables are inherited from permissions set at the Feature Store level in Databricks workspaces not enabled for Unity Catalog. This inheritance mechanism ensures that permissions applied broadly can propagate to existing and future feature tables, while allowing table-specific overrides that are additive only.

## Overview

In the legacy Databricks Feature Store (workspaces without [Unity Catalog](/concepts/unity-catalog.md)), permissions can be configured at two levels: the overall **Feature Store** level and the individual **feature table** level. Permissions set at the Feature Store level are inherited by all feature tables, both existing and future. ^[access-control-legacy-databricks-on-aws.md]

## Inheritance Behavior

When a workspace administrator or a user with CAN MANAGE permission for the Feature Store sets permissions on the Feature Store page, those permissions automatically propagate to all feature tables. The inherited permissions have specific characteristics: ^[access-control-legacy-databricks-on-aws.md]

- Permissions set at the Feature Store level are marked on individual feature table pages as "Some permissions cannot be removed because they are inherited." ^[access-control-legacy-databricks-on-aws.md]
- Inherited permissions can only be removed from the Feature Store page, not from individual feature table permission settings. ^[access-control-legacy-databricks-on-aws.md]
- Permissions set at the Feature Store page apply to **all** future feature tables created in that workspace. ^[access-control-legacy-databricks-on-aws.md]

## Override Rules

Permissions can be **overridden** at the individual feature table level, but only in an additive direction: ^[access-control-legacy-databricks-on-aws.md]

- On the feature table page, users can add permissions beyond what was inherited from the Feature Store level. ^[access-control-legacy-databricks-on-aws.md]
- Users **cannot** set more restrictive permissions on a feature table than what was set at the Feature Store level. ^[access-control-legacy-databricks-on-aws.md]
- When you navigate to a specific feature table page, permissions set from the Feature Store page are marked with a notice that they are inherited and cannot be removed from that page. ^[access-control-legacy-databricks-on-aws.md]

## Default Permissions

By default, when a feature table is created: ^[access-control-legacy-databricks-on-aws.md]

- The creator has CAN MANAGE permission.
- Workspace admins have CAN MANAGE permission.
- Other users have NO PERMISSIONS.

These defaults apply unless overridden by Feature Store-level permissions.

## Permission Levels

The Feature Store supports three permission levels for feature table metadata: ^[access-control-legacy-databricks-on-aws.md]

| Permission Level | Capabilities |
|---|---|
| CAN VIEW METADATA | View the feature table in the UI |
| CAN EDIT METADATA | View and edit the feature table's description |
| CAN MANAGE | Full control, including managing other users' permissions and deleting the table |

## Configuring Inheritance

### Setting Feature Store-Level Permissions

1. On the Feature Store page, click **Permissions** (available only to workspace administrators and users with CAN MANAGE permission for the Feature Store).
2. Edit the permissions and click **Save**.
3. These permissions propagate to all existing and future feature tables.

### Viewing Inherited Permissions on a Feature Table

1. On the feature table page, click the arrow to the right of the name and select **Permissions**.
2. Permissions inherited from the Feature Store level are displayed and marked as non-removable from this location.

## Related Concepts

- [Access Control (Legacy)](/concepts/feature-table-access-control-legacy.md) — The legacy permission system for workspaces not enabled for Unity Catalog.
- [Unity Catalog](/concepts/unity-catalog.md) — The recommended governance solution that replaces the legacy permission system.
- [Feature Table](/concepts/feature-table.md) — The primary resource to which permissions are applied.
- [Feature Store](/concepts/feature-store.md) — The overall repository where permissions can be set for inheritance.
- [CAN MANAGE Permission](/concepts/can-manage-permission.md) — The highest permission level that determines who can set Feature Store-level permissions.

## Sources

- access-control-legacy-databricks-on-aws.md

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
