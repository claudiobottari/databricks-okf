---
title: Disable access to the Hive metastore used by your Databricks workspace | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/disable-hms
ingestedAt: "2026-06-18T08:04:26.650Z"
---

This page describes how to disable direct access to the legacy Hive metastore that is used by your Databricks workspace, whether the workspace-local Hive metastore or an external Hive metastore, including AWS Glue. When you've completed your Unity Catalog migration or federated your Hive metastore as a foreign catalog that is governed by Unity Catalog, you can use a simple workspace admin setting to prevent users from bypassing Unity Catalog and accessing tables registered in the Hive metastore.

Data in Hive metastore is not governed by Unity Catalog. Disabling direct Hive metastore access is an important step in the process of migrating to Unity Catalog and ensuring that you take full advantage of Unity Catalog data governance. You can disable direct access and continue to query tables managed by your Hive metastore by taking advantage of Hive metastore federation. You can federate Hive metastore tables either before or after you disable direct workspace access to the Hive metastore. See [Upgrade Hive tables and views to Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/migrate) and [Hive metastore federation: enable Unity Catalog to govern tables registered in a Hive metastore](https://docs.databricks.com/aws/en/query-federation/hms-federation-concepts).

important

Even after migrating to Unity Catalog, Databricks compute clusters connect to the Hive metastore by default unless you explicitly disable Hive metastore access. To prevent Hive metastore maintenance from affecting your Unity Catalog workloads, you can disable direct access to Hive metastore for all clusters and workloads at once ([Disable all direct access to the Hive metastore](#disable-hms-workspace)), or use a Spark configuration to disable access on a cluster-by-cluster basis ([Disable all direct access to the Hive metastore](#disable-hms-workspace)).

To disable access to the Hive metastore at the account level for new workspaces, use the [Disable legacy features](https://docs.databricks.com/aws/en/admin/account-settings/legacy-features) account setting.

Before you disable the legacy Hive metastore, you should meet the following criteria:

*   You're done migrating all tables registered in the legacy metastore to Unity Catalog, or you have always used Unity Catalog and never the legacy Hive metastore.
*   You want to force your users to stop using tables registered in the legacy metastore.
*   You have upgraded all jobs to Databricks Runtime 13.3 LTS or above.

After you disable the legacy metastore:

*   Any jobs running against tables registered to the Hive metastore will fail.
    
*   [Fallback](https://docs.databricks.com/aws/en/query-federation/hms-federation-concepts#fallback) is disabled.
    
*   Jobs that run on Databricks Runtime versions below 13.3 will fail.
    
    Currently running jobs will continue to work until they are terminated, but restarts on those clusters will fail.
    
*   The **Legacy** heading and `hive_metastore` catalog disappear from the Catalog Explorer browser pane.
    
*   SQL commands that attempt to show the contents of the `hive_metastore` catalog will fail.
    

note

Disabling legacy access does not prevent users from using cluster-level credentials, such as instance profiles or service principals, that are available on a cluster. Databricks recommends that you remove such credentials from your clusters.

_No Isolation shared_ clusters do not respect the legacy Hive metastore disablement setting. To prevent users from creating and using such clusters, enable the _Enforce User Isolation_ setting for the workspace. See [Enforce user isolation cluster types on a workspace](https://docs.databricks.com/aws/en/admin/workspace-settings/enforce-user-isolation).

Disable your workspace's legacy Hive metastore using the **Disable legacy access** workspace admin setting:

1.  As a workspace admin, log in to your Databricks workspace.
2.  Click the user profile menu at the top right and select **Settings** from the menu.
3.  Go to **Workspace admin > Security**.
4.  Set **Disable legacy access** to **Disabled: legacy access features cannot be used**.
5.  To ensure that the new setting has taken effect, wait approximately five minutes.
6.  Restart all running clusters.

## Disable access for individual compute clusters[​](#disable-access-for-individual-compute-clusters "Direct link to disable-access-for-individual-compute-clusters")

You can also disable direct access to the Hive metastore gradually, on a cluster-by-cluster basis. This approach can be useful during a Unity Catalog migration when you want to reduce reliance on Hive metastore incrementally until you can disable it for the entire workspace.

To disable direct access, set the following [Spark configurations](https://docs.databricks.com/aws/en/compute/configure#spark-configuration) on the cluster:

    spark.databricks.unityCatalogOnlyMode Truespark.databricks.sql.initial.catalog.namespace <catalog-name>

Replace `<catalog-name>` with the name of a Unity Catalog catalog that exists in your metastore. When you enable Unity Catalog\-only mode, you must also set an initial catalog because the cluster can no longer use `hive_metastore` as the [default catalog](https://docs.databricks.com/aws/en/catalogs/default).
