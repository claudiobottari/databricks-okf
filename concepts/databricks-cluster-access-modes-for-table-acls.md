---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5205d1983df715fa810d62c7e5a1a06cc6408b3224b0cf88d0e6d54457bdd136
  pageDirectory: concepts
  sources:
    - enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-cluster-access-modes-for-table-acls
    - DCAMFTA
  citations:
    - file: enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md
title: Databricks Cluster Access Modes for Table ACLs
description: How table access control is enabled by default in Standard access mode clusters and configured via Spark conf settings.
tags:
  - databricks
  - compute
  - clusters
  - access-modes
timestamp: "2026-06-19T10:21:00.128Z"
---

# Databricks Cluster Access Modes for Table ACLs

**Databricks Cluster Access Modes for Table ACLs** define how table access control (a legacy Hive [Metastore](/concepts/metastore.md) security feature) is enforced on a cluster. Two access modes are available: **SQL-only table access control** and **Python and SQL table access control**. These modes control which commands users can run and how data access is restricted.

## Overview

Table access control for the built-in Hive [Metastore](/concepts/metastore.md) must be enabled at the cluster level before administrators can grant privileges on securable objects. Databricks offers two versions of table access control, each with different restrictions on user commands. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

> **Important:** Even when table access control is enabled for a cluster, Databricks workspace administrators retain access to file-level data. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

Table access control is **not supported** with Machine Learning Runtime. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## SQL‑Only Table Access Control

This mode restricts users to SQL commands only. To enable it on a cluster, set the following Spark configuration:

```ini
spark.databricks.acl.sqlOnly true
```

^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

Note that access to SQL‑only table access control is **not** affected by the workspace-wide *Enable Table Access Control* setting. That setting controls only the Python and SQL version. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Python and SQL Table Access Control

This mode allows users to run both SQL and Python commands that use the DataFrame API. When it is enabled on a cluster, the following restrictions apply: ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

- Users can access Spark **only** through the Spark SQL API or DataFrame API. Access to tables and views is restricted by administrators according to Hive metastore privileges and securable objects (legacy).
- Commands execute as a low‑privilege user that cannot:
  - Access sensitive parts of the filesystem.
  - Create network connections to ports other than 80 and 443, except:
    - Built‑in Spark functions can create connections on any port.
    - Workspace admins or users with `ANY FILE` privilege can read data via the PySpark JDBC connector.
- To allow Python processes to access additional outbound ports, set the Spark configuration `spark.databricks.pyspark.iptable.outbound.whitelisted.ports` to a comma‑separated list of ports or ranges (e.g., `21,22,9000:9999`). Ports must be in the range 0–65535. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

Attempts to bypass these restrictions result in exceptions. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Enable Table Access Control for the Workspace

Before users can configure Python and SQL table access control, a Databricks workspace admin must enable it at the workspace level and deny users access to clusters that are not enabled: ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

1. Go to the [admin settings page](https://docs.databricks.com/aws/en/admin/admin-concepts#admin-settings).
2. Click the **Security** tab.
3. Turn on the **Table Access Control** option.

### Enforce Table Access Control

To ensure users access only the data you intend them to, restrict them to clusters with table access control enabled. In particular: ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

- Ensure users **do not** have permission to create clusters (a cluster without table access control would allow unrestricted data access).
- Ensure users **do not** have `CAN ATTACH TO` permission for any cluster that is not enabled for table access control.

See Compute permissions for more information. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Create a Cluster Enabled for Table Access Control

Table access control is enabled **by default** in clusters with [Standard Access Mode](/concepts/standard-access-mode.md). ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

To create a cluster using the REST API, see [Create new cluster](https://docs.databricks.com/api/workspace/clusters/create). ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Set Privileges on a Data Object

Once table access control is enabled on a cluster, administrators can grant privileges on Hive [Metastore](/concepts/metastore.md) securable objects. See Hive metastore privileges and securable objects (legacy). ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Sources

- enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md

# Citations

1. [enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md](/references/enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws-9c6f8fe1.md)
