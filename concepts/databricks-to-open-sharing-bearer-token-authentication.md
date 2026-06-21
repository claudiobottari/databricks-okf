---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 248e3fcec291183fd680a12d3f1214005b0cfbc696d31e1b3eaa688de08b50dc
  pageDirectory: concepts
  sources:
    - create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-to-open-sharing-bearer-token-authentication
    - DS(TA
  citations:
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
title: Databricks-to-Open Sharing (Bearer Token Authentication)
description: An authentication flow in Delta Sharing where data providers create recipient objects using bearer tokens for non-Databricks users to access shared data without a Unity Catalog workspace.
tags:
  - delta-sharing
  - authentication
  - databricks
timestamp: "2026-06-19T14:30:25.245Z"
---

# Databricks-to-Open Sharing (Bearer Token Authentication)

**Databricks-to-Open Sharing (Bearer Token Authentication)** is an authentication flow within [Delta Sharing](/concepts/delta-sharing.md) that allows data providers to share data with recipients who do not have access to a Unity Catalog-enabled Databricks workspace. The recipient authenticates using a bearer token embedded in a credential file. This flow, together with [OIDC federation](/concepts/oidc-federation-policy.md), is called _open sharing_.  ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## How It Works

The data provider creates a [recipient object](/concepts/opensharing-recipient-object.md) in their [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) and selects the bearer token method. Databricks generates a token, a credential file containing the token, and an activation link. The recipient accesses the activation link to download the credential file, which they use to authenticate and read the shared tables. The recipient object has an authentication type of `TOKEN`. Providers can refresh or revoke the token as needed.  ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

> **Important**: All Databricks-to-Open sharing recipient tokens issued before December 8, 2025, with expiration dates after December 8, 2026, or with no expiration date, automatically expire on December 8, 2026. Providers should review their integrations and renew tokens as needed to avoid breaking changes after this date.  ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Creating a Recipient

To create a recipient for bearer token authentication, use Catalog Explorer, the Databricks Unity Catalog CLI, or the `CREATE RECIPIENT` SQL command. Required permissions: [Metastore](/concepts/metastore.md) admin or `CREATE RECIPIENT` privilege on the [Metastore](/concepts/metastore.md).  ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

When creating a recipient, the provider:
- Enters a recipient name.
- Selects **Open** as the recipient type.
- Selects **Token** as the authentication method.
- Optionally sets a token lifetime (expiration time). Tokens are valid for a maximum of one year after creation. If left blank, the lifetime defaults to the [Metastore](/concepts/metastore.md) configuration.
- Optionally adds a comment and custom recipient properties.

After creation, the activation link is generated and must be shared with the recipient over a secure channel.  ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Getting the Activation Link

The activation link can be retrieved using Catalog Explorer, the CLI, or the `DESCRIBE RECIPIENT` SQL command. Required permissions: [Metastore](/concepts/metastore.md) admin, `USE RECIPIENT` privilege, or recipient object owner. Once the recipient has downloaded the credential file, the activation link is no longer displayed.  ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Sending Connection Information

Providers must send the activation link and a link to instructions for using it to the recipient over a secure channel. The credential file can be downloaded only once. Recipients should treat the credential as a secret and must not share it outside their organization. If there are concerns about insecure handling, the provider can rotate the credential immediately.  ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Managing Recipient Tokens

### Token Rotation

Rotating a token sets the existing token to expire and generates a new token with a new activation URL. Rotation is necessary when:
- The current token is about to expire.
- The activation link is lost or compromised.
- The credential is corrupted, lost, or compromised after download.
- The metastore’s recipient token lifetime is modified.  ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

A recipient can have at most two tokens: an active token and a rotated token (set to expire). The `--existing-token-expire-in-seconds` option controls how quickly the old token expires. Setting it to `0` expires it immediately. Databricks recommends using a short expiration period to minimize the overlap of two active tokens. If the existing token is suspected compromised, force immediate expiration.  ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

If an activation URL is accidentally shared with the wrong person, the provider should:
1. Revoke the recipient’s access to the share.
2. Rotate the recipient with `--existing-token-expire-in-seconds` set to `0`.
3. Share the new activation link with the intended recipient over a secure channel.
4. Grant access again after the activation URL has been accessed.  ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Updating Token Lifetime for an Existing Recipient

The recipient token lifetime for an existing recipient can be updated via Catalog Explorer by the recipient object owner. The change takes effect immediately for that recipient.  ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Modifying the Default Recipient Token Lifetime for the [Metastore](/concepts/metastore.md)

An account admin can modify the default recipient token lifetime for the entire [Metastore](/concepts/metastore.md) using Catalog Explorer or the CLI. This change does **not** automatically update existing recipients; their tokens must be rotated to apply the new lifetime.  ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Security Considerations

- The credential file is downloaded only once; after that, the activation link is unavailable.
- Providers should use secure channels for sharing activation links.
- If a credential is compromised, rotate the token and revoke share access immediately.
- In extreme situations, the recipient can be dropped and re-created.  ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Alternative: OIDC Federation

The [OIDC federation](/concepts/oidc-federation-policy.md) flow is an alternative to bearer token authentication that offers advantages in security and convenience.  ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md)
- [Open Sharing](/concepts/opensharing.md)
- [OIDC federation](/concepts/oidc-federation-policy.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- Recipient object
- [Credential file](/concepts/credential-file-opensharing.md)
- [IP access lists for OpenSharing](/concepts/ip-access-lists-for-opensharing-recipients.md)

## Sources

- create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md

# Citations

1. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
