---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3cabbe0074c54b4873e5085f2ef408ee94de0a921ba992c898c399700aecf133
  pageDirectory: concepts
  sources:
    - create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - open-sharing-databricks-to-open-sharing
    - OS(S
  citations:
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
title: Open Sharing (Databricks-to-Open Sharing)
description: An authentication flow in Databricks Delta Sharing that allows data providers to share data with recipients who do not have access to a Unity Catalog-enabled Databricks workspace, using bearer tokens or OIDC federation.
tags:
  - delta-sharing
  - authentication
  - data-sharing
timestamp: "2026-06-19T17:56:43.948Z"
---

# Open Sharing (Databricks-to-Open Sharing)

**Open Sharing** (also called **Databricks-to-Open sharing**) is a [Delta Sharing](/concepts/delta-sharing.md) authentication flow that allows data providers in a [Unity Catalog](/concepts/unity-catalog.md)–enabled Databricks workspace to share data with recipients who do **not** have access to a Unity Catalog [Metastore](/concepts/metastore.md). Open Sharing uses either bearer tokens or OIDC token federation for authentication. This page describes the bearer token flow. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## How it works

In the bearer token flow, the data provider creates a [Recipient](/concepts/data-recipient.md) object in their Unity Catalog [Metastore](/concepts/metastore.md) and selects the token authentication method. Databricks generates a bearer token, a credential file that contains the token, and an activation link. The recipient uses the activation link to download the credential file and then uses that file to authenticate and gain read access to the tables included in the shares granted to them. The recipient object is created with `authentication_type` set to `TOKEN`. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

The OIDC federation flow is an alternative that offers security and convenience advantages over the bearer token flow. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Create the recipient

To create a recipient for Databricks-to-Open sharing, use Catalog Explorer, the Databricks Unity Catalog CLI, or the `CREATE RECIPIENT` SQL command. The required permission is [Metastore](/concepts/metastore.md) admin or `CREATE RECIPIENT` privilege on the [Metastore](/concepts/metastore.md) where the shared data is registered. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Using Catalog Explorer

Navigate to **Catalog** > gear icon > **OpenSharing** > **Shared by me** > **New recipient**. Enter a name, select **Open** as recipient type, choose **Token**, optionally set a token lifetime expiration, add a comment, and create. The activation link is displayed after creation. You can also add custom **Recipient properties**. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Token lifetime

Tokens are valid for a maximum of one year after creation. If you enable expiration but leave the field blank, the lifetime defaults to the metastore-level recipient token lifetime value. When the recipient downloads the credential file, the activation link is no longer returned. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Get the activation link

To retrieve the activation link after creation, use Catalog Explorer (under **Recipients** > select recipient > copy **Activation link**), the `DESCRIBE RECIPIENT` SQL command, or the Unity Catalog CLI. The activation link is not displayed once the recipient has already downloaded the credential file. Required permissions: [Metastore](/concepts/metastore.md) admin, `USE RECIPIENT` privilege, or recipient object owner. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Send the recipient their connection information

Share the activation link and a link to instructions for using it over a secure channel. The credential file can be downloaded only once. Recipients must treat the downloaded credential as a secret and not share it outside their organization. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Grant share access

After creating the recipient and creating shares, the provider grants the recipient access to those shares using Catalog Explorer, the Unity Catalog CLI, or the `GRANT ON SHARE` SQL command. Required permissions: [Metastore](/concepts/metastore.md) admin, or delegated permissions on both the share and the recipient objects (`USE SHARE` + `SET SHARE PERMISSION` or share owner) AND (`USE RECIPIENT` or recipient owner). ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Manage recipient tokens

### When to rotate a token

Rotate a recipient's token (set the existing token to expire and issue a new one) in the following circumstances:

- The existing token is about to expire.
- The activation URL is lost or compromised.
- The credential is corrupted, lost, or compromised after download.
- The metastore-level recipient token lifetime is modified. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Security considerations for tokens

A recipient can have at most two tokens at any time: an active token and a rotated token (set to expire). Attempting to rotate again before the rotated token expires results in an error. When rotating, you can optionally set `--existing-token-expire-in-seconds` to the number of seconds before the existing token expires. Setting it to `0` forces immediate expiration. Databricks recommends a short overlap period unless compromise is suspected. If an activation URL has never been accessed, rotating invalidates it and replaces it. If all tokens have expired, rotating replaces the activation URL. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

If a recipient activation URL is inadvertently sent to the wrong person or over an insecure channel, Databricks recommends: revoking share access, rotating with immediate expiration, sharing the new activation URL over a secure channel, then regranting access after activation. In extreme cases, drop and re-create the recipient. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Rotate a token

In Catalog Explorer, go to **OpenSharing** > **Shared by me** > **Recipients** > select recipient > under **Token management**, click **Rotate**, set expiration preference, and create. Share the new activation link. Required permission: recipient object owner. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Update recipient token lifetime

To change the lifetime of an existing token, use Catalog Explorer: select the recipient, under **Token management** click **Update**, set the new lifetime, and save. Required permission: recipient object owner. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Modify the metastore-level recipient token lifetime

Account admins can change the default recipient token lifetime for the [Metastore](/concepts/metastore.md) in the account console under **Catalog** > [Metastore](/concepts/metastore.md) name > **OpenSharing recipient token lifetime** > **Edit**. The change does not apply automatically to existing recipients; their tokens must be rotated to adopt the new lifetime. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Important notice about token expiration

All Databricks-to-Open sharing recipient tokens issued before December 8, 2025, with expiration dates after December 8, 2026, or with no expiration date, automatically expire on December 8, 2026. Providers should review integrations and renew tokens as needed. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Additional resources

- [Manage access to OpenSharing data shares (for providers)](https://docs.databricks.com/aws/en/delta-sharing/grant-access)
- [Manage data recipients for OpenSharing](https://docs.databricks.com/aws/en/delta-sharing/manage-recipients)
- [Restrict OpenSharing recipient access using IP access lists](https://docs.databricks.com/aws/en/delta-sharing/access-list)

## Related concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for sharing data across platforms
- [Recipient](/concepts/data-recipient.md) — Object representing a data consumer in Delta Sharing
- [Unity Catalog](/concepts/unity-catalog.md) — The [Metastore](/concepts/metastore.md) that manages shares, recipients, and policies
- [Bearer Token](/concepts/oidc-vs-bearer-token-authentication.md) — Authentication method for open sharing recipients
- [OIDC federation](/concepts/oidc-federation-policy.md) — Alternative, more secure authentication flow for open sharing
- [OpenSharing](/concepts/opensharing.md) — The UI and management interface in Databricks
- Provider — The Databricks workspace that shares data (recipient side)

## Sources

- create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md

# Citations

1. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
