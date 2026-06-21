---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2aa4a5521388963d5332df183334bc7cb53cf74c5138c241e73d3062c8906abd
  pageDirectory: concepts
  sources:
    - create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
    - set-up-opensharing-for-your-account-for-providers-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - recipient-token-lifetime
    - RTL
    - token lifetime
    - recipient-token-lifetime-configuration
    - RTLC
    - recipient-token-lifetime-management
    - RTLM
  citations:
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
    - file: set-up-opensharing-for-your-account-for-providers-databricks-on-aws.md
title: Recipient Token Lifetime
description: The configurable expiration period for bearer tokens assigned to open sharing recipients, with a maximum validity of one year from creation, configurable per recipient or at the metastore level.
tags:
  - delta-sharing
  - security
  - configuration
timestamp: "2026-06-18T14:48:54.341Z"
---

# Recipient Token Lifetime

**Recipient Token Lifetime** refers to the configurable expiration time for bearer tokens used in the [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md) (also known as OpenSharing) protocol. This setting determines the maximum period after which all recipient tokens expire and must be regenerated for the recipient to continue accessing shared data.^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Overview

When a data provider creates a recipient object for [OpenSharing](/concepts/opensharing.md), a bearer token is generated as part of the activation link and credential file. The token lifetime is the duration for which that token remains valid. After the lifetime expires, the recipient can no longer use the token to authenticate and access shared data.^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

Token lifetimes are used only in the Databricks-to-Open sharing protocol and are not relevant for [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md) or [OIDC token federation](/concepts/oidc-token-federation-delta-sharing.md) flows.^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md, set-up-opensharing-for-your-account-for-providers-databricks-on-aws.md]

## Maximum Token Lifetime

Recipient tokens are valid for a maximum of one year after creation. This limit applies both to the default lifetime set at the [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) level and to any custom lifetime specified when creating an individual recipient.^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md, set-up-opensharing-for-your-account-for-providers-databricks-on-aws.md]

## Setting and Modifying the Lifetime

### At the [Metastore](/concepts/metastore.md) Level (Account Admin)

As a Databricks account admin, you can set the default recipient token lifetime for the entire Unity Catalog [Metastore](/concepts/metastore.md). This can be done through the Databricks account console by:^[set-up-opensharing-for-your-account-for-providers-databricks-on-aws.md]

1. Navigating to the [Metastore](/concepts/metastore.md) details page.
2. Enabling **Set expiration**.
3. Entering a value in seconds, minutes, hours, or days (up to one year maximum).
4. Clicking **Enable**.

### At the Recipient Level ([Metastore](/concepts/metastore.md) Admin or Recipient Owner)

When creating an individual recipient, you can set a custom token lifetime that overrides the [Metastore](/concepts/metastore.md) default. Set the lifetime in the **Token lifetime** field during creation, specifying the expiration in seconds, minutes, hours, or days from the recipient creation time. If the field is left blank, the [Metastore](/concepts/metastore.md)'s default recipient token lifetime is used.^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Modifying an Existing Recipient's Token Lifetime

To update the lifetime of an existing recipient token, use Catalog Explorer. The recipient object owner must perform this operation.^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

**Important:** Changing the default token lifetime for a [Metastore](/concepts/metastore.md) does **not** automatically update the token lifetime for existing recipients. To apply a new token lifetime to a given recipient, you must rotate their token by setting the existing token to expire and generating a new one.^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md, set-up-opensharing-for-your-account-for-providers-databricks-on-aws.md]

## Automatic Expiration of Pre-December 2025 Tokens

All Databricks-to-Open sharing recipient tokens issued before December 8, 2025, with expiration dates after December 8, 2026, or with no expiration date, automatically expire on December 8, 2026. If you currently use recipient tokens with long or unlimited lifetimes, review your integrations and renew tokens as needed to avoid service disruption.^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Token Rotation

Rotating a recipient's token consists of setting an existing token to expire and replacing it with a new token and activation URL. You should rotate a token when:^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

- The existing token is about to expire.
- The activation URL is lost or compromised.
- The credential is corrupted, lost, or compromised after download.
- The recipient token lifetime is modified at the [Metastore](/concepts/metastore.md) level.

When rotating, you can optionally set `--existing-token-expire-in-seconds` to `0` (immediate expiration) or a short period to allow the recipient time to transition. If you suspect a token is compromised, Databricks recommends forcing immediate expiration.^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Security Considerations

At any given time, a recipient can have at most two tokens: an active token and a rotated token (one set to expire). Attempting to rotate again while a rotated token still exists results in an error.^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Related Concepts

- Recipient object — The object that holds the bearer token and activation link.
- [OpenSharing](/concepts/opensharing.md) — The protocol for sharing data outside Databricks using bearer tokens.
- [Credential file](/concepts/credential-file-opensharing.md) — Contains the bearer token for recipient authentication.
- [Activation link](/concepts/activation-link-delta-sharing.md) — The URL the recipient uses to download the credential file.
- [Token rotation](/concepts/recipient-token-rotation.md) — The process of expiring and replacing a recipient's token.

## Sources

- create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
- set-up-opensharing-for-your-account-for-providers-databricks-on-aws.md

# Citations

1. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
2. [set-up-opensharing-for-your-account-for-providers-databricks-on-aws.md](/references/set-up-opensharing-for-your-account-for-providers-databricks-on-aws-4b18295d.md)
