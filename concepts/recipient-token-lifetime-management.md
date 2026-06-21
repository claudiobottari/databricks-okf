---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fb35125d5bc2a8bbe7ea15ab3a103aa533eb40a7c28721dbac950df545e2167b
  pageDirectory: concepts
  sources:
    - create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - recipient-token-lifetime-management
    - RTLM
  citations:
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
title: Recipient Token Lifetime Management
description: Configuration of expiration periods for Delta Sharing recipient bearer tokens, including per-recipient settings and metastore-wide defaults, with a maximum validity of one year.
tags:
  - delta-sharing
  - configuration
  - security-policies
timestamp: "2026-06-18T11:15:19.664Z"
---

# Recipient Token Lifetime Management

**Recipient Token Lifetime Management** refers to the administrative practices for controlling the expiration, rotation, and security of bearer tokens used by [OpenSharing](/concepts/opensharing.md) recipients in [Delta Sharing](/concepts/delta-sharing.md). These tokens authenticate non-Databricks users who access shared data through the Databricks-to-Open sharing bearer token flow.

## Overview

When a data provider creates a recipient object for Databricks-to-Open sharing using the bearer token method, Databricks generates a token, a credential file that includes the token, and an activation link to share with the recipient. The recipient uses the credential file to authenticate and get read access to the tables included in the shares they are granted access to. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

All Databricks-to-Open sharing recipient tokens issued before December 8, 2025, with expiration dates after December 8, 2026, or with no expiration date, automatically expire on December 8, 2026. If you currently use recipient tokens with long or unlimited lifetimes, review your integrations and renew tokens as needed to avoid breaking changes after this date. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Token Lifetime Configuration

### Setting Token Lifetime During Creation

When creating a recipient, you can optionally set the **Token lifetime** expiration time (in seconds, minutes, hours, or days from recipient creation time). Tokens are valid for a maximum of one year after creation. If you select **Set expiration** and leave the field blank, the token lifetime defaults to the recipient token lifetime value set in the [Metastore](/concepts/metastore.md) configuration. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Modifying Default [Metastore](/concepts/metastore.md) Token Lifetime

Account admins can modify the default recipient token lifetime for a Unity Catalog [Metastore](/concepts/metastore.md). To do so:

1. Log in to the account console.
2. Click **Catalog**.
3. Click the [Metastore](/concepts/metastore.md) name.
4. Under **OpenSharing recipient token lifetime**, click **Edit**.
5. Enable **Set expiration**.
6. Enter a number of seconds, minutes, hours, or days, and select the unit of measure. Tokens are valid for a maximum of one year after creation.
7. Click **Save**.

^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

The recipient token lifetime for existing recipients is not updated automatically when you change the default recipient token lifetime for a [Metastore](/concepts/metastore.md). To apply the new token lifetime to a given recipient, you must rotate their token. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Updating an Existing Recipient's Token Lifetime

To update the lifetime of an existing recipient token, use Catalog Explorer. You need recipient object owner permissions. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

1. In your Databricks workspace, click **Catalog**.
2. Click the gear icon and select **OpenSharing**.
3. Expand the **OpenSharing** menu and select **Shared by me**.
4. Click **Recipients**, and select the recipient.
5. Under **Token management**, next to **Token expiration**, click **Update**.
6. Set the new token lifetime and click **Save**.

^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Token Rotation

Rotating a token consists of setting an existing token to expire and replacing it with a new token and activation URL. You should rotate a recipient's token in the following circumstances:

- When the existing recipient token is about to expire.
- If a recipient loses their activation URL or if it is compromised.
- If the credential is corrupted, lost, or compromised after it is downloaded by a recipient.
- When you modify the recipient token lifetime for a [Metastore](/concepts/metastore.md).

^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Limitations

At any given time, a recipient can have at most two tokens: an active token and a rotated token. The rotated token is one that has been set to expire and be replaced by the active token. Until the rotated token expires, attempting to rotate the token again results in an error. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Performing a Token Rotation

To rotate a recipient's token, use Catalog Explorer or the Databricks Unity Catalog CLI. You need recipient object owner permissions. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

Using **Catalog Explorer**:

1. Click **Catalog**, then click the gear icon and select **OpenSharing**.
2. Expand **OpenSharing** and select **Shared by me**.
3. Click **Recipients**, and select the recipient.
4. Under **Token management**, next to **Token expiration**, click **Rotate**.
5. Set the token to expire either immediately or for a set period of time.
6. Click **Rotate**.
7. Copy the new activation link and share it with the recipient over a secure channel.

^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

After sharing the new activation link, the recipient must apply the new credential on their side. If the recipient imported the credential as a provider object in Unity Catalog, they must update the provider object with the Databricks REST API. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Rotation Options

When you rotate a recipient's token, you can optionally set `--existing-token-expire-in-seconds` to the number of seconds before the existing token expires. If you set the value to `0`, the existing token expires immediately. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

Databricks recommends setting this to a relatively short period that gives the recipient organization time to access the new activation URL while minimizing the time the recipient has two active tokens. If you suspect the existing token is compromised, force it to expire immediately. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

If a recipient's existing activation URL has never been accessed, rotating the token invalidates that activation URL and replaces it with a new one. If all recipient tokens have expired, rotating the token replaces the existing activation URL with a new one. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Security Considerations

Recipients should treat the downloaded credential as a secret and must not share it outside of their organization. If you have concerns that a credential may have been handled insecurely, you can rotate a recipient's credential at any time. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

If a recipient activation URL is inadvertently sent to the wrong person or over an insecure channel:

1. Revoke the recipient's access to the share.
2. Rotate the recipient and set `--existing-token-expire-in-seconds` to `0`.
3. Share the new activation URL with the intended recipient over a secure channel.
4. After the activation URL has been accessed, grant the recipient access to the share again.

^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

In extreme situations, instead of rotating the recipient's token, you can drop and re-create the recipient. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

Databricks recommends promptly rotating or dropping a recipient whose token has expired. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for secure data sharing
- [OpenSharing](/concepts/opensharing.md) — Sharing with non-Databricks users using bearer tokens or OIDC federation
- [Recipient Objects](/concepts/recipient-object-delta-sharing.md) — Objects that define who can receive shared data
- [Delta Sharing Activation Link](/concepts/opensharing-recipient-activation-link.md) — The URL recipients use to download their credential file
- [OIDC Federation for OpenSharing](/concepts/oidc-federation-for-opensharing.md) — An alternative authentication flow with security advantages over bearer tokens

## Sources

- create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md

# Citations

1. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
