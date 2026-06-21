---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3e7e7ce9fea2e1c9a9c1d484026d7f12cd10df9c08ab953f0139b8c2f4adf73b
  pageDirectory: concepts
  sources:
    - enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - enforcing-table-access-control-in-databricks
    - ETACID
  citations:
    - file: enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md
title: Enforcing Table Access Control in Databricks
description: Workspace-level enforcement mechanisms to ensure users only access data through clusters that have table access control enabled.
tags:
  - databricks
  - security
  - enforcement
  - workspace-admin
timestamp: "2026-06-19T10:20:46.481Z"
---

# Enforcing Table Access Control in Databricks

**Enforcing Table Access Control in Databricks** refers to the practice of ensuring that users can only access data through clusters that have table access control enabled, preventing unauthorized data access through unprotected compute resources.

## Overview

Table access control in Databricks restricts user access to data objects based on privileges granted by administrators. However, simply enabling table access control on a cluster is not sufficient to guarantee data security. Administrators must also enforce that users cannot bypass these controls by using clusters without table access control enabled. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Enforcing Table Access Control

To ensure that users access only the data you want them to, you must restrict users to clusters with table access control enabled. This requires two key measures: ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

### Restrict Cluster Creation

Users should not have permission to create clusters. If a user creates a cluster without table access control enabled, they can access any data from that cluster, bypassing all access restrictions. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

### Restrict Cluster Attachment

Users should not have `CAN ATTACH TO` permission for any cluster that is not enabled for table access control. This prevents users from attaching to existing unprotected clusters. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Workspace-Level Enablement

Before users can configure Python and SQL table access control, a Databricks workspace admin must enable table access control for the workspace and deny users access to clusters that are not enabled for table access control. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

To enable table access control at the workspace level:

1. Go to the [settings page](https://docs.databricks.com/aws/en/admin/admin-concepts#admin-settings).
2. Click the **Security** tab.
3. Turn on the **Table Access Control** option.

## Table Access Control Versions

Table access control is available in two versions: ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

### SQL-Only Table Access Control

This version restricts users to SQL commands only. To enable it, set the following flag in the cluster's Spark configuration: ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

```ini
spark.databricks.acl.sqlOnly true
```

Note that access to SQL-only table access control is not affected by the workspace-level "Enable Table Access Control" setting. That setting controls only the workspace-wide enablement of Python and SQL table access control. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

### Python and SQL Table Access Control

This version allows users to run Python commands using the DataFrame API as well as SQL. When enabled on a cluster, users on that cluster: ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

- Can access Spark only using the Spark SQL API or DataFrame API. Access to tables and views is restricted by administrators according to Databricks privileges.
- Must run commands on cluster nodes as a low-privilege user forbidden from accessing sensitive parts of the filesystem or creating network connections to ports other than 80 and 443.
- Only built-in Spark functions can create network connections on ports other than 80 and 443.
- Only workspace admin users or users with `ANY FILE` privilege can read data from external databases through the PySpark JDBC connector.

Attempts to get around these restrictions will fail with an exception. These restrictions ensure that users can never access unprivileged data through the cluster. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Important Considerations

Even if table access control is enabled for a cluster, Databricks workspace administrators have access to file-level data. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

Table access control is not supported with Machine Learning Runtime. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Related Concepts

- [Hive Metastore Privileges and Securable Objects](/concepts/hive-metastore-privileges-and-securable-objects.md) — Setting privileges on data objects once table access control is enabled
- Cluster Access Modes — Standard access mode enables table access control by default
- [Compute Permissions](/concepts/can-manage-permission.md) — Managing cluster-level permissions including CAN ATTACH TO
- [Unity Catalog](/concepts/unity-catalog.md) — Modern data governance solution that supersedes Hive [Metastore](/concepts/metastore.md) table access control
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Alternative access control approach using tags and policies

## Sources

- enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md

# Citations

1. [enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md](/references/enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws-9c6f8fe1.md)
