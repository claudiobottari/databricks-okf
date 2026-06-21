---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea79a2d9b0b8d0283d9eb4bd3dad24909bb271249b2beac7854a8c1e48507991
  pageDirectory: concepts
  sources:
    - read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-using-oidc-federation
    - OUOF
    - Read data shared using OIDC federation in a U2M flow
  citations:
    - file: read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md
title: OpenSharing using OIDC Federation
description: Pattern for data recipients to use OpenID Connect (OIDC) federation with an Iceberg REST Catalog client to access Delta Sharing/OpenSharing shares created in Databricks.
tags:
  - data-sharing
  - authentication
  - databricks
  - delta-sharing
timestamp: "2026-06-19T20:07:50.656Z"
---

# OpenSharing using OIDC Federation

**OpenSharing using OIDC Federation** is a method for data recipients to access [Delta Sharing](/concepts/delta-sharing.md) shares created in Databricks without using bearer tokens. Instead, it relies on OpenID Connect (OIDC) federation, allowing recipients to authenticate through their own identity provider (IdP) using OAuth 2.0 credentials. The data is read via an [Iceberg REST Catalog](/concepts/iceberg-rest-catalog-irc-protocol.md) (IRC) client, such as open-source Apache Spark or Snowflake. ^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

## Overview

In this model, the Databricks provider enables OIDC federation for a recipient and shares an OIDC profile portal URL. The recipient uses that portal to download an Iceberg profile file, which contains the catalog endpoint and placeholder values for OAuth credentials. The recipient then replaces those placeholders with their own `clientId`, `clientSecret`, and `scope` values, and configures an Iceberg REST Catalog client to authenticate using OAuth 2.0 against their IdP. The client can then query tables in the share. ^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

## Getting the Iceberg Profile from the OIDC Portal

To start, the recipient must obtain the OIDC profile portal URL from the Databricks provider. On the portal page, the recipient clicks **Download file**. The downloaded file includes placeholders for `clientId`, `clientSecret`, and `scope`, which the recipient replaces with their actual OAuth credentials. The file is then imported into the client code. ^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

## Client Configuration Examples

The following examples show how to configure common Iceberg REST Catalog clients to read shared data using OIDC federation.

### Snowflake

In Snowflake, the recipient creates a catalog integration of type `ICEBERG_REST` with OAuth authentication. The SQL command can also be copied from the OIDC profile portal. Placeholder values must be replaced: `<catalog-integration-name>`, `<catalog-uri>` (from the profile file), `<share-name>`, `<oauth-token-uri>` (the IdP’s OAuth token endpoint), `<oauth-client-id>`, `<oauth-client-secret>`, and `<oauth-scope>`. ^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

```sql
USE ROLE ACCOUNTADMIN;
CREATE OR REPLACE CATALOG INTEGRATION <catalog-integration-name>
    CATALOG_SOURCE = ICEBERG_REST
    TABLE_FORMAT = ICEBERG
    REST_CONFIG = (
        CATALOG_URI = '<catalog-uri>'
        WAREHOUSE = '<share-name>'
        ACCESS_DELEGATION_MODE = VENDED_CREDENTIALS
    )
    REST_AUTHENTICATION = (
        TYPE = OAUTH
        OAUTH_TOKEN_URI = '<oauth-token-uri>'
        OAUTH_CLIENT_ID = '<oauth-client-id>'
        OAUTH_CLIENT_SECRET = '<oauth-client-secret>'
        OAUTH_ALLOWED_SCOPES = ('<oauth-scope>')
    )
    REFRESH_INTERVAL_SECONDS = 30
    ENABLED = TRUE;
```

After creating the catalog integration, the recipient creates a linked database:

```sql
CREATE DATABASE <database-name>
    LINKED_CATALOG = (
        CATALOG = <catalog-integration-name>
    );
```

^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

### Open-Source Spark (OSS Spark)

The recipient runs `spark-shell` with the Iceberg Spark runtime and AWS bundle JARs, and configures Spark SQL catalogs to use the REST catalog type with OAuth2. Placeholder values to replace include: `<spark-home>`, `<iceberg-jars-path>`, `<catalog-uri>`, `<share-name>`, `<oauth-token-uri>`, `<oauth-client-id>`, `<oauth-client-secret>`, `<oauth-scope>`, and `<spark-script>`. ^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

```bash
JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64 \
PATH=/usr/lib/jvm/java-17-openjdk-amd64/bin:$PATH \
<spark-home>/bin/spark-shell \
  --jars <iceberg-jars-path>/iceberg-spark-runtime-4.0_2.13-1.10.2.jar,<iceberg-jars-path>/iceberg-aws-bundle-1.10.2.jar \
  --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions \
  --conf spark.sql.catalog.databricks=org.apache.iceberg.spark.SparkCatalog \
  --conf spark.sql.catalog.databricks.type=rest \
  --conf spark.sql.catalog.databricks.uri=<catalog-uri> \
  --conf spark.sql.catalog.databricks.warehouse=<share-name> \
  --conf spark.sql.catalog.databricks.rest.auth.type=oauth2 \
  --conf spark.sql.catalog.databricks.oauth2-server-uri=<oauth-token-uri> \
  --conf spark.sql.catalog.databricks.credential=<oauth-client-id>:<oauth-client-secret> \
  --conf spark.sql.catalog.databricks.scope=<oauth-scope> \
  --conf spark.sql.catalog.databricks.io-impl=org.apache.iceberg.aws.s3.S3FileIO \
  < <spark-script>
```

## Alternative: Bearer Tokens

If bearer tokens are used instead of OIDC federation, the recipient follows different instructions (see Create a recipient object for non-Databricks users using bearer tokens). ^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

## Provider-Side Setup

For information about how providers enable OIDC federation for recipients, see [Enable Open ID Connect (OIDC) federation for OpenSharing recipients](/concepts/oidc-federation-for-opensharing.md). ^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

## Related Concepts

- OIDC Federation – The underlying authentication mechanism.
- [Iceberg REST Catalog](/concepts/iceberg-rest-catalog-irc-protocol.md) – The catalog protocol used to access shared data.
- [Delta Sharing](/concepts/delta-sharing.md) – The open protocol for data sharing.
- [OpenSharing](/concepts/opensharing.md) – The Databricks-to-Open sharing model.
- OAuth 2.0 – The authentication standard used for token exchange.

## Sources

- read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md

# Citations

1. [read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md](/references/read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws-2663b307.md)
