---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9f076ba6d2f6741ec3e9c87c37fccf44a741407fc52f7382737e62c585ccc7ad
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-store-access-control-permission-levels
    - FSACPL
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: Feature Store Access Control Permission Levels
description: "Three permission levels for feature table metadata: CAN VIEW METADATA, CAN EDIT METADATA, and CAN MANAGE."
tags:
  - access-control
  - feature-store
  - permissions
timestamp: "2026-06-19T17:24:54.710Z"
---

---
title: Feature Store Access Control Permission Levels
summary: Three permission levels (CAN VIEW METADATA, CAN EDIT METADATA, CAN MANAGE) that control access to feature table metadata in Databricks Feature Store workspaces not enabled for Unity Catalog.
sources:
  - access-control-legacy-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:44:59.232Z"
updatedAt: "2026-06-19T10:44:59.232Z"
tags:
  - databricks
  - feature-store
  - access-control
aliases:
  - feature-store-access-control-permission-levels
  - FSACPL
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Feature Store Access Control Permission Levels

**Feature Store Access Control** allows administrators to grant fine-grained permissions on feature table metadata in workspaces that are **not** enabled for [Unity Catalog](/concepts/unity-catalog.md). For Unity Catalog‑enabled workspaces, use [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) instead. ^[access-control-legacy-databricks-on-aws.md]

## Permission Levels

There are three permission levels for feature table metadata:

| Permission        | Abilities |
|-------------------|-----------|
| **CAN VIEW METADATA** | View the feature table in the UI. |
| **CAN EDIT METADATA** | Edit the feature table description (implies view). |
| **CAN MANAGE**        | Grant or revoke permissions for other users, and delete the feature table (implies edit and view). |

^[access-control-legacy-databricks-on-aws.md]

Any user can create a new feature table. When a feature table is created, the default permissions are: ^[access-control-legacy-databricks-on-aws.md]

* The creator has **CAN MANAGE**.
* Workspace admins have **CAN MANAGE**.
* All other users have **NO PERMISSIONS**.

## Configuring Permissions on a Single Feature Table

On the feature table page, click the arrow to the right of the table name and select **Permissions**. This option is visible only if you have CAN MANAGE permission on that table. Edit the permissions and click **Save**. ^[access-control-legacy-databricks-on-aws.md]

## Configuring Permissions for All Feature Tables (Global Setting)

Workspace administrators (or any user with CAN MANAGE permission on the Feature Store itself) can set a baseline permission level that applies to **all existing and future** feature tables. ^[access-control-legacy-databricks-on-aws.md]

1. On the Feature Store page, click **Permissions**.
2. Edit the permissions and click **Save**.

Permissions set at the Feature Store level:
* Can only be removed from the Feature Store page.
* Can be **overridden** on a per‑table page to **add** permissions, but cannot be made more restrictive than the global baseline.
* When viewing a specific feature table, inherited permissions are marked with the message “Some permissions cannot be removed because they are inherited”. ^[access-control-legacy-databricks-on-aws.md]

## Related Concepts

* [Feature Store](/concepts/feature-store.md) — Overview of Databricks Feature Store.
* [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — Access control for workspaces using Unity Catalog.
* [Workspace Administration](/concepts/workspace-admin-unity-catalog.md) — The role that always receives CAN MANAGE by default.
* [Feature Table Metadata](/concepts/feature-table.md) — The artifacts to which these permissions apply.

## Sources

- access-control-legacy-databricks-on-aws.md

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
