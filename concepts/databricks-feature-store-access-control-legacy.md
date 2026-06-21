---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2678235c1b7d8f6606a7cd60e8fd4d8665db663dc05d5cf5503e8e5d5575faaa
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-feature-store-access-control-legacy
    - DFSAC(
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: Databricks Feature Store Access Control (Legacy)
description: Granular permission system for feature table metadata in Databricks workspaces not enabled for Unity Catalog
tags:
  - databricks
  - access-control
  - feature-store
timestamp: "2026-06-18T14:16:32.971Z"
---

## Databricks Feature Store Access Control (Legacy)

**Databricks Feature Store Access Control (Legacy)** enables fine-grained permissions on feature table metadata for workspaces that are **not** enabled for [Unity Catalog](/concepts/unity-catalog.md). If your workspace is enabled for Unity Catalog, you must use [Unity Catalog privileges](/concepts/unity-catalog-privilege-management.md) instead. ^[access-control-legacy-databricks-on-aws.md]

### Permission Levels

Three permission levels are available for feature table metadata:

| Permission Level | Abilities |
|-----------------|-----------|
| CAN VIEW METADATA | View the feature table in the UI |
| CAN EDIT METADATA | Edit the feature table's description |
| CAN MANAGE | Manage other users' permissions on the feature table, and delete the table |

Any user can create a new feature table. ^[access-control-legacy-databricks-on-aws.md]

### Default Permissions

When a feature table is created, the following default permissions are applied:

- The creator of the feature table receives **CAN MANAGE**.
- [Workspace admins](/concepts/workspace-admins-unity-catalog.md) receive **CAN MANAGE**.
- All other users receive **NO PERMISSIONS**. ^[access-control-legacy-databricks-on-aws.md]

### Configuring Permissions for a Single Feature Table

1. On the feature table page, click the arrow to the right of the feature table name and select **Permissions**. This option is visible only if you have **CAN MANAGE** permission on that feature table. ^[access-control-legacy-databricks-on-aws.md]
2. Edit the permissions and click **Save**.

### Configuring Permissions for All Feature Tables

Workspace administrators (or any user with **CAN MANAGE** permission on the Feature Store itself) can set permission levels that apply to **all current and future** feature tables in the Feature Store.

1. On the Feature Store page, click **Permissions**. This button is visible only to workspace administrators and users with **CAN MANAGE** on the Feature Store. ^[access-control-legacy-databricks-on-aws.md]
2. Edit the permissions and click **Save**.

Permissions set at the Feature Store level are inherited by every feature table. These inherited permissions are marked on a specific feature table’s permissions page with the note “Some permissions cannot be removed because they are inherited”. Importantly:

- Permissions set on the Feature Store page can **only** be removed from that page.
- On a specific feature table page, you can **add** permissions (overriding the inherited settings to be more permissive), but you **cannot** set more restrictive permissions than those inherited from the Feature Store level. ^[access-control-legacy-databricks-on-aws.md]

### Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that supersedes legacy access control when enabled
- [Feature Store](/concepts/feature-store.md) — The centralized repository for feature tables
- [Feature Tables](/concepts/feature-tables.md) — The securable objects to which permissions are applied
- [Workspace Admin](/concepts/workspace-admin-unity-catalog.md) — A role that always receives CAN MANAGE on new feature tables

### Sources

- access-control-legacy-databricks-on-aws.md

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
