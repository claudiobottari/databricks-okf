---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 70b06096479219771edc5f3c0c06d26564407fa9546f485604b27f7a3c29d33f
  pageDirectory: concepts
  sources:
    - enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - python-and-sql-table-access-control
    - SQL Table Access Control and Python
    - PASTAC
    - Python and SQL Table Access Control (legacy)
  citations:
    - file: enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md
title: Python and SQL Table Access Control
description: A version of table access control that allows users to run SQL, Python, and PySpark DataFrame API commands while enforcing low-privilege user restrictions and network/firewall constraints.
tags:
  - databricks
  - security
  - python
  - pyspark
  - access-control
timestamp: "2026-06-19T18:39:50.066Z"
---

# Python and SQL Table Access Control

**Python and SQL Table Access Control** is a legacy access control mode for the built-in [Hive metastore](/concepts/built-in-hive-metastore.md) on Databricks clusters. It allows users to run both SQL and Python commands that use the DataFrame API while restricting access to tables and views based on administrator-defined privileges. This mode is distinct from [SQL-only Table Access Control](/concepts/sql-only-table-access-control.md), which limits users to SQL commands only. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Overview

When Python and SQL table access control is enabled on a cluster, users on that cluster can access Spark only using the Spark SQL API or the DataFrame API. In both cases, access to tables and views is restricted according to the Hive metastore privileges and securable objects (legacy) set by administrators. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Enabling Python and SQL Table Access Control

### Cluster-Level Enablement

Python and SQL table access control is the **default behavior** when table access control is enabled on a cluster and the `spark.databricks.acl.sqlOnly` Spark configuration is **not** set to `true`. To instead enable SQL-only mode, set:

```ini
spark.databricks.acl.sqlOnly true
```

If this flag is not present (or set to `false`), the cluster uses Python and SQL table access control. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

### Workspace-Level Enablement

Before users can configure Python and SQL table access control, a Databricks workspace admin must enable table access control at the workspace level and deny users access to clusters that are not enabled for table access control. The steps are: ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

1. Go to the workspace **settings page**.
2. Click the **Security** tab.
3. Turn on the **Table Access Control** option.

After this setting is enabled, users can only use clusters that have table access control turned on (which is the default in clusters with [Standard Access Mode](/concepts/standard-access-mode.md)). ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

### Enforcement

To ensure users access only the data they are permitted to see, administrators should: ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

- **Restrict cluster creation** – Users should not have permission to create clusters, because a cluster without table access control would allow access to any data.
- **Restrict cluster attachment** – Users should not be granted `CAN ATTACH TO` permission for any cluster that is not enabled for table access control.

See Compute permissions for details on cluster-level permissions. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

### Using the REST API

To create a cluster with table access control enabled via the REST API, use the [Create new cluster](https://docs.databricks.com/api/workspace/clusters/create) endpoint. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## User Restrictions

When Python and SQL table access control is active, users are subject to the following restrictions: ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

- **Low-privilege execution** – User commands run on cluster nodes as a low-privilege user that cannot access sensitive parts of the filesystem or create network connections to ports other than 80 and 443.
  - Only built-in Spark functions can create network connections on ports other than 80 and 443.
  - Only workspace admin users or users with the `ANY FILE` privilege can read data from external databases through the PySpark JDBC connector.
- **Outbound port configuration** – If Python processes need to access additional outbound ports, administrators can set the Spark config `spark.databricks.pyspark.iptable.outbound.whitelisted.ports` to a comma-separated list of ports or port ranges (e.g., `21,22,9000:9999`). Ports must be in the range 0–65535. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

Attempts to circumvent these restrictions result in an exception. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Important Notes

- Python and SQL table access control is **not supported** with Machine Learning Runtime. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]
- Even when table access control is enabled for a cluster, Databricks workspace administrators retain access to file-level data. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]
- Access to SQL-only table access control is unaffected by the workspace-level "Enable Table Access Control" setting. That setting controls only the workspace-wide enablement of Python and SQL table access control. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Granting Privileges

See Hive metastore privileges and securable objects (legacy) for details on how to set privileges on data objects once table access control is enabled. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Related Concepts

- [Table access control (legacy)](/concepts/table-access-control-tacl.md) – Overview of Hive [Metastore](/concepts/metastore.md) access control
- [SQL-only Table Access Control](/concepts/sql-only-table-access-control.md) – A restricted variant that allows only SQL commands
- [Standard Access Mode](/concepts/standard-access-mode.md) – The default cluster access mode that enables table access control
- [Unity Catalog](/concepts/unity-catalog.md) – The modern data governance solution that supersedes Hive [Metastore](/concepts/metastore.md) ACLs

## Sources

- enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md

# Citations

1. [enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md](/references/enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws-9c6f8fe1.md)
