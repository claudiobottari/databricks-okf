---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c27113131d9db95ed77fb26d006ff8474fdafbac312017d7da3ba9108b3228bc
  pageDirectory: concepts
  sources:
    - access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - credential-file-opensharing
    - CF(
    - Credential file
  citations:
    - file: access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
title: Credential file (OpenSharing)
description: A file downloaded via an activation link in the Databricks-to-Open sharing model, used for bearer token authentication; downloadable only once and should be stored securely.
tags:
  - authentication
  - credentials
  - security
timestamp: "2026-06-19T08:49:46.492Z"
---

# Credential file (OpenSharing)

A **credential file** is a security token file that a [Data Recipient](/concepts/data-recipient.md) downloads to authenticate and access shared data in the [OpenSharing](/concepts/opensharing.md) Databricks-to‑Open sharing model. It is the equivalent of a long-lived bearer token that proves the recipient’s identity to the data provider’s account. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Obtaining the credential file

When a data provider shares data using the Databricks‑to‑Open sharing protocol, they send the recipient an **activation URL** or a **portal URL** over a secure channel. The recipient follows the link and downloads the credential file. The activation link can be used only once; after the file has been downloaded, the **Download Credential File** button is disabled. If the activation link is lost before it is used, the recipient must contact the data provider. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

Both bearer tokens and [OAuth Client Credentials](/concepts/oauth-client-credentials-grant-m2m-flow.md) are supported for the credential file. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Using the credential file

The credential file is used to authenticate to the data provider’s account and read the shared data. Access persists as long as the underlying token is valid and the provider continues to share the data. Recipients can read and make copies of the shared data, but they cannot modify the source data. Updates made by the provider are visible in near real time. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

For instructions on using the credential file with Databricks, Apache Spark, pandas, and Power BI, see the documentation on reading shared data with bearer tokens. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Security and expiration

- **Token lifetime**: Tokens are valid for a maximum of one year after creation. Providers are responsible for token expiration and rotation. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]
- **Storage**: The credential file must be stored in a secure location. Databricks recommends using a password manager if the file must be shared within the recipient’s organization. The file should never be shared with people outside the group of users who should have access. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Related concepts

- [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md) – The sharing model that uses credential files.
- [OpenSharing](/concepts/opensharing.md) – The open standard for secure data sharing.
- [Data Recipient](/concepts/data-recipient.md) – The person or group receiving shared data.
- Data provider – The Databricks user who shares data.
- Bearer token – The authentication mechanism for the credential file.
- [OIDC federation](/concepts/oidc-federation-policy.md) – An alternative authentication method for Databricks‑to‑Open sharing.
- [Reading shared data with OIDC federation](/concepts/opensharing-with-oidc-federation.md) – For Tableau, Power BI, and Python clients.

## Sources

- access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md

# Citations

1. [access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md](/references/access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws-7bb360b8.md)
