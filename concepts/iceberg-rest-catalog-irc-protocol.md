---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e9c29641f02c6cb2b8fb6b3305c811b11b9a883080301a6363f4246fdcc70e32
  pageDirectory: concepts
  sources:
    - read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - iceberg-rest-catalog-irc-protocol
    - IRC(P
    - Iceberg REST Catalog (IRC)
    - Apache Iceberg REST Catalog
    - Apache Iceberg REST Catalog API
    - Iceberg REST Catalog
    - Iceberg REST Catalog API
  citations:
    - file: read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md
title: Iceberg REST Catalog (IRC) Protocol
description: The open protocol that allows clients like Spark and Snowflake to read Iceberg tables from a catalog endpoint, used here to access shared data from Databricks OpenSharing.
tags:
  - iceberg
  - protocol
  - data-sharing
timestamp: "2026-06-19T20:07:47.277Z"
---

---
title: Iceberg REST Catalog (IRC) Protocol
summary: A protocol that enables clients like OSS Spark and Snowflake to access Apache Iceberg tables hosted in Databricks via a REST API, supporting OAuth2 authentication and S3 storage.
sources:
  - read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md
kind: concept
createdAt: "2026-06-21T00:00:00.000Z"
updatedAt: "2026-06-21T00:00:00.000Z"
tags:
  - iceberg
  - protocol
  - databricks
  - delta-sharing
  - open-sharing
aliases:
  - irc-protocol
  - iceberg-rest-catalog
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# Iceberg REST Catalog (IRC) Protocol

The **Iceberg REST Catalog (IRC) Protocol** is an API specification that allows external compute engines to discover, read, and write Apache Iceberg tables through a RESTful interface. In the context of [Delta Sharing](/concepts/delta-sharing.md) and OpenSharing, Databricks exposes an IRC endpoint that Open ID Connect (OIDC) federation recipients can use to access shared data without running Databricks compute. ^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

## Overview

When a Databricks provider enables OIDC federation for an OpenSharing recipient, the recipient receives a profile file containing an IRC endpoint URI. Clients that support the Iceberg REST Catalog — such as OSS Apache Spark and Snowflake — can use this endpoint to list shares and query tables. The protocol handles authentication via OAuth2, returning short-lived credentials for accessing the underlying cloud storage (Amazon S3). ^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

## Authentication

The IRC protocol used with OIDC federation supports OAuth2 as the authentication mechanism. The client provides:

- **OAuth token URI** — the IdP's token endpoint.
- **Client ID** and **Client secret** — OAuth credentials.
- **Scope** — the OAuth scope required for token exchange.

In the catalog configuration, `rest.auth.type` is set to `oauth2`, and the credential is passed as `client-id:client-secret`. ^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

## Configuration Examples

### Snowflake

In Snowflake, create a catalog integration with `CATALOG_SOURCE = ICEBERG_REST` and `TABLE_FORMAT = ICEBERG`. The `REST_CONFIG` includes the `CATALOG_URI` and sets `WAREHOUSE` to the share name. The `ACCESS_DELEGATION_MODE` is set to `VENDED_CREDENTIALS` to allow Snowflake to obtain temporary storage credentials. The `REST_AUTHENTICATION` block configures OAuth2 with the IdP's token endpoint and client credentials. ^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

A linked database is then created referencing the catalog integration, making the shared tables available for querying. ^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

### OSS Apache Spark

For OSS Spark, the catalog is configured via Spark configuration properties. The catalog type is set to `rest`, and the URI points to the IRC endpoint. The warehouse is set to the share name. Authentication uses `oauth2` with the server URI, credentials, and scope. The `io-impl` property is set to `org.apache.iceberg.aws.s3.S3FileIO` to enable direct S3 access using the vended credentials. ^[read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md]

## Supported Clients

- Snowflake — via `CREATE CATALOG INTEGRATION` with `ICEBERG_REST` source.
- [OSS Apache Spark](/concepts/apache-spark-compatibility.md) — using the Iceberg Spark runtime and AWS bundle JARs.
- Any other Iceberg REST Catalog client that supports OAuth2 authentication and vended credentials.

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The framework for sharing data across platforms.
- [OpenSharing](/concepts/opensharing.md) — Databricks' open standard for sharing without requiring recipients to use Databricks.
- Open ID Connect (OIDC) Federation — The identity federation mechanism used for authentication.
- [Apache Iceberg](/concepts/uniform-apache-iceberg-format.md) — The open table format underlying the IRC protocol.
- OAuth2 — The authentication protocol used for token exchange.
- [Vended Credentials](/concepts/vended-credentials-access-delegation.md) — Temporary cloud storage credentials provided by the catalog.

## Sources

- read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md

# Citations

1. [read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws.md](/references/read-data-shared-using-open-id-connect-oidc-federation-from-an-iceberg-client-databricks-on-aws-2663b307.md)
