---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6c96f44f8d358d3823844b33720de168d1455bba39391ba88eeb5ba221dee1bf
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-store-wide-permission-inheritance
    - FSPI
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: Feature Store-Wide Permission Inheritance
description: Permissions set at the Feature Store level apply to all feature tables (current and future) and can be overridden per-table to add but not restrict permissions
tags:
  - access-control
  - permissions
  - inheritance
  - feature-store
timestamp: "2026-06-19T21:55:38.174Z"
---

# Feature Store-Wide Permission Inheritance

**Feature Store-Wide Permission Inheritance** is a capability in Databricks Feature Store (non-Unity Catalog workspaces) that allows workspace administrators and users with `CAN MANAGE` permission on the Feature Store to set baseline permission levels across all feature tables from a single interface. These inherited permissions apply to both existing and future feature tables, providing a centralized access control mechanism. ^[access-control-legacy-databricks-on-aws.md]

## Overview

In workspaces not enabled for Unity Catalog, Feature Store access control uses three permission levels: `CAN VIEW METADATA`, `CAN EDIT METADATA`, and `CAN MANAGE`. When permissions are configured at the Feature Store level (the "store-wide" level), they are inherited by every individual feature table. Permissions set store-wide can only be removed from the store-wide page; they cannot be removed at the individual feature table level. ^[access-control-legacy-databricks-on-aws.md]

## How Inheritance Works

### Store-Wide Permissions as Baseline

Store-wide permissions function as a baseline that applies uniformly across all feature tables. When a user or group is granted a permission level at the store-wide level, that permission is inherited by every feature table in the Feature Store. This inheritance applies automatically to newly created feature tables as well. ^[access-control-legacy-databricks-on-aws.md]

### Override Behavior at Feature Table Level

On a specific feature table page, permissions set from the store-wide level are marked with the note "Some permissions cannot be removed because they are inherited." At the individual feature table level, you can add additional permissions beyond what is inherited, but you **cannot set more restrictive permissions** than what is granted store-wide. This means: ^[access-control-legacy-databricks-on-aws.md]

- Inheritance is **additive only** — you can grant broader access on a specific table, but you cannot revoke store-wide permissions on that table.
- The most permissive setting, whether inherited or table-specific, determines what a user can do.

### Scope

Permissions set from the Feature Store page apply to **all current and future feature tables**. This makes store-wide permission configuration a convenient way to establish a baseline access policy without needing to configure each table individually. ^[access-control-legacy-databricks-on-aws.md]

## Configuring Store-Wide Permissions

### Prerequisites

To configure Feature Store-wide permissions, you must be either:
- A workspace administrator, or
- A user with `CAN MANAGE` permission for the Feature Store itself ^[access-control-legacy-databricks-on-aws.md]

### Steps

1. On the Feature Store page, click **Permissions**.
2. Edit the permissions for users or groups.
3. Click **Save**.

The **Permissions** button on the Feature Store page is only visible to workspace administrators and users with `CAN MANAGE` permission for the Feature Store. ^[access-control-legacy-databricks-on-aws.md]

## Default Permissions

When a feature table is created, the following default permissions apply: ^[access-control-legacy-databricks-on-aws.md]

| Principal | Default Permission |
|---|---|
| Creator of the table | `CAN MANAGE` |
| Workspace admins | `CAN MANAGE` |
| Other users | `NO PERMISSIONS` |

Store-wide permissions override the `NO PERMISSIONS` default for other users if configured.

## Permission Levels

The three permission levels in the Feature Store access control model are: ^[access-control-legacy-databricks-on-aws.md]

| Permission Level | Capabilities |
|---|---|
| `CAN VIEW METADATA` | View the feature table in the UI |
| `CAN EDIT METADATA` | Edit the feature table's description and metadata |
| `CAN MANAGE` | Manage permissions for other users, edit metadata, and delete the table |

Any user can create a new feature table regardless of their permission level on other tables.

## Use Case Example

Consider a scenario where an organization wants all data scientists to have at least `CAN VIEW METADATA` on every feature table, while a specific engineering group should have `CAN MANAGE` across all tables. By configuring these permissions at the store-wide level, the administrator ensures:

- New feature tables automatically grant `CAN VIEW METADATA` to all data scientists.
- The engineering group automatically receives `CAN MANAGE` on all tables, including newly created ones.
- Individual feature table owners can grant additional permissions on their tables, but cannot revoke the store-wide baseline.

## Limitations

- Store-wide permissions cannot be removed from individual feature tables — they can only be removed from the store-wide settings page.
- At the feature table level, you cannot set more restrictive permissions than what is inherited from the store-wide level. Inheritance is additive only.
- This feature applies only to workspaces that are **not** enabled for Unity Catalog. For Unity Catalog-enabled workspaces, use [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) instead. ^[access-control-legacy-databricks-on-aws.md]

## Related Concepts

- [Feature Store Access Control](/concepts/feature-store-access-control-legacy.md) — The broader permission model for feature tables
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — The access control system for Unity Catalog-enabled workspaces
- [Feature Store](/concepts/feature-store.md) — The centralized repository for feature engineering and serving

## Sources

- access-control-legacy-databricks-on-aws.md

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
