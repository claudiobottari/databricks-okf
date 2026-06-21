---
title: Admin privileges in Unity Catalog | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/admin-privileges
ingestedAt: "2026-06-18T08:04:44.326Z"
---

Databricks has [many administrator roles](https://docs.databricks.com/aws/en/admin/admin-concepts#admin-types). From a Unity Catalog permissions perspective, the three most important are account admins, workspace admins, and metastore admins. Account admins and workspace admins are required for all deployments, and the metastore admin role is optional. Understanding each role's responsibilities helps you assign admins with the right scope.

*   **Account admins** operate at the Databricks account level. They create and link metastores and workspaces, and can assign admin roles.
*   **Workspace admins** operate within a single workspace. They manage workspace membership, jobs, and workspace objects.
*   **Metastore admins (optional)** operate within a single Unity Catalog metastore. They govern data access, ownership, and top-level Unity Catalog securable objects.

![Unity Catalog account and admin overview](https://docs.databricks.com/aws/en/assets/images/unity-catalog-admin-overview-e7de43f366684fa951281ccbaa0eeb20.png)

## Admin roles at a glance[​](#admin-roles-at-a-glance "Direct link to Admin roles at a glance")

note

Account admins and metastore admins are separate roles. When an account admin creates a metastore, they become its initial metastore admin by default. They can then assign the metastore admin role to a different user, group, or service principal and relinquish it themselves.

## Account admins[​](#account-admins "Direct link to account-admins")

Account admin is a highly privileged role that you should distribute carefully. Account admins have privileges over the entire Databricks account, which includes the following key capabilities:

For more information, see [What are account admins?](https://docs.databricks.com/aws/en/admin/admin-concepts#what-are-account-admins).

## Workspace admins[​](#workspace-admins "Direct link to workspace-admins")

Workspace admin is a highly privileged role that you should distribute carefully. Workspace admins have admin privileges within a single workspace, which includes the following key capabilities:

For more information, see [What are workspace admins?](https://docs.databricks.com/aws/en/admin/admin-concepts#what-are-workspace-admins).

Account admins can restrict workspace admin privileges using the `RestrictWorkspaceAdmins` setting. See [Restrict workspace admins](https://docs.databricks.com/aws/en/admin/workspace-settings/restrict-workspace-admins).

### Workspace admin privileges when workspaces are enabled for Unity Catalog automatically[​](#workspace-admin-privileges-when-workspaces-are-enabled-for-unity-catalog-automatically "Direct link to workspace-admin-privileges-when-workspaces-are-enabled-for-unity-catalog-automatically")

If your workspace was enabled for Unity Catalog automatically (applies to all workspaces created after November 8, 2023), the workspace is attached to a metastore by default. For more information see [Get started with Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/get-started). In addition, workspace admins have the following privileges on the attached metastore by default:

*   `CREATE CATALOG`

*   `CREATE CLEAN ROOM`

*   `CREATE EXTERNAL LOCATION`
*   `CREATE SERVICE CREDENTIAL`
*   `CREATE STORAGE CREDENTIAL`
*   `CREATE CONNECTION`
*   `CREATE SHARE`
*   `CREATE RECIPIENT`
*   `CREATE PROVIDER`
*   `CREATE MATERIALIZED VIEW`

note

These privilege grants are visible in the metastore **Permissions** tab in the account console. Databricks represents them with an auto-generated system group named `_workspace_admins_databricks_<account_id>_workspace_<workspace_id>`.

Workspace admins are the default owners of the workspace catalog, if a workspace catalog was provisioned for your workspace. Ownership of this catalog grants the following privileges:

*   Manage the privileges for or transfer ownership of any object within the workspace catalog.
    
    This includes the ability to grant themselves read and write access to all data in the catalog (no direct access by default; granting permissions is audit-logged).
    
*   Transfer ownership of the workspace catalog itself.
    

All workspace users receive the `USE CATALOG` privilege on the workspace catalog. Workspace users also receive the `USE SCHEMA`, `CREATE TABLE`, `CREATE VOLUME`, `CREATE MODEL`, `CREATE FUNCTION`, and `CREATE MATERIALIZED VIEW` privileges on the `default` schema in the catalog.

note

The default privileges granted on the attached metastore and workspace catalog are not maintained across workspaces (if, for example, the workspace catalog is also bound to another workspace).

The metastore admin is an optional but highly privileged user or group in Unity Catalog. Metastore admins have privileges from two sources: default privileges granted by the role, and ownership privileges because they are the owners of the metastore.

### When to assign a metastore admin[​](#when-to-assign-a-metastore-admin "Direct link to When to assign a metastore admin")

For workspaces created after November 8, 2023, the metastore admin role is optional. This is because workspace admins receive sufficient metastore-level privileges by default (see [Workspace admin privileges when workspaces are enabled for Unity Catalog automatically](#workspace-admins-auto)). However, you must assign a metastore admin if you need to perform the following actions:

*   [Change ownership](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/#manage-ownership) of objects or grant privileges on objects that you do not own. For example, this is required when taking over a catalog after the original owning account is removed. Workspace admins can create objects but cannot make grants on or change ownership of existing objects they do not own.
*   Remove [default workspace admin permissions](#workspace-admins-auto).
*   Add managed storage to the metastore, if it has none. This requires an account admin to add the storage location to the metastore definition. See [Add managed storage to an existing metastore](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-metastore#add-storage).
*   Enable default access request destinations for objects that don't have destinations explicitly set. See [Enable default email destinations](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/access-request-destinations#default-destinations).

### Default metastore admin privileges[​](#default-metastore-admin-privileges "Direct link to Default metastore admin privileges")

Metastore admins have the following privileges on the metastore by default:

### Ownership privileges[​](#ownership-privileges "Direct link to Ownership privileges")

As owners of the metastore, metastore admins have the following privileges:

### Who has initial metastore admin privileges?[​](#who-has-initial-metastore-admin-privileges "Direct link to Who has initial metastore admin privileges?")

If an account admin creates the metastore manually, that account admin is the metastore's initial owner and metastore admin. All metastores created before November 8, 2023 were created manually by an account admin.

If the metastore was provisioned as part of automatic Unity Catalog enablement, the metastore was created without a metastore admin. Workspace admins in that case are automatically granted privileges that make the metastore admin optional. If needed, account admins can assign the metastore admin role to a user, service principal, or group. Groups are strongly recommended. See [Get started with Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/get-started).

### Assign a metastore admin[​](#assign-a-metastore-admin "Direct link to assign-a-metastore-admin")

Metastore admin is a highly privileged role that you should distribute carefully. It is optional.

Account admins can assign the metastore admin role. Databricks recommends nominating a group as the metastore admin. By doing this, any member of the group is automatically a metastore admin.

To assign the metastore admin role to a group:

1.  As an account admin, log in to the [account console](https://accounts.cloud.databricks.com/).
2.  Click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog**.
3.  Click the name of a metastore to open its properties.
4.  Under **Metastore Admin**, click **Edit**.
5.  Select a group from the drop-down. You can enter text in the field to search for options.
6.  Click **Save**.

important

It can take up to 30 seconds for a metastore admin assignment change to be reflected in your account, and it may take longer to take effect in some workspaces than others. This delay is due to caching protocols.
