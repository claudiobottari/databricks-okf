---
title: Managed versus external assets in Unity Catalog | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/managed-versus-external
ingestedAt: "2026-06-18T08:04:38.440Z"
---

Every [securable object](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects) that you register in Unity Catalog is centrally governed. This means that Unity Catalog manages the object's metadata, allowing it to control all aspects of governance including access, auditing, and lineage.

However, for data assets like tables and volumes, Unity Catalog can also control the storage location and lifecycle of the underlying data files in your cloud account, which includes how they are organized, optimized, and when they are deleted. This distinction is what separates **managed** from **external** data assets.

*   **Managed assets**: Unity Catalog controls both governance (access control, auditing, lineage) and the underlying file storage lifecycle (file optimization, how they are organized, and when they are deleted).
*   **External assets**: Unity Catalog controls governance only. The underlying file storage lifecycle is controlled by you or an external system.

When you register a managed asset in Unity Catalog, you retain full ownership of your data. The data files always remain in your cloud account. Unity Catalog determines where within your account they are stored, but does not transfer them to Databricks or own them.

The distinction between managed and external applies to tables and volumes only. Other Unity Catalog securable objects, such as views, models, and functions, do not have managed and external variants.

## Summary of differences[​](#summary-of-differences "Direct link to Summary of differences")

The following table summarizes the differences between managed and external assets in Unity Catalog:

## Uses of the word "manage" across Unity Catalog[​](#uses-of-the-word-manage-across-unity-catalog "Direct link to uses-of-the-word-manage-across-unity-catalog")

The word _manage_ has multiple uses across Unity Catalog. This section summarizes the meaning of _manage_ in different contexts.

When people say that an object is _managed by Unity Catalog_, they typically mean that Unity Catalog governs access to it. This applies to all registered Unity Catalog objects, including external tables and volumes.

The word _managed_ in "managed table" or "managed volume" has a more specific meaning: Unity Catalog determines where in your cloud account the underlying data files are stored, and controls the file lifecycle (optimization, organization, and deletion). This is referred to as the _managed storage location_. Your data remains in your cloud account at all times. Databricks does not own or hold your data.

The word `MANAGE` also appears as a privilege that you can assign to Unity Catalog objects. Generally, `MANAGE` allows a user to assign or revoke privileges on, transfer ownership of, and delete an object without being the owner. See [MANAGE](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/privileges-reference#manage).

The following table summarizes these common uses of _manage_:

## Managed and external tables[​](#managed-and-external-tables "Direct link to managed-and-external-tables")

A **Unity Catalog managed table** is a table where Unity Catalog determines the storage location for the underlying data files. Unity Catalog stores managed tables in the managed storage location defined on the containing schema, catalog, or metastore. When you drop a managed table, Unity Catalog deletes the underlying data files. Managed tables use the Delta or Apache Iceberg format.

An **external table** is a table where you specify the storage location for the underlying data files. When you drop an external table, Unity Catalog removes the table metadata from the metastore, but the underlying data files remain in place. External tables support multiple formats, including Delta, CSV, JSON, Avro, Parquet, and ORC.

For more information about table types, see [Databricks Unity Catalog table types](https://docs.databricks.com/aws/en/tables/types).

Both managed and external tables support read, write, and create access from external engines via open APIs, including the Unity REST API and the Iceberg REST Catalog (IRC). This means that managed tables do not cause vendor lock-in. Any engine that supports these APIs can access managed tables. See [Access Databricks data using external systems](https://docs.databricks.com/aws/en/external-access/).

## Managed and external volumes[​](#managed-and-external-volumes "Direct link to managed-and-external-volumes")

A **Unity Catalog managed volume** is a volume where Unity Catalog determines the storage location. Unity Catalog automatically stores managed volumes in the managed storage location of the containing schema within your cloud account. As with managed tables, you retain full ownership of the underlying data. When you drop a managed volume, Unity Catalog deletes the underlying data files.

An **external volume** is a volume where you specify the storage location. The location must be a path covered by a Unity Catalog external location. When you drop an external volume, Unity Catalog removes the volume definition, but the underlying data files remain in place.

For more information about volumes, see [What are Unity Catalog volumes?](https://docs.databricks.com/aws/en/volumes/).
