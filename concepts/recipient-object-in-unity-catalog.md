---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2b29fd5236b722c448fe79bad466566155fa58644d3fd67a69392065b496db65
  pageDirectory: concepts
  sources:
    - create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - recipient-object-in-unity-catalog
    - ROIUC
  citations:
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
title: Recipient Object in Unity Catalog
description: A Unity Catalog object representing a data recipient in Delta Sharing, created with authentication type TOKEN for bearer token flows, which controls access to shared data shares.
tags:
  - delta-sharing
  - unity-catalog
  - recipient-management
timestamp: "2026-06-19T17:57:47.587Z"
---

# Recipient Object in Unity Catalog

A **Recipient Object** in Unity Catalog represents a consumer that receives access to shared data through [Delta Sharing](/concepts/delta-sharing.md). It defines the identity and authentication method for a data recipient who can access data from a [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md).

## Overview

When a data provider wants to share data with a recipient who does not have access to a Unity Catalog-enabled Databricks workspace, the provider creates a recipient object in their Unity Catalog [Metastore](/concepts/metastore.md). The recipient object specifies how the recipient authenticates and includes the token or credential information needed to establish a secure connection. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

This authentication flow, along with [OIDC Token Federation](/concepts/oidc-token-federation-delta-sharing.md), is called **open sharing** (Databricks-to-Open sharing). ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## How It Works

The recipient creation and activation process follows these steps:

1. As a data provider, you create the recipient object in your Unity Catalog [Metastore](/concepts/metastore.md).
2. When you create the recipient object, you select the bearer token method. Databricks generates a token, a credential file that includes the token, and an activation link for you to share with the recipient. The recipient object has the authentication type of `TOKEN`.
3. The recipient accesses the activation link, downloads the credential file, and uses the credential file to authenticate and get read access to the tables included in the shares they have been granted access to. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Creating a Recipient

To create a recipient for Databricks-to-Open sharing, you can use Catalog Explorer, the Databricks Unity Catalog CLI, or the `CREATE RECIPIENT` SQL command in a Databricks notebook or the Databricks SQL query editor. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

**Required permissions**: [Metastore](/concepts/metastore.md) admin or user with the `CREATE RECIPIENT` privilege for the Unity Catalog [Metastore](/concepts/metastore.md) where the data you want to share is registered. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Using Catalog Explorer

1. In your Databricks workspace, click **Catalog**.
2. At the top of the **Catalog** pane, click the gear icon and select **OpenSharing** (or click **Share > OpenSharing** in the upper-right corner).
3. On the **Shared by me** tab, click **New recipient**.
4. Enter the **Recipient name**.
5. For **Recipient type**, select **Open**.
6. Select **Token**.
7. (Optional) Set the **Token lifetime** expiration time. Tokens are valid for a maximum of one year after creation.
8. (Optional) Enter a comment.
9. Click **Create**.
10. Copy the activation link and share it with the recipient over a secure channel.

## Token Lifetime and Expiration

When creating a recipient, you can optionally set a token lifetime expiration time in seconds, minutes, hours, or days from recipient creation time. If you select **Set expiration** and leave the field blank, the token lifetime defaults to the recipient token lifetime value set in the [Metastore](/concepts/metastore.md) configuration. Tokens are valid for a maximum of one year after creation. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Important Expiration Rule

All Databricks-to-Open sharing recipient tokens issued before December 8, 2025, with expiration dates after December 8, 2026, or with no expiration date, automatically expire on December 8, 2026. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Managing Recipient Tokens

You may need to rotate a recipient's token and generate a new activation URL in the following circumstances:

- When the existing recipient token is about to expire.
- If a recipient loses their activation URL or if it is compromised.
- If the credential is corrupted, lost, or compromised after it is downloaded by a recipient.
- When you modify the recipient token lifetime for a [Metastore](/concepts/metastore.md). ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Security Considerations

At any given time, a recipient can have at most two tokens: an active token and a rotated token. The rotated token is one that has been set to expire and be replaced by the active token. Until the rotated token expires, attempting to rotate the token again results in an error. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

Databricks recommends setting `--existing-token-expire-in-seconds` to a relatively short period that gives the recipient organization time to access the new activation URL while minimizing the time that the recipient has two active tokens. If you suspect the existing token is compromised, force it to expire immediately by setting the value to `0`. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Rotating a Token

To rotate a recipient's token, use Catalog Explorer or the Databricks Unity Catalog CLI. After rotation, share the new activation link with the recipient over a secure channel. If the recipient imported the credential as a provider object in Unity Catalog, they must update the provider object using the Databricks REST API. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Modifying Default Token Lifetime

To modify the default recipient token lifetime for your Unity Catalog [Metastore](/concepts/metastore.md), use Catalog Explorer or the Databricks Unity Catalog CLI. Note that the recipient token lifetime for existing recipients is not updated automatically when you change the default — you must rotate their token to apply the new lifetime. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

**Required permissions**: Account admin to modify the metastore-level default. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Activation Link

To retrieve a new recipient's activation link, use Catalog Explorer, the Databricks Unity Catalog CLI, or the `DESCRIBE RECIPIENT` SQL command. If the recipient has already downloaded the credential file, the activation link is not returned or displayed. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

**Required permissions**: [Metastore](/concepts/metastore.md) admin, user with the `USE RECIPIENT` privilege, or the recipient object owner. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Granting Access to Shares

Once you have created the recipient, you can grant them access to shares using Catalog Explorer, the Databricks Unity Catalog CLI, or the `GRANT ON SHARE` SQL command. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

**Required permissions**: One of the following:
- [Metastore](/concepts/metastore.md) admin.
- Delegated permissions or ownership on both the share and the recipient objects (`USE SHARE` + `SET SHARE PERMISSION` or share owner) AND (`USE RECIPIENT` or recipient owner). ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The underlying protocol for secure data sharing.
- [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) — The top-level container for data and sharing objects.
- Share Object in Unity Catalog — The object that defines a collection of tables to share.
- [Open Sharing](/concepts/opensharing.md) — The authentication flow for non-Databricks recipients.
- [OIDC Token Federation](/concepts/oidc-token-federation-delta-sharing.md) — An alternative authentication method for open sharing recipients.
- Provider Object in Unity Catalog — The reciprocal object for recipients who import shared data into Unity Catalog.

## Sources

- create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md

# Citations

1. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
