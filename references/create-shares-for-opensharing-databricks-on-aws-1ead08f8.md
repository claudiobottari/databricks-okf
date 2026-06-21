---
title: Create shares for OpenSharing | Databricks on AWS
source: https://docs.databricks.com/aws/en/delta-sharing/create-share
ingestedAt: "2026-06-18T08:05:22.142Z"
truncated: true
originalChars: 179689
---

This page explains how to create shares for OpenSharing.

A share is a securable object in Unity Catalog that you use for sharing the following data assets with one or more recipients:

*   [Tables and table partitions](#add-tables)
*   [Streaming tables](#streaming-tables)
*   [Managed Iceberg tables](#managed-iceberg)
*   [Foreign Iceberg tables](#foreign-iceberg)
*   [Foreign schemas and tables](#foreign-asset)
*   [Views](#views), including [dynamic views](#dynamic-views) that restrict access at the row and column level
*   [Materialized views](#materialized-views)
*   [Volumes](#volumes)
*   [Python UDFs](#python-udfs)
*   [Notebooks](#add-remove-notebook-files)
*   [AI models](#models)
*   [Genie Spaces](https://docs.databricks.com/aws/en/delta-sharing/share-genie-space)

*   [`FeatureSpecs`](#featurespec)

If you share an entire schema (database), the recipient can access all of the tables, streaming tables, views, materialized views, models, and volumes in the schema at the moment you share it, along with any data and AI assets added to the schema in the future.

A share can contain data and AI assets from only one Unity Catalog metastore. You can add or remove data and AI assets from a share at any time.

Before creating a share, verify that you have [Set up OpenSharing for your account (for providers)](https://docs.databricks.com/aws/en/delta-sharing/set-up).

To learn more about the sharing model, see [Shares, providers, and recipients](https://docs.databricks.com/aws/en/delta-sharing/#shares-recipients).

## Requirements[​](#requirements "Direct link to Requirements")

Check that you meet the listed requirements for each task you want to complete.

tip

When adding data assets to a share, Databricks recommends that you use a group as the share owner.

### Compute requirements[​](#compute-requirements "Direct link to Compute requirements")

*   If you use a Databricks notebook to create the share, your compute resource must use Databricks Runtime 11.3 LTS or above and have a standard or dedicated access mode (formerly shared and single user).
*   If you use SQL statements to add a schema to a share (or update or remove a schema), you must use a SQL warehouse or compute running Databricks Runtime 13.3 LTS or above. Doing the same using Catalog Explorer has no compute requirements.

Check that you meet the [requirements](https://docs.databricks.com/aws/en/delta-sharing/create-share#requirements) before creating a share object.

To create a share, use Catalog Explorer, the Databricks Unity Catalog CLI, or the `CREATE SHARE` SQL command in a Databricks notebook or the Databricks SQL query editor.

*   Catalog Explorer
*   SQL
*   CLI

1.  In your Databricks workspace, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
    
2.  At the top of the **Catalog** pane, click the ![Gear icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzEzMTIzXzM1MDE5KSI+CjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNNy45ODQzMyA1QzYuMzI3NDcgNSA0Ljk4NDMzIDYuMzQzMTUgNC45ODQzMyA4QzQuOTg0MzMgOS42NTY4NSA2LjMyNzQ3IDExIDcuOTg0MzMgMTFDOS42NDExOCAxMSAxMC45ODQzIDkuNjU2ODUgMTAuOTg0MyA4QzEwLjk4NDMgNi4zNDMxNSA5LjY0MTE4IDUgNy45ODQzMyA1Wk02LjQ4NDMzIDhDNi40ODQzMyA3LjE3MTU3IDcuMTU1OSA2LjUgNy45ODQzMyA2LjVDOC44MTI3NSA2LjUgOS40ODQzMyA3LjE3MTU3IDkuNDg0MzMgOEM5LjQ4NDMzIDguODI4NDMgOC44MTI3NSA5LjUgNy45ODQzMyA5LjVDNy4xNTU5IDkuNSA2LjQ4NDMzIDguODI4NDMgNi40ODQzMyA4WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTcuOTY1NSAwQzcuNjI1NTIgMCA3LjI5MDE0IDAuMDIxMjUxMSA2Ljk2MDcgMC4wNjI1NzM2QzYuNjczMDQgMC4wOTg2NTU4IDYuNDMxOTQgMC4yOTczIDYuMzQxNDggMC41NzI3NDVMNS43MDI0IDIuNTE4ODhDNS40OTI0NCAyLjYwNTY1IDUuMjg4NiAyLjcwNDExIDUuMDkxNyAyLjgxMzQxTDMuMTcxOTggMi4wOTk3OUMyLjkwMDU0IDEuOTk4ODggMi41OTUyNiAyLjA2MzI2IDIuMzg3NjkgMi4yNjUxOUMxLjkwNjkgMi43MzI4OSAxLjQ4NDY0IDMuMjYwNjggMS4xMzMwMSAzLjgzNjYxQzAuOTgxOTgyIDQuMDgzOTkgMC45ODcwMDYgNC4zOTYyNSAxLjE0NTkyIDQuNjM4NjRMMi4yNjkxOSA2LjM1MTk4QzIuMjA2OTIgNi41Njc1NyAyLjE1NjU2IDYuNzg4MTQgMi4xMTg4NSA3LjAxMjkzTDAuMzYzMzIyIDguMDY5MjhDMC4xMTU0ODMgOC4yMTg0MiAtMC4wMjQ1MDg2IDguNDk2NzggMC4wMDM1NDkyOSA4Ljc4NDY2QzAuMDcwMDUzNiA5LjQ2NzAyIDAuMjIyMzY1IDEwLjEyNDggMC40NDk2NjkgMTAuNzQ2NkMwLjU0OTA4NSAxMS4wMTg2IDAuNzk2MTg5IDExLjIwOSAxLjA4NDUxIDExLjIzNTlMMy4xMjY2NyAxMS40MjYxQzMuMjU3MzUgMTEuNjEwNCAzLjM5ODI2IDExLjc4NjggMy41NDg1OCAxMS45NTQ2TDMuMjc5NzQgMTMuOTg3MkMzLjI0MTggMTQuMjc0IDMuMzcyMjIgMTQuNTU3MSAzLjYxNDkgMTQuNzE0NkM0LjE3NDI3IDE1LjA3NzcgNC43ODIxNiAxNS4zNzMgNS40MjY4NiAxNS41ODg2QzUuNzAxNDcgMTUuNjgwNCA2LjAwNDQyIDE1LjYwNiA2LjIwNTE4IDE1LjM5NzNMNy42Mjc0MyAxMy45MTlDNy43MzkzOSAxMy45MjU0IDcuODUyMTEgMTMuOTI4NSA3Ljk2NTUxIDEzLjkyODVDOC4wNzg4OSAxMy45Mjg1IDguMTkxNiAxMy45MjU0IDguMzAzNTQgMTMuOTE5TDkuNzI1OCAxNS4zOTczQzkuOTI2NTYgMTUuNjA2IDEwLjIyOTUgMTUuNjgwNCAxMC41MDQxIDE1LjU4ODZDMTEuMTQ4OCAxNS4zNzMgMTEuNzU2NyAxNS4wNzc3IDEyLjMxNjEgMTQuNzE0NkMxMi41NTg4IDE0LjU1NzEgMTIuNjg5MiAxNC4yNzQgMTIuNjUxMiAxMy45ODcyTDEyLjM4MjQgMTEuOTU0N0MxMi41MzI3IDExLjc4NjkgMTIuNjczNyAxMS42MTA0IDEyLjgwNDMgMTEuNDI2MUwxNC44NDY1IDExLjIzNTlDMTUuMTM0OCAxMS4yMDkgMTUuMzgxOSAxMS4wMTg2IDE1LjQ4MTMgMTAuNzQ2NkMxNS43MDg2IDEwLjEyNDggMTUuODYwOSA5LjQ2NzA0IDE1LjkyNzUgOC43ODQ2OUMxNS45NTU1IDguNDk2OCAxNS44MTU1IDguMjE4NDQgMTUuNTY3NyA4LjA2OTNMMTMuODEyMiA3LjAxMjk2QzEzLjc3NDUgNi43ODgxNSAxMy43MjQxIDYuNTY3NTQgMTMuNjYxOCA2LjM1MTkzTDE0Ljc4NTEgNC42Mzg2MUMxNC45NDQgNC4zOTYyMiAxNC45NDkgNC4wODM5NiAxNC43OTggMy44MzY1OEMxNC40NDYzIDMuMjYwNjUgMTQuMDI0MSAyLjczMjg3IDEzLjU0MzMgMi4yNjUxOEMxMy4zMzU3IDIuMDYzMjUgMTMuMDMwNSAxLjk5ODg3IDEyLjc1OSAyLjA5OTc4TDEwLjgzOTMgMi44MTM0QzEwLjY0MjQgMi43MDQwOSAxMC40Mzg1IDIuNjA1NjMgMTAuMjI4NiAyLjUxODg1TDkuNTg5NDkgMC41NzI3NDFDOS40OTkwMyAwLjI5NzI5NCA5LjI1NzkzIDAuMDk4NjQ5NiA4Ljk3MDI2IDAuMDYyNTY4NkM4LjY0MDgzIDAuMDIxMjQ5NCA4LjMwNTQ4IDAgNy45NjU1IDBaTTcuMDE1NDggMy4zMjgwNUw3LjYxMjcxIDEuNTA5MzlDNy43Mjk0NiAxLjUwMzE2IDcuODQ3MDggMS41IDcuOTY1NSAxLjVDOC4wODM5MSAxLjUgOC4yMDE1MyAxLjUwMzE2IDguMzE4MjYgMS41MDkzOUw4LjkxNTQ4IDMuMzI4MDRDOC45ODkxIDMuNTUyMjEgOS4xNjM5MiAzLjcyODY4IDkuMzg3NCAzLjgwNDM4QzkuNzMxNjEgMy45MjA5OSAxMC4wNTcxIDQuMDc4OTIgMTAuMzU3OCA0LjI3MjQyQzEwLjU1NjQgNC40MDAxOSAxMC44MDM2IDQuNDI2OTYgMTEuMDI1IDQuMzQ0NjhMMTIuODIgMy42Nzc0QzEyLjk3NjQgMy44NTI5IDEzLjEyMzQgNC4wMzY5MSAxMy4yNjAyIDQuMjI4NjNMMTIuMjEwNSA1LjgyOTgyQzEyLjA4MTEgNi4wMjcxMyAxMi4wNTIyIDYuMjczODIgMTIuMTMyMyA2LjQ5NTc0QzEyLjI1MjUgNi44Mjg3OCAxMi4zMzQgNy4xODA1OCAxMi4zNzEyIDcuNTQ1OTdDMTIuMzk1IDcuNzgwOTcgMTIuNTI4MiA3Ljk5MDk5IDEyLjczMDYgOC4xMTI3N0wxNC4zNzI4IDkuMTAwOTJDMTQuMzMzIDkuMzM0NTIgMTQuMjgwNyA5LjU2Mzc5IDE0LjIxNjcgOS43ODgwNkwxMi4zMDggOS45NjU4N0MxMi4wNzM0IDkuOTg3NzMgMTEuODYyNyAxMC4xMTg2IDExLjczOTEgMTAuMzE5MkMxMS41NDk2IDEwLjYyNjggMTEuMzIzNCAxMC45MDk2IDExLjA2NjYgMTEuMTYxNkMxMC44OTgyIDExLjMyNjcgMTAuODE3MyAxMS41NjE1IDEwLjg0ODMgMTEuNzk1M0wxMS4wOTk3IDEzLjY5NkMxMC44OTQ2IDEzLjgwOTEgMTAuNjgyOCAxMy45MTE0IDEwLjQ2NTEgMTQuMDAyMkw5LjEzNTg0IDEyLjYyMDZDOC45NzI1MiAxMi40NTA5IDguNzM4OTQgMTIuMzY3NyA4LjUwNTA5IDEyLjM5NjFDOC4zMjg1MiAxMi40MTc1IDguMTQ4NDcgMTIuNDI4NSA3Ljk2NTUxIDEyLjQyODVDNy43ODI1MyAxMi40Mjg1IDcuNjAyNDcgMTIuNDE3NSA3LjQyNTg5IDEyLjM5NjFDNy4xOTIwNCAxMi4zNjc3IDYuOTU4NDYgMTIuNDUwOSA2Ljc5NTE0IDEyLjYyMDZMNS40NjU4OSAxNC4wMDIyQzUuMjQ4MTYgMTMuOTExNCA1LjAzNjM4IDEzLjgwOTEgNC44MzEzMSAxMy42OTZMNS4wODI3MiAxMS43OTUzQzUuMTEzNjUgMTEuNTYxNSA1LjAzMjc4IDExLjMyNjcgNC44NjQ0MiAxMS4xNjE1QzQuNjA3NjEgMTAuOTA5NiA0LjM4MTQ0IDEwLjYyNjggNC4xOTE5NSAxMC4zMTkyQzQuMDY4MzMgMTAuMTE4NiAzLjg1NzYyIDkuOTg3NzMgMy42MjI5OSA5Ljk2NTg3TDEuNzE0MzMgOS43ODgwNkMxLjY1MDMyIDkuNTYzNzkgMS41OTgwNCA5LjMzNDUxIDEuNTU4MjIgOS4xMDA5TDMuMjAwNCA4LjExMjc1QzMuNDAyNzkgNy45OTA5NiAzLjUzNTk5IDcuNzgwOTUgMy41NTk4NyA3LjU0NTk1QzMuNTk3IDcuMTgwNTggMy42Nzg0NyA2LjgyODggMy43OTg3MiA2LjQ5NTc4QzMuODc4ODQgNi4yNzM4NiAzLjg0OTg4IDYuMDI3MTggMy43MjA1MSA1LjgyOTg2TDIuNjcwNzYgNC4yMjg2NUMyLjgwNzU5IDQuMDM2OTMgMi45NTQ2IDMuODUyOTIgMy4xMTEgMy42Nzc0MUw0LjkwNjA1IDQuMzQ0NjlDNS4xMjc0IDQuNDI2OTcgNS4zNzQ1NyA0LjQwMDIgNS41NzMxNyA0LjI3MjQzQzUuODczOTQgNC4wNzg5MyA2LjE5OTM3IDMuOTIxMDEgNi41NDM1NyAzLjgwNDRDNi43NjcwNSAzLjcyODY5IDYuOTQxODcgMy41NTIyMyA3LjAxNTQ4IDMuMzI4MDVaIiBmaWxsPSIjNkY2RjZGIi8+CjwvZz4KPGRlZnM+CjxjbGlwUGF0aCBpZD0iY2xpcDBfMTMxMjNfMzUwMTkiPgo8cmVjdCB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9IndoaXRlIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==) gear icon and select **OpenSharing**.
    
    Alternatively, in the upper-right corner, click **Share > OpenSharing**.
    
3.  On the **Shared by me** tab, click the **Share data** button.
    
4.  On the **Create share** page, enter the share **Name** and an optional comment.
    
5.  Click **Save and continue**.
    
    You can continue to add data assets, or you can stop and come back later.
    
6.  On the **Add data assets** tab, select the data assets you want to share.
    
    For detailed instructions, additional requirements, and related limitations, see:
    
    *   [Add tables to a share](#add-tables)
    *   [Add streaming tables to a share](#streaming-tables)
    *   [Add managed Iceberg tables to a share](#managed-iceberg)
    *   [Add foreign schemas or tables to a share](#foreign-asset)
    *   [Add volumes to a share](#volumes)
    *   [Add views to a share](#views)
    *   [Add materialized views to a share](#materialized-views)
    *   [Add models to a share](#models)
7.  Click **Save and continue**.
    
8.  On the **Add notebooks** tab, select the notebooks you want to share.
    
    For detailed instructions, see [Add notebook files to a share](#add-remove-notebook-files).
    
9.  Click **Save and continue**.
    
10.  On the **Add recipients** tab, select the recipients you want to share with.
     
     For detailed instructions, see [Manage access to OpenSharing data shares (for providers)](https://docs.databricks.com/aws/en/delta-sharing/grant-access).
     
11.  Click **Share data** to share the data with the recipients.
     
     If you have not created recipients yet, click **Share data**, create recipients, and grant them access later.
     

Check that you meet the [requirements](https://docs.databricks.com/aws/en/delta-sharing/create-share#requirements) before adding tables to a share.

If you are a workspace admin and you inherited the `USE SCHEMA` and `USE CATALOG` permissions on the schema and catalog that contain the table from the workspace admin group, then you cannot add the table to a share. You must first grant yourself the `USE SCHEMA` and `USE CATALOG` permissions on the schema and catalog.

note

Table comments, column comments, and [primary key constraints](https://docs.databricks.com/aws/en/tables/constraints) are included in shares that are shared with a recipient using Databricks-to-Databricks sharing on or after July 25, 2024. If you want to start sharing comments and constraints through a share that was shared with a recipient before the release date, you must revoke and re-grant recipient access to trigger comment and constraint sharing.

To add tables to a share, use Catalog Explorer, the Databricks Unity Catalog CLI, or SQL commands in a Databricks notebook or the Databricks SQL query editor.

*   Catalog Explorer
*   SQL
*   CLI

1.  In your Databricks workspace, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
    
2.  At the top of the **Catalog** pane, click the ![Gear icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzEzMTIzXzM1MDE5KSI+CjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNNy45ODQzMyA1QzYuMzI3NDcgNSA0Ljk4NDMzIDYuMzQzMTUgNC45ODQzMyA4QzQuOTg0MzMgOS42NTY4NSA2LjMyNzQ3IDExIDcuOTg0MzMgMTFDOS42NDExOCAxMSAxMC45ODQzIDkuNjU2ODUgMTAuOTg0MyA4QzEwLjk4NDMgNi4zNDMxNSA5LjY0MTE4IDUgNy45ODQzMyA1Wk02LjQ4NDMzIDhDNi40ODQzMyA3LjE3MTU3IDcuMTU1OSA2LjUgNy45ODQzMyA2LjVDOC44MTI3NSA2LjUgOS40ODQzMyA3LjE3MTU3IDkuNDg0MzMgOEM5LjQ4NDMzIDguODI4NDMgOC44MTI3NSA5LjUgNy45ODQzMyA5LjVDNy4xNTU5IDkuNSA2LjQ4NDMzIDguODI4NDMgNi40ODQzMyA4WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTcuOTY1NSAwQzcuNjI1NTIgMCA3LjI5MDE0IDAuMDIxMjUxMSA2Ljk2MDcgMC4wNjI1NzM2QzYuNjczMDQgMC4wOTg2NTU4IDYuNDMxOTQgMC4yOTczIDYuMzQxNDggMC41NzI3NDVMNS43MDI0IDIuNTE4ODhDNS40OTI0NCAyLjYwNTY1IDUuMjg4NiAyLjcwNDExIDUuMDkxNyAyLjgxMzQxTDMuMTcxOTggMi4wOTk3OUMyLjkwMDU0IDEuOTk4ODggMi41OTUyNiAyLjA2MzI2IDIuMzg3NjkgMi4yNjUxOUMxLjkwNjkgMi43MzI4OSAxLjQ4NDY0IDMuMjYwNjggMS4xMzMwMSAzLjgzNjYxQzAuOTgxOTgyIDQuMDgzOTkgMC45ODcwMDYgNC4zOTYyNSAxLjE0NTkyIDQuNjM4NjRMMi4yNjkxOSA2LjM1MTk4QzIuMjA2OTIgNi41Njc1NyAyLjE1NjU2IDYuNzg4MTQgMi4xMTg4NSA3LjAxMjkzTDAuMzYzMzIyIDguMDY5MjhDMC4xMTU0ODMgOC4yMTg0MiAtMC4wMjQ1MDg2IDguNDk2NzggMC4wMDM1NDkyOSA4Ljc4NDY2QzAuMDcwMDUzNiA5LjQ2NzAyIDAuMjIyMzY1IDEwLjEyNDggMC40NDk2NjkgMTAuNzQ2NkMwLjU0OTA4NSAxMS4wMTg2IDAuNzk2MTg5IDExLjIwOSAxLjA4NDUxIDExLjIzNTlMMy4xMjY2NyAxMS40MjYxQzMuMjU3MzUgMTEuNjEwNCAzLjM5ODI2IDExLjc4NjggMy41NDg1OCAxMS45NTQ2TDMuMjc5NzQgMTMuOTg3MkMzLjI0MTggMTQuMjc0IDMuMzcyMjIgMTQuNTU3MSAzLjYxNDkgMTQuNzE0NkM0LjE3NDI3IDE1LjA3NzcgNC43ODIxNiAxNS4zNzMgNS40MjY4NiAxNS41ODg2QzUuNzAxNDcgMTUuNjgwNCA2LjAwNDQyIDE1LjYwNiA2LjIwNTE4IDE1LjM5NzNMNy42Mjc0MyAxMy45MTlDNy43MzkzOSAxMy45MjU0IDcuODUyMTEgMTMuOTI4NSA3Ljk2NTUxIDEzLjkyODVDOC4wNzg4OSAxMy45Mjg1IDguMTkxNiAxMy45MjU0IDguMzAzNTQgMTMuOTE5TDkuNzI1OCAxNS4zOTczQzkuOTI2NTYgMTUuNjA2IDEwLjIyOTUgMTUuNjgwNCAxMC41MDQxIDE1LjU4ODZDMTEuMTQ4OCAxNS4zNzMgMTEuNzU2NyAxNS4wNzc3IDEyLjMxNjEgMTQuNzE0NkMxMi41NTg4IDE0LjU1NzEgMTIuNjg5MiAxNC4yNzQgMTIuNjUxMiAxMy45ODcyTDEyLjM4MjQgMTEuOTU0N0MxMi41MzI3IDExLjc4NjkgMTIuNjczNyAxMS42MTA0IDEyLjgwNDMgMTEuNDI2MUwxNC44NDY1IDExLjIzNTlDMTUuMTM0OCAxMS4yMDkgMTUuMzgxOSAxMS4wMTg2IDE1LjQ4MTMgMTAuNzQ2NkMxNS43MDg2IDEwLjEyNDggMTUuODYwOSA5LjQ2NzA0IDE1LjkyNzUgOC43ODQ2OUMxNS45NTU1IDguNDk2OCAxNS44MTU1IDguMjE4NDQgMTUuNTY3NyA4LjA2OTNMMTMuODEyMiA3LjAxMjk2QzEzLjc3NDUgNi43ODgxNSAxMy43MjQxIDYuNTY3NTQgMTMuNjYxOCA2LjM1MTkzTDE0Ljc4NTEgNC42Mzg2MUMxNC45NDQgNC4zOTYyMiAxNC45NDkgNC4wODM5NiAxNC43OTggMy44MzY1OEMxNC40NDYzIDMuMjYwNjUgMTQuMDI0MSAyLjczMjg3IDEzLjU0MzMgMi4yNjUxOEMxMy4zMzU3IDIuMDYzMjUgMTMuMDMwNSAxLjk5ODg3IDEyLjc1OSAyLjA5OTc4TDEwLjgzOTMgMi44MTM0QzEwLjY0MjQgMi43MDQwOSAxMC40Mzg1IDIuNjA1NjMgMTAuMjI4NiAyLjUxODg1TDkuNTg5NDkgMC41NzI3NDFDOS40OTkwMyAwLjI5NzI5NCA5LjI1NzkzIDAuMDk4NjQ5NiA4Ljk3MDI2IDAuMDYyNTY4NkM4LjY0MDgzIDAuMDIxMjQ5NCA4LjMwNTQ4IDAgNy45NjU1IDBaTTcuMDE1NDggMy4zMjgwNUw3LjYxMjcxIDEuNTA5MzlDNy43Mjk0NiAxLjUwMzE2IDcuODQ3MDggMS41IDcuOTY1NSAxLjVDOC4wODM5MSAxLjUgOC4yMDE1MyAxLjUwMzE2IDguMzE4MjYgMS41MDkzOUw4LjkxNTQ4IDMuMzI4MDRDOC45ODkxIDMuNTUyMjEgOS4xNjM5MiAzLjcyODY4IDkuMzg3NCAzLjgwNDM4QzkuNzMxNjEgMy45MjA5OSAxMC4wNTcxIDQuMDc4OTIgMTAuMzU3OCA0LjI3MjQyQzEwLjU1NjQgNC40MDAxOSAxMC44MDM2IDQuNDI2OTYgMTEuMDI1IDQuMzQ0NjhMMTIuODIgMy42Nzc0QzEyLjk3NjQgMy44NTI5IDEzLjEyMzQgNC4wMzY5MSAxMy4yNjAyIDQuMjI4NjNMMTIuMjEwNSA1LjgyOTgyQzEyLjA4MTEgNi4wMjcxMyAxMi4wNTIyIDYuMjczODIgMTIuMTMyMyA2LjQ5NTc0QzEyLjI1MjUgNi44Mjg3OCAxMi4zMzQgNy4xODA1OCAxMi4zNzEyIDcuNTQ1OTdDMTIuMzk1IDcuNzgwOTcgMTIuNTI4MiA3Ljk5MDk5IDEyLjczMDYgOC4xMTI3N0wxNC4zNzI4IDkuMTAwOTJDMTQuMzMzIDkuMzM0NTIgMTQuMjgwNyA5LjU2Mzc5IDE0LjIxNjcgOS43ODgwNkwxMi4zMDggOS45NjU4N0MxMi4wNzM0IDkuOTg3NzMgMTEuODYyNyAxMC4xMTg2IDExLjczOTEgMTAuMzE5MkMxMS41NDk2IDEwLjYyNjggMTEuMzIzNCAxMC45MDk2IDExLjA2NjYgMTEuMTYxNkMxMC44OTgyIDExLjMyNjcgMTAuODE3MyAxMS41NjE1IDEwLjg0ODMgMTEuNzk1M0wxMS4wOTk3IDEzLjY5NkMxMC44OTQ2IDEzLjgwOTEgMTAuNjgyOCAxMy45MTE0IDEwLjQ2NTEgMTQuMDAyMkw5LjEzNTg0IDEyLjYyMDZDOC45NzI1MiAxMi40NTA5IDguNzM4OTQgMTIuMzY3NyA4LjUwNTA5IDEyLjM5NjFDOC4zMjg1MiAxMi40MTc1IDguMTQ4NDcgMTIuNDI4NSA3Ljk2NTUxIDEyLjQyODVDNy43ODI1MyAxMi40Mjg1IDcuNjAyNDcgMTIuNDE3NSA3LjQyNTg5IDEyLjM5NjFDNy4xOTIwNCAxMi4zNjc3IDYuOTU4NDYgMTIuNDUwOSA2Ljc5NTE0IDEyLjYyMDZMNS40NjU4OSAxNC4wMDIyQzUuMjQ4MTYgMTMuOTExNCA1LjAzNjM4IDEzLjgwOTEgNC44MzEzMSAxMy42OTZMNS4wODI3MiAxMS43OTUzQzUuMTEzNjUgMTEuNTYxNSA1LjAzMjc4IDExLjMyNjcgNC44NjQ0MiAxMS4xNjE1QzQuNjA3NjEgMTAuOTA5NiA0LjM4MTQ0IDEwLjYyNjggNC4xOTE5NSAxMC4zMTkyQzQuMDY4MzMgMTAuMTE4NiAzLjg1NzYyIDkuOTg3NzMgMy42MjI5OSA5Ljk2NTg3TDEuNzE0MzMgOS43ODgwNkMxLjY1MDMyIDkuNTYzNzkgMS41OTgwNCA5LjMzNDUxIDEuNTU4MjIgOS4xMDA5TDMuMjAwNCA4LjExMjc1QzMuNDAyNzkgNy45OTA5NiAzLjUzNTk5IDcuNzgwOTUgMy41NTk4NyA3LjU0NTk1QzMuNTk3IDcuMTgwNTggMy42Nzg0NyA2LjgyODggMy43OTg3MiA2LjQ5NTc4QzMuODc4ODQgNi4yNzM4NiAzLjg0OTg4IDYuMDI3MTggMy43MjA1MSA1LjgyOTg2TDIuNjcwNzYgNC4yMjg2NUMyLjgwNzU5IDQuMDM2OTMgMi45NTQ2IDMuODUyOTIgMy4xMTEgMy42Nzc0MUw0LjkwNjA1IDQuMzQ0NjlDNS4xMjc0IDQuNDI2OTcgNS4zNzQ1NyA0LjQwMDIgNS41NzMxNyA0LjI3MjQzQzUuODczOTQgNC4wNzg5MyA2LjE5OTM3IDMuOTIxMDEgNi41NDM1NyAzLjgwNDRDNi43NjcwNSAzLjcyODY5IDYuOTQxODcgMy41NTIyMyA3LjAxNTQ4IDMuMzI4MDVaIiBmaWxsPSIjNkY2RjZGIi8+CjwvZz4KPGRlZnM+CjxjbGlwUGF0aCBpZD0iY2xpcDBfMTMxMjNfMzUwMTkiPgo8cmVjdCB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9IndoaXRlIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==) gear icon and select **OpenSharing**.
    
    Alternatively, in the upper-right corner, click **Share > OpenSharing**.
    
3.  On the **Shared by me** tab, find the share you want to add a table to and click its name. You can add tables with [row tracking](https://docs.databricks.com/aws/en/tables/features/row-tracking) enabled. Recipients can query the row tracking columns.
    
4.  Click **Manage assets > Edit assets**.
    
5.  On the **Edit assets** page, select either an entire schema (database) or individual tables.
    
    *   To select a table, first select the catalog, then the schema that contains the table, then the table itself.
        
        You can search for tables by name, column name, or comment using workspace search. See [Search for workspace objects](https://docs.databricks.com/aws/en/search/).
        
    *   To select a schema, first select the catalog and then the schema.
        
        For detailed information about sharing schemas, see [Add schemas to a share](#schemas).
        
6.  **History**: Share the table history to allow recipients to perform time travel queries, read the table with Spark Structured Streaming, or run [transactions](https://docs.databricks.com/aws/en/transactions/). For Databricks-to-Databricks shares, the table's Delta log is also shared to improve performance. See [Improve table read performance with history sharing](https://docs.databricks.com/aws/en/delta-sharing/share-data-databricks#share-history). History sharing requires Databricks Runtime 12.2 LTS or above.
    
7.  (Optional) Click ![Speech bubble plus icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTcuMjUgOS41VjcuNzVINS41VjYuMjVINy4yNVY0LjVIOC43NVY2LjI1SDEwLjVWNy43NUg4Ljc1VjkuNUg3LjI1WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTYgMUMyLjY4NjI5IDEgMCAzLjY4NjI5IDAgN1Y3LjI1QzAgMTAuMTcxNCAyLjE3ODczIDEyLjU4NCA1IDEyLjk1MTVWMTUuMjVDNSAxNS41NTMzIDUuMTgyNzMgMTUuODI2OCA1LjQ2Mjk5IDE1Ljk0MjlDNS43NDMyNCAxNi4wNTkgNi4wNjU4MyAxNS45OTQ4IDYuMjgwMzMgMTUuNzgwM0w5LjA2MDY2IDEzSDEwQzEzLjMxMzcgMTMgMTYgMTAuMzEzNyAxNiA3QzE2IDMuNjg2MjkgMTMuMzEzNyAxIDEwIDFINlpNMS41IDdDMS41IDQuNTE0NzIgMy41MTQ3MiAyLjUgNiAyLjVIMTBDMTIuNDg1MyAyLjUgMTQuNSA0LjUxNDcyIDE0LjUgN0MxNC41IDkuNDg1MjggMTIuNDg1MyAxMS41IDEwIDExLjVIOC43NUM4LjU1MTA5IDExLjUgOC4zNjAzMiAxMS41NzkgOC4yMTk2NyAxMS43MTk3TDYuNSAxMy40MzkzVjEyLjI1QzYuNSAxMS44MzU4IDYuMTY0MjEgMTEuNSA1Ljc1IDExLjVDMy40MDI3OSAxMS41IDEuNSA5LjU5NzIxIDEuNSA3LjI1VjdaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) under the **Alias** or **Partition** columns to add an alias or partition. Alias and partitions are not available if you select an entire schema. Table history is included by default if you select an entire schema.
    
    *   **Alias**: An alternate table name to make the table name more readable. The alias is the table name that the recipient sees and must use in queries. Recipients cannot use the actual table name if an alias is specified.
    *   **Partition**: Share only part of the table. For example, `(column = 'value')`. See [Specify table partitions to share](#partitions) and [Use recipient properties to do partition filtering](#properties).
8.  Click **Save**.
    

For information about removing tables from a share, see [Update shares](https://docs.databricks.com/aws/en/delta-sharing/manage-share#update).

### Cloud token eligibility[​](#cloud-token-eligibility "Direct link to cloud-token-eligibility")

Databricks uses cloud tokens (temporary, path-scoped cloud credentials) to give recipients direct read access to shared Delta table files. In the Databricks-to-Open sharing protocol, this is also called _directory-based access mode_. Views, materialized views, foreign tables, streaming tables, volumes, notebooks, Python UDFs, and AI models are not supported. Which tables qualify depends on the sharing protocol.

**Databricks-to-Databricks sharing**: Cloud tokens are used when all of the following are true:

*   The table is shared `WITH HISTORY` (full history from the beginning).
*   The table is shared without a partition filter.

**Databricks-to-Open sharing**: Cloud tokens (directory-based access mode) are used when all of the following are true:

*   The shared object is a _managed or external Delta table_.
*   The table is shared `WITH HISTORY` (full history from the beginning).
*   The table is shared without a partition filter.
*   The table is not a CCv2 table.
*   The table does not use default storage.

For Databricks-to-Databricks shares, cloud tokens are exchanged directly between Unity Catalog metastores without long-lived bearer tokens, resulting in performance comparable to direct source table access. For Databricks-to-Open sharing, the OpenSharing server includes the table's cloud storage location and `accessModes: ["url", "dir"]` in list and metadata responses. Open recipients can call the [Generate Temporary Table Credentials](https://github.com/delta-io/delta-sharing/blob/main/PROTOCOL.md#generate-temporary-table-credential) endpoint to obtain credentials and read directly from cloud storage.

important

When cloud token access is used, recipients receive credentials scoped to the root directory of the shared Delta table. This grants read access to both the data files and the Delta log. The Delta log contains the commit history for each table version, information about the committer, and deleted data that has not been vacuumed.

To share only part of a table when you add the table to a share, provide a partition specification. Specify partitions when you add a table to a share or update a share, using Catalog Explorer, the Databricks Unity Catalog CLI, or SQL commands in a Databricks notebook or the Databricks SQL query editor. See [Add tables to a share](#add-tables) and [Update shares](https://docs.databricks.com/aws/en/delta-sharing/manage-share#update).

### Example[​](#example "Direct link to Example")

The following SQL example shares part of the data in the `inventory` table, partitioned by the `year`, `month`, and `date` columns:

*   Data for the year 2021.
*   Data for December 2020.
*   Data for December 25, 2019.

SQL

    ALTER SHARE share_nameADD TABLE inventoryPARTITION (year = "2021"),          (year = "2020", month = "Dec"),          (year = "2019", month = "Dec", date = "2019-12-25");

### Use recipient properties to do partition filtering[​](#use-recipient-properties-to-do-partition-filtering "Direct link to use-recipient-properties-to-do-partition-filtering")

You can share a table partition that matches [data recipient properties](https://docs.databricks.com/aws/en/delta-sharing/manage-recipients#properties), also known as parameterized partition sharing.

Default properties include:

*   `databricks.accountId`: The Databricks account that a data recipient belongs to (Databricks-to-Databricks sharing only).
*   `databricks.metastoreId`: The Unity Catalog metastore that a data recipient belongs to (Databricks-to-Databricks sharing only).
*   `databricks.name`: The name of the data recipient.

You can create any custom property when you create or update a recipient.

Filtering by recipient property enables you to share the same tables, using the same share, across multiple Databricks accounts, workspaces, and users while maintaining data boundaries between them.

For example, if your tables include a Databricks account ID column, you can create a single share with table partitions defined by Databricks account ID. When you share, OpenSharing dynamically delivers to each recipient only the data associated with their Databricks account.

![Diagram of parameter-based dynamic partition sharing in OpenSharing](https://docs.databricks.com/aws/en/assets/images/parameterized-partitions-e88462c18172d2952f6537399bb3c841.png)

Without the ability to dynamically partition by property, you would have to create a separate share for each recipient.

To specify a partition that filters by recipient properties when you create or update a share, you can use Catalog Explorer or the `CURRENT_RECIPIENT` SQL function in a Databricks notebook or the Databricks SQL query editor:

note

Recipient properties are available on Databricks Runtime 12.2 or above.

*   Catalog Explorer
*   SQL

1.  In your Databricks workspace, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
    
2.  At the top of the **Catalog** pane, click the ![Gear icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzEzMTIzXzM1MDE5KSI+CjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNNy45ODQzMyA1QzYuMzI3NDcgNSA0Ljk4NDMzIDYuMzQzMTUgNC45ODQzMyA4QzQuOTg0MzMgOS42NTY4NSA2LjMyNzQ3IDExIDcuOTg0MzMgMTFDOS42NDExOCAxMSAxMC45ODQzIDkuNjU2ODUgMTAuOTg0MyA4QzEwLjk4NDMgNi4zNDMxNSA5LjY0MTE4IDUgNy45ODQzMyA1Wk02LjQ4NDMzIDhDNi40ODQzMyA3LjE3MTU3IDcuMTU1OSA2LjUgNy45ODQzMyA2LjVDOC44MTI3NSA2LjUgOS40ODQzMyA3LjE3MTU3IDkuNDg0MzMgOEM5LjQ4NDMzIDguODI4NDMgOC44MTI3NSA5LjUgNy45ODQzMyA5LjVDNy4xNTU5IDkuNSA2LjQ4NDMzIDguODI4NDMgNi40ODQzMyA4WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTcuOTY1NSAwQzcuNjI1NTIgMCA3LjI5MDE0IDAuMDIxMjUxMSA2Ljk2MDcgMC4wNjI1NzM2QzYuNjczMDQgMC4wOTg2NTU4IDYuNDMxOTQgMC4yOTczIDYuMzQxNDggMC41NzI3NDVMNS43MDI0IDIuNTE4ODhDNS40OTI0NCAyLjYwNTY1IDUuMjg4NiAyLjcwNDExIDUuMDkxNyAyLjgxMzQxTDMuMTcxOTggMi4wOTk3OUMyLjkwMDU0IDEuOTk4ODggMi41OTUyNiAyLjA2MzI2IDIuMzg3NjkgMi4yNjUxOUMxLjkwNjkgMi43MzI4OSAxLjQ4NDY0IDMuMjYwNjggMS4xMzMwMSAzLjgzNjYxQzAuOTgxOTgyIDQuMDgzOTkgMC45ODcwMDYgNC4zOTYyNSAxLjE0NTkyIDQuNjM4NjRMMi4yNjkxOSA2LjM1MTk4QzIuMjA2OTIgNi41Njc1NyAyLjE1NjU2IDYuNzg4MTQgMi4xMTg4NSA3LjAxMjkzTDAuMzYzMzIyIDguMDY5MjhDMC4xMTU0ODMgOC4yMTg0MiAtMC4wMjQ1MDg2IDguNDk2NzggMC4wMDM1NDkyOSA4Ljc4NDY2QzAuMDcwMDUzNiA5LjQ2NzAyIDAuMjIyMzY1IDEwLjEyNDggMC40NDk2NjkgMTAuNzQ2NkMwLjU0OTA4NSAxMS4wMTg2IDAuNzk2MTg5IDExLjIwOSAxLjA4NDUxIDExLjIzNTlMMy4xMjY2NyAxMS40MjYxQzMuMjU3MzUgMTEuNjEwNCAzLjM5ODI2IDExLjc4NjggMy41NDg1OCAxMS45NTQ2TDMuMjc5NzQgMTMuOTg3MkMzLjI0MTggMTQuMjc0IDMuMzcyMjIgMTQuNTU3MSAzLjYxNDkgMTQuNzE0NkM0LjE3NDI3IDE1LjA3NzcgNC43ODIxNiAxNS4zNzMgNS40MjY4NiAxNS41ODg2QzUuNzAxNDcgMTUuNjgwNCA2LjAwNDQyIDE1LjYwNiA2LjIwNTE4IDE1LjM5NzNMNy42Mjc0MyAxMy45MTlDNy43MzkzOSAxMy45MjU0IDcuODUyMTEgMTMuOTI4NSA3Ljk2NTUxIDEzLjkyODVDOC4wNzg4OSAxMy45Mjg1IDguMTkxNiAxMy45MjU0IDguMzAzNTQgMTMuOTE5TDkuNzI1OCAxNS4zOTczQzkuOTI2NTYgMTUuNjA2IDEwLjIyOTUgMTUuNjgwNCAxMC41MDQxIDE1LjU4ODZDMTEuMTQ4OCAxNS4zNzMgMTEuNzU2NyAxNS4wNzc3IDEyLjMxNjEgMTQuNzE0NkMxMi41NTg4IDE0LjU1NzEgMTIuNjg5MiAxNC4yNzQgMTIuNjUxMiAxMy45ODcyTDEyLjM4MjQgMTEuOTU0N0MxMi41MzI3IDExLjc4NjkgMTIuNjczNyAxMS42MTA0IDEyLjgwNDMgMTEuNDI2MUwxNC44NDY1IDExLjIzNTlDMTUuMTM0OCAxMS4yMDkgMTUuMzgxOSAxMS4wMTg2IDE1LjQ4MTMgMTAuNzQ2NkMxNS43MDg2IDEwLjEyNDggMTUuODYwOSA5LjQ2NzA0IDE1LjkyNzUgOC43ODQ2OUMxNS45NTU1IDguNDk2OCAxNS44MTU1IDguMjE4NDQgMTUuNTY3NyA4LjA2OTNMMTMuODEyMiA3LjAxMjk2QzEzLjc3NDUgNi43ODgxNSAxMy43MjQxIDYuNTY3NTQgMTMuNjYxOCA2LjM1MTkzTDE0Ljc4NTEgNC42Mzg2MUMxNC45NDQgNC4zOTYyMiAxNC45NDkgNC4wODM5NiAxNC43OTggMy44MzY1OEMxNC40NDYzIDMuMjYwNjUgMTQuMDI0MSAyLjczMjg3IDEzLjU0MzMgMi4yNjUxOEMxMy4zMzU3IDIuMDYzMjUgMTMuMDMwNSAxLjk5ODg3IDEyLjc1OSAyLjA5OTc4TDEwLjgzOTMgMi44MTM0QzEwLjY0MjQgMi43MDQwOSAxMC40Mzg1IDIuNjA1NjMgMTAuMjI4NiAyLjUxODg1TDkuNTg5NDkgMC41NzI3NDFDOS40OTkwMyAwLjI5NzI5NCA5LjI1NzkzIDAuMDk4NjQ5NiA4Ljk3MDI2IDAuMDYyNTY4NkM4LjY0MDgzIDAuMDIxMjQ5NCA4LjMwNTQ4IDAgNy45NjU1IDBaTTcuMDE1NDggMy4zMjgwNUw3LjYxMjcxIDEuNTA5MzlDNy43Mjk0NiAxLjUwMzE2IDcuODQ3MDggMS41IDcuOTY1NSAxLjVDOC4wODM5MSAxLjUgOC4yMDE1MyAxLjUwMzE2IDguMzE4MjYgMS41MDkzOUw4LjkxNTQ4IDMuMzI4MDRDOC45ODkxIDMuNTUyMjEgOS4xNjM5MiAzLjcyODY4IDkuMzg3NCAzLjgwNDM4QzkuNzMxNjEgMy45MjA5OSAxMC4wNTcxIDQuMDc4OTIgMTAuMzU3OCA0LjI3MjQyQzEwLjU1NjQgNC40MDAxOSAxMC44MDM2IDQuNDI2OTYgMTEuMDI1IDQuMzQ0NjhMMTIuODIgMy42Nzc0QzEyLjk3NjQgMy44NTI5IDEzLjEyMzQgNC4wMzY5MSAxMy4yNjAyIDQuMjI4NjNMMTIuMjEwNSA1LjgyOTgyQzEyLjA4MTEgNi4wMjcxMyAxMi4wNTIyIDYuMjczODIgMTIuMTMyMyA2LjQ5NTc0QzEyLjI1MjUgNi44Mjg3OCAxMi4zMzQgNy4xODA1OCAxMi4zNzEyIDcuNTQ1OTdDMTIuMzk1IDcuNzgwOTcgMTIuNTI4MiA3Ljk5MDk5IDEyLjczMDYgOC4xMTI3N0wxNC4zNzI4IDkuMTAwOTJDMTQuMzMzIDkuMzM0NTIgMTQuMjgwNyA5LjU2Mzc5IDE0LjIxNjcgOS43ODgwNkwxMi4zMDggOS45NjU4N0MxMi4wNzM0IDkuOTg3NzMgMTEuODYyNyAxMC4xMTg2IDExLjczOTEgMTAuMzE5MkMxMS41NDk2IDEwLjYyNjggMTEuMzIzNCAxMC45MDk2IDExLjA2NjYgMTEuMTYxNkMxMC44OTgyIDExLjMyNjcgMTAuODE3MyAxMS41NjE1IDEwLjg0ODMgMTEuNzk1M0wxMS4wOTk3IDEzLjY5NkMxMC44OTQ2IDEzLjgwOTEgMTAuNjgyOCAxMy45MTE0IDEwLjQ2NTEgMTQuMDAyMkw5LjEzNTg0IDEyLjYyMDZDOC45NzI1MiAxMi40NTA5IDguNzM4OTQgMTIuMzY3NyA4LjUwNTA5IDEyLjM5NjFDOC4zMjg1MiAxMi40MTc1IDguMTQ4NDcgMTIuNDI4NSA3Ljk2NTUxIDEyLjQyODVDNy43ODI1MyAxMi40Mjg1IDcuNjAyNDcgMTIuNDE3NSA3LjQyNTg5IDEyLjM5NjFDNy4xOTIwNCAxMi4zNjc3IDYuOTU4NDYgMTIuNDUwOSA2Ljc5NTE0IDEyLjYyMDZMNS40NjU4OSAxNC4wMDIyQzUuMjQ4MTYgMTMuOTExNCA1LjAzNjM4IDEzLjgwOTEgNC44MzEzMSAxMy42OTZMNS4wODI3MiAxMS43OTUzQzUuMTEzNjUgMTEuNTYxNSA1LjAzMjc4IDExLjMyNjcgNC44NjQ0MiAxMS4xNjE1QzQuNjA3NjEgMTAuOTA5NiA0LjM4MTQ0IDEwLjYyNjggNC4xOTE5NSAxMC4zMTkyQzQuMDY4MzMgMTAuMTE4NiAzLjg1NzYyIDkuOTg3NzMgMy42MjI5OSA5Ljk2NTg3TDEuNzE0MzMgOS43ODgwNkMxLjY1MDMyIDkuNTYzNzkgMS41OTgwNCA5LjMzNDUxIDEuNTU4MjIgOS4xMDA5TDMuMjAwNCA4LjExMjc1QzMuNDAyNzkgNy45OTA5NiAzLjUzNTk5IDcuNzgwOTUgMy41NTk4NyA3LjU0NTk1QzMuNTk3IDcuMTgwNTggMy42Nzg0NyA2LjgyODggMy43OTg3MiA2LjQ5NTc4QzMuODc4ODQgNi4yNzM4NiAzLjg0OTg4IDYuMDI3MTggMy43MjA1MSA1LjgyOTg2TDIuNjcwNzYgNC4yMjg2NUMyLjgwNzU5IDQuMDM2OTMgMi45NTQ2IDMuODUyOTIgMy4xMTEgMy42Nzc0MUw0LjkwNjA1IDQuMzQ0NjlDNS4xMjc0IDQuNDI2OTcgNS4zNzQ1NyA0LjQwMDIgNS41NzMxNyA0LjI3MjQzQzUuODczOTQgNC4wNzg5MyA2LjE5OTM3IDMuOTIxMDEgNi41NDM1NyAzLjgwNDRDNi43NjcwNSAzLjcyODY5IDYuOTQxODcgMy41NTIyMyA3LjAxNTQ4IDMuMzI4MDVaIiBmaWxsPSIjNkY2RjZGIi8+CjwvZz4KPGRlZnM+CjxjbGlwUGF0aCBpZD0iY2xpcDBfMTMxMjNfMzUwMTkiPgo8cmVjdCB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9IndoaXRlIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==) gear icon and select **OpenSharing**.
    
    Alternatively, in the upper-right corner, click **Share > OpenSharing**.
    
3.  On the **Shared by me** tab, find the share you want to update and click its name.
    
4.  Click **Manage assets > Add data assets**.
    
5.  On the **Add tables** page, select the catalog and database that contain the table, then select the table.
    
    If you aren't sure which catalog and database contain the table, you can search for it by name, column name, or comment using workspace search. See [Search for workspace objects](https://docs.databricks.com/aws/en/search/).
    
6.  (Optional) Click ![Speech bubble plus icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTcuMjUgOS41VjcuNzVINS41VjYuMjVINy4yNVY0LjVIOC43NVY2LjI1SDEwLjVWNy43NUg4Ljc1VjkuNUg3LjI1WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTYgMUMyLjY4NjI5IDEgMCAzLjY4NjI5IDAgN1Y3LjI1QzAgMTAuMTcxNCAyLjE3ODczIDEyLjU4NCA1IDEyLjk1MTVWMTUuMjVDNSAxNS41NTMzIDUuMTgyNzMgMTUuODI2OCA1LjQ2Mjk5IDE1Ljk0MjlDNS43NDMyNCAxNi4wNTkgNi4wNjU4MyAxNS45OTQ4IDYuMjgwMzMgMTUuNzgwM0w5LjA2MDY2IDEzSDEwQzEzLjMxMzcgMTMgMTYgMTAuMzEzNyAxNiA3QzE2IDMuNjg2MjkgMTMuMzEzNyAxIDEwIDFINlpNMS41IDdDMS41IDQuNTE0NzIgMy41MTQ3MiAyLjUgNiAyLjVIMTBDMTIuNDg1MyAyLjUgMTQuNSA0LjUxNDcyIDE0LjUgN0MxNC41IDkuNDg1MjggMTIuNDg1MyAxMS41IDEwIDExLjVIOC43NUM4LjU1MTA5IDExLjUgOC4zNjAzMiAxMS41NzkgOC4yMTk2NyAxMS43MTk3TDYuNSAxMy40MzkzVjEyLjI1QzYuNSAxMS44MzU4IDYuMTY0MjEgMTEuNSA1Ljc1IDExLjVDMy40MDI3OSAxMS41IDEuNSA5LjU5NzIxIDEuNSA3LjI1VjdaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) under **Partition** column to add a partition.
    
    On the **Add partition to the table** dialog, add the property-based partition specification using the following syntax:
    
        (<column-name> = CURRENT_RECIPIENT().<property-key>)
    
    For example,
    
        (country = CURRENT_RECIPIENT().country)
    
7.  Click **Save**.
    

Deletion vectors are a storage optimization feature that you can enable on Delta tables. See [Deletion vectors in Databricks](https://docs.databricks.com/aws/en/tables/features/deletion-vectors).

Databricks also supports column mapping for Delta tables. See [Rename and drop columns with Delta Lake column mapping](https://docs.databricks.com/aws/en/tables/features/column-mapping).

To share a table with deletion vectors or column mapping, you must share it with history. See [Add tables to a share](#add-tables).

When you share a table with deletion vectors or column mapping, recipients can query the table using a SQL warehouse, a compute running Databricks Runtime 14.1 or above, or a compute that is running open source `delta-sharing-spark` 3.1 or above. See [Read tables with deletion vectors or column mapping enabled](https://docs.databricks.com/aws/en/delta-sharing/read-data-databricks#deletion-vectors) and [Read tables with deletion vectors or column mapping enabled](https://docs.databricks.com/aws/en/delta-sharing/read-data-databricks#deletion-vectors).

Check that you meet the [requirements](https://docs.databricks.com/aws/en/delta-sharing/create-share#requirements) before adding schemas to a share.

Adding an entire schema to a share provides your recipients with access to all of the data assets in the schema at the time that you create the share, as well as any assets that are added to the schema over time. This includes all tables, views, and volumes in the schema. Tables shared this way always include full history.

To add a schema to a share, follow the instructions in [Add tables to a share](#add-tables), paying attention to the content that specifies how to add a schema.

Adding, updating, or removing a schema using SQL requires a SQL warehouse or compute running Databricks Runtime 13.3 LTS or above. Doing the same using Catalog Explorer has no compute requirements.

### Limitations[​](#limitations "Direct link to limitations")

*   You can share schemas even if they include unsupported data assets. These assets are filtered out and not shared with recipients. Unsupported data assets include the following:
    
    *   Tables that use liquid clustering with partition filtering
    *   R2 tables with V2 checkpoint
    *   Tables with collations enabled
    *   Tables with row filters or columns masks
    *   `SHALLOW CLONE` tables
    *   [Foreign key constraints](https://docs.databricks.com/aws/en/tables/constraints) in shared tables
*   Table aliases, partitions, and volume aliases are not available if you share an entire schema. If you have created aliases or partitions for any assets in the schema, these are removed when you add the entire schema to the share.
    
*   If you want to specify advanced options for a table or volume in the schema, you must share the table or volume using SQL and give the table or volume an alias with a different schema name.
    
*   Schema-level aliasing is not supported. Schemas with the same name from different catalogs can't be added to the same share. Instead, share individual tables with aliased schema names.
    

[Attribute-based access control (ABAC)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/) is a data governance model that provides flexible, scalable, and centralized access control across Databricks.

You can share a table or schema secured by ABAC policies like standard tables. To learn how to apply ABAC policies to your data assets, see [Create and manage row filter and column mask policies](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/policies).

However, you must be a _privileged user_. A privileged user is the share owner _and_ a user who is excluded from the ABAC policies applied to the data asset. The policy does not govern the recipient's access. Recipients have full access to the shared asset. [ABAC limitations](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/requirements) apply.

Streaming tables are regular Delta tables with extra support for streaming or incremental data processing. Streaming tables are designed for append-only data sources and process inputs only once. See [Use standalone streaming tables](https://docs.databricks.com/aws/en/ldp/dbsql/streaming).

Check that you meet the [requirements](https://docs.databricks.com/aws/en/delta-sharing/create-share#requirements) before adding streaming tables to a share.

### Additional requirements[​](#additional-requirements "Direct link to Additional requirements")

*   If your workspace has workspace-catalog bindings enabled, check that the workspace has read and write access to the catalog the streaming table is in. For more information, see [Workspace-catalog binding](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/workspace-catalog-binding).
*   Shareable streaming tables must be defined on Delta tables or other shareable streaming tables or views.
*   You must use a SQL warehouse or a compute on Databricks Runtime 13.3 LTS or above when you add a streaming table to a share.

### Limitations[​](#limitations-1 "Direct link to Limitations")

*   The streaming table cannot have row filters and column masks.
    *   The base table of the streaming table can have row filters and column masks.
*   The streaming table cannot have partition filters. Instead, create a view on top of the streaming table.
*   Databricks-to-Open sharing recipients can only read the current snapshot of the streaming table. Time travel, query history, streaming reads, and CDF are not supported for open recipients. If your recipients need CDF, share a regular Delta table with CDF enabled.
*   If the recipient doesn't have direct access to the underlying data, `LIMIT` clauses and predicate pushdown aren't supported. The system fully materializes all query results before returning them to the recipient, regardless of query filters. See [Do recipients have direct access to the underlying data in shared views, materialized views, and streaming tables?](https://docs.databricks.com/aws/en/delta-sharing/#accessing-views).
*   General limitations for streaming tables also apply. See [Streaming table limitations](https://docs.databricks.com/aws/en/ldp/concepts/streaming-tables#streaming-table-limitations).

To add streaming tables to a share:

*   Catalog Explorer
*   SQL
*   CLI

1.  In your Databricks workspace, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
    
2.  At the top of the **Catalog** pane, click the ![Gear icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzEzMTIzXzM1MDE5KSI+CjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNNy45ODQzMyA1QzYuMzI3NDcgNSA0Ljk4NDMzIDYuMzQzMTUgNC45ODQzMyA4QzQuOTg0MzMgOS42NTY4NSA2LjMyNzQ3IDExIDcuOTg0MzMgMTFDOS42NDExOCAxMSAxMC45ODQzIDkuNjU2ODUgMTAuOTg0MyA4QzEwLjk4NDMgNi4zNDMxNSA5LjY0MTE4IDUgNy45ODQzMyA1Wk02LjQ4NDMzIDhDNi40ODQzMyA3LjE3MTU3IDcuMTU1OSA2LjUgNy45ODQzMyA2LjVDOC44MTI3NSA2LjUgOS40ODQzMyA3LjE3MTU3IDkuNDg0MzMgOEM5LjQ4NDMzIDguODI4NDMgOC44MTI3NSA5LjUgNy45ODQzMyA5LjVDNy4xNTU5IDkuNSA2LjQ4NDMzIDguODI4NDMgNi40ODQzMyA4WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTcuOTY1NSAwQzcuNjI1NTIgMCA3LjI5MDE0IDAuMDIxMjUxMSA2Ljk2MDcgMC4wNjI1NzM2QzYuNjczMDQgMC4wOTg2NTU4IDYuNDMxOTQgMC4yOTczIDYuMzQxNDggMC41NzI3NDVMNS43MDI0IDIuNTE4ODhDNS40OTI0NCAyLjYwNTY1IDUuMjg4NiAyLjcwNDExIDUuMDkxNyAyLjgxMzQxTDMuMTcxOTggMi4wOTk3OUMyLjkwMDU0IDEuOTk4ODggMi41OTUyNiAyLjA2MzI2IDIuMzg3NjkgMi4yNjUxOUMxLjkwNjkgMi43MzI4OSAxLjQ4NDY0IDMuMjYwNjggMS4xMzMwMSAzLjgzNjYxQzAuOTgxOTgyIDQuMDgzOTkgMC45ODcwMDYgNC4zOTYyNSAxLjE0NTkyIDQuNjM4NjRMMi4yNjkxOSA2LjM1MTk4QzIuMjA2OTIgNi41Njc1NyAyLjE1NjU2IDYuNzg4MTQgMi4xMTg4NSA3LjAxMjkzTDAuMzYzMzIyIDguMDY5MjhDMC4xMTU0ODMgOC4yMTg0MiAtMC4wMjQ1MDg2IDguNDk2NzggMC4wMDM1NDkyOSA4Ljc4NDY2QzAuMDcwMDUzNiA5LjQ2NzAyIDAuMjIyMzY1IDEwLjEyNDggMC40NDk2NjkgMTAuNzQ2NkMwLjU0OTA4NSAxMS4wMTg2IDAuNzk2MTg5IDExLjIwOSAxLjA4NDUxIDExLjIzNTlMMy4xMjY2NyAxMS40MjYxQzMuMjU3MzUgMTEuNjEwNCAzLjM5ODI2IDExLjc4NjggMy41NDg1OCAxMS45NTQ2TDMuMjc5NzQgMTMuOTg3MkMzLjI0MTggMTQuMjc0IDMuMzcyMjIgMTQuNTU3MSAzLjYxNDkgMTQuNzE0NkM0LjE3NDI3IDE1LjA3NzcgNC43ODIxNiAxNS4zNzMgNS40MjY4NiAxNS41ODg2QzUuNzAxNDcgMTUuNjgwNCA2LjAwNDQyIDE1LjYwNiA2LjIwNTE4IDE1LjM5NzNMNy42Mjc0MyAxMy45MTlDNy43MzkzOSAxMy45MjU0IDcuODUyMTEgMTMuOTI4NSA3Ljk2NTUxIDEzLjkyODVDOC4wNzg4OSAxMy45Mjg1IDguMTkxNiAxMy45MjU0IDguMzAzNTQgMTMuOTE5TDkuNzI1OCAxNS4zOTczQzkuOTI2NTYgMTUuNjA2IDEwLjIyOTUgMTUuNjgwNCAxMC41MDQxIDE1LjU4ODZDMTEuMTQ4OCAxNS4zNzMgMTEuNzU2NyAxNS4wNzc3IDEyLjMxNjEgMTQuNzE0NkMxMi41NTg4IDE0LjU1NzEgMTIuNjg5MiAxNC4yNzQgMTIuNjUxMiAxMy45ODcyTDEyLjM4MjQgMTEuOTU0N0MxMi41MzI3IDExLjc4NjkgMTIuNjczNyAxMS42MTA0IDEyLjgwNDMgMTEuNDI2MUwxNC44NDY1IDExLjIzNTlDMTUuMTM0OCAxMS4yMDkgMTUuMzgxOSAxMS4wMTg2IDE1LjQ4MTMgMTAuNzQ2NkMxNS43MDg2IDEwLjEyNDggMTUuODYwOSA5LjQ2NzA0IDE1LjkyNzUgOC43ODQ2OUMxNS45NTU1IDguNDk2OCAxNS44MTU1IDguMjE4NDQgMTUuNTY3NyA4LjA2OTNMMTMuODEyMiA3LjAxMjk2QzEzLjc3NDUgNi43ODgxNSAxMy43MjQxIDYuNTY3NTQgMTMuNjYxOCA2LjM1MTkzTDE0Ljc4NTEgNC42Mzg2MUMxNC45NDQgNC4zOTYyMiAxNC45NDkgNC4wODM5NiAxNC43OTggMy44MzY1OEMxNC40NDYzIDMuMjYwNjUgMTQuMDI0MSAyLjczMjg3IDEzLjU0MzMgMi4yNjUxOEMxMy4zMzU3IDIuMDYzMjUgMTMuMDMwNSAxLjk5ODg3IDEyLjc1OSAyLjA5OTc4TDEwLjgzOTMgMi44MTM0QzEwLjY0MjQgMi43MDQwOSAxMC40Mzg1IDIuNjA1NjMgMTAuMjI4NiAyLjUxODg1TDkuNTg5NDkgMC41NzI3NDFDOS40OTkwMyAwLjI5NzI5NCA5LjI1NzkzIDAuMDk4NjQ5NiA4Ljk3MDI2IDAuMDYyNTY4NkM4LjY0MDgzIDAuMDIxMjQ5NCA4LjMwNTQ4IDAgNy45NjU1IDBaTTcuMDE1NDggMy4zMjgwNUw3LjYxMjcxIDEuNTA5MzlDNy43Mjk0NiAxLjUwMzE2IDcuODQ3MDggMS41IDcuOTY1NSAxLjVDOC4wODM5MSAxLjUgOC4yMDE1MyAxLjUwMzE2IDguMzE4MjYgMS41MDkzOUw4LjkxNTQ4IDMuMzI4MDRDOC45ODkxIDMuNTUyMjEgOS4xNjM5MiAzLjcyODY4IDkuMzg3NCAzLjgwNDM4QzkuNzMxNjEgMy45MjA5OSAxMC4wNTcxIDQuMDc4OTIgMTAuMzU3OCA0LjI3MjQyQzEwLjU1NjQgNC40MDAxOSAxMC44MDM2IDQuNDI2OTYgMTEuMDI1IDQuMzQ0NjhMMTIuODIgMy42Nzc0QzEyLjk3NjQgMy44NTI5IDEzLjEyMzQgNC4wMzY5MSAxMy4yNjAyIDQuMjI4NjNMMTIuMjEwNSA1LjgyOTgyQzEyLjA4MTEgNi4wMjcxMyAxMi4wNTIyIDYuMjczODIgMTIuMTMyMyA2LjQ5NTc0QzEyLjI1MjUgNi44Mjg3OCAxMi4zMzQgNy4xODA1OCAxMi4zNzEyIDcuNTQ1OTdDMTIuMzk1IDcuNzgwOTcgMTIuNTI4MiA3Ljk5MDk5IDEyLjczMDYgOC4xMTI3N0wxNC4zNzI4IDkuMTAwOTJDMTQuMzMzIDkuMzM0NTIgMTQuMjgwNyA5LjU2Mzc5IDE0LjIxNjcgOS43ODgwNkwxMi4zMDggOS45NjU4N0MxMi4wNzM0IDkuOTg3NzMgMTEuODYyNyAxMC4xMTg2IDExLjczOTEgMTAuMzE5MkMxMS41NDk2IDEwLjYyNjggMTEuMzIzNCAxMC45MDk2IDExLjA2NjYgMTEuMTYxNkMxMC44OTgyIDExLjMyNjcgMTAuODE3MyAxMS41NjE1IDEwLjg0ODMgMTEuNzk1M0wxMS4wOTk3IDEzLjY5NkMxMC44OTQ2IDEzLjgwOTEgMTAuNjgyOCAxMy45MTE0IDEwLjQ2NTEgMTQuMDAyMkw5LjEzNTg0IDEyLjYyMDZDOC45NzI1MiAxMi40NTA5IDguNzM4OTQgMTIuMzY3NyA4LjUwNTA5IDEyLjM5NjFDOC4zMjg1MiAxMi40MTc1IDguMTQ4NDcgMTIuNDI4NSA3Ljk2NTUxIDEyLjQyODVDNy43ODI1MyAxMi40Mjg1IDcuNjAyNDcgMTIuNDE3NSA3LjQyNTg5IDEyLjM5NjFDNy4xOTIwNCAxMi4zNjc3IDYuOTU4NDYgMTIuNDUwOSA2Ljc5NTE0IDEyLjYyMDZMNS40NjU4OSAxNC4wMDIyQzUuMjQ4MTYgMTMuOTExNCA1LjAzNjM4IDEzLjgwOTEgNC44MzEzMSAxMy42OTZMNS4wODI3MiAxMS43OTUzQzUuMTEzNjUgMTEuNTYxNSA1LjAzMjc4IDExLjMyNjcgNC44NjQ0MiAxMS4xNjE1QzQuNjA3NjEgMTAuOTA5NiA0LjM4MTQ0IDEwLjYyNjggNC4xOTE5NSAxMC4zMTkyQzQuMDY4MzMgMTAuMTE4NiAzLjg1NzYyIDkuOTg3NzMgMy42MjI5OSA5Ljk2NTg3TDEuNzE0MzMgOS43ODgwNkMxLjY1MDMyIDkuNTYzNzkgMS41OTgwNCA5LjMzNDUxIDEuNTU4MjIgOS4xMDA5TDMuMjAwNCA4LjExMjc1QzMuNDAyNzkgNy45OTA5NiAzLjUzNTk5IDcuNzgwOTUgMy41NTk4NyA3LjU0NTk1QzMuNTk3IDcuMTgwNTggMy42Nzg0NyA2LjgyODggMy43OTg3MiA2LjQ5NTc4QzMuODc4ODQgNi4yNzM4NiAzLjg0OTg4IDYuMDI3MTggMy43MjA1MSA1LjgyOTg2TDIuNjcwNzYgNC4yMjg2NUMyLjgwNzU5IDQuMDM2OTMgMi45NTQ2IDMuODUyOTIgMy4xMTEgMy42Nzc0MUw0LjkwNjA1IDQuMzQ0NjlDNS4xMjc0IDQuNDI2OTcgNS4zNzQ1NyA0LjQwMDIgNS41NzMxNyA0LjI3MjQzQzUuODczOTQgNC4wNzg5MyA2LjE5OTM3IDMuOTIxMDEgNi41NDM1NyAzLjgwNDRDNi43NjcwNSAzLjcyODY5IDYuOTQxODcgMy41NTIyMyA3LjAxNTQ4IDMuMzI4MDVaIiBmaWxsPSIjNkY2RjZGIi8+CjwvZz4KPGRlZnM+CjxjbGlwUGF0aCBpZD0iY2xpcDBfMTMxMjNfMzUwMTkiPgo8cmVjdCB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9IndoaXRlIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==) gear icon and select **OpenSharing**.
    
    Alternatively, in the upper-right corner, click **Share > OpenSharing**.
    
3.  On the **Shared by me** tab, find the share you want to add a streaming table to and click its name.
    
4.  Click **Manage assets > Edit assets**.
    
5.  On the **Edit assets** page, search or browse for the streaming table that you want to share and select it.
    
6.  (Optional) In the **Alias** column, click ![Speech bubble plus icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTcuMjUgOS41VjcuNzVINS41VjYuMjVINy4yNVY0LjVIOC43NVY2LjI1SDEwLjVWNy43NUg4Ljc1VjkuNUg3LjI1WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTYgMUMyLjY4NjI5IDEgMCAzLjY4NjI5IDAgN1Y3LjI1QzAgMTAuMTcxNCAyLjE3ODczIDEyLjU4NCA1IDEyLjk1MTVWMTUuMjVDNSAxNS41NTMzIDUuMTgyNzMgMTUuODI2OCA1LjQ2Mjk5IDE1Ljk0MjlDNS43NDMyNCAxNi4wNTkgNi4wNjU4MyAxNS45OTQ4IDYuMjgwMzMgMTUuNzgwM0w5LjA2MDY2IDEzSDEwQzEzLjMxMzcgMTMgMTYgMTAuMzEzNyAxNiA3QzE2IDMuNjg2MjkgMTMuMzEzNyAxIDEwIDFINlpNMS41IDdDMS41IDQuNTE0NzIgMy41MTQ3MiAyLjUgNiAyLjVIMTBDMTIuNDg1MyAyLjUgMTQuNSA0LjUxNDcyIDE0LjUgN0MxNC41IDkuNDg1MjggMTIuNDg1MyAxMS41IDEwIDExLjVIOC43NUM4LjU1MTA5IDExLjUgOC4zNjAzMiAxMS41NzkgOC4yMTk2NyAxMS43MTk3TDYuNSAxMy40MzkzVjEyLjI1QzYuNSAxMS44MzU4IDYuMTY0MjEgMTEuNSA1Ljc1IDExLjVDMy40MDI3OSAxMS41IDEuNSA5LjU5NzIxIDEuNSA3LjI1VjdaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) to specify an alias, or alternate streaming table name, to make the streaming table name more readable. The alias is the name that the recipient sees and must use in queries. Recipients cannot use the actual streaming table name if an alias is specified.
    
7.  Click **Save**.
    

For information about removing streaming tables from a share, see [Update shares](https://docs.databricks.com/aws/en/delta-sharing/manage-share#update).

Apache Iceberg is an open source table format for analytics workloads. In Databricks, you can create [Iceberg tables](https://docs.databricks.com/aws/en/iceberg/) in Unity Catalog, known as [managed Iceberg tables](https://docs.databricks.com/aws/en/tables/managed).

Check that you meet the [requirements](https://docs.databricks.com/aws/en/delta-sharing/create-share#requirements) before adding managed Iceberg tables to a share. Iceberg table and managed Iceberg table limitations apply. See [Limitations](https://docs.databricks.com/aws/en/iceberg/#iceberg-limitations).

note

Databricks does not support sharing managed Iceberg tables to external Iceberg clients.

To add managed Iceberg tables to a share:

*   Catalog Explorer
*   SQL
*   CLI

1.  In your Databricks workspace, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
    
2.  At the top of the **Catalog** pane, click the ![Gear icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzEzMTIzXzM1MDE5KSI+CjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNNy45ODQzMyA1QzYuMzI3NDcgNSA0Ljk4NDMzIDYuMzQzMTUgNC45ODQzMyA4QzQuOTg0MzMgOS42NTY4NSA2LjMyNzQ3IDExIDcuOTg0MzMgMTFDOS42NDExOCAxMSAxMC45ODQzIDkuNjU2ODUgMTAuOTg0MyA4QzEwLjk4NDMgNi4zNDMxNSA5LjY0MTE4IDUgNy45ODQzMyA1Wk02LjQ4NDMzIDhDNi40ODQzMyA3LjE3MTU3IDcuMTU1OSA2LjUgNy45ODQzMyA2LjVDOC44MTI3NSA2LjUgOS40ODQzMyA3LjE3MTU3IDkuNDg0MzMgOEM5LjQ4NDMzIDguODI4NDMgOC44MTI3NSA5LjUgNy45ODQzMyA5LjVDNy4xNTU5IDkuNSA2LjQ4NDMzIDguODI4NDMgNi40ODQzMyA4WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTcuOTY1NSAwQzcuNjI1NTIgMCA3LjI5MDE0IDAuMDIxMjUxMSA2Ljk2MDcgMC4wNjI1NzM2QzYuNjczMDQgMC4wOTg2NTU4IDYuNDMxOTQgMC4yOTczIDYuMzQxNDggMC41NzI3NDVMNS43MDI0IDIuNTE4ODhDNS40OTI0NCAyLjYwNTY1IDUuMjg4NiAyLjcwNDExIDUuMDkxNyAyLjgxMzQxTDMuMTcxOTggMi4wOTk3OUMyLjkwMDU0IDEuOTk4ODggMi41OTUyNiAyLjA2MzI2IDIuMzg3NjkgMi4yNjUxOUMxLjkwNjkgMi43MzI4OSAxLjQ4NDY0IDMuMjYwNjggMS4xMzMwMSAzLjgzNjYxQzAuOTgxOTgyIDQuMDgzOTkgMC45ODcwMDYgNC4zOTYyNSAxLjE0NTkyIDQuNjM4NjRMMi4yNjkxOSA2LjM1MTk4QzIuMjA2OTIgNi41Njc1NyAyLjE1NjU2IDYuNzg4MTQgMi4xMTg4NSA3LjAxMjkzTDAuMzYzMzIyIDguMDY5MjhDMC4xMTU0ODMgOC4yMTg0MiAtMC4wMjQ1MDg2IDguNDk2NzggMC4wMDM1NDkyOSA4Ljc4NDY2QzAuMDcwMDUzNiA5LjQ2NzAyIDAuMjIyMzY1IDEwLjEyNDggMC40NDk2NjkgMTAuNzQ2NkMwLjU0OTA4NSAxMS4wMTg2IDAuNzk2MTg5IDExLjIwOSAxLjA4NDUxIDExLjIzNTlMMy4xMjY2NyAxMS40MjYxQzMuMjU3MzUgMTEuNjEwNCAzLjM5ODI2IDExLjc4NjggMy41NDg1OCAxMS45NTQ2TDMuMjc5NzQgMTMuOTg3MkMzLjI0MTggMTQuMjc0IDMuMzcyMjIgMTQuNTU3MSAzLjYxNDkgMTQuNzE0NkM0LjE3NDI3IDE1LjA3NzcgNC43ODIxNiAxNS4zNzMgNS40MjY4NiAxNS41ODg2QzUuNzAxNDcgMTUuNjgwNCA2LjAwNDQyIDE1LjYwNiA2LjIwNTE4IDE1LjM5NzNMNy42Mjc0MyAxMy45MTlDNy43MzkzOSAxMy45MjU0IDcuODUyMTEgMTMuOTI4NSA3Ljk2NTUxIDEzLjkyODVDOC4wNzg4OSAxMy45Mjg1IDguMTkxNiAxMy45MjU0IDguMzAzNTQgMTMuOTE5TDkuNzI1OCAxNS4zOTczQzkuOTI2NTYgMTUuNjA2IDEwLjIyOTUgMTUuNjgwNCAxMC41MDQxIDE1LjU4ODZDMTEuMTQ4OCAxNS4zNzMgMTEuNzU2NyAxNS4wNzc3IDEyLjMxNjEgMTQuNzE0NkMxMi41NTg4IDE0LjU1NzEgMTIuNjg5MiAxNC4yNzQgMTIuNjUxMiAxMy45ODcyTDEyLjM4MjQgMTEuOTU0N0MxMi41MzI3IDExLjc4NjkgMTIuNjczNyAxMS42MTA0IDEyLjgwNDMgMTEuNDI2MUwxNC44NDY1IDExLjIzNTlDMTUuMTM0OCAxMS4yMDkgMTUuMzgxOSAxMS4wMTg2IDE1LjQ4MTMgMTAuNzQ2NkMxNS43MDg2IDEwLjEyNDggMTUuODYwOSA5LjQ2NzA0IDE1LjkyNzUgOC43ODQ2OUMxNS45NTU1IDguNDk2OCAxNS44MTU1IDguMjE4NDQgMTUuNTY3NyA4LjA2OTNMMTMuODEyMiA3LjAxMjk2QzEzLjc3NDUgNi43ODgxNSAxMy43MjQxIDYuNTY3NTQgMTMuNjYxOCA2LjM1MTkzTDE0Ljc4NTEgNC42Mzg2MUMxNC45NDQgNC4zOTYyMiAxNC45NDkgNC4wODM5NiAxNC43OTggMy44MzY1OEMxNC40NDYzIDMuMjYwNjUgMTQuMDI0MSAyLjczMjg3IDEzLjU0MzMgMi4yNjUxOEMxMy4zMzU3IDIuMDYzMjUgMTMuMDMwNSAxLjk5ODg3IDEyLjc1OSAyLjA5OTc4TDEwLjgzOTMgMi44MTM0QzEwLjY0MjQgMi43MDQwOSAxMC40Mzg1IDIuNjA1NjMgMTAuMjI4NiAyLjUxODg1TDkuNTg5NDkgMC41NzI3NDFDOS40OTkwMyAwLjI5NzI5NCA5LjI1NzkzIDAuMDk4NjQ5NiA4Ljk3MDI2IDAuMDYyNTY4NkM4LjY0MDgzIDAuMDIxMjQ5NCA4LjMwNTQ4IDAgNy45NjU1IDBaTTcuMDE1NDggMy4zMjgwNUw3LjYxMjcxIDEuNTA5MzlDNy43Mjk0NiAxLjUwMzE2IDcuODQ3MDggMS41IDcuOTY1NSAxLjVDOC4wODM5MSAxLjUgOC4yMDE1MyAxLjUwMzE2IDguMzE4MjYgMS41MDkzOUw4LjkxNTQ4IDMuMzI4MDRDOC45ODkxIDMuNTUyMjEgOS4xNjM5MiAzLjcyODY4IDkuMzg3NCAzLjgwNDM4QzkuNzMxNjEgMy45MjA5OSAxMC4wNTcxIDQuMDc4OTIgMTAuMzU3OCA0LjI3MjQyQzEwLjU1NjQgNC40MDAxOSAxMC44MDM2IDQuNDI2OTYgMTEuMDI1IDQuMzQ0NjhMMTIuODIgMy42Nzc0QzEyLjk3NjQgMy44NTI5IDEzLjEyMzQgNC4wMzY5MSAxMy4yNjAyIDQuMjI4NjNMMTIuMjEwNSA1LjgyOTgyQzEyLjA4MTEgNi4wMjcxMyAxMi4wNTIyIDYuMjczODIgMTIuMTMyMyA2LjQ5NTc0QzEyLjI1MjUgNi44Mjg3OCAxMi4zMzQgNy4xODA1OCAxMi4zNzEyIDcuNTQ1OTdDMTIuMzk1IDcuNzgwOTcgMTIuNTI4MiA3Ljk5MDk5IDEyLjczMDYgOC4xMTI3N0wxNC4zNzI4IDkuMTAwOTJDMTQuMzMzIDkuMzM0NTIgMTQuMjgwNyA5LjU2Mzc5IDE0LjIxNjcgOS43ODgwNkwxMi4zMDggOS45NjU4N0MxMi4wNzM0IDkuOTg3NzMgMTEuODYyNyAxMC4xMTg2IDExLjczOTEgMTAuMzE5MkMxMS41NDk2IDEwLjYyNjggMTEuMzIzNCAxMC45MDk2IDExLjA2NjYgMTEuMTYxNkMxMC44OTgyIDExLjMyNjcgMTAuODE3MyAxMS41NjE1IDEwLjg0ODMgMTEuNzk1M0wxMS4wOTk3IDEzLjY5NkMxMC44OTQ2IDEzLjgwOTEgMTAuNjgyOCAxMy45MTE0IDEwLjQ2NTEgMTQuMDAyMkw5LjEzNTg0IDEyLjYyMDZDOC45NzI1MiAxMi40NTA5IDguNzM4OTQgMTIuMzY3NyA4LjUwNTA5IDEyLjM5NjFDOC4zMjg1MiAxMi40MTc1IDguMTQ4NDcgMTIuNDI4NSA3Ljk2NTUxIDEyLjQyODVDNy43ODI1MyAxMi40Mjg1IDcuNjAyNDcgMTIuNDE3NSA3LjQyNTg5IDEyLjM5NjFDNy4xOTIwNCAxMi4zNjc3IDYuOTU4NDYgMTIuNDUwOSA2Ljc5NTE0IDEyLjYyMDZMNS40NjU4OSAxNC4wMDIyQzUuMjQ4MTYgMTMuOTExNCA1LjAzNjM4IDEzLjgwOTEgNC44MzEzMSAxMy42OTZMNS4wODI3MiAxMS43OTUzQzUuMTEzNjUgMTEuNTYxNSA1LjAzMjc4IDExLjMyNjcgNC44NjQ0MiAxMS4xNjE1QzQuNjA3NjEgMTAuOTA5NiA0LjM4MTQ0IDEwLjYyNjggNC4xOTE5NSAxMC4zMTkyQzQuMDY4MzMgMTAuMTE4NiAzLjg1NzYyIDkuOTg3NzMgMy42MjI5OSA5Ljk2NTg3TDEuNzE0MzMgOS43ODgwNkMxLjY1MDMyIDkuNTYzNzkgMS41OTgwNCA5LjMzNDUxIDEuNTU4MjIgOS4xMDA5TDMuMjAwNCA4LjExMjc1QzMuNDAyNzkgNy45OTA5NiAzLjUzNTk5IDcuNzgwOTUgMy41NTk4NyA3LjU0NTk1QzMuNTk3IDcuMTgwNTggMy42Nzg0NyA2LjgyODggMy43OTg3MiA2LjQ5NTc4QzMuODc4ODQgNi4yNzM4NiAzLjg0OTg4IDYuMDI3MTggMy43MjA1MSA1LjgyOTg2TDIuNjcwNzYgNC4yMjg2NUMyLjgwNzU5IDQuMDM2OTMgMi45NTQ2IDMuODUyOTIgMy4xMTEgMy42Nzc0MUw0LjkwNjA1IDQuMzQ0NjlDNS4xMjc0IDQuNDI2OTcgNS4zNzQ1NyA0LjQwMDIgNS41NzMxNyA0LjI3MjQzQzUuODczOTQgNC4wNzg5MyA2LjE5OTM3IDMuOTIxMDEgNi41NDM1NyAzLjgwNDRDNi43NjcwNSAzLjcyODY5IDYuOTQxODcgMy41NTIyMyA3LjAxNTQ4IDMuMzI4MDVaIiBmaWxsPSIjNkY2RjZGIi8+CjwvZz4KPGRlZnM+CjxjbGlwUGF0aCBpZD0iY2xpcDBfMTMxMjNfMzUwMTkiPgo8cmVjdCB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9IndoaXRlIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==) gear icon and select **OpenSharing**.
    
    Alternatively, in the upper-right corner, click **Share > OpenSharing**.
    
3.  On the **Shared by me** tab, find the share you want to add a managed Iceberg table to and click its name.
    
4.  Click **Manage assets** > **Edit assets**.
    
5.  On the **Edit assets** page, search or browse for the managed Iceberg table that you want to share and select it.
    
6.  (Optional) In the **Alias** column, click ![Speech bubble plus icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTcuMjUgOS41VjcuNzVINS41VjYuMjVINy4yNVY0LjVIOC43NVY2LjI1SDEwLjVWNy43NUg4Ljc1VjkuNUg3LjI1WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTYgMUMyLjY4NjI5IDEgMCAzLjY4NjI5IDAgN1Y3LjI1QzAgMTAuMTcxNCAyLjE3ODczIDEyLjU4NCA1IDEyLjk1MTVWMTUuMjVDNSAxNS41NTMzIDUuMTgyNzMgMTUuODI2OCA1LjQ2Mjk5IDE1Ljk0MjlDNS43NDMyNCAxNi4wNTkgNi4wNjU4MyAxNS45OTQ4IDYuMjgwMzMgMTUuNzgwM0w5LjA2MDY2IDEzSDEwQzEzLjMxMzcgMTMgMTYgMTAuMzEzNyAxNiA3QzE2IDMuNjg2MjkgMTMuMzEzNyAxIDEwIDFINlpNMS41IDdDMS41IDQuNTE0NzIgMy41MTQ3MiAyLjUgNiAyLjVIMTBDMTIuNDg1MyAyLjUgMTQuNSA0LjUxNDcyIDE0LjUgN0MxNC41IDkuNDg1MjggMTIuNDg1MyAxMS41IDEwIDExLjVIOC43NUM4LjU1MTA5IDExLjUgOC4zNjAzMiAxMS41NzkgOC4yMTk2NyAxMS43MTk3TDYuNSAxMy40MzkzVjEyLjI1QzYuNSAxMS44MzU4IDYuMTY0MjEgMTEuNSA1Ljc1IDExLjVDMy40MDI3OSAxMS41IDEuNSA5LjU5NzIxIDEuNSA3LjI1VjdaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) to specify an alias, or alternate managed Iceberg table name, to make the name more readable. The alias is the name that the recipient sees and must use in queries. Recipients cannot use the actual managed Iceberg table name if an alias is specified.
    
7.  Click **Save**.
    

Lakehouse Federation enables you to use Databricks to run queries against external data sources. You can create foreign schemas and tables, which contain data and metadata managed by external systems, with Unity Catalog adding data governance to query these tables. To learn more about connecting to external sources, see [Connect to external databases and catalogs](https://docs.databricks.com/aws/en/query-federation/).

OpenSharing enables you to securely share foreign data from its original location, without copying data into Databricks, complex network setups, or credential transfers.

Check that you meet the [requirements](https://docs.databricks.com/aws/en/delta-sharing/create-share#requirements) before adding foreign schemas or tables to a share.

### Additional requirements[​](#additional-requirements-1 "Direct link to Additional requirements")

*   You must enable **Lakehouse Federation Sharing** in your account-level Previews. See [Manage Databricks previews](https://docs.databricks.com/aws/en/admin/workspace-settings/manage-previews).
    
*   You must enable **Serverless compute for workflows, notebooks, and Lakeflow Spark Declarative Pipelines** in the account where foreign schema or foreign table sharing is set up. See [Connect to serverless compute](https://docs.databricks.com/aws/en/compute/serverless/).
    
*   When sharing foreign schemas and tables, the data is queried and temporarily materialized on the provider's side. By default, the materialized data is stored in a hidden schema using Databricks [default storage](https://docs.databricks.com/aws/en/storage/default-storage). Verify that you meet the [requirements](https://docs.databricks.com/aws/en/storage/default-storage#requirements) and observe the [limitations](https://docs.databricks.com/aws/en/storage/default-storage#limitations) for default storage.
    
    For details about default storage regional availability, see [Serverless availability](https://docs.databricks.com/aws/en/resources/feature-region-support#serverless-aws).
    
    To opt out the use of Databricks default storage and use your own storage for temporary materialization, open a [support case](https://docs.databricks.com/aws/en/resources/support).
    
    important
    
    Foreign tables that are too large to materialize can't be shared. If materialization exceeds limits, the query fails.
    
*   If you choose to use default storage, you must enable the **OpenSharing for Default Storage – Expanded Access** preview at the account level. See [Manage Databricks previews](https://docs.databricks.com/aws/en/admin/workspace-settings/manage-previews).
    

### Limitations[​](#limitations-2 "Direct link to limitations-2")

*   Shared foreign tables don't support `LIMIT` clauses or predicate pushdown. The system fully materializes all query results before returning them to the recipient, regardless of query filters.

### Recommended usage patterns[​](#recommended-usage-patterns "Direct link to Recommended usage patterns")

Query results are generated on-demand for each query, so foreign table and schema sharing might not be as cost-efficient compared to sharing tables or materialized views. Databricks recommends the following to improve performance:

*   Keep the size of typical query results less than 10 GBs.
*   Use ad-hoc exploratory queries instead of frequent data dumps.
*   When using cloud-token sharing, consider sharing materialized views created on top of foreign tables for cost-efficiency and better performance.

To add foreign schemas or tables to a share, use Catalog Explorer, the Databricks Unity Catalog CLI, or SQL commands in a Databricks notebook or the Databricks SQL query editor.

*   Catalog Explorer
*   SQL
*   CLI

1.  In your Databricks workspace, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
    
2.  At the top of the **Catalog** pane, click the ![Gear icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzEzMTIzXzM1MDE5KSI+CjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNNy45ODQzMyA1QzYuMzI3NDcgNSA0Ljk4NDMzIDYuMzQzMTUgNC45ODQzMyA4QzQuOTg0MzMgOS42NTY4NSA2LjMyNzQ3IDExIDcuOTg0MzMgMTFDOS42NDExOCAxMSAxMC45ODQzIDkuNjU2ODUgMTAuOTg0MyA4QzEwLjk4NDMgNi4zNDMxNSA5LjY0MTE4IDUgNy45ODQzMyA1Wk02LjQ4NDMzIDhDNi40ODQzMyA3LjE3MTU3IDcuMTU1OSA2LjUgNy45ODQzMyA2LjVDOC44MTI3NSA2LjUgOS40ODQzMyA3LjE3MTU3IDkuNDg0MzMgOEM5LjQ4NDMzIDguODI4NDMgOC44MTI3NSA5LjUgNy45ODQzMyA5LjVDNy4xNTU5IDkuNSA2LjQ4NDMzIDguODI4NDMgNi40ODQzMyA4WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTcuOTY1NSAwQzcuNjI1NTIgMCA3LjI5MDE0IDAuMDIxMjUxMSA2Ljk2MDcgMC4wNjI1NzM2QzYuNjczMDQgMC4wOTg2NTU4IDYuNDMxOTQgMC4yOTczIDYuMzQxNDggMC41NzI3NDVMNS43MDI0IDIuNTE4ODhDNS40OTI0NCAyLjYwNTY1IDUuMjg4NiAyLjcwNDExIDUuMDkxNyAyLjgxMzQxTDMuMTcxOTggMi4wOTk3OUMyLjkwMDU0IDEuOTk4ODggMi41OTUyNiAyLjA2MzI2IDIuMzg3NjkgMi4yNjUxOUMxLjkwNjkgMi43MzI4OSAxLjQ4NDY0IDMuMjYwNjggMS4xMzMwMSAzLjgzNjYxQzAuOTgxOTgyIDQuMDgzOTkgMC45ODcwMDYgNC4zOTYyNSAxLjE0NTkyIDQuNjM4NjRMMi4yNjkxOSA2LjM1MTk4QzIuMjA2OTIgNi41Njc1NyAyLjE1NjU2IDYuNzg4MTQgMi4xMTg4NSA3LjAxMjkzTDAuMzYzMzIyIDguMDY5MjhDMC4xMTU0ODMgOC4yMTg0MiAtMC4wMjQ1MDg2IDguNDk2NzggMC4wMDM1NDkyOSA4Ljc4NDY2QzAuMDcwMDUzNiA5LjQ2NzAyIDAuMjIyMzY1IDEwLjEyNDggMC40NDk2NjkgMTAuNzQ2NkMwLjU0OTA4NSAxMS4wMTg2IDAuNzk2MTg5IDExLjIwOSAxLjA4NDUxIDExLjIzNTlMMy4xMjY2NyAxMS40MjYxQzMuMjU3MzUgMTEuNjEwNCAzLjM5ODI2IDExLjc4NjggMy41NDg1OCAxMS45NTQ2TDMuMjc5NzQgMTMuOTg3MkMzLjI0MTggMTQuMjc0IDMuMzcyMjIgMTQuNTU3MSAzLjYxNDkgMTQuNzE0NkM0LjE3NDI3IDE1LjA3NzcgNC43ODIxNiAxNS4zNzMgNS40MjY4NiAxNS41ODg2QzUuNzAxNDcgMTUuNjgwNCA2LjAwNDQyIDE1LjYwNiA2LjIwNTE4IDE1LjM5NzNMNy42Mjc0MyAxMy45MTlDNy43MzkzOSAxMy45MjU0IDcuODUyMTEgMTMuOTI4NSA3Ljk2NTUxIDEzLjkyODVDOC4wNzg4OSAxMy45Mjg1IDguMTkxNiAxMy45MjU0IDguMzAzNTQgMTMuOTE5TDkuNzI1OCAxNS4zOTczQzkuOTI2NTYgMTUuNjA2IDEwLjIyOTUgMTUuNjgwNCAxMC41MDQxIDE1LjU4ODZDMTEuMTQ4OCAxNS4zNzMgMTEuNzU2NyAxNS4wNzc3IDEyLjMxNjEgMTQuNzE0NkMxMi41NTg4IDE0LjU1NzEgMTIuNjg5MiAxNC4yNzQgMTIuNjUxMiAxMy45ODcyTDEyLjM4MjQgMTEuOTU0N0MxMi41MzI3IDExLjc4NjkgMTIuNjczNyAxMS42MTA0IDEyLjgwNDMgMTEuNDI2MUwxNC44NDY1IDExLjIzNTlDMTUuMTM0OCAxMS4yMDkgMTUuMzgxOSAxMS4wMTg2IDE1LjQ4MTMgMTAuNzQ2NkMxNS43MDg2IDEwLjEyNDggMTUuODYwOSA5LjQ2NzA0IDE1LjkyNzUgOC43ODQ2OUMxNS45NTU1IDguNDk2OCAxNS44MTU1IDguMjE4NDQgMTUuNTY3NyA4LjA2OTNMMTMuODEyMiA3LjAxMjk2QzEzLjc3NDUgNi43ODgxNSAxMy43MjQxIDYuNTY3NTQgMTMuNjYxOCA2LjM1MTkzTDE0Ljc4NTEgNC42Mzg2MUMxNC45NDQgNC4zOTYyMiAxNC45NDkgNC4wODM5NiAxNC43OTggMy44MzY1OEMxNC40NDYzIDMuMjYwNjUgMTQuMDI0MSAyLjczMjg3IDEzLjU0MzMgMi4yNjUxOEMxMy4zMzU3IDIuMDYzMjUgMTMuMDMwNSAxLjk5ODg3IDEyLjc1OSAyLjA5OTc4TDEwLjgzOTMgMi44MTM0QzEwLjY0MjQgMi43MDQwOSAxMC40Mzg1IDIuNjA1NjMgMTAuMjI4NiAyLjUxODg1TDkuNTg5NDkgMC41NzI3NDFDOS40OTkwMyAwLjI5NzI5NCA5LjI1NzkzIDAuMDk4NjQ5NiA4Ljk3MDI2IDAuMDYyNTY4NkM4LjY0MDgzIDAuMDIxMjQ5NCA4LjMwNTQ4IDAgNy45NjU1IDBaTTcuMDE1NDggMy4zMjgwNUw3LjYxMjcxIDEuNTA5MzlDNy43Mjk0NiAxLjUwMzE2IDcuODQ3MDggMS41IDcuOTY1NSAxLjVDOC4wODM5MSAxLjUgOC4yMDE1MyAxLjUwMzE2IDguMzE4MjYgMS41MDkzOUw4LjkxNTQ4IDMuMzI4MDRDOC45ODkxIDMuNTUyMjEgOS4xNjM5MiAzLjcyODY4IDkuMzg3NCAzLjgwNDM4QzkuNzMxNjEgMy45MjA5OSAxMC4wNTcxIDQuMDc4OTIgMTAuMzU3OCA0LjI3MjQyQzEwLjU1NjQgNC40MDAxOSAxMC44MDM2IDQuNDI2OTYgMTEuMDI1IDQuMzQ0NjhMMTIuODIgMy42Nzc0QzEyLjk3NjQgMy44NTI5IDEzLjEyMzQgNC4wMzY5MSAxMy4yNjAyIDQuMjI4NjNMMTIuMjEwNSA1LjgyOTgyQzEyLjA4MTEgNi4wMjcxMyAxMi4wNTIyIDYuMjczODIgMTIuMTMyMyA2LjQ5NTc0QzEyLjI1MjUgNi44Mjg3OCAxMi4zMzQgNy4xODA1OCAxMi4zNzEyIDcuNTQ1OTdDMTIuMzk1IDcuNzgwOTcgMTIuNTI4MiA3Ljk5MDk5IDEyLjczMDYgOC4xMTI3N0wxNC4zNzI4IDkuMTAwOTJDMTQuMzMzIDkuMzM0NTIgMTQuMjgwNyA5LjU2Mzc5IDE0LjIxNjcgOS43ODgwNkwxMi4zMDggOS45NjU4N0MxMi4wNzM0IDkuOTg3NzMgMTEuODYyNyAxMC4xMTg2IDExLjczOTEgMTAuMzE5MkMxMS41NDk2IDEwLjYyNjggMTEuMzIzNCAxMC45MDk2IDExLjA2NjYgMTEuMTYxNkMxMC44OTgyIDExLjMyNjcgMTAuODE3MyAxMS41NjE1IDEwLjg0ODMgMTEuNzk1M0wxMS4wOTk3IDEzLjY5NkMxMC44OTQ2IDEzLjgwOTEgMTAuNjgyOCAxMy45MTE0IDEwLjQ2NTEgMTQuMDAyMkw5LjEzNTg0IDEyLjYyMDZDOC45NzI1MiAxMi40NTA5IDguNzM4OTQgMTIuMzY3NyA4LjUwNTA5IDEyLjM5NjFDOC4zMjg1MiAxMi40MTc1IDguMTQ4NDcgMTIuNDI4NSA3Ljk2NTUxIDEyLjQyODVDNy43ODI1MyAxMi40Mjg1IDcuNjAyNDcgMTIuNDE3NSA3LjQyNTg5IDEyLjM5NjFDNy4xOTIwNCAxMi4zNjc3IDYuOTU4NDYgMTIuNDUwOSA2Ljc5NTE0IDEyLjYyMDZMNS40NjU4OSAxNC4wMDIyQzUuMjQ4MTYgMTMuOTExNCA1LjAzNjM4IDEzLjgwOTEgNC44MzEzMSAxMy42OTZMNS4wODI3MiAxMS43OTUzQzUuMTEzNjUgMTEuNTYxNSA1LjAzMjc4IDExLjMyNjcgNC44NjQ0MiAxMS4xNjE1QzQuNjA3NjEgMTAuOTA5NiA0LjM4MTQ0IDEwLjYyNjggNC4xOTE5NSAxMC4zMTkyQzQuMDY4MzMgMTAuMTE4NiAzLjg1NzYyIDkuOTg3NzMgMy42MjI5OSA5Ljk2NTg3TDEuNzE0MzMgOS43ODgwNkMxLjY1MDMyIDkuNTYzNzkgMS41OTgwNCA5LjMzNDUxIDEuNTU4MjIgOS4xMDA5TDMuMjAwNCA4LjExMjc1QzMuNDAyNzkgNy45OTA5NiAzLjUzNTk5IDcuNzgwOTUgMy41NTk4NyA3LjU0NTk1QzMuNTk3IDcuMTgwNTggMy42Nzg0NyA2LjgyODggMy43OTg3MiA2LjQ5NTc4QzMuODc4ODQgNi4yNzM4NiAzLjg0OTg4IDYuMDI3MTggMy43MjA1MSA1LjgyOTg2TDIuNjcwNzYgNC4yMjg2NUMyLjgwNzU5IDQuMDM2OTMgMi45NTQ2IDMuODUyOTIgMy4xMTEgMy42Nzc0MUw0LjkwNjA1IDQuMzQ0NjlDNS4xMjc0IDQuNDI2OTcgNS4zNzQ1NyA0LjQwMDIgNS41NzMxNyA0LjI3MjQzQzUuODczOTQgNC4wNzg5MyA2LjE5OTM3IDMuOTIxMDEgNi41NDM1NyAzLjgwNDRDNi43NjcwNSAzLjcyODY5IDYuOTQxODcgMy41NTIyMyA3LjAxNTQ4IDMuMzI4MDVaIiBmaWxsPSIjNkY2RjZGIi8+CjwvZz4KPGRlZnM+CjxjbGlwUGF0aCBpZD0iY2xpcDBfMTMxMjNfMzUwMTkiPgo8cmVjdCB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9IndoaXRlIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==) gear icon and select **OpenSharing**.
    
    Alternatively, in the upper-right corner, click **Share > OpenSharing**.
    
3.  On the **Shared by me** tab, find the share you want to add a foreign table or schema to and click its name.
    
4.  Click **Manage assets > Edit assets**.
    
5.  On the **Edit assets** page, search or browse for the foreign table or schema that you want to share and select it.
    
6.  (Optional) In the **Alias** column, click ![Speech bubble plus icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTcuMjUgOS41VjcuNzVINS41VjYuMjVINy4yNVY0LjVIOC43NVY2LjI1SDEwLjVWNy43NUg4Ljc1VjkuNUg3LjI1WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTYgMUMyLjY4NjI5IDEgMCAzLjY4NjI5IDAgN1Y3LjI1QzAgMTAuMTcxNCAyLjE3ODczIDEyLjU4NCA1IDEyLjk1MTVWMTUuMjVDNSAxNS41NTMzIDUuMTgyNzMgMTUuODI2OCA1LjQ2Mjk5IDE1Ljk0MjlDNS43NDMyNCAxNi4wNTkgNi4wNjU4MyAxNS45OTQ4IDYuMjgwMzMgMTUuNzgwM0w5LjA2MDY2IDEzSDEwQzEzLjMxMzcgMTMgMTYgMTAuMzEzNyAxNiA3QzE2IDMuNjg2MjkgMTMuMzEzNyAxIDEwIDFINlpNMS41IDdDMS41IDQuNTE0NzIgMy41MTQ3MiAyLjUgNiAyLjVIMTBDMTIuNDg1MyAyLjUgMTQuNSA0LjUxNDcyIDE0LjUgN0MxNC41IDkuNDg1MjggMTIuNDg1MyAxMS41IDEwIDExLjVIOC43NUM4LjU1MTA5IDExLjUgOC4zNjAzMiAxMS41NzkgOC4yMTk2NyAxMS43MTk3TDYuNSAxMy40MzkzVjEyLjI1QzYuNSAxMS44MzU4IDYuMTY0MjEgMTEuNSA1Ljc1IDExLjVDMy40MDI3OSAxMS41IDEuNSA5LjU5NzIxIDEuNSA3LjI1VjdaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) to specify an alias, or alternate foreign schema or table name, to make the foreign schema or table name more readable. The alias is the name that the recipient sees and must use in queries. Recipients cannot use the actual foreign schema or table name if an alias is specified.
    
7.  Click **Save**.
    

Foreign Iceberg tables are tables federated from foreign Iceberg catalogs using Lakehouse Federation. To learn more about Apache Iceberg tables in Databricks, see [What is Apache Iceberg in Databricks?](https://docs.databricks.com/aws/en/iceberg/).

Before you begin, check that you meet the general [requirements](#requirements) and [create a share](#create-a-share-object). You can also share foreign Iceberg tables to recipients using external Iceberg clients. For more information, see [Enable sharing to external Iceberg clients](#iceberg-clients).

note

To verify recipients receive the freshest data, periodically refresh your foreign Iceberg tables. Any `SELECT` query or `REFRESH TABLE` command refreshes the table metadata.

Databricks recommends setting up a scheduled job so the foreign Iceberg table on Databricks stays in sync with the remote Iceberg source. For more information about scheduling refreshes, see [Schedule a query](https://docs.databricks.com/aws/en/sql/user/queries/schedule-query).

### Additional requirements[​](#additional-requirements-2 "Direct link to additional-requirements-2")

*   You must enable the **Lakehouse Federation Sharing** preview at the account level. See [Manage Databricks previews](https://docs.databricks.com/aws/en/admin/workspace-settings/manage-previews).
*   If you are sharing foreign Iceberg tables with open recipients not using Iceberg clients, you must use [default storage](https://docs.databricks.com/aws/en/storage/default-storage). You must enable the **OpenSharing for Default Storage – Expanded Access** preview at the account level. See [Manage Databricks previews](https://docs.databricks.com/aws/en/admin/workspace-settings/manage-previews).
*   When sharing with open recipients not using Iceberg clients, the shared data is first filtered and materialized using your compute and storage. You might incur additional costs. For more information, see [How do I incur and check OpenSharing costs?](https://docs.databricks.com/aws/en/delta-sharing/#share-costs) and [Do recipients have direct access to the underlying data in shared views, materialized views, and streaming tables?](https://docs.databricks.com/aws/en/delta-sharing/#accessing-views).
*   Foreign Iceberg tables must have Delta Uniform enabled. If Uniform is not enabled, the table cannot be added to a share. See [Read Delta Lake tables with Iceberg clients](https://docs.databricks.com/aws/en/delta/uniform). ![Foreign Iceberg table with Delta Uniform Iceberg section in details tab.](https://docs.databricks.com/aws/en/assets/images/iceberg-delta-uniform-e8f7a8841409fa19d092ce3d3010967a.png)

### Limitations[​](#limitations-3 "Direct link to limitations-3")

*   Partitions aren't supported.
*   When sharing with open recipients not using an Iceberg client, `LIMIT` clauses and predicate pushdown aren't supported. The system fully materializes all query results before returning them to the recipient, regardless of query filters.

Foreign Iceberg tables are automatically shared with full history.

To add a foreign Iceberg table to a share:

*   Catalog Explorer
*   SQL
*   CLI

1.  In your Databricks workspace, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
    
2.  At the top of the **Catalog** pane, click the ![Gear icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzEzMTIzXzM1MDE5KSI+CjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNNy45ODQzMyA1QzYuMzI3NDcgNSA0Ljk4NDMzIDYuMzQzMTUgNC45ODQzMyA4QzQuOTg0MzMgOS42NTY4NSA2LjMyNzQ3IDExIDcuOTg0MzMgMTFDOS42NDExOCAxMSAxMC45ODQzIDkuNjU2ODUgMTAuOTg0MyA4QzEwLjk4NDMgNi4zNDMxNSA5LjY0MTE4IDUgNy45ODQzMyA1Wk02LjQ4NDMzIDhDNi40ODQzMyA3LjE3MTU3IDcuMTU1OSA2LjUgNy45ODQzMyA2LjVDOC44MTI3NSA2LjUgOS40ODQzMyA3LjE3MTU3IDkuNDg0MzMgOEM5LjQ4NDMzIDguODI4NDMgOC44MTI3NSA5LjUgNy45ODQzMyA5LjVDNy4xNTU5IDkuNSA2LjQ4NDMzIDguODI4NDMgNi40ODQzMyA4WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTcuOTY1NSAwQzcuNjI1NTIgMCA3LjI5MDE0IDAuMDIxMjUxMSA2Ljk2MDcgMC4wNjI1NzM2QzYuNjczMDQgMC4wOTg2NTU4IDYuNDMxOTQgMC4yOTczIDYuMzQxNDggMC41NzI3NDVMNS43MDI0IDIuNTE4ODhDNS40OTI0NCAyLjYwNTY1IDUuMjg4NiAyLjcwNDExIDUuMDkxNyAyLjgxMzQxTDMuMTcxOTggMi4wOTk3OUMyLjkwMDU0IDEuOTk4ODggMi41OTUyNiAyLjA2MzI2IDIuMzg3NjkgMi4yNjUxOUMxLjkwNjkgMi43MzI4OSAxLjQ4NDY0IDMuMjYwNjggMS4xMzMwMSAzLjgzNjYxQzAuOTgxOTgyIDQuMDgzOTkgMC45ODcwMDYgNC4zOTYyNSAxLjE0NTkyIDQuNjM4NjRMMi4yNjkxOSA2LjM1MTk4QzIuMjA2OTIgNi41Njc1NyAyLjE1NjU2IDYuNzg4MTQgMi4xMTg4NSA3LjAxMjkzTDAuMzYzMzIyIDguMDY5MjhDMC4xMTU0ODMgOC4yMTg0MiAtMC4wMjQ1MDg2IDguNDk2NzggMC4wMDM1NDkyOSA4Ljc4NDY2QzAuMDcwMDUzNiA5LjQ2NzAyIDAuMjIyMzY1IDEwLjEyNDggMC40NDk2NjkgMTAuNzQ2NkMwLjU0OTA4NSAxMS4wMTg2IDAuNzk2MTg5IDExLjIwOSAxLjA4NDUxIDExLjIzNTlMMy4xMjY2NyAxMS40MjYxQzMuMjU3MzUgMTEuNjEwNCAzLjM5ODI2IDExLjc4NjggMy41NDg1OCAxMS45NTQ2TDMuMjc5NzQgMTMuOTg3MkMzLjI0MTggMTQuMjc0IDMuMzcyMjIgMTQuNTU3MSAzLjYxNDkgMTQuNzE0NkM0LjE3NDI3IDE1LjA3NzcgNC43ODIxNiAxNS4zNzMgNS40MjY4NiAxNS41ODg2QzUuNzAxNDcgMTUuNjgwNCA2LjAwNDQyIDE1LjYwNiA2LjIwNTE4IDE1LjM5NzNMNy42Mjc0MyAxMy45MTlDNy43MzkzOSAxMy45MjU0IDcuODUyMTEgMTMuOTI4NSA3Ljk2NTUxIDEzLjkyODVDOC4wNzg4OSAxMy45Mjg1IDguMTkxNiAxMy45MjU0IDguMzAzNTQgMTMuOTE5TDkuNzI1OCAxNS4zOTczQzkuOTI2NTYgMTUuNjA2IDEwLjIyOTUgMTUuNjgwNCAxMC41MDQxIDE1LjU4ODZDMTEuMTQ4OCAxNS4zNzMgMTEuNzU2NyAxNS4wNzc3IDEyLjMxNjEgMTQuNzE0NkMxMi41NTg4IDE0LjU1NzEgMTIuNjg5MiAxNC4yNzQgMTIuNjUxMiAxMy45ODcyTDEyLjM4MjQgMTEuOTU0N0MxMi41MzI3IDExLjc4NjkgMTIuNjczNyAxMS42MTA0IDEyLjgwNDMgMTEuNDI2MUwxNC44NDY1IDExLjIzNTlDMTUuMTM0OCAxMS4yMDkgMTUuMzgxOSAxMS4wMTg2IDE1LjQ4MTMgMTAuNzQ2NkMxNS43MDg2IDEwLjEyNDggMTUuODYwOSA5LjQ2NzA0IDE1LjkyNzUgOC43ODQ2OUMxNS45NTU1IDguNDk2OCAxNS44MTU1IDguMjE4NDQgMTUuNTY3NyA4LjA2OTNMMTMuODEyMiA3LjAxMjk2QzEzLjc3NDUgNi43ODgxNSAxMy43MjQxIDYuNTY3NTQgMTMuNjYxOCA2LjM1MTkzTDE0Ljc4NTEgNC42Mzg2MUMxNC45NDQgNC4zOTYyMiAxNC45NDkgNC4wODM5NiAxNC43OTggMy44MzY1OEMxNC40NDYzIDMuMjYwNjUgMTQuMDI0MSAyLjczMjg3IDEzLjU0MzMgMi4yNjUxOEMxMy4zMzU3IDIuMDYzMjUgMTMuMDMwNSAxLjk5ODg3IDEyLjc1OSAyLjA5OTc4TDEwLjgzOTMgMi44MTM0QzEwLjY0MjQgMi43MDQwOSAxMC40Mzg1IDIuNjA1NjMgMTAuMjI4NiAyLjUxODg1TDkuNTg5NDkgMC41NzI3NDFDOS40OTkwMyAwLjI5NzI5NCA5LjI1NzkzIDAuMDk4NjQ5NiA4Ljk3MDI2IDAuMDYyNTY4NkM4LjY0MDgzIDAuMDIxMjQ5NCA4LjMwNTQ4IDAgNy45NjU1IDBaTTcuMDE1NDggMy4zMjgwNUw3LjYxMjcxIDEuNTA5MzlDNy43Mjk0NiAxLjUwMzE2IDcuODQ3MDggMS41IDcuOTY1NSAxLjVDOC4wODM5MSAxLjUgOC4yMDE1MyAxLjUwMzE2IDguMzE4MjYgMS41MDkzOUw4LjkxNTQ4IDMuMzI4MDRDOC45ODkxIDMuNTUyMjEgOS4xNjM5MiAzLjcyODY4IDkuMzg3NCAzLjgwNDM4QzkuNzMxNjEgMy45MjA5OSAxMC4wNTcxIDQuMDc4OTIgMTAuMzU3OCA0LjI3MjQyQzEwLjU1NjQgNC40MDAxOSAxMC44MDM2IDQuNDI2OTYgMTEuMDI1IDQuMzQ0NjhMMTIuODIgMy42Nzc0QzEyLjk3NjQgMy44NTI5IDEzLjEyMzQgNC4wMzY5MSAxMy4yNjAyIDQuMjI4NjNMMTIuMjEwNSA1LjgyOTgyQzEyLjA4MTEgNi4wMjcxMyAxMi4wNTIyIDYuMjczODIgMTIuMTMyMyA2LjQ5NTc0QzEyLjI1MjUgNi44Mjg3OCAxMi4zMzQgNy4xODA1OCAxMi4zNzEyIDcuNTQ1OTdDMTIuMzk1IDcuNzgwOTcgMTIuNTI4MiA3Ljk5MDk5IDEyLjczMDYgOC4xMTI3N0wxNC4zNzI4IDkuMTAwOTJDMTQuMzMzIDkuMzM0NTIgMTQuMjgwNyA5LjU2Mzc5IDE0LjIxNjcgOS43ODgwNkwxMi4zMDggOS45NjU4N0MxMi4wNzM0IDkuOTg3NzMgMTEuODYyNyAxMC4xMTg2IDExLjczOTEgMTAuMzE5MkMxMS41NDk2IDEwLjYyNjggMTEuMzIzNCAxMC45MDk2IDExLjA2NjYgMTEuMTYxNkMxMC44OTgyIDExLjMyNjcgMTAuODE3MyAxMS41NjE1IDEwLjg0ODMgMTEuNzk1M0wxMS4wOTk3IDEzLjY5NkMxMC44OTQ2IDEzLjgwOTEgMTAuNjgyOCAxMy45MTE0IDEwLjQ2NTEgMTQuMDAyMkw5LjEzNTg0IDEyLjYyMDZDOC45NzI1MiAxMi40NTA5IDguNzM4OTQgMTIuMzY3NyA4LjUwNTA5IDEyLjM5NjFDOC4zMjg1MiAxMi40MTc1IDguMTQ4NDcgMTIuNDI4NSA3Ljk2NTUxIDEyLjQyODVDNy43ODI1MyAxMi40Mjg1IDcuNjAyNDcgMTIuNDE3NSA3LjQyNTg5IDEyLjM5NjFDNy4xOTIwNCAxMi4zNjc3IDYuOTU4NDYgMTIuNDUwOSA2Ljc5NTE0IDEyLjYyMDZMNS40NjU4OSAxNC4wMDIyQzUuMjQ4MTYgMTMuOTExNCA1LjAzNjM4IDEzLjgwOTEgNC44MzEzMSAxMy42OTZMNS4wODI3MiAxMS43OTUzQzUuMTEzNjUgMTEuNTYxNSA1LjAzMjc4IDExLjMyNjcgNC44NjQ0MiAxMS4xNjE1QzQuNjA3NjEgMTAuOTA5NiA0LjM4MTQ0IDEwLjYyNjggNC4xOTE5NSAxMC4zMTkyQzQuMDY4MzMgMTAuMTE4NiAzLjg1NzYyIDkuOTg3NzMgMy42MjI5OSA5Ljk2NTg3TDEuNzE0MzMgOS43ODgwNkMxLjY1MDMyIDkuNTYzNzkgMS41OTgwNCA5LjMzNDUxIDEuNTU4MjIgOS4xMDA5TDMuMjAwNCA4LjExMjc1QzMuNDAyNzkgNy45OTA5NiAzLjUzNTk5IDcuNzgwOTUgMy41NTk4NyA3LjU0NTk1QzMuNTk3IDcuMTgwNTggMy42Nzg0NyA2LjgyODggMy43OTg3MiA2LjQ5NTc4QzMuODc4ODQgNi4yNzM4NiAzLjg0OTg4IDYuMDI3MTggMy43MjA1MSA1LjgyOTg2TDIuNjcwNzYgNC4yMjg2NUMyLjgwNzU5IDQuMDM2OTMgMi45NTQ2IDMuODUyOTIgMy4xMTEgMy42Nzc0MUw0LjkwNjA1IDQuMzQ0NjlDNS4xMjc0IDQuNDI2OTcgNS4zNzQ1NyA0LjQwMDIgNS41NzMxNyA0LjI3MjQzQzUuODczOTQgNC4wNzg5MyA2LjE5OTM3IDMuOTIxMDEgNi41NDM1NyAzLjgwNDRDNi43NjcwNSAzLjcyODY5IDYuOTQxODcgMy41NTIyMyA3LjAxNTQ4IDMuMzI4MDVaIiBmaWxsPSIjNkY2RjZGIi8+CjwvZz4KPGRlZnM+CjxjbGlwUGF0aCBpZD0iY2xpcDBfMTMxMjNfMzUwMTkiPgo8cmVjdCB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9IndoaXRlIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==) gear icon and select **OpenSharing**.
    
    Alternatively, in the upper-right corner, click **Share > OpenSharing**.
    
3.  On the **Shared by me** tab, find the share you want to add a foreign Iceberg table to and click its name.
    
4.  Click **Manage assets** > **Edit assets**.
    
5.  On the **Edit assets** page, search or browse for the foreign Iceberg table that you want to share and select it.
    
6.  (Optional) In the **Alias** column, click ![Speech bubble plus icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTcuMjUgOS41VjcuNzVINS41VjYuMjVINy4yNVY0LjVIOC43NVY2LjI1SDEwLjVWNy43NUg4Ljc1VjkuNUg3LjI1WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTYgMUMyLjY4NjI5IDEgMCAzLjY4NjI5IDAgN1Y3LjI1QzAgMTAuMTcxNCAyLjE3ODczIDEyLjU4NCA1IDEyLjk1MTVWMTUuMjVDNSAxNS41NTMzIDUuMTgyNzMgMTUuODI2OCA1LjQ2Mjk5IDE1Ljk0MjlDNS43NDMyNCAxNi4wNTkgNi4wNjU4MyAxNS45OTQ4IDYuMjgwMzMgMTUuNzgwM0w5LjA2MDY2IDEzSDEwQzEzLjMxMzcgMTMgMTYgMTAuMzEzNyAxNiA3QzE2IDMuNjg2MjkgMTMuMzEzNyAxIDEwIDFINlpNMS41IDdDMS41IDQuNTE0NzIgMy41MTQ3MiAyLjUgNiAyLjVIMTBDMTIuNDg1MyAyLjUgMTQuNSA0LjUxNDcyIDE0LjUgN0MxNC41IDkuNDg1MjggMTIuNDg1MyAxMS41IDEwIDExLjVIOC43NUM4LjU1MTA5IDExLjUgOC4zNjAzMiAxMS41NzkgOC4yMTk2NyAxMS43MTk3TDYuNSAxMy40MzkzVjEyLjI1QzYuNSAxMS44MzU4IDYuMTY0MjEgMTEuNSA1Ljc1IDExLjVDMy40MDI3OSAxMS41IDEuNSA5LjU5NzIxIDEuNSA3LjI1VjdaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) to specify an alias. The alias is the name that the recipient sees and must use in queries.
    
7.  Click **Save**.
    

Views are read-only objects created from one or more tables or other views. A view can be created from tables and other views that are contained in multiple schemas and catalogs in a Unity Catalog metastore. See [Create and manage views](https://docs.databricks.com/aws/en/views/create-views).

When sharing views, the data is queried and temporarily materialized. The materialized data is stored in the storage location of the view's parent schema or catalog, or in the metastore root location.

Check that you meet the [requirements](https://docs.databricks.com/aws/en/delta-sharing/create-share#requirements) before adding views to a share.

### Additional requirements[​](#additional-requirements-3 "Direct link to Additional requirements")

*   Shareable views must be defined on Delta tables, other shareable views, or local materialized views and streaming tables. Shareable views cannot be defined on foreign tables.
*   You must use a SQL warehouse or a compute on Databricks Runtime 13.3 LTS or above when you add a view to a share.
*   If your workspace has workspace-catalog bindings enabled, check that the workspace has read and write access to the catalog. For more information, see [Workspace-catalog binding](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/workspace-catalog-binding).
*   When sharing views, the data might be queried and temporarily materialized on the provider side, depending on the recipient's compute type and account relationship. The materialized data is stored in the storage location of the view's parent schema or catalog, or in the metastore root location. For details about when materialization occurs and who pays for it, see [Do recipients have direct access to the underlying data in shared views, materialized views, and streaming tables?](https://docs.databricks.com/aws/en/delta-sharing/#accessing-views) and [How do I incur and check OpenSharing costs?](https://docs.databricks.com/aws/en/delta-sharing/#share-costs).
*   If the storage location has custom network configurations, such as a firewall or private link, you must verify that your recipients are allowlisted to connect to the storage location. For instructions on configuring firewall rules for serverless compute, see [Serverless compute firewall configuration](https://docs.databricks.com/aws/en/security/network/serverless-network-security/serverless-firewall-config).

*   Alternatively, use [Share data behind a firewall with SecureConnect](https://docs.databricks.com/aws/en/delta-sharing/secureconnect-provider) to broker access without per-recipient allowlisting.

### Limitations[​](#limitations-4 "Direct link to limitations-4")

*   You cannot share views that reference shared tables or shared views.
*   You cannot share views that reference foreign tables, including foreign Iceberg tables.
*   If the recipient doesn't have direct access to the underlying data, `LIMIT` clauses and predicate pushdown aren't supported. The system fully materializes all query results before returning them to the recipient, regardless of query filters. See [Do recipients have direct access to the underlying data in shared views, materialized views, and streaming tables?](https://docs.databricks.com/aws/en/delta-sharing/#accessing-views).

This section describes how to add views to a share using Catalog Explorer, Databricks CLI, or SQL commands in a Databricks notebook or the Databricks SQL query editor. If you prefer to use the Unity Catalog REST API, see [PATCH /api/2.1/unity-catalog/shares/](https://docs.databricks.com/api/workspace/shares/update) in the REST API reference.

*   Catalog Explorer
*   SQL
*   CLI

1.  In your Databricks workspace, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
    
2.  At the top of the **Catalog** pane, click the ![Gear icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzEzMTIzXzM1MDE5KSI+CjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNNy45ODQzMyA1QzYuMzI3NDcgNSA0Ljk4NDMzIDYuMzQzMTUgNC45ODQzMyA4QzQuOTg0MzMgOS42NTY4NSA2LjMyNzQ3IDExIDcuOTg0MzMgMTFDOS42NDExOCAxMSAxMC45ODQzIDkuNjU2ODUgMTAuOTg0MyA4QzEwLjk4NDMgNi4zNDMxNSA5LjY0MTE4IDUgNy45ODQzMyA1Wk02LjQ4NDMzIDhDNi40ODQzMyA3LjE3MTU3IDcuMTU1OSA2LjUgNy45ODQzMyA2LjVDOC44MTI3NSA2LjUgOS40ODQzMyA3LjE3MTU3IDkuNDg0MzMgOEM5LjQ4NDMzIDguODI4NDMgOC44MTI3NSA5LjUgNy45ODQzMyA5LjVDNy4xNTU5IDkuNSA2LjQ4NDMzIDguODI4NDMgNi40ODQzMyA4WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTcuOTY1NSAwQzcuNjI1NTIgMCA3LjI5MDE0IDAuMDIxMjUxMSA2Ljk2MDcgMC4wNjI1NzM2QzYuNjczMDQgMC4wOTg2NTU4IDYuNDMxOTQgMC4yOTczIDYuMzQxNDggMC41NzI3NDVMNS43MDI0IDIuNTE4ODhDNS40OTI0NCAyLjYwNTY1IDUuMjg4NiAyLjcwNDExIDUuMDkxNyAyLjgxMzQxTDMuMTcxOTggMi4wOTk3OUMyLjkwMDU0IDEuOTk4ODggMi41OTUyNiAyLjA2MzI2IDIuMzg3NjkgMi4yNjUxOUMxLjkwNjkgMi43MzI4OSAxLjQ4NDY0IDMuMjYwNjggMS4xMzMwMSAzLjgzNjYxQzAuOTgxOTgyIDQuMDgzOTkgMC45ODcwMDYgNC4zOTYyNSAxLjE0NTkyIDQuNjM4NjRMMi4yNjkxOSA2LjM1MTk4QzIuMjA2OTIgNi41Njc1NyAyLjE1NjU2IDYuNzg4MTQgMi4xMTg4NSA3LjAxMjkzTDAuMzYzMzIyIDguMDY5MjhDMC4xMTU0ODMgOC4yMTg0MiAtMC4wMjQ1MDg2IDguNDk2NzggMC4wMDM1NDkyOSA4Ljc4NDY2QzAuMDcwMDUzNiA5LjQ2NzAyIDAuMjIyMzY1IDEwLjEyNDggMC40NDk2NjkgMTAuNzQ2NkMwLjU0OTA4NSAxMS4wMTg2IDAuNzk2MTg5IDExLjIwOSAxLjA4NDUxIDExLjIzNTlMMy4xMjY2NyAxMS40MjYxQzMuMjU3MzUgMTEuNjEwNCAzLjM5ODI2IDExLjc4NjggMy41NDg1OCAxMS45NTQ2TDMuMjc5NzQgMTMuOTg3MkMzLjI0MTggMTQuMjc0IDMuMzcyMjIgMTQuNTU3MSAzLjYxNDkgMTQuNzE0NkM0LjE3NDI3IDE1LjA3NzcgNC43ODIxNiAxNS4zNzMgNS40MjY4NiAxNS41ODg2QzUuNzAxNDcgMTUuNjgwNCA2LjAwNDQyIDE1LjYwNiA2LjIwNTE4IDE1LjM5NzNMNy42Mjc0MyAxMy45MTlDNy43MzkzOSAxMy45MjU0IDcuODUyMTEgMTMuOTI4NSA3Ljk2NTUxIDEzLjkyODVDOC4wNzg4OSAxMy45Mjg1IDguMTkxNiAxMy45MjU0IDguMzAzNTQgMTMuOTE5TDkuNzI1OCAxNS4zOTczQzkuOTI2NTYgMTUuNjA2IDEwLjIyOTUgMTUuNjgwNCAxMC41MDQxIDE1LjU4ODZDMTEuMTQ4OCAxNS4zNzMgMTEuNzU2NyAxNS4wNzc3IDEyLjMxNjEgMTQuNzE0NkMxMi41NTg4IDE0LjU1NzEgMTIuNjg5MiAxNC4yNzQgMTIuNjUxMiAxMy45ODcyTDEyLjM4MjQgMTEuOTU0N0MxMi41MzI3IDExLjc4NjkgMTIuNjczNyAxMS42MTA0IDEyLjgwNDMgMTEuNDI2MUwxNC44NDY1IDExLjIzNTlDMTUuMTM0OCAxMS4yMDkgMTUuMzgxOSAxMS4wMTg2IDE1LjQ4MTMgMTAuNzQ2NkMxNS43MDg2IDEwLjEyNDggMTUuODYwOSA5LjQ2NzA0IDE1LjkyNzUgOC43ODQ2OUMxNS45NTU1IDguNDk2OCAxNS44MTU1IDguMjE4NDQgMTUuNTY3NyA4LjA2OTNMMTMuODEyMiA3LjAxMjk2QzEzLjc3NDUgNi43ODgxNSAxMy43MjQxIDYuNTY3NTQgMTMuNjYxOCA2LjM1MTkzTDE0Ljc4NTEgNC42Mzg2MUMxNC45NDQgNC4zOTYyMiAxNC45NDkgNC4wODM5NiAxNC43OTggMy44MzY1OEMxNC40NDYzIDMuMjYwNjUgMTQuMDI0MSAyLjczMjg3IDEzLjU0MzMgMi4yNjUxOEMxMy4zMzU3IDIuMDYzMjUgMTMuMDMwNSAxLjk5ODg3IDEyLjc1OSAyLjA5OTc4TDEwLjgzOTMgMi44MTM0QzEwLjY0MjQgMi43MDQwOSAxMC40Mzg1IDIuNjA1NjMgMTAuMjI4NiAyLjUxODg1TDkuNTg5NDkgMC41NzI3NDFDOS40OTkwMyAwLjI5NzI5NCA5LjI1NzkzIDAuMDk4NjQ5NiA4Ljk3MDI2IDAuMDYyNTY4NkM4LjY0MDgzIDAuMDIxMjQ5NCA4LjMwNTQ4IDAgNy45NjU1IDBaTTcuMDE1NDggMy4zMjgwNUw3LjYxMjcxIDEuNTA5MzlDNy43Mjk0NiAxLjUwMzE2IDcuODQ3MDggMS41IDcuOTY1NSAxLjVDOC4wODM5MSAxLjUgOC4yMDE1MyAxLjUwMzE2IDguMzE4MjYgMS41MDkzOUw4LjkxNTQ4IDMuMzI4MDRDOC45ODkxIDMuNTUyMjEgOS4xNjM5MiAzLjcyODY4IDkuMzg3NCAzLjgwNDM4QzkuNzMxNjEgMy45MjA5OSAxMC4wNTcxIDQuMDc4OTIgMTAuMzU3OCA0LjI3MjQyQzEwLjU1NjQgNC40MDAxOSAxMC44MDM2IDQuNDI2OTYgMTEuMDI1IDQuMzQ0NjhMMTIuODIgMy42Nzc0QzEyLjk3NjQgMy44NTI5IDEzLjEyMzQgNC4wMzY5MSAxMy4yNjAyIDQuMjI4NjNMMTIuMjEwNSA1LjgyOTgyQzEyLjA4MTEgNi4wMjcxMyAxMi4wNTIyIDYuMjczODIgMTIuMTMyMyA2LjQ5NTc0QzEyLjI1MjUgNi44Mjg3OCAxMi4zMzQgNy4xODA1OCAxMi4zNzEyIDcuNTQ1OTdDMTIuMzk1IDcuNzgwOTcgMTIuNTI4MiA3Ljk5MDk5IDEyLjczMDYgOC4xMTI3N0wxNC4zNzI4IDkuMTAwOTJDMTQuMzMzIDkuMzM0NTIgMTQuMjgwNyA5LjU2Mzc5IDE0LjIxNjcgOS43ODgwNkwxMi4zMDggOS45NjU4N0MxMi4wNzM0IDkuOTg3NzMgMTEuODYyNyAxMC4xMTg2IDExLjczOTEgMTAuMzE5MkMxMS41NDk2IDEwLjYyNjggMTEuMzIzNCAxMC45MDk2IDExLjA2NjYgMTEuMTYxNkMxMC44OTgyIDExLjMyNjcgMTAuODE3MyAxMS41NjE1IDEwLjg0ODMgMTEuNzk1M0wxMS4wOTk3IDEzLjY5NkMxMC44OTQ2IDEzLjgwOTEgMTAuNjgyOCAxMy45MTE0IDEwLjQ2NTEgMTQuMDAyMkw5LjEzNTg0IDEyLjYyMDZDOC45NzI1MiAxMi40NTA5IDguNzM4OTQgMTIuMzY3NyA4LjUwNTA5IDEyLjM5NjFDOC4zMjg1MiAxMi40MTc1IDguMTQ4NDcgMTIuNDI4NSA3Ljk2NTUxIDEyLjQyODVDNy43ODI1MyAxMi40Mjg1IDcuNjAyNDcgMTIuNDE3NSA3LjQyNTg5IDEyLjM5NjFDNy4xOTIwNCAxMi4zNjc3IDYuOTU4NDYgMTIuNDUwOSA2Ljc5NTE0IDEyLjYyMDZMNS40NjU4OSAxNC4wMDIyQzUuMjQ4MTYgMTMuOTExNCA1LjAzNjM4IDEzLjgwOTEgNC44MzEzMSAxMy42OTZMNS4wODI3MiAxMS43OTUzQzUuMTEzNjUgMTEuNTYxNSA1LjAzMjc4IDExLjMyNjcgNC44NjQ0MiAxMS4xNjE1QzQuNjA3NjEgMTAuOTA5NiA0LjM4MTQ0IDEwLjYyNjggNC4xOTE5NSAxMC4zMTkyQzQuMDY4MzMgMTAuMTE4NiAzLjg1NzYyIDkuOTg3NzMgMy42MjI5OSA5Ljk2NTg3TDEuNzE0MzMgOS43ODgwNkMxLjY1MDMyIDkuNTYzNzkgMS41OTgwNCA5LjMzNDUxIDEuNTU4MjIgOS4xMDA5TDMuMjAwNCA4LjExMjc1QzMuNDAyNzkgNy45OTA5NiAzLjUzNTk5IDcuNzgwOTUgMy41NTk4NyA3LjU0NTk1QzMuNTk3IDcuMTgwNTggMy42Nzg0NyA2LjgyODggMy43OTg3MiA2LjQ5NTc4QzMuODc4ODQgNi4yNzM4NiAzLjg0OTg4IDYuMDI3MTggMy43MjA1MSA1LjgyOTg2TDIuNjcwNzYgNC4yMjg2NUMyLjgwNzU5IDQuMDM2OTMgMi45NTQ2IDMuODUyOTIgMy4xMTEgMy42Nzc0MUw0LjkwNjA1IDQuMzQ0NjlDNS4xMjc0IDQuNDI2OTcgNS4zNzQ1NyA0LjQwMDIgNS41NzMxNyA0LjI3MjQzQzUuODczOTQgNC4wNzg5MyA2LjE5OTM3IDMuOTIxMDEgNi41NDM1NyAzLjgwNDRDNi43NjcwNSAzLjcyODY5IDYuOTQxODcgMy41NTIyMyA3LjAxNTQ4IDMuMzI4MDVaIiBmaWxsPSIjNkY2RjZGIi8+CjwvZz4KPGRlZnM+CjxjbGlwUGF0aCBpZD0iY2xpcDBfMTMxMjNfMzUwMTkiPgo8cmVjdCB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9IndoaXRlIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==) gear icon and select **OpenSharing**.
    
    Alternatively, in the upper-right corner, click **Share > OpenSharing**.
    
3.  On the **Shared by me** tab, find the share you want to add a view to and click its name.
    
4.  Click **Manage assets > Add data assets**.
    
5.  On the **Add tables** page, search or browse for the view that you want to share and select it.
    
6.  (Optional) Click ![Speech bubble plus icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTcuMjUgOS41VjcuNzVINS41VjYuMjVINy4yNVY0LjVIOC43NVY2LjI1SDEwLjVWNy43NUg4Ljc1VjkuNUg3LjI1WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTYgMUMyLjY4NjI5IDEgMCAzLjY4NjI5IDAgN1Y3LjI1QzAgMTAuMTcxNCAyLjE3ODczIDEyLjU4NCA1IDEyLjk1MTVWMTUuMjVDNSAxNS41NTMzIDUuMTgyNzMgMTUuODI2OCA1LjQ2Mjk5IDE1Ljk0MjlDNS43NDMyNCAxNi4wNTkgNi4wNjU4MyAxNS45OTQ4IDYuMjgwMzMgMTUuNzgwM0w5LjA2MDY2IDEzSDEwQzEzLjMxMzcgMTMgMTYgMTAuMzEzNyAxNiA3QzE2IDMuNjg2MjkgMTMuMzEzNyAxIDEwIDFINlpNMS41IDdDMS41IDQuNTE0NzIgMy41MTQ3MiAyLjUgNiAyLjVIMTBDMTIuNDg1MyAyLjUgMTQuNSA0LjUxNDcyIDE0LjUgN0MxNC41IDkuNDg1MjggMTIuNDg1MyAxMS41IDEwIDExLjVIOC43NUM4LjU1MTA5IDExLjUgOC4zNjAzMiAxMS41NzkgOC4yMTk2NyAxMS43MTk3TDYuNSAxMy40MzkzVjEyLjI1QzYuNSAxMS44MzU4IDYuMTY0MjEgMTEuNSA1Ljc1IDExLjVDMy40MDI3OSAxMS41IDEuNSA5LjU5NzIxIDEuNSA3LjI1VjdaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) under the **Alias** column to specify an alternate view name, or **Alias**, to make the view name more readable. The alias is the name that the recipient sees and must use in queries. Recipients cannot use the actual view name if an alias is specified.
    
7.  Click **Save**.
    

For information about removing views from a share, see [Update shares](https://docs.databricks.com/aws/en/delta-sharing/manage-share#update).

You can use dynamic views to configure fine-grained access control to table data, including:

*   Security at the level of columns or rows.
*   Data masking.

When you create a dynamic view that uses the [CURRENT\_RECIPIENT() function](https://docs.databricks.com/aws/en/sql/language-manual/functions/current_recipient), you can limit recipient access according to properties that you specify in the recipient definition.

This section provides examples of restricting recipient access to table data at both the row and column level using a dynamic view.

### Requirements[​](#requirements-1 "Direct link to Requirements")

*   Check that you meet the [requirements](https://docs.databricks.com/aws/en/delta-sharing/create-share#requirements) for adding a view to a share.
*   **Databricks Runtime version**: The `CURRENT_RECIPIENT` function is supported in Databricks Runtime 14.2 and above.

### Limitations[​](#limitations-5 "Direct link to Limitations")

*   All limitations for [view sharing](#views) apply.
*   When a provide
