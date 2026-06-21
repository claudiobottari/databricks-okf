---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4422848399f80b4810a74e3a85aaff036f518814ff348281d138f7757350c56d
  pageDirectory: concepts
  sources:
    - create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-sharing-open-sharing
    - DSOS
    - Delta Sharing / OpenSharing
    - Create Shares for OpenSharing
    - Data Shares for OpenSharing
  citations:
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
title: Delta Sharing Open Sharing
description: An authentication flow for sharing data via Delta Sharing with recipients who do not have access to a Unity Catalog-enabled Databricks workspace, using either bearer tokens or OIDC federation.
tags:
  - delta-sharing
  - authentication
  - data-sharing
timestamp: "2026-06-18T11:14:59.186Z"
---

# Delta Sharing Open Sharing

**Delta Sharing Open Sharing** is an authentication flow in [Delta Sharing](/concepts/delta-sharing.md) that enables data providers to securely share data with recipients who do not have access to a Unity Catalog–enabled Databricks workspace. Open sharing uses either bearer tokens or OpenID Connect (OIDC) token federation as the authentication mechanism. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Overview

In a Delta Sharing Open Sharing arrangement, the data provider creates a **recipient object** in their Unity Catalog [Metastore](/concepts/metastore.md). When using the bearer token method, Databricks generates a token, a credential file that includes the token, and an activation link. The provider shares the activation link with the recipient over a secure channel. The recipient accesses the link, downloads the credential file, and uses it to authenticate and read the shared data. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

The OIDC federation flow is an alternative to the bearer token flow and offers advantages in security and convenience. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Authentication Flows

Two authentication flows are available for Open Sharing recipients:

- **Bearer token (TOKEN)** – The provider selects the bearer token method when creating the recipient. Databricks generates a token and an activation link. The recipient object has `authentication_type = 'TOKEN'`. Tokens can be refreshed and revoked as needed. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]
- **OIDC token federation** – An alternative to bearer tokens that uses federated identity. For details, see [Enable OpenID Connect (OIDC) federation for OpenSharing recipients](/concepts/oidc-federation-for-opensharing.md). ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Provider Workflow

### Creating a Recipient

To create a recipient for Open Sharing, the provider must be a [Metastore](/concepts/metastore.md) admin or have the `CREATE RECIPIENT` privilege on the Unity Catalog [Metastore](/concepts/metastore.md) where the data is registered. The provider can use Catalog Explorer, the Databricks Unity Catalog CLI, or the `CREATE RECIPIENT` SQL command. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

When creating the recipient, the provider:

1. Selects **Open** as the recipient type.
2. Chooses **Token** as the authentication method.
3. Optionally sets a **Token lifetime** expiration time (in seconds, minutes, hours, or days from creation). Tokens are valid for a maximum of one year after creation.
4. Optionally adds a comment and custom **Recipient properties**.
5. Clicks **Create** and copies the activation link.

If the expiration field is left blank, the token lifetime defaults to the [Metastore](/concepts/metastore.md)'s recipient token lifetime configuration. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Granting Access to Shares

After creating the recipient and creating shares, the provider grants the recipient access to those shares. Permissions required: [Metastore](/concepts/metastore.md) admin, or delegated permissions (`USE SHARE` + `SET SHARE PERMISSION` or share owner) AND (`USE RECIPIENT` or recipient owner). ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Token Expiration and Management

- All Databricks-to-Open sharing recipient tokens issued before December 8, 2025, with expiration dates after December 8, 2026, or with no expiration date, automatically expire on December 8, 2026. Providers should review integrations and renew tokens as needed. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]
- A recipient can have at most two tokens at any time: an active token and a rotated token (one that has been set to expire and replaced by the active token). Rotating a token while a rotated token is still valid results in an error. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Rotating a Recipient's Token

Token rotation is used when the existing token is about to expire, the activation link is lost or compromised, the credential is corrupted or compromised, or the [Metastore](/concepts/metastore.md)'s recipient token lifetime has been modified. To rotate, the provider uses Catalog Explorer or the CLI. After rotation, a new activation link is generated and must be shared with the recipient over a secure channel. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

When rotating, the provider can set `existing-token-expire-in-seconds` to control when the old token expires. Databricks recommends a short period to minimize the time during which the recipient has two active tokens. If compromise is suspected, set the value to `0` to expire the existing token immediately. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

If the recipient's existing activation URL has never been accessed, rotating invalidates that URL and replaces it with a new one. If all tokens have expired, rotating replaces the activation URL with a new one. Databricks recommends promptly rotating or dropping a recipient whose token has expired. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Modifying the Recipient Token Lifetime

The default recipient token lifetime for a Unity Catalog [Metastore](/concepts/metastore.md) can be modified by an account admin using the account console or CLI. The change does not automatically apply to existing recipients; to apply the new lifetime to a specific recipient, the provider must rotate that recipient's token. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Activation Link

After creation, the provider retrieves the activation link using Catalog Explorer, the CLI, or the `DESCRIBE RECIPIENT` SQL command. Permissions required: [Metastore](/concepts/metastore.md) admin, `USE RECIPIENT` privilege, or recipient object owner. If the recipient has already downloaded the credential file, the activation link is not returned. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

The provider must securely share the activation link and accompanying instructions with the recipient. Recipients should treat the downloaded credential as a secret and must not share it outside their organization. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Security Considerations

- If a recipient activation URL is inadvertently sent to the wrong person or over an insecure channel, Databricks recommends:
  1. Revoke the recipient's access to the share.
  2. Rotate the recipient and set `existing-token-expire-in-seconds` to `0`.
  3. Share the new activation URL with the intended recipient over a secure channel.
  4. After the activation URL has been accessed, grant the recipient access to the share again.
- In extreme situations, instead of rotating the token, the provider may drop and re-create the recipient. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Recipient Steps

After receiving the activation link, the recipient:

1. Accesses the link.
2. Downloads the credential file.
3. Uses the credential file to authenticate and get read access to the shared tables.

If the recipient imported the credential as a provider object in Unity Catalog, they must update the provider object with the Databricks REST API when the token is rotated. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) – The open protocol for secure data sharing.
- [Unity Catalog](/concepts/unity-catalog.md) – The data governance layer that manages recipient objects.
- [OIDC Federation for OpenSharing](/concepts/oidc-federation-for-opensharing.md) – The alternative authentication flow for open sharing recipients.
- Recipient Object – The object created in Unity Catalog to represent a data consumer.
- Share – A logical container for the data assets being shared.
- Credential File – The file containing the bearer token that recipients use to authenticate.

## Sources

- create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md

# Citations

1. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
