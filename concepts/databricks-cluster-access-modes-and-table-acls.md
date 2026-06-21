---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b66abd9ff5b613c7bfc717de22e34d8096f9b7da7e37258587fd58a4799071b2
  pageDirectory: concepts
  sources:
    - enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-cluster-access-modes-and-table-acls
    - Table ACLs and Databricks Cluster Access Modes
    - DCAMATA
  citations:
    - file: enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md
title: Databricks Cluster Access Modes and Table ACLs
description: Table access control is enabled by default on clusters with Standard access mode, and is not supported on Machine Learning Runtime.
tags:
  - databricks
  - compute
  - access-control
  - clusters
timestamp: "2026-06-18T15:36:00.741Z"
---

# Databricks Cluster Access Modes and Table ACLs

**Databricks Cluster Access Modes and Table ACLs** refers to the mechanisms for controlling user access to data in the built-in Hive [Metastore](/concepts/metastore.md) by enabling table access control on specific cluster access modes. Table ACLs (Access Control Lists) allow administrators to grant or revoke privileges on Hive [Metastore](/concepts/metastore.md) objects such as tables, views, and databases. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Overview

Table access control is a legacy feature of the Hive [Metastore](/concepts/metastore.md) that restricts what data users can see and manipulate through a cluster. It is available in two versions: **SQL-only table access control** and **Python and SQL table access control**. The version you choose determines which APIs users can employ and the security restrictions applied. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

Access modes determine the level of isolation and security on a cluster. Table access control is enabled by default on clusters with **Standard access mode**. For custom clusters, administrators must explicitly configure table access control through Spark Config settings. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## SQL-Only Table Access Control

This version restricts users to **SQL commands only**. To enable it, set the following Spark configuration property on the cluster:

```
spark.databricks.acl.sqlOnly true
```

When SQL-only mode is active, users cannot run Python or PySpark commands. This mode is not affected by the workspace-level **Enable Table Access Control** toggle; it operates independently. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Python and SQL Table Access Control

This version allows users to run **SQL** as well as **Python commands that use the DataFrame API**. When enabled, the following restrictions apply:

- Users may only access tables and views using the Spark SQL API or DataFrame API. Access is limited according to privileges granted by administrators.
- User code runs as a low‑privilege operating system user that cannot access sensitive parts of the filesystem or create network connections except to ports 80 and 443.
- Only built‑in Spark functions can open network connections on other ports.
- Only workspace admins or users with the [ANY FILE Privilege](/concepts/any-file-securable.md) can read data from external databases via the PySpark JDBC connector.
- To allow Python processes to access additional outbound ports, set the Spark configuration `spark.databricks.pyspark.iptable.outbound.whitelisted.ports` to a comma‑separated list of port numbers or port ranges (e.g., `21,22,9000:9999`). Ports must be in the valid range 0–65535.

Attempts to bypass these restrictions result in exceptions. These safeguards prevent users from reaching unprivileged data. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Enabling Table Access Control

### Cluster‑Level Enablement

- **Standard access mode**: Table access control is enabled by default.
- **Custom clusters**: You must set the appropriate Spark configuration (SQL‑only or Python+SQL) in the cluster’s Spark configuration.
- **REST API**: When creating a cluster via the [Create new cluster API](https://docs.databricks.com/api/workspace/clusters/create), include the relevant Spark configuration.

Table access control is **not supported** on [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md). ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

### Workspace‑Level Enablement (Python+SQL only)

Before users can configure Python and SQL table access control on clusters, a Databricks [Workspace Admin](/concepts/workspace-admin-unity-catalog.md) must enable table access control for the workspace:

1. Navigate to the **Settings** page.
2. Click the **Security** tab.
3. Turn on **Table Access Control**.

This setting controls only the workspace‑wide enablement of Python and SQL table access control; it does not affect SQL‑only mode. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Enforcing Table Access Control

To ensure users only access authorized data, administrators must restrict users to clusters that have table access control enabled. Specifically:

- Users should **not** have permission to create clusters. A cluster created without table access control allows full data access.
- Users should **not** have `CAN ATTACH TO` permission on any cluster that lacks table access control.

See [Cluster Permissions](/concepts/cluster-scoped-data-access-permissions.md) for details. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Setting Privileges on Data Objects

Once table access control is enabled on a cluster, administrators set privileges on Hive [Metastore](/concepts/metastore.md) securable objects (databases, tables, views, etc.) using standard SQL `GRANT` and `REVOKE` statements. For a complete list of privilege types, see [Hive Metastore Privileges and Securable Objects (Legacy)](/concepts/hive-metastore-privileges-and-securable-objects.md). ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Important Notes

- Even with table access control enabled, **workspace administrators always have access to file‑level data** on the cluster. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The modern data governance solution replacing Hive [Metastore](/concepts/metastore.md) ACLs.
- [Hive Metastore](/concepts/built-in-hive-metastore.md) – Legacy metadata store for Databricks tables.
- Spark Config – Configuration properties for cluster behavior.
- DataFrame API – Python API used with table access control.
- [ANY FILE Privilege](/concepts/any-file-securable.md) – Privilege allowing read access to external data sources.
- [Workspace Admin](/concepts/workspace-admin-unity-catalog.md) – Administrative role in Databricks.
- [Cluster Permissions](/concepts/cluster-scoped-data-access-permissions.md) – Permissions for creating, attaching to, and managing clusters.

## Sources

- enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md

# Citations

1. [enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md](/references/enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws-9c6f8fe1.md)
