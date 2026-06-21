---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4291637577551dc0860aebb77ded3b9572bab45a72da36d08ef5658a94c21945
  pageDirectory: concepts
  sources:
    - hive-metastore-table-access-control-legacy-databricks-on-aws.md
    - what-is-the-any-file-securable-databricks-on-aws.md
  confidence: 0.8
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - any-file-securable
    - AFS
    - ANY FILE Privilege
    - What is the ANY FILE Securable?
    - What is the `ANY FILE` securable?
  citations:
    - file: what-is-the-any-file-securable-databricks-on-aws.md
title: ANY FILE Securable
description: A special Hive metastore securable object type that controls access to files at arbitrary paths, going beyond standard table-level permissions.
tags:
  - databricks
  - security
  - file-access
  - hive
timestamp: "2026-06-19T19:04:53.819Z"
---

# ANY FILE Securable

The **`ANY FILE` securable** is a legacy access control object in the [Hive Metastore Table Access Control (Legacy)](/concepts/hive-metastore-table-access-control-legacy.md) model that grants entitled principals direct filesystem-level access to data in cloud object storage. Privileges on `ANY FILE` bypass any Hive table ACLs set on database objects such as schemas or tables, but they cannot override [Unity Catalog](/concepts/unity-catalog.md) governance. ^[what-is-the-any-file-securable-databricks-on-aws.md]

## Privileges

You can grant `MODIFY` or `SELECT` privilege on the `ANY FILE` securable to any user, service principal, or group using legacy Hive table access control lists (ACLs). All workspace admins have `MODIFY` privileges on `ANY FILE` by default. Any user with `MODIFY` privileges can grant or revoke those privileges on others. ^[what-is-the-any-file-securable-databricks-on-aws.md]

Privileges on `ANY FILE` are required when using custom data sources or JDBC drivers not covered by [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md). They apply only when using SQL warehouses or clusters with **standard access mode** (formerly shared access mode). ^[what-is-the-any-file-securable-databricks-on-aws.md]

## Interaction with Unity Catalog

On Unity Catalog–enabled standard clusters or SQL warehouses, `ANY FILE` privileges are evaluated **after** all Unity Catalog privileges and serve as a fallback for storage paths and connector libraries not managed by Unity Catalog. Access to any data governed by Unity Catalog using URIs cannot use `ANY FILE` privileges. ^[what-is-the-any-file-securable-databricks-on-aws.md]

Users with `SELECT` on `ANY FILE` can read the following on Unity Catalog–enabled standard clusters:
- Cloud object storage using URIs.
- Data stored in the [DBFS root](/concepts/dbfs-root-location.md) or using DBFS mounts.
- Data sources using custom libraries or drivers.
- JDBC drivers not configured with Lakehouse Federation.
- External data sources not governed by Unity Catalog.
- Streaming data sources, except tables and volumes governed by Unity Catalog and streams that use table names registered to the Hive [Metastore](/concepts/metastore.md). ^[what-is-the-any-file-securable-databricks-on-aws.md]

Unity Catalog volumes and tables provide full governance without requiring `ANY FILE` privileges. Databricks recommends [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md) for read-only access to supported external data sources, which never requires `ANY FILE` privileges. ^[what-is-the-any-file-securable-databricks-on-aws.md]

## Concerns

Privileges on the `ANY FILE` securable effectively bypass legacy Hive table ACLs. Grant them with discretion if you still rely on those ACLs for data access before migrating fully to Unity Catalog. `ANY FILE` never bypasses Unity Catalog governance, but users with that privilege gain expanded ability to configure and access data sources outside Unity Catalog. ^[what-is-the-any-file-securable-databricks-on-aws.md]

## Limitations

`ANY FILE` is a legacy securable that is **not reported** in the information schema. ^[what-is-the-any-file-securable-databricks-on-aws.md]

## Related Concepts

- [Hive Metastore Table Access Control (Legacy)](/concepts/hive-metastore-table-access-control-legacy.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Lakehouse Federation](/concepts/lakehouse-federation-data-sharing.md)
- [DBFS root](/concepts/dbfs-root-location.md)
- [Storage credentials (legacy)](/concepts/storage-credential-iam-role-for-unity-catalog.md)

## Sources

- hive-metastore-table-access-control-legacy-databricks-on-aws.md
- what-is-the-any-file-securable-databricks-on-aws.md

# Citations

1. [what-is-the-any-file-securable-databricks-on-aws.md](/references/what-is-the-any-file-securable-databricks-on-aws-2b8e33ad.md)
