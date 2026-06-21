---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ee01e30b08789fa6979f276f0a816bc64f3199e71bf26e4f39ad2bec91c7e3bf
  pageDirectory: concepts
  sources:
    - access-control-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-table-permission-levels
    - FTPL
    - Feature Table Permissions
    - Feature table permissions
    - feature-store-permission-levels-legacy
    - FSPL(
  citations:
    - file: access-control-legacy-databricks-on-aws.md
title: Feature Table Permission Levels
description: "Databricks Feature Store defines three fine-grained permission levels for feature table metadata: CAN VIEW METADATA, CAN EDIT METADATA, and CAN MANAGE."
tags:
  - databricks
  - feature-store
  - access-control
timestamp: "2026-06-19T13:51:24.116Z"
---

```yaml
---
title: Feature Table Permission Levels
summary: Three tiers of access — CAN VIEW METADATA, CAN EDIT METADATA, and CAN MANAGE — for controlling user actions on feature tables
sources:
  - access-control-legacy-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:16:39.512Z"
updatedAt: "2026-06-18T14:16:39.512Z"
tags:
  - permissions
  - authorization
  - feature-store
aliases:
  - feature-table-permission-levels
  - FTPL
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Feature Table Permission Levels

**Feature Table Permission Levels** control access to feature table metadata in workspaces that are not enabled for [[Unity Catalog]]. These permissions govern a user's ability to view a feature table in the UI, edit its description, manage other users' permissions on the table, and delete the table.^[access-control-legacy-databricks-on-aws.md]

## Permission Levels

The Feature Store provides three permission levels for feature table metadata. Any user can create a new feature table. The table lists the abilities for each permission.^[access-control-legacy-databricks-on-aws.md]

| Permission Level | Abilities |
|-----------------|-----------|
| **CAN VIEW METADATA** | View the feature table in the UI. |
| **CAN EDIT METADATA** | View metadata and edit the feature table’s description. |
| **CAN MANAGE** | View metadata, edit descriptions, manage other users’ permissions on the table, and delete the table. |

## Default Permissions

When a feature table is created, the following default permissions apply:^[access-control-legacy-databricks-on-aws.md]

* The creator receives **CAN MANAGE** permission.
* Workspace administrators receive **CAN MANAGE** permission.
* All other users have **NO PERMISSIONS**.

## Configure Permissions for a Feature Table

To configure permissions for a specific feature table:^[access-control-legacy-databricks-on-aws.md]

1. On the feature table page, click the arrow to the right of the feature table name and select **Permissions**.
2. Edit the permissions and click **Save**.

Only users with **CAN MANAGE** permission for the feature table will see the **Permissions** option.^[access-control-legacy-databricks-on-aws.md]

## Configure Permissions for All Feature Tables

Workspace administrators can use the Feature Store UI to set permission levels on all feature tables for specific users or groups. Users with **CAN MANAGE** permission for the Feature Store can also change Feature Store permissions for all other users.^[access-control-legacy-databricks-on-aws.md]

1. On the Feature Store page, click **Permissions**. This button is only available to workspace administrators and users with **CAN MANAGE** permission for the Feature Store.
2. Edit the permissions and click **Save**.

Permissions set on the Feature Store page apply to all existing and future feature tables. These permissions can only be removed from the Feature Store page. On individual feature table pages, you can override settings to add permissions, but you cannot set more restrictive permissions than those inherited from the Feature Store level. Inherited permissions are marked with the note *“Some permissions cannot be removed because they are inherited.”*^[access-control-legacy-databricks-on-aws.md]

## Related Concepts

* [[Unity Catalog]] – The data governance solution that replaces legacy access controls.
* [[Feature Store]] – The system for managing and serving feature tables.
* [[Feature Table]] – The individual table object subject to these permissions.
* [[Unity Catalog Privilege Management|Unity Catalog Privileges]] – Access control for Unity Catalog-enabled workspaces.

## Sources

* access-control-legacy-databricks-on-aws.md
```

# Citations

1. [access-control-legacy-databricks-on-aws.md](/references/access-control-legacy-databricks-on-aws-0be88992.md)
