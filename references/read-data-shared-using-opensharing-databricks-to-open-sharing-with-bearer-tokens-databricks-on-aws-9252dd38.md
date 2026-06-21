---
title: Read data shared using OpenSharing Databricks-to-Open sharing with bearer tokens | Databricks on AWS
source: https://docs.databricks.com/aws/en/delta-sharing/read-data-open
ingestedAt: "2026-06-18T08:05:36.966Z"
---

This page describes how to read data shared with you using the OpenSharing _open sharing_ protocol with bearer tokens. It includes instructions for reading shared data using the following tools:

*   [Databricks](#databricks-open-connectors)
*   [Iceberg clients](#iceberg)
*   [Apache Spark](#apache-spark)
*   [Pandas](#pandas)
*   [Power BI](#power-bi)
*   [Tableau](#tableau)

In this Databricks-to-Open sharing model, you use a credential file, shared with a member of your team by the data provider, to gain secure read access to shared data. Access persists as long as the credential is valid and the provider continues to share the data. Providers manage credential expiration and rotation. Updates to the data are available in near real time. You can read and make copies of the shared data, but you cannot modify the source data.

note

In Databricks-to-Open sharing, the storage bucket and credential capabilities (scope, expiration, read vs. read/write) are determined by the provider. Mounting an open share in a Secure Egress Gateway (SEG) workspace automatically allowlists the provider's bucket for outbound access — verify the provider before mounting.

The following sections describe how to use Databricks, Apache Spark, `pandas`, Power BI, and Iceberg clients to access and read shared data using the credential file. For a full list of OpenSharing connectors and information about how to use them, see the [OpenSharing open source documentation](https://opensharing.io/). If you run into trouble accessing the shared data, contact the data provider.

## Before you begin[​](#before-you-begin "Direct link to before-you-begin")

A member of your team must download the credential file shared by the data provider and use a secure channel to share that file or file location with you. See [Get access in the Databricks-to-Open sharing model](https://docs.databricks.com/aws/en/delta-sharing/recipient#get-access-open).

For connector-specific documentation, see [the download credentials page](https://oregon.cloud.databricks.com/delta-sharing/download-credentials).

This section describes how to import a provider and how to query the shared data in Catalog Explorer or in a Python notebook:

*   If your Databricks workspace is enabled for Unity Catalog, use the Import provider UI in Catalog Explorer. You can do the following without needing to store or specify a credential file:
    
    *   Create catalogs from shares with the click of a button.
    *   Use Unity Catalog access controls to grant access to shared tables.
    *   Query shared data using standard Unity Catalog syntax.
    *   Apply a rotated credential to the existing provider object without recreating the catalog. See [Rotate credentials for open recipients](https://docs.databricks.com/aws/en/delta-sharing/manage-provider#rotate-credentials).
*   If your Databricks workspace is not enabled for Unity Catalog, use the Python notebook instructions as an example.
    

*   Catalog Explorer
*   Python

**Permissions required**: A metastore admin or a user who has both the `CREATE PROVIDER` and `USE PROVIDER` privileges for your Unity Catalog metastore.

1.  In your Databricks workspace, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog** to open Catalog Explorer.
    
2.  At the top of the **Catalog** pane, click ![Gear icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzEzMTIzXzM1MDE5KSI+CjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNNy45ODQzMyA1QzYuMzI3NDcgNSA0Ljk4NDMzIDYuMzQzMTUgNC45ODQzMyA4QzQuOTg0MzMgOS42NTY4NSA2LjMyNzQ3IDExIDcuOTg0MzMgMTFDOS42NDExOCAxMSAxMC45ODQzIDkuNjU2ODUgMTAuOTg0MyA4QzEwLjk4NDMgNi4zNDMxNSA5LjY0MTE4IDUgNy45ODQzMyA1Wk02LjQ4NDMzIDhDNi40ODQzMyA3LjE3MTU3IDcuMTU1OSA2LjUgNy45ODQzMyA2LjVDOC44MTI3NSA2LjUgOS40ODQzMyA3LjE3MTU3IDkuNDg0MzMgOEM5LjQ4NDMzIDguODI4NDMgOC44MTI3NSA5LjUgNy45ODQzMyA5LjVDNy4xNTU5IDkuNSA2LjQ4NDMzIDguODI4NDMgNi40ODQzMyA4WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTcuOTY1NSAwQzcuNjI1NTIgMCA3LjI5MDE0IDAuMDIxMjUxMSA2Ljk2MDcgMC4wNjI1NzM2QzYuNjczMDQgMC4wOTg2NTU4IDYuNDMxOTQgMC4yOTczIDYuMzQxNDggMC41NzI3NDVMNS43MDI0IDIuNTE4ODhDNS40OTI0NCAyLjYwNTY1IDUuMjg4NiAyLjcwNDExIDUuMDkxNyAyLjgxMzQxTDMuMTcxOTggMi4wOTk3OUMyLjkwMDU0IDEuOTk4ODggMi41OTUyNiAyLjA2MzI2IDIuMzg3NjkgMi4yNjUxOUMxLjkwNjkgMi43MzI4OSAxLjQ4NDY0IDMuMjYwNjggMS4xMzMwMSAzLjgzNjYxQzAuOTgxOTgyIDQuMDgzOTkgMC45ODcwMDYgNC4zOTYyNSAxLjE0NTkyIDQuNjM4NjRMMi4yNjkxOSA2LjM1MTk4QzIuMjA2OTIgNi41Njc1NyAyLjE1NjU2IDYuNzg4MTQgMi4xMTg4NSA3LjAxMjkzTDAuMzYzMzIyIDguMDY5MjhDMC4xMTU0ODMgOC4yMTg0MiAtMC4wMjQ1MDg2IDguNDk2NzggMC4wMDM1NDkyOSA4Ljc4NDY2QzAuMDcwMDUzNiA5LjQ2NzAyIDAuMjIyMzY1IDEwLjEyNDggMC40NDk2NjkgMTAuNzQ2NkMwLjU0OTA4NSAxMS4wMTg2IDAuNzk2MTg5IDExLjIwOSAxLjA4NDUxIDExLjIzNTlMMy4xMjY2NyAxMS40MjYxQzMuMjU3MzUgMTEuNjEwNCAzLjM5ODI2IDExLjc4NjggMy41NDg1OCAxMS45NTQ2TDMuMjc5NzQgMTMuOTg3MkMzLjI0MTggMTQuMjc0IDMuMzcyMjIgMTQuNTU3MSAzLjYxNDkgMTQuNzE0NkM0LjE3NDI3IDE1LjA3NzcgNC43ODIxNiAxNS4zNzMgNS40MjY4NiAxNS41ODg2QzUuNzAxNDcgMTUuNjgwNCA2LjAwNDQyIDE1LjYwNiA2LjIwNTE4IDE1LjM5NzNMNy42Mjc0MyAxMy45MTlDNy43MzkzOSAxMy45MjU0IDcuODUyMTEgMTMuOTI4NSA3Ljk2NTUxIDEzLjkyODVDOC4wNzg4OSAxMy45Mjg1IDguMTkxNiAxMy45MjU0IDguMzAzNTQgMTMuOTE5TDkuNzI1OCAxNS4zOTczQzkuOTI2NTYgMTUuNjA2IDEwLjIyOTUgMTUuNjgwNCAxMC41MDQxIDE1LjU4ODZDMTEuMTQ4OCAxNS4zNzMgMTEuNzU2NyAxNS4wNzc3IDEyLjMxNjEgMTQuNzE0NkMxMi41NTg4IDE0LjU1NzEgMTIuNjg5MiAxNC4yNzQgMTIuNjUxMiAxMy45ODcyTDEyLjM4MjQgMTEuOTU0N0MxMi41MzI3IDExLjc4NjkgMTIuNjczNyAxMS42MTA0IDEyLjgwNDMgMTEuNDI2MUwxNC44NDY1IDExLjIzNTlDMTUuMTM0OCAxMS4yMDkgMTUuMzgxOSAxMS4wMTg2IDE1LjQ4MTMgMTAuNzQ2NkMxNS43MDg2IDEwLjEyNDggMTUuODYwOSA5LjQ2NzA0IDE1LjkyNzUgOC43ODQ2OUMxNS45NTU1IDguNDk2OCAxNS44MTU1IDguMjE4NDQgMTUuNTY3NyA4LjA2OTNMMTMuODEyMiA3LjAxMjk2QzEzLjc3NDUgNi43ODgxNSAxMy43MjQxIDYuNTY3NTQgMTMuNjYxOCA2LjM1MTkzTDE0Ljc4NTEgNC42Mzg2MUMxNC45NDQgNC4zOTYyMiAxNC45NDkgNC4wODM5NiAxNC43OTggMy44MzY1OEMxNC40NDYzIDMuMjYwNjUgMTQuMDI0MSAyLjczMjg3IDEzLjU0MzMgMi4yNjUxOEMxMy4zMzU3IDIuMDYzMjUgMTMuMDMwNSAxLjk5ODg3IDEyLjc1OSAyLjA5OTc4TDEwLjgzOTMgMi44MTM0QzEwLjY0MjQgMi43MDQwOSAxMC40Mzg1IDIuNjA1NjMgMTAuMjI4NiAyLjUxODg1TDkuNTg5NDkgMC41NzI3NDFDOS40OTkwMyAwLjI5NzI5NCA5LjI1NzkzIDAuMDk4NjQ5NiA4Ljk3MDI2IDAuMDYyNTY4NkM4LjY0MDgzIDAuMDIxMjQ5NCA4LjMwNTQ4IDAgNy45NjU1IDBaTTcuMDE1NDggMy4zMjgwNUw3LjYxMjcxIDEuNTA5MzlDNy43Mjk0NiAxLjUwMzE2IDcuODQ3MDggMS41IDcuOTY1NSAxLjVDOC4wODM5MSAxLjUgOC4yMDE1MyAxLjUwMzE2IDguMzE4MjYgMS41MDkzOUw4LjkxNTQ4IDMuMzI4MDRDOC45ODkxIDMuNTUyMjEgOS4xNjM5MiAzLjcyODY4IDkuMzg3NCAzLjgwNDM4QzkuNzMxNjEgMy45MjA5OSAxMC4wNTcxIDQuMDc4OTIgMTAuMzU3OCA0LjI3MjQyQzEwLjU1NjQgNC40MDAxOSAxMC44MDM2IDQuNDI2OTYgMTEuMDI1IDQuMzQ0NjhMMTIuODIgMy42Nzc0QzEyLjk3NjQgMy44NTI5IDEzLjEyMzQgNC4wMzY5MSAxMy4yNjAyIDQuMjI4NjNMMTIuMjEwNSA1LjgyOTgyQzEyLjA4MTEgNi4wMjcxMyAxMi4wNTIyIDYuMjczODIgMTIuMTMyMyA2LjQ5NTc0QzEyLjI1MjUgNi44Mjg3OCAxMi4zMzQgNy4xODA1OCAxMi4zNzEyIDcuNTQ1OTdDMTIuMzk1IDcuNzgwOTcgMTIuNTI4MiA3Ljk5MDk5IDEyLjczMDYgOC4xMTI3N0wxNC4zNzI4IDkuMTAwOTJDMTQuMzMzIDkuMzM0NTIgMTQuMjgwNyA5LjU2Mzc5IDE0LjIxNjcgOS43ODgwNkwxMi4zMDggOS45NjU4N0MxMi4wNzM0IDkuOTg3NzMgMTEuODYyNyAxMC4xMTg2IDExLjczOTEgMTAuMzE5MkMxMS41NDk2IDEwLjYyNjggMTEuMzIzNCAxMC45MDk2IDExLjA2NjYgMTEuMTYxNkMxMC44OTgyIDExLjMyNjcgMTAuODE3MyAxMS41NjE1IDEwLjg0ODMgMTEuNzk1M0wxMS4wOTk3IDEzLjY5NkMxMC44OTQ2IDEzLjgwOTEgMTAuNjgyOCAxMy45MTE0IDEwLjQ2NTEgMTQuMDAyMkw5LjEzNTg0IDEyLjYyMDZDOC45NzI1MiAxMi40NTA5IDguNzM4OTQgMTIuMzY3NyA4LjUwNTA5IDEyLjM5NjFDOC4zMjg1MiAxMi40MTc1IDguMTQ4NDcgMTIuNDI4NSA3Ljk2NTUxIDEyLjQyODVDNy43ODI1MyAxMi40Mjg1IDcuNjAyNDcgMTIuNDE3NSA3LjQyNTg5IDEyLjM5NjFDNy4xOTIwNCAxMi4zNjc3IDYuOTU4NDYgMTIuNDUwOSA2Ljc5NTE0IDEyLjYyMDZMNS40NjU4OSAxNC4wMDIyQzUuMjQ4MTYgMTMuOTExNCA1LjAzNjM4IDEzLjgwOTEgNC44MzEzMSAxMy42OTZMNS4wODI3MiAxMS43OTUzQzUuMTEzNjUgMTEuNTYxNSA1LjAzMjc4IDExLjMyNjcgNC44NjQ0MiAxMS4xNjE1QzQuNjA3NjEgMTAuOTA5NiA0LjM4MTQ0IDEwLjYyNjggNC4xOTE5NSAxMC4zMTkyQzQuMDY4MzMgMTAuMTE4NiAzLjg1NzYyIDkuOTg3NzMgMy42MjI5OSA5Ljk2NTg3TDEuNzE0MzMgOS43ODgwNkMxLjY1MDMyIDkuNTYzNzkgMS41OTgwNCA5LjMzNDUxIDEuNTU4MjIgOS4xMDA5TDMuMjAwNCA4LjExMjc1QzMuNDAyNzkgNy45OTA5NiAzLjUzNTk5IDcuNzgwOTUgMy41NTk4NyA3LjU0NTk1QzMuNTk3IDcuMTgwNTggMy42Nzg0NyA2LjgyODggMy43OTg3MiA2LjQ5NTc4QzMuODc4ODQgNi4yNzM4NiAzLjg0OTg4IDYuMDI3MTggMy43MjA1MSA1LjgyOTg2TDIuNjcwNzYgNC4yMjg2NUMyLjgwNzU5IDQuMDM2OTMgMi45NTQ2IDMuODUyOTIgMy4xMTEgMy42Nzc0MUw0LjkwNjA1IDQuMzQ0NjlDNS4xMjc0IDQuNDI2OTcgNS4zNzQ1NyA0LjQwMDIgNS41NzMxNyA0LjI3MjQzQzUuODczOTQgNC4wNzg5MyA2LjE5OTM3IDMuOTIxMDEgNi41NDM1NyAzLjgwNDRDNi43NjcwNSAzLjcyODY5IDYuOTQxODcgMy41NTIyMyA3LjAxNTQ4IDMuMzI4MDVaIiBmaWxsPSIjNkY2RjZGIi8+CjwvZz4KPGRlZnM+CjxjbGlwUGF0aCBpZD0iY2xpcDBfMTMxMjNfMzUwMTkiPgo8cmVjdCB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9IndoaXRlIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==) and select **OpenSharing**.
    
    Alternatively, in the upper-right corner, click **Share > OpenSharing**.
    
3.  On the **Shared with me** tab, click **Install share**.
    
4.  Enter the provider name.
    
    The name cannot include spaces.
    
5.  Upload the credential file that the provider shared with you.
    
    Many providers have their own OpenSharing networks that you can receive shares from. For more information, see [Provider-specific configurations](https://docs.databricks.com/aws/en/delta-sharing/share-data-open#proprietary).
    
6.  (Optional) Enter a comment.
    
    ![Import a provider&#39;s credential file directly from a provider](https://docs.databricks.com/aws/en/assets/images/import-provider-new2-a2b752ee2e892ed8b5dfbe6fe85d55ed.png)
    
7.  Click **Import**.
    
8.  Create catalogs from the shared data.
    
    On the **Shares** tab, click **Create catalog** on the share row.
    
    For information about using SQL or the Databricks CLI to create a catalog from a share, see [Create a catalog from a share](https://docs.databricks.com/aws/en/delta-sharing/read-data-databricks#create-catalog).
    
9.  Grant access to the catalogs.
    
    See [How do I make shared data available to my team?](https://docs.databricks.com/aws/en/delta-sharing/read-data-databricks#overview) and [Manage permissions for the schemas, tables, and volumes in an OpenSharing catalog](https://docs.databricks.com/aws/en/delta-sharing/read-data-databricks#schema-table-permissions).
    
10.  Read the shared data objects just like you would any data object that is registered in Unity Catalog.
     
     For details and examples, see [Access data in a shared table or volume](https://docs.databricks.com/aws/en/delta-sharing/read-data-databricks#access-data).
     

Use external Iceberg clients, such as Snowflake, Trino, Flink, and Spark, to read shared data assets with zero-copy access using the [Apache Iceberg REST Catalog API](https://github.com/apache/iceberg/blob/main/open-api/rest-catalog-open-api.yaml).

### Obtain connection credentials[​](#obtain-connection-credentials "Direct link to Obtain connection credentials")

Before you access shared data assets with external Iceberg clients, gather the following credentials:

*   The Iceberg REST Catalog endpoint
*   A valid Bearer token
*   The share name
*   (Optional) The namespace or schema name
*   (Optional) The table name

The Iceberg REST Catalog endpoint (`icebergEndpoint`) and Bearer token are found in the credential file shared with you by your data provider. For more information, see [Before you begin](#before). The share name, namespace, and table name can be discovered programmatically using OpenSharing APIs.

important

The `icebergEndpoint` is found in the credential file and has the format `<workspace-url>/api/2.0/delta-sharing/metastores/<metastore-id>/iceberg`.

The following examples show how to obtain the additional credentials. Enter the endpoint, Iceberg endpoint, and the Bearer token from the credential file where needed:

Shell

    // List sharescurl -X GET "<endpoint>/shares" \   -H "Authorization: Bearer <bearerToken>"// List namespacescurl -X GET "<icebergEndpoint>/v1/shares/<share>/namespaces" \   -H "Authorization: Bearer <bearerToken>"// List tablescurl -X GET "<icebergEndpoint>/v1/shares/<share>/namespaces/<namespace>/tables" \   -H "Authorization: Bearer <bearerToken>"

note

This method always retrieves the most up-to-date list of assets. However, it requires internet access and can be harder to integrate in no-code environments.

### Configure Iceberg catalog[​](#configure-iceberg-catalog "Direct link to configure-iceberg-catalog")

After you obtain the necessary connection credentials, configure your client to use the Iceberg REST Catalog endpoints to create and query tables.

1.  For each share, create a catalog integration.
    
    SQL
    
        USE ROLE ACCOUNTADMIN;CREATE OR REPLACE CATALOG INTEGRATION <CATALOG_PLACEHOLDER>CATALOG_SOURCE = ICEBERG_RESTTABLE_FORMAT = ICEBERGREST_CONFIG = (   CATALOG_URI = '<icebergEndpoint>',   WAREHOUSE = '<share_name>',   ACCESS_DELEGATION_MODE = VENDED_CREDENTIALS)REST_AUTHENTICATION = (   TYPE = BEARER,   BEARER_TOKEN = '<bearerToken>')ENABLED = TRUE;
    
2.  Optionally, add `REFRESH_INTERVAL_SECONDS` to keep metadata up to date. Set the value based on your catalog update frequency.
    
    SQL
    
        REFRESH_INTERVAL_SECONDS = 30
    
3.  After the catalog is configured, create a database from the catalog. This automatically creates all schemas and tables in that catalog.
    
    SQL
    
        CREATE DATABASE <DATABASE_PLACEHOLDER>LINKED_CATALOG = (   CATALOG = <CATALOG_PLACEHOLDER>);
    
4.  To confirm that the sharing is successful, query from a table in the database. You should see the shared data from Databricks.
    

If the result is empty or an error occurs, follow these common troubleshooting steps:

*   Double-check the privileges, snapshot generation status, and REST credentials.
*   Contact your data provider.
*   See the documentation specific to your Iceberg client.

### Example: Access shared tables using different Iceberg clients[​](#example-access-shared-tables-using-different-iceberg-clients "Direct link to example-access-shared-tables-using-different-iceberg-clients")

The following examples show how to access openshared tables using external Iceberg clients, such as Snowflake, Apache Spark, PyIceberg, and REST API, after obtaining your connection credentials. For more on obtaining connection credentials, see [Before you begin](#before).

*   Snowflake
*   Apache Spark
*   PyIceberg
*   REST API

To read shared data assets in Snowflake, upload the credential file you downloaded and generate the necessary SQL command:

1.  From your OpenSharing activation link, click the Snowflake icon.
    
2.  On the Snowflake integration page, upload the credential file you received from the data provider.
    
    ![Upload credential file in Snowflake](https://docs.databricks.com/aws/en/assets/images/upload-cred-snowflake-7db47039137be4e663a4ff8b36afccde.png)
    
3.  After loading the credential, choose the share you want to access in Snowflake.
    
4.  Click **Generate SQL** after selecting the desired assets.
    
    ![Generate SQL command for Snowflake](https://docs.databricks.com/aws/en/assets/images/sql-command-snowflake-605973555847669ea92d9406842bf8fd.png)
    
5.  Copy and paste the generated SQL into your Snowflake worksheet. Replace `CATALOG_PLACEHOLDER` with the name of the catalog you want to use and `DATABASE_PLACEHOLDER` with the name of the database you want to use.
    

**Limitations**

Connecting to the Iceberg REST Catalog in Snowflake has the following limitations:

*   The metadata file doesn't automatically update with the latest snapshot. You must rely on auto-refresh or manual refreshes.
*   R2 is not supported.
*   All [Iceberg client limitations](#iceberg-client-limitations) apply.

### Iceberg client limitations[​](#iceberg-client-limitations "Direct link to iceberg-client-limitations")

The following limitations apply when querying OpenSharing data from Iceberg clients:

*   When listing tables in a namespace, if the namespace contains more than 100 shared views, the response is limited to the first 100 views.

Follow these steps to access shared data using Spark 3.x or above.

These instructions assume that you have access to the credential file that was shared by the data provider. See [Get access in the Databricks-to-Open sharing model](https://docs.databricks.com/aws/en/delta-sharing/recipient#get-access-open).

important

Ensure your credential file is accessible by Apache Spark by using an absolute path. The path can refer to a cloud object or Unity Catalog volume.

note

If you are using Spark on a Databricks workspace that is enabled for Unity Catalog, and you used the import provider UI to import the provider and share, the instructions in this section do not apply to you. You can access shared tables just as you would any other table that is registered in Unity Catalog. You do not need to install the `delta-sharing` Python connector or provide the path to the credential file. See [Databricks: Read shared data using Databricks-to-Open sharing connectors](#databricks-open-connectors).

### Install the OpenSharing Python and Spark connectors[​](#install-the-opensharing-python-and-spark-connectors "Direct link to install-the-opensharing-python-and-spark-connectors")

To access metadata related to the shared data, such as the list of tables shared with you, do the following. This example uses Python.

1.  Install the [delta-sharing Python connector](https://delta.io/connectors/). For information about Python connector limitations, see [OpenSharing Python connector limitations](#python-limitations).
    
    Bash
    
        pip install delta-sharing
    
2.  Install the [Apache Spark connector](https://go.delta.io/sharing).
    

### List shared tables using Spark[​](#list-shared-tables-using-spark "Direct link to List shared tables using Spark")

List the tables in the share. In the following example, replace `<profile-path>` with the location of the credential file.

Python

    import delta_sharingclient = delta_sharing.SharingClient(f"<profile-path>/config.share")client.list_all_tables()

The result is an array of tables, along with metadata for each table. The following output shows two tables:

Console

    Out[10]: [Table(name='example_table', share='example_share_0', schema='default'), Table(name='other_example_table', share='example_share_0', schema='default')]

If the output is empty or doesn't contain the tables you expect, contact the data provider.

### Access shared data using Spark[​](#access-shared-data-using-spark "Direct link to Access shared data using Spark")

Run the following, replacing these variables:

*   `<profile-path>`: the location of the credential file.
*   `<share-name>`: the value of `share=` for the table.
*   `<schema-name>`: the value of `schema=` for the table.
*   `<table-name>`: the value of `name=` for the table.
*   `<version-as-of>`: optional. The version of the table to load the data. Only works if the data provider shares the history of the table. Requires `delta-sharing-spark` 0.5.0 or above.
*   `<timestamp-as-of>`: optional. Load the data at the version before or at the given timestamp. Only works if the data provider shares the history of the table. Requires `delta-sharing-spark` 0.6.0 or above.

*   Python
*   Scala

Python

    delta_sharing.load_as_spark(f"<profile-path>#<share-name>.<schema-name>.<table-name>", version=<version-as-of>)spark.read.format("deltaSharing")\.option("versionAsOf", <version-as-of>)\.load("<profile-path>#<share-name>.<schema-name>.<table-name>")\.limit(10)delta_sharing.load_as_spark(f"<profile-path>#<share-name>.<schema-name>.<table-name>", timestamp=<timestamp-as-of>)spark.read.format("deltaSharing")\.option("timestampAsOf", <timestamp-as-of>)\.load("<profile-path>#<share-name>.<schema-name>.<table-name>")\.limit(10)

### Access shared change data feed using Spark[​](#access-shared-change-data-feed-using-spark "Direct link to Access shared change data feed using Spark")

If the table history has been shared with you and change data feed (CDF) is enabled on the source table, access the change data feed by running the following, replacing these variables. Requires `delta-sharing-spark` 0.5.0 or above.

One start parameter must be provided.

*   `<profile-path>`: the location of the credential file.
*   `<share-name>`: the value of `share=` for the table.
*   `<schema-name>`: the value of `schema=` for the table.
*   `<table-name>`: the value of `name=` for the table.
*   `<starting-version>`: optional. The starting version of the query, inclusive. Specify as a Long.
*   `<ending-version>`: optional. The ending version of the query, inclusive. If the ending version is not provided, the API uses the latest table version.
*   `<starting-timestamp>`: optional. The starting timestamp of the query, this is converted to a version created greater or equal to this timestamp. Specify as a string in the format `yyyy-mm-dd hh:mm:ss[.fffffffff]`.
*   `<ending-timestamp>`: optional. The ending timestamp of the query, this is converted to a version created earlier or equal to this timestamp. Specify as a string in the format `yyyy-mm-dd hh:mm:ss[.fffffffff]`

*   Python
*   Scala

Python

    delta_sharing.load_table_changes_as_spark(f"<profile-path>#<share-name>.<schema-name>.<table-name>",  starting_version=<starting-version>,  ending_version=<ending-version>)delta_sharing.load_table_changes_as_spark(f"<profile-path>#<share-name>.<schema-name>.<table-name>",  starting_timestamp=<starting-timestamp>,  ending_timestamp=<ending-timestamp>)spark.read.format("deltaSharing").option("readChangeFeed", "true")\.option("startingVersion", <starting-version>)\.option("endingVersion", <ending-version>)\.load("<profile-path>#<share-name>.<schema-name>.<table-name>")spark.read.format("deltaSharing").option("readChangeFeed", "true")\.option("startingTimestamp", <starting-timestamp>)\.option("endingTimestamp", <ending-timestamp>)\.load("<profile-path>#<share-name>.<schema-name>.<table-name>")

If the output is empty or doesn't contain the data you expect, contact the data provider.

### Access a shared table using Spark Structured Streaming[​](#access-a-shared-table-using-spark-structured-streaming "Direct link to access-a-shared-table-using-spark-structured-streaming")

If the table history is shared with you, you can stream read the shared data. Requires `delta-sharing-spark` 0.6.0 or above.

Supported options:

*   `ignoreDeletes`: Ignore transactions that delete data.
*   `ignoreChanges`: Re-process updates if files were rewritten in the source table due to a data changing operation such as `UPDATE`, `MERGE INTO`, `DELETE` (within partitions), or `OVERWRITE`. Unchanged rows can still be emitted. Therefore, your downstream consumers should be able to handle duplicates. Deletes are not propagated downstream. `ignoreChanges` subsumes `ignoreDeletes`. Therefore, if you use `ignoreChanges`, your stream is not disrupted by either deletions or updates to the source table.
*   `startingVersion`: The shared table version to start from. All table changes starting from this version (inclusive) are read by the streaming source.
*   `startingTimestamp`: The timestamp to start from. All table changes committed at or after the timestamp (inclusive) are read by the streaming source. Example: `"2023-01-01 00:00:00.0"`.
*   `maxFilesPerTrigger`: The number of new files to be considered in every micro-batch.
*   `maxBytesPerTrigger`: The amount of data that gets processed in each micro-batch. This option sets a “soft max”, meaning that a batch processes approximately this amount of data and may process more than the limit in order to make the streaming query move forward in cases when the smallest input unit is larger than this limit.
*   `readChangeFeed`: Stream read the change data feed of the shared table.

Unsupported options:

*   `Trigger.availableNow`

#### Sample Structured Streaming queries[​](#sample-structured-streaming-queries "Direct link to Sample Structured Streaming queries")

*   Python
*   Scala

Python

    spark.readStream.format("deltaSharing")\.option("startingVersion", 0)\.option("ignoreDeletes", true)\.option("maxBytesPerTrigger", 10000)\.load("<profile-path>#<share-name>.<schema-name>.<table-name>")

See also [Structured Streaming concepts](https://docs.databricks.com/aws/en/structured-streaming/concepts).

### Read tables with deletion vectors or column mapping enabled[​](#read-tables-with-deletion-vectors-or-column-mapping-enabled "Direct link to read-tables-with-deletion-vectors-or-column-mapping-enabled")

Deletion vectors are a storage optimization feature that your provider can enable on shared Delta tables. See [Deletion vectors in Databricks](https://docs.databricks.com/aws/en/tables/features/deletion-vectors).

Databricks also supports column mapping for Delta tables. See [Rename and drop columns with Delta Lake column mapping](https://docs.databricks.com/aws/en/tables/features/column-mapping).

If your provider shared a table with deletion vectors or column mapping enabled, you can read the table using compute that is running `delta-sharing-spark` 3.1 or above. If you are using Databricks clusters, you can perform batch reads using a cluster running Databricks Runtime 14.1 or above. CDF and streaming queries require Databricks Runtime 14.2 or above.

You can perform batch queries as-is, because they can automatically resolve `responseFormat` based on the table features of the shared table.

To read a change data feed (CDF) or to perform streaming queries on shared tables with deletion vectors or column mapping enabled, you must set the additional option `responseFormat=delta`.

The following examples show batch, CDF, and streaming queries:

Scala

    import org.apache.spark.sql.SparkSessionval spark = SparkSession        .builder()        .appName("...")        .master("...")        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")        .getOrCreate()val tablePath = "<profile-file-path>#<share-name>.<schema-name>.<table-name>"// Batch queryspark.read.format("deltaSharing").load(tablePath)// CDF queryspark.read.format("deltaSharing")  .option("readChangeFeed", "true")  .option("responseFormat", "delta")  .option("startingVersion", 1)  .load(tablePath)// Streaming queryspark.readStream.format("deltaSharing").option("responseFormat", "delta").load(tablePath)

### Read row tracking columns in shared tables[​](#read-row-tracking-columns-in-shared-tables "Direct link to read-row-tracking-columns-in-shared-tables")

If the data provider has enabled row tracking on a shared table, you can query the row tracking metadata columns using Scala Spark. See [Row tracking in Databricks](https://docs.databricks.com/aws/en/tables/features/row-tracking) for a list of available columns.

You must set the `responseFormat` option to `delta`.

Scala

    spark.read.format("deltaSharing")  .option("responseFormat", "delta")  .load("<profile-path>#<share-name>.<schema-name>.<table-name>")  .select("_metadata.row_id")  .show()

note

Only the delta response format is supported for querying row tracking columns in the Spark client. Dump connectors are not supported.

Follow these steps to access shared data in `pandas` 0.25.3 or above.

These instructions assume that you have access to the credential file that was shared by the data provider. See [Get access in the Databricks-to-Open sharing model](https://docs.databricks.com/aws/en/delta-sharing/recipient#get-access-open).

note

If you are using `pandas` on a Databricks workspace that is enabled for Unity Catalog, and you used the import provider UI to import the provider and share, the instructions in this section do not apply to you. You can access shared tables just as you would any other table that is registered in Unity Catalog. You do not need to install the `delta-sharing` Python connector or provide the path to the credential file. See [Databricks: Read shared data using Databricks-to-Open sharing connectors](#databricks-open-connectors).

### Install the OpenSharing Python connector[​](#install-the-opensharing-python-connector "Direct link to install-the-opensharing-python-connector")

To access metadata related to the shared data, such as the list of tables shared with you, you must install the [delta-sharing Python connector](https://delta.io/connectors/). For information about Python connector limitations, see [OpenSharing Python connector limitations](#python-limitations).

Bash

    pip install delta-sharing

### List shared tables using `pandas`[​](#list-shared-tables-using-pandas "Direct link to list-shared-tables-using-pandas")

To list the tables in the share, run the following, replacing `<profile-path>/config.share` with the location of the credential file.

Python

    import delta_sharingclient = delta_sharing.SharingClient(f"<profile-path>/config.share")client.list_all_tables()

If the output is empty or doesn't contain the tables you expect, contact the data provider.

### Access shared data using `pandas`[​](#access-shared-data-using-pandas "Direct link to access-shared-data-using-pandas")

To access shared data in `pandas` using Python, run the following, replacing the variables as follows:

*   `<profile-path>`: the location of the credential file.
*   `<share-name>`: the value of `share=` for the table.
*   `<schema-name>`: the value of `schema=` for the table.
*   `<table-name>`: the value of `name=` for the table.

Python

    import delta_sharingdelta_sharing.load_as_pandas(f"<profile-path>#<share-name>.<schema-name>.<table-name>")

### Access a shared change data feed using `pandas`[​](#access-a-shared-change-data-feed-using-pandas "Direct link to access-a-shared-change-data-feed-using-pandas")

To access the change data feed for a shared table in `pandas` using Python run the following, replacing the variables as follows. A change data feed may not be available, depending on whether or not the data provider shared the change data feed for the table.

*   `<starting-version>`: optional. The starting version of the query, inclusive.
*   `<ending-version>`: optional. The ending version of the query, inclusive.
*   `<starting-timestamp>`: optional. The starting timestamp of the query. This is converted to a version created greater or equal to this timestamp.
*   `<ending-timestamp>`: optional. The ending timestamp of the query. This is converted to a version created earlier or equal to this timestamp.

Python

    import delta_sharingdelta_sharing.load_table_changes_as_pandas(  f"<profile-path>#<share-name>.<schema-name>.<table-name>",  starting_version=<starting-version>,  ending_version=<ending-version>)delta_sharing.load_table_changes_as_pandas(  f"<profile-path>#<share-name>.<schema-name>.<table-name>",  starting_timestamp=<starting-timestamp>,  ending_timestamp=<ending-timestamp>)

If the output is empty or doesn't contain the data you expect, contact the data provider.

The Power BI OpenSharing connector allows you to discover, analyze, and visualize datasets shared with you through the OpenSharing open protocol.

### Requirements[​](#requirements "Direct link to Requirements")

*   Power BI Desktop 2.99.621.0 or above.
*   Access to the credential file that was shared by the data provider. See [Get access in the Databricks-to-Open sharing model](https://docs.databricks.com/aws/en/delta-sharing/recipient#get-access-open).

### Connect to Databricks[​](#connect-to-databricks "Direct link to Connect to Databricks")

To connect to Databricks using the OpenSharing connector, do the following:

1.  Open the shared credential file with a text editor to retrieve the endpoint URL and the token.
2.  Open Power BI Desktop.
3.  On the **Get Data** menu, search for **OpenSharing**.
4.  Select the connector and click **Connect**.
5.  Enter the endpoint URL that you copied from the credentials file into the **OpenSharing Server URL** field.
6.  Optionally, in the **Advanced Options** tab, set a **Row Limit** for the maximum number of rows that you can download. This is set to 1 million rows by default.
7.  Click **OK**.
8.  For **Authentication**, copy the token that you retrieved from the credentials file into **Bearer Token**.
9.  Click **Connect**.

### Limitations of the Power BI OpenSharing connector[​](#limitations-of-the-power-bi-opensharing-connector "Direct link to limitations-of-the-power-bi-opensharing-connector")

The Power BI OpenSharing Connector has the following limitations:

*   The data that the connector loads must fit into the memory of your machine. To manage this requirement, the connector limits the number of imported rows to the **Row Limit** that you set under the Advanced Options tab in Power BI Desktop.

The Tableau OpenSharing connector allows you to discover, analyze, and visualize datasets that are shared with you through the OpenSharing open protocol.

### Requirements[​](#requirements-1 "Direct link to Requirements")

*   Tableau Desktop and Tableau Server 2024.1 or above
*   Access to the credential file that was shared by the data provider. See [Get access in the Databricks-to-Open sharing model](https://docs.databricks.com/aws/en/delta-sharing/recipient#get-access-open).

### Connect to Databricks[​](#connect-to-databricks-1 "Direct link to connect-to-databricks-1")

To connect to Databricks using the OpenSharing connector, do the following:

1.  Go to [Tableau Exchange](https://exchange.tableau.com/products/1019), follow the instructions to download the OpenSharing Connector, and put it in an appropriate desktop folder.
2.  Open Tableau Desktop.
3.  On the **Connectors** page, search for “OpenSharing by Databricks”.
4.  Select **Upload Share file**, and choose the credential file that was shared by the provider.
5.  Click **Get Data**.
6.  In the Data Explorer, select the table.
7.  Optionally add SQL filters or row limits.
8.  Click **Get Table Data**.

### Limitations[​](#limitations "Direct link to limitations")

The Tableau OpenSharing Connector has the following limitations:

*   The data that the connector loads must fit into the memory of your machine. To manage this requirement, the connector limits the number of imported rows to the row limit that you set in Tableau.
*   All columns are returned as type `String`.
*   SQL Filter only works if your OpenSharing server supports [predicateHint](https://github.com/delta-io/delta-sharing/blob/main/PROTOCOL.md#request-body).
*   Deletion vectors are not supported.
*   Column mapping is not supported.

## OpenSharing Python connector limitations[​](#-opensharing-python-connector-limitations "Direct link to -opensharing-python-connector-limitations")

These limitations are specific to the OpenSharing Python connector:

*   The OpenSharing Python connector 1.1.0+ supports snapshot queries on tables with column mapping but CDF queries on tables with column mapping are not supported.
*   The OpenSharing Python connector fails CDF queries with `use_delta_format=True` if the schema changed during the queried version range.

## Streaming table limitations[​](#streaming-table-limitations "Direct link to streaming-table-limitations")

You can only read the current snapshot of a shared streaming table. The following features are not supported for streaming tables in Databricks-to-Open sharing:

*   Querying the table's history data
*   Querying the table's change data feed (CDF)
*   Using the table as a source for Spark Structured Streaming

## Materialized view limitations[​](#materialized-view-limitations "Direct link to Materialized view limitations")

You can only read the current snapshot of a shared materialized view. Using a materialized view as a source for Spark Structured Streaming is not supported in Databricks-to-Open sharing.

## Request a new credential[​](#request-a-new-credential "Direct link to Request a new credential")

If your credential activation URL or downloaded credential is lost, corrupted, or compromised, or your credential expires without your provider sending you a new one, contact your provider to request a new credential.

If you're a Databricks recipient who imported the credential as a provider object in Unity Catalog, apply the new credential using the Databricks REST API. See [Rotate credentials for open recipients](https://docs.databricks.com/aws/en/delta-sharing/manage-provider#rotate-credentials).
