---
title: Upgrade Hive tables and views to Unity Catalog | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/migrate
ingestedAt: "2026-06-18T08:04:47.325Z"
---

This article describes how to upgrade tables and views registered in your existing workspace-local Hive metastore to Unity Catalog.

You can upgrade a Hive table either to a _managed table_ or _external table_ in Unity Catalog.

*   **Managed tables** are the preferred way to create tables in Unity Catalog. Unity Catalog fully manages their lifecycle, file layout, and storage. Unity Catalog also optimizes their performance automatically. Managed tables always use the [Delta](https://docs.databricks.com/aws/en/delta/) table format.
    
    Managed tables reside in a [managed storage location](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/managed-storage) that you reserve for Unity Catalog. Because of this storage requirement, you must use [CLONE](#clone) or [CREATE TABLE AS SELECT](#create-table-as-select) (CTAS) if you want to copy existing Hive tables to Unity Catalog as managed tables.
    
*   **External tables** are tables whose data lifecycle, file layout, and storage location are not managed by Unity Catalog. Multiple data formats are supported for external tables.
    
    Typically you use external tables only when you also need direct access to data using non-Databricks compute (that is, not using Databricks clusters or Databricks SQL warehouses). External tables are also convenient in migration scenarios, because you can register existing data in Unity Catalog quickly without having to that copy data. This is thanks to the fact that data in external tables doesn't have to reside in reserved managed storage.
    

For more information about managed and external tables in Unity Catalog, see [Databricks tables](https://docs.databricks.com/aws/en/tables/).

## Hive to Unity Catalog migration options[​](#hive-to-unity-catalog-migration-options "Direct link to hive-to-unity-catalog-migration-options")

When you are ready to migrate Hive tables to Unity Catalog, you have several options, depending on your use case:

This article describes how to perform all but the UCX-driven upgrade process. Databricks recommends UCX for most workspace upgrade scenarios. However, for simpler use cases, you might prefer one or more of the tools described here.

## Before you begin[​](#before-you-begin "Direct link to before-you-begin")

This section describes some of the impacts of migration that you should be prepared for, along with permissions and compute requirements.

### Understand the impact[​](#understand-the-impact "Direct link to Understand the impact")

You should be aware that when you modify your workloads to use the new Unity Catalog tables, you might need to change some behaviors:

*   Unity Catalog manages partitions differently than Hive. Hive commands that directly manipulate partitions are not supported on tables managed by Unity Catalog.
*   Table history is not migrated when you run `CREATE TABLE CLONE`. Any tables in the Hive metastore that you clone to Unity Catalog are treated as new tables. You cannot perform Delta Lake time travel or other operations that rely on pre-migration history.

For more information, see [Work with the legacy Hive metastore alongside Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/hive-metastore).

### Requirements[​](#requirements "Direct link to Requirements")

To perform migrations, you must have:

*   A workspace that that has a Unity Catalog metastore and at least one Unity Catalog catalog. See [Get started with Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/get-started).
    
*   Privileges on the Unity Catalog catalogs to which you are migrating tables. These privilege requirements are enumerated at the start of each procedure covered in this article.
    
*   For migration to Unity Catalog external tables: storage credentials and external locations defined in Unity Catalog, and the `CREATE EXTERNAL TABLE` privilege on the external location.
    
*   Access to Databricks compute that meets both of the following requirements:
    
    *   Supports Unity Catalog (SQL warehouses or compute resources that use standard or dedicated access mode).
    *   Allows access to the tables in the Hive metastore.
    
    Because compute resources that use standard access mode are enabled for [legacy table access control](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/table-acls/) by default, that means that if you use that access mode, you must have table access control privileges on the Hive metastore that you are migrating from. You can grant yourself access using the following SQL command:
    
    SQL
    
        GRANT ALL PRIVILEGES ON catalog hive_metastore TO `<user>`
    
    Alternatively, you can use a compute resource in dedicated access mode.
    

For more information about managing privileges on objects in the Hive metastore, see [Hive metastore privileges and securable objects (legacy)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/table-acls/object-privileges). For more information about managing privileges on objects in the Unity Catalog metastore, see [Manage privileges in Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/).

To determine whether a table is currently registered in Unity Catalog, check the catalog name. Tables in the catalog `hive_metastore` are registered in the workspace-local Hive metastore. Any other catalogs listed are governed by Unity Catalog.

To view the tables in the `hive_metastore` catalog using Catalog Explorer:

1.  Click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog** in the sidebar.
2.  In the catalog pane, browse to the `hive_metastore` catalog and expand the schema nodes.

You can also search for a specific table using the filter field in the Catalog pane.

You can copy complete schemas (databases) and multiple external or managed tables from your Databricks default Hive metastore to the Unity Catalog metastore using the **Catalog Explorer** upgrade wizard. The upgraded tables will be external tables in Unity Catalog.

For help deciding when to use the upgrade wizard, see [Hive to Unity Catalog migration options](#comparison-table).

### Requirements[​](#requirements-1 "Direct link to Requirements")

**Data format requirements**:

*   See [Work with external tables](https://docs.databricks.com/aws/en/tables/external).

**Compute requirements**:

*   A compute resource that supports Unity Catalog. See [Before you begin](#before).

**Unity Catalog object and permission requirements**:

*   A [storage credential](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/#storage-credentials) for an IAM role that authorizes Unity Catalog to access the tables' location path.
*   An [external location](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/#external-locations) that references the storage credential you just created and the path to the data on your cloud tenant.
*   `CREATE EXTERNAL TABLE` permission on the external locations of the tables to be upgraded.

**Hive table access requirements**:

*   If your compute uses standard access mode, you need access to the tables in the Hive metastore, granted using legacy table access control. See [Before you begin](#before).

### Upgrade process[​](#upgrade-process "Direct link to Upgrade process")

1.  Click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog** in the sidebar to open the [Catalog Explorer](https://docs.databricks.com/aws/en/catalog-explorer/).
    
2.  Select `hive_metastore` as your catalog and select the schema (database) that you want to upgrade.
    
    ![Select database](https://docs.databricks.com/aws/en/assets/images/data-explorer-select-database-341e978fefda18f86251149b89774b36.png)
    
3.  Click **Upgrade** at the top right of the schema detail view.
    
4.  Select all of the tables that you want to upgrade and click **Next**.
    
    Only external tables in formats supported by Unity Catalog can be upgraded using the upgrade wizard. See [Work with external tables](https://docs.databricks.com/aws/en/tables/external).
    
5.  Set the destination catalog, schema (database), and owner for each table.
    
    Users will be able to access the newly created table in the context of their privileges on the [catalog and schema](https://docs.databricks.com/aws/en/database-objects/).
    
    Table owners have all privileges on the table, including `SELECT` and `MODIFY`. If you don't select an owner, the managed tables are created with you as the owner. Databricks generally recommends that you grant table ownership to groups. To learn more about object ownership in Unity Catalog, see [Manage object ownership](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/#manage-ownership).
    
    To assign the same catalog and schema to multiple tables, select the tables and click the **Set destination** button.
    
    To assign the same owner to multiple tables, select the tables and click the **Set owner** button.
    
6.  Review the table configurations. To modify them, click the **Previous** button.
    
7.  Click **Run upgrade** to run the upgrade immediately or click **Create notebook for upgrade**.
    
    If you create a notebook for upgrade, name your notebook and choose a path to save it. Then run the notebook.
    
    When the upgrade is done, each table's metadata has been copied from Hive metastore to Unity Catalog. These tables are marked as upgraded in the upgrade wizard.
    
8.  Define fine-grained access control using the **Permissions** tab of each new table.
    
9.  (Optional) Add comments to each upgraded Hive table that points users to the new Unity Catalog table.
    
    Return to the original table in the `hive.metastore` catalog to add the table comment.
    
    If you use the following syntax in the table comment, notebooks and SQL query editor queries that reference the deprecated Hive table will display the deprecated table name using strikethrough text, display the comment as a warning, and provide a **Quick Fix** link to Genie Code, which can update your code to reference the new table.
    
        This table is deprecated. Please use catalog.default.table instead of hive_metastore.schema.table.
    
    See [Add comments to indicate that a Hive table has been migrated](#deprecated-comment).
    
10.  Modify your workloads to use the new tables.
     
     If you added a comment to the original Hive table like the one listed in the optional previous step, you can use Genie Code to help you find and modify workloads. See [Use Genie Code to update a deprecated table reference](#update-deprecated).
     
     note
     
     If you no longer need the old tables, you can drop them from the Hive metastore. Dropping an external table does not modify the data files on your cloud tenant.
     

## Upgrade a Hive table to a Unity Catalog external table using SYNC[​](#upgrade-a-hive-table-to-a-unity-catalog-external-table-using-sync "Direct link to upgrade-a-hive-table-to-a-unity-catalog-external-table-using-sync")

You can use the `SYNC` SQL command to copy external tables in your Hive metastore to external tables in Unity Catalog. You can sync individual tables or entire schemas.

You can also use `SYNC` to copy Hive managed tables that are stored outside of Databricks workspace storage (sometimes called DBFS root) to external tables in Unity Catalog. You cannot use it to copy Hive managed tables stored in workspace storage. To copy those tables, use [CREATE TABLE CLONE](#clone) instead.

The `SYNC` command performs a write operation to each source table it upgrades to add additional table properties for bookkeeping, including a record of the target Unity Catalog external table.

`SYNC` can also be used to update existing Unity Catalog tables when the source tables in the Hive metastore are changed. This makes it a good tool for transitioning to Unity Catalog gradually.

*   For a demo of using `SYNC` to upgrade external tables, see [Unity Catalog - External Table on HMS](https://app.getreprise.com/launch/m6ErK0n/).
*   For a demo of using `SYNC` to upgrade managed tables, see [Unity Catalog - Managed Table on HMS](https://app.getreprise.com/launch/MXxjgN6/).

For details, see [`SYNC`](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-aux-sync). For help deciding when to use the upgrade wizard, see [Hive to Unity Catalog migration options](#comparison-table).

### Requirements[​](#requirements-2 "Direct link to Requirements")

**Data format requirements**:

*   See [Work with external tables](https://docs.databricks.com/aws/en/tables/external).

**Compute requirements**:

*   A compute resource that supports Unity Catalog. See [Before you begin](#before).

**Unity Catalog object and permission requirements**:

*   A [storage credential](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/#storage-credentials) for an IAM role that authorizes Unity Catalog to access the tables' location path.
*   An [external location](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/#external-locations) that references the storage credential you just created and the path to the data on your cloud tenant.
*   `CREATE EXTERNAL TABLE` permission on the external locations of the tables to be upgraded.

**Hive table access requirements**:

*   If your compute uses standard access mode, you need access to the tables in the Hive metastore, granted using legacy table access control. See [Before you begin](#before).

### Upgrade process[​](#upgrade-process-1 "Direct link to Upgrade process")

To upgrade tables in your Hive metastore to Unity Catalog external tables using `SYNC`:

1.  In a notebook or the SQL query editor, run one of the following:
    
    Sync an external Hive table:
    
    SQL
    
        SYNC TABLE <uc-catalog>.<uc-schema>.<new-table> FROM hive_metastore.<source-schema>.<source-table>SET OWNER <principal>;
    
    Sync an external Hive schema and all of its tables:
    
    SQL
    
        SYNC SCHEMA <uc-catalog>.<new-schema> FROM hive_metastore.<source-schema>SET OWNER <principal>;
    
    Sync a managed Hive table that is stored outside of Databricks workspace storage:
    
    SQL
    
        SYNC TABLE <uc-catalog>.<uc-schema>.<new-table> AS EXTERNAL FROM hive_metastore.<source-schema>.<source-table>SET OWNER <principal>;
    
    Sync a schema that contains managed Hive tables that are stored outside of Databricks workspace storage:
    
    SQL
    
        SYNC SCHEMA <uc-catalog>.<new-schema> AS EXTERNAL FROM hive_metastore.<source-schema>SET OWNER <principal>;
    
2.  Grant account-level users or groups access to the new table. See [Manage privileges in Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/).
    
3.  (Optional) Add a comment to the original Hive table that points users to the new Unity Catalog table.
    
    Return to the original table in the `hive.metastore` catalog to add the table comment. To learn how to add table comments using Catalog Explorer, see [Add comments to data and AI assets](https://docs.databricks.com/aws/en/comments/). To learn how to add table comments using SQL statements in a notebook or the SQL query editor, see [COMMENT ON](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-comment).
    
    If you use the following syntax in the table comment, notebooks and SQL query editor queries that reference the deprecated Hive table will display the deprecated table name using strikethrough text, display the comment as a warning, and provide a **Quick Fix** link to Genie Code, which can update your code to reference the new table.
    
        This table is deprecated. Please use catalog.default.table instead of hive_metastore.schema.table.
    
    See [Add comments to indicate that a Hive table has been migrated](#deprecated-comment).
    
4.  After the table is migrated, users should update their existing queries and workloads to use the new table.
    
    If you added a comment to the original Hive table like the one listed in the optional previous step, you can use Genie Code to help you find and modify workloads. See [Use Genie Code to update a deprecated table reference](#update-deprecated).
    
5.  Before you drop the old table, test for dependencies by revoking access to it and re-running related queries and workloads.
    
    Don't drop the old table if you are still relying on deprecation comments to help you find and update existing code that references the old table. Likewise, don't drop the old table if that table has changed since your original sync: `SYNC` can be used to update existing Unity Catalog tables with changes from source Hive tables.
    

## Upgrade a Hive managed table to a Unity Catalog managed table using CLONE[​](#upgrade-a-hive-managed-table-to-a-unity-catalog-managed-table-using-clone "Direct link to upgrade-a-hive-managed-table-to-a-unity-catalog-managed-table-using-clone")

Use `CREATE TABLE CLONE` to upgrade managed Delta tables in your Hive metastore to managed tables in Unity Catalog. You can clone individual tables. You must use deep clones when you clone tables from the legacy Hive metastore to Unity Catalog.

For help deciding when to use `CLONE`, see [Hive to Unity Catalog migration options](#comparison-table). For more information about `CLONE`, see [Clone a table on Databricks](https://docs.databricks.com/aws/en/tables/operations/clone).

### Requirements[​](#requirements-3 "Direct link to Requirements")

**Data format requirements**:

*   Managed Hive tables in Delta format.

**Compute requirements**:

*   A compute resource that supports Unity Catalog. See [Before you begin](#before).

**Permission requirements**:

*   The `USE CATALOG` and `USE SCHEMA` privileges on the catalog and schema that you add the table to, along with `CREATE TABLE` on the schema, or you must be the owner of the catalog or schema. See [Unity Catalog privileges reference](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/privileges-reference).
*   If your compute uses standard access mode, you need access to the tables in the Hive metastore, granted using legacy table access control. See [Before you begin](#before).

### Upgrade process[​](#upgrade-process-2 "Direct link to Upgrade process")

To upgrade managed tables in your Hive metastore to managed tables in Unity Catalog:

1.  In a notebook or the SQL query editor, run one of the following:
    
    Deep clone a managed table in the Hive metastore:
    
    SQL
    
        CREATE OR REPLACE TABLE <uc-catalog>.<uc-schema>.<new-table>DEEP CLONE hive_metastore.<source-schema>.<source-table>;
    
    For information about additional parameters, including table properties, see [CREATE TABLE CLONE](https://docs.databricks.com/aws/en/sql/language-manual/delta-clone).
    
2.  Grant account-level users or groups access to the new table. See [Manage privileges in Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/).
    
3.  (Optional) Add a comment to the original Hive table that points users to the new Unity Catalog table.
    
    Return to the original table in the `hive.metastore` catalog to add the table comment. To learn how to add table comments using Catalog Explorer, see [Add comments to data and AI assets](https://docs.databricks.com/aws/en/comments/). To learn how to add table comments using SQL statements in a notebook or the SQL query editor, see [COMMENT ON](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-comment).
    
    If you use the following syntax in the table comment, notebooks and SQL query editor queries that reference the deprecated Hive table will display the deprecated table name using strikethrough text, display the comment as a warning, and provide a **Quick Fix** link to Genie Code, which can update your code to reference the new table.
    
        This table is deprecated. Please use catalog.default.table instead of hive_metastore.schema.table.
    
    See [Add comments to indicate that a Hive table has been migrated](#deprecated-comment).
    
4.  After the table is migrated, users should update their existing queries and workloads to use the new table.
    
    If you added a comment to the original Hive table like the one listed in the optional previous step, you can use Genie Code to help you find and modify workloads. See [Use Genie Code to update a deprecated table reference](#update-deprecated).
    
5.  Before you drop the old table, test for dependencies by revoking access to it and re-running related queries and workloads.
    
    Don't drop the old table if you are still relying on deprecation comments to help you find and update existing code that references the old table. Likewise, don't drop the old table if you performed a shallow clone. Shallow clones reference data from the source Hive table.
    

## Upgrade a Hive table to a Unity Catalog managed table using CREATE TABLE AS SELECT[​](#upgrade-a-hive-table-to-a-unity-catalog-managed-table-using-create-table-as-select "Direct link to upgrade-a-hive-table-to-a-unity-catalog-managed-table-using-create-table-as-select")

If you cannot use or prefer not to use `CREATE TABLE CLONE` to migrate a table in your Hive metastore to a managed table in Unity Catalog, you can create a new managed table in Unity Catalog by querying the Hive table using `CREATE TABLE AS SELECT`. For information about the differences between `CREATE TABLE CLONE` and `CREATE TABLE AS SELECT`, see [Hive to Unity Catalog migration options](#comparison-table).

For a demo of upgrading a managed table using `CREATE TABLE AS SELECT`, see [Managed Tables On HMS Without SYNC](https://app.getreprise.com/launch/dyRBKBy/).

### Requirements[​](#requirements-4 "Direct link to Requirements")

**Compute requirements**:

*   A compute resource that supports Unity Catalog. See [Before you begin](#before).

**Permission requirements**:

*   The `USE CATALOG` and `USE SCHEMA` privileges on the catalog and schema that you add the table to, along with `CREATE TABLE` on the schema, or you must be the owner of the catalog or schema. See [Unity Catalog privileges reference](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/privileges-reference).
*   If your compute uses standard access mode, you need access to the tables in the Hive metastore, granted using legacy table access control. See [Before you begin](#before).

### Upgrade process[​](#upgrade-process-3 "Direct link to Upgrade process")

To upgrade a table in your Hive metastore to a managed table in Unity Catalog using `CREATE TABLE AS SELECT`:

1.  Create a new Unity Catalog table by querying the existing table. Replace the placeholder values:
    
    *   `<uc-catalog>`: The Unity Catalog catalog for the new table.
    *   `<uc-schema>`: The Unity Catalog schema for the new table.
    *   `<new-table>`: A name for the Unity Catalog table.
    *   `<source-schema>`: The schema for the Hive table, such as `default`.
    *   `<source-table>`: The name of the Hive table.
    
    *   SQL
    *   Python
    *   R
    *   Scala
    
    SQL
    
        CREATE TABLE <uc-catalog>.<new-schema>.<new-table>AS SELECT * FROM hive_metastore.<source-schema>.<source-table>;
    
    If you want to migrate only some columns or rows, modify the `SELECT` statement.
    
2.  Grant account-level users or groups access to the new table. See [Manage privileges in Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/).
    
3.  (Optional) Add a comment to the original Hive table that points users to the new Unity Catalog table.
    
    Return to the original table in the `hive.metastore` catalog to add the table comment. To learn how to add table comments using Catalog Explorer, see [Add comments to data and AI assets](https://docs.databricks.com/aws/en/comments/). To learn how to add table comments using SQL statements in a notebook or the SQL query editor, see [COMMENT ON](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-comment).
    
    If you use the following syntax in the table comment, notebooks and SQL query editor queries that reference the deprecated Hive table will display the deprecated table name using strikethrough text, display the comment as a warning, and provide a **Quick Fix** link to Genie Code, which can update your code to reference the new table.
    
        This table is deprecated. Please use catalog.default.table instead of hive_metastore.schema.table.
    
    See [Add comments to indicate that a Hive table has been migrated](#deprecated-comment).
    
4.  After the table is migrated, users should update their existing queries and workloads to use the new table.
    
    If you added a comment to the original Hive table like the one listed in the optional previous step, you can use Genie Code to help you find and modify workloads. See [Use Genie Code to update a deprecated table reference](#update-deprecated).
    
5.  Before you drop the old table, test for dependencies by revoking access to it and re-running related queries and workloads.
    
    Don't drop the old table if you are still relying on deprecation comments to help you find and update existing code that references the old table.
    

## Upgrade a view to Unity Catalog[​](#upgrade-a-view-to-unity-catalog "Direct link to upgrade-a-view-to-unity-catalog")

After you upgrade all of a view's referenced tables to the same Unity Catalog metastore, you can [create a new view](https://docs.databricks.com/aws/en/views/create-views) that references the new tables.

When you add a comment to the deprecated Hive table that points users to the new Unity Catalog table, notebooks and SQL query editor queries that reference the deprecated Hive table will display the deprecated table name using strikethrough text, display the comment as a warning, and provide a **Quick Fix** link to Genie Code, which can update your code to reference the new table.

![Hive table deprecation warning](https://docs.databricks.com/aws/en/assets/images/hive-migration-table-comment-6fe656130720603c30fc201d54067d46.png)

Your comment must use the following format:

    This table is deprecated. Please use catalog.default.table instead of hive_metastore.schema.table.

To learn how to add table comments using Catalog Explorer, see [Add comments to data and AI assets](https://docs.databricks.com/aws/en/comments/). To learn how to add table comments using SQL statements in a notebook or the SQL query editor, see [COMMENT ON](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-comment).

## Use Genie Code to update a deprecated table reference[​](#use-genie-code-to-update-a-deprecated-table-reference "Direct link to use-genie-code-to-update-a-deprecated-table-reference")

You can use Genie Code to replace references to deprecated Hive metastore tables with their Unity Catalog equivalents. Genie Code has advanced table search capabilities that can find the equivalent Unity Catalog table even if you don't know where in your catalog it is. Ask Genie Code to replace a `hive_metastore` table with an equivalent one in Unity Catalog, and it searches your catalog, identifies the best match based on schema similarity, and updates your code.

![Using Genie Code to replace a Hive metastore table with a UC equivalent.](https://docs.databricks.com/aws/en/assets/images/hive-to-uc-sql-15a2933312001d85fabd3ce8636d8a4d.gif)

See also [Use Genie Code](https://docs.databricks.com/aws/en/genie-code/use-genie-code).
