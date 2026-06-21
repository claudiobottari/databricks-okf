---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 19c2d85f3d45433422ff94c24c3738b7b84ab7bab6baf2c9e455e62d24a55fc0
  pageDirectory: concepts
  sources:
    - enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - enforcing-table-access-control-via-workspace-settings
    - ETACVWS
  citations:
    - file: enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md
title: Enforcing Table Access Control via Workspace Settings
description: Workspace-level administrative controls to enable table access control and restrict users to secured clusters with table access control enabled.
tags:
  - databricks
  - administration
  - access-control
  - workspace
timestamp: "2026-06-18T15:35:45.749Z"
---

# Enforcing Table Access Control via Workspace Settings

**Enforcing Table Access Control via Workspace Settings** refers to the administrative configuration in Databricks that enables table access control at the workspace level and restricts users to clusters that enforce those controls. This ensures that users can only access data according to the privileges granted by administrators.

## Overview

Table access control in Databricks can be enabled at two levels: the cluster level and the workspace level. Workspace-level enforcement is a critical security measure that prevents users from bypassing access controls by using clusters that do not have table access control enabled. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Enabling Table Access Control for the Workspace

Before users can configure Python and SQL table access control on clusters, a Databricks workspace admin must enable table access control for the entire workspace. This is done through the admin settings page:

1. Go to the [settings page](https://docs.databricks.com/aws/en/admin/admin-concepts#admin-settings).
2. Click the **Security** tab.
3. Turn on the **Table Access Control** option.

^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Enforcing Table Access Control

To ensure that users access only the data that administrators intend, workspace admins must restrict users to clusters with table access control enabled. This enforcement requires two key measures: ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

- **Restrict cluster creation permissions**: Users should not have permission to create clusters. If a user creates a cluster without table access control, they can access any data from that cluster. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]
- **Restrict cluster attachment permissions**: Users should not have CAN ATTACH TO permission for any cluster that is not enabled for table access control. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

For more information on managing these permissions, see Compute permissions. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Important Security Note

Even when table access control is enabled for a cluster, Databricks workspace administrators retain access to file-level data. This means that workspace admins can still access underlying data files directly, regardless of the table access control settings. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Related Concepts

- Table Access Control (Legacy) — The overall framework for controlling access to Hive [Metastore](/concepts/metastore.md) objects
- [Hive Metastore Privileges and Securable Objects](/concepts/hive-metastore-privileges-and-securable-objects.md) — The specific privileges that can be granted on data objects
- Cluster Access Modes — How access modes like Standard access mode enable table access control by default
- [Compute Permissions](/concepts/can-manage-permission.md) — Managing who can create, attach to, and manage clusters
- [Unity Catalog](/concepts/unity-catalog.md) — The modern alternative to Hive [Metastore](/concepts/metastore.md) table access control

## Sources

- enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md

# Citations

1. [enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md](/references/enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws-9c6f8fe1.md)
