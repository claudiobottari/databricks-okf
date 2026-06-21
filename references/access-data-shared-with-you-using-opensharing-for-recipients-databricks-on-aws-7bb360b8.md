---
title: Access data shared with you using OpenSharing (for recipients) | Databricks on AWS
source: https://docs.databricks.com/aws/en/delta-sharing/recipient
ingestedAt: "2026-06-18T08:05:38.496Z"
---

This page explains how to access data that has been shared with you using OpenSharing. OpenSharing supports two models: Databricks-to-Databricks sharing, for Databricks workspace users with Unity Catalog, and Databricks-to-Open sharing, for any recipient using any tool.

## OpenSharing and data recipients[​](#opensharing-and-data-recipients "Direct link to opensharing-and-data-recipients")

OpenSharing is an open standard for secure data sharing. A Databricks user, referred to as a _data provider_ in this context, can use OpenSharing on Databricks to share data with a person or group outside of their organization, called a _data recipient_.

### Databricks-to-Databricks sharing and Databricks-to-Open sharing[​](#databricks-to-databricks-sharing-and-databricks-to-open-sharing "Direct link to databricks-to-databricks-sharing-and-databricks-to-open-sharing")

How you access the data depends on whether you yourself are a Databricks user and whether or not your data provider configured the data being shared with you for _Databricks-to-Databricks_ sharing or _open sharing_.

**In the Databricks-to-Databricks model**, you must be a user on a Databricks workspace that is enabled for [Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/). A member of your team provides the data provider with a unique identifier for your Unity Catalog metastore, and the data provider uses that to create a secure sharing connection. The shared data becomes available for access in your workspace. If necessary, a member of your team configures granular access control on that data.

**In the Databricks-to-Open sharing model**, you can use any tool you like (including Databricks) to access the shared data. The data provider sends you an activation URL or a portal link over a secure channel. You follow it to download a credential file or URL that lets you access the data shared with you.

The shared data is not provided by Databricks directly but by data providers running on Databricks.

note

Databricks may collect information about data recipients' use of and access to the shared data (including identifying any individual or company who accesses the data using the credential file in connection with such information) and may share it with the applicable data provider.

