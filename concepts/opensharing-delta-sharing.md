---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eedc2de752b2bd6263a87cda004ed49108b755c2a00c5b65247c3a6a82d8900d
  pageDirectory: concepts
  sources:
    - delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
    - read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md
    - set-up-opensharing-for-your-account-for-providers-databricks-on-aws.md
    - what-is-the-opensharing-databricks-to-databricks-protocol-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - opensharing-delta-sharing
    - O(S
    - Open Sharing (Delta Sharing)
    - Monitoring Data Sharing
  citations:
    - file: what-is-the-opensharing-databricks-to-databricks-protocol-databricks-on-aws.md
    - file: set-up-opensharing-for-your-account-for-providers-databricks-on-aws.md
    - file: read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md
    - file: delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
title: OpenSharing (Delta Sharing)
description: An open protocol for sharing datasets across platforms; objects shared via OpenSharing cannot be dropped — only altered — to prevent breaking downstream consumers.
tags:
  - databricks
  - delta-sharing
  - data-sharing
timestamp: "2026-06-19T18:26:45.293Z"
---

# OpenSharing (Delta Sharing)

**OpenSharing** (formerly known as Delta Sharing) is an open protocol developed by Databricks for secure data sharing across organizations, regardless of the computing platforms those organizations use. It enables providers to share live data and AI assets with recipients both inside and outside their Databricks environment without data replication. The protocol is available as an [open-source project](https://opensharing.io/). ^[what-is-the-opensharing-databricks-to-databricks-protocol-databricks-on-aws.md]

OpenSharing is built on [Unity Catalog](/concepts/unity-catalog.md) and can be used with Databricks Marketplace and [Clean Rooms](/concepts/databricks-clean-rooms.md). A provider must have at least one Unity Catalog-enabled workspace to manage shares and recipients using the built-in OpenSharing server. ^[set-up-opensharing-for-your-account-for-providers-databricks-on-aws.md]

## Sharing Protocols

OpenSharing supports three primary sharing approaches: ^[what-is-the-opensharing-databricks-to-databricks-protocol-databricks-on-aws.md]

- **Databricks-to-Databricks sharing** – Data is shared from a provider’s Unity Catalog-enabled workspace to a recipient’s Unity Catalog-enabled Databricks workspace. This protocol supports notebook sharing, Unity Catalog governance, auditing, and usage tracking. The recipient’s *sharing identifier* (a string in the format `<cloud>:<region>:<uuid>`) is used to establish the secure connection. ^[what-is-the-opensharing-databricks-to-databricks-protocol-databricks-on-aws.md]
- **Databricks-to-Open sharing** – Data managed in a Unity Catalog-enabled workspace is shared with users on any computing platform using bearer tokens or Open ID Connect (OIDC) federation. ^[what-is-the-opensharing-databricks-to-databricks-protocol-databricks-on-aws.md]
- **Customer-managed OpenSharing server** – Organizations deploy the open-source server to share from any platform to any platform, regardless of Databricks. ^[what-is-the-opensharing-databricks-to-databricks-protocol-databricks-on-aws.md]

## Provider Setup

To enable OpenSharing on a Databricks account, a [Metastore](/concepts/metastore.md) admin must complete the following steps: ^[set-up-opensharing-for-your-account-for-providers-databricks-on-aws.md]

1. Enable OpenSharing on a Unity Catalog [Metastore](/concepts/metastore.md) in the account console by checking **Allow OpenSharing with parties outside your organization**.
2. Configure a default recipient token lifetime (maximum one year).
3. (Optional) Install the Unity Catalog CLI to manage shares and recipients.
4. Grant privileges such as `CREATE SHARE`, `CREATE RECIPIENT`, `USE SHARE`, and `USE RECIPIENT` to delegate management tasks.
5. Configure the time-to-live (TTL) of data materialization (default 8 hours) for dynamic views, materialized views, streaming tables, and foreign tables.
6. Allow network access to storage by adding recipient networks to the cloud storage allowlist, or use [SecureConnect](https://docs.databricks.com/aws/en/delta-sharing/secureconnect-provider) for managed proxy access.

[Metastore](/concepts/metastore.md) admins can also transfer ownership of shares and recipients. Share owners can add tables and volumes to shares as long as they have `SELECT` access to tables and `READ VOLUME` access to volumes. ^[set-up-opensharing-for-your-account-for-providers-databricks-on-aws.md]

## Data Recipients and Shares

A *share* is a named collection of tables, views, volumes, and notebooks. A *recipient* is an object that represents an organization and is associated with a sharing identifier or credentials. The provider grants the recipient access to a share. Recipients can then create a catalog from the share in their Unity Catalog workspace to access the data. ^[what-is-the-opensharing-databricks-to-databricks-protocol-databricks-on-aws.md]

Shared notebooks live at the catalog level. Users with `USE CATALOG` privilege can access them. Permissions on shared catalogs work like any other Unity Catalog object, with read-only access. ^[what-is-the-opensharing-databricks-to-databricks-protocol-databricks-on-aws.md]

## Reading Shared Data with Apache Spark

Recipients can query shared tables using Apache Spark DataFrames with the `deltasharing` format keyword: ^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]

```python
df = (spark.read
  .format("deltasharing")
  .load("<profile-path>#<share-name>.<schema-name>.<table-name>"))
```

If history sharing is enabled on the source table, recipients can read change data feed (CDF) records and use Structured Streaming. History sharing requires Databricks Runtime 12.2 LTS or above. ^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]

Example with CDF and batch reading:

```python
df = (spark.read
  .format("deltasharing")
  .option("readChangeFeed", "true")
  .option("startingTimestamp", "2021-04-21 05:45:46")
  .option("endingTimestamp", "2021-05-21 12:00:00")
  .load("<profile-path>#<share-name>.<schema-name>.<table-name>"))
```

Recipients can also query shared tables using SQL syntax such as `SELECT * FROM shared_table_name` when the share is registered as a catalog. ^[read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md]

## History Sharing

Databricks-to-Databricks table shares can enable *history sharing* to improve read performance. When history sharing is enabled, Databricks uses temporary cloud storage credentials scoped to the provider’s Delta table root directory, providing performance close to direct table access. ^[what-is-the-opensharing-databricks-to-databricks-protocol-databricks-on-aws.md]

- For new table shares, the provider specifies `WITH HISTORY` when adding the table. When sharing with Databricks Runtime 16.2+, history is the default.
- For existing shares, the provider alters the share to enable history.
- Sharing an entire schema includes all tables with history by default.

Cloud token eligibility requirements and data privacy considerations apply. ^[what-is-the-opensharing-databricks-to-databricks-protocol-databricks-on-aws.md]

## Error Conditions

A common error when trying to delete a Unity Catalog securable (table, view, or volume) that is part of an active OpenSharing share is `DELTA_SHARING_SECURABLE_DELETE_BLOCKED`. The error message indicates the securable cannot be deleted because it is being shared via OpenSharing, and lists the share names or clean room IDs. The resolution is to use `ALTER VIEW` or remove the securable from the share before deletion. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

The SQLSTATE for this error is 55006. Sub-conditions include `BY_CLEAN_ROOMS`, `NO_HINT`, and combinations. ^[delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md]

## Sources

- delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md
- read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md
- set-up-opensharing-for-your-account-for-providers-databricks-on-aws.md
- what-is-the-opensharing-databricks-to-databricks-protocol-databricks-on-aws.md

# Citations

1. [what-is-the-opensharing-databricks-to-databricks-protocol-databricks-on-aws.md](/references/what-is-the-opensharing-databricks-to-databricks-protocol-databricks-on-aws-53f3616c.md)
2. [set-up-opensharing-for-your-account-for-providers-databricks-on-aws.md](/references/set-up-opensharing-for-your-account-for-providers-databricks-on-aws-4b18295d.md)
3. [read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws.md](/references/read-opensharing-shared-tables-using-apache-spark-dataframes-databricks-on-aws-a44c61ff.md)
4. [delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws.md](/references/delta_sharing_securable_delete_blocked-error-condition-databricks-on-aws-0eeb76c6.md)
