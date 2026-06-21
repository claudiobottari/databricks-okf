---
title: Read data shared using Databricks-to-Databricks OpenSharing (for recipients) | Databricks on AWS
source: https://docs.databricks.com/aws/en/delta-sharing/read-data-databricks
ingestedAt: "2026-06-18T08:05:35.086Z"
---

This page describes how to read data shared with you using the _Databricks-to-Databricks_ OpenSharing protocol, where Databricks manages a secure connection for data sharing. Unlike the OpenSharing _open sharing_ protocol, the Databricks-to-Databricks protocol does not require a credential file (token-based security).

Databricks-to-Databricks sharing requires that you, as the recipient, meet _both_ of the following requirements:

*   You have access to a Databricks workspace that is [enabled for Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/enable-workspaces).
*   The provider is using the _Databricks-to-Databricks_ OpenSharing protocol, not the Databricks-to-Open sharing protocol, which provides you with a credential file.

If either requirement is not met, see [Read data shared using OpenSharing Databricks-to-Open sharing with bearer tokens](https://docs.databricks.com/aws/en/delta-sharing/read-data-open).

To read data and notebooks that have been shared with you using the Databricks-to-Databricks protocol, you must be a user on a Databricks workspace that is enabled for [Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/). A member of your team gives the data provider a unique identifier for your Unity Catalog metastore, and the data provider uses that identifier to create a secure sharing connection with your organization. The shared data then becomes available for read access in your workspace. Updates the data provider makes to the shared tables, views, volumes, and partitions are reflected in your workspace in near real time.

note

Column changes, such as adding, renaming, or deleting, may not appear in Catalog Explorer for up to one minute. Likewise, new shares and updates to shares, including adding new tables, are cached for one minute before they are available for you to view and query.

note

The tables in `information_schema` from a shared catalog reflect metadata stored in Unity Catalog. This metadata is updated from the provider only when you query the shared table directly or run a command such as [DESCRIBE](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-aux-describe-table) or [REFRESH FOREIGN](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-refresh-foreign). Until then, `information_schema` might appear stale compared to the provider's data.

To read data that has been shared with you:

1.  A user on your team finds the _share_—the container for the tables, views, volumes, and notebooks that have been shared with you—and uses that share to create a _catalog_—the top-level container for all data in Databricks Unity Catalog.
2.  A user on your team grants or denies access to the catalog and the objects inside the catalog (schemas, tables, views, and volumes) to members of your team.
3.  You read the data in the tables, views, and volumes that you have been granted access to like any data asset in Databricks that you have read-only (`SELECT` or `READ VOLUME`) access to.
4.  You can preview and clone notebooks in the share, as long as you have the `USE CATALOG` privilege on the catalog.

## Permissions required[​](#permissions-required "Direct link to permissions-required")

To be able to list and view details about all providers and provider shares, you must have the `USE PROVIDER` privilege. Other users have access only to the providers and shares that they own.

To create a catalog from a provider share, you must be a metastore admin, a user who has both the `CREATE CATALOG` and `USE PROVIDER` privileges for your Unity Catalog metastore, or a user who has both the `CREATE CATALOG` privilege and ownership of the provider object.

The ability to grant read-only access to the schemas (databases), tables, views, and volumes in the catalog created from the share follows the typical Unity Catalog privilege hierarchy. The ability to view notebooks in the catalog created from the share requires the `USE CATALOG` privilege on the catalog. See [Manage permissions for the schemas, tables, and volumes in an OpenSharing catalog](#schema-table-permissions).

To read data in a shared table or volume:

1.  A privileged user must create a catalog from the share that contains the table or volume. This can be a metastore admin, a user who has both the `CREATE CATALOG` and `USE PROVIDER` privileges for your Unity Catalog metastore, or a user who has both the `CREATE CATALOG` privilege and ownership of the provider object.
2.  That user or a user with the same privileges must grant you access to the shared table or volume.
3.  You can access the table or volume just as you would any other data asset registered in your Unity Catalog metastore.

To make the data in a share accessible to your team, you must create a catalog from the share or mount the share to an existing shared catalog. To create a catalog from a share, you can use Catalog Explorer, the Databricks Unity Catalog CLI, or SQL commands in a Databricks notebook or the Databricks SQL query editor. To mount the share to an existing shared catalog, you can use the Catalog Explorer.

**Permissions required to create a catalog**: A metastore admin, a user who has both the `CREATE CATALOG` and `USE PROVIDER` privileges for your Unity Catalog metastore, or a user who has both the `CREATE CATALOG` privilege and ownership of the provider object.

**Permissions required to mount share to an existing catalog**: A user must have the `USE PROVIDER` privilege or have ownership of the provider object, and must also either own the existing shared catalog or have both `MANAGE` and `USE CATALOG` privileges on the existing shared catalog.

**Limitations:** If you want to add a data product from [SAP Business Data Cloud (BDC)](https://docs.databricks.com/aws/en/delta-sharing/sap-bdc/#what-is), serverless compute or Databricks Runtime 15 or above is required.

note

If you are creating a catalog from an [SAP BDC](https://docs.databricks.com/aws/en/delta-sharing/sap-bdc/) share, SAP semantic metadata (table and column comments, primary keys, foreign keys, and governance tags) syncs automatically into the catalog. No additional action is required. For details, see [SAP BDC semantic metadata](https://docs.databricks.com/aws/en/delta-sharing/sap-bdc/semantic-metadata).

note

If the share includes views, you must use a catalog name that is different than the name of the catalog that contains the view in the provider's metastore.

*   Catalog Explorer
*   SQL
*   CLI

1.  In your Databricks workspace, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog** to open Catalog Explorer.
    
2.  At the top of the **Catalog** pane, click the ![Gear icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzEzMTIzXzM1MDE5KSI+CjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNNy45ODQzMyA1QzYuMzI3NDcgNSA0Ljk4NDMzIDYuMzQzMTUgNC45ODQzMyA4QzQuOTg0MzMgOS42NTY4NSA2LjMyNzQ3IDExIDcuOTg0MzMgMTFDOS42NDExOCAxMSAxMC45ODQzIDkuNjU2ODUgMTAuOTg0MyA4QzEwLjk4NDMgNi4zNDMxNSA5LjY0MTE4IDUgNy45ODQzMyA1Wk02LjQ4NDMzIDhDNi40ODQzMyA3LjE3MTU3IDcuMTU1OSA2LjUgNy45ODQzMyA2LjVDOC44MTI3NSA2LjUgOS40ODQzMyA3LjE3MTU3IDkuNDg0MzMgOEM5LjQ4NDMzIDguODI4NDMgOC44MTI3NSA5LjUgNy45ODQzMyA5LjVDNy4xNTU5IDkuNSA2LjQ4NDMzIDguODI4NDMgNi40ODQzMyA4WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTcuOTY1NSAwQzcuNjI1NTIgMCA3LjI5MDE0IDAuMDIxMjUxMSA2Ljk2MDcgMC4wNjI1NzM2QzYuNjczMDQgMC4wOTg2NTU4IDYuNDMxOTQgMC4yOTczIDYuMzQxNDggMC41NzI3NDVMNS43MDI0IDIuNTE4ODhDNS40OTI0NCAyLjYwNTY1IDUuMjg4NiAyLjcwNDExIDUuMDkxNyAyLjgxMzQxTDMuMTcxOTggMi4wOTk3OUMyLjkwMDU0IDEuOTk4ODggMi41OTUyNiAyLjA2MzI2IDIuMzg3NjkgMi4yNjUxOUMxLjkwNjkgMi43MzI4OSAxLjQ4NDY0IDMuMjYwNjggMS4xMzMwMSAzLjgzNjYxQzAuOTgxOTgyIDQuMDgzOTkgMC45ODcwMDYgNC4zOTYyNSAxLjE0NTkyIDQuNjM4NjRMMi4yNjkxOSA2LjM1MTk4QzIuMjA2OTIgNi41Njc1NyAyLjE1NjU2IDYuNzg4MTQgMi4xMTg4NSA3LjAxMjkzTDAuMzYzMzIyIDguMDY5MjhDMC4xMTU0ODMgOC4yMTg0MiAtMC4wMjQ1MDg2IDguNDk2NzggMC4wMDM1NDkyOSA4Ljc4NDY2QzAuMDcwMDUzNiA5LjQ2NzAyIDAuMjIyMzY1IDEwLjEyNDggMC40NDk2NjkgMTAuNzQ2NkMwLjU0OTA4NSAxMS4wMTg2IDAuNzk2MTg5IDExLjIwOSAxLjA4NDUxIDExLjIzNTlMMy4xMjY2NyAxMS40MjYxQzMuMjU3MzUgMTEuNjEwNCAzLjM5ODI2IDExLjc4NjggMy41NDg1OCAxMS45NTQ2TDMuMjc5NzQgMTMuOTg3MkMzLjI0MTggMTQuMjc0IDMuMzcyMjIgMTQuNTU3MSAzLjYxNDkgMTQuNzE0NkM0LjE3NDI3IDE1LjA3NzcgNC43ODIxNiAxNS4zNzMgNS40MjY4NiAxNS41ODg2QzUuNzAxNDcgMTUuNjgwNCA2LjAwNDQyIDE1LjYwNiA2LjIwNTE4IDE1LjM5NzNMNy42Mjc0MyAxMy45MTlDNy43MzkzOSAxMy45MjU0IDcuODUyMTEgMTMuOTI4NSA3Ljk2NTUxIDEzLjkyODVDOC4wNzg4OSAxMy45Mjg1IDguMTkxNiAxMy45MjU0IDguMzAzNTQgMTMuOTE5TDkuNzI1OCAxNS4zOTczQzkuOTI2NTYgMTUuNjA2IDEwLjIyOTUgMTUuNjgwNCAxMC41MDQxIDE1LjU4ODZDMTEuMTQ4OCAxNS4zNzMgMTEuNzU2NyAxNS4wNzc3IDEyLjMxNjEgMTQuNzE0NkMxMi41NTg4IDE0LjU1NzEgMTIuNjg5MiAxNC4yNzQgMTIuNjUxMiAxMy45ODcyTDEyLjM4MjQgMTEuOTU0N0MxMi41MzI3IDExLjc4NjkgMTIuNjczNyAxMS42MTA0IDEyLjgwNDMgMTEuNDI2MUwxNC44NDY1IDExLjIzNTlDMTUuMTM0OCAxMS4yMDkgMTUuMzgxOSAxMS4wMTg2IDE1LjQ4MTMgMTAuNzQ2NkMxNS43MDg2IDEwLjEyNDggMTUuODYwOSA5LjQ2NzA0IDE1LjkyNzUgOC43ODQ2OUMxNS45NTU1IDguNDk2OCAxNS44MTU1IDguMjE4NDQgMTUuNTY3NyA4LjA2OTNMMTMuODEyMiA3LjAxMjk2QzEzLjc3NDUgNi43ODgxNSAxMy43MjQxIDYuNTY3NTQgMTMuNjYxOCA2LjM1MTkzTDE0Ljc4NTEgNC42Mzg2MUMxNC45NDQgNC4zOTYyMiAxNC45NDkgNC4wODM5NiAxNC43OTggMy44MzY1OEMxNC40NDYzIDMuMjYwNjUgMTQuMDI0MSAyLjczMjg3IDEzLjU0MzMgMi4yNjUxOEMxMy4zMzU3IDIuMDYzMjUgMTMuMDMwNSAxLjk5ODg3IDEyLjc1OSAyLjA5OTc4TDEwLjgzOTMgMi44MTM0QzEwLjY0MjQgMi43MDQwOSAxMC40Mzg1IDIuNjA1NjMgMTAuMjI4NiAyLjUxODg1TDkuNTg5NDkgMC41NzI3NDFDOS40OTkwMyAwLjI5NzI5NCA5LjI1NzkzIDAuMDk4NjQ5NiA4Ljk3MDI2IDAuMDYyNTY4NkM4LjY0MDgzIDAuMDIxMjQ5NCA4LjMwNTQ4IDAgNy45NjU1IDBaTTcuMDE1NDggMy4zMjgwNUw3LjYxMjcxIDEuNTA5MzlDNy43Mjk0NiAxLjUwMzE2IDcuODQ3MDggMS41IDcuOTY1NSAxLjVDOC4wODM5MSAxLjUgOC4yMDE1MyAxLjUwMzE2IDguMzE4MjYgMS41MDkzOUw4LjkxNTQ4IDMuMzI4MDRDOC45ODkxIDMuNTUyMjEgOS4xNjM5MiAzLjcyODY4IDkuMzg3NCAzLjgwNDM4QzkuNzMxNjEgMy45MjA5OSAxMC4wNTcxIDQuMDc4OTIgMTAuMzU3OCA0LjI3MjQyQzEwLjU1NjQgNC40MDAxOSAxMC44MDM2IDQuNDI2OTYgMTEuMDI1IDQuMzQ0NjhMMTIuODIgMy42Nzc0QzEyLjk3NjQgMy44NTI5IDEzLjEyMzQgNC4wMzY5MSAxMy4yNjAyIDQuMjI4NjNMMTIuMjEwNSA1LjgyOTgyQzEyLjA4MTEgNi4wMjcxMyAxMi4wNTIyIDYuMjczODIgMTIuMTMyMyA2LjQ5NTc0QzEyLjI1MjUgNi44Mjg3OCAxMi4zMzQgNy4xODA1OCAxMi4zNzEyIDcuNTQ1OTdDMTIuMzk1IDcuNzgwOTcgMTIuNTI4MiA3Ljk5MDk5IDEyLjczMDYgOC4xMTI3N0wxNC4zNzI4IDkuMTAwOTJDMTQuMzMzIDkuMzM0NTIgMTQuMjgwNyA5LjU2Mzc5IDE0LjIxNjcgOS43ODgwNkwxMi4zMDggOS45NjU4N0MxMi4wNzM0IDkuOTg3NzMgMTEuODYyNyAxMC4xMTg2IDExLjczOTEgMTAuMzE5MkMxMS41NDk2IDEwLjYyNjggMTEuMzIzNCAxMC45MDk2IDExLjA2NjYgMTEuMTYxNkMxMC44OTgyIDExLjMyNjcgMTAuODE3MyAxMS41NjE1IDEwLjg0ODMgMTEuNzk1M0wxMS4wOTk3IDEzLjY5NkMxMC44OTQ2IDEzLjgwOTEgMTAuNjgyOCAxMy45MTE0IDEwLjQ2NTEgMTQuMDAyMkw5LjEzNTg0IDEyLjYyMDZDOC45NzI1MiAxMi40NTA5IDguNzM4OTQgMTIuMzY3NyA4LjUwNTA5IDEyLjM5NjFDOC4zMjg1MiAxMi40MTc1IDguMTQ4NDcgMTIuNDI4NSA3Ljk2NTUxIDEyLjQyODVDNy43ODI1MyAxMi40Mjg1IDcuNjAyNDcgMTIuNDE3NSA3LjQyNTg5IDEyLjM5NjFDNy4xOTIwNCAxMi4zNjc3IDYuOTU4NDYgMTIuNDUwOSA2Ljc5NTE0IDEyLjYyMDZMNS40NjU4OSAxNC4wMDIyQzUuMjQ4MTYgMTMuOTExNCA1LjAzNjM4IDEzLjgwOTEgNC44MzEzMSAxMy42OTZMNS4wODI3MiAxMS43OTUzQzUuMTEzNjUgMTEuNTYxNSA1LjAzMjc4IDExLjMyNjcgNC44NjQ0MiAxMS4xNjE1QzQuNjA3NjEgMTAuOTA5NiA0LjM4MTQ0IDEwLjYyNjggNC4xOTE5NSAxMC4zMTkyQzQuMDY4MzMgMTAuMTE4NiAzLjg1NzYyIDkuOTg3NzMgMy42MjI5OSA5Ljk2NTg3TDEuNzE0MzMgOS43ODgwNkMxLjY1MDMyIDkuNTYzNzkgMS41OTgwNCA5LjMzNDUxIDEuNTU4MjIgOS4xMDA5TDMuMjAwNCA4LjExMjc1QzMuNDAyNzkgNy45OTA5NiAzLjUzNTk5IDcuNzgwOTUgMy41NTk4NyA3LjU0NTk1QzMuNTk3IDcuMTgwNTggMy42Nzg0NyA2LjgyODggMy43OTg3MiA2LjQ5NTc4QzMuODc4ODQgNi4yNzM4NiAzLjg0OTg4IDYuMDI3MTggMy43MjA1MSA1LjgyOTg2TDIuNjcwNzYgNC4yMjg2NUMyLjgwNzU5IDQuMDM2OTMgMi45NTQ2IDMuODUyOTIgMy4xMTEgMy42Nzc0MUw0LjkwNjA1IDQuMzQ0NjlDNS4xMjc0IDQuNDI2OTcgNS4zNzQ1NyA0LjQwMDIgNS41NzMxNyA0LjI3MjQzQzUuODczOTQgNC4wNzg5MyA2LjE5OTM3IDMuOTIxMDEgNi41NDM1NyAzLjgwNDRDNi43NjcwNSAzLjcyODY5IDYuOTQxODcgMy41NTIyMyA3LjAxNTQ4IDMuMzI4MDVaIiBmaWxsPSIjNkY2RjZGIi8+CjwvZz4KPGRlZnM+CjxjbGlwUGF0aCBpZD0iY2xpcDBfMTMxMjNfMzUwMTkiPgo8cmVjdCB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9IndoaXRlIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==) gear icon and select **OpenSharing**.
    
    Alternatively, in the upper-right corner, click **Share > OpenSharing**.
    
3.  On the **Shared with me** tab, find and select the provider.
    
4.  Find the desired share and click **Mount to catalog** on the share row.
    
5.  Select **Create a new catalog** or **Mount to existing catalog** to add the data asset to an existing catalog.
    
6.  Enter a name for your new catalog or choose which existing catalog to add the share to.
    
7.  Click **Create** or **Mount**.
    

Alternatively, when you open Catalog Explorer, you can click **\+ > Create Catalog** in the upper right to create a shared catalog. See [Create catalogs](https://docs.databricks.com/aws/en/catalogs/create-catalog).

The catalog created from a share has a catalog type of OpenSharing. You can view the type on the catalog details page in Catalog Explorer or by running the [DESCRIBE CATALOG](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-aux-describe-catalog) SQL command in a notebook or Databricks SQL query. All shared catalogs are listed under **Catalog > Shared** in the Catalog Explorer left pane.

An OpenSharing catalog can be managed in the same way as regular catalogs on a Unity Catalog metastore. You can view, update, and delete an OpenSharing catalog using Catalog Explorer, the Databricks CLI, and by using `SHOW CATALOGS`, `DESCRIBE CATALOG`, `ALTER CATALOG`, and `DROP CATALOG` SQL commands.

The 3-level namespace structure under an OpenSharing catalog created from a share is the same as the one under a regular catalog on Unity Catalog: `catalog.schema.table` or `catalog.schema.volume`.

Table and volume data under a shared catalog is read-only, which means you can perform read operations like:

*   `DESCRIBE`, `SHOW`, and `SELECT` for tables.
*   `DESCRIBE VOLUME`, `LIST <volume-path>`, `SELECT * FROM <format>.'<volume_path>'`, and `COPY INTO` for volumes.

Notebooks in a shared catalog can be previewed and cloned by any user with `USE CATALOG` on the catalog.

Models in a shared catalog can be read and loaded for inference by any user with the following privileges: `EXECUTE` privilege on the registered model, plus `USE SCHEMA` and `USE CATALOG` privileges on the schema and catalog containing the model.

### Manage permissions for the schemas, tables, and volumes in an OpenSharing catalog[​](#manage-permissions-for-the-schemas-tables-and-volumes-in-an-opensharing-catalog "Direct link to manage-permissions-for-the-schemas-tables-and-volumes-in-an-opensharing-catalog")

By default, the catalog creator is the owner of all data objects under an OpenSharing catalog and can manage permissions for any of them.

Privileges are inherited downward, although some workspaces may still be on the legacy security model that did not provide inheritance. See [Privilege inheritance](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/permissions-concepts#inheritance). Any user granted the `SELECT` privilege on the catalog will have the `SELECT` privilege on all of the schemas and tables in the catalog unless that privilege is revoked. Likewise, any user granted the `READ VOLUME` privilege on the catalog will have the `READ VOLUME` privilege on all of the volumes in the catalog unless that privilege is revoked. You cannot grant privileges that give write or update access to an OpenSharing catalog or objects in an OpenSharing catalog.

The catalog owner can delegate the ownership of data objects to other users or groups, thereby granting those users the ability to manage the object permissions and life cycles.

For detailed information about managing privileges on data objects using Unity Catalog, see [Manage privileges in Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/).

### Read data in a shared table[​](#read-data-in-a-shared-table "Direct link to Read data in a shared table")

You can read data in a shared table using any of the tools available to you as a Databricks user: Catalog Explorer, notebooks, SQL queries, the Databricks CLI, and Databricks REST APIs. You must have the `SELECT` privilege on the table.

If your provider has shared the table `WITH HISTORY`, you can run transactions on the table. For more information about transaction requirements and limitations, see [Transactions](https://docs.databricks.com/aws/en/transactions/).

### Read data in a shared foreign table or foreign schema[​](#read-data-in-a-shared-foreign-table-or-foreign-schema "Direct link to read-data-in-a-shared-foreign-table-or-foreign-schema")

You can read data in a shared foreign table or foreign schema using any of the tools available to you as a Databricks user: Catalog Explorer, notebooks, SQL queries, the Databricks CLI, and Databricks REST APIs. You must have the `SELECT` privilege on the shared foreign table or foreign schema.

You can run transactions on shared foreign tables. See [transaction requirements and limitations](https://docs.databricks.com/aws/en/transactions/#limitations).

There are additional costs when accessing a shared foreign table or foreign schema. For information on how sharing costs are computed, see [How do I incur and check OpenSharing costs?](https://docs.databricks.com/aws/en/delta-sharing/#share-costs).

**Limitations**: You can't bypass cluster restriction to read shared foreign tables, even if the provider permits it.

### Read data in a shared foreign Iceberg table[​](#read-data-in-a-shared-foreign-iceberg-table "Direct link to read-data-in-a-shared-foreign-iceberg-table")

You can read data in a shared foreign Iceberg table using any of the tools available to you as a Databricks user: Catalog Explorer, notebooks, SQL queries, the Databricks CLI, and Databricks REST APIs. In Catalog Explorer, a shared foreign Iceberg table displays with a table type of **Foreign** and a data source format of **Iceberg**.

You have access to the source Iceberg location but can only perform the following types of queries:

*   Snapshot queries
*   Streaming queries

**Requirements**:

*   You must have the `SELECT` privilege on the shared foreign Iceberg table.
*   You must use Databricks Runtime 15.4 LTS or above.

### Read data in a shared volume[​](#read-data-in-a-shared-volume "Direct link to read-data-in-a-shared-volume")

You can read data in a shared volume using any of the tools available to you as a Databricks user: Catalog Explorer, notebooks, SQL queries, the Databricks CLI, and Databricks REST APIs. You must have the `READ VOLUME` privilege on the volume.

### Read ABAC-secured data and apply ABAC policies[​](#read-abac-secured-data-and-apply-abac-policies "Direct link to read-abac-secured-data-and-apply-abac-policies")

[Attribute-based access control (ABAC)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/) is a data governance model that provides flexible, scalable, and centralized access control across Databricks.

Create ABAC policies for shared tables, schemas, and catalogs created from a share. Materialized views are supported with [limitations](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/requirements#materialized-views-and-streaming-tables). You _can't_ create ABAC policies for shared streaming tables or materialized views. To configure ABAC policies, see [Create and manage row filter and column mask policies](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/policies).

### Read row tracking columns in shared tables[​](#read-row-tracking-columns-in-shared-tables "Direct link to read-row-tracking-columns-in-shared-tables")

If the data provider has enabled row tracking on a shared table, you can query the row tracking metadata columns. See [Row tracking in Databricks](https://docs.databricks.com/aws/en/tables/features/row-tracking) for a list of available columns.

How you access these columns depends on the type of table shared:

*   **Tables shared with history and without partition filters**: You can query row tracking columns without restrictions.
    
*   **Tables with partition filters or tables shared without history**: You must use Scala Spark and explicitly set the `responseFormat` option to `delta`.
    
    Scala
    
        spark.read.option(“responseformat”, “delta”).table(“shared_table”).select(“_metadata.row_id”).show()
    

### Load a shared model for inference[​](#load-a-shared-model-for-inference "Direct link to Load a shared model for inference")

For details on loading a shared model and using it for batch inference, see [Load model version by alias for inference workloads](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/#load-models-for-inference).

### Query a table's history data[​](#query-a-tables-history-data "Direct link to Query a table's history data")

If history is shared along with the table, you can query the table data as of a version or timestamp. Requires Databricks Runtime 12.2 LTS or above.

For example:

SQL

    SELECT * FROM vaccine.vaccine_us.vaccine_us_distribution VERSION AS OF 3;SELECT * FROM vaccine.vaccine_us.vaccine_us_distribution TIMESTAMP AS OF "2023-01-01 00:00:00";

In addition, if the change data feed (CDF) is enabled with the table, you can query the CDF. Both version and timestamp are supported:

SQL

    SELECT * FROM table_changes('vaccine.vaccine_us.vaccine_us_distribution', 0, 3);SELECT * FROM table_changes('vaccine.vaccine_us.vaccine_us_distribution', "2023-01-01 00:00:00", "2022-02-01 00:00:00");

For more information about change data feed, see [Use change data feed on Databricks](https://docs.databricks.com/aws/en/tables/features/change-data-feed).

### Query a table using Apache Spark Structured Streaming[​](#query-a-table-using-apache-spark-structured-streaming "Direct link to query-a-table-using-apache-spark-structured-streaming")

If a table is shared with history, you can use it as the source for Spark Structured Streaming. Requires Databricks Runtime 12.2 LTS or above.

Supported options:

*   `ignoreDeletes`: Ignore transactions that delete data.
*   `ignoreChanges`: Re-process updates if files were rewritten in the source table due to a data changing operation such as `UPDATE`, `MERGE INTO`, `DELETE` (within partitions), or `OVERWRITE`. Unchanged rows can still be emitted. Therefore your downstream consumers should be able to handle duplicates. Deletes are not propagated downstream. `ignoreChanges` subsumes `ignoreDeletes`. Therefore, if you use `ignoreChanges`, your stream will not be disrupted by either deletions or updates to the source table.
*   `startingVersion`: The shared table version to start from. All table changes starting from this version (inclusive) will be read by the streaming source.
*   `startingTimestamp`: The timestamp to start from. All table changes committed at or after the timestamp (inclusive) will be read by the streaming source. Example: `"2023-01-01 00:00:00.0"`
*   `maxFilesPerTrigger`: The number of new files to be considered in every micro-batch.
*   `maxBytesPerTrigger`: The amount of data that gets processed in each micro-batch. This option sets a “soft max”, meaning that a batch processes approximately this amount of data and might process more than the limit in order to make the streaming query move forward in cases when the smallest input unit is larger than this limit.
*   `readChangeFeed`: Stream read the change data feed of the shared table.

Unsupported options:

*   `Trigger.availableNow`

#### Sample Structured Streaming queries[​](#sample-structured-streaming-queries "Direct link to sample-structured-streaming-queries")

*   Scala
*   Python

Scala

    spark.readStream.format("deltaSharing").option("startingVersion", 0).option("ignoreChanges", true).option("maxFilesPerTrigger", 10).table("vaccine.vaccine_us.vaccine_us_distribution")

If change data feed (CDF) is enabled with the table, you can stream read the CDF.

Scala

    spark.readStream.format("deltaSharing").option("readChangeFeed", "true").table("vaccine.vaccine_us.vaccine_us_distribution")

### Apply row filters and column masks[​](#apply-row-filters-and-column-masks "Direct link to apply-row-filters-and-column-masks")

To apply row filters and column masks on tables and foreign tables shared by your data provider, see [Manually apply row filters and column masks](https://docs.databricks.com/aws/en/data-governance/unity-catalog/filters-and-masks/manually-apply). You cannot apply columns masks to streaming tables or materialized views.

## Read tables with deletion vectors or column mapping enabled[​](#read-tables-with-deletion-vectors-or-column-mapping-enabled "Direct link to read-tables-with-deletion-vectors-or-column-mapping-enabled")

Deletion vectors are a storage optimization feature that your provider can enable on shared Delta tables. See [Deletion vectors in Databricks](https://docs.databricks.com/aws/en/tables/features/deletion-vectors).

Databricks also supports column mapping for Delta tables. See [Rename and drop columns with Delta Lake column mapping](https://docs.databricks.com/aws/en/tables/features/column-mapping).

If your provider shared a table with deletion vectors or column mapping enabled, you can perform batch reads on the table using a SQL warehouse or a cluster running Databricks Runtime 14.1 or above. CDF and streaming queries require Databricks Runtime 14.2 or above.

You can perform batch queries as-is, because they can automatically resolve `responseFormat` based on the table features of the shared table.

To read a change data feed (CDF) or to perform streaming queries on shared tables with deletion vectors or column mapping enabled, you must set the additional option `responseFormat=delta`.

The following examples show batch, CDF, and streaming queries:

Scala

    import org.apache.spark.sql.SparkSession// Batch queryspark.read.format("deltaSharing").table(<tableName>)// CDF queryspark.read.format("deltaSharing")  .option("readChangeFeed", "true")  .option("responseFormat", "delta")  .option("startingVersion", 1)  .table(<tableName>)// Streaming queryspark.readStream.format("deltaSharing").option("responseFormat", "delta").table(<tableName>)

Reading shared managed Iceberg tables is the same as [reading shared tables](#access-data), with these exceptions:

**Support in Databricks-to-Open sharing:**

The instructions in this article focus on reading shared data using Databricks user interfaces, specifically Unity Catalog syntax and interfaces. Due to the limitation on advanced Delta feature support for OpenSharing connectors, querying shared managed Iceberg tables using Python, Tableau, and Power BI is not supported.

**Change data feed:**

Change data feed is not supported for managed Iceberg tables.

**Databricks Iceberg limitations:**

Iceberg table and managed Iceberg table limitations apply. See [Limitations](https://docs.databricks.com/aws/en/iceberg/#iceberg-limitations).

Reading shared views is the same as [reading shared tables](#access-data), with these exceptions:

**Shared views restrictions:**

*   Shared views only support a subset of built-in functions and operators in Databricks. See [Functions supported in Databricks-to-Databricks view sharing](https://docs.databricks.com/aws/en/delta-sharing/shared-view-functions-data-databricks).
*   Recipients can't query more than 20 shared views in a query in Databricks-to-Databricks sharing. The shared views can't be from more than five different provider-shares.
*   When the provider is from the same account, or when you use serverless compute in a different account, you can't query multiple dependent views from the same provider in a single query. For example, if `view1` depends on `view2` on the provider side and both views are shared with you, you can't reference both `view1` and `view2` in the same query.
*   You can run transactions on shared views. See [transaction requirements and limitations](https://docs.databricks.com/aws/en/transactions/#limitations).

**Naming requirements:**

The catalog name that you use for the shared catalog that contains the view cannot be the same as any provider catalog that contains a table referenced by the view. For example, if the shared view is contained in your `test` catalog, and one of the provider's tables referenced in that view is contained in the provider's `test` catalog, the query will result in a namespace conflict error. See [Create a catalog from a share](#create-catalog).

**Query result timeout:**

If you don't have [direct access](https://docs.databricks.com/aws/en/delta-sharing/#accessing-views) to the underlying data, Databricks performs on-the-fly materialization when querying the view. When this materialization takes longer than 5 minutes, the query times out. Switch to serverless compute to avoid this limitation.

**History and streaming:**

You cannot query history or use a view as a streaming source.

**View support in Databricks-to-Open sharing:**

The instructions in this article focus on reading shared data using Databricks user interfaces, specifically Unity Catalog syntax and interfaces. You can also query shared views using Apache Spark, Python, and BI tools like Tableau and Power BI.

**Costs:**

For information on how sharing costs are computed, see [How do I incur and check OpenSharing costs?](https://docs.databricks.com/aws/en/delta-sharing/#share-costs).

Reading shared streaming tables and materialized views is the same as [reading shared tables](#access-data), with these exceptions:

**Support in Databricks-to-Open sharing:**

The instructions on this page focus on reading shared data using Databricks user interfaces, specifically Unity Catalog syntax and interfaces. You can also query shared streaming tables and materialized views using Apache Spark, Python, and BI tools like Tableau and Power BI. See [Read data shared using OpenSharing Databricks-to-Open sharing with bearer tokens](https://docs.databricks.com/aws/en/delta-sharing/read-data-open).

**Transactions:**

*   You can run transactions on shared materialized views and streaming tables. See [transaction requirements and limitations](https://docs.databricks.com/aws/en/transactions/#limitations).

**SQL limitations**:

*   The `current_recipient` function is not supported.
*   The `DESCRIBE EXTENDED` command is not supported.

**Column mapping:**

If you are using classic compute when receiving a share from a different Databricks account, you must specify the `responseFormat` like below when querying a materialized view or streaming tables with column mapping.

Python

    spark.read.option("responseFormat", "delta").table("catalog_name.schema_name.mv_name")

If you are using classic compute when sharing within the same Databricks account or serverless compute in any scenario, you can query without restrictions.

**Costs:**

For information on how sharing costs are computed, see [How do I incur and check OpenSharing costs?](https://docs.databricks.com/aws/en/delta-sharing/#share-costs).

*   Materialized view specific exceptions
*   Streaming table specific exceptions

**History:**

You cannot query history.

**Refresh:**

You cannot access the refresh status and refresh schedule of the materialized view.

**View and streaming table creation:**

You cannot create streaming tables on shared materialized views.

Reading shared Python UDFs is the same as [reading shared tables](#access-data). After you create a new catalog for the share or mount the share to an existing catalog, you can access and use the Python UDF.

Reading shared `FeatureSpecs` is the same as [reading shared tables](#access-data). After you create a new catalog for the share or mount the share to an existing catalog, you can deploy the `FeatureSpec` to your desired serving endpoint. To learn how to create an endpoint, see [Create an endpoint](https://docs.databricks.com/aws/en/machine-learning/feature-store/feature-function-serving#create-an-endpoint).

If your provider updates with the `FeatureSpec` with a new dependency but does not share the dependency with you, your model fails. Contact your data provider to check for new dependencies.

Before serving the `FeatureSpec`, you must create an online store and publish the dependent tables in your workspace. For how to create online stores and publish the table, see [Databricks Online Feature Stores](https://docs.databricks.com/aws/en/machine-learning/feature-store/online-feature-store).

To preview and clone shared notebook files, you can use Catalog Explorer.

**Storage limitation:** If your storage uses Private Endpoints, you cannot read shared notebooks.

**Permissions required:** Catalog owner or user with the `USE CATALOG` privilege on the catalog created from the share.

1.  In your Databricks workspace, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
    
2.  In the left pane, expand the **Catalog** menu, find and select the catalog created from the share.
    
3.  On the **Other assets** tab, you'll see any shared notebook files.
    
4.  Click the name of a shared notebook file to preview it.
    
5.  (Optional) Click the **Clone** button to import the shared notebook file to your workspace.
    
    1.  On the **Clone to** dialog, optionally enter a **New name**, then select the workspace folder you want to clone the notebook file to.
    2.  Click **Clone**.
    3.  Once the notebook is cloned, a dialog pops up to let you know that it successfully cloned. Click **reveal in the notebook editor** on the dialog to view it in the notebook editor.
    
    See [Databricks notebooks](https://docs.databricks.com/aws/en/notebooks/).
    

Unmount a share to remove the data asset from its catalog.

**Permissions required:** User with the `USE CATALOG` and `MANAGE` privileges on the shared catalog.

1.  In your Databricks workspace, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog** to open Catalog Explorer.
    
2.  At the top of the **Catalog** pane, click the ![Gear icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzEzMTIzXzM1MDE5KSI+CjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNNy45ODQzMyA1QzYuMzI3NDcgNSA0Ljk4NDMzIDYuMzQzMTUgNC45ODQzMyA4QzQuOTg0MzMgOS42NTY4NSA2LjMyNzQ3IDExIDcuOTg0MzMgMTFDOS42NDExOCAxMSAxMC45ODQzIDkuNjU2ODUgMTAuOTg0MyA4QzEwLjk4NDMgNi4zNDMxNSA5LjY0MTE4IDUgNy45ODQzMyA1Wk02LjQ4NDMzIDhDNi40ODQzMyA3LjE3MTU3IDcuMTU1OSA2LjUgNy45ODQzMyA2LjVDOC44MTI3NSA2LjUgOS40ODQzMyA3LjE3MTU3IDkuNDg0MzMgOEM5LjQ4NDMzIDguODI4NDMgOC44MTI3NSA5LjUgNy45ODQzMyA5LjVDNy4xNTU5IDkuNSA2LjQ4NDMzIDguODI4NDMgNi40ODQzMyA4WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTcuOTY1NSAwQzcuNjI1NTIgMCA3LjI5MDE0IDAuMDIxMjUxMSA2Ljk2MDcgMC4wNjI1NzM2QzYuNjczMDQgMC4wOTg2NTU4IDYuNDMxOTQgMC4yOTczIDYuMzQxNDggMC41NzI3NDVMNS43MDI0IDIuNTE4ODhDNS40OTI0NCAyLjYwNTY1IDUuMjg4NiAyLjcwNDExIDUuMDkxNyAyLjgxMzQxTDMuMTcxOTggMi4wOTk3OUMyLjkwMDU0IDEuOTk4ODggMi41OTUyNiAyLjA2MzI2IDIuMzg3NjkgMi4yNjUxOUMxLjkwNjkgMi43MzI4OSAxLjQ4NDY0IDMuMjYwNjggMS4xMzMwMSAzLjgzNjYxQzAuOTgxOTgyIDQuMDgzOTkgMC45ODcwMDYgNC4zOTYyNSAxLjE0NTkyIDQuNjM4NjRMMi4yNjkxOSA2LjM1MTk4QzIuMjA2OTIgNi41Njc1NyAyLjE1NjU2IDYuNzg4MTQgMi4xMTg4NSA3LjAxMjkzTDAuMzYzMzIyIDguMDY5MjhDMC4xMTU0ODMgOC4yMTg0MiAtMC4wMjQ1MDg2IDguNDk2NzggMC4wMDM1NDkyOSA4Ljc4NDY2QzAuMDcwMDUzNiA5LjQ2NzAyIDAuMjIyMzY1IDEwLjEyNDggMC40NDk2NjkgMTAuNzQ2NkMwLjU0OTA4NSAxMS4wMTg2IDAuNzk2MTg5IDExLjIwOSAxLjA4NDUxIDExLjIzNTlMMy4xMjY2NyAxMS40MjYxQzMuMjU3MzUgMTEuNjEwNCAzLjM5ODI2IDExLjc4NjggMy41NDg1OCAxMS45NTQ2TDMuMjc5NzQgMTMuOTg3MkMzLjI0MTggMTQuMjc0IDMuMzcyMjIgMTQuNTU3MSAzLjYxNDkgMTQuNzE0NkM0LjE3NDI3IDE1LjA3NzcgNC43ODIxNiAxNS4zNzMgNS40MjY4NiAxNS41ODg2QzUuNzAxNDcgMTUuNjgwNCA2LjAwNDQyIDE1LjYwNiA2LjIwNTE4IDE1LjM5NzNMNy42Mjc0MyAxMy45MTlDNy43MzkzOSAxMy45MjU0IDcuODUyMTEgMTMuOTI4NSA3Ljk2NTUxIDEzLjkyODVDOC4wNzg4OSAxMy45Mjg1IDguMTkxNiAxMy45MjU0IDguMzAzNTQgMTMuOTE5TDkuNzI1OCAxNS4zOTczQzkuOTI2NTYgMTUuNjA2IDEwLjIyOTUgMTUuNjgwNCAxMC41MDQxIDE1LjU4ODZDMTEuMTQ4OCAxNS4zNzMgMTEuNzU2NyAxNS4wNzc3IDEyLjMxNjEgMTQuNzE0NkMxMi41NTg4IDE0LjU1NzEgMTIuNjg5MiAxNC4yNzQgMTIuNjUxMiAxMy45ODcyTDEyLjM4MjQgMTEuOTU0N0MxMi41MzI3IDExLjc4NjkgMTIuNjczNyAxMS42MTA0IDEyLjgwNDMgMTEuNDI2MUwxNC44NDY1IDExLjIzNTlDMTUuMTM0OCAxMS4yMDkgMTUuMzgxOSAxMS4wMTg2IDE1LjQ4MTMgMTAuNzQ2NkMxNS43MDg2IDEwLjEyNDggMTUuODYwOSA5LjQ2NzA0IDE1LjkyNzUgOC43ODQ2OUMxNS45NTU1IDguNDk2OCAxNS44MTU1IDguMjE4NDQgMTUuNTY3NyA4LjA2OTNMMTMuODEyMiA3LjAxMjk2QzEzLjc3NDUgNi43ODgxNSAxMy43MjQxIDYuNTY3NTQgMTMuNjYxOCA2LjM1MTkzTDE0Ljc4NTEgNC42Mzg2MUMxNC45NDQgNC4zOTYyMiAxNC45NDkgNC4wODM5NiAxNC43OTggMy44MzY1OEMxNC40NDYzIDMuMjYwNjUgMTQuMDI0MSAyLjczMjg3IDEzLjU0MzMgMi4yNjUxOEMxMy4zMzU3IDIuMDYzMjUgMTMuMDMwNSAxLjk5ODg3IDEyLjc1OSAyLjA5OTc4TDEwLjgzOTMgMi44MTM0QzEwLjY0MjQgMi43MDQwOSAxMC40Mzg1IDIuNjA1NjMgMTAuMjI4NiAyLjUxODg1TDkuNTg5NDkgMC41NzI3NDFDOS40OTkwMyAwLjI5NzI5NCA5LjI1NzkzIDAuMDk4NjQ5NiA4Ljk3MDI2IDAuMDYyNTY4NkM4LjY0MDgzIDAuMDIxMjQ5NCA4LjMwNTQ4IDAgNy45NjU1IDBaTTcuMDE1NDggMy4zMjgwNUw3LjYxMjcxIDEuNTA5MzlDNy43Mjk0NiAxLjUwMzE2IDcuODQ3MDggMS41IDcuOTY1NSAxLjVDOC4wODM5MSAxLjUgOC4yMDE1MyAxLjUwMzE2IDguMzE4MjYgMS41MDkzOUw4LjkxNTQ4IDMuMzI4MDRDOC45ODkxIDMuNTUyMjEgOS4xNjM5MiAzLjcyODY4IDkuMzg3NCAzLjgwNDM4QzkuNzMxNjEgMy45MjA5OSAxMC4wNTcxIDQuMDc4OTIgMTAuMzU3OCA0LjI3MjQyQzEwLjU1NjQgNC40MDAxOSAxMC44MDM2IDQuNDI2OTYgMTEuMDI1IDQuMzQ0NjhMMTIuODIgMy42Nzc0QzEyLjk3NjQgMy44NTI5IDEzLjEyMzQgNC4wMzY5MSAxMy4yNjAyIDQuMjI4NjNMMTIuMjEwNSA1LjgyOTgyQzEyLjA4MTEgNi4wMjcxMyAxMi4wNTIyIDYuMjczODIgMTIuMTMyMyA2LjQ5NTc0QzEyLjI1MjUgNi44Mjg3OCAxMi4zMzQgNy4xODA1OCAxMi4zNzEyIDcuNTQ1OTdDMTIuMzk1IDcuNzgwOTcgMTIuNTI4MiA3Ljk5MDk5IDEyLjczMDYgOC4xMTI3N0wxNC4zNzI4IDkuMTAwOTJDMTQuMzMzIDkuMzM0NTIgMTQuMjgwNyA5LjU2Mzc5IDE0LjIxNjcgOS43ODgwNkwxMi4zMDggOS45NjU4N0MxMi4wNzM0IDkuOTg3NzMgMTEuODYyNyAxMC4xMTg2IDExLjczOTEgMTAuMzE5MkMxMS41NDk2IDEwLjYyNjggMTEuMzIzNCAxMC45MDk2IDExLjA2NjYgMTEuMTYxNkMxMC44OTgyIDExLjMyNjcgMTAuODE3MyAxMS41NjE1IDEwLjg0ODMgMTEuNzk1M0wxMS4wOTk3IDEzLjY5NkMxMC44OTQ2IDEzLjgwOTEgMTAuNjgyOCAxMy45MTE0IDEwLjQ2NTEgMTQuMDAyMkw5LjEzNTg0IDEyLjYyMDZDOC45NzI1MiAxMi40NTA5IDguNzM4OTQgMTIuMzY3NyA4LjUwNTA5IDEyLjM5NjFDOC4zMjg1MiAxMi40MTc1IDguMTQ4NDcgMTIuNDI4NSA3Ljk2NTUxIDEyLjQyODVDNy43ODI1MyAxMi40Mjg1IDcuNjAyNDcgMTIuNDE3NSA3LjQyNTg5IDEyLjM5NjFDNy4xOTIwNCAxMi4zNjc3IDYuOTU4NDYgMTIuNDUwOSA2Ljc5NTE0IDEyLjYyMDZMNS40NjU4OSAxNC4wMDIyQzUuMjQ4MTYgMTMuOTExNCA1LjAzNjM4IDEzLjgwOTEgNC44MzEzMSAxMy42OTZMNS4wODI3MiAxMS43OTUzQzUuMTEzNjUgMTEuNTYxNSA1LjAzMjc4IDExLjMyNjcgNC44NjQ0MiAxMS4xNjE1QzQuNjA3NjEgMTAuOTA5NiA0LjM4MTQ0IDEwLjYyNjggNC4xOTE5NSAxMC4zMTkyQzQuMDY4MzMgMTAuMTE4NiAzLjg1NzYyIDkuOTg3NzMgMy42MjI5OSA5Ljk2NTg3TDEuNzE0MzMgOS43ODgwNkMxLjY1MDMyIDkuNTYzNzkgMS41OTgwNCA5LjMzNDUxIDEuNTU4MjIgOS4xMDA5TDMuMjAwNCA4LjExMjc1QzMuNDAyNzkgNy45OTA5NiAzLjUzNTk5IDcuNzgwOTUgMy41NTk4NyA3LjU0NTk1QzMuNTk3IDcuMTgwNTggMy42Nzg0NyA2LjgyODggMy43OTg3MiA2LjQ5NTc4QzMuODc4ODQgNi4yNzM4NiAzLjg0OTg4IDYuMDI3MTggMy43MjA1MSA1LjgyOTg2TDIuNjcwNzYgNC4yMjg2NUMyLjgwNzU5IDQuMDM2OTMgMi45NTQ2IDMuODUyOTIgMy4xMTEgMy42Nzc0MUw0LjkwNjA1IDQuMzQ0NjlDNS4xMjc0IDQuNDI2OTcgNS4zNzQ1NyA0LjQwMDIgNS41NzMxNyA0LjI3MjQzQzUuODczOTQgNC4wNzg5MyA2LjE5OTM3IDMuOTIxMDEgNi41NDM1NyAzLjgwNDRDNi43NjcwNSAzLjcyODY5IDYuOTQxODcgMy41NTIyMyA3LjAxNTQ4IDMuMzI4MDVaIiBmaWxsPSIjNkY2RjZGIi8+CjwvZz4KPGRlZnM+CjxjbGlwUGF0aCBpZD0iY2xpcDBfMTMxMjNfMzUwMTkiPgo8cmVjdCB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9IndoaXRlIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==) gear icon and select **OpenSharing**.
    
    Alternatively, in the upper-right corner, click **Share > OpenSharing**.
    
3.  On the **Shared with me** tab, find and select the provider.
    
4.  Click ![Kebab menu icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTggMUM3LjAzMzUgMSA2LjI1IDEuNzgzNSA2LjI1IDIuNzVDNi4yNSAzLjcxNjUgNy4wMzM1IDQuNSA4IDQuNUM4Ljk2NjUgNC41IDkuNzUgMy43MTY1IDkuNzUgMi43NUM5Ljc1IDEuNzgzNSA4Ljk2NjUgMSA4IDFaIiBmaWxsPSIjNkY2RjZGIi8+CjxwYXRoIGQ9Ik04IDYuMjVDNy4wMzM1IDYuMjUgNi4yNSA3LjAzMzUgNi4yNSA4QzYuMjUgOC45NjY1IDcuMDMzNSA5Ljc1IDggOS43NUM4Ljk2NjUgOS43NSA5Ljc1IDguOTY2NSA5Ljc1IDhDOS43NSA3LjAzMzUgOC45NjY1IDYuMjUgOCA2LjI1WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBkPSJNOCAxMS41QzcuMDMzNSAxMS41IDYuMjUgMTIuMjgzNSA2LjI1IDEzLjI1QzYuMjUgMTQuMjE2NSA3LjAzMzUgMTUgOCAxNUM4Ljk2NjUgMTUgOS43NSAxNC4yMTY1IDkuNzUgMTMuMjVDOS43NSAxMi4yODM1IDguOTY2NSAxMS41IDggMTEuNVoiIGZpbGw9IiM2RjZGNkYiLz4KPC9zdmc+Cg==) on the share row.
    
5.  Click **Unmount share**.
    
6.  Click **Unmount**.
