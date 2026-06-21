---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 664db5367a7bf6d32c5846217715bb7dcb2a216c3c8aec568478e602c928de47
  pageDirectory: concepts
  sources:
    - create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - recipient-token-lifecycle-management
    - RTLM
  citations:
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
title: Recipient Token Lifecycle Management
description: The process of creating, rotating, updating, and expiring bearer tokens for OpenSharing recipients, including token lifetime defaults, expiration policies, and mandatory rotation procedures.
tags:
  - delta-sharing
  - token-management
  - security
timestamp: "2026-06-19T14:31:02.398Z"
---

# Recipient Token Lifecycle Management

**Recipient Token Lifecycle Management** refers to the processes of creating, distributing, rotating, and expiring bearer tokens used for Databricks-to-Open sharing with non-Databricks users. These tokens enable recipients who do not have access to a Unity Catalog-enabled Databricks workspace to authenticate and access shared data securely. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Overview

When a data provider creates a recipient object in their Unity Catalog [Metastore](/concepts/metastore.md) using the bearer token method, Databricks generates a token, a credential file that includes the token, and an activation link to share with the recipient. The recipient object has the authentication type of `TOKEN`. The recipient accesses the activation link, downloads the credential file, and uses it to authenticate and get read access to the tables included in the shares granted to them. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

All Databricks-to-Open sharing recipient tokens issued before December 8, 2025, with expiration dates after December 8, 2026, or with no expiration date, automatically expire on December 8, 2026. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Token Creation

To create a recipient token, the data provider uses Catalog Explorer, the Databricks Unity Catalog CLI, or the `CREATE RECIPIENT` SQL command. The creator must be a [Metastore](/concepts/metastore.md) admin or a user with the `CREATE RECIPIENT` privilege for the Unity Catalog [Metastore](/concepts/metastore.md) where the shared data is registered. During creation, the provider selects the **Token** authentication type and optionally sets the token lifetime expiration time. Tokens are valid for a maximum of one year after creation. If an expiration is set but the field is left blank, the token lifetime defaults to the value configured in the [Metastore](/concepts/metastore.md) settings. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Activation Link Distribution

After the recipient is created, the provider copies the activation link and sends it to the recipient over a secure channel, along with instructions for using it. The credential file can be downloaded only once. Recipients should treat the downloaded credential as a secret and must not share it outside of their organization. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Token Rotation

Rotating a token consists of setting an existing token to expire and replacing it with a new token and activation URL. Rotation is necessary when the existing token is about to expire, when the activation URL is lost or compromised, when the credential is corrupted or compromised after download, or when the recipient token lifetime for the [Metastore](/concepts/metastore.md) is modified. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

At any given time, a recipient can have at most two tokens: an active token and a rotated token. The rotated token is one that has been set to expire and be replaced by the active token. Until the rotated token expires, attempting to rotate the token again results in an error. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

When rotating a token, the provider can set `--existing-token-expire-in-seconds` to the number of seconds before the existing token expires. Setting this value to `0` causes immediate expiration. Databricks recommends setting a relatively short period that gives the recipient organization time to access the new activation URL while minimizing the time the recipient has two active tokens. If compromise is suspected, immediate expiration is recommended. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

If a recipient's existing activation URL has never been accessed, rotating the token invalidates that activation URL and replaces it with a new one. If all recipient tokens have expired, rotating the token replaces the existing activation URL with a new one. Databricks recommends promptly rotating or dropping a recipient whose token has expired. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Security Considerations

If a recipient activation URL is inadvertently sent to the wrong person or over an insecure channel, Databricks recommends the following steps: revoke the recipient's access to the share, rotate the recipient and set `--existing-token-expire-in-seconds` to `0`, share the new activation URL with the intended recipient over a secure channel, and after the activation URL has been accessed, grant the recipient access to the share again. In extreme situations, instead of rotating the token, the provider can drop and re-create the recipient. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

After sharing a new activation link, the recipient must apply the new credential on their side. If the recipient imported the credential as a provider object in Unity Catalog, they must update the provider object using the Databricks REST API. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Token Lifetime Modification

To modify the default recipient token lifetime for a Unity Catalog [Metastore](/concepts/metastore.md), an account admin can use Catalog Explorer or the Databricks Unity Catalog CLI. The recipient token lifetime for existing recipients is not updated automatically when the default lifetime is changed. To apply the new token lifetime to a given recipient, the provider must rotate their token. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Related Concepts

- [Recipient Object Management](/concepts/recipient-lifecycle-management.md) — Creating, viewing, and deleting recipient objects for OpenSharing
- [Bearer Token Authentication](/concepts/bearer-token-authentication-for-delta-sharing.md) — Token-based authentication flow for Delta Sharing
- [OIDC Federation for OpenSharing](/concepts/oidc-federation-for-opensharing.md) — Alternative authentication flow with advantages in security and convenience
- [Delta Sharing Security](/concepts/delta-sharing-security-model.md) — Secure data sharing practices and considerations
- [IP Access Lists for OpenSharing](/concepts/ip-access-lists-for-opensharing-recipients.md) — Restricting recipient access by IP address
- [OpenSharing Data Shares](/concepts/opensharing-share.md) — Creating and managing data shares for OpenSharing

## Sources

- create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md

# Citations

1. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
