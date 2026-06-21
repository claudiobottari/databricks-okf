---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a74b07fea8d5cecc2a2c7ae17f18102e7452100880e7c263bea62941a2ce4a12
  pageDirectory: concepts
  sources:
    - create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - oidc-token-federation-for-open-sharing
    - OTFFOS
  citations:
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
title: OIDC Token Federation for Open Sharing
description: An alternative authentication method to bearer tokens for Databricks-to-Open sharing, offering advantages in security and convenience for recipients without Databricks workspaces.
tags:
  - delta-sharing
  - authentication
  - oidc
  - federation
timestamp: "2026-06-18T11:15:32.626Z"
---

# OIDC Token Federation for Open Sharing

**OIDC Token Federation for Open Sharing** is an authentication flow for Databricks-to-Open sharing that uses OpenID Connect (OIDC) tokens instead of static bearer tokens. It provides an alternative to the bearer token flow for granting non-Databricks recipients access to securely shared data. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Overview

In Databricks-to-Open sharing, data providers create recipient objects in their Unity Catalog [Metastore](/concepts/metastore.md) to grant external, non-Databricks users access to shares. Two authentication flows are available:

- **Bearer token flow**: A static token is generated, and the recipient downloads a credential file containing the token.
- **OIDC federation flow**: Uses OIDC token federation instead of static tokens.

The OIDC flow offers advantages in security and convenience compared to the bearer token flow. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## How It Works

When creating an Open recipient, the provider selects the OIDC authentication method. The recipient object then uses the `authentication_type` of `OIDC`. The process for generating activation links and distributing credentials differs from the bearer token approach. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

For full instructions on setting up OIDC federation for OpenSharing recipients, see the dedicated article: [Enable Open ID Connect (OIDC) federation for OpenSharing recipients](https://docs.databricks.com/aws/en/delta-sharing/create-recipient-oidc-fed). ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Advantages Over Bearer Tokens

- **Improved security**: OIDC tokens are short-lived and can be refreshed without exposing long-lived secrets. Bearer tokens may have longer lifetimes and require manual rotation.
- **Greater convenience**: The federation flow reduces the operational overhead of managing token expiration and rotation for both providers and recipients.

## Related Concepts

- [Open Sharing](/concepts/opensharing.md) — The model for sharing data to non-Databricks recipients
- [Bearer Token Authentication](/concepts/bearer-token-authentication-for-delta-sharing.md) — The alternative authentication flow using static tokens
- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol underlying Databricks-to-Open sharing
- [Unity Catalog](/concepts/unity-catalog.md) — The [Metastore](/concepts/metastore.md) where recipient objects are defined

## Sources

- create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md

# Citations

1. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
