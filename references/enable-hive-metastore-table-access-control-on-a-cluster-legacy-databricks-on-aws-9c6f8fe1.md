---
title: Enable Hive metastore table access control on a cluster (legacy) | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/table-acls/table-acl
ingestedAt: "2026-06-18T08:03:50.633Z"
---

This article describes how to enable table access control for the built-in Hive metastore on a cluster.

For information about how to set privileges on Hive metastore securable objects once table access control has been enabled on a cluster, see [Hive metastore privileges and securable objects (legacy)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/table-acls/object-privileges).

## Enable table access control for a cluster[​](#enable-table-access-control-for-a-cluster "Direct link to enable-table-access-control-for-a-cluster")

Table access control is available in two versions:

*   [SQL-only table access control](#sql-only-table-access-control), which restricts users to SQL commands.
*   [Python and SQL table access control](#python-and-sql-table-access-control), which allows users to run SQL, Python, and PySpark commands.

Table access control is not supported with [Machine Learning Runtime](https://docs.databricks.com/aws/en/machine-learning/).

important

Even if table access control is enabled for a cluster, Databricks workspace administrators have access to file-level data.

### SQL-only table access control[​](#sql-only-table-access-control "Direct link to sql-only-table-access-control")

This version of table access control restricts users to SQL commands only.

To enable SQL-only table access control on a cluster and restrict that cluster to use only SQL commands, set the following flag in the cluster's [Spark conf](https://docs.databricks.com/aws/en/compute/configure#spark-configuration):

ini

    spark.databricks.acl.sqlOnly true

note

Access to SQL-only table access control is not affected by the [Enable Table Access Control](#enable-table-acl-workspace) setting in the admin settings page. That setting controls only the workspace-wide enablement of Python and SQL table access control.

### Python and SQL table access control[​](#python-and-sql-table-access-control "Direct link to python-and-sql-table-access-control")

This version of table access control lets users run Python commands that use the DataFrame API as well as SQL. When it is enabled on a cluster, users on that cluster:

*   Can access Spark only using the Spark SQL API or DataFrame API. In both cases, access to tables and views is restricted by administrators according to the Databricks [Privileges you can grant on Hive metastore objects](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/table-acls/object-privileges#privilege-types).
*   Must run their commands on cluster nodes as a low-privilege user forbidden from accessing sensitive parts of the filesystem or creating network connections to ports other than 80 and 443.
    *   Only built-in Spark functions can create network connections on ports other than 80 and 443.
    *   Only workspace admin users or users with [ANY FILE](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/table-acls/object-privileges#privilege-types) privilege can read data from external databases through the [PySpark JDBC connector](https://docs.databricks.com/aws/en/archive/connectors/jdbc).
    *   If you want Python processes to be able to access additional outbound ports, you can set the [Spark config](https://docs.databricks.com/aws/en/compute/configure#spark-configuration) `spark.databricks.pyspark.iptable.outbound.whitelisted.ports` to the ports you want to allow access. The supported format of the configuration value is `[port[:port][,port[:port]]...]`, for example: `21,22,9000:9999`. The port must be within the valid range, that is, `0-65535`.

Attempts to get around these restrictions will fail with an exception. These restrictions are in place so that users can never access unprivileged data through the cluster.

## Enable table access control for your workspace[​](#enable-table-access-control-for-your-workspace "Direct link to enable-table-access-control-for-your-workspace")

Before users can configure Python and SQL table access control, a Databricks workspace admin must enable table access control for the Databricks workspace and deny users access to clusters that are not enabled for table access control.

1.  Go to the [settings page](https://docs.databricks.com/aws/en/admin/admin-concepts#admin-settings).
2.  Click the **Security** tab.
3.  Turn on the **Table Access Control** option.

### Enforce table access control[​](#enforce-table-access-control "Direct link to enforce-table-access-control")

To ensure that your users access only the data that you want them to, you must restrict your users to clusters with table access control enabled. In particular, you should ensure that:

*   Users do not have permission to create clusters. If they create a cluster without table access control, they can access any data from that cluster.
*   Users do not have CAN ATTACH TO permission for any cluster that is not enabled for table access control.

See [Compute permissions](https://docs.databricks.com/aws/en/compute/clusters-manage#cluster-level-permissions) for more information.

## Create a cluster enabled for table access control[​](#create-a-cluster-enabled-for-table-access-control "Direct link to create-a-cluster-enabled-for-table-access-control")

Table access control is enabled by default in clusters with [Standard access mode](https://docs.databricks.com/aws/en/compute/configure#access-mode).

To create the cluster using the REST API, see [Create new cluster](https://docs.databricks.com/api/workspace/clusters/create).

## Set privileges on a data object[​](#set-privileges-on-a-data-object "Direct link to Set privileges on a data object")

See [Hive metastore privileges and securable objects (legacy)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/table-acls/object-privileges).
