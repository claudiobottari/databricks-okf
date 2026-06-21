---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0d7b054d890240d9b71b8a9d4b22942c24f080281cd909832aa10238638be498
  pageDirectory: concepts
  sources:
    - create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metastore-recipient-token-lifetime-configuration
    - MRTLC
    - unity-catalog-metastore-recipient-token-lifetime-configuration
    - UCMRTLC
  citations:
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
title: Metastore Recipient Token Lifetime Configuration
description: The default token lifetime setting for a Unity Catalog metastore that applies to new recipients when no explicit token lifetime is set, configurable only by account admins.
tags:
  - delta-sharing
  - admins
  - metastore-configuration
timestamp: "2026-06-18T14:49:09.693Z"
---

# [Metastore](/concepts/metastore.md) Recipient Token Lifetime Configuration

**Metastore Recipient Token Lifetime Configuration** refers to the default expiration duration applied to bearer tokens created for OpenSharing recipients in Databricks-to-Open sharing. This metastore-level setting controls the maximum lifetime of recipient tokens unless overridden when creating an individual recipient.

## Overview

When a data provider creates an OpenSharing recipient using the bearer token method, Databricks generates a token credential. The token's lifetime is determined by the [Metastore](/concepts/metastore.md)'s recipient token lifetime configuration. If the [Metastore](/concepts/metastore.md) has no expiration configured, tokens may default to a longer lifetime — but all tokens issued before December 8, 2025, with expiration dates after December 8, 2026, or with no expiration date, automatically expire on December 8, 2026. Providers should review integrations and renew tokens as needed to avoid breaking changes after this date. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

The default recipient token lifetime applies to newly created recipients unless a specific token lifetime is provided during recipient creation. When creating a recipient via the UI with **Set expiration** enabled but no value provided, the token lifetime defaults to the value configured in the [Metastore](/concepts/metastore.md). ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Modifying the Default Lifetime

Account admins can modify the default recipient token lifetime for the Unity Catalog [Metastore](/concepts/metastore.md) using Catalog Explorer or the Databricks Unity Catalog CLI. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Requirements

- **Permissions required**: Account admin. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Using Catalog Explorer

1. Log in to the account console.
2. Click **Catalog** in the sidebar.
3. Click the [Metastore](/concepts/metastore.md) name.
4. Under **OpenSharing recipient token lifetime**, click **Edit**.
5. Enable **Set expiration**.
6. Enter a number of seconds, minutes, hours, or days, and select the unit of measure. Tokens are valid for a maximum of one year after creation.
7. Click **Save**.

^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Important Notes on Modification

Changing the metastore-level default does not retroactively update existing recipient tokens. To apply the new lifetime to an existing recipient, providers must rotate that recipient's token. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Updating Individual Recipient Token Lifetime

Recipient object owners can update the lifetime of an existing recipient token using Catalog Explorer. This is distinct from modifying the [Metastore](/concepts/metastore.md) default and applies only to the selected recipient. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Relationship to Token Rotation

When the [Metastore](/concepts/metastore.md) recipient token lifetime is modified, existing recipient tokens are not automatically updated. Providers should rotate recipient tokens to activate the new lifetime setting. Rotating a token involves setting the existing token to expire (optionally immediately) and generating a new token with a new activation URL. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Security Considerations

- Tokens are valid for a maximum of one year after creation, whether set at the [Metastore](/concepts/metastore.md) level or per-recipient. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]
- Databricks recommends using the OIDC federation flow as an alternative to bearer tokens for improved security and convenience. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]
- If a credential is compromised, providers should rotate the token immediately (set `--existing-token-expire-in-seconds` to `0`) and share a new activation URL over a secure channel. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for data sharing
- [OpenSharing Recipients](/concepts/opensharing-recipient.md) — Non-Databricks users accessing shared data
- [Bearer Token Authentication for OpenSharing](/concepts/bearer-token-authentication-for-opensharing.md) — Token-based authentication flow
- [OIDC Federation for OpenSharing](/concepts/oidc-federation-for-opensharing.md) — Alternative authentication flow with improved security
- [Recipient Token Rotation](/concepts/recipient-token-rotation.md) — Managing and updating token credentials

## Sources

- create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md

# Citations

1. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
