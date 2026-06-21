---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2c6fcf5c03f5e706b73629339d9bbd392371d6cec55c14436a78f0b1c56f9df5
  pageDirectory: concepts
  sources:
    - access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-recipient
    - Data Recipients
    - Manage recipients
    - Recipient
    - Recipients
    - recipient
  citations:
    - file: access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
title: Data Recipient
description: A person or group outside the data provider's organization who receives and accesses shared data via OpenSharing, with read-only access.
tags:
  - data-sharing
  - roles
  - access-control
timestamp: "2026-06-18T14:17:26.212Z"
---

# Data Recipient

A **data recipient** is a person or group outside of a data provider's organization who receives access to data shared through [OpenSharing](/concepts/opensharing.md). The data recipient may be an individual user, a team, or an entire organization that has been granted permission to read shared datasets, tables, volumes, or views. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Overview

In the OpenSharing model, a Databricks user (the *data provider*) shares data with recipients outside their organization. The shared data is not provided by Databricks directly but by data providers running on Databricks. Databricks may collect information about data recipients' use of and access to the shared data (including identifying any individual or company who accesses the data using the credential file) and may share it with the data provider. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Access Models

How a data recipient accesses shared data depends on the sharing model configured by the data provider.

### Databricks-to-Databricks Sharing

In this model, the data recipient must be a user on a Databricks workspace that is enabled for [Unity Catalog](/concepts/unity-catalog.md). A member of the recipient's team provides the data provider with a unique sharing identifier for their Unity Catalog [Metastore](/concepts/metastore.md). The sharing identifier is a string in the format `<cloud>:<region>:<uuid>`, for example `aws:eu-west-1:b0c978c8-3e68-4cdf-94af-d05c120ed1ef`. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

To obtain the sharing identifier using Catalog Explorer:
1. In the Databricks workspace, click **Catalog**.
2. At the top of the **Catalog** pane, click the gear icon and select **OpenSharing**.
3. On the **Shared with me** tab, select the Databricks sharing organization name and choose **Copy sharing identifier**.

To obtain the sharing identifier using a notebook or Databricks SQL query, use the `CURRENT_METASTORE()` function. The notebook must run on a standard or dedicated access mode in the workspace used to access the shared data. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

```sql
SELECT CURRENT_METASTORE();
```

The data provider then creates a *recipient* in their Databricks account to represent the recipient's organization and a *share* representing the tables, volumes, and views to be shared. The shared data becomes automatically discoverable in the recipient's Databricks workspace without requiring a credential file. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

### Databricks-to-Open Sharing

In this model, the data recipient can use any tool (including Databricks) to access the shared data. The data provider sends the recipient an activation URL or a portal link over a secure channel. The recipient follows the link to download a credential file or URL that enables access to the shared data. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

Both bearer tokens and OAuth Client Credentials are supported for authentication. The activation link should not be shared with anyone, and a credential file can be downloaded only once. If the activation link is lost before use, the recipient must contact the data provider. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

The credential file must be stored in a secure location and should not be shared outside the group of users who should have access to the shared data. Databricks recommends using a password manager for sharing within an organization. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Reading Shared Data

### Using a Credential File (Bearer Tokens)

When data is shared using the Databricks-to-Open sharing protocol with bearer tokens, the recipient uses the downloaded credential file to authenticate to the data provider's account. Access persists as long as the underlying token is valid and the provider continues to share the data. Tokens are valid for a maximum of one year after creation. Updates to the data are available in near real time. The recipient can read and make copies of the shared data but cannot modify the source data. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

### Using OIDC Federation

When data is shared using the Databricks-to-Open sharing protocol with OIDC federation, the recipient uses the URL sent to them to authenticate to the data provider's account. Access persists as long as the provider continues to share the data. Updates are available in near real time, and the recipient can read and make copies of the shared data but cannot modify the source data. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

### Using Databricks-to-Databricks Sharing

When data is shared using the Databricks-to-Databricks model, no credential file is required. Databricks manages the secure connection, and the shared data is automatically discoverable in the recipient's Databricks workspace. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Audit and Monitoring

If the data recipient has access to a Databricks workspace, they can use Databricks audit logs to understand who in their organization is accessing which data using OpenSharing. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The open standard for secure data sharing
- Data Provider — The entity that shares data with recipients
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution required for Databricks-to-Databricks sharing
- [Delta Sharing](/concepts/delta-sharing.md) — The underlying protocol for data sharing
- Credential File — The authentication file used in Databricks-to-Open sharing

## Sources

- access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md

# Citations

1. [access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md](/references/access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws-7bb360b8.md)
