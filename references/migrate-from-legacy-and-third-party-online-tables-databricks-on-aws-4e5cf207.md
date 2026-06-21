---
title: Migrate from legacy and third-party online tables | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/feature-store/migrate-from-online-tables
ingestedAt: "2026-06-18T08:10:23.164Z"
---

Migrate your existing online tables to one of the following:

*   An online feature store
*   A Lakebase synced table

## List all existing online tables[​](#list-all-existing-online-tables "Direct link to List all existing online tables")

To see all existing online tables in your workspace, use a SQL query or a Python script.

*   SQL
*   Python

Replace `<workspace_url>` and `<workspace_id>` with your workspace information.

SQL

    SELECT  CONCAT("https://<workspace_url>/pipelines/", usage_metadata.dlt_pipeline_id, "?o=<workspace_id>"),  SUM(usage_quantity)FROM  system.billing.usageWHERE  usage_date > DATE_SUB(NOW(), 7)  AND billing_origin_product = 'ONLINE_TABLES'GROUP BY  ALL;

## Migrate online tables to online feature store for model or feature serving endpoints[​](#migrate-online-tables-to-online-feature-store-for-model-or-feature-serving-endpoints "Direct link to Migrate online tables to online feature store for model or feature serving endpoints")

info

After you publish your feature tables to [Online Feature Store](https://docs.databricks.com/aws/en/machine-learning/feature-store/online-feature-store), any subsequent change to your serving endpoints - including scaling operations - automatically switches them to use Online Feature Store as the default source. Ensure your downstream systems are prepared for this change before publishing.

### Step 1: Create an online feature store and publish the feature tables[​](#step-1-create-an-online-feature-store-and-publish-the-feature-tables "Direct link to Step 1: Create an online feature store and publish the feature tables")

Databricks recommends creating a single online store per workspace for testing and proof of concept. For production use cases or isolation requirements, you can provision additional stores.

Python

    from databricks.feature_engineering import FeatureEngineeringClientfe = FeatureEngineeringClient()# Create a single online store that can support multiple feature tablesfe.create_online_store(    name="online-feature-store",    capacity="CU_2")

For details on publishing feature tables, see [Databricks Online Feature Stores](https://docs.databricks.com/aws/en/machine-learning/feature-store/online-feature-store).

### Step 2: Redeploy your serving endpoint with the `FEATURE_SOURCE` environment variable[​](#step-2-redeploy-your-serving-endpoint-with-the-feature_source-environment-variable "Direct link to step-2-redeploy-your-serving-endpoint-with-the-feature_source-environment-variable")

To switch your serving endpoint to the new online store, set the `FEATURE_SOURCE` environment variable to `DATABRICKS_ONLINE_STORE` on each served entity and redeploy the endpoint.

You can configure this in the serving endpoint UI under **Advanced configuration > Environment variables**, or by using the REST API.

### Step 3: Verify migration and clean up your online tables[​](#step-3-verify-migration-and-clean-up-your-online-tables "Direct link to Step 3: Verify migration and clean up your online tables")

After your next endpoint change, verify that the endpoint is using the new online store by checking if the endpoint events contain messages like `Linked to Online Feature Store table: "table name"`. See [Monitor model quality and endpoint health](https://docs.databricks.com/aws/en/machine-learning/model-serving/monitor-diagnose-endpoints).

Once verified, delete your legacy online tables. See [Delete an online table using the UI](#delete-an-online-table-using-the-ui) or [Delete an online table using APIs](#delete-an-online-table-using-apis).

## Migrate online tables to synced tables for OLTP[​](#migrate-online-tables-to-synced-tables-for-oltp "Direct link to Migrate online tables to synced tables for OLTP")

info

Lakebase Provisioned is the original Lakebase offering that uses provisioned compute you scale manually. For supported regions, see [Region availability](https://docs.databricks.com/aws/en/oltp/instances/#availability). For the latest version of Lakebase, with autoscaling compute, scale-to-zero, branching, and instant restore, see [Lakebase Autoscaling](https://docs.databricks.com/aws/en/oltp/projects/).

Since March 12, 2026, new Lakebase instances are created as Autoscaling projects. Existing Provisioned instances are being upgraded automatically to Autoscaling, starting in June 2026. For details, see [Upgrade to Lakebase Autoscaling](https://docs.databricks.com/aws/en/oltp/upgrade-to-autoscaling).

### Step 1: Create a database instance[​](#step-1-create-a-database-instance "Direct link to Step 1: Create a database instance")

To start, create a Lakebase database instance to store your synced tables. See [Create and manage a database instance](https://docs.databricks.com/aws/en/oltp/instances/create/).

Optionally, you can create a database catalog to use Unity Catalog privileges to manage data access. See [Register your database in Unity Catalog](https://docs.databricks.com/aws/en/oltp/instances/register-uc).

### Step 2: Create a synced table from the source table[​](#step-2-create-a-synced-table-from-the-source-table "Direct link to Step 2: Create a synced table from the source table")

A synced table is a Unity Catalog read-only Postgres table that automatically synchronizes data from a Unity Catalog table to your Lakebase database instance.

To migrate from online tables to synced tables, create a synced table from the source table of an online table:

1.  In ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**, select the online table you want to migrate to a synced table.
2.  In the **Overview** tab, under the **Description** section, click the name of the **Source table**.
3.  Create a synced table from the selected source table. See [Serve lakehouse data with synced tables (Lakebase Provisioned)](https://docs.databricks.com/aws/en/oltp/instances/sync-data/sync-table).
    *   You can store the synced table in the same catalog location as the existing online table.
    *   You can share a pipeline between synced tables.
4.  After your synced table is created, you can connect to the database instance and query it directly. See [Connect and query a database instance](https://docs.databricks.com/aws/en/oltp/instances/query/connect).

### Step 3: Clean up your online tables[​](#step-3-clean-up-your-online-tables "Direct link to Step 3: Clean up your online tables")

After you create your synced tables, delete your online tables. See [Delete an online table using the UI](#delete-an-online-table-using-the-ui) or [Delete an online table using APIs](#delete-an-online-table-using-apis).

## Delete an online table using the UI[​](#delete-an-online-table-using-the-ui "Direct link to Delete an online table using the UI")

From the online table page, select **Delete** from the ![Kebab menu icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTggMUM3LjAzMzUgMSA2LjI1IDEuNzgzNSA2LjI1IDIuNzVDNi4yNSAzLjcxNjUgNy4wMzM1IDQuNSA4IDQuNUM4Ljk2NjUgNC41IDkuNzUgMy43MTY1IDkuNzUgMi43NUM5Ljc1IDEuNzgzNSA4Ljk2NjUgMSA4IDFaIiBmaWxsPSIjNkY2RjZGIi8+CjxwYXRoIGQ9Ik04IDYuMjVDNy4wMzM1IDYuMjUgNi4yNSA3LjAzMzUgNi4yNSA4QzYuMjUgOC45NjY1IDcuMDMzNSA5Ljc1IDggOS43NUM4Ljk2NjUgOS43NSA5Ljc1IDguOTY2NSA5Ljc1IDhDOS43NSA3LjAzMzUgOC45NjY1IDYuMjUgOCA2LjI1WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBkPSJNOCAxMS41QzcuMDMzNSAxMS41IDYuMjUgMTIuMjgzNSA2LjI1IDEzLjI1QzYuMjUgMTQuMjE2NSA3LjAzMzUgMTUgOCAxNUM4Ljk2NjUgMTUgOS43NSAxNC4yMTY1IDkuNzUgMTMuMjVDOS43NSAxMi4yODM1IDguOTY2NSAxMS41IDggMTEuNVoiIGZpbGw9IiM2RjZGNkYiLz4KPC9zdmc+Cg==) kebab menu.

## Delete an online table using APIs[​](#delete-an-online-table-using-apis "Direct link to Delete an online table using APIs")

*   Databricks SDK - Python
*   REST API

Python

    w.online_tables.delete('main.default.my_online_table')

Deleting the online table stops any ongoing data synchronization and releases all its resources.
