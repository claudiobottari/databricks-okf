---
title: External lineage | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/external-lineage
ingestedAt: "2026-06-18T08:04:29.448Z"
---

Unity Catalog automatically captures runtime data lineage across queries that are run on Databricks. However, you might have workloads that run outside of Databricks (for example, first-mile ETL or last-mile BI). Unity Catalog lets you add external lineage metadata to augment the Databricks data lineage it captures automatically, giving you an end-to-end lineage view in Unity Catalog. This is useful when you want to capture where data came from (for example, Salesforce or MySQL) before it was ingested into Unity Catalog or where data is consumed outside of Unity Catalog (for example, Tableau or Power BI).

You can add external lineage in two ways:

*   Manually, using the Catalog Explorer UI, the External Metadata and External Lineage APIs, or the [Databricks SDK for Python](https://docs.databricks.com/aws/en/dev-tools/sdk-python).
*   Automatically, using [Lakeflow Connect](https://docs.databricks.com/aws/en/ingestion/lakeflow-connect/) managed ingestion pipelines, which record source lineage from your source tables to the destination tables in Unity Catalog. See [Track source data lineage for managed ingestion pipelines](https://docs.databricks.com/aws/en/ingestion/lakeflow-connect/source-lineage).

The following lineage graph shows two external tables in MySQL and PostgreSQL that were ingested into Databricks as a Unity Catalog managed table, with columns transformed into a `release_date` column, and then consumed by an external report.

![A lineage graph showing external upstream tables and a downstream report connected to a Unity Catalog table, with the Create external lineage button in the upper-right corner.](https://docs.databricks.com/aws/en/assets/images/lineage-external-metadata-f5483e379e1aba0a8c34699c63b4d07e.png)

For general information about data lineage in Databricks, see [Data lineage in Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-lineage).

## Requirements[​](#requirements "Direct link to requirements")

To add external lineage metadata in Unity Catalog, you must have the following privileges, depending on the specific task:

*   To create an external metadata securable object in Unity Catalog, you must have the `CREATE EXTERNAL METADATA` privilege on the metastore.
*   To specify lineage relationships between an external metadata object and any other Unity Catalog object, you must have the `MODIFY` privilege on the external metadata object.
*   To specify a downstream lineage relationship to a Unity Catalog object, you must have read privileges on the object (for example, `SELECT` on a table).
*   To specify an upstream lineage relationship to a Unity Catalog object, you must have write privileges on the object (for example, `MODIFY` on a table).

To add external lineage metadata:

1.  Create an external metadata securable object in Unity Catalog.
    
    This object represents an entity in an external system, such as a dashboard in Tableau.
    
2.  Configure a lineage relationship between the external metadata object and another Unity Catalog object, such as a table, model, path, or other external metadata object.
    
    When you have created lineage relationships, the external metadata object appears in the lineage graph view.
    

You can create external metadata objects and configure lineage relationships using the Catalog Explorer UI. To start from an existing lineage graph, click **Create external lineage** in the upper-right corner of the graph. You can also begin from the **External data** section in Catalog Explorer, as described in the following sections.

### Create an external metadata object[​](#create-an-external-metadata-object "Direct link to Create an external metadata object")

You can create an external metadata object using Catalog Explorer or the [External Metadata API](https://docs.databricks.com/api/workspace/externalmetadata).

To use Catalog Explorer to create an external metadata object:

1.  In your Databricks workspace, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
    
2.  Click the **External data >** button, go to the **External Metadata** tab, and click **Create external metadata**.
    
3.  Specify the metadata details.
    
    Required:
    
    *   **Name**: Enter a human-readable name that helps Databricks users understand what they are seeing in lineage. You cannot use spaces.
    *   **System type**: Select from the list of common external data and BI systems. If you don't find yours, select **Custom**.
    *   **Entity type**: Enter the type of object, such as "table" or "dashboard."
    
    Optional:
    
    *   **URL**: Enter the URL of the object if you want lineage graph viewers to be able to click through to the external asset (such as a Tableau dashboard, for example).
    *   **Description**
    
    Advanced:
    
    *   **Columns**: If you want to do column-level mapping from this external object to another Unity Catalog object, enter column names. Select **UI** to enter them one at a time or **Text Input** to enter a comma-delimited list in a single text box.
    *   **Properties**: If there are other properties that you want to track in lineage, enter them as a JSON key-value pairs. You can use the **UI** to enter each key-value pair, or enter a complete **JSON** object.
4.  Click **Create**.
    
    A dialog gives you the option to view the external metadata object or to create lineage relationships for the object.
    

### Create lineage relationships[​](#create-lineage-relationships "Direct link to Create lineage relationships")

You can create lineage relationships using Catalog Explorer, the [External Lineage API](https://docs.databricks.com/api/workspace/externallineage), or the [Databricks SDK for Python](https://docs.databricks.com/aws/en/dev-tools/sdk-python).

To add relationships between an external metadata object and other Unity Catalog objects:

1.  Follow the prompt mentioned above or find the existing external metadata object in Catalog Explorer:
    
    1.  Click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**
    2.  Click the **External data >** button
    3.  Go to the **External Metadata** tab and select the external metadata object.
2.  Click **Create lineage relationship**.
    
3.  Select whether you want to create an upstream or downstream relationship.
    
4.  Enter the **Object type** that you want to create the relationship to:
    
    *   **Table**: Select the table using the search dialog.
    *   **Model**: Select the model using the search dialog, and then select the model version.
    *   **Path**: For volumes or external locations, enter the path.
    *   **External metadata**: Select the external metadata object from the drop-down menu.
5.  (Optional) Click **Advanced** to add:
    
    *   Column mappings between the external metadata object and the source or target object.
    *   Other metadata as JSON key-value pairs. For example, you can use these to enter the text of the query that created a table from the external metadata object or annotations that explain the external workflow that generated the relationship.
6.  Click **Create**.
    

You can now see the external lineage relationship in the Lineage tab of the related objects.

## Model external lineage relationships[​](#model-external-lineage-relationships "Direct link to model-external-lineage-relationships")

When you add external lineage manually, use the following patterns to model more complex relationships:

*   **Connect two Unity Catalog tables**: To specify a lineage relationship between two tables that are both registered in Unity Catalog, create an external metadata object that sits between them. Specify one table as upstream to the external metadata object and the other as downstream so that they appear connected in the lineage graph.
*   **Add multiple levels of lineage**: To annotate data that passes through multiple systems before it enters Databricks, create multiple external metadata objects and configure external lineage relationships between each of them.
*   **Add column-level lineage**: Specify column names when you create the external metadata object, then map the source and target columns when you configure the lineage relationship.

## Limitations[​](#limitations "Direct link to limitations")

*   External lineage is not recorded in the lineage system tables (`system.access.table_lineage` and `system.access.column_lineage`).
*   You can create up to 10,000 external metadata objects and 100,000 external lineage relationships per metastore. See [Resource limits](https://docs.databricks.com/aws/en/resources/limits).

## Additional resources[​](#additional-resources "Direct link to additional-resources")

*   [Data lineage in Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-lineage)
*   [Track source data lineage for managed ingestion pipelines](https://docs.databricks.com/aws/en/ingestion/lakeflow-connect/source-lineage)
*   [External Metadata API](https://docs.databricks.com/api/workspace/externalmetadata)
*   [External Lineage API](https://docs.databricks.com/api/workspace/externallineage)
*   [Databricks SDK for Python](https://docs.databricks.com/aws/en/dev-tools/sdk-python)
