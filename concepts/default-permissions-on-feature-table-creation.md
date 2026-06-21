---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7e7bdf0147b677c498c50d9977eda38d24b41801644feb9286756ca1f16542e2
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - default-permissions-on-feature-table-creation
    - DPOFTC
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: Default Permissions on Feature Table Creation
description: When a feature table is created in Databricks Feature Store, the creator and workspace admins get CAN MANAGE, while other users get NO PERMISSIONS by default.
tags:
  - databricks
  - access-control
  - feature-store
timestamp: "2026-06-19T08:49:21.517Z"
---

```markdown
---
title: Default Permissions on Feature Table Creation
summary: When a feature table is created in legacy Feature Store, the creator and workspace admins get CAN MANAGE permission, while all other users have NO PERMISSIONS by default.
sources:
  - access-control-legacy-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:36:50.709Z"
updatedAt: "2026-06-18T10:36:50.709Z"
tags:
  - databricks
  - feature-store
  - defaults
aliases:
  - default-permissions-on-feature-table-creation
  - DPOFTC
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Default Permissions on Feature Table Creation

When a feature table is created in Databricks Feature Store (in workspaces not enabled for Unity Catalog), specific default permissions are automatically assigned. These defaults govern who can view, edit, or manage the feature table immediately after creation. ^[access-control-legacy-databricks-on-aws.md]

## Default Permissions

By default, when a feature table is created:

* **The creator** receives **CAN MANAGE** permission.
* **All workspace admins** receive **CAN MANAGE** permission.
* **All other users** have **NO PERMISSIONS**.

Any user can create a feature table. ^[access-control-legacy-databricks-on-aws.md]

## Permission Levels

The Feature Store defines three permission levels for feature table metadata:

| Permission | Abilities |
|---|---|
| **CAN VIEW METADATA** | View the feature table in the UI and see its metadata. |
| **CAN EDIT METADATA** | Modify the feature table’s description and other metadata. |
| **CAN MANAGE** | Grant permissions to other users, edit metadata, and delete the feature table. |

Workspace admins and the creator have **CAN MANAGE** by default on their newly created tables. ^[access-control-legacy-databricks-on-aws.md]

## Managing Defaults After Creation

Default permissions can be changed at the individual feature table level by a user with **CAN MANAGE** permission on that table. Additionally, workspace admins or any user with **CAN MANAGE** on the Feature Store itself (set from the Feature Store page) can establish permissions that apply to all feature tables, including future ones. However, permissions set at the Feature Store level can only be removed from that page. On an individual feature table page, you can *add* more permissive settings on top of the Feature Store defaults, but you cannot apply more restrictive settings than the inherited ones. ^[access-control-legacy-databricks-on-aws.md]

## Unity Catalog Workspaces

This article describes default permissions for workspaces that are **not** enabled for Unity Catalog. If your workspace is enabled for Unity Catalog, use [[Unity Catalog Privilege Management|Unity Catalog Privileges]] instead of the legacy Feature Store access control model. ^[access-control-legacy-databricks-on-aws.md]

## Related Concepts

- [[Feature Store Access Control (Legacy)|Feature Store Access Control]] – Overview of permissions on feature tables
- [[Unity Catalog Privilege Management|Unity Catalog Privileges]] – The privilege model for Unity Catalog-enabled workspaces
- [[CAN MANAGE Permission]] – The highest permission level on feature table metadata

## Sources

- access-control-legacy-databricks-on-aws.md
```

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
