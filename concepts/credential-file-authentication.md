---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5e6c7a016abfa42320545d31fe3ac18f08a94bdb1d62ceadf107a548f3bdfcbd
  pageDirectory: concepts
  sources:
    - access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - credential-file-authentication
    - CFA
  citations:
    - file: access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
title: Credential File Authentication
description: A bearer-token-based authentication method for Databricks-to-Open sharing, where recipients download a credential file (one-time) from an activation URL to access shared data; tokens are valid for up to one year.
tags:
  - authentication
  - data-sharing
  - security
timestamp: "2026-06-19T17:24:47.685Z"
---

```markdown
---
title: Credential File Authentication
summary: In Databricks-to-Open sharing with bearer tokens, recipients download a credential file once to authenticate and access shared data.
sources:
  - access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:17:13.085Z"
updatedAt: "2026-06-18T14:17:13.085Z"
tags:
  - authentication
  - data-sharing
  - security
aliases:
  - credential-file-authentication
  - CFA
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Credential File Authentication

**Credential file authentication** is a method for accessing data shared via OpenSharing’s Databricks-to-Open model. Instead of relying on a Databricks workspace identity, the data recipient downloads a credential file – containing a bearer token – from the data provider and uses that file to authenticate and read the shared data. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Obtaining a Credential File

In the Databricks-to-Open sharing model, the data provider creates a recipient and a share, then sends the recipient an **activation URL** (or a portal URL) over a secure channel. The recipient follows the activation link to download the credential file. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

The credential file can be downloaded **only once**. If the activation link is visited again after the download has already occurred, the **Download Credential File** button is disabled. If the activation link is lost before it is used, the recipient must contact the data provider for a new link. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

Once downloaded, the credential file must be stored in a secure location. Databricks recommends using a password manager if the file needs to be shared with others within the same organization. The credential file should **never** be shared with anyone outside the authorized group of users. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Using a Credential File

The credential file is used to authenticate to the data provider’s account and read the shared data. Access persists as long as the underlying bearer token is valid and the provider continues to share the data. The data provider manages token expiration and rotation; tokens are valid for a maximum of one year after creation. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

Recipients can read the shared data and create local copies, but **cannot modify the source data**. Updates made by the provider to the underlying data become available to the recipient in near real time. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

The credential file can be used with multiple tools to read the shared data. Databricks provides documentation for accessing data via the credential file in: ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

- Apache Spark
- pandas
- Power BI
- Databricks workspaces

## Contrast with Databricks-to-Databricks Sharing

In the Databricks-to-Databricks sharing model, no credential file is required. Databricks automatically handles the secure connection, and the shared data is discoverable directly in the recipient’s workspace. Granular access control on that data can be configured by the recipient’s team if necessary. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Related Concepts

- [[OpenSharing]] — The open standard for secure data sharing
- [[Databricks-to-Open sharing]] — The model that uses credential file authentication
- [[Databricks-to-Databricks sharing]] — The alternative model that does not use credential files
- Bearer token — The authentication mechanism embedded in the credential file
- [[Delta Sharing]] — The protocol underlying OpenSharing on Databricks

## Sources

- access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
```

# Citations

1. [access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md](/references/access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws-7bb360b8.md)
