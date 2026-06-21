---
title: Workspace-catalog binding | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/workspace-catalog-binding
ingestedAt: "2026-06-18T08:03:52.062Z"
---

In Unity Catalog, all catalogs are accessible by default from any workspace attached to the same metastore. Workspace-catalog binding lets you override this default to restrict a catalog to one or more specific workspaces. Access from an unbound workspace is denied, even for users with explicit privilege grants on the catalog.

## Why use workspace-catalog binding[​](#why-use-workspace-catalog-binding "Direct link to Why use workspace-catalog binding")

Organizational and compliance requirements often specify that certain data must remain accessible only in designated environments. You may also need to:

*   Isolate production data from development or test environments.
*   Prevent certain data domains from being joined together.
*   Ensure that sensitive data can only be processed in specific workspaces.

In Databricks, the workspace is the primary data processing environment, and the catalog is the primary data domain. Workspace-catalog binding connects these two concepts, letting catalog owners and users with the `MANAGE` privilege define which workspaces can access which catalogs.

## How workspace-catalog binding works[​](#how-workspace-catalog-binding-works "Direct link to How workspace-catalog binding works")

When you bind a catalog to specific workspaces, only the workspaces you assign can access the catalog. Any workspace not in the assigned list receives an error when users try to access the catalog, overriding any individual privilege grants those users hold.

![Catalog-workspace binding diagram](https://docs.databricks.com/aws/en/assets/images/workspace-catalog-binding-example-80fd4c0c839905a034c0c98302f01229.png)

In this diagram, `prod_catalog` is bound to two production workspaces. Even if a user holds a `SELECT` grant on a table in `prod_catalog`, they cannot access that table from the Dev workspace.

### Read-only access[​](#read-only-access "Direct link to Read-only access")

When binding a catalog to a workspace, you can optionally restrict that workspace to read-only access. All write operations from that workspace to the catalog are blocked.

### Default workspace catalog behavior[​](#default-workspace-catalog-behavior "Direct link to Default workspace catalog behavior")

The exception to the default open behavior is the [default workspace catalog](https://docs.databricks.com/aws/en/catalogs/default) created automatically for all new workspaces. This workspace catalog is bound only to its own workspace by default. If you unbind this catalog or extend access to other workspaces, you must grant any required permissions manually, because the workspace admins group is workspace-local and cannot be used across workspaces.

### Platform-wide enforcement[​](#platform-wide-enforcement "Direct link to Platform-wide enforcement")

Workspace-catalog bindings are enforced consistently across the platform:

*   Information schema queries return only the catalogs accessible in the current workspace.
*   Data lineage and Catalog Explorer show only catalogs that are assigned to the current workspace.

## What can be bound to workspaces[​](#what-can-be-bound-to-workspaces "Direct link to What can be bound to workspaces")

Workspace binding applies beyond catalogs. You can also bind:

*   **External locations**: restrict which workspaces can access specific cloud storage paths. See [Assign an external location to specific workspaces](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/manage-external-locations#workspace-binding).
*   **Storage credentials**: restrict which workspaces can use specific cloud credentials. See [Assign a storage credential to specific workspaces](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/manage-storage-credentials#workspace-binding).

*   **Service credentials**: restrict which workspaces can use specific cloud service credentials. See [(Optional) Assign a service credential to specific workspaces](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-services/service-credentials#workspace-binding).

## Video walkthrough[​](#video-walkthrough "Direct link to Video walkthrough")

This video demonstrates how to limit catalog access to specific workspaces (5 minutes).

## Bind a catalog to one or more workspaces[​](#bind-a-catalog-to-one-or-more-workspaces "Direct link to bind-a-catalog-to-one-or-more-workspaces")

To assign a catalog to specific workspaces, you can use Catalog Explorer or the Databricks CLI.

**Permissions required**: Metastore admin, catalog owner, or `MANAGE` and `USE CATALOG` on the catalog.

note

Regardless of whether a catalog is assigned to the current workspace, metastore admins can see all catalogs in a metastore, and catalog owners can see all catalogs they own in a metastore. Catalogs that aren't assigned to the workspace appear grayed out, and no child objects are visible or queryable.

*   Catalog Explorer
*   CLI

1.  Log in to a workspace that is linked to the metastore.
    
2.  Click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
    
3.  In the **Catalog** pane, on the left, click the catalog name.
    
    The main Catalog Explorer pane defaults to the **Catalogs** list. You can also select the catalog there.
    
4.  On the **Workspaces** tab, clear the **All workspaces have access** checkbox.
    
    If your catalog is already bound to one or more workspaces, this checkbox is already cleared.
    
5.  Click **Assign to workspaces** and enter or find the workspaces you want to assign.
    
6.  (Optional) Limit workspace access to read-only.
    
    On the **Manage Access Level** menu, select **Change access to read-only**.
    
    You can reverse this selection at any time by editing the catalog and selecting **Change access to read & write**.
    

To revoke access, go to the **Workspaces** tab, select the workspace, and click **Revoke**.

### Unbind a catalog from a workspace[​](#unbind-a-catalog-from-a-workspace "Direct link to unbind-a-catalog-from-a-workspace")

Instructions for revoking workspace access to a catalog using Catalog Explorer or the `workspace-bindings` CLI command group are included in [Bind a catalog to one or more workspaces](#bind).

important

If your workspace was enabled for Unity Catalog automatically and you have a default workspace catalog, workspace admins own that catalog and have all permissions on that catalog **in the workspace only**. If you unbind that catalog or bind it to other catalogs, you must grant any required permissions manually to the members of the workspace admins group as individual users or using account-level groups, because the workspace admins group is a workspace-local group. For more information about account groups vs workspace-local groups, see [Group sources](https://docs.databricks.com/aws/en/admin/users-groups/groups#sources).
