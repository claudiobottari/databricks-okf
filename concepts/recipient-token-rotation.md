---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f214b486d05247245a1774cc270e0b92aee6a9983eab9b621748836fe85192a4
  pageDirectory: concepts
  sources:
    - create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - recipient-token-rotation
    - RTR
    - Rotate Recipient Token
    - Token rotation
    - recipient-token-rotation-delta-sharing
    - RTR(S
    - Token Rotation (Delta Sharing)
  citations:
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
title: Recipient Token Rotation
description: The process of expiring an existing recipient token and generating a new token and activation URL, used when tokens are about to expire, compromised, or when metastore token lifetime is modified.
tags:
  - delta-sharing
  - security
  - token-management
timestamp: "2026-06-18T14:48:44.670Z"
---

# Recipient Token Rotation

**Recipient token rotation** is the process of replacing an existing bearer token used for [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md) with a new token and activation URL. Token rotation is a security control that ensures continued access for recipients of shared data while allowing the provider to manage credential lifecycles.^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## When to Rotate a Recipient's Token

The provider should rotate a recipient's token and generate a new activation URL in the following circumstances:^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

- When the existing recipient token is about to expire.
- If a recipient loses their activation URL or if it is compromised.
- If the credential is corrupted, lost, or compromised after it is downloaded by a recipient.
- When the recipient token lifetime is modified for a [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) (existing recipients are not automatically updated).

## How Token Rotation Works

At any given time, a recipient can have at most two tokens: an active token and a rotated token. The rotated token is one that has been set to expire and be replaced by the active token. Attempting to rotate the token again while a rotated token is still valid results in an error.^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

When you rotate a recipient's token, you can set the `--existing-token-expire-in-seconds` parameter to control when the existing token expires:^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

- Setting the value to `0` causes the existing recipient token to expire immediately.
- Setting a longer period gives the recipient organization time to access the new activation URL before the old token expires.

If a recipient's existing activation URL has never been accessed, rotating the token invalidates that activation URL and replaces it with a new one. If all recipient tokens have expired, rotating the token replaces the existing activation URL with a new one.^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Security Considerations

Databricks recommends using a relatively short expiration period when rotating tokens to minimize the time window during which a recipient has two active tokens. If you suspect the existing token is compromised, force it to expire immediately.^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

If an activation URL is inadvertently sent to the wrong person or over an insecure channel:^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

1. Revoke the recipient's access to the share.
2. Rotate the recipient and set `--existing-token-expire-in-seconds` to `0`.
3. Share the new activation URL with the intended recipient over a secure channel.
4. After the activation URL has been accessed, grant the recipient access again.

In extreme situations, instead of rotating the token, you can drop and re-create the recipient.^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Token Lifetime Management

### Default Token Lifetime

All Databricks-to-Open sharing recipient tokens issued before December 8, 2025, with expiration dates after December 8, 2026, or with no expiration date, automatically expire on December 8, 2026. Users should review integrations and renew tokens as needed to avoid breaking changes.^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Modifying Default Lifetime

The default recipient token lifetime for a Unity Catalog [Metastore](/concepts/metastore.md) can be modified by account admins. The maximum allowed lifetime is one year from creation. The modification does not apply to existing recipients automatically — each recipient must have its token rotated to apply the new lifetime.^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Performing Token Rotation

To rotate a recipient's token, use Catalog Explorer or the Databricks Unity Catalog CLI. You must have the recipient object owner permission.^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

When rotating, you generate a new activation link. You must share this link with the recipient over a secure channel. After the recipient accesses the new activation URL and downloads the credential file, they must apply the new credential on their side.^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

If the recipient is a provider in another Unity Catalog [Metastore](/concepts/metastore.md), they must update the provider object using the [Databricks REST API](/concepts/databricks-mlflow-rest-api-20.md). The credential file can only be downloaded once — recipients should treat it as a secret and not share it outside their organization.^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The data sharing framework using bearer tokens
- [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md) — Sharing to non-Databricks consumers
- Bearer token — The authentication mechanism for open sharing recipients
- [Activation link](/concepts/activation-link-delta-sharing.md) — The URL used by recipients to download credentials
- Recipient object — The metadata object representing a data consumer
- [Credential file](/concepts/credential-file-opensharing.md) — The file containing the bearer token for authentication
- IP access lists — Additional security for restricting recipient access

## Sources

- create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md

# Citations

1. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
