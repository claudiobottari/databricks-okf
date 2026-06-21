---
title: Allowlist libraries and init scripts on compute with standard access mode (formerly shared access mode) | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/allowlist
ingestedAt: "2026-06-18T08:04:45.741Z"
---

In Databricks Runtime 13.3 LTS and above, the `allowlist` in Unity Catalog controls which libraries and init scripts can run on standard access mode compute. This allows users to leverage these artifacts on compute configured with standard access mode.

By default, the allowlist is empty. You cannot disable this feature. To modify the allowlist, you must have the `MANAGE ALLOWLIST` privilege. See [MANAGE ALLOWLIST](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/privileges-reference#manage-allowlist).

You can add a directory or file to the allowlist even if it hasn't been created yet. See [Work with files in Unity Catalog volumes](https://docs.databricks.com/aws/en/volumes/volume-files).

important

Libraries used as JDBC drivers or custom Spark data sources on Unity Catalog\-enabled standard compute require `ANY FILE` permissions.

Some installed libraries store data of all users in one common temp directory. These libraries might compromise user isolation.

## Security and operational risks[​](#security-and-operational-risks "Direct link to Security and operational risks")

Understanding the security implications of allowlists is critical for maintaining cluster isolation and protecting your data on standard access mode compute. Proper allowlist usage prevents users from adding arbitrary libraries and init scripts. This reduces the likelihood of security issues, cluster instability, and other unpredictable behavior.

Be deliberate about who receives `MANAGE ALLOWLIST` privileges. Users with `MANAGE ALLOWLIST` privileges can allowlist any path or Maven coordinate, effectively controlling what code can run on standard access mode compute.

As the metastore admin, periodically review items on the allowlist and verify that they come from trusted sources. Allowlisted artifacts can access cluster resources and user data, so they should be subject to the same security and governance controls as other sensitive components.

Databricks recommends these best practices for managing the allowlist:

*   Grant the `MANAGE ALLOWLIST` privilege only to metastore admins and trusted platform administrators. For other users, grant `MANAGE ALLOWLIST` only on a temporary, as-needed basis.
*   Review and audit allowlist additions regularly.
*   Use specific paths and Maven coordinates rather than broad patterns.
*   Configure storage locations for allowlisted artifacts with read-only permissions.
*   Implement a formal approval process for allowlist additions in production environments.
*   Test allowlisted libraries and init scripts in non-production environments before adding them to production allowlists.

## How to add items to the allowlist[​](#how-to-add-items-to-the-allowlist "Direct link to How to add items to the allowlist")

You can add items to the `allowlist` with [Catalog Explorer](https://docs.databricks.com/aws/en/catalog-explorer/) or the [REST API](https://docs.databricks.com/api/workspace/artifactallowlists).

To open the dialog for adding items to the allowlist in Catalog Explorer, do the following:

1.  In your Databricks workspace, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
2.  Click the gear icon ![Gear icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzEzMTIzXzM1MDE5KSI+CjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNNy45ODQzMyA1QzYuMzI3NDcgNSA0Ljk4NDMzIDYuMzQzMTUgNC45ODQzMyA4QzQuOTg0MzMgOS42NTY4NSA2LjMyNzQ3IDExIDcuOTg0MzMgMTFDOS42NDExOCAxMSAxMC45ODQzIDkuNjU2ODUgMTAuOTg0MyA4QzEwLjk4NDMgNi4zNDMxNSA5LjY0MTE4IDUgNy45ODQzMyA1Wk02LjQ4NDMzIDhDNi40ODQzMyA3LjE3MTU3IDcuMTU1OSA2LjUgNy45ODQzMyA2LjVDOC44MTI3NSA2LjUgOS40ODQzMyA3LjE3MTU3IDkuNDg0MzMgOEM5LjQ4NDMzIDguODI4NDMgOC44MTI3NSA5LjUgNy45ODQzMyA5LjVDNy4xNTU5IDkuNSA2LjQ4NDMzIDguODI4NDMgNi40ODQzMyA4WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTcuOTY1NSAwQzcuNjI1NTIgMCA3LjI5MDE0IDAuMDIxMjUxMSA2Ljk2MDcgMC4wNjI1NzM2QzYuNjczMDQgMC4wOTg2NTU4IDYuNDMxOTQgMC4yOTczIDYuMzQxNDggMC41NzI3NDVMNS43MDI0IDIuNTE4ODhDNS40OTI0NCAyLjYwNTY1IDUuMjg4NiAyLjcwNDExIDUuMDkxNyAyLjgxMzQxTDMuMTcxOTggMi4wOTk3OUMyLjkwMDU0IDEuOTk4ODggMi41OTUyNiAyLjA2MzI2IDIuMzg3NjkgMi4yNjUxOUMxLjkwNjkgMi43MzI4OSAxLjQ4NDY0IDMuMjYwNjggMS4xMzMwMSAzLjgzNjYxQzAuOTgxOTgyIDQuMDgzOTkgMC45ODcwMDYgNC4zOTYyNSAxLjE0NTkyIDQuNjM4NjRMMi4yNjkxOSA2LjM1MTk4QzIuMjA2OTIgNi41Njc1NyAyLjE1NjU2IDYuNzg4MTQgMi4xMTg4NSA3LjAxMjkzTDAuMzYzMzIyIDguMDY5MjhDMC4xMTU0ODMgOC4yMTg0MiAtMC4wMjQ1MDg2IDguNDk2NzggMC4wMDM1NDkyOSA4Ljc4NDY2QzAuMDcwMDUzNiA5LjQ2NzAyIDAuMjIyMzY1IDEwLjEyNDggMC40NDk2NjkgMTAuNzQ2NkMwLjU0OTA4NSAxMS4wMTg2IDAuNzk2MTg5IDExLjIwOSAxLjA4NDUxIDExLjIzNTlMMy4xMjY2NyAxMS40MjYxQzMuMjU3MzUgMTEuNjEwNCAzLjM5ODI2IDExLjc4NjggMy41NDg1OCAxMS45NTQ2TDMuMjc5NzQgMTMuOTg3MkMzLjI0MTggMTQuMjc0IDMuMzcyMjIgMTQuNTU3MSAzLjYxNDkgMTQuNzE0NkM0LjE3NDI3IDE1LjA3NzcgNC43ODIxNiAxNS4zNzMgNS40MjY4NiAxNS41ODg2QzUuNzAxNDcgMTUuNjgwNCA2LjAwNDQyIDE1LjYwNiA2LjIwNTE4IDE1LjM5NzNMNy42Mjc0MyAxMy45MTlDNy43MzkzOSAxMy45MjU0IDcuODUyMTEgMTMuOTI4NSA3Ljk2NTUxIDEzLjkyODVDOC4wNzg4OSAxMy45Mjg1IDguMTkxNiAxMy45MjU0IDguMzAzNTQgMTMuOTE5TDkuNzI1OCAxNS4zOTczQzkuOTI2NTYgMTUuNjA2IDEwLjIyOTUgMTUuNjgwNCAxMC41MDQxIDE1LjU4ODZDMTEuMTQ4OCAxNS4zNzMgMTEuNzU2NyAxNS4wNzc3IDEyLjMxNjEgMTQuNzE0NkMxMi41NTg4IDE0LjU1NzEgMTIuNjg5MiAxNC4yNzQgMTIuNjUxMiAxMy45ODcyTDEyLjM4MjQgMTEuOTU0N0MxMi41MzI3IDExLjc4NjkgMTIuNjczNyAxMS42MTA0IDEyLjgwNDMgMTEuNDI2MUwxNC44NDY1IDExLjIzNTlDMTUuMTM0OCAxMS4yMDkgMTUuMzgxOSAxMS4wMTg2IDE1LjQ4MTMgMTAuNzQ2NkMxNS43MDg2IDEwLjEyNDggMTUuODYwOSA5LjQ2NzA0IDE1LjkyNzUgOC43ODQ2OUMxNS45NTU1IDguNDk2OCAxNS44MTU1IDguMjE4NDQgMTUuNTY3NyA4LjA2OTNMMTMuODEyMiA3LjAxMjk2QzEzLjc3NDUgNi43ODgxNSAxMy43MjQxIDYuNTY3NTQgMTMuNjYxOCA2LjM1MTkzTDE0Ljc4NTEgNC42Mzg2MUMxNC45NDQgNC4zOTYyMiAxNC45NDkgNC4wODM5NiAxNC43OTggMy44MzY1OEMxNC40NDYzIDMuMjYwNjUgMTQuMDI0MSAyLjczMjg3IDEzLjU0MzMgMi4yNjUxOEMxMy4zMzU3IDIuMDYzMjUgMTMuMDMwNSAxLjk5ODg3IDEyLjc1OSAyLjA5OTc4TDEwLjgzOTMgMi44MTM0QzEwLjY0MjQgMi43MDQwOSAxMC40Mzg1IDIuNjA1NjMgMTAuMjI4NiAyLjUxODg1TDkuNTg5NDkgMC41NzI3NDFDOS40OTkwMyAwLjI5NzI5NCA5LjI1NzkzIDAuMDk4NjQ5NiA4Ljk3MDI2IDAuMDYyNTY4NkM4LjY0MDgzIDAuMDIxMjQ5NCA4LjMwNTQ4IDAgNy45NjU1IDBaTTcuMDE1NDggMy4zMjgwNUw3LjYxMjcxIDEuNTA5MzlDNy43Mjk0NiAxLjUwMzE2IDcuODQ3MDggMS41IDcuOTY1NSAxLjVDOC4wODM5MSAxLjUgOC4yMDE1MyAxLjUwMzE2IDguMzE4MjYgMS41MDkzOUw4LjkxNTQ4IDMuMzI4MDRDOC45ODkxIDMuNTUyMjEgOS4xNjM5MiAzLjcyODY4IDkuMzg3NCAzLjgwNDM4QzkuNzMxNjEgMy45MjA5OSAxMC4wNTcxIDQuMDc4OTIgMTAuMzU3OCA0LjI3MjQyQzEwLjU1NjQgNC40MDAxOSAxMC44MDM2IDQuNDI2OTYgMTEuMDI1IDQuMzQ0NjhMMTIuODIgMy42Nzc0QzEyLjk3NjQgMy44NTI5IDEzLjEyMzQgNC4wMzY5MSAxMy4yNjAyIDQuMjI4NjNMMTIuMjEwNSA1LjgyOTgyQzEyLjA4MTEgNi4wMjcxMyAxMi4wNTIyIDYuMjczODIgMTIuMTMyMyA2LjQ5NTc0QzEyLjI1MjUgNi44Mjg3OCAxMi4zMzQgNy4xODA1OCAxMi4zNzEyIDcuNTQ1OTdDMTIuMzk1IDcuNzgwOTcgMTIuNTI4MiA3Ljk5MDk5IDEyLjczMDYgOC4xMTI3N0wxNC4zNzI4IDkuMTAwOTJDMTQuMzMzIDkuMzM0NTIgMTQuMjgwNyA5LjU2Mzc5IDE0LjIxNjcgOS43ODgwNkwxMi4zMDggOS45NjU4N0MxMi4wNzM0IDkuOTg3NzMgMTEuODYyNyAxMC4xMTg2IDExLjczOTEgMTAuMzE5MkMxMS41NDk2IDEwLjYyNjggMTEuMzIzNCAxMC45MDk2IDExLjA2NjYgMTEuMTYxNkMxMC44OTgyIDExLjMyNjcgMTAuODE3MyAxMS41NjE1IDEwLjg0ODMgMTEuNzk1M0wxMS4wOTk3IDEzLjY5NkMxMC44OTQ2IDEzLjgwOTEgMTAuNjgyOCAxMy45MTE0IDEwLjQ2NTEgMTQuMDAyMkw5LjEzNTg0IDEyLjYyMDZDOC45NzI1MiAxMi40NTA5IDguNzM4OTQgMTIuMzY3NyA4LjUwNTA5IDEyLjM5NjFDOC4zMjg1MiAxMi40MTc1IDguMTQ4NDcgMTIuNDI4NSA3Ljk2NTUxIDEyLjQyODVDNy43ODI1MyAxMi40Mjg1IDcuNjAyNDcgMTIuNDE3NSA3LjQyNTg5IDEyLjM5NjFDNy4xOTIwNCAxMi4zNjc3IDYuOTU4NDYgMTIuNDUwOSA2Ljc5NTE0IDEyLjYyMDZMNS40NjU4OSAxNC4wMDIyQzUuMjQ4MTYgMTMuOTExNCA1LjAzNjM4IDEzLjgwOTEgNC44MzEzMSAxMy42OTZMNS4wODI3MiAxMS43OTUzQzUuMTEzNjUgMTEuNTYxNSA1LjAzMjc4IDExLjMyNjcgNC44NjQ0MiAxMS4xNjE1QzQuNjA3NjEgMTAuOTA5NiA0LjM4MTQ0IDEwLjYyNjggNC4xOTE5NSAxMC4zMTkyQzQuMDY4MzMgMTAuMTE4NiAzLjg1NzYyIDkuOTg3NzMgMy42MjI5OSA5Ljk2NTg3TDEuNzE0MzMgOS43ODgwNkMxLjY1MDMyIDkuNTYzNzkgMS41OTgwNCA5LjMzNDUxIDEuNTU4MjIgOS4xMDA5TDMuMjAwNCA4LjExMjc1QzMuNDAyNzkgNy45OTA5NiAzLjUzNTk5IDcuNzgwOTUgMy41NTk4NyA3LjU0NTk1QzMuNTk3IDcuMTgwNTggMy42Nzg0NyA2LjgyODggMy43OTg3MiA2LjQ5NTc4QzMuODc4ODQgNi4yNzM4NiAzLjg0OTg4IDYuMDI3MTggMy43MjA1MSA1LjgyOTg2TDIuNjcwNzYgNC4yMjg2NUMyLjgwNzU5IDQuMDM2OTMgMi45NTQ2IDMuODUyOTIgMy4xMTEgMy42Nzc0MUw0LjkwNjA1IDQuMzQ0NjlDNS4xMjc0IDQuNDI2OTcgNS4zNzQ1NyA0LjQwMDIgNS41NzMxNyA0LjI3MjQzQzUuODczOTQgNC4wNzg5MyA2LjE5OTM3IDMuOTIxMDEgNi41NDM1NyAzLjgwNDRDNi43NjcwNSAzLjcyODY5IDYuOTQxODcgMy41NTIyMyA3LjAxNTQ4IDMuMzI4MDVaIiBmaWxsPSIjNkY2RjZGIi8+CjwvZz4KPGRlZnM+CjxjbGlwUGF0aCBpZD0iY2xpcDBfMTMxMjNfMzUwMTkiPgo8cmVjdCB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGZpbGw9IndoaXRlIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==).
3.  Click the metastore name to open the metastore details and permissions UI.
4.  Select **Allowed JARs/Init Scripts**.
5.  Click **Add**.

important

This option only displays for users with the `MANAGE ALLOWLIST` privilege on the metastore. If you cannot access the allowlist UI, contact your [metastore admin](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/admin-privileges#metastore-admins) for assistance in allowlisting libraries and init scripts.

## Add an init script to the allowlist[​](#add-an-init-script-to-the-allowlist "Direct link to add-an-init-script-to-the-allowlist")

Complete the following steps in the allowlist dialog to add an init script to the allowlist:

1.  For **Type**, select **Init Script**.
2.  For **Source Type**, select **Volume** or the object storage protocol.
3.  Specify the source path to add to the allowlist. See [How are permissions on paths enforced in the allowlist?](#paths).

## Add a JAR to the allowlist[​](#add-a-jar-to-the-allowlist "Direct link to Add a JAR to the allowlist")

Complete the following steps in the allowlist dialog to add a JAR to the allowlist:

1.  For **Type**, select **JAR**.
2.  For **Source Type**, select **Volume** or the object storage protocol.
3.  Specify the source path to add to the allowlist. See [How are permissions on paths enforced in the allowlist?](#paths).

## Add Maven coordinates to the allowlist[​](#add-maven-coordinates-to-the-allowlist "Direct link to add-maven-coordinates-to-the-allowlist")

important

Before adding Maven coordinates to the allowlist, you must have CAN ATTACH TO and CAN MANAGE permissions set on the compute where you want to install the library. See [Compute permissions](https://docs.databricks.com/aws/en/compute/clusters-manage#compute-permissions).

Complete the following steps in the allowlist dialog to add Maven coordinates to the allowlist:

1.  For **Type**, select **Maven**.
2.  For **Source Type**, select **Coordinates**.
3.  Enter coordinates in the following format: `groudId:artifactId:version`.
    *   You can include all versions of a library by allowlisting the following format: `groudId:artifactId`.
    *   You can include all artifacts in a group by allowlisting the following format: `groupId`.

## How are permissions on paths enforced in the allowlist?[​](#how-are-permissions-on-paths-enforced-in-the-allowlist "Direct link to how-are-permissions-on-paths-enforced-in-the-allowlist")

You can use the allowlist to grant access to JARs or init scripts stored in Unity Catalog volumes and object storage. If you add a path for a directory rather than a file, allowlist permissions propagate to contained files and directories.

Prefix matching is used for all artifacts stored in Unity Catalog volumes or object storage. To prevent prefix matching at a given directory level, include a trailing slash (`/`). For example, `/Volumes/prod-libraries/` will not perform prefix matching for files prefixed with `prod-libraries`. Instead, all files and directories within `/Volumes/prod-libraries/` are added to the allowlist.

You can define permissions at the following levels:

1.  The base path for the volume or storage container.
2.  A directory nested at any depth from the base path.
3.  A single file.

Adding a path to the allowlist only means that the path can be used for either init scripts or JAR installation. Databricks still checks for permissions to access data in the specified location.

The principal used must have `READ VOLUME` permissions on the specified volume. See [READ VOLUME](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/privileges-reference#read-volume).

In dedicated access mode (formerly single user access mode), the identity of the assigned principal (a user or group) is used.

In standard access mode:

*   Libraries use the identity of the library installer.
*   Init scripts use the identity of the cluster owner.

note

No-isolation shared access mode does not support volumes, but uses the same identity assignment as standard access mode.

Databricks recommends configuring all object storage privileges related to init scripts and libraries with read-only permissions. Users with write permissions on these locations can potentially modify code in library files or init scripts.

Databricks recommends using instance profiles to manage access to JARs or init scripts stored in S3. Use the following documentation in the cross-reference link to complete this setup:

1.  Create a IAM role with read and list permissions on your desired buckets. See [Tutorial: Configure S3 access with an instance profile](https://docs.databricks.com/aws/en/archive/storage/tutorial-s3-instance-profile).
2.  Launch a cluster with the instance profile. See [Instance profiles](https://docs.databricks.com/aws/en/compute/configure#instance-profiles).

note

Allowlist permissions for JARs and init scripts are managed separately. If you use the same location to store both types of objects, you must add the location to the allowlist for each.
