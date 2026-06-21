---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ffaf0047c4acb80c58dfc6bd23cb28db827e221f5996a0bea18400d8a01c7cb5
  pageDirectory: concepts
  sources:
    - read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-oidc-profile-portal
    - DOPP
  citations:
    - file: read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md
title: Databricks OIDC Profile Portal
description: A portal URL provided by the Databricks provider where recipients download an Iceberg profile file containing catalog endpoint, share name, and placeholders for OAuth credentials.
tags:
  - databricks
  - oidc
  - configuration
timestamp: "2026-06-19T20:08:00.814Z"
---

Here is the wiki page for "Databricks OIDC Profile Portal".

---

## Databricks OIDC Profile Portal

The **Databricks OIDC Profile Portal** is a web-based interface provided by a Databricks Delta Sharing provider to recipients who use **Open ID Connect (OIDC) federation** for authentication. Through the portal, recipients can download an **Iceberg profile file** that contains the connection details needed to access shared data using an Iceberg REST Catalog (IRC) client, such as OSS Spark or Snowflake. ^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

### Accessing the Portal

The URL for the OIDC profile portal is shared by the Databricks provider. If a recipient has not yet received the URL, they must request it directly from the provider. ^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

### Downloading and Using the Profile

1. Navigate to the OIDC profile portal URL provided by the Databricks provider.
2. On the portal page, click **Download file** to obtain the profile.
3. In the downloaded file, replace the placeholders `clientId`, `clientSecret`, and `scope` with your own OAuth credentials.
4. Import the modified profile file into your client code.

After downloading and configuring the profile, you can access the shared data using any [Iceberg REST Catalog (IRC)](/concepts/iceberg-rest-catalog-irc-protocol.md) client. ^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

### Related Concepts

- Open ID Connect (OIDC) Federation — The authentication mechanism used by OIDC federation recipients to access Delta Sharing shares.
- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for sharing data across platforms, of which OIDC federation is a specific authentication method.
- [Iceberg REST Catalog (IRC)](/concepts/iceberg-rest-catalog-irc-protocol.md) — The catalog interface used to access shared data from OIDC federation recipients.
- [Delta Sharing Recipient](/concepts/delta-sharing-recipient-object.md) — The entity that receives and accesses shared data via Delta Sharing.
- Delta Sharing Provider — The Databricks workspace that shares data and manages recipient access.

## Sources

- read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md

# Citations

1. [read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md](/references/read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws-2663b307.md)
