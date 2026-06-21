---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 24d73fe114ee419f0a6bf8239b2f93d30c595cc9feac359cc99f4636fd131f98
  pageDirectory: concepts
  sources:
    - create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - token-rotation-and-security-management
    - Security Management and Token Rotation
    - TRASM
  citations:
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
title: Token Rotation and Security Management
description: The process of rotating a recipient's bearer token to generate a new token and activation URL, used when tokens are about to expire, compromised, or when security best practices require credential refresh.
tags:
  - delta-sharing
  - security
  - token-management
timestamp: "2026-06-19T17:56:59.651Z"
---

# Token Rotation and Security Management

**Token Rotation and Security Management** refers to the practices and procedures for rotating bearer tokens used in [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md) (open sharing) and managing their lifecycle securely. Bearer tokens are credentials that grant non-Databricks recipients access to shared data. Proper rotation and management minimize the risk of compromised credentials. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Token Rotation

Token rotation is the process of replacing an existing bearer token with a new one, invalidating the old token after a configurable delay. A recipient can have at most two tokens at any time: an active token and a rotated token that is set to expire. Attempting to rotate again while the rotated token is still active results in an error. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

Rotation should be performed in the following circumstances:

- The existing recipient token is about to expire.
- The activation URL is lost or compromised.
- The credential file is corrupted, lost, or compromised after download.
- The recipient token lifetime for the [Metastore](/concepts/metastore.md) has been modified (existing recipients are not automatically updated—rotation is required to apply the new lifetime). ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

When rotating, the provider can set an `existing-token-expire-in-seconds` value. Setting it to `0` expires the old token immediately. Databricks recommends using a short expiration period to minimize the window where two tokens are active, unless compromise is suspected, in which case immediate expiration is advised. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Rotation Procedure

Token rotation is performed by the recipient object owner using Catalog Explorer or the Databricks Unity Catalog CLI. After rotation, a new activation link is generated and must be shared with the recipient over a secure channel. The recipient must then apply the new credential. If the recipient imported the credential as a provider object in Unity Catalog, they must update the provider object using the Databricks REST API. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

If the existing activation URL has never been accessed, rotation invalidates it and replaces it with a new one. If all recipient tokens have expired, rotation generates a fresh activation URL. Databricks recommends promptly rotating or dropping recipients whose tokens have expired. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Security Considerations

Bearer tokens must be treated as secrets. The credential file can be downloaded only once, and recipients must not share it outside their organization. If a credential may have been handled insecurely, the provider should:

1. Revoke the recipient's access to the share.
2. Rotate the token, setting `--existing-token-expire-in-seconds` to `0`.
3. Share the new activation URL with the intended recipient over a secure channel.
4. Re‑grant access after the new activation URL has been used. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

In extreme situations, the recipient can be dropped and re‑created instead of rotated. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Token Lifetime

### Per‑Recipient Token Lifetime

When creating a recipient, the provider can set a token lifetime (expiration time in seconds, minutes, hours, or days). Tokens are valid for a maximum of one year after creation. If no explicit expiration is set, the default lifetime from the [Metastore](/concepts/metastore.md) configuration applies. The token lifetime for an existing recipient can be updated in Catalog Explorer. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Metastore‑Level Default Lifetime

The default recipient token lifetime for a Unity Catalog [Metastore](/concepts/metastore.md) can be modified by an account admin in the account console. Changes to the [Metastore](/concepts/metastore.md) default do **not** apply to existing recipients; each recipient must be rotated to adopt the new lifetime. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Important Expiration Note

All Databricks‑to‑Open sharing recipient tokens issued before December 8, 2025, with expiration dates after December 8, 2026, or with no expiration date, automatically expire on December 8, 2026. Providers should review integrations and renew tokens as needed to avoid breaking changes. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Related Concepts

- [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md) – The sharing model that uses bearer tokens or OIDC federation.
- [Bearer Token](/concepts/oidc-vs-bearer-token-authentication.md) – The credential type used for non‑Databricks recipients.
- Recipient Object – The Unity Catalog object that represents a data consumer.
- [Activation Link](/concepts/activation-link-delta-sharing.md) – The URL used to download the credential file.
- [OIDC Token Federation](/concepts/oidc-token-federation-delta-sharing.md) – An alternative authentication flow with improved security and convenience.

## Sources

- create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md

# Citations

1. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
