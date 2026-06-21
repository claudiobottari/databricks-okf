---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7b271162643a47e725b089f663d14eb037e5360cc663a327d77a937abf22dcca
  pageDirectory: concepts
  sources:
    - create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - oidc-token-federation-delta-sharing
    - OTF(S
    - OIDC Token Federation
    - OIDC token federation
  citations:
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
title: OIDC Token Federation (Delta Sharing)
description: An alternative authentication flow for Open Sharing that offers security and convenience advantages over the bearer token method, recommended as a replacement for long-lived tokens.
tags:
  - delta-sharing
  - authentication
  - federation
  - oidc
timestamp: "2026-06-19T09:29:47.804Z"
---

# OIDC Token Federation (Delta Sharing)

**OIDC Token Federation** is an authentication flow for [Delta Sharing](/concepts/delta-sharing.md)'s **Databricks-to-Open sharing** model that allows non-Databricks recipients to securely access shared data using OpenID Connect (OIDC) tokens. It is an alternative to the [Bearer Token Authentication (Delta Sharing)|bearer token authentication flow](/concepts/bearer-token-authentication-for-delta-sharing.md) and offers improved security and convenience. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Overview

In Databricks-to-Open sharing, a data provider creates a recipient object in their Unity Catalog [Metastore](/concepts/metastore.md) and grants the recipient access to shares. Two authentication methods are available:

- **Bearer token flow** – Databricks generates a token, a credential file, and an activation link. The recipient downloads the credential and uses it to authenticate. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]
- **OIDC token federation flow** – The recipient authenticates using an OIDC identity provider. This flow is the recommended alternative and is supported alongside bearer tokens. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

Both flows are collectively referred to as *open sharing*. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Advantages

OIDC token federation provides several benefits over the bearer token approach: ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

- **Enhanced security** – Tokens are short-lived and managed by the recipient's OIDC provider, reducing the risk of long-lived credential exposure.
- **Improved convenience** – Recipients can leverage their existing identity infrastructure, eliminating the need to distribute and manage static credential files.
- **Simplified rotation** – Credentials are rotated automatically through the OIDC flow, avoiding manual token refresh steps.

## How It Works

The provider creates a recipient object with authentication type set to OIDC federation (instead of `TOKEN`). The recipient then uses their OIDC identity provider to obtain a federation token, which is exchanged for a Delta Sharing credential. Detailed instructions are available in the official documentation: [Enable Open ID Connect (OIDC) federation for OpenSharing recipients](https://docs.databricks.com/aws/en/delta-sharing/create-recipient-oidc-fed). ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Related Concepts

- [Bearer Token Authentication (Delta Sharing)](/concepts/bearer-token-authentication-for-delta-sharing.md) – The alternative authentication flow for open sharing.
- [Recipient Object (Delta Sharing)](/concepts/recipient-object-delta-sharing.md) – The Unity Catalog object that represents a data consumer.
- [Open Sharing (Delta Sharing)](/concepts/opensharing-delta-sharing.md) – The umbrella term for Databricks-to-Open sharing with either bearer token or OIDC federation.
- [Delta Sharing](/concepts/delta-sharing.md) – The open protocol for secure data sharing.
- [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) – The catalog system where recipient objects are created.

## Sources

- create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md

# Citations

1. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
