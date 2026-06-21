---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 89b2b903dc8ba0585f3fad31b2c0a91d0ad6b8b93416e8d96c4452a761c3683f
  pageDirectory: concepts
  sources:
    - access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-to-open-sharing-model
    - DSM
  citations:
    - file: access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
    - file: read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md
title: Databricks-to-Open Sharing Model
description: A sharing model where recipients can use any tool (including Databricks) to access shared data via an activation URL or portal link to download a credential file or URL.
tags:
  - data-sharing
  - cross-platform
  - databricks
timestamp: "2026-06-19T13:51:38.795Z"
---

```yaml
---
title: Databricks-to-Open sharing model
summary: A sharing model where recipients can use any tool (including Databricks) to access shared data via an activation URL or portal link to download a credential file or URL.
sources:
  - access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
  - read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:38:16.834Z"
updatedAt: "2026-06-19T08:51:08.296Z"
tags:
  - data-sharing
  - open-sharing
  - credentials
aliases:
  - databricks-to-open-sharing-model
  - DSM
confidence: 0.95
provenanceState: merged
inferredParagraphs: 2
---

# Databricks-to-Open Sharing Model

The **Databricks-to-Open sharing model** is one of two OpenSharing protocols for secure data sharing between a Databricks data provider and an external data recipient. In this model, recipients can use any tool — including Databricks, Apache Spark, pandas, Power BI, Tableau, and Iceberg clients — to access shared data without requiring a Databricks workspace enabled for Unity Catalog. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Overview

OpenSharing is an open standard for secure data sharing between organizations. A Databricks user acts as a *data provider*, sharing data with a person or group outside their organization called a *data recipient*. The Databricks-to-Open sharing model is designed for recipients who are not Databricks users or who choose to use tools other than Databricks. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

This model contrasts with the [[Databricks-to-Databricks sharing model]], which requires both parties to have Databricks workspaces enabled for Unity Catalog and uses a secure sharing connection without credential files. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## How Access Works

### Credential-Based Access

In the Databricks-to-Open sharing model, the data provider creates a *recipient* in their Databricks account and a *share* (a representation of the tables, volumes, and views to be shared). The provider then sends the recipient an activation URL or portal link over a secure channel. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

The recipient follows the activation link to download a **credential file** that authenticates them to the provider's account. This file can only be downloaded once; after download, the activation link's download button is disabled. If the link is lost before use, the recipient must contact the provider for a new one. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

Both bearer tokens and OAuth Client Credentials are supported for authentication in this model. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

### OIDC Federation Access

Alternatively, if the data provider uses OpenID Connect (OIDC) federation, the recipient receives a URL rather than a credential file. This enables user-to-machine (U2M) flows for Tableau and Power BI, and machine-to-machine (M2M) flows for Python client applications. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Reading Shared Data

### Using Databricks (Unity Catalog Workspaces)

If the recipient has a Databricks workspace enabled for Unity Catalog, they can use the **Import provider UI** in Catalog Explorer to import the credential file without needing to store or specify it manually. This allows them to: ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

- Create catalogs from shares with a single click.
- Use [[Unity Catalog Privilege Management|Unity Catalog Privileges]] to grant access to shared tables.
- Query shared data using standard Unity Catalog syntax.
- Apply rotated credentials without recreating the catalog.

The process requires a [[metastore|Metastore]] admin or a user with both `CREATE PROVIDER` and `USE PROVIDER` privileges. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

### Using Apache Spark

For Spark 3.x and above, recipients install the `delta-sharing` Python connector and the Apache Spark connector. They then list available tables and load data using the credential file path: ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

```python
import delta_sharing
client = delta_sharing.SharingClient("<profile-path>/config.share")
client.list_all_tables()
```

Recipients can also access change data feeds (CDF), perform batch and streaming queries, and read tables with deletion vectors or column mapping enabled (with appropriate connector versions). ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

### Using pandas

The same `delta-sharing` Python connector supports pandas. Recipients load data with: ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

```python
import delta_sharing
delta_sharing.load_as_pandas("<profile-path>#<share-name>.<schema-name>.<table-name>")
```

CDF queries are also supported with optional version or timestamp parameters. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

### Using Power BI

The Power BI OpenSharing connector (Power BI Desktop 2.99.621.0+) allows recipients to discover and visualize shared datasets. Recipients enter the endpoint URL and bearer token from the credential file, optionally setting a row limit (default 1 million rows). ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

### Using Tableau

Tableau Desktop and Tableau Server 2024.1+ support the OpenSharing connector available from Tableau Exchange. Recipients upload the credential file directly and select tables in the Data Explorer. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

### Using Iceberg Clients

Recipients can use external Iceberg clients (Snowflake, Trino, Flink, Spark) via the Apache Iceberg REST Catalog API. The credential file contains the Iceberg REST Catalog endpoint and bearer token. Recipients configure a catalog integration, create a database from the catalog, and query shared tables. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Important Considerations

### Security

- The credential file should never be shared outside the group of authorized users. Databricks recommends using a password manager if sharing within the organization is necessary. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]
- Tokens are valid for a maximum of one year after creation. Providers manage token expiration and rotation. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]
- Databricks may collect information about recipients' use of and access to shared data and share it with the data provider. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

### Limitations

- **Power BI**: Data must fit into machine memory; row limits apply. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]
- **Tableau**: All columns are returned as type `String`; deletion vectors and column mapping are not supported. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]
- **Streaming tables**: Only the current snapshot can be read; history, CDF, and Spark Structured Streaming are not supported. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]
- **Materialized views**: Only the current snapshot can be read; Structured Streaming is not supported. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]
- **Python connector**: CDF queries on tables with column mapping are not supported; CDF queries with `use_delta_format=True` fail if the schema changed during the queried version range. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The open standard for secure data sharing
- [Databricks-to-Databricks Sharing Model](/concepts/databricks-to-databricks-sharing-model.md) — The alternative sharing protocol for Databricks-to-Databricks sharing
- [Delta Sharing](/concepts/delta-sharing.md) — The underlying technology for OpenSharing
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution for Databricks workspaces
- [Apache Iceberg REST Catalog API](/concepts/iceberg-rest-catalog-irc-protocol.md) — Interface for Iceberg client access

## Sources

- access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
- read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md

# Citations

1. [access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md](/references/access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws-7bb360b8.md)
2. [read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md](/references/read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws-9252dd38.md)
