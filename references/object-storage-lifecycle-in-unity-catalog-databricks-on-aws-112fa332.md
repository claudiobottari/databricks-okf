---
title: Object storage lifecycle in Unity Catalog | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/object-storage-lifecycle
ingestedAt: "2026-06-18T08:04:48.763Z"
---

When you delete a Unity Catalog [securable object](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects) (via Catalog Explorer, SQL `DROP`, etc.), what happens depends on the object type and storage type. This page describes the data file lifecycle, storage billing, and recovery options after deletion.

## Storage type determines what happens to the data files[​](#storage-type-determines-what-happens-to-the-data-files "Direct link to storage-type-determines-what-happens-to-the-data-files")

For tables and volumes, what happens to the underlying data files depends on whether the asset is managed or external. For more about this distinction, see [Managed versus external assets in Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/managed-versus-external).

*   **Managed tables and volumes**: Unity Catalog controls the storage location and data file lifecycle. Data files live in the managed storage location defined at the metastore, catalog, or schema level. When you delete a managed table or volume, Unity Catalog deletes the underlying data files through a multi-phase lifecycle. Managed storage locations come in two flavors:
    
    *   **Databricks default storage**: Object storage that Databricks provisions and manages in your Databricks account.
    *   **Customer-provided managed storage**: A cloud storage location in your cloud account, configured at the metastore, catalog, or schema level, that Databricks writes and manages data to.
    
    Both flavors share the same data file lifecycle, but billing and post-deletion file retention differ. See [Managed objects on Databricks default storage versus customer-provided storage](#default-storage-vs-customer-storage).
    
*   **External tables and volumes**: You control the storage location and lifecycle. When you delete an external table or volume, Unity Catalog removes the metadata from the metastore, but the data files remain in your cloud storage location.
    
*   **Foreign and federated catalogs**: Data lives in another data source (such as a federated database through Lakehouse Federation, or a Hive metastore through Hive metastore federation). Unity Catalog holds only the connection metadata. When you delete a foreign catalog, Unity Catalog removes the connection metadata. Data in the source system is unaffected.
    

For other securable objects (catalogs, schemas, views, functions, models), deletion removes metadata only — there are no associated data files for Unity Catalog to manage. Dropping a catalog or schema with `CASCADE` removes the contained tables and volumes, each according to its own managed-or-external behavior above.

## Recover a deleted object[​](#recover-a-deleted-object "Direct link to recover-a-deleted-object")

How you recover a deleted object depends on the object type.

warning

Recovery is time-limited and best-effort. Delete an object only after you confirm you no longer need the data. Use the `RESTRICT` option (the default) on `DROP CATALOG` and `DROP SCHEMA` to prevent accidental recursive deletion of non-empty objects.

## Lifecycle of managed data after a delete[​](#lifecycle-of-managed-data-after-a-delete "Direct link to lifecycle-of-managed-data-after-a-delete")

Deleting a managed table or volume does not immediately delete the data files from cloud storage. Data files are retained during a recovery window and permanently deleted afterward.

### Phase 1: Recovery window[​](#phase-1-recovery-window "Direct link to phase-1-recovery-window")

For 7 days after the delete, Unity Catalog retains the soft-deleted data so that you can recover the object. During this window:

*   Use the [UNDROP](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-undrop-table) SQL command to recover tables, materialized views, and streaming tables.
*   Unity Catalog retains the dropped object's metadata, and storage billing continues.

### Phase 2: Purge[​](#phase-2-purge "Direct link to phase-2-purge")

When the 7-day recovery window ends, the object can no longer be recovered. Unity Catalog permanently deletes the data files within 48 hours. For storage billing details in each phase, see [Storage billing after a delete](#billing).

## Managed objects on Databricks default storage versus customer-provided storage[​](#managed-objects-on-databricks-default-storage-versus-customer-provided-storage "Direct link to managed-objects-on-databricks-default-storage-versus-customer-provided-storage")

Managed objects can use two types of managed storage. The data lifecycle and Unity Catalog purge behavior are the same, but billing and post-purge file retention differ.

For more about Databricks default storage, see [Default storage in Databricks](https://docs.databricks.com/aws/en/storage/default-storage). To configure customer-provided managed storage, see [Specify a managed storage location in Unity Catalog](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/managed-storage).

## External tables and volumes[​](#external-tables-and-volumes "Direct link to external-tables-and-volumes")

When you delete an external table or external volume, Unity Catalog removes the metadata from the metastore. The data files in your cloud storage are not deleted. Your cloud provider continues to bill you for the storage according to your bucket's policies.

To remove the files, delete them directly from cloud storage.

## Foreign and federated catalogs[​](#foreign-and-federated-catalogs "Direct link to foreign-and-federated-catalogs")

A foreign catalog contains metadata that references an external data source. When you delete a foreign catalog, Unity Catalog removes the connection metadata. The data in the source system is unaffected. Databricks does not bill you for storage in the source system; the source system's billing applies.

## Storage billing after a delete[​](#storage-billing-after-a-delete "Direct link to storage-billing-after-a-delete")

The following table summarizes how Databricks and your cloud provider bill for storage in each phase. Databricks only bills for storage on Databricks default storage, and only during the recovery window — storage billing stops once the 7-day recovery window passes. For customer-provided managed storage and external storage, your cloud provider bills you directly.

After deleting a managed object on customer-provided storage, you might still see storage charges from your cloud provider. To reduce these charges, check your bucket's object versioning, soft-delete, and lifecycle policies.

## Delete an object from Catalog Explorer[​](#delete-an-object-from-catalog-explorer "Direct link to delete-an-object-from-catalog-explorer")

You can delete Unity Catalog objects from Catalog Explorer in the workspace UI. The data lifecycle described in this article applies whether you delete an object from Catalog Explorer or run a SQL `DROP` statement.

*   Delete a catalog: see [Delete a catalog](https://docs.databricks.com/aws/en/catalogs/manage-catalog#delete).
*   Delete a schema: see [Manage schemas](https://docs.databricks.com/aws/en/schemas/manage-schema).
*   Delete a volume: see [Drop a volume](https://docs.databricks.com/aws/en/volumes/utility-commands#drop-a-volume).

## What happens when you delete a workspace[​](#what-happens-when-you-delete-a-workspace "Direct link to what-happens-when-you-delete-a-workspace")

By default, deleting a workspace does not automatically delete the workspace's default Unity Catalog catalog. If the catalog is retained, its managed tables and volumes remain, and storage billing continues until the catalog is dropped.

The workspace catalog must be dropped manually after workspace deletion. Drop the catalog from another workspace assigned to the same metastore. See [Workspace catalog retention behavior](https://docs.databricks.com/aws/en/admin/workspace/delete-workspace#aws-gcp-retention-behavior).

For details about workspace deletion, see [Delete a workspace](https://docs.databricks.com/aws/en/admin/workspace/delete-workspace).

## Related articles[​](#related-articles "Direct link to related-articles")

*   [Delete a workspace](https://docs.databricks.com/aws/en/admin/workspace/delete-workspace)
*   [Managed versus external assets in Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/managed-versus-external)
*   [Default storage in Databricks](https://docs.databricks.com/aws/en/storage/default-storage)
*   [DROP CATALOG](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-drop-catalog)
*   [DROP SCHEMA](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-drop-schema)
*   [DROP TABLE](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-drop-table)
*   [DROP VOLUME](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-drop-volume)
*   [UNDROP](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-ddl-undrop-table)
