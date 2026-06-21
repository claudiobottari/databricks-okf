---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f3eaf32c27013f5e6fc6e478fa3d45b64a0d9fb7d79e0783cec924576f715ed0
  pageDirectory: concepts
  sources:
    - enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - enforcing-table-access-control-via-cluster-permissions
    - ETACVCP
  citations:
    - file: enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md
title: Enforcing Table Access Control via Cluster Permissions
description: The practice of denying users the ability to create clusters or attach to clusters without table access control enabled, to ensure data access restrictions are consistently applied.
tags:
  - databricks
  - access-control
  - cluster-permissions
  - security
timestamp: "2026-06-18T12:10:26.554Z"
---

# Enforcing Table Access Control via Cluster Permissions

**Enforcing Table Access Control via Cluster Permissions** refers to the practice of using Hive [Metastore](/concepts/metastore.md) table access control (legacy) on a cluster to restrict user access to data objects based on privileges. This is a legacy capability in Databricks that must be explicitly enabled per cluster and optionally enforced workspace-wide by denying users access to clusters without table access control. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Overview

Table access control for the built-in Hive [Metastore](/concepts/metastore.md) is available in two versions: SQL-only, which restricts users to SQL commands, and Python and SQL, which allows both SQL and Python (DataFrame API) commands but imposes additional runtime restrictions. Both versions require explicit configuration on a cluster and, for the Python and SQL variant, workspace-level enablement by a Databricks admin. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

Table access control is **not supported** with Machine Learning Runtime clusters. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

> **Important:** Even when table access control is enabled for a cluster, Databricks workspace administrators retain access to file-level data. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## SQL-Only Table Access Control

SQL-only table access control restricts cluster users to SQL commands only. To enable it, set the following Spark configuration in the cluster's Spark conf:

```ini
spark.databricks.acl.sqlOnly true
```

When this flag is set, users on that cluster can only interact with data through SQL. Access to tables and views is enforced according to the privileges administrators grant on Hive [Metastore](/concepts/metastore.md) objects. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

Access to SQL-only table access control is **not** affected by the workspace-level **Enable Table Access Control** setting. That setting only controls workspace-wide enablement of the Python and SQL variant. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Python and SQL Table Access Control

This version allows users to run Python commands that use the DataFrame API as well as SQL. When enabled on a cluster, users on that cluster:

- Can access Spark only using the Spark SQL API or DataFrame API. In both cases, access to tables and views is restricted by administrators according to the Databricks privileges on Hive [Metastore](/concepts/metastore.md) objects.
- Must run their commands on cluster nodes as a low-privilege user forbidden from accessing sensitive parts of the filesystem or creating network connections to ports other than 80 and 443.
  - Only built-in Spark functions can create network connections on ports other than 80 and 443.
  - Only workspace admin users or users with the `ANY FILE` privilege can read data from external databases through the PySpark JDBC connector.
  - To allow Python processes to access additional outbound ports, set the Spark config `spark.databricks.pyspark.iptable.outbound.whitelisted.ports` to a comma-separated list of ports or port ranges (e.g., `21,22,9000:9999`). Ports must be within 0–65535.

Attempts to bypass these restrictions will fail with an exception. These safeguards prevent users from accessing unprivileged data through the cluster. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Enabling Table Access Control for the Workspace

Before users can configure Python and SQL table access control on a cluster, a Databricks workspace admin must enable table access control for the workspace and deny users access to clusters that are not enabled for table access control.

1. Go to the admin settings page.
2. Click the **Security** tab.
3. Turn on the **Table Access Control** option.

This workspace-level setting only affects Python and SQL table access control; it does not impact SQL-only mode. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Enforcing Table Access Control

To ensure that users access only the data they are authorized to see, administrators must restrict users to clusters with table access control enabled. Specifically:

- **Users should not have permission to create clusters.** If a user creates a cluster without table access control, they can access any data from that cluster.
- **Users should not have `CAN ATTACH TO` permission** for any cluster that is not enabled for table access control.

For details, see Compute permissions. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Creating a Cluster with Table Access Control Enabled

In clusters using **Standard access mode**, table access control is enabled by default. To create such a cluster via the REST API, see the [Create new cluster](https://docs.databricks.com/api/workspace/clusters/create) endpoint. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

After the cluster is running, administrators can set privileges on Hive [Metastore](/concepts/metastore.md) securable objects. See Hive metastore privileges and securable objects (legacy).

## Related Concepts

- Hive metastore privileges and securable objects (legacy) — How to grant specific permissions on tables, views, and databases.
- [Cluster access modes](/concepts/databricks-connect-cluster-access-modes.md) — Standard mode vs. other modes; table access control is enabled by default in Standard mode.
- Compute permissions — Controlling who can create, attach to, and manage clusters.

## Sources

- enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md

# Citations

1. [enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md](/references/enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws-9c6f8fe1.md)
