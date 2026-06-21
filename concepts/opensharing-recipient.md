---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 78dd21c4a48a6dedbc414671eea828bdcc206a4febfeb9ab6452f3dc4cb5cff6
  pageDirectory: concepts
  sources:
    - access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
    - create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
    - manage-data-recipients-for-opensharing-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - opensharing-recipient
    - Open Sharing Recipient
    - OpenSharing Recipients
    - OpenSharing recipient setup
    - Open Recipients
    - Open recipient
  citations:
    - file: create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
    - file: access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
title: OpenSharing Recipient
description: A person or group outside the data provider's organization who receives access to shared data; represented as a 'recipient' object in the provider's Databricks account.
tags:
  - data-sharing
  - access-control
  - databricks
timestamp: "2026-06-19T21:56:19.940Z"
---

# OpenSharing Recipient

**OpenSharing Recipient** is a named object in [Unity Catalog](/concepts/unity-catalog.md) that represents the identity of a user or group of users who consume shared data via [Delta Sharing](/concepts/delta-sharing.md). The recipient object is created by a data provider to control how recipients access shared datasets. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Overview

An OpenSharing recipient is a representation of the person or organization that will receive access to shared data. A data provider running on Databricks creates a _recipient_ in their account to represent the data consumer and their users. The way recipients are created differs depending on whether the recipient has access to a Databricks workspace enabled for Unity Catalog. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Recipient Models

There are two primary recipient models in OpenSharing:

### Databricks-to-Databricks Recipient

In the **Databricks-to-Databricks model**, the recipient must be a user on a Databricks workspace that is enabled for Unity Catalog. A member of the recipient's team provides the data provider with a unique sharing identifier for their Unity Catalog [Metastore](/concepts/metastore.md), and the data provider uses that to create a secure sharing connection. The shared data becomes automatically discoverable in the recipient's workspace, and no credential file is required. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

The sharing identifier is a string in the format `<cloud>:<region>:<uuid>`, for example `aws:us-west-2:19a84bee-54bc-43a2-87de-023d0ec16016`. Recipients can obtain this identifier using Catalog Explorer, the `CURRENT_METASTORE` SQL function, or the Databricks Unity Catalog CLI. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

### Databricks-to-Open Sharing Recipient

In the **Databricks-to-Open sharing model**, the recipient can use any tool (including Databricks) to access the shared data. This model uses token-based authentication with either bearer tokens or OAuth federation. The data provider sends the recipient an activation URL or portal link over a secure channel. The recipient follows the URL to download a credential file or receive a URL that authenticates access to the shared data. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Creating a Recipient

### Requirements

To create a recipient, you must have the `CREATE RECIPIENT` privilege for the Unity Catalog [Metastore](/concepts/metastore.md) where the data you want to share is registered. You must create the recipient using a Databricks workspace that has that Unity Catalog [Metastore](/concepts/metastore.md) attached. If using a Databricks notebook, your compute must use Databricks Runtime 11.3 LTS or above with standard or dedicated access mode. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

### Creating a Databricks-to-Databricks Recipient

To create a recipient for Databricks-to-Databricks sharing, you can use Catalog Explorer, the Databricks Unity Catalog CLI, or the `CREATE RECIPIENT` SQL command in a Databricks notebook or the Databricks SQL query editor. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

**Step 1: Request the recipient's sharing identifier**

Ask a recipient user to send you the sharing identifier for the Unity Catalog [Metastore](/concepts/metastore.md) attached to the workspaces where they will work with the shared data. The sharing identifier is a string in the format `<cloud>:<region>:<uuid>`. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

The recipient can find the identifier using:
- **Catalog Explorer**: Navigate to Catalog, click the gear icon, select **OpenSharing**, then on the **Shared with me** tab, click the sharing organization name and select **Copy sharing identifier**. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]
- **SQL**: Use the `CURRENT_METASTORE` function in a Databricks notebook or SQL query. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]
- **CLI**: Use the Databricks Unity Catalog CLI. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

**Step 2: Create the recipient**

Using Catalog Explorer:
1. Click **Catalog**, then the gear icon, and select **OpenSharing**.
2. On the **Shared by me** tab, click **New recipient**.
3. Enter the **Recipient name**.
4. For **Recipient type**, select **Databricks**.
5. Enter the recipient's **Sharing identifier** in the format `<cloud>:<region>:<uuid>`.
6. (Optional) Enter a comment.
7. Click **Create**. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

The recipient is created with the `authentication_type` of `DATABRICKS`. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Recipient Object

The data provider creates two objects to enable sharing:
1. A **recipient** in their Databricks account to represent the data consumer and their users.
2. A **share**, which represents the tables, volumes, and views to be shared with the recipient. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Accessing Shared Data

### Databricks-to-Databricks Recipient Access

Recipients access data by connecting to their Databricks workspace, where shared data is automatically discoverable. No credential file is needed. The data shared with this recipient can be accessed only on the specific Unity Catalog [Metastore](/concepts/metastore.md) identified by the sharing identifier. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

### Open Sharing Recipient Access

Recipients use the credential file or OIDC federation URL to authenticate and read shared data. Access persists as long as the underlying token is valid and the provider continues to share the data. Recipients can read and make copies of the shared data but cannot modify the source data. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for secure data sharing
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution for Databricks
- [Sharing Identifier](/concepts/sharing-identifier.md) — The unique identifier for a Unity Catalog [Metastore](/concepts/metastore.md)
- Data Provider — The entity sharing data via OpenSharing
- [Open Sharing](/concepts/opensharing.md) — The Databricks-to-Open sharing model using token-based authentication
- Credential File — The authentication file used in the open sharing model
- OIDC Federation — Open ID Connect federation for user and machine authentication

## Sources

- create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
- access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
- manage-data-recipients-for-opensharing-databricks-on-aws.md

# Citations

1. [create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md](/references/create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws-a4778c5e.md)
2. [access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md](/references/access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws-7bb360b8.md)
