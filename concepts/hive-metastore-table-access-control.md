---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e3feee3377a3dca2435c567205e5b71d0643ebd2386190e14b31ffeb1e7564d4
  pageDirectory: concepts
  sources:
    - enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - hive-metastore-table-access-control
    - HMTAC
    - Hive metastore table
  citations:
    - file: enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md
title: Hive Metastore Table Access Control
description: A Databricks security feature that restricts access to Hive metastore tables and views on a cluster based on administrator-defined privileges.
tags:
  - databricks
  - security
  - hive-metastore
  - access-control
timestamp: "2026-06-19T18:39:43.116Z"
---

# Hive [Metastore](/concepts/metastore.md) Table Access Control

**Hive [Metastore](/concepts/metastore.md) Table Access Control** is a legacy feature on Databricks that allows administrators to restrict user access to data objects stored in the built-in [Hive metastore](/concepts/built-in-hive-metastore.md). When enabled on a cluster, users are limited to only the tables, views, and other securable objects for which they have been granted privileges. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Versions of Table Access Control

Table access control is available in two versions: **SQL-only** and **Python and SQL**. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

### SQL-only Table Access Control

This version restricts users to SQL commands only. It is enabled by setting the Spark configuration `spark.databricks.acl.sqlOnly` to `true` in the cluster's Spark conf. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

Note that this setting is **not** affected by the workspace-level **Enable Table Access Control** toggle. That toggle controls only the workspace-wide enablement of the Python and SQL version. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

SQL-only table access control is particularly useful when you want to allow SQL-based access to data while preventing execution of arbitrary Python or PySpark code that might bypass access restrictions. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

### Python and SQL Table Access Control

This version lets users run both SQL and Python commands that use the DataFrame API on clusters where it is enabled. When active, users on that cluster: ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

- Can access Spark only through the Spark SQL API or DataFrame API. Access to tables and views is restricted according to the privileges granted by administrators. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]
- Must run their commands as a low-privilege user, forbidden from accessing sensitive parts of the filesystem or creating network connections to ports other than 80 and 443. Only built-in Spark functions can create network connections on other ports. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]
- Only workspace admin users or users with the `ANY FILE` privilege can read data from external databases through the PySpark JDBC connector. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]
- If Python processes need additional outbound ports, administrators can set the Spark configuration `spark.databricks.pyspark.iptable.outbound.whitelisted.ports` to a comma-separated list of ports or port ranges (e.g., `21,22,9000:9999`). ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

Attempts to bypass these restrictions will raise an exception. The restrictions are designed so that users can never access unprivileged data through the cluster. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Workspace-Level Enablement

Before users can configure Python and SQL table access control, a Databricks workspace admin must enable the feature at the workspace level and deny users access to clusters that are not enabled for table access control. To do this: ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

1. Go to the admin settings page.
2. Click the **Security** tab.
3. Turn on the **Table Access Control** option.

## Enforcing Table Access Control

To ensure users access only the data intended for them, administrators must restrict users to clusters that have table access control enabled. Specifically: ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

- Users should not have permission to create clusters. A cluster created without table access control would allow unrestricted data access.
- Users should not have `CAN ATTACH TO` permission for any cluster that is not enabled for table access control.

See Compute permissions for further details. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Creating a Cluster with Table Access Control

Table access control is enabled by default in clusters with **Standard access mode**. For clusters created via the REST API, see [Create new cluster](https://docs.databricks.com/api/workspace/clusters/create). ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Setting Privileges on Data Objects

Once table access control is enabled on a cluster, administrators can grant or revoke privileges on Hive [Metastore](/concepts/metastore.md) securable objects such as databases, tables, views, and functions. See Hive metastore privileges and securable objects (legacy) for details. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Limitations

- Table access control is **not supported** with Machine Learning Runtime. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]
- Even when table access control is enabled for a cluster, Databricks workspace administrators retain access to file-level data. ^[enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Table access control](/concepts/table-access-control-tacl.md)
- Spark conf
- DataFrame API
- [Hive metastore](/concepts/built-in-hive-metastore.md)

## Sources

- enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md

# Citations

1. [enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws.md](/references/enable-hive-metastore-table-access-control-on-a-cluster-legacy-databricks-on-aws-9c6f8fe1.md)
