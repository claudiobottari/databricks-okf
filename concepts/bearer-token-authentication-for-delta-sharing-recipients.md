---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fbdbf5ca6e2da472888ce13c8707ec728e47f8621ec8d990b17082a1a3f9d5d0
  pageDirectory: concepts
  sources:
    - create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - bearer-token-authentication-for-delta-sharing-recipients
    - BTAFDSR
  citations:
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
title: Bearer Token Authentication for Delta Sharing Recipients
description: A Databricks-to-Open sharing authentication method where the provider creates a recipient object, Databricks generates a bearer token and credential file, and the recipient authenticates via an activation link.
tags:
  - delta-sharing
  - authentication
  - bearer-tokens
  - security
timestamp: "2026-06-18T11:15:01.516Z"
---

# Bearer Token Authentication for Delta Sharing Recipients

**Bearer token authentication** is one of the authentication methods used in [Delta Sharing](/concepts/delta-sharing.md) for *Databricks-to-Open sharing* (also called *open sharing*). In this flow, a data provider creates a recipient object in their [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md), selects the bearer token method, and Databricks generates a token, a credential file containing the token, and an activation link. The recipient uses the activation link to download the credential file, then presents the bearer token to authenticate and gain read access to the shared data. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

This method is intended for recipients who do not have access to a Unity Catalog‑enabled Databricks workspace. The alternative authentication flow for open sharing is [OIDC token federation](/concepts/oidc-token-federation-delta-sharing.md), which offers advantages in security and convenience. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## How the Bearer Token Flow Works

1. The data provider creates a recipient object in the Unity Catalog [Metastore](/concepts/metastore.md), selecting the **Token** authentication type. Databricks generates a bearer token, a credential file, and an activation link. The recipient object is created with `authentication_type = TOKEN`. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]
2. The provider shares the activation link with the intended recipient over a secure channel.
3. The recipient accesses the activation link, downloads the credential file once, and treats it as a secret. The credential file is used to authenticate and obtain read access to the shares the provider has granted to the recipient. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Creating a Bearer Token Recipient

Permissions required: [Metastore](/concepts/metastore.md) admin or a user with the `CREATE RECIPIENT` privilege on the [Metastore](/concepts/metastore.md). ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

Using Catalog Explorer, the SQL `CREATE RECIPIENT` command, or the Databricks CLI, the provider specifies a recipient name, chooses the **Open** recipient type and **Token** authentication, and optionally sets a token lifetime (up to a maximum of one year). If the lifetime is left blank and expiration is enabled, the token defaults to the metastore-level recipient token lifetime. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

The activation link is generated at creation time. It can later be retrieved by users with `USE RECIPIENT` privilege or by the recipient owner. Once the credential file has been downloaded, the activation link is no longer displayed. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Managing Recipient Tokens

A recipient can have at most two tokens at any time: an active token and a rotated token (one that has been set to expire). ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Rotating a Token

Rotation is necessary when the existing token is about to expire, the activation link is lost or compromised, the credential is corrupted, or the metastore-level token lifetime is changed. The rotation process expires the old token (optionally immediately by setting `--existing-token-expire-in-seconds` to `0`) and generates a new activation link and credential. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

The recipient object owner can perform rotation via Catalog Explorer or the CLI. After rotation, the provider must share the new activation link with the recipient, who must then apply the new credential on their side. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Updating Token Lifetime

The lifetime of an existing token can be modified using Catalog Explorer. This does not automatically apply the [Metastore](/concepts/metastore.md) default; it updates the individual recipient's token duration. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Modifying the Metastore-Level Default

Account admins can change the default recipient token lifetime for the [Metastore](/concepts/metastore.md) using the account console or CLI. Existing recipients are not affected until their tokens are rotated. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Security Considerations

- **Credential secrecy:** The downloaded credential must be treated as a secret and never shared outside the recipient's organization. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]
- **Compromise response:** If suspicion of compromise arises, the provider should revoke share access, rotate the token (setting the old token to expire immediately), and share the new activation link over a secure channel. In extreme cases, the recipient can be dropped and re-created. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]
- **Token expiration:** All bearer tokens issued before December 8, 2025, with expiration dates after December 8, 2026, or with no expiration date, automatically expire on December 8, 2026. Providers should review and renew such tokens. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Granting Share Access to the Recipient

After the recipient object is created, the provider must grant the recipient access to specific shares. This requires either [Metastore](/concepts/metastore.md) admin privileges or delegated permissions (`USE SHARE` + `SET SHARE PERMISSION` and `USE RECIPIENT` or recipient ownership). Grants can be managed via Catalog Explorer, SQL `GRANT ON SHARE`, or the CLI. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) – The open protocol for secure data sharing
- [Open Sharing](/concepts/opensharing.md) – Sharing with recipients outside Databricks
- [OIDC Token Federation](/concepts/oidc-token-federation-delta-sharing.md) – Alternative authentication method for open sharing
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that manages recipients and shares
- Recipient Management – Creating, updating, and deleting recipients
- Share Management – Creating and granting access to data shares

## Sources

- create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md

# Citations

1. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
