---
title: What is the ANY FILE securable? | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/table-acls/any-file
ingestedAt: "2026-06-18T08:03:47.335Z"
---

Privileges on the `ANY FILE` securable grant the entitled principal direct access to the filesystem and data in cloud object storage, regardless of any Hive table ACLs set on database objects like schemas or tables.

## Privileges for `ANY FILE`[​](#privileges-for-any-file "Direct link to privileges-for-any-file")

You can grant `MODIFY` or `SELECT` privilege on the `ANY FILE` securable to any service principal, user, or group using legacy Hive table access control lists (ACLs). All workspace admins have `MODIFY` privileges on `ANY FILE` by default. Any user with `MODIFY` privileges can grant or revoke privileges on `ANY FILE`.

You must have privileges on the `ANY FILE` securable when using custom data sources or JDBC drivers not included in Lakehouse Federation. See [Connect to external databases and catalogs](https://docs.databricks.com/aws/en/query-federation/).

Privileges on the `ANY FILE` securable cannot override Unity Catalog privileges and do not grant or expand privileges on data objects governed by Unity Catalog. Some drivers and custom-installed libraries might compromise user isolation by storing data of all users in one common temp directory.

Privileges on the `ANY FILE` securable apply only when you use SQL warehouses or clusters with standard access mode (formerly shared access mode).

`ANY FILE` respects legacy access patterns for data in cloud object storage, including mounts and storage credentials defined at the compute level. See [Configure access to cloud object storage for Databricks using legacy patterns](https://docs.databricks.com/aws/en/archive/storage/connect-storage-index).

## How does `ANY FILE` interact with Unity Catalog?[​](#how-does-any-file-interact-with-unity-catalog "Direct link to how-does-any-file-interact-with-unity-catalog")

When using Unity Catalog\-enabled standard clusters or SQL warehouses, privileges on the `ANY FILE` securable are evaluated when accessing storage paths or data sources that are _not governed_ by Unity Catalog. Privileges on the `ANY FILE` securable are evaluated after all Unity Catalog\-related privileges and serve as a fallback for storage paths and connector libraries not managed with Unity Catalog.

Databricks recommends using Lakehouse Federation for configuring read-only access to supported external data sources. Lakehouse Federation never requires privileges on the `ANY FILE` securable. See [Connect to external databases and catalogs](https://docs.databricks.com/aws/en/query-federation/).

Unity Catalog volumes and tables provide full governance for tabular and nontabular data and do not require privileges on the `ANY FILE` securable.

Access to any data governed by Unity Catalog using URIs cannot use privileges on the `ANY FILE` securable. See [Connect to cloud object storage using Unity Catalog](https://docs.databricks.com/aws/en/connect/unity-catalog/cloud-storage/).

You must have `SELECT` privileges on the `ANY FILE` securable to read using the following patterns on Unity Catalog\-enabled standard clusters:

*   Cloud object storage using URIs.
*   Data stored in the DBFS root or using DBFS mounts.
*   Data sources using custom libraries or drivers.
*   JDBC drivers not configured with Lakehouse Federation.
*   External data sources that are not governed by Unity Catalog.
*   Streaming data sources, except tables and volumes governed by Unity Catalog and streams that use table names registered to the Hive metastore.

## Concerns about `ANY FILE` securable privileges[​](#concerns-about-any-file-securable-privileges "Direct link to concerns-about-any-file-securable-privileges")

Privileges on the `ANY FILE` securable essentially bypass legacy Hive table ACLs set on database objects. Use discretion when you grant privileges on the `ANY FILE` securable, if you have not fully migrated all tables to Unity Catalog and you still rely on legacy Hive table ACLs for managing access to data.

Privileges granted on the `ANY FILE` securable never bypass Unity Catalog data governance. However, users that have privileges on the `ANY FILE` securable have expanded ability to configure and access data sources not governed by Unity Catalog.

## Limitations for `ANY FILE`[​](#limitations-for-any-file "Direct link to limitations-for-any-file")

`ANY FILE` is a legacy securable that is not reported in the information schema.
