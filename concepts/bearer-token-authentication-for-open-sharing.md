---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5e5482288ac597282a0f0a59819c1f441fccb20b99834a010d6b88e2881683e5
  pageDirectory: concepts
  sources:
    - create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - bearer-token-authentication-for-open-sharing
    - BTAFOS
  citations:
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
      start: 1
      end: 6
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
      start: 8
      end: 14
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
      start: 19
      end: 22
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
      start: 18
      end: 18
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
      start: 33
      end: 36
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
      start: 34
      end: 35
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
      start: 77
      end: 79
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
      start: 142
      end: 148
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
      start: 150
      end: 158
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
      start: 174
      end: 174
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
      start: 209
      end: 214
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
      start: 225
      end: 229
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
      start: 133
      end: 135
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
      start: 168
      end: 171
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
      start: 172
      end: 172
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
      start: 24
      end: 27
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
      start: 119
      end: 126
title: Bearer Token Authentication for Open Sharing
description: A token-based authentication method for open sharing where Databricks generates a bearer token, a credential file, and an activation link for the recipient to download and use for read access to shared data.
tags:
  - delta-sharing
  - authentication
  - tokens
timestamp: "2026-06-18T14:48:27.641Z"
---

# Bearer Token Authentication for Open Sharing

**Bearer Token Authentication for Open Sharing** is an authentication flow used in [Delta Sharing](/concepts/delta-sharing.md) to allow recipients who do not have access to a [Unity Catalog](/concepts/unity-catalog.md)–enabled Databricks workspace to securely access shared data. It is one of two open sharing authentication methods, alongside [OIDC Token Federation for Open Sharing](/concepts/oidc-token-federation-for-open-sharing.md). ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:1-6]

## How It Works

1. A data provider creates a [recipient object](/concepts/opensharing-recipient-object.md) in their Unity Catalog [Metastore](/concepts/metastore.md), selecting the bearer token method. Databricks generates a bearer token, a credential file that contains the token, and an activation link. The recipient object has `authentication_type` set to `TOKEN`. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:8-14]
2. The data provider shares the activation link with the recipient over a secure channel.
3. The recipient accesses the activation link, downloads the credential file, and uses it to authenticate and obtain read access to the tables and shares they have been granted. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:19-22]

Tokens can be refreshed and revoked by the provider as needed. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:18]

## Creating a Recipient

**Permissions required:** [Metastore](/concepts/metastore.md) admin or a user with the `CREATE RECIPIENT` privilege on the [Metastore](/concepts/metastore.md) where the shared data is registered. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:33-36]

You can create a recipient using [Catalog Explorer](/concepts/catalog-explorer.md), the Databricks Unity Catalog CLI, or the `CREATE RECIPIENT` SQL command in a Databricks notebook or SQL query editor. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:34-35]

| Method | Steps |
|--------|-------|
| Catalog Explorer | Navigate to **Catalog > OpenSharing > Shared by me > New recipient**. Enter a recipient name, set **Recipient type** to **Open**, select **Token**, optionally set the token lifetime, and click **Create**. Copy the activation link. |
| SQL | Run `CREATE RECIPIENT <name> USING TOKEN` with optional `COMMENT` and `TOKEN_LIFETIME` parameters. |
| CLI | Use `databricks unity-catalog recipients create` with the `--authentication-type TOKEN` flag. |

### Token Lifetime

When creating a recipient, you can set the token expiration time (in seconds, minutes, hours, or days) up to a maximum of one year. If no expiration is provided, the token defaults to the recipient token lifetime configured for the [Metastore](/concepts/metastore.md). ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:77-79]

## Managing Recipient Tokens

Providers can manage recipient tokens by rotating them or updating their lifetime.

### Rotating a Token

Rotation replaces an existing token and generates a new activation URL. It is recommended when: ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:142-148]

- The existing token is about to expire.
- The activation URL is lost or compromised.
- The credential file is corrupted, lost, or compromised.
- The recipient token lifetime for the [Metastore](/concepts/metastore.md) has been modified.

A recipient can have at most two tokens simultaneously: an active token and a rotated token. During rotation, you can set `--existing-token-expire-in-seconds` to control when the old token expires. Setting it to `0` expires it immediately. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:150-158]

**Permissions required:** Recipient object owner. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:174]

### Updating Token Lifetime

The lifetime of an existing recipient token can be changed via Catalog Explorer. This does not affect the default [Metastore](/concepts/metastore.md) lifetime; existing recipients must be rotated to apply a new default. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:209-214]

### Modifying the [Metastore](/concepts/metastore.md) Default Lifetime

Account admins can change the default recipient token lifetime for the Unity Catalog [Metastore](/concepts/metastore.md) using Catalog Explorer or the CLI. Existing recipients are not automatically updated — they require a token rotation to use the new default. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:225-229]

## Security Considerations

- The credential file can only be downloaded once. Recipients must treat it as a secret and not share it outside their organization. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:133-135]
- If an activation URL is sent to the wrong party or over an insecure channel, Databricks recommends revoking share access, rotating the token (with immediate expiration), sharing the new activation URL securely, and then re‑granting access. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:168-171]
- In extreme cases, you can drop and re‑create the recipient instead of rotating. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:172]

### Token Auto‑Expiration

All Databricks-to-Open sharing recipient tokens issued before December 8, 2025, with expiration dates after December 8, 2026, or with no expiration date, automatically expire on December 8, 2026. Providers should review integrations and renew tokens as needed. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:24-27]

## Granting Share Access

After creating a recipient and creating shares, you must grant the recipient access to those shares. Permissions required: [Metastore](/concepts/metastore.md) admin, or delegated permissions/ownership on both the share and recipient objects (`USE SHARE` + `SET SHARE PERMISSION` or share owner, and `USE RECIPIENT` or recipient owner). ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:119-126]

## Related Concepts

- [Open Sharing](/concepts/opensharing.md) — The overall model for sharing data outside Databricks workspaces.
- [OIDC Token Federation for Open Sharing](/concepts/oidc-token-federation-for-open-sharing.md) — The alternative authentication flow for open sharing.
- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol underlying Databricks data sharing.
- Recipient Object — The Unity Catalog object representing a data recipient.
- Credential File — The file containing the bearer token and connection details.
- [Activation Link](/concepts/activation-link-delta-sharing.md) — The URL provided to the recipient for first‑time credential download.
- [IP Access Lists for Open Sharing](/concepts/ip-access-lists-for-opensharing-recipients.md) — Restricting recipient access by IP.
- Managing Open Sharing Recipients — Lifecycle operations for recipient objects.

## Sources

- create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md

# Citations

1. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:1-6](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
2. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:8-14](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
3. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:19-22](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
4. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:18-18](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
5. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:33-36](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
6. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:34-35](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
7. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:77-79](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
8. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:142-148](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
9. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:150-158](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
10. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:174-174](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
11. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:209-214](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
12. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:225-229](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
13. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:133-135](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
14. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:168-171](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
15. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:172-172](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
16. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:24-27](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
17. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md:119-126](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