How you access the data depends on whether your data provider shared data with you using the Databricks-to-Open sharing protocol or the Databricks-to-Databricks sharing protocol. See [Databricks-to-Databricks sharing and Databricks-to-Open sharing](#open-sharing-vs-db-to-db).

### Get access in the Databricks-to-Databricks model[​](#get-access-in-the-databricks-to-databricks-model "Direct link to get-access-in-the-databricks-to-databricks-model")

tip

Use VPC gateway endpoints or [interface endpoints for S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html#create-gateway-endpoint-s3) instead of NAT gateways for in-region storage access whenever possible to reduce costs and enhance security.

In the Databricks-to-Databricks model:

1.  The data provider sends you instructions for finding a unique identifier for the [Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/) metastore associated with your Databricks workspace, and you send it to them.
    
    The sharing identifier is a string consisting of the metastore's cloud, region, and UUID (the unique identifier for the metastore), in the format `<cloud>:<region>:<uuid>`. For example, `aws:eu-west-1:b0c978c8-3e68-4cdf-94af-d05c120ed1ef`.
    
    To get the sharing identifier using Catalog Explorer:
    
    1.  In your Databricks workspace, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
        
    2.  At the top of the **Catalog** pane, click the ![Gear icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzEzMTIzXzM1MDE5KSI+CjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNNy45ODQzMyA1QzYuMzI3NDcgNSA0Ljk4NDMzIDYuMzQzMTUgNC45ODQzMyA4QzQuOTg0MzMgOS42NTY4NSA2LjMyNzQ3IDExIDcuOTg0MzMgMTFDOS42NDExOCAxMSAxMC45ODQzIDkuNjU2ODUgMTAuOTg0MyA4QzEwLjk4NDMgNi4zNDMxNSA5LjY0MTE4IDUgNy45ODQzMyA1Wk02LjQ4NDMzIDhDNi40ODQzMyA3LjE3MTU3IDcuMTU1OSA2LjUgNy45ODQzMyA2LjVDOC44MTI3NSA2LjUgOS40ODQzMyA3LjE3MTU3IDkuNDg0MzMgOEM5LjQ4NDMzIDguODI4NDMgOC44MTI3NSA5LjUgNy45ODQzMyA5LjVDNy4xNTU5IDkuNSA2LjQ4NDMzIDguODI4NDMgNi40ODQzMyA4WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTcuOTY1NSAwQzcuNjI1NTIgMCA3LjI5MDE0IDAuMDIxMjUxMSA2Ljk2MDcgMC4wNjI1NzM2QzYuNjczMDQgMC4wOTg2NTU4IDYuNDMxOTQgMC4yOTczIDYuMzQxNDggMC41NzI3NDVMNS43MDI0IDIuNTE4ODhDNS40OTI0NCAyLjYwNTY1IDUuMjg4NiAyLjcwNDExIDUuMDkxNyAyLjgxMzQxTDMuMTcxOTggMi4wOTk3OUMyLjkwMDU0IDEuOTk4ODggMi41OTUyNiAyLjA2MzI2IDIuMzg3NjkgMi4yNjUxOUMxLjkwNjkgMi43MzI4OSAxLjQ4NDY0IDMuMjYwNjggMS4xMzMwMSAzLjgzNjYxQzAuOTgxOTgyIDQuMDgzOTkgMC45ODcwMDYgNC4zOTYyNSAxLjE0NTkyIDQuNjM4NjRMMi4yNjkxOSA2LjM1MTk4QzIuMjA2OTIgNi41Njc1NyAyLjE1NjU2IDYuNzg4MTQgMi4xMTg4NSA3LjAxMjkzTDAuMzYzMzIyIDguMDY5MjhDMC4xMTU0ODMgOC4yMTg0MiAtMC4wMjQ1MDg2IDguNDk2NzggMC4wMDM1NDkyOSA4Ljc4NDY2QzAuMDcwMDUzNiA5LjQ2NzAyIDAuMjIyMzY1IDEwLjEyNDggMC40NDk2NjkgMTAuNzQ2NkMwLjU0OTA4NSAxMS4wMTg2IDAuNzk2MTg5IDExLjIwOSAxLjA4NDUxIDExLjIzNTlMMy4xMjY2NyAxMS40MjYxQzMuMjU3MzUgMTEuNjEwNCAzLjM5ODI2IDExLjc4NjggMy41NDg1OCAxMS45NTQ2TDMuMjc5NzQgMTMuOTg3MkMzLjI0MTggMTQuMjc0IDMuMzcyMjIgMTQuNTU3MSAzLjYxNDkgMTQuNzE0NkM0LjE3NDI3IDE1LjA3NzcgNC43ODIxNiAxNS4zNzMgNS40MjY4NiAxNS41ODg2QzUuNzAxNDcgMTUuNjgwNCA2LjAwNDQyIDE1LjYwNiA2LjIwNTE4IDE1LjM5NzNMNy42Mjc0MyAxMy45MTlDNy43MzkzOSAxMy45MjU0IDcuODUyMTEgMTMuOTI4NSA3Ljk2NTUxIDEzLjkyODVDOC4wNzg4OSAxMy45Mjg1IDguMTkxNiAxMy45MjU0IDguMzAzNTQgMTMuOTE5TDkuNzI1OCAxNS4zOTczQzkuOTI2NTYgMTUuNjA2IDEwLjIyOTUgMTUuNjgwNCAxMC41MDQxIDE1LjU4ODZDMTEuMTQ4OCAxNS4zNzMgMTEuNzU2NyAxNS4wNzc3IDEyLjMxNjEgMTQuNzE0NkMxMi41NTg4IDE0LjU1NzEgMTIuNjg5MiAxNC4yNzQgMTIuNjUxMiAxMy45ODcyTDEyLjM4MjQgMTEuOTU0N0MxMi41MzI3IDExLjc4NjkgMTIuNjczNyAxMS42MTA0IDEyLjgwNDMgMTEuNDI2MUwxNC44NDY1IDExLjIzNTlDMTUuMTM0OCAxMS4yMDkgMTUuMzgxOSAxMS4wMTg2IDE1LjQ4MTMgMTAuNzQ2NkMxNS43MDg2IDEwLjEyNDggMTUuODYwOSA5LjQ2NzA0IDE1LjkyNzUgOC43ODQ2OUMxNS45NTU1IDguNDk2OCAxNS44MTU1IDguMjE4NDQgMTUuNTY3NyA4LjA2OTNMMTMuODEyMiA3LjAxMjk2QzEzLjc3NDUgNi43ODgxNSAxMy43MjQxIDYuNTY3NTQgMTMuNjYxOCA2LjM1MTkzTDE0Ljc4NTEgNC42Mzg2MUMxNC45NDQgNC4zOTYyMiAxNC45NDkgNC4wODM5NiAxNC43OTggMy44MzY1OEMxNC40NDYzIDMuMjYwNjUgMTQuMDI0MSAyLjczMjg3IDEzLjU0MzMgMi4yNjUxOEMxMy4zMzU3IDIuMDYzMjUgMTMuMDMwNSAxLjk5ODg3IDEyLjc1OSAyLjA5OTc4TDEwLjgzOTMgMi44MTM0QzEwLjY0MjQgMi43MDQwOSAxMC40Mzg1IDIuNjA1NjMgMTAuMjI4NiAyLjUxODg1TDkuNTg5NDkgMC41NzI3NDFDOS40OTkwMyAwLjI5NzI5NCA5LjI1NzkzIDAuMDk4NjQ5NiA4Ljk3MDI2IDAuMDYyNTY4NkM4LjY0MDgzIDAuMDIxMjQ5NCA4LjMwNTQ4IDAgNy45NjU1IDBaTTcuMDE1NDggMy4zMjgwNUw3LjYxMjcxIDEuNTA5MzlDNy43Mjk0NiAxLjUwMzE2IDcuODQ3MDggMS41IDcuOTY1NSAxLjVDOC4wODM5MSAxLjUgOC4yMDE1MyAxLjUwMzE2IDguMzE4MjYgMS41MDkzOUw4LjkxNTQ4IDMuMzI4MDRDOC45ODkxIDMuNTUyMjEgOS4xNjM5MiAzLjcyODY4IDkuMzg3NCAzLjgwNDM4QzkuNzMxNjEgMy45MjA5OSAxMC4wNTcxIDQuMDc4OTIgMTAuMzU3OCA0LjI3MjQyQzEwLjU1NjQgNC40MDAxOSAxMC44MDM2IDQuNDI2OTYgMTEuMDI1IDQuMzQ0NjhMMTIuODIgMy42Nzc0QzEyLjk3NjQgMy44NTI5IDEzLjEyMzQgNC4wMzY5MSAxMy4yNjAyIDQuMjI4NjNMMTIuMjEwNSA1LjgyOTgyQzEyLjA4MTEgNi4wMjcxMyAxMi4wNTIyIDYuMjczODIgMTIuMTMyMyA2LjQ5NTc0QzEyLjI1MjUgNi44Mjg3OCAxMi4zMzQgNy4xODA1OCAxMi4zNzEyIDcuNTQ1OTdDMTIuMzk1IDcuNzgwOTcgMTIuNTI4MiA3Ljk5MDk5IDEyLjczMDYgOC4xMTI3N0wxNC4zNzI4IDkuMTAwOTJDMTQuMzMzIDkuMzM0NTIgMTQuMjgwNyA5LjU2Mzc5IDE0LjIxNjcgOS43ODgwNkwxMi4zMDggOS45NjU4N0MxMi4wNzM0IDkuOTg3NzMgMTEuODYyNyAxMC4xMTg2IDExLjczOTEgMTAuMzE5MkMxMS41NDk2IDEwLjYyNjggMTEuMzIzNCAxMC45MDk2IDExLjA2NjYgMTEuMTYxNkMxMC44OTgyIDExLjMyNjcgMTAuODE3MyAxMS41NjE1IDEwLjg0ODMgMTEuNzk1M0wxMS4wOTk3IDEzLjY5NkMxMC44OTQ2IDEzLjgwOTEgMTAuNjgyOCAxMy45MTE0IDEwLjQ2NTEgMTQuMDAyMkw5LjEzNTg0IDEyLjYyMDZDOC45NzI1MiAxMi40NTA5IDguNzM4OTQgMTIuMzY3NyA4LjUwNTA5IDEyLjM5NjFDOC4zMjg1MiAxMi40MTc1IDguMTQ4NDcgMTIuNDI4NSA3Ljk2NTUxIDEyLjQyODVDNy43ODI1MyAxMi40Mjg1IDcuNjAyNDcgMTIuNDE3NSA3LjQyNTg5IDEyLjM5NjFDNy4xOTIwNCAxMi4zNjc3IDYuOTU4NDYgMTIuNDUwOSA2Ljc5NTE0IDEyLjYyMDZMNS40NjU4OSAxNC4wMDIyQzUuMjQ4MTYgMTMuOTExNCA1LjAzNjM4IDEzLjgwOTEgNC44MzEzMSAxMy42OTZMNS4wODI3MiAxMS43OTUzQzUuMTEzNjUgMTEuNTYxNSA1LjAzMjc4IDExLjMyNjcgNC44NjQ0MiAxMS4xNjE1QzQuNjA3NjEgMTAuOTA5NiA0LjM4MTQ0IDEwLjYyNjggNC4xOTE5NSAxMC4zMTkyQzQuMDY4MzMgMTAuMTE4NiAzLjg1NzYyIDkuOTg3NzMgMy42MjI5OSA5Ljk2NTg3TDEuNzE0MzMgOS43ODgwNkMxLjY1MDMyIDkuNTYzNzkgMS41OTgwNCA5LjMzNDUxIDEuNTU4MjIgOS4xMDA5TDMuMjAwNCA4LjExMjc1QzMuNDAyNzkgNy45OTA5NiAzLjUzNTk5IDcuNzgwOTUgMy41NTk4NyA3LjU0NTk1QzMuNTk3IDcuMTgwNTggMy42Nzg0NyA2LjgyODggMy43OTg3MiA2LjQ5NTc4QzMuODc4ODQgNi4yNzM4NiAzLjg0OTg4IDYuMDI3MTggMy43MjA1MSA1LjgyOTg2TDIuNjcwNzYgNC4yMjg2NUMyLjgwNzU5IDQuMDM2OTMgMi45NTQ2IDMuODUyOTIgMy4xMTEgMy42Nzc0MUw0LjkwNjA1IDQuMzQ0NjlDNS4xMjc0IDQuNDI2OTcgNS4zNzQ1NyA0LjQwMDIgNS41NzMxNyA0LjI3MjQzQzUuODczOTQgNC4wNzg5MyA2LjE5OTM3IDMuOTIxMDEgNi41NDM1NyAzLjgwNDRDNi43NjcwNSAzLjcyODY5IDYuOTQxODcgMy41NTIyMyA3LjAxNTQ4IDMuMzI4MDVaIiBmaWxsPSIjNkY2RjZGIi8+CjwvZz4KPGRlZnM+CjxjbGlwUGF0aCBpZD0iY2xpcDBfMTMxMjNfMzUwMTkiPgo8cmVjdCB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9IndoaXRlIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==) gear icon and select **OpenSharing**.
        
        Alternatively, in the upper-right corner, click **Share > OpenSharing**.
        
    3.  On the **Shared with me** tab, select your Databricks sharing organization name in the upper right, and select **Copy sharing identifier**.
        
    
    To get the sharing identifier using a notebook or Databricks SQL query, use the default SQL function `CURRENT_METASTORE`. If you use a notebook, it must run on a [standard or dedicated access mode](https://docs.databricks.com/aws/en/compute/configure#access-mode) in the workspace you will use to access the shared data.
    
    SQL
    
        SELECT CURRENT_METASTORE();
    
2.  The data provider creates:
    
    *   A _recipient_ in their Databricks account to represent you and the users in your organization who will access the data.
    *   A _share_, which is a representation of the tables, volumes, and views to be shared with you.
3.  You access the data shared with you. You or someone on your team can, if necessary, configure granular data access on that data for your users. See [Read data shared using Databricks-to-Databricks OpenSharing (for recipients)](https://docs.databricks.com/aws/en/delta-sharing/read-data-databricks).
    

### Get access in the Databricks-to-Open sharing model[​](#get-access-in-the-databricks-to-open-sharing-model "Direct link to get-access-in-the-databricks-to-open-sharing-model")

In the Databricks-to-Open sharing model:

1.  The data provider creates:
    
    *   A _recipient_ in their Databricks account to represent you and the users in your organization who will access the data.
    *   A _share_, which is a representation of the tables and partitions to be shared with you.
2.  The data provider sends you either an activation URL (over a secure channel) or a portal URL. You follow it to download a credential file or a URL that lets you access the data shared with you.
    
    Both bearer tokens and OAuth Client Credentials are supported.
    
    important
    
    Don't share the activation link with anyone. You can download a credential file only once. If you visit the activation link again after the credential file has already downloaded, the **Download Credential File** button is disabled.
    
    If you lose the activation link before you use it, contact the data provider.
    
3.  Store the credential file in a secure location.
    
    Don't share the credential file with anyone outside the group of users who should have access to the shared data. If you need to share it with someone in your organization, Databricks recommends using a password manager.
    

How you read data that has been shared securely with you using OpenSharing depends on whether you received a credential file (the Databricks-to-Open sharing model) or you are using a Databricks workspace and you provided the data provider with your sharing identifier (the Databricks-to-Databricks model).

### Read shared data using a credential file (Databricks-to-Open sharing)[​](#read-shared-data-using-a-credential-file-databricks-to-open-sharing "Direct link to read-shared-data-using-a-credential-file-databricks-to-open-sharing")

If data has been shared with you using the OpenSharing Databricks-to-Open sharing protocol with bearer tokens, you use the credential file that you downloaded to authenticate to the data provider's account and read the shared data. Access persists as long as the underlying token is valid and the provider continues to share the data. Providers manage token expiration and rotation. Tokens are valid for a maximum of one year after creation. Updates to the data are available to you in near real time. You can read and make copies of the shared data, but you can't modify the source data.

To learn how to access and read shared data using the credential file in Databricks, Apache Spark, pandas, and Power BI, see [Read data shared using OpenSharing Databricks-to-Open sharing with bearer tokens](https://docs.databricks.com/aws/en/delta-sharing/read-data-open).

### Read shared data using a OIDC federation (Databricks-to-Open sharing)[​](#read-shared-data-using-a-oidc-federation-databricks-to-open-sharing "Direct link to read-shared-data-using-a-oidc-federation-databricks-to-open-sharing")

If data has been shared with you using the OpenSharing Databricks-to-Open sharing protocol with OIDC federation, you use the URL that was sent to you to authenticate to the data provider's account and read the shared data. Access persists as long as the provider continues to share the data. Updates to the data are available to you in near real time. You can read and make copies of the shared data, but you can't modify the source data.

To learn how to access and read shared data using the OIDC token federation flow in Tableau and Power BI, see [Read data shared using Open ID Connect (OIDC) federation in a U2M flow](https://docs.databricks.com/aws/en/delta-sharing/sharing-over-oidc-u2m). To learn how to access and read shared data using the OIDC token federation flow in a Python client app, see [Read data shared using Open ID Connect (OIDC) federation in an M2M flow](https://docs.databricks.com/aws/en/delta-sharing/sharing-over-oidc-m2m).

### Read shared data using Databricks-to-Databricks sharing[​](#read-shared-data-using-databricks-to-databricks-sharing "Direct link to Read shared data using Databricks-to-Databricks sharing")

If data has been shared with you using the Databricks-to-Databricks model, then no credential file is required to access the shared data. Databricks takes care of the secure connection, and the shared data is automatically discoverable in your Databricks workspace.

To learn how to find, read, and manage that shared data in your Databricks workspace, see [Read data shared using Databricks-to-Databricks OpenSharing (for recipients)](https://docs.databricks.com/aws/en/delta-sharing/read-data-databricks).

If you have access to a Databricks workspace, you can use Databricks audit logs to understand who in your organization is accessing which data using OpenSharing. See [Audit and monitor data sharing](https://docs.databricks.com/aws/en/delta-sharing/audit-logs).

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Learn more about Databricks](https://docs.databricks.com/aws/en/introduction/)
*   [Learn more about OpenSharing](https://opensharing.io/)
*   [Learn more about Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/)
*   [Troubleshoot common sharing issues in OpenSharing](https://docs.databricks.com/aws/en/delta-sharing/troubleshooting)
