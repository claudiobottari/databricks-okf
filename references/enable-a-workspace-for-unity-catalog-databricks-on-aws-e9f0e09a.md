---
title: Enable a workspace for Unity Catalog | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/enable-workspaces
ingestedAt: "2026-06-18T08:04:28.050Z"
---

This article explains how to enable a workspace for Unity Catalog by assigning a Unity Catalog metastore. This article applies only when you are upgrading an existing non-Unity Catalog workspace to use Unity Catalog.

important

On November 8, 2023, Databricks started to enable new workspaces for Unity Catalog automatically, with a rollout proceeding gradually. If your workspace was enabled for Unity Catalog automatically, this article does not apply to you.

To determine if your workspace is already enabled for Unity Catalog, see [Step 1: Confirm that your workspace is enabled for Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/setup-uc#confirm-uc).

## About enabling workspaces for Unity Catalog[​](#about-enabling-workspaces-for-unity-catalog "Direct link to about-enabling-workspaces-for-unity-catalog")

Enabling Unity Catalog for a workspace means that:

*   Users in that workspace can potentially access the same data that users in other workspaces in your account can access, and data stewards can manage that data access centrally, across workspaces
*   Data access is audited automatically
*   Identity federation is enabled for the workspace, allowing admins to [manage identities](https://docs.databricks.com/aws/en/admin/users-groups/) centrally using the account console and other account-level interfaces. This includes [assigning users to workspaces](https://docs.databricks.com/aws/en/admin/users-groups/#assign-users-to-workspaces).

To enable a Databricks workspace for Unity Catalog, you assign the workspace to a [Unity Catalog metastore](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#metastore). A metastore is the top-level container for data in Unity Catalog. Each metastore exposes a three-level namespace (that is, `catalog`.`schema`.`table`) by which data can be organized.

You can share a single metastore across multiple Databricks workspaces in an account. Each linked workspace has the same view of the data in the metastore, and you can manage data access control across workspaces. You can create one metastore per region and attach it to any number of workspaces in that region.

## Considerations before you enable a workspace for Unity Catalog[​](#considerations-before-you-enable-a-workspace-for-unity-catalog "Direct link to considerations-before-you-enable-a-workspace-for-unity-catalog")

Before you enable a workspace for Unity Catalog, you should:

*   Understand the privileges of workspace admins in workspaces that are enabled for Unity Catalog, and review your existing workspace admin assignments.
    
    Workspace admin is a privileged role that you should distribute carefully.
    
    Workspace admins can manage operations for their workspace including adding users and service principals, creating clusters, and delegating other users to be workspace admins. If your workspace was enabled for Unity Catalog automatically, the workspace admin also has a number of additional privileges by default, including the ability to create most Unity Catalog object types and grant access to the ones they create. See [Admin privileges in Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/admin-privileges).
    
    If your workspace was not enabled for Unity Catalog automatically, then your workspace admins have no more access to Unity Catalog objects by default than any other user, but they do have the ability to perform workspace management tasks such as managing job ownership and viewing notebooks, which may give indirect access to data registered in Unity Catalog.
    
    Account admins can restrict workspace admin privileges using the `RestrictWorkspaceAdmins` setting. See [Restrict workspace admins](https://docs.databricks.com/aws/en/admin/workspace-settings/restrict-workspace-admins).
    
    If you use workspaces to isolate user data access, you might want to use workspace-catalog bindings. Workspace-catalog bindings enable you to limit catalog access by workspace boundaries. For example, you can ensure that workspace admins and users can only access production data in `prod_catalog` from a production workspace environment, `prod_workspace`. The default is to share the catalog with all workspaces attached to the current metastore. Likewise, you can bind access to external locations such that they are accessible only from specified workspaces. See [Workspace-catalog binding](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/workspace-catalog-binding) and [Assign an external location to specific workspaces](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/manage-external-locations#workspace-binding).
    
*   Update any automation that has been configured to manage users, groups, and service principals, such as SCIM provisioning connectors and Terraform automation, so that they refer to account endpoints instead of workspace endpoints. See [Account-level and workspace-level SCIM provisioning](https://docs.databricks.com/aws/en/admin/users-groups/scim/#account-workspace-scim).
    
*   Be aware that enabling a workspace for Unity Catalog cannot be reversed. Once you enable the workspace, you will manage users, groups, and service principals for this workspace using account-level interfaces.
    

## Requirements[​](#requirements "Direct link to Requirements")

Before you can enable your workspace for Unity Catalog, you must have a Unity Catalog metastore configured for your Databricks account. See [Create a Unity Catalog metastore](https://docs.databricks.com/aws/en/data-governance/unity-catalog/create-metastore).

## Enable your workspace for Unity Catalog[​](#enable-your-workspace-for-unity-catalog "Direct link to enable-your-workspace-for-unity-catalog")

When you create a metastore, you are prompted to assign workspaces to that metastore, which enables those workspaces for Unity Catalog. You can also return to the account console to enable a workspace for Unity Catalog at any time, including when you create workspaces using the account console. Note that most workspaces are automatically enabled for Unity Catalog when you create them. See [Get started with Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/get-started).

To enable an existing workspace for Unity Catalog using the account console:

1.  As an account admin, log in to the [account console](https://accounts.cloud.databricks.com/).
2.  Click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
3.  Click the metastore name.
4.  Click the **Workspaces** tab.
5.  Click **Assign to workspace**.
6.  Select one or more workspaces. You can type part of the workspace name to filter the list.
7.  Scroll to the bottom of the dialog, and click **Assign**.
8.  On the confirmation dialog, click **Enable**.

To enable Unity Catalog when you create a workspace using the account console:

1.  As an account admin, log in to the [account console](https://accounts.cloud.databricks.com/).
2.  Click ![Workspaces icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTIuNSAxQzIuMDg1NzkgMSAxLjc1IDEuMzM1NzkgMS43NSAxLjc1VjQuNzVDMS43NSA1LjE2NDIxIDIuMDg1NzkgNS41IDIuNSA1LjVINlY0SDMuMjVWMi41SDEyLjc1VjRIMTBWNS41SDEzLjVDMTMuOTE0MiA1LjUgMTQuMjUgNS4xNjQyMSAxNC4yNSA0Ljc1VjEuNzVDMTQuMjUgMS4zMzU3OSAxMy45MTQyIDEgMTMuNSAxSDIuNVoiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0wIDEyLjI1QzAgMTAuOTg5OCAwLjg0NzY1MSA5LjkyNzU5IDIuMDAzOSA5LjYwMjQyQzIuMDgwNTggOC4xNTIyNSAzLjI4MDczIDcgNC43NSA3SDcuMjVWNEg4Ljc1VjdIMTEuMjVDMTIuNzE5MyA3IDEzLjkxOTQgOC4xNTIyNSAxMy45OTYxIDkuNjAyNDJDMTUuMTUyMyA5LjkyNzU5IDE2IDEwLjk4OTggMTYgMTIuMjVDMTYgMTMuNzY4OCAxNC43Njg4IDE1IDEzLjI1IDE1QzEyLjAxNzYgMTUgMTAuOTc0NSAxNC4xODkzIDEwLjYyNSAxMy4wNzIxQzEwLjI3NTUgMTQuMTg5MyA5LjIzMjQgMTUgOCAxNUM2Ljc2NzYgMTUgNS43MjQ1NCAxNC4xODkzIDUuMzc1IDEzLjA3MjFDNS4wMjU0NiAxNC4xODkzIDMuOTgyNCAxNSAyLjc1IDE1QzEuMjMxMjIgMTUgMCAxMy43Njg4IDAgMTIuMjVaTTIuNzUgMTFDMi4wNTk2NCAxMSAxLjUgMTEuNTU5NiAxLjUgMTIuMjVDMS41IDEyLjk0MDQgMi4wNTk2NCAxMy41IDIuNzUgMTMuNUMzLjQ0MDM2IDEzLjUgNCAxMi45NDA0IDQgMTIuMjVDNCAxMS41NTk2IDMuNDQwMzYgMTEgMi43NSAxMVpNNS4zNzUgMTEuNDI3OUM1LjEwMDA2IDEwLjU0OTEgNC4zOTYgOS44NTk5NiAzLjUwODIyIDkuNjA1ODZDMy41Nzk2OSA4Ljk4MzM5IDQuMTA4MzkgOC41IDQuNzUgOC41SDcuMjVWOS42MDM1MkM2LjM1ODM1IDkuODU1NzEgNS42NTA4IDEwLjU0NjQgNS4zNzUgMTEuNDI3OVpNOC43NSA5LjYwMzUyVjguNUgxMS4yNUMxMS44OTE2IDguNSAxMi40MjAzIDguOTgzMzkgMTIuNDkxOCA5LjYwNTg2QzExLjYwNCA5Ljg1OTk2IDEwLjg5OTkgMTAuNTQ5MSAxMC42MjUgMTEuNDI3OUMxMC4zNDkyIDEwLjU0NjQgOS42NDE2NSA5Ljg1NTcxIDguNzUgOS42MDM1MlpNMTIgMTIuMjVDMTIgMTEuNTU5NiAxMi41NTk2IDExIDEzLjI1IDExQzEzLjk0MDQgMTEgMTQuNSAxMS41NTk2IDE0LjUgMTIuMjVDMTQuNSAxMi45NDA0IDEzLjk0MDQgMTMuNSAxMy4yNSAxMy41QzEyLjU1OTYgMTMuNSAxMiAxMi45NDA0IDEyIDEyLjI1Wk02Ljc1IDEyLjI1QzYuNzUgMTIuOTQwNCA3LjMwOTY0IDEzLjUgOCAxMy41QzguNjkwMzYgMTMuNSA5LjI1IDEyLjk0MDQgOS4yNSAxMi4yNUM5LjI1IDExLjU1OTYgOC42OTAzNiAxMSA4IDExQzcuMzA5NjQgMTEgNi43NSAxMS41NTk2IDYuNzUgMTIuMjVaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Workspaces**.
3.  Click **Create workspace**.
4.  On the Create workspace page, click the **Enable Unity Catalog** toggle.
5.  On the confirmation dialog, click **Enable**.
6.  Select the **Metastore**.
7.  Complete the workspace creation configuration and click **Save**.

When the assignment is complete, the workspace appears in the metastore's **Workspaces** tab, and the metastore appears on the workspace's **Configuration** tab.

### Next steps[​](#next-steps "Direct link to Next steps")

*   [Create catalogs](https://docs.databricks.com/aws/en/catalogs/create-catalog)
*   [Create schemas](https://docs.databricks.com/aws/en/schemas/create-schema)
*   [Databricks tables](https://docs.databricks.com/aws/en/tables/)
*   Learn more about Unity Catalog: [What is Unity Catalog?](https://docs.databricks.com/aws/en/data-governance/unity-catalog/)
