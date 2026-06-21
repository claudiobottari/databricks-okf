---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6eb3cfef727ebececf7909d189e235cd299565643b95f655485e7eb5a69e5135
  pageDirectory: concepts
  sources:
    - create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - oidc-token-federation-for-opensharing
    - OTFFO
    - oidc-token-federation-for-open-sharing
    - OTFFOS
  citations:
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
title: OIDC Token Federation for OpenSharing
description: An alternative authentication flow to bearer tokens for Databricks-to-Open sharing that offers improved security and convenience by using OpenID Connect federation.
tags:
  - delta-sharing
  - authentication
  - oidc
  - databricks
timestamp: "2026-06-19T14:30:38.765Z"
---

# OIDC Token Federation for OpenSharing

**OIDC Token Federation for OpenSharing** is an authentication flow that allows non-Databricks users to securely access shared data via Open ID Connect (OIDC) tokens. It is an alternative to the bearer‑token authentication flow for Databricks‑to‑Open sharing recipients. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Overview

In the [OpenSharing](/concepts/opensharing.md) model, a data provider creates a recipient object in their Unity Catalog [Metastore](/concepts/metastore.md) and grants the recipient access to shares. Two authentication methods are available: bearer tokens (the default) and OIDC token federation. The OIDC federation flow offers advantages in security and convenience over the bearer‑token flow. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Comparison with Bearer Token Authentication

| Aspect | Bearer Token | OIDC Token Federation |
|--------|--------------|-----------------------|
| Token management | Provider generates, rotates, and revokes tokens. Tokens have configurable lifetimes (max. one year). | Uses federated identity; token lifecycle managed via OIDC identity provider. |
| Security posture | Requires secure sharing of activation links; tokens can be rotated if compromised. | Inherits security of the provider’s OIDC infrastructure; generally considered more secure. |
| Convenience | Recipient must download a credential file and treat it as a secret. | Recipient uses existing OIDC credentials; no separate secret file to manage. |

The bearer token flow is described in detail in Create a recipient object for non-Databricks users using bearer tokens. For complete guidance on setting up OIDC federation, see the official Databricks documentation: [Enable Open ID Connect (OIDC) federation for OpenSharing recipients](https://docs.databricks.com/aws/en/delta-sharing/create-recipient-oidc-fed). ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) – The data sharing model for non-Databricks users.
- Recipient object – The Unity Catalog object that represents an external data consumer.
- [Bearer Token Authentication for OpenSharing](/concepts/bearer-token-authentication-for-opensharing.md) – The alternative authentication method.
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) that manages recipients and shares.

## Sources

- create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md

# Citations

1. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
