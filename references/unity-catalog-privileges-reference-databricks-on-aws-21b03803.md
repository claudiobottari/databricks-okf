---
title: Unity Catalog privileges reference | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/privileges-reference
ingestedAt: "2026-06-18T08:03:44.141Z"
---

This page is a reference for Unity Catalog privileges and the securable objects they apply to.

For detailed descriptions of each securable object type, see [Unity Catalog securable objects reference](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects). To learn how to grant privileges in Unity Catalog, see [Show, grant, and revoke privileges](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/#grant).

note

This page refers to the Unity Catalog privileges and inheritance model in Privilege Model version 1.0. If you created your Unity Catalog metastore during the public preview (before August 25, 2022), you might be on an earlier privilege model that doesn't support the current inheritance model. You can upgrade to Privilege Model version 1.0 to get [privilege inheritance](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/permissions-concepts#inheritance). See [Upgrade to privilege inheritance](https://docs.databricks.com/aws/en/archive/unity-catalog/upgrade-privilege-model).

## Securable objects in Unity Catalog[​](#securable-objects-in-unity-catalog "Direct link to securable-objects-in-unity-catalog")

A securable object is an object defined in the Unity Catalog [metastore](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#metastore) on which privileges can be granted to a principal (user, service principal, or group). Securable objects in Unity Catalog are hierarchical, from the [metastore](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#metastore) at the top, through [catalogs](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#catalog) and [schemas](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#schema), down to the data objects they contain ([tables](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#table), [views](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#view), [volumes](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#volume), [functions](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#function), and [models](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#model)). Additional securable objects govern access to external storage, external services, and OpenSharing.

![Unity Catalog object hierarchy](https://docs.databricks.com/aws/en/assets/images/object-hierarchy-0c4abcfff85defd8dbdb09f71b45575d.png)

For detailed descriptions of each securable object type, see [Unity Catalog securable objects reference](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects).

## What privileges apply to each securable object?[​](#what-privileges-apply-to-each-securable-object "Direct link to what-privileges-apply-to-each-securable-object")

The following table lists the privileges that apply to each securable object in Unity Catalog. To learn how to grant privileges in Unity Catalog, see [Show, grant, and revoke privileges](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/#grant).

## Overview of privileges in Unity Catalog[​](#overview-of-privileges-in-unity-catalog "Direct link to overview-of-privileges-in-unity-catalog")

The following table summarizes the capability each Unity Catalog privilege grants. For full descriptions, see [Detailed Unity Catalog privileges reference](#privilege-descriptions).

## Detailed Unity Catalog privileges reference[​](#detailed-unity-catalog-privileges-reference "Direct link to detailed-unity-catalog-privileges-reference")

This section provides details about the privileges that apply generally to Unity Catalog. To learn how to grant privileges in Unity Catalog, see [Show, grant, and revoke privileges](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/#grant).

### ACCESS[​](#access "Direct link to access")

*   **Applicable object types: `SERVICE CREDENTIAL`**

Allows a user to use a [service credential](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#service-credential) to access external services.

### ALL PRIVILEGES[​](#all-privileges "Direct link to all-privileges")

*   **Applicable object types: `CONNECTION`, `EXTERNAL LOCATION`, `EXTERNAL METADATA`, `FUNCTION` (including models), `MATERIALIZED VIEW`, `SERVICE CREDENTIAL`, `STORAGE CREDENTIAL`, `TABLE`, `VIEW`, `VOLUME`**
*   **Applicable container objects: `SCHEMA`, `CATALOG`**

`ALL PRIVILEGES` is a special privilege that allows a user to perform all capabilities on the securable object and its child objects. `ALL PRIVILEGES` _implies_ all applicable privileges for a specific object type, and Databricks doesn't explicitly grant each individual privilege.

The following table describes what `ALL PRIVILEGES` implies for data objects in the Unity Catalog hierarchy:

The following table describes what `ALL PRIVILEGES` implies for non-data securable objects:

\*To prevent accidental data exfiltration or privilege escalation, `ALL PRIVILEGES` does not include the `EXTERNAL USE SCHEMA`, `EXTERNAL USE LOCATION`, or `MANAGE` privileges.

When listing permissions using the Databricks API or with a [`SHOW GRANTS`](https://docs.databricks.com/aws/en/sql/language-manual/security-show-grant) command for a user with `ALL PRIVILEGES`, only `ALL PRIVILEGES` is returned, not the individual implied privileges like `SELECT` or `MODIFY`.

When `ALL PRIVILEGES` is revoked, both the `ALL PRIVILEGES` grant and any individual privileges implied by it are removed. The `EXTERNAL USE SCHEMA`, `EXTERNAL USE LOCATION`, and `MANAGE` privileges are not affected.

To maintain backward compatibility, `ALL PRIVILEGES` is evaluated at the time permissions checks are made. This means that as Databricks releases new privileges and securable objects, an existing `ALL PRIVILEGES` grant automatically includes any new privileges applicable to the securable object, and all new and existing child objects.

### APPLY TAG[​](#apply-tag "Direct link to apply-tag")

*   **Applicable object types: `EXTERNAL METADATA`, `FUNCTION` (registered models only), `MATERIALIZED VIEW`, `TABLE`, `VIEW`, `VOLUME`**
*   **Applicable container objects: `SCHEMA`, `CATALOG`**

Allows a user to add and edit tags on a securable object. In addition:

*   For a [table](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#table) or [view](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#view), having `APPLY TAG` also enables column-level tagging.
*   For a registered [model](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#model), `APPLY TAG` also enables version-level tagging.

The user must also have `USE CATALOG` on the parent catalog and `USE SCHEMA` on the parent schema. [External metadata](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#external-metadata) objects are not contained in a catalog or schema, so these usage privileges do not apply.

To apply a [governed tag](https://docs.databricks.com/aws/en/admin/governed-tags/), you must also have the `ASSIGN` privilege on the governed tag. See [Manage permissions on governed tags](https://docs.databricks.com/aws/en/admin/governed-tags/manage-permissions).

Public Preview

Applying tags to [external metadata](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#external-metadata) objects is in Public Preview. SQL support for tagging external metadata requires Databricks Runtime 18.2 or above.

### BROWSE[​](#browse "Direct link to browse")

*   **Applicable object types: `CLEAN ROOM`, `EXTERNAL LOCATION`, `EXTERNAL METADATA`**
*   **Applicable container objects: `CATALOG`**

The `BROWSE` privilege is a special privilege that allows users to discover and view metadata about objects without granting access to the underlying data. Users with `BROWSE` can:

*   See that an object exists
*   View its name, description, and tags
*   Request access to it

For data objects (tables, views, volumes, and functions), `BROWSE` can be granted at the catalog level only. It allows you to discover and view all objects within that catalog, but it won't explicitly appear as an inherited privilege when viewing permissions on schemas and child objects in Catalog Explorer.

For [external locations](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#external-location), [external metadata](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#external-metadata), and [clean rooms](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#clean-room), you can grant `BROWSE` directly on the object itself.

Users with `BROWSE` do not need usage privileges like `USE CATALOG` or `USE SCHEMA` to discover and view metadata.

Databricks recommends granting `BROWSE` on [catalogs](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#catalog) to the `All account users` group to make data discoverable throughout your organization. This enables users to find data and request access without requiring administrators to grant permissions preemptively.

### CREATE CATALOG[​](#create-catalog "Direct link to create-catalog")

*   **Applicable container objects: Unity Catalog metastore**

Allows a user to create a [catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#catalog) in a Unity Catalog [metastore](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#metastore). To create a foreign catalog, you must also have the [CREATE FOREIGN CATALOG](#foreign-catalog) privilege on the [connection](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#connection) that contains the foreign catalog or on the [metastore](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#metastore).

### CREATE CLEAN ROOM[​](#create-clean-room "Direct link to create-clean-room")

*   **Applicable container objects: Unity Catalog metastore**

Allows a user to create a [clean room](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#clean-room) for securely collaborating on projects with other organizations without sharing underlying data.

### CREATE CONNECTION[​](#create-connection "Direct link to create-connection")

*   **Applicable object types: `SERVICE CREDENTIAL`**
*   **Applicable container objects: Unity Catalog metastore**

Allows a user to create a [connection](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#connection) to an external database in a Lakehouse Federation scenario. To use a service credential to create a connection, the user must have this privilege on both the [metastore](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#metastore) and the [service credential](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#service-credential).

### CREATE EXTERNAL LOCATION[​](#create-external-location "Direct link to create-external-location")

*   **Applicable object types: `STORAGE CREDENTIAL`**
*   **Applicable container objects: Unity Catalog metastore**

To create an [external location](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#external-location), the user must have this privilege on both the [metastore](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#metastore) and the [storage credential](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#storage-credential) that is being referenced in the external location.

### CREATE EXTERNAL METADATA[​](#create-external-metadata "Direct link to create-external-metadata")

*   **Applicable container objects: Unity Catalog metastore**

Allows a user to create an [external metadata](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#external-metadata) object for use in custom lineage. To add lineage relationships to the external metadata object, the user must have the `MODIFY` privilege on the external metadata object, along with privileges on the Unity Catalog object that they are specifying the relationship with.

### CREATE EXTERNAL TABLE[​](#create-external-table "Direct link to create-external-table")

*   **Applicable object types: `EXTERNAL LOCATION`, `STORAGE CREDENTIAL`**

Allows a user to create external tables directly in your cloud tenant using an [external location](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#external-location) or [storage credential](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#storage-credential). Databricks recommends granting this privilege on an external location rather than storage credential because it's scoped to a path, which allows more control over where users can create external tables in your cloud tenant.

### CREATE EXTERNAL VOLUME[​](#create-external-volume "Direct link to create-external-volume")

*   **Applicable object types: `EXTERNAL LOCATION`**

Allows a user to create external volumes using an [external location](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#external-location).

### CREATE FOREIGN CATALOG[​](#create-foreign-catalog "Direct link to create-foreign-catalog")

*   **Applicable object types: `CONNECTION`**

Allows a user to create foreign catalogs using a [connection](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#connection) to an external database in a Lakehouse Federation scenario.

### CREATE FOREIGN SECURABLE[​](#create-foreign-securable "Direct link to create-foreign-securable")

*   **Applicable object types: `EXTERNAL LOCATION`**

Allows a user who is creating a foreign catalog to specify [authorized paths](https://docs.databricks.com/aws/en/query-federation/hms-federation-concepts#authorized-paths) that are covered by the [external location](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#external-location).

The user must also have `CREATE CATALOG` on the [metastore](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#metastore) and `CREATE FOREIGN CATALOG` on the [connection](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#connection).

### CREATE FUNCTION[​](#create-function "Direct link to create-function")

*   **Applicable container objects: `SCHEMA`, `CATALOG`**

Allows a user to create a [function](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#function). Following the principle of least privilege, Databricks recommends granting `CREATE FUNCTION` at the schema level, which allows users to create functions in that schema. You can also grant `CREATE FUNCTION` on a [catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#catalog) to allow a user to create [functions](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#function) in any existing or future schema in the catalog.

The user must also have the `USE CATALOG` privilege on the parent catalog and `USE SCHEMA` on the parent schema.

### CREATE MANAGED STORAGE[​](#create-managed-storage "Direct link to create-managed-storage")

*   **Applicable object types: `EXTERNAL LOCATION`**

Allows a user to configure a custom managed storage location within an [external location](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#external-location) when creating a [catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#catalog) or [schema](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#schema). When used during catalog creation, the specified location becomes the default managed storage for all schemas in that catalog (overriding the [metastore](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#metastore) default). When used during schema creation, the specified location applies to that schema only (overriding any catalog-level default).

### CREATE MATERIALIZED VIEW[​](#create-materialized-view "Direct link to create-materialized-view")

*   **Applicable container objects: `SCHEMA`, `CATALOG`**

Allows a user to create a [materialized view](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#materialized-view) in a [schema](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#schema) on which `CREATE MATERIALIZED VIEW` is granted. Following the principle of least privilege, Databricks recommends granting `CREATE MATERIALIZED VIEW` at the schema level. You can also grant `CREATE MATERIALIZED VIEW` on a [catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#catalog) to allow a user to create materialized views in any existing or future schema in the catalog.

The user must also have the `USE CATALOG` privilege on the parent catalog and `USE SCHEMA` on the parent schema.

### CREATE MODEL[​](#create-model "Direct link to create-model")

*   **Applicable container objects: `SCHEMA`, `CATALOG`**

Allows a user to create an MLflow registered [model](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#model) (which is a type of [function](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#function)) in a [schema](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#schema) on which `CREATE MODEL` is granted. Following the principle of least privilege, Databricks recommends granting `CREATE MODEL` at the schema level. You can also grant `CREATE MODEL` on a [catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#catalog) to allow a user to create registered models in any existing or future schema in the catalog.

The user must also have the `USE CATALOG` privilege on the parent catalog and `USE SCHEMA` on the parent schema.

### CREATE MODEL VERSION[​](#create-model-version "Direct link to create-model-version")

*   **Applicable object types: `MODEL`**

Allows a user to register a new version of an MLflow registered [model](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#model) (which is a type of [function](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#function)). Does not grant permission to execute, modify, or add tags to a model version.

The user must also have the `USE CATALOG` privilege on the parent catalog and `USE SCHEMA` on the parent schema.

### CREATE SCHEMA[​](#create-schema "Direct link to create-schema")

*   **Applicable container objects: `CATALOG`**

Allows a user to create a [schema](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#schema) in a [catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#catalog) on which `CREATE SCHEMA` is granted. The user must also have the `USE CATALOG` privilege on the catalog.

### CREATE SERVICE CREDENTIAL[​](#create-service-credential "Direct link to create-service-credential")

*   **Applicable container objects: Unity Catalog metastore**

Allows a user to create a [service credential](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#service-credential) in a Unity Catalog [metastore](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#metastore).

### CREATE STORAGE CREDENTIAL[​](#create-storage-credential "Direct link to create-storage-credential")

*   **Applicable container objects: Unity Catalog metastore**

Allows a user to create a [storage credential](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#storage-credential) in a Unity Catalog [metastore](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#metastore).

### CREATE TABLE[​](#create-table "Direct link to create-table")

*   **Applicable container objects: `SCHEMA`, `CATALOG`**

Allows a user to create a [table](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#table) or [view](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#view) in a [schema](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#schema) on which `CREATE TABLE` is granted. Following the principle of least privilege, Databricks recommends granting `CREATE TABLE` at the schema level. You can also grant `CREATE TABLE` on a [catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#catalog) to allow a user to create tables or views in any existing or future schema in the catalog.

The user must also have the `USE CATALOG` privilege on the parent catalog and the `USE SCHEMA` privilege on the parent schema.

### CREATE VOLUME[​](#create-volume "Direct link to create-volume")

*   **Applicable container objects: `SCHEMA`, `CATALOG`**

Allows a user to create a [volume](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#volume) in a [schema](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#schema) on which `CREATE VOLUME` is granted. Following the principle of least privilege, Databricks recommends granting `CREATE VOLUME` at the schema level. You can also grant `CREATE VOLUME` on a [catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#catalog) to allow a user to create [volumes](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#volume) in any existing or future schema in the catalog.

The user must also have the `USE CATALOG` privilege on the parent catalog and the `USE SCHEMA` privilege on the parent schema.

### EXECUTE[​](#execute "Direct link to execute")

*   **Applicable object types: `FUNCTION`**
*   **Applicable container objects: `SCHEMA`, `CATALOG`**

Allows a user to invoke a [function](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#function) or load a registered [model](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#model) for inference. For functions, `EXECUTE` also grants the ability to view the function definition and metadata. For registered models, `EXECUTE` also grants the ability to view metadata for all model versions and download model files.

Following the principle of least privilege, Databricks recommends granting `EXECUTE` on individual functions. You can also grant `EXECUTE` on a [schema](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#schema) or [catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#catalog) to allow a user to execute all current and future functions within that schema or catalog.

The user must also have `USE CATALOG` on the parent catalog and `USE SCHEMA` on the parent schema.

### EXECUTE CLEAN ROOM TASK[​](#execute-clean-room-task "Direct link to execute-clean-room-task")

*   **Applicable object types: `CLEAN ROOM`**

Allows a user to run tasks (notebooks) in a [clean room](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#clean-room). Also enables the user to view clean room details.

### EXTERNAL USE LOCATION[​](#external-use-location "Direct link to external-use-location")

*   **Applicable object types: `EXTERNAL LOCATION`**

Allows a user to obtain a temporary credential to access an [external location](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#external-location) from an external processing engine using the Unity Catalog open APIs or Apache Spark.

To avoid accidental data exfiltration, `ALL PRIVILEGES` does not include the `EXTERNAL USE LOCATION` privilege, and external location owners do not have this privilege by default. This means that only users with the `MANAGE` privilege on the external location can grant this privilege.

See [Enable external data access to Unity Catalog](https://docs.databricks.com/aws/en/external-access/admin).

### EXTERNAL USE SCHEMA[​](#external-use-schema "Direct link to external-use-schema")

*   **Applicable container objects: `SCHEMA`**

Allows a user to be granted a temporary credential to access Unity Catalog tables from an external processing engine using the Unity Catalog open APIs or Iceberg REST APIs.

To avoid accidental data exfiltration, `ALL PRIVILEGES` does not include the `EXTERNAL USE SCHEMA` privilege, and schema owners do not have this privilege by default. Only the [catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#catalog) owner can grant this privilege.

See [Enable external data access to Unity Catalog](https://docs.databricks.com/aws/en/external-access/admin).

### MANAGE[​](#manage "Direct link to manage")

*   **Applicable object types: `CLEAN ROOM`, `CONNECTION`, `EXTERNAL LOCATION`, `EXTERNAL METADATA`, `FUNCTION` (including models), `MATERIALIZED VIEW`, `SERVICE CREDENTIAL`, `STORAGE CREDENTIAL`, `TABLE`, `VIEW`, `VOLUME`**
*   **Applicable container objects: `SCHEMA`, `CATALOG`**

Allows a user to manage privileges on, transfer ownership of, and delete an object without being the owner. `MANAGE` is similar to object ownership, but there are some important differences. See [Ownership versus the `MANAGE` privilege](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/permissions-concepts#ownership-vs-manage).

Users with `MANAGE` are not automatically granted all privileges on the object. They must be granted each specific privilege separately, but users with `MANAGE` can explicitly grant themselves these privileges.

To exercise `MANAGE`, the user must also have the appropriate usage privileges on the object and all its parent objects. For example, to exercise `MANAGE` on a [schema](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#schema), the user also needs `USE SCHEMA` on the schema and `USE CATALOG` on the parent catalog.

If `MANAGE` is granted on a container object, the user also gets `MANAGE` on all child objects. For example, granting `MANAGE` on a [catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#catalog) also explicitly grants `MANAGE` on all child schemas and tables.

`ALL PRIVILEGES` does not include the `MANAGE` privilege.

### MANAGE ALLOWLIST[​](#manage-allowlist "Direct link to manage-allowlist")

*   **Applicable container objects: Unity Catalog metastore**

Allows a user to add, modify, and remove entries in the allowlist that controls which init scripts, JAR files, and Maven coordinates can run on Unity Catalog\-enabled clusters configured with standard access mode. By default, the allowlist is empty.

Because users with `MANAGE ALLOWLIST` can control what code runs on standard access mode compute, Databricks recommends granting this privilege to metastore admins and trusted platform administrators only.

See [Allowlist libraries and init scripts on compute with standard access mode (formerly shared access mode)](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/allowlist).

### MODIFY[​](#modify "Direct link to modify")

*   **Applicable object types: `EXTERNAL METADATA`, `TABLE`**
*   **Applicable container objects: `SCHEMA`, `CATALOG`**

When applied to a [table](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#table), allows a user to insert, update, and delete data in the table. The user must also have `SELECT` on the table, `USE SCHEMA` on the parent schema, and `USE CATALOG` on the parent catalog.

Due to [privilege inheritance](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/permissions-concepts#inheritance), you can grant `MODIFY` on a [schema](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#schema) to automatically grant `MODIFY` on all current and future tables in the schema. Similarly, you can grant `MODIFY` on a [catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#catalog) to automatically grant `MODIFY` on all current and future tables in the catalog.

When applied to an [external metadata](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#external-metadata) object, allows a user to add lineage relationships to that object.

note

`MODIFY` cannot be granted on a [foreign table](https://docs.databricks.com/aws/en/tables/foreign) because foreign tables are read-only.

### MODIFY CLEAN ROOM[​](#modify-clean-room "Direct link to modify-clean-room")

*   **Applicable object types: `CLEAN ROOM`**

Allows a user to update a [clean room](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#clean-room), which includes adding and removing data assets, adding and removing notebooks, and updating comments. Also enables the user to view clean room details.

### READ FILES[​](#read-files "Direct link to read-files")

*   **Applicable object types: `EXTERNAL LOCATION`**

Allows a user to read files directly from cloud object storage configured as an [external location](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#external-location). Databricks recommends against reading files directly from cloud object storage. Instead, manage read access to data in cloud object storage using [volumes](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#volume) and the `READ VOLUME` privilege. See [External locations](https://docs.databricks.com/aws/en/data-governance/unity-catalog/best-practices#external-loc).

`READ FILES` is also required for write operations on external locations. Any principal that has the `WRITE FILES` privilege only on an external location receives a `PERMISSION_DENIED` error when attempting to write files. See [WRITE FILES](#write-files).

### READ VOLUME[​](#read-volume "Direct link to read-volume")

*   **Applicable object types: `VOLUME`**
*   **Applicable container objects: `SCHEMA`, `CATALOG`**

Allows a user to read files and directories stored inside a [volume](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#volume). The user must also have `USE SCHEMA` on the parent schema and `USE CATALOG` on the parent catalog.

Due to [privilege inheritance](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/permissions-concepts#inheritance), you can grant `READ VOLUME` on a [schema](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#schema) to automatically grant `READ VOLUME` on all current and future volumes in the schema. Similarly, you can grant `READ VOLUME` on a [catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#catalog) to automatically grant `READ VOLUME` on all current and future volumes in the catalog.

### REFRESH[​](#refresh "Direct link to refresh")

*   **Applicable object types: `MATERIALIZED VIEW`**
*   **Applicable container objects: `SCHEMA`, `CATALOG`**

Allows a user to refresh a materialized view. The user must also have `USE SCHEMA` on the parent schema and `USE CATALOG` on the parent catalog.

Due to [privilege inheritance](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/permissions-concepts#inheritance), you can grant `REFRESH` on a [schema](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#schema) to automatically grant `REFRESH` on all current and future materialized views in the schema. Similarly, you can grant `REFRESH` on a [catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#catalog) to automatically grant `REFRESH` on all current and future materialized views in the catalog.

### SELECT[​](#select "Direct link to select")

*   **Applicable object types: `MATERIALIZED VIEW`, `SHARE`, `TABLE`, `VIEW`**
*   **Applicable container objects: `SCHEMA`, `CATALOG`**

When applied to a [table](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#table), [view](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#view), or materialized view, allows a user to select from the object. The user must also have `USE CATALOG` on the parent catalog and `USE SCHEMA` on the parent schema. When applied to a [share](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#share), allows a [recipient](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#recipient) to select from the share.

Due to [privilege inheritance](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/permissions-concepts#inheritance), you can grant `SELECT` on a [schema](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#schema) to automatically grant `SELECT` on all current and future tables and views in the schema. Similarly, you can grant `SELECT` on a [catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#catalog) to automatically grant `SELECT` on all current and future tables and views in the catalog.

### USE CATALOG[​](#use-catalog "Direct link to use-catalog")

*   **Applicable container objects: `CATALOG`**

`USE CATALOG` is a [usage privilege](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/permissions-concepts#usage-privileges). Generally, users need this privilege to interact with any object within the [catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#catalog). `USE CATALOG` does not grant access to the catalog itself or to any specific objects within it.

For example, to read from a table, a user needs `SELECT` on the table, `USE CATALOG` on the parent catalog, and `USE SCHEMA` on the parent schema.

`USE CATALOG` also provides an important access control boundary for catalog owners. Even if a table owner grants `SELECT` on a table to another user, that user cannot access the table unless they also have `USE CATALOG` on the parent catalog. Because only catalog owners or users with `MANAGE` on the catalog can grant `USE CATALOG`, catalog owners retain control over which users can access their objects, regardless of what individual table or schema owners grant.

`USE CATALOG` is not required to discover or read object metadata if the user has the [`BROWSE`](#browse) privilege on that catalog.

### USE CONNECTION[​](#use-connection "Direct link to use-connection")

*   **Applicable object types: `CONNECTION`**

Allows a user to list and view details about [connections](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#connection) to external databases in a [Lakehouse Federation](https://docs.databricks.com/aws/en/query-federation/) scenario. `USE CONNECTION` is also required to use the [`remote_query` function](https://docs.databricks.com/aws/en/query-federation/remote-queries) to run SQL queries directly on external databases.

### USE SCHEMA[​](#use-schema "Direct link to use-schema")

*   **Applicable container objects: `SCHEMA`, `CATALOG`**

`USE SCHEMA` is a [usage privilege](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/permissions-concepts#usage-privileges). Generally, users need this privilege to interact with any object within the [schema](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#schema). `USE SCHEMA` does not grant access to the schema itself or to any specific objects within it.

For example, to read from a table, a user needs `SELECT` on the table, `USE SCHEMA` on the parent schema, and `USE CATALOG` on the parent catalog.

`USE SCHEMA` also provides an important access control boundary for schema owners. Even if a table owner grants `SELECT` on a table to another user, that user cannot access the table unless they also have `USE SCHEMA` on the parent schema. Because only schema owners or users with `MANAGE` on the schema can grant `USE SCHEMA`, schema owners retain control over which users can access their objects, regardless of what individual table owners grant.

Due to [privilege inheritance](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/permissions-concepts#inheritance), you can grant `USE SCHEMA` on a [catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#catalog) to automatically grant `USE SCHEMA` on all current and future schemas in the catalog.

`USE SCHEMA` is not required to discover or read object metadata if the user has the [`BROWSE`](#browse) privilege on the parent catalog.

### WRITE FILES[​](#write-files "Direct link to write-files")

*   **Applicable object types: `EXTERNAL LOCATION`**

Allows a user to write files directly to cloud object storage configured as an [external location](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#external-location). Databricks recommends against writing files directly to cloud object storage. Instead, manage write access to data in cloud object storage using [volumes](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#volume) and the `WRITE VOLUME` privilege. For more guidance, see [Managed and external volumes](https://docs.databricks.com/aws/en/data-governance/unity-catalog/best-practices#managed-external-volumes).

note

`WRITE FILES` requires `READ FILES` to also be granted on the same external location. Write operations on cloud object storage involve metadata checks and path validation that require read access.

### WRITE VOLUME[​](#write-volume "Direct link to write-volume")

*   **Applicable object types: `VOLUME`**
*   **Applicable container objects: `SCHEMA`, `CATALOG`**

Allows a user to add, remove, or modify files and directories stored inside a [volume](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#volume). The user must also have `USE CATALOG` on the parent catalog and `USE SCHEMA` on the parent schema.

Due to [privilege inheritance](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/permissions-concepts#inheritance), you can grant `WRITE VOLUME` on a [schema](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#schema) to automatically grant `WRITE VOLUME` on all current and future volumes in the schema. Similarly, you can grant `WRITE VOLUME` on a [catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#catalog) to automatically grant `WRITE VOLUME` on all current and future volumes in the catalog.

## Privileges that apply only to OpenSharing or Databricks Marketplace[​](#privileges-that-apply-only-to-opensharing-or-databricks-marketplace "Direct link to privileges-that-apply-only-to-opensharing-or-databricks-marketplace")

This section provides details about the privileges that apply only to OpenSharing.

### CREATE PROVIDER[​](#create-provider "Direct link to create-provider")

*   **Applicable container objects: Unity Catalog metastore**

Allows a user to create an OpenSharing [provider](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#provider) object in the [metastore](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#metastore). A provider identifies an organization or group of users that shares data using OpenSharing. Provider objects are created by a user in the [recipient](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#recipient)'s Databricks account. See [What is OpenSharing?](https://docs.databricks.com/aws/en/delta-sharing/).

### CREATE RECIPIENT[​](#create-recipient "Direct link to create-recipient")

*   **Applicable container objects: Unity Catalog metastore**

Allows a user to create an OpenSharing [recipient](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#recipient) object in the [metastore](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#metastore). A recipient identifies an organization or group of users that receives shared data using OpenSharing. Recipient objects are created by a user in the [provider](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#provider)'s Databricks account. See [What is OpenSharing?](https://docs.databricks.com/aws/en/delta-sharing/).

*   **Applicable container objects: Unity Catalog metastore**

Allows a user to create a [share](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#share) in the [metastore](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#metastore). A share is a logical grouping of [tables](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#table) and other assets that a [provider](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#provider) intends to share using OpenSharing.

*   **Applicable container objects: Unity Catalog metastore**

In OpenSharing, `SET SHARE PERMISSION` allows a [provider](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#provider) user to set permissions on a [share](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#share), including granting [recipient](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#recipient) access and transferring ownership. To grant a [recipient](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#recipient) access to a [share](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#share), the user must also have `USE SHARE`, and either `USE RECIPIENT` or ownership of the [recipient](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#recipient) object. To transfer ownership of a [share](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#share), the user must also have `USE SHARE`.

### USE MARKETPLACE ASSETS[​](#use-marketplace-assets "Direct link to use-marketplace-assets")

*   **Applicable container objects: Unity Catalog metastore**

_Enabled by default for all Unity Catalog [metastores](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#metastore)._ In Databricks Marketplace, `USE MARKETPLACE ASSETS` allows a user to get or request access to data products in Marketplace listings. It also allows a user to access the read-only [catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#catalog) that is created when a [provider](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#provider) shares a data product.

Without this privilege, users must have the `CREATE CATALOG` and `USE PROVIDER` privileges, or the metastore admin role. Granting `USE MARKETPLACE ASSETS` instead allows administrators to limit the number of users with those more powerful privileges.

### USE PROVIDER[​](#use-provider "Direct link to use-provider")

*   **Applicable container objects: Unity Catalog metastore**

In OpenSharing, `USE PROVIDER` allows a [recipient](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#recipient) user to view all [providers](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#provider) in the [metastore](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#metastore) and their associated [shares](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#share) (read-only). Combined with `CREATE CATALOG`, `USE PROVIDER` also allows a [recipient](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#recipient) user who is not a metastore admin to mount a [share](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#share) as a [catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#catalog). This allows administrators to limit the number of users with the metastore admin role.

### USE RECIPIENT[​](#use-recipient "Direct link to use-recipient")

*   **Applicable container objects: Unity Catalog metastore**

In OpenSharing, `USE RECIPIENT` allows a [provider](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#provider) user to view all [recipients](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#recipient) in the [metastore](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#metastore) (read-only), including recipient details, authentication status, and the [shares](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#share) the [provider](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#provider) has shared with each [recipient](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#recipient). A [provider](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#provider) user does not need to be a metastore admin to use this privilege.

In [Databricks Marketplace](https://docs.databricks.com/aws/en/marketplace/), `USE RECIPIENT` allows [provider](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#provider) users to view listings and consumer requests in the Provider console.

*   **Applicable container objects: Unity Catalog metastore**

In OpenSharing, `USE SHARE` allows a [provider](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#provider) user to view all [shares](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#share) in the [metastore](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#metastore) (read-only), including the assets ([tables](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#table) and notebooks) in each [share](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#share) and the [share](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#share)'s [recipients](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#recipient). A [provider](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#provider) user does not need to be a metastore admin to use this privilege.

In [Databricks Marketplace](https://docs.databricks.com/aws/en/marketplace/), `USE SHARE` allows [provider](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects#provider) users to view details about the data shared in a listing.
