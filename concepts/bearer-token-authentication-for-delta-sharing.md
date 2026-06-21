---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ff6f6a91a0e42bbc6a15b3da5762e22ec2ce6f53bd4ef9fc19a34b172a19ef5a
  pageDirectory: concepts
  sources:
    - create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - bearer-token-authentication-for-delta-sharing
    - BTAFDS
    - Bearer Token Authentication (Delta Sharing)
    - Bearer Token Authentication in Delta Sharing
    - Bearer Token Authentication
    - Bearer Token Authentication (Delta Sharing)|bearer token authentication flow
    - Bearer Tokens for Delta Sharing
    - Bearer token (Delta Sharing)
  citations:
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
title: Bearer Token Authentication for Delta Sharing
description: A token-based authentication method for Open Sharing recipients where Databricks generates a bearer token, a credential file, and an activation link for the recipient to download credentials and access shared data.
tags:
  - delta-sharing
  - authentication
  - bearer-token
timestamp: "2026-06-19T17:56:47.007Z"
---

# Bearer Token Authentication for Delta Sharing

**Bearer Token Authentication for Delta Sharing**, also known as the **Databricks-to-Open** sharing bearer token flow, is one of two authentication methods available for creating "Open" recipient objects in Unity Catalog. It provides a mechanism for data providers to share data with recipients who do not have access to a Unity Catalog-enabled Databricks workspace. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## How It Works

In the bearer token flow, the data provider creates a recipient object in Unity Catalog and selects the bearer token authentication method. Databricks generates a token, a credential file containing the token, and an activation link that the provider shares with the recipient. The recipient object has an authentication type of `TOKEN`. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

The recipient accesses the activation link, downloads the credential file, and uses it to authenticate and obtain read access to the tables included in the shares they have been granted access to. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Alternative Authentication Methods

The [OIDC Token Federation](/concepts/oidc-token-federation-delta-sharing.md) flow is an alternative to the bearer token flow that offers advantages in security and convenience over the bearer token flow. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Creating a Recipient

To create a recipient for Databricks-to-Open sharing using bearer tokens, you can use Catalog Explorer, the Databricks Unity Catalog CLI, or the `CREATE RECIPIENT` SQL command in a Databricks notebook or the Databricks SQL query editor. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

**Required permissions**: [Metastore](/concepts/metastore.md) admin or a user with the `CREATE RECIPIENT` privilege for the Unity Catalog [Metastore](/concepts/metastore.md) where the data to be shared is registered. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Using Catalog Explorer

1. In your Databricks workspace, click **Catalog**.
2. At the top of the Catalog pane, click the gear icon and select **OpenSharing**.
3. On the **Shared by me** tab, click **New recipient**.
4. Enter the **Recipient name**.
5. For **Recipient type**, select **Open**.
6. Select **Token**.
7. Optionally, set the **Token lifetime** expiration time. Leave **Set expiration** selected to set an expiration time. Tokens are valid for a maximum of one year after creation.
8. Optionally, enter a comment.
9. Click **Create**.
10. Copy the activation link.

### Managing Token Lifetime

When creating a recipient, you can optionally set a token lifetime (in seconds, minutes, hours, or days from recipient creation time). If you select **Set expiration** and leave the field blank, the token lifetime defaults to the recipient token lifetime value set in the [Metastore](/concepts/metastore.md) configuration. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

To modify the default recipient token lifetime for a Unity Catalog [Metastore](/concepts/metastore.md), you can use Catalog Explorer or the Databricks Unity Catalog CLI with account admin permissions. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Getting the Activation Link

To retrieve the activation link for an existing recipient, you can use Catalog Explorer, the Databricks Unity Catalog CLI, or the `DESCRIBE RECIPIENT` SQL command. If the recipient has already downloaded the credential file, the activation link is not returned or displayed. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

**Required permissions**: [Metastore](/concepts/metastore.md) admin, user with the `USE RECIPIENT` privilege, or the recipient object owner. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Granting Share Access

After creating the recipient and creating shares, you can grant the recipient access to those shares using Catalog Explorer, the Databricks Unity Catalog CLI, or the `GRANT ON SHARE` SQL command. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

**Required permissions**: One of the following: ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

- [Metastore](/concepts/metastore.md) admin
- Delegated permissions or ownership on both the share and the recipient objects (`USE SHARE` + `SET SHARE PERMISSION` or share owner) AND (`USE RECIPIENT` or recipient owner)

## Managing Recipient Tokens

### Token Management

At any given time, a recipient can have at most two tokens: an active token and a rotated token. The rotated token is one that has been set to expire and be replaced by the active token. Until the rotated token expires, attempting to rotate the token again results in an error. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Security Considerations

Databricks recommends setting the `--existing-token-expire-in-seconds` to a relatively short period that gives the recipient organization time to access the new activation URL while minimizing the time that the recipient has two active tokens. If suspecting compromise, Databricks recommends forcing the token to expire immediately. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

If an activation URL is inadvertently sent to the wrong person or over an insecure channel, Databricks recommends: ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

1. Revoke the recipient's access to the share.
2. Rotate the recipient and set `--existing-token-expire-in-seconds` to `0`.
3. Share the new activation URL with the intended recipient over a secure channel.
4. After the activation URL has been accessed, grant the recipient access to the share again.

### Token Expiration

All Databricks-to-Open sharing recipient tokens issued before December 8, 2025, with expiration dates after December 8, 2026, or with no expiration date, automatically expire on December 8, 2026. Databricks recommends reviewing integrations and renewing tokens as needed to avoid breaking changes after this date. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md)
- [Open Sharing](/concepts/opensharing.md)
- [OIDC Token Federation](/concepts/oidc-token-federation-delta-sharing.md)
- [Recipient Objects](/concepts/recipient-object-delta-sharing.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- Credential Management

## Sources

- create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md

# Citations

1. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
