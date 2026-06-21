---
title: Work with the legacy Hive metastore alongside Unity Catalog | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/hive-metastore
ingestedAt: "2026-06-18T08:04:35.468Z"
---

This article explains one approach to continuing to use the legacy per-workspace Hive metastore when your Databricks workspace is enabled for Unity Catalog.

If your workspace was in service before it was enabled for Unity Catalog, it likely has a Hive metastore that contains data that you might want to continue to use. This article describes how to continue to work with tables that are registered in a Hive metastore.

important

The per-workspace Hive metastore is a legacy feature, and the instructions provided in this article represent legacy workflows.

Tables in the Hive metastore do not benefit from the full set of security and governance features provided by Unity Catalog, such as built-in auditing, lineage, and access control. Databricks recommends that you migrate those tables and the workloads that reference them to Unity Catalog and [disable direct access to the Hive metastore](#disable-hms).

Two migration paths are available:

*   Upgrade all tables registered in the Hive metastore to Unity Catalog.
    
*   Federate your Hive metastore to Unity Catalog using [Hive Metastore federation](https://docs.databricks.com/aws/en/query-federation/hms-federation-concepts#migration-3) for a more gradual approach. Hive metastore federation creates a foreign catalog in Unity Catalog that mirrors the Hive metastore.
    

See [Upgrade a Databricks workspace to Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/upgrade/).

The Unity Catalog metastore is additive, meaning it can be used with the per-workspace Hive metastore in Databricks. The Hive metastore appears as a top-level catalog called `hive_metastore` in the three-level namespace.

For example, you can refer to a table called `sales_raw` in the `sales` schema in the legacy Hive metastore by using the following notation:

*   SQL
*   Python
*   R
*   Scala

SQL

    SELECT * from hive_metastore.sales.sales_raw;

You can also specify the catalog and schema with a `USE` statement:

*   SQL
*   Python
*   R
*   Scala

SQL

    USE hive_metastore.sales;SELECT * from sales_raw;

If you configured [legacy table access control](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/table-acls/) on the Hive metastore, Databricks continues to enforce those access controls for data in the `hive_metastore` catalog for clusters running in the standard access mode.

The Unity Catalog access model differs slightly from legacy access controls:

*   **Metastore**: The Unity Catalog is an account-level object, and the Hive metastore is a workspace-level object. Permissions defined within the `hive_metastore` catalog always refer to the local users and groups in the workspace.
*   **Account groups**: Access control policies in Unity Catalog are applied to account groups, while access control policies for the Hive metastore are applied to workspace-local groups. See [Group sources](https://docs.databricks.com/aws/en/admin/users-groups/groups#sources).
*   **`USE CATALOG` and `USE SCHEMA` permissions are required on the catalog and schema for all operations on objects inside the catalog or schema**: Regardless of a principal's privileges on a table, the principal must also have the `USE CATALOG` privilege on its parent catalog to access the schema and the `USE SCHEMA` privilege to access objects within the schema. With workspace-level table access controls, on the other hand, granting `USAGE` on the root catalog automatically grants `USAGE` on all databases, but `USAGE` on the root catalog is not required.
*   **Views**: In Unity Catalog, the owner of a view does not need to be an owner of the view's referenced tables and views. Having the `SELECT` privilege is sufficient, along with `USE SCHEMA` on the views' parent schema and `USE CATALOG` on the parent catalog. With workspace-level table access controls, a view's owner needs to be an owner of all referenced tables and views.
*   **No support for `ANY FILE` or `ANONYMOUS FUNCTION`**: In Unity Catalog, there is no concept of an `ANY FILE` or `ANONYMOUS FUNCTION` securable that might allow an unprivileged user to run privileged code.
*   **No support for `DENY`**: The Unity Catalog privilege model is built on the principle of least privilege. Privileges that are not granted are implicitly denied.
*   **No `READ_METADATA` privilege**: Unity Catalog manages access to view metadata in a different way. See [Unity Catalog privileges reference](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/privileges-reference).

By using three-level namespace notation, you can join data in a Unity Catalog metastore with data in the legacy Hive metastore.

note

A join with data in the legacy Hive metastore will only work on the workspace where that data resides. Trying to run such a join in another workspace results in an error. Databricks recommends that you [upgrade](https://docs.databricks.com/aws/en/data-governance/unity-catalog/migrate) legacy tables and views to Unity Catalog.

The following example joins results from the `sales_current` table in the legacy Hive metastore with the `sales_historical` table in the Unity Catalog metastore when the `order_id` fields are equal.

*   SQL
*   Python
*   R
*   Scala

SQL

    SELECT * FROM hive_metastore.sales.sales_currentJOIN main.shared_sales.sales_historicalON hive_metastore.sales.sales_current.order_id = main.shared_sales.sales_historical.order_id;

## Default catalog[​](#default-catalog "Direct link to Default catalog")

A default catalog is configured for each workspace that is enabled for Unity Catalog.

If you omit the top-level catalog name when you perform data operations, the default catalog is assumed.

The default catalog that was initially configured for your workspace depends on how your workspace was enabled for Unity Catalog:

*   If your workspace was enabled for Unity Catalog automatically, the _workspace catalog_ was set as the default catalog. See [Get started with Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/get-started).
*   If your workspace was enabled for Unity Catalog manually, the `hive_metastore` catalog was set as the default catalog.

If you are transitioning from the Hive metastore to Unity Catalog within an existing workspace, it makes sense to use `hive_metastore` as the default catalog to avoid impacting existing code that references the hive metastore unless you have fully migrated off Hive metastore.

To learn how to get and switch the default catalog, see [Manage the default catalog](https://docs.databricks.com/aws/en/catalogs/default)

## Cluster-scoped data access permissions[​](#cluster-scoped-data-access-permissions "Direct link to Cluster-scoped data access permissions")

When you use the Hive metastore alongside Unity Catalog, data access credentials associated with the cluster are used to access Hive metastore data but not data registered in Unity Catalog.

If users access paths that are outside Unity Catalog (such as a path not registered as a table or external location) then the access credentials assigned to the cluster are used.

The Databricks\-hosted legacy Hive metastore has resource limits to ensure reliability, including limits on concurrent (active) connections and connections per hour. If workloads exceed these limits, clusters and jobs might encounter metastore connection errors or fail to start.

To avoid reaching these limits:

*   **Migrate to Unity Catalog**: The most effective approach is to upgrade tables and [disable direct access to the Hive metastore](#disable-hms). Unity Catalog doesn't use the legacy Hive metastore, so Hive metastore\-specific database connection limits no longer apply. See [Upgrade a Databricks workspace to Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/upgrade/).
*   **Optimize workload orchestration to smooth peak concurrency**: Avoid synchronized job and cluster launches, limit burst fan-out, and minimize transient Hive metastore activity spikes that increase the likelihood of connection-limit breaches.

After you migrate your tables to Unity Catalog, Databricks recommends explicitly disabling direct access to the Hive metastore. By default, Databricks compute clusters continue to connect to the Hive metastore even after migration, unless you explicitly disable Hive metastore access.

You can disable direct access to the Hive metastore across your entire workspace, or individually per compute cluster. See [Disable access to the Hive metastore used by your Databricks workspace](https://docs.databricks.com/aws/en/data-governance/unity-catalog/disable-hms).
