---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e6762b82f3b91ec819b09d72407a41cb30a73cd33643516dc91c9847a16a9868
  pageDirectory: concepts
  sources:
    - access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-credential-file
    - OCF
  citations:
    - file: access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
    - file: read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md
title: OpenSharing Credential File
description: A downloadable file used in Databricks-to-Open sharing with bearer tokens to authenticate and read shared data; can only be downloaded once and must be stored securely.
tags:
  - data-sharing
  - authentication
  - security
timestamp: "2026-06-19T21:56:37.683Z"
---

# OpenSharing Credential File

An **OpenSharing credential file** is a downloadable file that authenticates a data recipient to access datasets shared through the Databricks-to-Open sharing protocol. It contains bearer tokens and endpoint metadata that enable read-only, near-real-time access to shared Delta Lake tables, views, and volumes without granting the recipient any ability to modify the source data. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md, read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Overview

In the [OpenSharing](/concepts/opensharing.md) Databricks-to-Open sharing model, a data provider creates a recipient object in their Databricks account and sends the intended recipient an activation URL or a portal link over a secure channel (e.g., email or encrypted messaging). The recipient follows the link to download the credential file. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

The activation link can be used **only once**. After the file has been downloaded, visiting the link again will show a disabled **Download Credential File** button. If the link is lost before use, the recipient must contact the data provider to request a new one. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Security Considerations

The credential file should be stored in a secure location and **never shared** with anyone outside the authorized group of users. If you need to share it with someone in your organization, Databricks recommends using a password manager. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

Databricks may collect information about data recipients' use of and access to the shared data (including identifying individuals or companies who access the data using the credential file) and may share it with the applicable data provider. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Bearer Token Lifecycle

Access to shared data persists as long as the underlying bearer token is valid and the provider continues to share the data. Tokens are valid for a maximum of **one year** after creation. Providers manage token expiration and rotation — when a token expires, the recipient receives new credentials through a fresh activation link or an updated credential file. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md, read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## File Structure

The credential file contains configuration details for connecting to the provider's Delta Sharing server. The following table summarizes the key fields:

| Field | Purpose |
|-------|---------|
| `endpoint` | The base URL of the provider's Delta Sharing server |
| `bearerToken` | The short-lived bearer token used for authentication |
| `icebergEndpoint` | (Optional) The Iceberg REST Catalog endpoint, present if the provider enables Iceberg client access |
| `shareCredentialsVersion` | Version of the credential format |

The `delta-sharing` Python connector and Spark connector read this file to discover available shares, schemas, and tables. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Access Limitations

The credential file only supports **read-only** access; recipients can read and make copies of the shared data but cannot modify the source data. Updates to the shared data are available in near real time. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The open standard for secure data sharing
- [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md) — The protocol that uses credential files for authentication
- [Delta Sharing](/concepts/delta-sharing.md) — The broader sharing framework
- Data Provider — The entity that creates shares and issues credential files
- [Data Recipient](/concepts/data-recipient.md) — The entity that uses the credential file to access shared data
- [Bearer Token](/concepts/oidc-vs-bearer-token-authentication.md) — The authentication mechanism embedded in the credential file
- [OAuth Client Credentials](/concepts/oauth-client-credentials-grant-m2m-flow.md) — Alternative authentication method for OIDC-based sharing
- [Unity Catalog](/concepts/unity-catalog.md) — Databricks' governance layer that can ingest credential files

## Sources

- access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
- read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md

# Citations

1. [access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md](/references/access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws-7bb360b8.md)
2. [read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md](/references/read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws-9252dd38.md)
