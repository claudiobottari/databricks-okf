---
title: Unity Catalog setup guide | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/setup-uc
ingestedAt: "2026-06-18T08:04:53.322Z"
---

This page covers the initial Unity Catalog setup for workspace admins in a new Databricks workspace, including:

*   Confirming that your workspace is enabled for Unity Catalog
*   Managing workspace access and identities
*   Creating Unity Catalog\-compliant compute resources
*   Creating a catalog and schema for your data
*   Granting users the privileges they need

## Before you begin[​](#before-you-begin "Direct link to Before you begin")

Before starting, familiarize yourself with the following Unity Catalog concepts:

*   **Metastore**: The top-level Unity Catalog container, scoped to a single cloud region. It holds all [securable objects](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/permissions-concepts#securable-objects): catalogs, storage credentials, external locations, and more. See [Metastore](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#metastore).
*   **Catalog**: The highest-level data container object within a metastore. Catalogs hold schemas, which in turn contain tables, views, volumes, and functions. See [Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#catalog).
*   **Admin roles**: Unity Catalog has three main admin roles, account admin, workspace admin, and metastore admin, each with a different scope and responsibilities. See [Admin privileges in Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/admin-privileges).

You also need the following:

*   A Databricks workspace on the [Premium plan or above](https://databricks.com/product/pricing/platform-addons).
*   [Workspace admin](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/admin-privileges#workspace-admins) privileges. You might need [account admin](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/admin-privileges#account-admins) privileges in the following cases:
    *   If your workspace doesn't have compute resources yet, you need account admin privileges to verify that Unity Catalog is enabled via the account console in [Step 1: Confirm that your workspace is enabled for Unity Catalog](#confirm-uc).
    *   If your workspace isn't attached to a Unity Catalog metastore, you need account admin privileges to attach it.
    *   If a metastore doesn't exist, you need account admin privileges to create it.

## Step 1: Confirm that your workspace is enabled for Unity Catalog[​](#step-1-confirm-that-your-workspace-is-enabled-for-unity-catalog "Direct link to step-1-confirm-that-your-workspace-is-enabled-for-unity-catalog")

Use one of the following methods to confirm that your workspace is attached to a Unity Catalog metastore.

*   Use the account console
*   Run a SQL query

This method requires account admin privileges.

1.  As a Databricks account admin, log into the account console.
2.  Click ![Workspaces icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTIuNSAxQzIuMDg1NzkgMSAxLjc1IDEuMzM1NzkgMS43NSAxLjc1VjQuNzVDMS43NSA1LjE2NDIxIDIuMDg1NzkgNS41IDIuNSA1LjVINlY0SDMuMjVWMi41SDEyLjc1VjRIMTBWNS41SDEzLjVDMTMuOTE0MiA1LjUgMTQuMjUgNS4xNjQyMSAxNC4yNSA0Ljc1VjEuNzVDMTQuMjUgMS4zMzU3OSAxMy45MTQyIDEgMTMuNSAxSDIuNVoiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0wIDEyLjI1QzAgMTAuOTg5OCAwLjg0NzY1MSA5LjkyNzU5IDIuMDAzOSA5LjYwMjQyQzIuMDgwNTggOC4xNTIyNSAzLjI4MDczIDcgNC43NSA3SDcuMjVWNEg4Ljc1VjdIMTEuMjVDMTIuNzE5MyA3IDEzLjkxOTQgOC4xNTIyNSAxMy45OTYxIDkuNjAyNDJDMTUuMTUyMyA5LjkyNzU5IDE2IDEwLjk4OTggMTYgMTIuMjVDMTYgMTMuNzY4OCAxNC43Njg4IDE1IDEzLjI1IDE1QzEyLjAxNzYgMTUgMTAuOTc0NSAxNC4xODkzIDEwLjYyNSAxMy4wNzIxQzEwLjI3NTUgMTQuMTg5MyA5LjIzMjQgMTUgOCAxNUM2Ljc2NzYgMTUgNS43MjQ1NCAxNC4xODkzIDUuMzc1IDEzLjA3MjFDNS4wMjU0NiAxNC4xODkzIDMuOTgyNCAxNSAyLjc1IDE1QzEuMjMxMjIgMTUgMCAxMy43Njg4IDAgMTIuMjVaTTIuNzUgMTFDMi4wNTk2NCAxMSAxLjUgMTEuNTU5NiAxLjUgMTIuMjVDMS41IDEyLjk0MDQgMi4wNTk2NCAxMy41IDIuNzUgMTMuNUMzLjQ0MDM2IDEzLjUgNCAxMi45NDA0IDQgMTIuMjVDNCAxMS41NTk2IDMuNDQwMzYgMTEgMi43NSAxMVpNNS4zNzUgMTEuNDI3OUM1LjEwMDA2IDEwLjU0OTEgNC4zOTYgOS44NTk5NiAzLjUwODIyIDkuNjA1ODZDMy41Nzk2OSA4Ljk4MzM5IDQuMTA4MzkgOC41IDQuNzUgOC41SDcuMjVWOS42MDM1MkM2LjM1ODM1IDkuODU1NzEgNS42NTA4IDEwLjU0NjQgNS4zNzUgMTEuNDI3OVpNOC43NSA5LjYwMzUyVjguNUgxMS4yNUMxMS44OTE2IDguNSAxMi40MjAzIDguOTgzMzkgMTIuNDkxOCA5LjYwNTg2QzExLjYwNCA5Ljg1OTk2IDEwLjg5OTkgMTAuNTQ5MSAxMC42MjUgMTEuNDI3OUMxMC4zNDkyIDEwLjU0NjQgOS42NDE2NSA5Ljg1NTcxIDguNzUgOS42MDM1MlpNMTIgMTIuMjVDMTIgMTEuNTU5NiAxMi41NTk2IDExIDEzLjI1IDExQzEzLjk0MDQgMTEgMTQuNSAxMS41NTk2IDE0LjUgMTIuMjVDMTQuNSAxMi45NDA0IDEzLjk0MDQgMTMuNSAxMy4yNSAxMy41QzEyLjU1OTYgMTMuNSAxMiAxMi45NDA0IDEyIDEyLjI1Wk02Ljc1IDEyLjI1QzYuNzUgMTIuOTQwNCA3LjMwOTY0IDEzLjUgOCAxMy41QzguNjkwMzYgMTMuNSA5LjI1IDEyLjk0MDQgOS4yNSAxMi4yNUM5LjI1IDExLjU1OTYgOC42OTAzNiAxMSA4IDExQzcuMzA5NjQgMTEgNi43NSAxMS41NTk2IDYuNzUgMTIuMjVaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Workspaces**.
3.  Find your workspace and check the **Metastore** column. If a metastore name is present, your workspace is enabled for Unity Catalog.

If your workspace is not enabled for Unity Catalog, see [Upgrade a Databricks workspace to Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/upgrade/).

## Step 2: Manage workspace access and identities[​](#step-2-manage-workspace-access-and-identities "Direct link to step-2-manage-workspace-access-and-identities")

Workspace admins can add users and groups, assign admin roles, and manage service principals.

### Add users[​](#add-users "Direct link to Add users")

Add individual users who need access to this workspace. For instructions, see [Manage users](https://docs.databricks.com/aws/en/admin/users-groups/users).

### Organize users into groups[​](#organize-users-into-groups "Direct link to Organize users into groups")

Databricks recommends managing access through groups rather than individual users. Granting privileges to a group applies them to all members, which reduces administrative overhead as your team grows.

*   **If your organization already has groups in an identity provider (IdP)**: Sync them to Databricks using automatic identity management or SCIM provisioning so that group membership stays in sync automatically. See [Automatic identity management](https://docs.databricks.com/aws/en/admin/users-groups/automatic-identity-management/).
*   **If you don't have groups yet**: As a workspace admin, create account-level groups by navigating to **Settings** > **Identity and access** > **Manage** next to **Groups**. See [Manage groups](https://docs.databricks.com/aws/en/admin/users-groups/manage-groups).

### Assign admin roles[​](#assign-admin-roles "Direct link to Assign admin roles")

[Workspace admins](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/admin-privileges#workspace-admins) can perform most day-to-day administrative tasks: adding and removing users, managing compute, configuring workspace settings, and granting access to data. This role is appropriate for members of a central data platform or IT team who are responsible for maintaining the workspace. Be selective about who receives this role. Workspace admins have broad access to workspace resources and settings.

Usually, the workspace admin role is the only administrator role you need to assign. Optionally, you can assign [metastore admins](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/admin-privileges#metastore-admins) for special use cases. For example, you might assign this role to a dedicated data governance team or a small group of senior platform engineers if you need to:

*   Delegate catalog creation to non-workspace admins.
*   Manage the init script and JAR [allowlist](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/allowlist).
*   Receive shared data through [OpenSharing](https://docs.databricks.com/aws/en/delta-sharing/read-data-databricks#permissions).
*   Transfer object ownership when a team member leaves.

For instructions on assigning these roles, see [Admin privileges in Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/admin-privileges).

## Step 3: Create Unity Catalog\-compliant compute[​](#step-3-create-unity-catalog-compliant-compute "Direct link to step-3-create-unity-catalog-compliant-compute")

To run Unity Catalog workloads, compute resources must meet Unity Catalog security requirements. The following table shows which compute types are compliant:

To create UC-compliant compute:

*   **SQL warehouse**: See [Create a SQL warehouse](https://docs.databricks.com/aws/en/compute/sql-warehouse/create).
*   **Serverless compute**: See [Connect to serverless compute](https://docs.databricks.com/aws/en/compute/serverless/).
*   **Cluster**: When configuring a cluster, select **Single user** or **Shared** as the access mode. See [Access modes](https://docs.databricks.com/aws/en/compute/configure#access-modes).

As a workspace admin, you can restrict cluster creation to admins only, or use cluster policies to let users create their own Unity Catalog\-compliant clusters. See [Compute permissions](https://docs.databricks.com/aws/en/compute/clusters-manage#cluster-level-permissions) and [Create and manage compute policies](https://docs.databricks.com/aws/en/admin/clusters/policies).

## Step 4: Create catalogs and schemas[​](#step-4-create-catalogs-and-schemas "Direct link to step-4-create-catalogs-and-schemas")

Catalogs are the primary unit of data isolation in Unity Catalog. All schemas, tables, volumes, views, and functions live in catalogs.

### When to create a new catalog[​](#when-to-create-a-new-catalog "Direct link to When to create a new catalog")

New workspaces are automatically provisioned with a workspace catalog — by default, this catalog is named after your workspace. To check whether you have a workspace catalog, click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog** in the sidebar and look for a catalog matching your workspace name. If it exists, you might not need to create additional catalogs right away.

Over time, consider creating new catalogs as your usage grows, organized around logical boundaries such as:

*   **Teams or business units**: separate catalogs for engineering, finance, and marketing
*   **Environments**: separate `dev`, `staging`, and `prod` catalogs to isolate development from production data
*   **Projects**: a dedicated catalog per major data product or initiative

If your organization's data boundaries are already well-defined, you can create catalogs now.

### Create a catalog[​](#create-a-catalog "Direct link to Create a catalog")

To create a catalog, run the following SQL.

SQL

    CREATE CATALOG IF NOT EXISTS <catalog-name>;

Then, create a schema to organize your tables and other data objects:

SQL

    CREATE SCHEMA IF NOT EXISTS <catalog-name>.<schema-name>;

For detailed instructions and how to use Catalog Explorer, see [Create catalogs](https://docs.databricks.com/aws/en/catalogs/create-catalog) and [Create schemas](https://docs.databricks.com/aws/en/schemas/create-schema).

## Step 5: Grant privileges to users[​](#step-5-grant-privileges-to-users "Direct link to step-5-grant-privileges-to-users")

In Unity Catalog, users have no access to data by default. Workspace admins can grant privileges to securable objects across the workspace. Databricks recommends granting privileges to groups rather than individual users. This makes access easier to manage as your team grows.

### Enable data discovery[​](#enable-data-discovery "Direct link to Enable data discovery")

Databricks recommends granting the `BROWSE` privilege on all catalogs to the `All account users` group. `BROWSE` allows users to see that objects exist and view their metadata in Catalog Explorer without granting access to the underlying data. This enables your users to discover data and request access without requiring admins to grant permissions preemptively.

SQL

    GRANT BROWSE ON CATALOG <catalog-name> TO `account users`;

### Grant data access[​](#grant-data-access "Direct link to Grant data access")

To access data in Unity Catalog, users typically need the specific privilege for the operation (such as `SELECT` to read a table) and the appropriate [usage privileges](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/permissions-concepts#usage-privileges) (such as `USE CATALOG` on the parent catalog, and `USE SCHEMA` on the parent schema). See [Unity Catalog permissions model concepts](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/permissions-concepts).

Grant these privileges only to the users and groups that need access to specific catalogs and schemas. For example, to grant read-only access to a schema, use the following SQL:

SQL

    GRANT USE CATALOG ON CATALOG <catalog-name> TO `<group-name>`;GRANT USE SCHEMA ON SCHEMA <catalog-name>.<schema-name> TO `<group-name>`;GRANT SELECT ON SCHEMA <catalog-name>.<schema-name> TO `<group-name>`;

For read-write access:

SQL

    GRANT USE CATALOG ON CATALOG <catalog-name> TO `<group-name>`;GRANT USE SCHEMA ON SCHEMA <catalog-name>.<schema-name> TO `<group-name>`;GRANT SELECT, MODIFY ON SCHEMA <catalog-name>.<schema-name> TO `<group-name>`;

Access patterns change over time. Use the following pages as a reference when managing privileges in Unity Catalog:

*   [Unity Catalog permissions model concepts](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/permissions-concepts): Explains the object hierarchy, ownership, privilege inheritance, and how the Unity Catalog permissions model works.
*   [Unity Catalog privileges reference](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/privileges-reference): Lists every privilege in Unity Catalog, what securable objects it applies to, and what it allows.
*   [Manage privileges in Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/): Covers how to grant, revoke, and inspect privileges on securable objects using SQL or Catalog Explorer.

## Setup checklist[​](#setup-checklist "Direct link to Setup checklist")

If you've completed all five steps, Unity Catalog is set up in your workspace and your users can start working with data. Use the following checklist to confirm everything is in place:

*   Unity Catalog is enabled, meaning a Unity Catalog metastore is attached to your workspace. See [Step 1: Confirm that your workspace is enabled for Unity Catalog](#confirm-uc).
*   Users are added to the workspace and have appropriate roles. See [Step 2: Manage workspace access and identities](#manage-identities).
*   Unity Catalog\-compliant compute is available. See [Step 3: Create Unity Catalog\-compliant compute](#create-compute).
*   Catalogs and schemas are created to organize your data. See [Step 4: Create catalogs and schemas](#create-catalogs).
*   Users can access the intended catalogs. See [Step 5: Grant privileges to users](#grant-privileges).

## Next steps[​](#next-steps "Direct link to Next steps")

With Unity Catalog set up, you can start applying more advanced governance capabilities to your workspace.

### Attribute-based access control[​](#attribute-based-access-control "Direct link to Attribute-based access control")

[Attribute-based access control (ABAC)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/) lets you define dynamic, fine-grained access policies based on attributes of the data and the user accessing it. Instead of managing permissions table by table, you write policies that automatically enforce row-level filtering and column-level masking. For example, you can hide sensitive columns from users outside a specific region or mask PII for non-privileged roles.

![ABAC column masking in action](https://docs.databricks.com/aws/en/assets/images/abac-column-masking-results-8e6ab5cb50a4885c92a470a8e6dc77de.png)

### Data classification[​](#data-classification "Direct link to Data classification")

[Data classification](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-classification) uses an AI agent to automatically scan your catalog and tag sensitive data such as PII, financial information, and credentials. After classification, tags can integrate directly with ABAC policies, allowing you to apply governance controls based on what the data actually contains rather than managing access object by object.

![Data classification results](https://docs.databricks.com/aws/en/assets/images/data-classification-results-page-d72a16748a065ed0ac6a9a81ed84590c.png)

### Data quality monitoring[​](#data-quality-monitoring "Direct link to Data quality monitoring")

[Data quality monitoring](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/) provides anomaly detection across all tables in a schema and data profiling at the table level. Anomaly detection automatically monitors freshness and completeness using historical data patterns, surfacing issues without manual configuration. Data profiling captures statistical distributions over time, enabling you to track data integrity and set alerts for unexpected changes.

![Data quality monitoring dashboard](https://docs.databricks.com/aws/en/assets/images/metastore-data-quality-dashboard-9d194085ce5d7c9ccba7dff860d7988a.png)

### AI governance with Unity AI Gateway[​](#ai-governance-with-unity-ai-gateway "Direct link to ai-governance-with-unity-ai-gateway")

[Unity AI Gateway](https://docs.databricks.com/aws/en/ai-gateway/) extends Unity Catalog governance to AI. It provides enterprise governance for LLM endpoints, agents, and MCP servers, allowing you to implement access control, audit logging, and observability across all AI interactions in a unified UI.
