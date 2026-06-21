---
title: Unity Catalog best practices | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/best-practices
ingestedAt: "2026-06-18T08:03:54.886Z"
---

This document provides recommendations for using Unity Catalog to meet your data governance needs most effectively. For an introduction to data governance on Databricks, see [Data governance with Databricks](https://docs.databricks.com/aws/en/data-governance/). For an introduction to Unity Catalog, see [What is Unity Catalog?](https://docs.databricks.com/aws/en/data-governance/unity-catalog/).

## Identities[​](#identities "Direct link to identities")

Principals (users, groups, and service principals) must be defined at the Databricks account level in order to be assigned privileges on Unity Catalog securable objects. Databricks recommends that you use SCIM to provision principals to your Databricks account from your IdP.

Best practices:

*   Avoid (and turn off existing) workspace-level SCIM provisioning. Provisioning principals directly to a workspace should be reserved for legacy workspaces that are not enabled for Unity Catalog. You should manage provisioning entirely at the account level.
    
*   Define and manage groups in your IdP. They should be consistent with your organizational group definitions.
    
    Groups behave differently than users and service principals. Although users and service principals that you add to a workspace are automatically synchronized with your Databricksaccount, workspace-level groups are not. If you have workspace-local groups, you should manually migrate them to the account, preferably by replicating them in your IdP (if necessary) and provisioning them to the account.
    
*   Set up groups so that you can use them effectively to grant access to data and other Unity Catalog securables. Avoid direct grants to users whenever possible.
    
*   Use groups to assign ownership to most securable objects.
    
*   Avoid adding users manually, either to the account or the workspace. Avoid modifying groups in Databricks: use your IdP.
    
*   Use service principals to run jobs. Service principals enable job automation. If you use users to run jobs that write into production, you risk overwriting production data by accident.
    

For more information, see [Manage users, service principals, and groups](https://docs.databricks.com/aws/en/admin/users-groups/) and [Sync users and groups from your identity provider using SCIM](https://docs.databricks.com/aws/en/admin/users-groups/scim/).

## Admin roles and powerful privileges[​](#admin-roles-and-powerful-privileges "Direct link to admin-roles-and-powerful-privileges")

Assigning admin roles and powerful privileges like `ALL PRIVILEGES` and `MANAGE` requires care:

*   Understand the privileges of account admins, workspace admins, and metastore admins before you assign them. See [Admin privileges in Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/admin-privileges).
*   Assign these roles to groups whenever possible.
*   Metastore admins are optional. Assign them only if you need them. For guidance, see [Metastore admins](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/admin-privileges#metastore-admins).
*   Assign object ownership to groups, especially if objects are used in production. The creator of any object is its first owner. Creators should reassign ownership to appropriate groups.
*   Only metastore admins, owners, and users with the `MANAGE` privilege on an object can grant privileges on that object. Owners of parent catalogs and schemas also have the ability to grant privileges on all objects in the catalog or schema. Be sparing in your assignment of ownership and the `MANAGE` privilege.
*   Be sparing in your assignment of `ALL PRIVILEGES`, which includes all privileges except `MANAGE`, `EXTERNAL USE LOCATION`, and `EXTERNAL USE SCHEMA`.

## Privilege assignment[​](#privilege-assignment "Direct link to privilege-assignment")

Securable objects in Unity Catalog are hierarchical, and privileges are inherited downward. Use this inheritance hierarchy to develop an effective privilege model.

Best practices:

*   Understand the role of the `USE CATALOG` and `USE SCHEMA` privileges:
    
    *   `USE CATALOG | SCHEMA` grants the ability to view data in the catalog or schema. Alone, these privileges do not grant `SELECT` or `READ` on the objects inside the catalog or schema, but they are a prerequisite to granting users that access. Grant these privileges only to users who should be able to view data in the catalog or schema.
    *   `USE CATALOG | SCHEMA`, by restricting access to a catalog or schema, prevents object owners (for example, a table creator) from inadvertently assigning access to that object (table) to users who shouldn't have access. It is typical to create a schema per team and grant `USE SCHEMA` and `CREATE TABLE` only to that team (along with `USE CATALOG` on the parent catalog).
*   Understand the role of the `BROWSE` privilege:
    
    *   `BROWSE` allows users to view metadata for objects in a catalog using Catalog Explorer, the schema browser, search, the lineage graph, `information_schema`, and the REST API. It does not grant access to data.
    *   `BROWSE` enables users to discover data and request access to it, even if they do not have the `USE CATALOG` or `USE SCHEMA` privileges.
    *   Databricks recommends granting `BROWSE` on catalogs to the `All account users` group at the catalog level to make data discoverable and support access requests.
*   Configure access request destinations to support self-service access:
    
    *   When access request destinations are not configured, users cannot request access to objects, even if they can discover them.
    *   Databricks recommends enabling default email destinations so requests are automatically sent to the catalog owner or object owner when no other destination is configured.
    *   Destination can be configured to email addresses, Slack, Microsoft Teams, PagerDuty, webhooks, or a redirect URL to your organization's request system.
*   Understand the difference between object ownership and the `MANAGE` privilege:
    
    *   An object's owner has all privileges on the object, such as `SELECT` and `MODIFY` on a table, as well as permission to grant privileges on the securable object to other principals and to transfer ownership to other principals.
    *   Owners can grant the `MANAGE` privilege to delegate ownership abilities on an object to other principals.
    *   Catalog and schema owners can transfer ownership of any object in the catalog or schema.
    *   It is best to configure ownership or grant the `MANAGE` privilege on all objects to a group that is responsible for administration of grants on the object.
*   Use group ownership to enable collaborative editing of views and metric views:
    
    *   By default, only the owner of a view or metric view can edit its definition. This prevents privilege escalation where an editor could modify the view to access unauthorized data.
    *   To enable multiple users to safely edit the same view or metric view, transfer ownership to a group and grant that group access to the source tables. All group members can then edit the definition, and data access is limited to what the group has permission to see.
    *   For detailed guidance, see [Enable collaborative editing](https://docs.databricks.com/aws/en/business-semantics/metric-views/manage#enable-collaborative-editing).
*   Reserve direct `MODIFY` access to production tables for service principals.
    

For more information, see [Manage privileges in Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/).

The following are rules and best practices for creating and managing metastores:

*   You can have only one metastore per region. All workspaces in that region share that metastore. To share data between regions, see [Cross-region and cross-platform sharing](#x-region).
    
*   Metastores provide regional isolation but are not intended as default units of data isolation. Data isolation typically begins at the catalog level. However, if you prefer a more centralized governance model, you can create metastore-level managed storage. For recommendations, see [Managed storage](#storage).
    
*   The metastore admin role is optional. For recommendations about whether to assign an optional metastore admin, see [Admin roles and powerful privileges](#admin).
    

important

Do not register frequently accessed tables as external tables in more than one metastore. If you do, changes to the schema, table properties, comments, and other metadata that occur as a result of writes to metastore A will not register at all with metastore B. You can also cause consistency issues with the Databricks commit service.

## Catalogs and schemas[​](#catalogs-and-schemas "Direct link to catalogs-and-schemas")

Catalogs are the primary unit of data isolation in the typical Unity Catalog data governance model. Schemas add an additional layer of organization.

Best practices for catalog and schema usage:

*   Organize data and AI objects into catalogs and schemas that reflect organizational divisions and projects. Often, this means that catalogs correspond to an environment scope, team, business unit, or some combination of these. This makes it easier to use the privilege hierarchy to manage access effectively.
*   When work environments and data both have the same isolation requirements, you can bind a catalog to a specific workspace. When that is required, create catalogs that can be scoped to a limited set of workspaces.
*   Always assign ownership of production catalogs and schemas to groups, not individual users.
*   Grant `USE CATALOG` and `USE SCHEMA` only to users who should be able to see or query the data contained in them.

For more advice about granting privileges on catalogs and schemas, see [Privilege assignment](#privileges).

## Managed storage[​](#managed-storage "Direct link to managed-storage")

Managed tables and volumes, objects whose lifecycle is fully managed by Unity Catalog, are stored in default storage locations, known as _managed storage_. You can set up managed storage at the metastore, catalog, or schema level. Data is stored at the lowest available location in the hierarchy. For details, see [Specify a managed storage location in Unity Catalog](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/managed-storage).

Best practices for managed storage locations:

*   Give preference to catalog-level storage as your primary unit of data isolation.
    
    Metastore-level storage was required in early Unity Catalog environments but is no longer required.
    
*   If you choose to create a metastore-level managed location, use a dedicated bucket.
    
*   Do not use a bucket that can be accessed from outside of Unity Catalog.
    
    If an external service or principal accesses data in the managed storage location, bypassing Unity Catalog, access control and auditability on managed tables and volumes are compromised.
    
*   Do not reuse a bucket that is or was used for your [DBFS root file system](https://docs.databricks.com/aws/en/dbfs/).
    

## Managed and external tables[​](#managed-and-external-tables "Direct link to managed-and-external-tables")

_Managed tables_ are fully managed by Unity Catalog, which means that Unity Catalog manages both the governance and the underlying data files for each managed table. They are always in Delta or Apache Iceberg format.

_External tables_ are tables whose access from Databricks is managed by Unity Catalog, but whose data lifecycle and file layout are managed using your cloud provider and other data platforms. When you create an external table in Databricks, you specify its location, which must be on a path that is defined in a Unity Catalog _external location_.

Use managed tables:

*   For most use cases. Databricks recommends managed tables and volumes because they allow you to take full advantage of Unity Catalog governance capabilities and performance optimizations, including:
    
    *   Auto compaction
    *   Auto optimize
    *   Faster metadata reads (metadata caching)
    *   Intelligent file size optimizations
    
    New Databricks functionality gives precedence to managed tables.
    
*   For all new tables.
    

Use external tables:

*   When you're already using them and you are upgrading from Hive metastore to Unity Catalog.
    
    *   Using external tables can provide a quick and seamless “one-click” upgrade without moving data.
    *   Databricks recommends that you eventually migrate external tables to managed tables.
*   If you have disaster recovery requirements for this data that cannot be met by managed tables.
    
    Managed tables cannot be registered across multiple metastores in the same cloud.
    
*   If external readers or writers must be able to interact with the data from outside of Databricks.
    
    Typically, you should avoid letting external access even to the external tables that are registered in Unity Catalog. Doing so bypasses Unity Catalog access control, auditing, and lineage. It is a better practice to use managed tables and share data across regions or cloud providers using OpenSharing. If you must allow external access to external tables, limit it to reads, with all writes happening through Databricks and Unity Catalog.
    

*   You must support non-Delta or non-Iceberg tables, such as Parquet, Avro, ORC, and so forth.

More recommendations for using external tables:

*   Databricks recommends that you create external tables using one external location per schema.
*   Databricks strongly recommends against registering a table as an external table in more than one metastore due to the risk of consistency issues. For example, a change to the schema in one metastore will not register in the second metastore. Use OpenSharing for sharing data between metastores. See [Cross-region and cross-platform sharing](#x-region).

See also [Databricks tables](https://docs.databricks.com/aws/en/tables/).

## Managed and external volumes[​](#-managed-and-external-volumes "Direct link to -managed-and-external-volumes")

_Managed volumes_ are fully managed by Unity Catalog, which means that Unity Catalog manages access to the volume's storage location in your cloud provider account. _External volumes_ represent existing data in storage locations that are managed outside of Databricks, but registered in Unity Catalog to control and audit access from within Databricks. When you create an external volume in Databricks, you specify its location, which must be on a path that is defined in a Unity Catalog _external location_.

Use managed volumes:

*   For most use cases, to take full advantage of Unity Catalog governance capabilities.
*   If you want to create tables starting from files in a volume without running `COPY INTO` or CTAS (`CREATE TABLE AS`) statements.

Use external volumes:

*   To register landing areas for raw data produced by external systems to support its processing in the early stages of ETL pipelines and other data engineering activities.
*   To register staging locations for ingestion, for example, using Auto Loader, `COPY INTO`, or CTAS statements.
*   Provide file storage locations for data scientists, data analysts, and machine learning engineers to use as parts of their exploratory data analysis and other data science tasks, when managed volumes are not an option.
*   To give Databricks users access to arbitrary files produced and deposited in cloud storage by other systems, for example, large collections of unstructured data (such as image, audio, video, and PDF files) captured by surveillance systems or IoT devices, or library files (JARs and Python wheel files) exported from local dependency management systems or CI/CD pipelines.
*   To store operational data, for example, logging or checkpointing files, when managed volumes are not an option.

More recommendations for using external volumes:

*   Databricks recommends that you create external volumes from one external location within one schema.

tip

For ingestion use cases in which the data is copied to another location (for example, using Auto Loader or `COPY INTO`) use external volumes. Use external tables when you want to query data in place as a table, with no copy involved.

See also [Managed versus external volumes](https://docs.databricks.com/aws/en/volumes/#diff) and [External locations](#external-loc).

## External locations[​](#-external-locations "Direct link to -external-locations")

External location securable objects, by combining storage credentials and storage paths, provide strong control and auditability of storage access. It is important to prevent users from accessing the buckets registered as external locations directly, bypassing the access control provided by Unity Catalog.

To use external locations effectively:

*   Ensure that you limit the number of users with direct access to any bucket that is being used as an external location.
    
*   Do not mount storage accounts to DBFS if they are also being used as external locations. Databricks recommends that you migrate mounts on cloud storage locations to external locations in Unity Catalog using [Catalog Explorer](https://docs.databricks.com/aws/en/catalog-explorer/).
    
*   Grant the ability to create external locations only to administrators who are tasked with setting up connections between Unity Catalog and cloud storage, or to trusted data engineers.
    
    External locations provide access from within Unity Catalog to a broadly encompassing location in cloud storage, for example, an entire bucket or container (s3://mycompany-hr-prod) or a broad subpath (s3://mycompany-hr-prod/unity-catalog). The intention is that a cloud administrator can be involved in setting up a few external locations and then delegate the responsibility of managing those locations to a Databricks administrator in your organization. The Databricks administrator can then further organize the external location into areas with more granular permissions by registering external volumes or external tables at specific prefixes under the external location.
    
    Because external locations are so encompassing, Databricks recommends giving the `CREATE EXTERNAL LOCATION` permission only to an administrator who is tasked with setting up connections between Unity Catalog and cloud storage, or to trusted data engineers. To provide other users with more granular access, Databricks recommends registering external tables or volumes on top of external locations and granting users access to data using volumes or tables. Since tables and volumes are children of a catalog and schema, catalog or schema administrators have the ultimate control over access permissions.
    
    You can also control access to an external location by binding it to specific workspaces. See [Assign an external location to specific workspaces](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/manage-external-locations#workspace-binding).
    
*   Don't grant general `READ FILES` or `WRITE FILES` permissions on external locations to end users.
    
    Users shouldn't use external locations for anything but creating tables, volumes, or managed locations. They should not use external locations for path-based access for data science or other non-tabular data use cases.
    
    For path-based access to non-tabular data, use volumes. Cloud URI access to data under the volume path is governed by the privileges granted on the volume, not the privileges granted on the external location where the volume is stored.
    
    Volumes let you work with files using SQL commands, dbutils, Spark APIs, REST APIs, Terraform, and a user interface for browsing, uploading, and downloading files. Moreover, volumes offer a FUSE mount that is accessible on the local file system under `/Volumes/<catalog_name>/<schema_name>/<volume_name>/`. The FUSE mount allows data scientists and ML engineers to access files as if they were in a local filesystem, as required by many machine learning or operating system libraries.
    
    If you must grant direct access to files in an external location (for exploring files in cloud storage before a user creates an external table or volume, for example), you can grant `READ FILES`. Use cases for granting `WRITE FILES` are rare.
    
*   Avoid path overlap conflicts: never create external volumes or tables at the root of an external location.
    
    If you do create external volumes or tables at the external location root, you can't create any additional external volumes or tables on the external location. Instead, create external volumes or tables on a sub-directory inside the external location.
    
    If you encounter storage conflicts between external locations and workspace default Unity Catalog storage, see [Resolve storage path conflicts](https://docs.databricks.com/aws/en/data-governance/unity-catalog/storage-conflicts).
    
*   Enable [file events](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/manage-external-locations#file-events) for optimal file processing performance.
    
    When file events are enabled for an external location, Databricks tracks ingestion metadata by processing change notifications from cloud providers. This improves the performance and reliability of downstream features, such as [file arrival triggers](https://docs.databricks.com/aws/en/jobs/file-arrival-triggers) and [Auto Loader](https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/auto-loader/).
    

You should use external locations only to do the following:

*   Register external tables and volumes using the `CREATE EXTERNAL VOLUME` or `CREATE TABLE` commands.
*   Register a location as managed storage. The `CREATE MANAGED STORAGE` privilege is a precondition.
*   Explore existing files in cloud storage before you create an external table or volume at a specific prefix. The `READ FILES` privilege is a precondition. Assign this privilege sparingly. See the recommendation in the previous list for details.

### External locations vs. external volumes[​](#external-locations-vs-external-volumes "Direct link to external-locations-vs-external-volumes")

Before volumes were released, some Unity Catalog implementations assigned `READ FILES` access directly to external locations for data exploration. With the availability of volumes that register files in any format, including structured, semi-structured, and unstructured data, there is no real reason to use external locations for anything but creating tables, volumes, or managed locations. For detailed information about when to use external locations and when to use volumes, see [Managed and external volumes](#managed-external-volumes) and [External locations](#external-loc).

## Cross-region and cross-platform sharing[​](#cross-region-and-cross-platform-sharing "Direct link to cross-region-and-cross-platform-sharing")

You can have only one metastore per region. If you want to share data between workspaces on different regions, use Databricks-to-Databricks [OpenSharing](https://docs.databricks.com/aws/en/delta-sharing/).

Best practices:

*   Use your single-region metastore for all software development lifecycle scopes and business units, for example, dev, test, prod, sales, and marketing. Ensure that the workspaces that require frequent shared data access are located in the same region.
*   Use Databricks-to-Databricks OpenSharing between cloud regions or cloud providers.
*   Use OpenSharing for tables that are infrequently accessed, because you are responsible for egress charges from cloud region to cloud region. If you must share frequently accessed data across regions or cloud providers, see: [Monitor and manage OpenSharing egress costs (for providers)](https://docs.databricks.com/aws/en/delta-sharing/manage-egress).

Be aware of the following limitations when you use Databricks-to-Databricks sharing:

*   Lineage graphs are created at the metastore level, and do not cross region or platform boundaries. This applies even if a resource is shared across metastores within the same Databricks account: lineage information from the source is not be visible in the destination, and vice versa.
*   Access control is defined at the metastore level, and does not cross region or platform boundaries. If a resource has privileges assigned to it and that resource is shared to another metastore in the account, the privileges on that resource do not apply to the destination share. You must grant privileges on the destination share in the destination.

## Compute configurations[​](#compute-configurations "Direct link to compute-configurations")

Databricks recommends using compute policies to limit the ability to configure clusters based on a set of rules. Compute policies let you limit users to creating Unity Catalog\-enabled clusters, specifically clusters that use standard access mode (formerly shared access mode) or dedicated access mode (formerly single-user or assigned access mode).

Only clusters that use one of these access modes can access data in Unity Catalog. All serverless compute and DBSQL compute support Unity Catalog.

Databricks recommends standard access mode for all workloads. Use dedicated access mode only if your required functionality is not supported by standard access mode. See [Access modes](https://docs.databricks.com/aws/en/compute/configure#access-mode).
