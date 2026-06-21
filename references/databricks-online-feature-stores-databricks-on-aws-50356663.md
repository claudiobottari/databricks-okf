---
title: Databricks Online Feature Stores | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/feature-store/online-feature-store
ingestedAt: "2026-06-18T08:10:26.442Z"
---

Databricks Online Feature Stores are a high-performance, scalable solution for serving feature data to online applications and real-time machine learning models. Powered by Databricks Lakebase, Online Feature Stores provide low-latency access to feature data at a high scale while maintaining consistency with your offline feature tables.

The primary use cases for Online Feature Stores include:

*   [Serving features to real-time applications](https://docs.databricks.com/aws/en/machine-learning/feature-store/feature-function-serving) like recommendation systems, fraud detection, and personalization engines using Feature Serving Endpoints.
*   [Automatic feature lookup for real-time inference in model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/feature-store/online-workflows).

New Online Feature Stores are now created as Lakebase Autoscaling projects. For details and differences, see [Lakebase unification on Autoscaling](https://docs.databricks.com/aws/en/oltp/upgrade-to-autoscaling).

## Requirements[​](#requirements "Direct link to Requirements")

Databricks Online Feature Stores requires Databricks Runtime 16.4 LTS ML or above. You can also use [serverless compute](https://docs.databricks.com/aws/en/compute/serverless/).

To use Databricks Online Feature Stores, you must first install the package. The following lines of code must be executed each time a notebook is run:

Python

    %pip install databricks-feature-engineering>=0.13.0dbutils.library.restartPython()

## Create an online store[​](#-create-an-online-store "Direct link to -create-an-online-store")

When you create an online store, you provision a highly available managed infrastructure for real-time feature serving. The `create_online_store` API creates a Lakebase Autoscaling instance. For details about Lakebase Autoscaling, see [Lakebase Postgres](https://docs.databricks.com/aws/en/oltp/projects/).

To manage costs, [delete Lakebase Provisioned online stores](#delete-an-online-store) when not in use for development and testing.

To create a new online feature store:

Python

    from databricks.feature_engineering import FeatureEngineeringClient# Initialize the clientfe = FeatureEngineeringClient()# Create an online store with specified capacityfe.create_online_store(    name="my-online-store", # maximum of 63 bytes    capacity="CU_2"  # Valid options: "CU_1", "CU_2", "CU_4", "CU_8")

The `capacity` setting controls how much compute your online store can use. Its value refers to the Lakebase Provisioned capacity, as described in [Compute size](https://docs.databricks.com/aws/en/oltp/upgrade-to-autoscaling#compute-size).

For information about permissions for Lakebase Autoscaling instances, see [Grant project permissions](https://docs.databricks.com/aws/en/oltp/projects/manage-project-permissions#grant-permissions).

For information about the capacity options for Lakebase Provisioned instances, see [Manage instance capacity](https://docs.databricks.com/aws/en/oltp/instances/create/#capacity).

### Encryption with customer-managed keys[​](#encryption-with-customer-managed-keys "Direct link to encryption-with-customer-managed-keys")

Online feature stores support encryption at rest with a customer-managed key (CMK) due to underlying support from Lakebase Autoscaling. No Lakebase or Feature Store configuration is required; CMK applies automatically for relevant workspaces.

CMK applies automatically when all of the following are true:

*   The workspace has a customer-managed key configured for managed services. See [Customer-managed keys for Lakebase](https://docs.databricks.com/aws/en/oltp/projects/customer-managed-keys).
*   The online feature store is backed by a Lakebase Autoscaling project. All online feature stores created with `fe.create_online_store` after March 23, 2026 use Lakebase Autoscaling.
*   The backing Lakebase project was created after CMK support became available in your region. Lakebase projects created before that are not encrypted with a CMK even if the workspace later enables one.

The Lakebase project backing an online feature store has the same name as the online store. To find it, click the ![App icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0yLjc1IDFDMS43ODM1IDEgMSAxLjc4MzUgMSAyLjc1QzEgMy43MTY1IDEuNzgzNSA0LjUgMi43NSA0LjVDMy43MTY1IDQuNSA0LjUgMy43MTY1IDQuNSAyLjc1QzQuNSAxLjc4MzUgMy43MTY1IDEgMi43NSAxWk04IDFDNy4wMzM1IDEgNi4yNSAxLjc4MzUgNi4yNSAyLjc1QzYuMjUgMy43MTY1IDcuMDMzNSA0LjUgOCA0LjVDOC45NjY1IDQuNSA5Ljc1IDMuNzE2NSA5Ljc1IDIuNzVDOS43NSAxLjc4MzUgOC45NjY1IDEgOCAxWk0xMy4yNSAxQzEyLjI4MzUgMSAxMS41IDEuNzgzNSAxMS41IDIuNzVDMTEuNSAzLjcxNjUgMTIuMjgzNSA0LjUgMTMuMjUgNC41QzE0LjIxNjUgNC41IDE1IDMuNzE2NSAxNSAyLjc1QzE1IDEuNzgzNSAxNC4yMTY1IDEgMTMuMjUgMVpNMi43NSA2LjI1QzEuNzgzNSA2LjI1IDEgNy4wMzM1IDEgOEMxIDguOTY2NSAxLjc4MzUgOS43NSAyLjc1IDkuNzVDMy43MTY1IDkuNzUgNC41IDguOTY2NSA0LjUgOEM0LjUgNy4wMzM1IDMuNzE2NSA2LjI1IDIuNzUgNi4yNVpNOCA2LjI1QzcuMDMzNSA2LjI1IDYuMjUgNy4wMzM1IDYuMjUgOEM2LjI1IDguOTY2NSA3LjAzMzUgOS43NSA4IDkuNzVDOC45NjY1IDkuNzUgOS43NSA4Ljk2NjUgOS43NSA4QzkuNzUgNy4wMzM1IDguOTY2NSA2LjI1IDggNi4yNVpNMTMuMjUgNi4yNUMxMi4yODM1IDYuMjUgMTEuNSA3LjAzMzUgMTEuNSA4QzExLjUgOC45NjY1IDEyLjI4MzUgOS43NSAxMy4yNSA5Ljc1QzE0LjIxNjUgOS43NSAxNSA4Ljk2NjUgMTUgOEMxNSA3LjAzMzUgMTQuMjE2NSA2LjI1IDEzLjI1IDYuMjVaTTIuNzUgMTEuNUMxLjc4MzUgMTEuNSAxIDEyLjI4MzUgMSAxMy4yNUMxIDE0LjIxNjUgMS43ODM1IDE1IDIuNzUgMTVDMy43MTY1IDE1IDQuNSAxNC4yMTY1IDQuNSAxMy4yNUM0LjUgMTIuMjgzNSAzLjcxNjUgMTEuNSAyLjc1IDExLjVaTTggMTEuNUM3LjAzMzUgMTEuNSA2LjI1IDEyLjI4MzUgNi4yNSAxMy4yNUM2LjI1IDE0LjIxNjUgNy4wMzM1IDE1IDggMTVDOC45NjY1IDE1IDkuNzUgMTQuMjE2NSA5Ljc1IDEzLjI1QzkuNzUgMTIuMjgzNSA4Ljk2NjUgMTEuNSA4IDExLjVaTTEzLjI1IDExLjVDMTIuMjgzNSAxMS41IDExLjUgMTIuMjgzNSAxMS41IDEzLjI1QzExLjUgMTQuMjE2NSAxMi4yODM1IDE1IDEzLjI1IDE1QzE0LjIxNjUgMTUgMTUgMTQuMjE2NSAxNSAxMy4yNUMxNSAxMi4yODM1IDE0LjIxNjUgMTEuNSAxMy4yNSAxMS41WiIgZmlsbD0iIzZGNkY2RiIvPgo8L3N2Zz4K) apps switcher in the top right corner of your workspace to open the Lakebase App and locate the project with that name. To confirm the store is encrypted with your CMK, check the **Customer-managed keys** status card on that project. See [Check encryption status](https://docs.databricks.com/aws/en/oltp/projects/customer-managed-keys#check-status).

## Manage online stores[​](#manage-online-stores "Direct link to Manage online stores")

The following code shows how to retrieve online stores:

Python

    # List all accessible online storesstores = fe.list_online_stores()for store in stores:    print(f"Store: {store.name}, State: {store.state}, Capacity: {store.capacity}")# Get information about an existing online storestore = fe.get_online_store(name="my-online-store")if store:    print(f"Store: {store.name}, State: {store.state}, Capacity: {store.capacity}")

If you created an online store using `fe.create_online_store`, you can update it using `fe.update_online_store`:

Python

    # Update the capacity of an online store# Note: this does not work for an Autoscaling instance that was created using the projects API or the UIupdated_store = fe.update_online_store(    name="my-online-store",    capacity="CU_4"  # Upgrade to higher capacity)

## Add read replicas to an online store[​](#add-read-replicas-to-an-online-store "Direct link to Add read replicas to an online store")

When creating or updating an online feature store, you can add read replicas to the online store by specifying the `read_replica_count` parameter. Read traffic is automatically distributed across read replicas, reducing latency and improving performance and scalability for high-concurrency workloads.

You cannot add read replicas to a Lakebase Autoscaling project that was created using the API or the UI.

## Publish a feature table to an online store[​](#publish-a-feature-table-to-an-online-store "Direct link to Publish a feature table to an online store")

After your online store is in the **AVAILABLE** state, you can publish feature tables to make them available for low-latency access. The `publish_table` API synchronizes data from your offline feature table to online store created using `create_online_store` API. Review the table below to ensure that your source offline table was created correctly for the real-time use case.

### Prerequisites for publishing to online stores[​](#prerequisites-for-publishing-to-online-stores "Direct link to Prerequisites for publishing to online stores")

All feature tables (with or without time series) must meet these requirements before publishing:

1.  **Primary key constraint**: Required for online store publishing
2.  **Non-nullable primary keys**: Primary key columns cannot contain NULL values
3.  **Change Data Feed enabled**: Required for the `CONTINUOUS` and `TRIGGERED` publish modes. See [Use change data feed](https://docs.databricks.com/aws/en/tables/features/change-data-feed#enable) for how to enable Delta Table Change Data Feed, and [Publish modes](#publish-modes) for a discussion of publish modes.

SQL

    -- Enable CDF if not already enabledALTER TABLE catalog.schema.your_feature_tableSET TBLPROPERTIES ('delta.enableChangeDataFeed' = 'true');-- Ensure primary key columns are not nullableALTER TABLE catalog.schema.your_feature_tableALTER COLUMN user_id SET NOT NULL;

### Publish a feature table[​](#publish-a-feature-table "Direct link to Publish a feature table")

To publish a feature table to an online store:

Python

    from databricks.ml_features.entities.online_store import DatabricksOnlineStore# Get the online store instance# For Lakebase Autoscaling projects creating using the Lakebase API or UI,# `name` is the last part of the resouce name: projects/{online_store_name}online_store = fe.get_online_store(name="my-online-store")# Publish the feature table to the online storefe.publish_table(    online_store=online_store,    source_table_name="catalog_name.schema_name.feature_table_name",    # for online_table_name, the catalog name, schema name, and table name each are limited to a maximum of 63 bytes    online_table_name="catalog_name.schema_name.online_feature_table_name",    # `publish_mode` argument is optional and defaults to "TRIGGERED" mode if not specified)

The `publish_table` operation does the following:

1.  Create a table in the online store if it doesn't exist.
2.  Sync the feature data from the offline feature table to the online store.
3.  Set up the necessary infrastructure for keeping the online store in sync with the offline table.

`publish_table` always uses the default branch of the Lakebase Autoscaling project.

### Publish modes[​](#publish-modes "Direct link to Publish modes")

The `publish_mode` parameter determines how and when the online table is updated with changes from the offline feature table.

See [Sync modes explained](https://docs.databricks.com/aws/en/oltp/instances/sync-data/sync-table#sync-modes-explained) for full details on the supported modes.

The supported modes are summarized below:

The `publish_mode` parameter replaces the `streaming` parameter starting from v0.13.0.1 and prior versions. For backward compatibility, if `streaming=True` is passed, it is equivalent to setting `publish_mode="CONTINUOUS"`.

### Delete an online table[​](#delete-an-online-table "Direct link to Delete an online table")

To delete an online table, use the Databricks SDK:

Python

    from databricks.sdk import WorkspaceClientw = WorkspaceClient()w.feature_store.delete_online_table(online_table_name="catalog_name.schema_name.online_feature_table_name")

important

This is the _only_ recommended method for deleting an online table. It removes the the table from both Unity Catalog and the database. Other methods such as the Databricks SQL command [`DROP TABLE`](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-drop-table) or the Python SDK command to [delete a synced table](https://docs.databricks.com/aws/en/oltp/instances/sync-data/sync-table#delete) _do not_ delete the table from underlying database storage.

## Explore and query online features[​](#explore-and-query-online-features "Direct link to Explore and query online features")

After your published table status shows as "AVAILABLE", you can explore and query the feature data in several ways:

**Unity Catalog UI**: Navigate to the online table in Unity Catalog to view sample data and explore the schema directly in the UI. This provides a convenient way to inspect your feature data and verify that the publishing process completed successfully.

**SQL Editor**: For more advanced querying and data exploration, you can use the SQL editor to run PostgreSQL queries against your online feature tables. This allows you to perform complex queries, joins, and analysis on your feature data. For detailed instructions on using the SQL editor with online stores, see [Query from Lakebase SQL Editor](https://docs.databricks.com/aws/en/oltp/projects/sql-editor).

## Use online features in real-time applications[​](#use-online-features-in-real-time-applications "Direct link to Use online features in real-time applications")

To serve features to real-time applications and services, create a feature serving endpoint. See [Feature Serving endpoints](https://docs.databricks.com/aws/en/machine-learning/feature-store/feature-function-serving).

Models that are trained using features from Databricks automatically track lineage to the features they were trained on. When deployed as endpoints, these models use Unity Catalog to find appropriate features in online stores. For details, see [Use features in online workflows](https://docs.databricks.com/aws/en/machine-learning/feature-store/online-workflows).

## Delete an online store[​](#delete-an-online-store "Direct link to Delete an online store")

To delete an online store:

Python

    fe.delete_online_store(name="my-online-store")

note

Deleting an online published table can lead to unexpected failures in downstream dependencies. Before you delete a table, you should ensure that its online features are no longer used by model serving or feature serving endpoints.

## Cost optimization best practices[​](#cost-optimization-best-practices "Direct link to Cost optimization best practices")

*   **Reuse online stores**: You can publish multiple feature tables to a single online store. For development, testing, and training scenarios, we recommend sharing one online store across multiple projects or users rather than creating separate stores.
*   **Right-size capacity**: Start with CU\_2 for testing and only scale up or down based on performance and cost.
*   **Delete online stores that are not in use**: Online stores continuously incur costs. [Delete online stores](#delete-an-online-store) that are no longer needed.

## Limitations[​](#limitations "Direct link to Limitations")

*   Specifying a specific online table is not supported. When a feature table is published to multiple online tables, model serving and feature serving endpoints always resolve to the oldest online table based on the creation timestamp.
*   An online feature store supports up to 3 read replicas (4 compute instances total, including the primary). Read replicas offload read traffic from the primary and provide high availability by taking over if the primary fails.
*   The following parameters are not supported when publishing to a Databricks online feature store: `filter_condition`, `checkpoint_location`, `mode`, `trigger`, and `features`.
*   Only feature tables in Unity Catalog are supported.
*   The only supported publish mode is "merge".
*   Lakebase scale-to-zero is not supported.
*   Feature Serving and Model Serving endpoints that look up features from multiple online feature stores cannot use Lakebase Autoscaling instances.
*   Autoscaling instances created using the projects API or the UI do not use the following fields: `creator`, `read_replica_count`, and `capacity`.
*   You cannot update an Autoscaling instance that was created using the projects API or the UI.
*   Customer-managed keys (CMK) apply only to online feature stores created after CMK became available in the region. See [Encryption with customer-managed keys](#cmk).

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

**Error message: `Skipping publishing to online table '...' because the feature sync pipeline is already running.`**

This error occurs if multiple notebooks or jobs try to publish to an online table at the same time. Only a single sync operation is allowed per online table at a time to prevent data conflicts.

Databricks recommends designing your workflows to use a single `publish_table` command, for example a single task at the end of a job. If your workflows cannot be coordinated in this way, use `get_status()` to wait until other publish commands have finished syncing before triggering a new publish.

## Example notebook[​](#example-notebook "Direct link to Example notebook")

The following notebook shows an example of how to set up and access a Databricks Online Feature Store using Databricks Lakebase.

#### Online feature store with Lakebase notebook

## Additional resources[​](#additional-resources "Direct link to Additional resources")

*   Learn more about [**Feature Engineering in Databricks**](https://docs.databricks.com/aws/en/machine-learning/feature-store/).
*   Explore data governances and lineage in [**Unity Catalog**](https://docs.databricks.com/aws/en/data-governance/unity-catalog/).

*   Understand [**Lakebase**](https://docs.databricks.com/aws/en/oltp/instances/) architecture and capabilities.
