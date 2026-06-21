---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5b4b62cbcd1668be20f0962b84bcafacfa1bf13e127ce0f6a87e98c91f094e41
  pageDirectory: concepts
  sources:
    - read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - snowflake-catalog-integration-for-iceberg
    - SCIFI
    - Snowflake catalog integration
  citations:
    - file: read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md
title: Snowflake Catalog Integration for Iceberg
description: Snowflake SQL configuration to create a CATALOG INTEGRATION and linked database using the ICEBERG_REST catalog source with OAuth authentication and vended credentials access delegation.
tags:
  - snowflake
  - catalog-integration
  - iceberg
timestamp: "2026-06-19T20:08:04.440Z"
---

## Snowflake Catalog Integration for Iceberg

**Snowflake Catalog Integration for Iceberg** refers to the process of configuring Snowflake as an Iceberg REST Catalog (IRC) client to read data shared through [OpenSharing](/concepts/opensharing.md) (formerly Delta Sharing) from a Databricks provider, using OpenID Connect (OIDC) Federation for authentication. This integration allows data recipients to access shares directly from Snowflake without copying the data into Snowflake’s storage.^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

### Prerequisites

Before creating the catalog integration, a recipient must:

1. Obtain the OIDC profile portal URL from the Databricks provider.
2. Open that URL, click **Download file**, and replace `clientId`, `clientSecret`, and `scope` in the downloaded file with the recipient’s own OAuth credentials.^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

The downloaded profile contains the Iceberg REST Catalog endpoint (`catalog-uri`) and the share name that was granted to the recipient.^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

### Snowflake SQL Commands

In a Snowflake worksheet (using the `ACCOUNTADMIN` role or a role with the required privileges), execute two commands.

#### 1. Create the Catalog Integration

The `CREATE OR REPLACE CATALOG INTEGRATION` statement defines how Snowflake connects to the Iceberg REST Catalog. Replace the placeholder values before running.

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

Key configuration details:

- `CATALOG_SOURCE = ICEBERG_REST` tells Snowflake to use the Iceberg REST protocol.
- `TABLE_FORMAT = ICEBERG` specifies the Iceberg table format.
- `REST_CONFIG`: provides the catalog endpoint (`CATALOG_URI`) and the share name (`WAREHOUSE`). `ACCESS_DELEGATION_MODE = VENDED_CREDENTIALS` allows Snowflake to use temporary credentials to access the underlying cloud storage.
- `REST_AUTHENTICATION`: uses OAuth 2.0 with the recipient’s IdP token endpoint, client ID, client secret, and the required scope.
- `REFRESH_INTERVAL_SECONDS = 30` controls how often the integration refreshes authentication tokens.
- `ENABLED = TRUE` activates the integration.

^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

#### 2. Create a Linked Database

Use the catalog integration to create a database that references the share. Replace `<database-name>` with a name for the linked database.

```sql
CREATE DATABASE <database-name>
    LINKED_CATALOG = (
        CATALOG = <catalog-integration-name>
    );
```

After this step, tables and views from the share become accessible in Snowflake through the linked database.^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

### Alternative Client: OSS Spark

For comparison, recipients can also use an Apache Spark (OSS Spark) client with the Iceberg Spark runtime and AWS bundle JARs, configuring the catalog via Spark SQL properties with OAuth2 authentication. The same share and credential values are used.^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

### Related Concepts

- [Iceberg REST Catalog](/concepts/iceberg-rest-catalog-irc-protocol.md) – The protocol used by Snowflake to interact with the share.
- [OpenSharing](/concepts/opensharing.md) – The open standard for sharing data between different systems.
- [Delta Sharing](/concepts/delta-sharing.md) – The original Databricks sharing protocol; OpenSharing extends it.
- OIDC Federation – Authentication mechanism that avoids static bearer tokens.
- Snowflake – The cloud data platform acting as the client.
- [Access Delegation Mode](/concepts/vended-credentials-access-delegation.md) – Methods for granting temporary storage access (e.g., VENDED_CREDENTIALS).

### Sources

- read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md

# Citations

1. [read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md](/references/read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws-2663b307.md)
