---
title: Data lineage in Unity Catalog | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-lineage
ingestedAt: "2026-06-18T08:04:05.337Z"
---

Data lineage shows where data in Databricks came from and where it goes: which queries and files populate a table, which jobs and notebooks transform it, and which dashboards consume the results.

Unity Catalog captures lineage automatically for queries run on Databricks, down to the column level, and aggregates it across all workspaces attached to the metastore. Lineage in Unity Catalog lets you:

*   **Perform impact analysis**: Before changing or deleting a table or column, identify the downstream tables, jobs, and dashboards that depend on it.
*   **Investigate root causes**: When a downstream report shows unexpected results, trace upstream sources to find where the data diverged.
*   **Track sensitive data flow**: For compliance audits, see where regulated data originates, how it is transformed, and which downstream assets consume it.
*   **Understand cross-team dependencies**: Discover which teams own the upstream sources you rely on, or which teams consume your tables.

External lineage extends the lineage graph beyond Databricks. Register upstream sources like Salesforce or MySQL and downstream tools like Tableau or Power BI as external assets in Unity Catalog, and they appear alongside your Unity Catalog tables in a single graph. See [External lineage](https://docs.databricks.com/aws/en/data-governance/unity-catalog/external-lineage).

The following image is a sample lineage graph. Nodes can represent tables and views, ML model versions, external assets, and file paths.

![Lineage overview.](https://docs.databricks.com/aws/en/assets/images/uc-lineage-overview-96ca9004e65531e65b9dfdb4f30473d6.png)

## Requirements[​](#requirements "Direct link to requirements")

To capture data lineage using Unity Catalog:

*   Tables must be registered in a Unity Catalog metastore.
*   External assets (those not registered in the Unity Catalog metastore) must be added as _external metadata_ objects in Unity Catalog, configured to have relationships with other securable objects registered in your Unity Catalog metastore. See [External lineage](https://docs.databricks.com/aws/en/data-governance/unity-catalog/external-lineage).
*   Queries must use the Spark DataFrame (for example, Spark SQL functions that return a DataFrame) or Databricks SQL interfaces such as notebooks or the SQL query editor.

To view data lineage:

*   You must have at least the `BROWSE` privilege on the parent catalog of the table or view. The parent catalog must also be accessible from the workspace. See [Workspace-catalog binding](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/workspace-catalog-binding).
*   For notebooks, jobs, or dashboards, you must have permissions on these objects as defined by the access control settings in the workspace. For details, see [Permissions](#permissions).
*   For a [Unity Catalog-enabled pipeline](https://docs.databricks.com/aws/en/ldp/unity-catalog), you must have CAN VIEW permission on the pipeline.

Compute requirements:

*   Lineage tracking of streaming between Delta tables requires Databricks Runtime 11.3 LTS or above.
*   Column lineage tracking for Lakeflow Spark Declarative Pipelines workloads requires Databricks Runtime 13.3 LTS or above.

Networking requirements:

*   You might need to update your outbound firewall rules to allow for connectivity to the Amazon Kinesis endpoint in the Databricks control plane. Typically this applies if your Databricks workspace is deployed in your own VPC or you use AWS PrivateLink within your Databricks network environment. To get the Kinesis endpoint for your workspace region, see [Kinesis addresses](https://docs.databricks.com/aws/en/resources/ip-domain-region#kinesis). See also [Configure a customer-managed VPC](https://docs.databricks.com/aws/en/security/network/classic/customer-managed-vpc) and [Configure classic private connectivity to Databricks](https://docs.databricks.com/aws/en/security/network/classic/privatelink).

## View lineage in Catalog Explorer[​](#view-lineage-in-catalog-explorer "Direct link to view-lineage-in-catalog-explorer")

To use Catalog Explorer to view table lineage:

1.  In your Databricks workspace, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
    
2.  Search or browse for your table.
    
3.  Select the **Lineage** tab. The lineage panel appears and displays related tables.
    
4.  To view an interactive graph of the data lineage, click **See Lineage Graph**.
    
    By default, one level is displayed in the graph. Click the ![Plus Sign Icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAASCAYAAABb0P4QAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAFKADAAQAAAABAAAAEgAAAAA9nQVdAAAC5ElEQVQ4EX1U204TURRdM20pvdAKFNraUm613ALEcIkG0Rd4xlfis3/gd/gF/oBvPpr4pFWJgkQq0WIqhFJooQIWWijTdnDvM+kwQ9GdnDlnzuy9Zp2199nSJRlusOPCKT5+WUcmdyDG9u4+/B1t6Ap0IBzoxEisF5FQAEpVhSRJcNptsFpkSNcBz87LiC+viZHLH6GmXuJSVaHSf2UKlGQJFkmGr92LuZkpTI0Owutx65RMgLu5PD6sfkP8cwLF0hmBqbrj9YUsy/C4nOjvCWFh7gF6wkHhItcdLy4UvF1OYCWxgZNi6b9gHKPSzwrk93NzB6/jKyhTPJsOuJZMYePXNg6PCzDKKpGT02HHYH833C6H0EtE0oP9SiRRaiuNBMWz6YCfvn5HLn+ISrUqPtQfLLi3xY3ZyTG0eT2QSUOjMdM/lMAlSiCbAKxUa9jayeK8fGH0FWsdcHocrd4WSozOQfdViMQPOh3jWHk3lc40MGPRm6xWYkSzTbiJubnJBgvtVWs1MeqozDS5ua0B7mV/o1YzZzQc7MSThXnSjDS0N4u4x/MPcTZbFiX0nhLI5VW3KsXHV5NXGtY/GGdWy6yY9n59j2O4RnsDbRrD20EfLFTlRstkD/D8xUtx5CjV2rOni3j15h2SKU0rPrLROFmRkF8DjEbCsJFeRmNNyooi9FIqWuZ5LiuVBr05jrWO9Ua0I9usFgz0R+ByOoyYYs21VjgtCb2OC0XSz6w1O9kpUXdHYkTKcqXh9NgQ/L7WBqYaYBGchKPCCd0Qcy9hZrfoLt8bHxYEdOGGoz2I9UXQ3uo13wZy44bBdcb323SLKBEuRzPd5y4MRLvNgHZ7Ex5NjWNyNAav20mtyCIc/vVgZi3UHPq6Q5ifmQDHs5m6DW8wm6XVdeo660jv5m5uXwTmo5PcnxjDwJ0+uJ0utHsccFBPbABkULZ6g93J7SOTzSO9t49On9Zgo8RqiI4Y9Hc0NNi/Z5hC2gxppcUAAAAASUVORK5CYII=) icon on a node to reveal more connections if they are available.
    
5.  Click the icon on a connecting edge in the lineage graph to open the **Lineage details** panel.
    
    The **Lineage details** panel shows details about the connection, including source and target tables.
    
    ![Lineage graph.](https://docs.databricks.com/aws/en/assets/images/uc-lineage-details-598f25ffcce29065c3f5e9117f01e62d.png)
    
6.  To view an asset associated with a table, select the asset in the **Lineage details** panel. You can filter by notebooks, jobs, pipelines, and queries.
    
7.  To view column-level lineage, click a column in the graph to show links to related columns. For example, clicking on the `revenue` column in this sample graph shows the upstream columns from which the column was derived:
    
    ![Full menu column lineage.](https://docs.databricks.com/aws/en/assets/images/uc-column-lineage-c8dfa626d400501fd428b1606ad74e7c.png)
    

### View job lineage[​](#view-job-lineage "Direct link to View job lineage")

To view job lineage, go to a table's **Lineage** tab, select **Jobs**, and select **Downstream**. The job name appears under **Job Name** as a consumer of the table.

### View dashboard lineage[​](#view-dashboard-lineage "Direct link to View dashboard lineage")

To view dashboard lineage, go to a table's **Lineage** tab and click **Dashboards**. The dashboard appears under **Dashboard Name** as a consumer of the table.

## Get lineage using Genie Code[​](#get-lineage-using-genie-code "Direct link to get-lineage-using-genie-code")

Genie Code can answer lineage questions in natural language.

To get lineage information using Genie Code:

1.  In the workspace sidebar, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
2.  Browse or search for the catalog, click the catalog name, and then click the ![Genie code color icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xMC43MjU4IDguODEzMzFMMTMuMTk4NyA4LjAwMDAyTDEwLjcyNTggNy4xODY3NEM5LjgyMDc4IDYuODg5MDggOS4xMTA5MiA2LjE3OTIyIDguODEzMjYgNS4yNzQxNkw3Ljk5OTk4IDIuODAxMjdMNy4xODY2OSA1LjI3NDE2QzYuODg5MDMgNi4xNzkyMiA2LjE3OTE3IDYuODg5MDggNS4yNzQxMSA3LjE4Njc0TDIuODAxMjIgOC4wMDAwMkw1LjI3NDExIDguODEzMzFDNi4xNzkxNyA5LjExMDk3IDYuODg5MDMgOS44MjA4MyA3LjE4NjY5IDEwLjcyNTlMNy45OTk5OCAxMy4xOTg4TDguODEzMjYgMTAuNzI1OUM5LjExMDkyIDkuODIwODMgOS44MjA3OCA5LjExMDk3IDEwLjcyNTggOC44MTMzMVpNMTMuNjY3NCA5LjQyNDk0QzE1LjA0MjUgOC45NzI2NyAxNS4wNDI1IDcuMDI3MzcgMTMuNjY3NCA2LjU3NTExTDExLjE5NDUgNS43NjE4MkMxMC43NDE5IDUuNjEyOTkgMTAuMzg3IDUuMjU4MDYgMTAuMjM4MiA0LjgwNTUzTDkuNDI0ODkgMi4zMzI2NEM4Ljk3MjYzIDAuOTU3NDc5IDcuMDI3MzIgMC45NTc0NzkgNi41NzUwNiAyLjMzMjY0TDUuNzYxNzcgNC44MDU1M0M1LjYxMjk0IDUuMjU4MDYgNS4yNTgwMSA1LjYxMjk5IDQuODA1NDggNS43NjE4MkwyLjMzMjU5IDYuNTc1MTFDMC45NTc0MzIgNy4wMjczNyAwLjk1NzQzNCA4Ljk3MjY4IDIuMzMyNiA5LjQyNDk0TDQuODA1NDggMTAuMjM4MkM1LjI1ODAxIDEwLjM4NzEgNS42MTI5NCAxMC43NDIgNS43NjE3NyAxMS4xOTQ1TDYuNTc1MDYgMTMuNjY3NEM3LjAyNzMzIDE1LjA0MjYgOC45NzI2MyAxNS4wNDI2IDkuNDI0ODkgMTMuNjY3NEwxMC4yMzgyIDExLjE5NDVDMTAuMzg3IDEwLjc0MiAxMC43NDE5IDEwLjM4NzEgMTEuMTk0NSAxMC4yMzgyTDEzLjY2NzQgOS40MjQ5NFoiIGZpbGw9InVybCgjcGFpbnQwX2xpbmVhcl84MDU4XzY0NikiLz4KPGRlZnM+CjxsaW5lYXJHcmFkaWVudCBpZD0icGFpbnQwX2xpbmVhcl84MDU4XzY0NiIgeDE9IjE1LjMwNDgiIHkxPSIwLjMyMjk5MyIgeDI9IjAuMjQ4NTYyIiB5Mj0iMTUuMzc5MiIgZ3JhZGllbnRVbml0cz0idXNlclNwYWNlT25Vc2UiPgo8c3RvcCBvZmZzZXQ9IjAuMjM1IiBzdG9wLWNvbG9yPSIjNDI5OUUwIi8+CjxzdG9wIG9mZnNldD0iMC40NyIgc3RvcC1jb2xvcj0iI0NBNDJFMCIvPgo8c3RvcCBvZmZzZXQ9IjAuNzYiIHN0b3AtY29sb3I9IiNGRjVGNDYiLz4KPC9saW5lYXJHcmFkaWVudD4KPC9kZWZzPgo8L3N2Zz4K) Genie Code icon in the upper-right corner.
3.  At the Genie Code prompt, type:
    *   `/getTableLineages` to view upstream and downstream dependencies.
    *   `/getTableInsights` to access metadata-driven insights, such as user activity and query patterns.

These queries enable Genie Code to answer questions like "show me downstream lineages" or "who queries this table most often."

![Genie Code provides table lineage and insights.](https://docs.databricks.com/aws/en/assets/images/ai-assistant-data-lineage-59805c2d5fc60d4324eec18d19c99d82.png)

## Query lineage with system tables[​](#query-lineage-with-system-tables "Direct link to query-lineage-with-system-tables")

You can use the lineage system tables to programmatically query lineage data. For detailed instructions, see [System tables reference](https://docs.databricks.com/aws/en/admin/system-tables/) and [Lineage system tables reference](https://docs.databricks.com/aws/en/admin/system-tables/lineage).

## Permissions[​](#permissions "Direct link to permissions")

Lineage graphs share the same [permission model](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/permissions-concepts) as Unity Catalog. Tables and other data objects registered in the Unity Catalog metastore are visible only to users who have at least `BROWSE` permissions on those objects. If a user does not have the `BROWSE` or `SELECT` privilege on a table, they cannot explore its lineage.

Lineage is aggregated across all workspaces attached to a Unity Catalog metastore, so lineage captured in one workspace is visible in any other workspace that shares that metastore, as long as the user has adequate object permissions. Detailed information about workspace-level objects like notebooks and dashboards in other workspaces is masked. See [Limitations](#limitations).

For example, run the following commands for `userA`:

SQL

    GRANT USE SCHEMA on lineage_data.lineagedemo to `userA@company.com`;GRANT SELECT on lineage_data.lineagedemo.menu to `userA@company.com`;

When `userA` views the lineage graph for the `lineage_data.lineagedemo.menu` table, they see the `menu` table. They cannot see information about associated tables, such as the downstream `lineage_data.lineagedemo.dinner` table. The `dinner` table appears as a `masked` node to `userA`, and `userA` cannot expand the graph to reveal downstream tables from tables they do not have permission to access.

If you run the following command to grant the `BROWSE` permission to `userB`, that user can view the lineage graph for any table in the `lineage_data` schema:

SQL

    GRANT BROWSE on lineage_data to `userB@company.com`;

Lineage users must also have specific permissions to view workspace objects like notebooks, jobs, and dashboards. Detailed information about these objects is visible only in the workspace where they were created.

For more information about managing access to securable objects in Unity Catalog, see [Manage privileges in Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/). For more information about managing access to workspace objects like notebooks, jobs, and dashboards, see [Access control lists](https://docs.databricks.com/aws/en/security/auth/access-control/).

## Retention[​](#retention "Direct link to retention")

Lineage data displayed in Catalog Explorer is retained indefinitely. All lineage data captured after September 1, 2024 is available. For metastores created after that date, Catalog Explorer includes an **All time** option in the lineage time-range dropdown. For older metastores, the dropdown includes an **All available** option that starts from September 1, 2024. The default selection is **1 year**.

Lineage system tables (`system.access.table_lineage` and `system.access.column_lineage`) retain a rolling 1-year window of data. See [Lineage system tables reference](https://docs.databricks.com/aws/en/admin/system-tables/lineage).

## Limitations[​](#limitations "Direct link to limitations")

Data lineage has the following limitations. These limitations also apply to lineage system tables:

*   Lineage data captured before September 1, 2024 is not available.
*   Jobs that use the Jobs API `runs submit` request or the `spark submit` task type are unavailable in lineage views. Table and column level lineage is still captured for these workflows, but the link to the job run is not captured.
*   Lineage is not preserved for renamed catalogs, schemas, tables, views, or columns.
*   If you use Spark SQL dataset checkpointing, lineage is not captured.
*   Unity Catalog captures lineage from Lakeflow Spark Declarative Pipelines in most cases, but coverage is incomplete for pipelines that use [PRIVATE tables](https://docs.databricks.com/aws/en/ldp/developer/sql-dev#temporary-table).
*   Resilient Distributed Datasets (RDDs) are not captured in lineage.
*   Global temp views are not captured in lineage.
*   [Transactions](https://docs.databricks.com/aws/en/transactions/) emit lineage as each read and write occurs. Lineage events persist even if the transaction is rolled back.
*   Tables under `system.information_schema` are not captured in lineage.
*   Unity Catalog captures lineage to the column level as much as possible. However, there are some cases where column-level lineage cannot be captured. These include:
    *   Column lineage cannot be captured if the source or the target is referenced as path (Example: `select * from delta."s3://<bucket>/<path>"`). Column lineage is supported only when both the source and target are referenced by table name (Example: `select * from <catalog>.<schema>.<table>`).
        
    *   Use of user-defined functions (UDFs), which can obscure the mapping between source and target columns.
        

## Additional resources[​](#additional-resources "Direct link to additional-resources")

*   **Demo**: [Unity Catalog - Data Lineage](https://app.getreprise.com/launch/MnqjQDX/)
*   **ML model lineage**: To track lineage for a machine learning model, see [Track the data lineage of a model in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/#model-lineage).
*   **Table insights**: The **Insights** tab in Catalog Explorer shows usage trends for a table: query patterns, top users, and dashboards that read it. See [View table insights and popularity](https://docs.databricks.com/aws/en/discover/table-insights).
