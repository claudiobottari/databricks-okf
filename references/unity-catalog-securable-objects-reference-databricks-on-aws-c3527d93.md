---
title: Unity Catalog securable objects reference | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects
ingestedAt: "2026-06-18T08:04:51.777Z"
---

This page describes all securable objects in Unity Catalog. A [securable object](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/permissions-concepts#securable-objects) is an object defined in Unity Catalog on which privileges can be granted to a principal (user, service principal, or group).

## The Unity Catalog object hierarchy[​](#the-unity-catalog-object-hierarchy "Direct link to the-unity-catalog-object-hierarchy")

Securable objects in Unity Catalog are hierarchical. This hierarchical structure provides the foundation for access control in Unity Catalog.

The [metastore](#metastore) is the top-level securable object. Within this metastore, your data assets live in a three-level namespace that defines its [catalog](#catalog), [schema](#schema), and type of asset, such as [table](#table) (`catalog.schema.table`). The following diagram highlights these securable objects.

![Unity Catalog object hierarchy, focused on data assets](https://docs.databricks.com/aws/en/assets/images/object-hierarchy-0c4abcfff85defd8dbdb09f71b45575d.png)

The preceding diagram shows the following:

*   [**Catalogs**](#catalog) are the top-level layer for your data assets. Catalogs exist directly under the metastore. They are used to organize your data and AI assets, typically by organizational units or software development lifecycle scopes.
    *   [**Schemas**](#schema) exist within catalogs. They organize data and AI assets into categories that are more granular than catalogs. A schema may represent a single use case, project, or team sandbox.
        *   [**Tables**](#table) are collections of structured data organized by rows and columns.
        *   [**Views**](#view) are saved queries against other tables or views.
        *   [**Volumes**](#volume) represent collections of unstructured data in cloud object storage.
        *   [**Functions**](#function) are units of reusable logic that return a scalar value or set of rows.
        *   [**Models**](#model) are AI models packaged with MLflow and registered in Unity Catalog as functions.

There are also many other securable objects in Unity Catalog. All of these objects exist directly under the metastore. The following diagram highlights these securable objects.

![Unity Catalog object hierarchy, focused on non-data assets](https://docs.databricks.com/aws/en/assets/images/object-hierarchy-non-data-475640cdebef11bd4c370890d4aeafc3.png)

These securable objects can be broadly categorized into two groups. The first group includes objects that manage access to cloud storage and other external data sources and services:

*   [**Storage credentials**](#storage-credential) are objects that represent the authentication information required to access a specific path in cloud storage.
*   [**External locations**](#external-location) are objects that represent a specific path in cloud storage. It also includes a reference to the storage credential required to access that path.
*   An [**external metadata**](#external-metadata) object is used to define custom data lineage relationships for systems that operate outside of Unity Catalog.
*   [**Service credentials**](#service-credential) are objects that represent the authentication information required to access external cloud services.
*   [**Connections**](#connection) are objects that represent a connection to an external database system.

The second group includes objects that manage access to data and AI asset sharing across metastore or organizational boundaries:

*   [**Shares**](#share) are objects that represent a logical grouping of data assets that you intend to share with external [recipients](#recipient).
*   [**Providers**](#provider) are objects that represent an external organization or group of users that has shared data with your organization.
*   [**Recipients**](#recipient) are objects that represent an external organization or group of users that a [provider](#provider) shares data with.
*   [**Clean rooms**](#clean-room) are objects that represent a secure environment for collaborating with other organizations without exposing underlying data.

The following sections describe each securable object in greater detail.

The **metastore** is the top-level securable object in Unity Catalog. A metastore contains all securable objects registered in Unity Catalog in a single cloud region. These objects include not only the catalogs that organize your data, but also objects that control how data is accessed and shared, such as service credentials, storage credentials, external locations, connections, shares, recipients, providers, and clean rooms.

The following table summarizes important details about the metastore:

## Catalog[​](#catalog "Direct link to catalog")

Within a [metastore](#metastore), a **catalog** is the first and highest-level layer for your data assets. Catalogs are [container objects](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/permissions-concepts#container-objects). A catalog contains schemas, which in turn contain tables, views, volumes, and functions.

We frequently refer to the "three-level namespace" (`catalog`.`schema`.`table`) for data in Unity Catalog. Here, the catalog is the first layer of the three-level namespace.

The following table summarizes important details about catalogs:

For more information about catalogs, see [What are catalogs in Databricks?](https://docs.databricks.com/aws/en/catalogs/).

## Schema[​](#schema "Direct link to schema")

Within a [catalog](#catalog), a **schema** (also called a database) is the second layer of the object hierarchy for your data assets. Schemas are [container objects](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/permissions-concepts#container-objects). A schema contains tables, views, volumes, and functions.

We frequently refer to the _three-level namespace_ (that is, `catalog`.`schema`.`table`) for data in Unity Catalog. Here, the schema is the second layer of the three-level namespace.

The following table summarizes important details about schemas:

For more information about schemas, see [Schemas](https://docs.databricks.com/aws/en/schemas/).

## Table[​](#table "Direct link to table")

Within a [schema](#schema), a **table** is the primary securable object for structured data in Unity Catalog. Following are the types of tables in Databricks:

*   **Managed tables** are tables where the storage location path is determined by Unity Catalog. Importantly, the data itself still lives in your cloud account. Databricks recommends using managed tables to take advantage of the latest table features. See [Unity Catalog managed tables in Databricks for Delta Lake and Apache Iceberg](https://docs.databricks.com/aws/en/tables/managed).
*   **External tables** are tables where you specify the storage location path. Unity Catalog continues to manage the table's metadata, but doesn't manage the data's lifecycle, optimization, storage location, or layout. See [Work with external tables](https://docs.databricks.com/aws/en/tables/external).
*   **Foreign tables** are tables from a foreign catalog that are registered in Unity Catalog. See [Work with foreign tables](https://docs.databricks.com/aws/en/tables/foreign).

The following table summarizes important details about tables:

For more information about tables, see [Databricks tables](https://docs.databricks.com/aws/en/tables/).

## View[​](#view "Direct link to view")

Within a [schema](#schema), a **view** is a read-only object defined by a stored SQL query over one or more tables or other views. Views recompute results on every query.

The following table summarizes important details about views:

For more information about views, see [What is a view?](https://docs.databricks.com/aws/en/views/).

### Materialized view[​](#materialized-view "Direct link to materialized-view")

A **materialized view** is a view that pre-computes and stores its query results. Results reflect the state of data at the time the materialized view was last refreshed.

The permissions model for materialized views is the same as that of standard views. In addition to `SELECT` and `MANAGE`, materialized views support the `REFRESH` privilege, which allows a user to trigger a refresh of the materialized view's results. Users with only `SELECT` and the appropriate [usage privileges](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/permissions-concepts#usage-privileges) can query the stored results but cannot trigger a refresh.

For more information about materialized views, see [Materialized views](https://docs.databricks.com/aws/en/ldp/concepts/materialized-views).

### Metric view[​](#metric-view "Direct link to metric-view")

A **metric view** is a read-only object that defines a set of reusable metric definitions based on one or more tables, views, or SQL queries. Users query a metric view as they would a standard view.

The permissions model for materialized views is the same as that of standard views. Users need `SELECT` and the appropriate [usage privileges](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/permissions-concepts#usage-privileges) to query the metric view. The metric view owner's privileges are used to resolve the underlying data sources at query time.

For more information about metric views, see [Unity Catalog metric views](https://docs.databricks.com/aws/en/business-semantics/metric-views/).

## Volume[​](#volume "Direct link to volume")

Within a [schema](#schema), a **volume** is a securable object for unstructured data in cloud storage. Volumes can be managed (storage location determined by Unity Catalog) or external (you specify the storage path). Unlike tables and views, volumes do not support SQL query operations — they provide file-level read and write access to data in cloud storage. Following are the types of volumes in Databricks:

*   **Managed volumes** are volumes where the storage location path is determined by Unity Catalog. Importantly, the data itself still lives in your cloud account. Databricks recommends using managed volumes to have Unity Catalog automatically govern all data access.
*   **External volumes** are volumes where you specify the storage location path. You can use external volumes if you require external system access outside of Databricks, but be wary that external systems can bypass Unity Catalog governance.

The following table summarizes important details about volumes:

For more information about volumes, see [What are Unity Catalog volumes?](https://docs.databricks.com/aws/en/volumes/).

## Function[​](#function "Direct link to function")

Within a [schema](#schema), a **function** is a securable object in Unity Catalog that represents reusable, executable logic. Functions include user-defined functions (UDFs), stored procedures, and registered models (MLflow models registered in Unity Catalog).

*   **User-defined functions (UDFs)** are custom functions written in SQL or Python that can be called in SQL queries and notebooks. See [What are user-defined functions (UDFs)?](https://docs.databricks.com/aws/en/udf/).
*   **Stored procedures** are user-defined routines that execute a sequence of SQL statements and may include side effects such as inserting or updating data.
*   **Registered models** are MLflow machine learning models registered in Unity Catalog. In Unity Catalog, registered models are implemented as a type of function. See [Manage model lifecycle in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/).

The following table summarizes important details about functions:

### Model[​](#model "Direct link to model")

A **model** is a versioned MLflow machine learning model stored in Unity Catalog as a [function](#function) object. The model itself is the container. The artifacts and metadata for each training run are stored as **model versions** within it.

The permissions model for registered models is the same as that of functions. The following additional privileges apply specifically to models:

*   `APPLY TAG`: Allows adding and editing tags on a model and its versions. The user must also have `USE CATALOG` on the parent catalog and `USE SCHEMA` on the parent schema.
    
*   `CREATE MODEL VERSION`: Allows a user to register new versions of a model without granting the ability to execute, modify, or add tags to the model. The user must also have `USE CATALOG` on the parent catalog and `USE SCHEMA` on the parent schema.
    

Creating a model requires the `CREATE MODEL` privilege on the schema, not `CREATE FUNCTION`. `CREATE MODEL` can also be granted on a catalog to allow creating models in any schema in that catalog.

For more information about models, see [Manage model lifecycle in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/).

## Storage credential[​](#storage-credential "Direct link to storage-credential")

Within a [metastore](#metastore), a **storage credential** is a securable object that stores the authentication information required to access a specific path in cloud storage. The stored authentication method depends on the cloud provider: an IAM role on AWS, a service principal on Azure, or a service account on GCP.

Storage credentials are most commonly used as a building block for [external locations](#external-location), which pair a storage credential with a specific cloud storage path. A storage credential can also be used directly to create external tables.

To create a storage credential, a user needs the `CREATE STORAGE CREDENTIAL` privilege on the Unity Catalog metastore.

For more information about storage credentials, see [Overview of storage credentials](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/#storage-credentials).

## External location[​](#external-location "Direct link to external-location")

Within a [metastore](#metastore), an **external location** is a securable object that pairs a [storage credential](#storage-credential) with a cloud storage path. It governs access to a specific path in cloud storage.

To create an external location, a user needs the `CREATE EXTERNAL LOCATION` privilege on the Unity Catalog metastore.

After creating an external location, users need the `READ FILES` privilege to read files directly from the storage path, and the `WRITE FILES` privilege to write files. However, Databricks recommends managing cloud storage access through [volumes](#volume) and the `READ VOLUME` and `WRITE VOLUME` privileges rather than granting `READ FILES` and `WRITE FILES` directly on external locations.

For more information about external locations, see [Overview of external locations](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/#external-locations).

Within a [metastore](#metastore), an **external metadata** object is a securable object used to define custom data lineage relationships for systems that operate outside of Unity Catalog's native lineage tracking.

To create an external metadata object, a user needs the `CREATE EXTERNAL METADATA` privilege on the Unity Catalog metastore. To add or modify lineage relationships on the object, the user needs `MODIFY` on the external metadata object, plus the appropriate privileges on any Unity Catalog objects referenced in the relationship.

For more information about external metadata, see [Data lineage in Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-lineage).

## Service credential[​](#service-credential "Direct link to service-credential")

Within a [metastore](#metastore), a **service credential** is a securable object that stores authentication information for accessing external cloud services. This is unlike [storage credentials](#storage-credential), which govern access to cloud storage.

To create a service credential, a user needs the `CREATE SERVICE CREDENTIAL` privilege on the Unity Catalog metastore.

The `ACCESS` privilege allows a user to use the service credential to access an external service. `CREATE CONNECTION` on a service credential (combined with `CREATE CONNECTION` on the metastore) allows a user to create a connection to an external database using that credential.

For more information about service credentials, see [Create service credentials](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-services/service-credentials).

## Connection[​](#connection "Direct link to connection")

Within a [metastore](#metastore), a **connection** is a securable object that stores the endpoint and credentials needed to access an external system. Connections support the following scenarios:

*   [Query federation](https://docs.databricks.com/aws/en/query-federation/database-federation)
*   [Catalog federation](https://docs.databricks.com/aws/en/query-federation/catalog-federation)
*   [Managed ingestion](https://docs.databricks.com/aws/en/connect/managed-ingestion)
*   [JDBC access](https://docs.databricks.com/aws/en/connect/jdbc-connection)
*   [HTTP services](https://docs.databricks.com/aws/en/query-federation/http)

To create a connection, a user needs the `CREATE CONNECTION` privilege on the Unity Catalog metastore. If the connection uses a [service credential](#service-credential), the user also needs `CREATE CONNECTION` on that service credential.

The `USE CONNECTION` privilege allows a user to list and view connection details and use the connection for its supported scenario.

For more information, see [Unity Catalog connections](https://docs.databricks.com/aws/en/connect/uc-connections).

Within a [metastore](#metastore), a **share** is a securable object in OpenSharing that represents a logical grouping of data assets (tables, views, and volumes). A [provider](#provider) can then make the share available to external [recipients](#recipient).

The `SELECT` privilege on a share is granted to a recipient (not to individual users) to allow that recipient to read the assets in the share. To create a share, a user needs the `CREATE SHARE` privilege on the Unity Catalog metastore.

For more information about shares, see [Create shares for OpenSharing](https://docs.databricks.com/aws/en/delta-sharing/create-share).

## Provider[​](#provider "Direct link to provider")

Within a [metastore](#metastore), a **provider** is a securable object in OpenSharing that represents an external organization that has shared data with your organization. Provider objects are created in the recipient's Unity Catalog metastore. The `USE PROVIDER` privilege allows a user to view all providers and their shares, and, combined with `CREATE CATALOG`, to mount a shared catalog without requiring the metastore admin role.

To create a provider, a user needs the `CREATE PROVIDER` privilege on the Unity Catalog metastore.

For more information about providers, see [What is OpenSharing?](https://docs.databricks.com/aws/en/delta-sharing/).

## Recipient[​](#recipient "Direct link to recipient")

Within a [metastore](#metastore), a **recipient** is a securable object in OpenSharing that represents an external organization or group of users that a provider shares data with. Recipient objects are created in the provider's Unity Catalog metastore. No privileges can be granted on a recipient object itself. Access to shared data is controlled by granting `SELECT` on a [share](#share) to the recipient.

To create a recipient, a user needs the `CREATE RECIPIENT` privilege on the Unity Catalog metastore.

For more information about recipients, see [Create data recipients for OpenSharing (Databricks-to-Databricks sharing)](https://docs.databricks.com/aws/en/delta-sharing/create-recipient).

## Clean room[​](#clean-room "Direct link to clean-room")

Within a [metastore](#metastore), a **clean room** is a securable object that provides a secure environment for collaborating with other organizations on shared data without either party exposing their underlying data to the other.

To create a clean room, a user needs the `CREATE CLEAN ROOM` privilege on the Unity Catalog metastore.

The `EXECUTE CLEAN ROOM TASK` privilege allows a user to run notebooks inside the clean room and view clean room details. The `MODIFY CLEAN ROOM` privilege allows a user to update the clean room, including adding or removing data assets, notebooks, and comments.

For more information about clean rooms, see [What is Databricks Clean Rooms?](https://docs.databricks.com/aws/en/clean-rooms/).
