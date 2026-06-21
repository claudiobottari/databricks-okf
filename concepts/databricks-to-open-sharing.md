---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e6b2a3eac8bf5d89424aecc34e6297fce8b495f171359ff5863176506be02d6c
  pageDirectory: concepts
  sources:
    - access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
    - create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
    - what-is-opensharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-to-open-sharing
    - Databricks‑to‑open sharing
    - Databricks-to-Open
    - databricks-to-open-sharing-model
    - DSM
  citations:
    - file: what-is-opensharing-databricks-on-aws.md
    - file: access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
    - file: create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
title: Databricks-to-Open Sharing
description: A sharing model where the recipient can use any tool (including Databricks) to access shared data via an activation URL, portal link, credential file, or OIDC federation.
tags:
  - data-sharing
  - open-standard
  - databricks
timestamp: "2026-06-19T21:56:33.860Z"
---

---

title: Databricks-to-Open Sharing
summary: A sharing protocol in OpenSharing that allows data providers with a Unity Catalog-enabled Databricks workspace to share tabular data with recipients who do not have access to a Unity Catalog-enabled Databricks workspace, using token-based authentication (bearer tokens or OIDC federation).
sources:
  - access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
  - create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
  - what-is-opensharing-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:23:13.388Z"
updatedAt: "2026-06-19T17:24:44.117Z"
tags:
  - data-sharing
  - cross-platform
  - databricks
aliases:
  - databricks-to-open-sharing
confidence: 0.95
provenanceState: merged
inferredParagraphs: 0
---

# Databricks-to-Open Sharing

**Databricks-to-Open Sharing** is one of the two primary protocols in [OpenSharing](/concepts/opensharing.md) on Databricks. It enables a data provider who manages data in a Unity Catalog‑enabled Databricks workspace to share tabular data with recipients who **do not** have access to a Unity Catalog‑enabled Databricks workspace—or who may not use Databricks at all. The connection is secured using token‑based authentication, either a long‑lived bearer token or [OIDC federation](/concepts/oidc-federation-for-opensharing.md). ^[what-is-opensharing-databricks-on-aws.md]

## When to Use Databricks-to-Open Sharing

Use Databricks-to-Open Sharing when your recipients lack access to a Unity Catalog‑enabled Databricks workspace. If your recipients *do* have such a workspace, prefer [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md), which provides a secure connection managed entirely by Databricks, supports sharing of notebooks, volumes, and models, and does not require manual token management. ^[what-is-opensharing-databricks-on-aws.md]

## Authentication Methods

Providers can authenticate recipients using one of two methods:

- **Bearer token**: The provider generates a long‑lived bearer token and shares it with the recipient, typically via an activation link that allows the recipient to download a credential file. The token is sent securely by the provider and can have a configurable lifetime. Recipients present the token in every request to authenticate. ^[what-is-opensharing-databricks-on-aws.md]
- **Open ID Connect (OIDC) federation**: The provider grants short‑lived Databricks OAuth tokens in exchange for JWT tokens issued by the recipient’s identity provider (IdP). This avoids long‑lived secrets and supports both user‑to‑machine (U2M) and machine‑to‑machine (M2M) flows. The recipient receives a portal URL instead of a credential file. ^[what-is-opensharing-databricks-on-aws.md, access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Provider Setup

To set up Databricks-to-Open Sharing, a [Metastore](/concepts/metastore.md) admin or user with the `CREATE RECIPIENT` privilege must:

1. **Create a recipient object** with authentication type `TOKEN` or `OIDC_FEDERATION`. This object represents the consuming organization. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]
2. **Grant the recipient access** to one or more shares. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]
3. **Send the recipient** the connection information—an activation link (for bearer tokens) or a portal URL (for OIDC federation)—over a secure channel. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

The provider must have at least one Databricks workspace enabled for Unity Catalog. The OpenSharing server is built into Databricks, so no separate server setup is required. ^[what-is-opensharing-databricks-on-aws.md]

## Recipient Access

### Without a Unity Catalog‑enabled Workspace

Recipients can use a wide range of tools to read the shared data: Apache Spark, pandas, Power BI, Tableau, or any other platform that supports the OpenSharing open‑source connectors. They authenticate with the bearer token from the credential file or, for OIDC, with tokens obtained from their own IdP. The data is read‑only and updates appear in near real time. ^[what-is-opensharing-databricks-on-aws.md, access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

Recipients must keep the credential file secure and should not share it outside the authorized group. Tokens have a maximum validity of one year from creation. If the activation link is lost before use, the recipient must contact the provider. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

### With a Unity Catalog‑enabled Workspace

If the recipient happens to have a Unity Catalog‑enabled workspace, they can still access data shared via the open protocol. In that case, the recipient’s [Metastore](/concepts/metastore.md) may contain a **provider object** that represents the data‑sharing organization. This allows the recipient to view shared data as a read‑only catalog and manage granular access using Unity Catalog permissions. Token rotation or deletion can be handled through the provider object. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Limitations

- Only tabular assets can be shared: Delta tables, managed Iceberg tables, streaming tables, and materialized views. Notebooks, volumes, and models are not supported through this protocol—they require [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md). ^[what-is-opensharing-databricks-on-aws.md]
- Bearer tokens require manual management of credentials and activation links.
- Recipients with a Unity Catalog workspace cannot take advantage of the same‑account seamless integration that Databricks‑to‑Databricks provides.

## Related Concepts

- [OpenSharing](/concepts/opensharing.md)
- [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md)
- [Delta Sharing](/concepts/delta-sharing.md)
- [OIDC Federation for OpenSharing](/concepts/oidc-federation-for-opensharing.md)
- [Bearer Token Authentication for OpenSharing](/concepts/bearer-token-authentication-for-opensharing.md)
- Recipient Object
- Provider Object

## Sources

- access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
- create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
- what-is-opensharing-databricks-on-aws.md

# Citations

1. [what-is-opensharing-databricks-on-aws.md](/references/what-is-opensharing-databricks-on-aws-adff4826.md)
2. [access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md](/references/access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws-7bb360b8.md)
3. [create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md](/references/create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws-a4778c5e.md)
