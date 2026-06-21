---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea6bf1f625bca534155cd74109aaa01ed4b3a4b0975b24e8bbbabf4ae5809990
  pageDirectory: concepts
  sources:
    - read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - iceberg-rest-catalog-integration-for-opensharing
    - IRCIFO
  citations:
    - file: read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md
title: Iceberg REST Catalog Integration for OpenSharing
description: A method to access OpenSharing data using external Iceberg clients (Snowflake, Trino, Flink, Spark) via the Apache Iceberg REST Catalog API, using vended credentials.
tags:
  - iceberg
  - data-sharing
  - api
timestamp: "2026-06-19T20:11:19.274Z"
---

# Iceberg REST Catalog Integration for OpenSharing

**Iceberg REST Catalog Integration for OpenSharing** enables external Iceberg-compatible clients — such as Snowflake, Trino, Flink, and Apache Spark — to read shared data assets with zero-copy access by connecting to an OpenSharing provider through the [Apache Iceberg REST Catalog API](https://github.com/apache/iceberg/blob/main/open-api/rest-catalog-open-api.yaml). This integration allows organizations to consume shared data from Databricks-to-Open sharing without requiring Databricks-native compute. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Prerequisites

Before accessing shared data assets with external Iceberg clients, users must obtain the following credentials from the provider's credential file: ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

- **Iceberg REST Catalog endpoint** (`icebergEndpoint`) — formatted as `<workspace-url>/api/2.0/delta-sharing/metastores/<metastore-id>/iceberg`
- **Bearer token** — a valid authentication token from the credential file
- **Share name** — the name of the share containing the data
- **Namespace/schema name** (optional) — for scoping the query
- **Table name** (optional) — for targeting a specific table

The endpoint and bearer token are found in the credential file shared by the data provider. The share name, namespace, and table name can be discovered programmatically using OpenSharing APIs. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

### Discovering Shares and Tables

Use the following shell commands to explore available shares and tables after obtaining the endpoint and bearer token:

```shell
# List shares
curl -X GET "<endpoint>/shares" \
  -H "Authorization: Bearer <bearerToken>"

# List namespaces
curl -X GET "<icebergEndpoint>/v1/shares/<share>/namespaces" \
  -H "Authorization: Bearer <bearerToken>"

# List tables
curl -X GET "<icebergEndpoint>/v1/shares/<share>/namespaces/<namespace>/tables" \
  -H "Authorization: Bearer <bearerToken>"
```

^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

This method always retrieves the most up-to-date list of assets. However, it requires internet access and can be harder to integrate in no-code environments. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Configuring the Iceberg Catalog Integration

After obtaining the necessary connection credentials, configure your client to use the Iceberg REST Catalog endpoints to create and query tables. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

### Creating the Catalog Integration

For each share, create a catalog integration using SQL:

```sql
USE ROLE ACCOUNTADMIN;

CREATE OR REPLACE CATALOG INTEGRATION <CATALOG_PLACEHOLDER>
CATALOG_SOURCE = ICEBERG_REST
TABLE_FORMAT = ICEBERG
REST_CONFIG = (
  CATALOG_URI = '<icebergEndpoint>',
  WAREHOUSE = '<share_name>',
  ACCESS_DELEGATION_MODE = VENDED_CREDENTIALS
)
REST_AUTHENTICATION = (
  TYPE = BEARER,
  BEARER_TOKEN = '<bearerToken>'
)
ENABLED = TRUE;
```

^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

Optionally, add `REFRESH_INTERVAL_SECONDS` to keep metadata up to date, setting the value based on your catalog update frequency:

```sql
REFRESH_INTERVAL_SECONDS = 30
```

^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

### Creating a Database from the Catalog

After the catalog is configured, create a database from the catalog. This automatically creates all schemas and tables in that catalog:

```sql
CREATE DATABASE <DATABASE_PLACEHOLDER>
LINKED_CATALOG = (
  CATALOG = <CATALOG_PLACEHOLDER>
);
```

^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

### Verifying the Connection

To confirm that the sharing is successful, query from a table in the database. You should see the shared data from Databricks. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

If the result is empty or an error occurs, follow these common troubleshooting steps: ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

- Double-check the privileges, snapshot generation status, and REST credentials.
- Contact your data provider.
- See the documentation specific to your Iceberg client.

## Client-Specific Examples

### Snowflake

To read shared data assets in Snowflake, upload the credential file and generate the necessary SQL command:

1. From your OpenSharing activation link, click the Snowflake icon.
2. On the Snowflake integration page, upload the credential file received from the data provider.
3. After loading the credential, choose the share you want to access.
4. Click **Generate SQL** after selecting the desired assets.
5. Copy and paste the generated SQL into your Snowflake worksheet. Replace `CATALOG_PLACEHOLDER` with the catalog name and `DATABASE_PLACEHOLDER` with the database name.

^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

**Snowflake limitations:**

- The metadata file does not automatically update with the latest snapshot. You must rely on auto-refresh or manual refreshes.
- R2 is not supported.
- All Iceberg client limitations apply.

### Apache Spark

Shared data can be accessed via Apache Spark using the Iceberg REST Catalog integration after configuring the catalog. See the [Apache Spark connector](/concepts/opensharing-apache-spark-connector.md) documentation for complete examples. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

### PyIceberg

Shared data can be accessed via PyIceberg after configuring the catalog. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

### REST API

Shared data can be accessed directly using the Iceberg REST API. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Iceberg Client Limitations

The following limitations apply when querying OpenSharing data from Iceberg clients: ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

- When listing tables in a namespace, if the namespace contains more than 100 shared views, the response is limited to the first 100 views.

All Snowflake limitations also apply to the Iceberg REST Catalog integration when used with Snowflake. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Related Concepts

- [OpenSharing Protocol](/concepts/opensharing-protocol.md) — The open standard for data sharing used by this integration
- Bearer token authentication — The authentication method used by the Iceberg REST Catalog endpoint
- [Delta Sharing](/concepts/delta-sharing.md) — The broader data sharing framework that OpenSharing extends
- [Unity Catalog](/concepts/unity-catalog.md) — The [Metastore](/concepts/metastore.md) that hosts OpenSharing providers and shares
- [Apache Iceberg REST Catalog API](/concepts/iceberg-rest-catalog-irc-protocol.md) — The API specification that enables cross-platform table access
- External Iceberg Clients — Third-party tools that can consume Iceberg REST Catalog endpoints

## Sources

- read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md

# Citations

1. [read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md](/references/read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws-9252dd38.md)
