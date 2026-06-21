---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d96be84ddc9837db1e53cc22fa2e3bccfbcccf68dd7a704df9e44966badf36a3
  pageDirectory: concepts
  sources:
    - create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - recipient-token-security-best-practices
    - RTSBP
  citations:
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
title: Recipient Token Security Best Practices
description: Security guidelines for managing bearer tokens including immediate expiration on compromise, secure channel communication, credential rotation, and responding to token exposure incidents.
tags:
  - delta-sharing
  - security
  - best-practices
timestamp: "2026-06-19T14:30:27.352Z"
---

# Recipient Token Security Best Practices

**Recipient Token Security Best Practices** covers the recommended procedures for managing bearer tokens used in [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md) (Open Sharing) when granting non-Databricks users access to Delta Sharing data. Following these practices minimizes the risk of unauthorized data access and ensures compliance with security policies.

## Token Lifecycle Management

Each recipient can have at most two tokens at any given time: one active token and one rotated token. The rotated token is one that has been set to expire and be replaced by the active token. Attempting to rotate a token again while a rotated token is still valid results in an error. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

When creating a recipient object with bearer token authentication, you may optionally set a token lifetime at creation time. Tokens are valid for a maximum of one year after creation. If you leave the expiration field blank, the token lifetime defaults to the metastore-level recipient token lifetime value. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

**Important**: All recipient tokens issued before December 8, 2025, with expiration dates after December 8, 2026, or with no expiration date, automatically expire on December 8, 2026. Review integrations and renew tokens as needed to avoid breaking changes after this date. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Token Rotation

Rotate a recipient’s token in the following circumstances:

- The existing token is about to expire.
- The activation URL is lost or compromised.
- The credential file is corrupted, lost, or compromised after download.
- The metastore-level recipient token lifetime has been modified. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

When rotating, you can optionally set `existing-token-expire-in-seconds` to control how long the old token remains valid. Set this to a relatively short period to give the recipient time to obtain the new activation URL while minimizing the window of dual active tokens. If you suspect the existing token is compromised, set the value to `0` to force immediate expiration. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

If the existing activation URL has never been accessed, rotating the token invalidates that URL and generates a new one. If all recipient tokens have expired, rotating replaces the activation URL with a new one; Databricks recommends promptly rotating or dropping recipients with expired tokens. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Handling Compromised Credentials

If a credential is handled insecurely, take the following steps:

1. Revoke the recipient’s access to the share.
2. Rotate the recipient and set `existing-token-expire-in-seconds` to `0`.
3. Share the new activation URL with the intended recipient over a secure channel.
4. After the activation URL has been accessed, grant the recipient access to the share again.

In extreme situations, instead of rotating, you can drop and re‑create the recipient entirely. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Secure Distribution of Activation Links

The activation link and credential file must be shared with the recipient over a secure channel. The credential file can be downloaded only once; recipients must treat it as a secret and never share it outside their organization. If the activation link is inadvertently sent to the wrong person or over an insecure channel, follow the compromised‑credential procedure above. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Token Expiration Policies

The default recipient token lifetime for a Unity Catalog [Metastore](/concepts/metastore.md) can be modified by an account admin. After changing the default, existing recipients are **not** automatically updated; you must rotate each recipient’s token to apply the new lifetime. Tokens remain valid for a maximum of one year after creation. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## IP Access Lists (Additional Protection)

To further restrict recipient access, you can use IP access lists to limit the origins from which the token can be used. This is an optional but recommended security layer for Open Sharing recipients. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for secure data sharing.
- [Open Sharing](/concepts/opensharing.md) — Authentication flow using bearer tokens or OIDC federation.
- Recipient Object — Unity Catalog object that represents a data consumer.
- [Bearer Token](/concepts/oidc-vs-bearer-token-authentication.md) — The credential used for non-Databricks recipients.
- Token Rotation — The process of replacing an expiring or compromised token.
- IP Access Lists — Network security controls for recipient authentication.

## Sources

- create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md

# Citations

1. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
