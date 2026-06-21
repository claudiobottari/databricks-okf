---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 43ba121d7494fe343b53d6ddb6e6c1a0f9356516779744dbfaf98279be8d3056
  pageDirectory: concepts
  sources:
    - access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-provider-and-data-recipient-roles
    - data recipient roles and Data provider
    - DPADRR
    - Data Provider vs Data Recipient
  citations:
    - file: access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
title: Data provider and data recipient roles
description: In OpenSharing, a data provider (a Databricks user) shares data with a data recipient (a person or group outside their organization), with distinct responsibilities and workflows for each.
tags:
  - roles
  - data-sharing
  - databricks
timestamp: "2026-06-19T08:49:59.849Z"
---

# Data Provider and Data Recipient Roles

**Data provider** and **data recipient** are the two primary roles in [OpenSharing](/concepts/opensharing.md), an open standard for secure data sharing. A data provider shares data with a data recipient, who accesses that data from outside the provider's organization. The roles are complementary: every shared dataset has one provider and one or more recipients. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Overview

In the OpenSharing model on Databricks, the **data provider** is a Databricks user who configures and distributes data to external parties. The **data recipient** is a person or group outside the provider's organization who receives access to the shared data. The shared data is not provided by Databricks directly but by data providers running on Databricks. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Data Provider Responsibilities

The data provider performs the following tasks:

1. **Creates a recipient** in their Databricks account to represent the recipient organization and its users who will access the data. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]
2. **Creates a share**, which is a representation of the tables, volumes, views, and partitions to be shared with the recipient. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]
3. **Sends access credentials** to the recipient over a secure channel. The method varies by sharing model:
   - In the [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md) model, the provider receives a sharing identifier from the recipient's workspace and uses it to create a secure connection. No credential file is needed. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]
   - In the [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md) model, the provider sends an activation URL or a portal link to the recipient. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

The provider manages token expiration and rotation. Tokens are valid for a maximum of one year after creation. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Data Recipient Responsibilities

The data recipient's responsibilities depend on which sharing model the provider uses.

### In the Databricks-to-Databricks Model

The recipient must be a user on a Databricks workspace enabled for [Unity Catalog](/concepts/unity-catalog.md). A member of the recipient's team provides the data provider with a unique identifier for their Unity Catalog [Metastore](/concepts/metastore.md), in the format `<cloud>:<region>:<uuid>` (for example, `aws:eu-west-1:b0c978c8-3e68-4cdf-94af-d05c120ed1ef`). After the provider creates the share, the shared data becomes automatically discoverable in the recipient's workspace, and the recipient can read and manage it without any credential file. If necessary, a member of the recipient's team configures granular access control on that data. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

### In the Databricks-to-Open Sharing Model

The recipient can use any tool to access the shared data. The recipient:

1. Receives an activation URL or portal link from the provider over a secure channel. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]
2. Follows the link to download a credential file or URL. Both bearer tokens and OAuth Client Credentials are supported. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]
3. Stores the credential file in a secure location and does not share it outside the authorized group. Databricks recommends using a password manager if sharing is necessary within the organization. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

The activation link can be used only once to download the credential file. If the recipient loses the activation link before using it, they must contact the data provider. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Key Considerations

- **Read-only access**: Recipients can read and make copies of shared data but cannot modify the source data. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]
- **Near-real-time updates**: Updates made by the provider are available to the recipient in near real time. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]
- **Audit logging**: If the recipient has access to a Databricks workspace, they can use Databricks audit logs to understand who in their organization is accessing which data using OpenSharing. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]
- **Data collection notice**: Databricks may collect information about data recipients' use of and access to shared data (including identifying any individual or company who accesses the data using the credential file) and may share it with the applicable data provider. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The open standard underlying these roles
- [Delta Sharing](/concepts/delta-sharing.md) — The broader data sharing framework
- [Unity Catalog](/concepts/unity-catalog.md) — Required for Databricks-to-Databricks sharing recipients
- [Sharing Identifier](/concepts/sharing-identifier.md) — The [Metastore](/concepts/metastore.md) identifier used in Databricks-to-Databricks sharing
- [Credential file](/concepts/credential-file-opensharing.md) — Used for Databricks-to-Open sharing authentication

## Sources

- access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md

# Citations

1. [access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md](/references/access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws-7bb360b8.md)
