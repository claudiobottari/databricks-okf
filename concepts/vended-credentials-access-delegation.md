---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3d648923d858285d54ebc0a3767588d306232fa5bf69f500fabc404a2e168833
  pageDirectory: concepts
  sources:
    - read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - vended-credentials-access-delegation
    - VCAD
    - Access Delegation Mode
    - Vended Credentials
  citations:
    - file: read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md
title: Vended Credentials Access Delegation
description: An access delegation mode (ACCESS_DELEGATION_MODE = VENDED_CREDENTIALS) used in Snowflake's Iceberg REST Catalog integration to delegate credential management for accessing shared data.
tags:
  - security
  - credentials
  - snowflake
  - iceberg
timestamp: "2026-06-19T20:08:09.323Z"
---

## Vended Credentials Access Delegation

**Vended Credentials Access Delegation** is a configuration mode for data access delegation used when setting up an Iceberg REST Catalog (IRC) integration to read data shared via [Delta Sharing](/concepts/delta-sharing.md) or [OpenSharing](/concepts/opensharing.md) with [Open ID Connect (OIDC) federation](/concepts/opensharing-with-oidc-federation.md). When a client specifies `ACCESS_DELEGATION_MODE = VENDED_CREDENTIALS`, the Iceberg REST Catalog provides temporary credentials (vended credentials) to the client, allowing it to access the underlying cloud storage where the shared data resides. ^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

This mode is explicitly required when creating a Snowflake catalog integration for reading shared data. In the `REST_CONFIG`, the parameter `ACCESS_DELEGATION_MODE = VENDED_CREDENTIALS` is set alongside other connection details such as the catalog URI, share name, and OAuth authentication parameters. ^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

The use of vended credentials is a common pattern in [Iceberg REST Catalog](/concepts/iceberg-rest-catalog-irc-protocol.md) implementations, where the catalog acts as a credential vending service. The client receives short-lived cloud storage credentials (e.g., AWS temporary credentials) without needing direct access to the provider’s storage account. This enhances security by avoiding long-lived static credentials at the client side. ^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

### Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md)
- [Open ID Connect (OIDC) federation](/concepts/opensharing-with-oidc-federation.md)
- [Iceberg REST Catalog](/concepts/iceberg-rest-catalog-irc-protocol.md)
- Cloud Credentials
- Snowflake catalog integration
- [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md)

### Sources

- read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md

# Citations

1. [read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md](/references/read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws-2663b307.md)
