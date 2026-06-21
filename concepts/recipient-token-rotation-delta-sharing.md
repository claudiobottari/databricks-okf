---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7b1d3261e1aeadb267dd59d2c27c6ef701b53ccd28d14db267c831abcf993302
  pageDirectory: concepts
  sources:
    - create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - recipient-token-rotation-delta-sharing
    - RTR(S
    - Token Rotation (Delta Sharing)
  citations:
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
title: Recipient Token Rotation (Delta Sharing)
description: The process of setting an existing bearer token to expire and replacing it with a new token and activation URL, used when tokens are compromised, about to expire, or when the metastore token lifetime changes.
tags:
  - delta-sharing
  - security
  - token-management
timestamp: "2026-06-19T09:29:30.000Z"
---

# Recipient Token Rotation (Delta Sharing)

**Recipient Token Rotation** is the process of setting an existing bearer token to expire and replacing it with a new token and activation URL for a [Delta Sharing](/concepts/delta-sharing.md) recipient using Databricks-to-Open sharing. This operation is a key security practice for managing data access for recipients who authenticate using bearer tokens. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## When to Rotate a Token

You should rotate a recipient's token and generate a new activation URL in the following circumstances: ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

- When the existing recipient token is about to expire.
- If a recipient loses their activation URL or if it is compromised.
- If the credential is corrupted, lost, or compromised after it is downloaded by a recipient.
- When you modify the recipient token lifetime for a [Metastore](/concepts/metastore.md).

## Token Constraints

At any given time, a recipient can have at most two tokens: an active token and a rotated token. The rotated token is one that has been set to expire and be replaced by the active token. Attempting to rotate the token again while a rotated token is still active results in an error. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Rotation Process

To rotate a recipient's token, use Catalog Explorer or the Databricks Unity Catalog CLI. The user performing the rotation must be the recipient object owner. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

When rotating a token, you can optionally set `--existing-token-expire-in-seconds` to control how long the existing token remains valid. If set to `0`, the existing recipient token expires immediately. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Catalog Explorer Steps

1. In your Databricks workspace, click the **Catalog** icon.
2. At the top of the **Catalog** pane, click the gear icon and select **OpenSharing**.
3. In the left pane, expand the **OpenSharing** menu and select **Shared by me**.
4. On the **Shared by me** tab, click **Recipients**, and select the recipient.
5. Under **Token management**, next to **Token expiration**, click **Rotate**.
6. On the **Rotate token** dialog, set the token to expire either immediately or for a set period of time.
7. Click **Rotate**.
8. On the **Details** tab, copy the new **Activation link** and share it with the recipient over a secure channel. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Security Recommendations

Databricks recommends setting `--existing-token-expire-in-seconds` to a relatively short period that gives the recipient organization time to access the new activation URL while minimizing the amount of time that the recipient has two active tokens. If you suspect that the existing recipient token is compromised, Databricks recommends forcing it to expire immediately. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Handling Compromised Activation Links

If a recipient activation URL is inadvertently sent to the wrong person or is sent over an insecure channel: ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

1. Revoke the recipient's access to the share.
2. Rotate the recipient and set `--existing-token-expire-in-seconds` to `0`.
3. Share the new activation URL with the intended recipient over a secure channel.
4. After the activation URL has been accessed, grant the recipient access to the share again.

## Recipient Actions After Rotation

After receiving a new activation link, the recipient must apply the new credential on their side. If the recipient imported the credential as a provider object in Unity Catalog, they must update the provider object with the Databricks REST API. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Impact on Activation Links

If a recipient's existing activation URL has never been accessed, rotating the existing token invalidates that activation URL and replaces it with a new one. If all recipient tokens have expired, rotating the token replaces the existing activation URL with a new one. Databricks recommends promptly rotating or dropping a recipient whose token has expired. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Related Concepts

- [Recipient Objects (Delta Sharing)](/concepts/recipient-object-delta-sharing.md) — The entity that controls access for data recipients.
- [Bearer Token Authentication (Delta Sharing)](/concepts/bearer-token-authentication-for-delta-sharing.md) — The authentication method used by OpenSharing recipients.
- [OIDC Federation for OpenSharing](/concepts/oidc-federation-for-opensharing.md) — An alternative authentication flow with security and convenience advantages over bearer tokens.
- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for secure data sharing across platforms.
- Metastore Configuration (Delta Sharing) — Where default recipient token lifetimes are configured.

## Sources

- create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md

# Citations

1. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
