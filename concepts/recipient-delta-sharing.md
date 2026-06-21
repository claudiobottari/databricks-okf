---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b27656d29942bc66a2403656955b232343952140715527040fe10b03329b3e0a
  pageDirectory: concepts
  sources:
    - create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - recipient-delta-sharing
    - R(S
    - Recipient (Data Sharing)
  citations:
    - file: create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
title: Recipient (Delta Sharing)
description: A named object in OpenSharing that represents the identity of a user or group of users who consume shared data, created with a specific authentication type.
tags:
  - databricks
  - delta-sharing
  - recipient
timestamp: "2026-06-19T14:37:12.981Z"
---

# Recipient (Delta Sharing)

**Recipient** is a named object in [Delta Sharing](/concepts/delta-sharing.md) (via Databricks [OpenSharing](/concepts/opensharing.md)) that represents the identity of a user or group of users who consume shared data. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

The method for creating a recipient differs based on whether the consumer has access to a [Unity Catalog](/concepts/unity-catalog.md)–enabled Databricks workspace:

- **Databricks-to-Databricks sharing** – The recipient has access to a Unity Catalog–enabled workspace and authenticates via a Databricks-managed secure connection. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]
- **Databricks-to-Open sharing** – The recipient does not have a Unity Catalog–enabled workspace. The provider manages a secure connection using token-based authentication (bearer tokens or OAuth federation). ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

This page focuses on the first scenario: creating a recipient for Databricks-to-Databricks sharing.

## Requirements

To create a recipient you must:

- Have the `CREATE RECIPIENT` privilege on the Unity Catalog [Metastore](/concepts/metastore.md) where the data to be shared is registered. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]
- Use a Databricks workspace that has that [Metastore](/concepts/metastore.md) attached. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]
- If using a notebook, run on a compute resource with Databricks Runtime 11.3 LTS or above and standard or dedicated access mode. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Steps to create a Databricks-to-Databricks recipient

### 1. Obtain the recipient’s sharing identifier

Ask the recipient user to provide the **sharing identifier** for the Unity Catalog [Metastore](/concepts/metastore.md) attached to the workspace where they will consume the data. The identifier is a string in the format `<cloud>:<region>:<uuid>` (e.g., `aws:us-west-2:19a84bee-54bc-43a2-87de-023d0ec16016`). ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

The recipient can find this identifier using any of these methods:

- **Catalog Explorer** – In the **Shared with me** tab, the recipient clicks their Databricks sharing organization name and selects **Copy sharing identifier**. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]
- **SQL** – Run `SELECT CURRENT_METASTORE()` in a Databricks notebook or SQL query editor using Unity Catalog–capable compute. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]
- **CLI** – Use the Databricks Unity Catalog CLI to retrieve the [Metastore](/concepts/metastore.md) details. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

### 2. Create the recipient object

The provider creates the recipient object with an authentication type of `DATABRICKS`. The recipient’s sharing identifier is stored in the object, restricting access to only that specific [Metastore](/concepts/metastore.md). ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

You can create the recipient using any of these tools:

#### Catalog Explorer

1. Open **Catalog** in your workspace, click the gear icon and select **OpenSharing**.
2. Go to the **Shared by me** tab and click **New recipient**.
3. Enter a **Recipient name**, choose **Databricks** as the recipient type, and paste the sharing identifier.
4. (Optional) Add a comment or custom recipient properties, then click **Create**. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

#### SQL

Use the `CREATE RECIPIENT` SQL command:

```sql
CREATE RECIPIENT IF NOT EXISTS recipient_name
USING ID '<cloud>:<region>:<uuid>';
```

^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

#### CLI

Use the Databricks CLI with the `recipients create` subcommand, supplying the name and sharing identifier. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

### 3. (Optional) Add recipient properties

After creation, you can set custom key-value properties on the recipient (e.g., for access control or metadata). Properties are managed from the recipient’s **Overview** tab in Catalog Explorer, under **Recipient properties**. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Next steps

- [Grant access to shares for a recipient](/concepts/granting-share-access-to-recipients.md) – Grant the recipient access to one or more shares.
- [Manage data recipients for OpenSharing](/concepts/data-recipient-opensharing.md) – View, update, delete, manage properties, or restrict access with IP lists for an existing recipient.
- Create shares for OpenSharing – Create the shares to be granted to the recipient.

## Sources

- create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md

# Citations

1. [create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md](/references/create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws-a4778c5e.md)
