---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 62b98a3742551d82ee9a41bbc54f58d9b6f4bfd3c1ff46335597a0d94093f2e4
  pageDirectory: concepts
  sources:
    - custom-classifiers-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-classifier-requirements-and-permissions
    - Permissions and Custom Classifier Requirements
    - CCRAP
  citations:
    - file: custom-classifiers-databricks-on-aws.md
title: Custom Classifier Requirements and Permissions
description: To use custom classifiers, users must be metastore admins, have ASSIGN privileges on the governed tag, SELECT on example columns, and have Data Classification enabled with serverless compute available.
tags:
  - permissions
  - requirements
  - security
timestamp: "2026-06-19T09:38:58.005Z"
---

## Custom Classifier Requirements and Permissions

Custom classifiers extend [Databricks Data Classification](/concepts/databricks-data-classification.md) to detect sensitive data specific to your organization, such as internal employee IDs or proprietary product codes. To create, edit, or delete custom classifiers, users must satisfy a set of prerequisites and hold specific privileges in [Unity Catalog](/concepts/unity-catalog.md). ^[custom-classifiers-databricks-on-aws.md]

### Requirements

- **Data Classification must be enabled** on at least one catalog in the [Metastore](/concepts/metastore.md). Without an active classification scan scope, custom classifiers cannot generate detection rules. ^[custom-classifiers-databricks-on-aws.md]
- **Serverless compute** must be available in the workspace. This is enabled by default in workspaces with Unity Catalog. ^[custom-classifiers-databricks-on-aws.md]
- **Metastore admin role** is required to create, edit, or delete any custom classifier. Non-admin users cannot perform these actions even if they have other permissions. ^[custom-classifiers-databricks-on-aws.md]
- **`ASSIGN` privilege on the governed tag** is necessary when creating or editing a custom classifier. The classifier uses a [governed tag](/concepts/governed-tags.md) (and an optional tag value) to identify the data class. ^[custom-classifiers-databricks-on-aws.md]
- **`SELECT` privilege on the table** that contains the example column is required to select that column as a reference for the classifier. The user must have `SELECT` on the table holding the column. ^[custom-classifiers-databricks-on-aws.md]

### Permissions Summary

| Action | Required Role / Privilege |
|---|---|
| Create custom classifier | [Metastore](/concepts/metastore.md) admin + `ASSIGN` on the governed tag |
| Edit custom classifier (update example columns) | [Metastore](/concepts/metastore.md) admin + `ASSIGN` on the governed tag |
| Delete custom classifier | [Metastore](/concepts/metastore.md) admin only |
| Select an example column | `SELECT` on the table containing the column |

Additionally, custom classifier configuration and detection metadata are encrypted at rest. Workspace admins can use a customer-managed key (CMK) on the system catalog to manage this encryption. Configuring a CMK on the system catalog encrypts all data in that catalog, not just custom classifier data. ^[custom-classifiers-databricks-on-aws.md]

### Limitations Affecting Permissions

- The governed tag used by a custom classifier cannot be changed after creation. To use a different tag, delete the classifier and create a new one. ^[custom-classifiers-databricks-on-aws.md]
- You can create up to 50 custom classifiers per [Metastore](/concepts/metastore.md), and each must reference 1–10 example columns. ^[custom-classifiers-databricks-on-aws.md]

### Troubleshooting Permission Issues

- **Permission denied when creating or listing custom classifiers**: Verify you are a [Metastore](/concepts/metastore.md) admin and, for creation/editing, have the `ASSIGN` privilege on the governed tag. ^[custom-classifiers-databricks-on-aws.md]
- **Cannot select an example column**: Ensure you have `SELECT` on the table that contains the column. If not, ask the table owner to grant it, or choose a different column. ^[custom-classifiers-databricks-on-aws.md]

### Related Concepts

- [Data Classification](/concepts/data-classification.md) – Enabling scans to detect sensitive data.
- [Governed Tags](/concepts/governed-tags.md) – The attribute system used by custom classifiers.
- [Metastore Admin](/concepts/metastore-admin-role.md) – Role required to manage classifiers.
- ASSIGN privilege – Required on governed tags for classifier creation.
- SELECT privilege – Required on tables for example column selection.
- Serverless Compute – Prerequisite for classification features.
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) environment.

### Sources

- custom-classifiers-databricks-on-aws.md

# Citations

1. [custom-classifiers-databricks-on-aws.md](/references/custom-classifiers-databricks-on-aws-61f050db.md)
