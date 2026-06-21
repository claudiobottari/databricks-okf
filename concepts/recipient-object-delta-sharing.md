---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e3f0e4573d5777e1b6c27d6bde9e8e095c32314ad2049e8e47348e8932fdb7ec
  pageDirectory: concepts
  sources:
    - create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
    - what-is-the-opensharing-databricks-to-open-sharing-protocol-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - recipient-object-delta-sharing
    - RO(S
    - Recipient Objects (Delta Sharing)
    - Recipient Objects
    - Recipient objects
    - recipient objects
  citations:
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
    - file: what-is-the-opensharing-databricks-to-open-sharing-protocol-databricks-on-aws.md
title: Recipient Object (Delta Sharing)
description: A Unity Catalog object created by a data provider to represent a non-Databricks recipient, configured with authentication type TOKEN, and used to grant access to shared data shares.
tags:
  - delta-sharing
  - unity-catalog
  - recipients
timestamp: "2026-06-18T14:48:42.362Z"
---

# Recipient Object (Delta Sharing)

A **Recipient Object (Delta Sharing)** is a named object in the Unity Catalog [Metastore](/concepts/metastore.md) that represents a user or group of users that a data provider wants to share data with using the [OpenSharing](/concepts/opensharing.md) Databricks-to-Open sharing protocol. The recipient object serves as the foundation for establishing secure data sharing relationships between providers and consumers who may not have access to a Unity Catalog-enabled Databricks workspace. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md, what-is-the-opensharing-databricks-to-open-sharing-protocol-databricks-on-aws.md]

## Authentication Types

The recipient object supports two authentication flows for Databricks-to-Open sharing: bearer tokens and Open ID Connect (OIDC) federation. ^[what-is-the-opensharing-databricks-to-open-sharing-protocol-databricks-on-aws.md]

### Bearer Token Authentication

When created with bearer token authentication (authentication type `TOKEN`), Databricks generates a bearer token, a credential file that includes the token, and an activation link. The data provider sends the activation link to the recipient over a secure channel. The recipient follows the link to download the credential file, which they use to authenticate and gain read access to the shared data. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md, what-is-the-opensharing-databricks-to-open-sharing-protocol-databricks-on-aws.md]

All Databricks-to-Open sharing recipient tokens issued before December 8, 2025, with expiration dates after December 8, 2026, or with no expiration date, automatically expire on December 8, 2026. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### OIDC Federation Authentication

The OIDC federation flow offers advantages in security and convenience over bearer tokens. In this approach, the recipient's identity provider (IdP) manages authentication based on a policy created by the provider. ^[what-is-the-opensharing-databricks-to-open-sharing-protocol-databricks-on-aws.md]

## Creating a Recipient

### Required Permissions

[Metastore](/concepts/metastore.md) admin or user with the `CREATE RECIPIENT` privilege for the Unity Catalog [Metastore](/concepts/metastore.md) where the shared data is registered. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Creation Process (Bearer Token Method)

Recipients can be created using Catalog Explorer, the Databricks Unity Catalog CLI, or the `CREATE RECIPIENT` SQL command. When creating a recipient, you must set the recipient type to **Open** and select **Token** as the authentication method. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

**Creation options include:**
- **Token lifetime** — Set an expiration time (in seconds, minutes, hours, or days). Tokens are valid for a maximum of one year after creation. If left blank with **Set expiration** enabled, the lifetime defaults to the [Metastore](/concepts/metastore.md)'s recipient token lifetime configuration. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]
- **Comment** — Optional descriptive text.
- **Recipient properties** — Custom key-value pairs. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Granting Share Access

Once the recipient object is created and shares have been defined, the provider must grant the recipient access to the share. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

Permissions required: One of the following:
- [Metastore](/concepts/metastore.md) admin.
- Delegated permissions or ownership on both the share and the recipient objects (`USE SHARE` + `SET SHARE PERMISSION` or share owner) AND (`USE RECIPIENT` or recipient owner).

## Activation Link

The activation link allows the recipient to download the credential file. To retrieve the link, use Catalog Explorer, the Databricks Unity Catalog CLI, or the `DESCRIBE RECIPIENT` SQL command. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

Permissions required: [Metastore](/concepts/metastore.md) admin, user with the `USE RECIPIENT` privilege, or recipient object owner.

If the recipient has already downloaded the credential file, the activation link is no longer returned or displayed. The credential file can be downloaded only once. Recipients must treat the downloaded credential as a secret and not share it outside their organization. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Token Management

### Token Lifetime Configuration

The default recipient token lifetime for a Unity Catalog [Metastore](/concepts/metastore.md) can be modified by an account admin. Tokens are valid for a maximum of one year after creation. This change does not automatically update existing recipients — each recipient's token must be rotated to apply the new lifetime. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Token Rotation

A recipient can have at most two tokens at any given time: an active token and a rotated token set to expire. Rotating a token sets the existing token to expire and replaces it with a new token and activation URL. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

**When to rotate:**
- The existing token is about to expire.
- The activation URL is lost or compromised.
- The credential file is corrupted, lost, or compromised after download.
- The [Metastore](/concepts/metastore.md) token lifetime has been modified. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

**Recommendations:**
- Set the existing token to expire after a short period to minimize the time the recipient has two active tokens.
- If the existing token is suspected to be compromised, force it to expire immediately by setting `--existing-token-expire-in-seconds` to `0`.
- If an activation URL is inadvertently sent to the wrong recipient, revoke share access, rotate the token, share the new activation URL over a secure channel, then re-grant access. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

**Permissions required:** Recipient object owner.

### Update Existing Token Lifetime

The lifetime of an existing recipient token can be updated using Catalog Explorer. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Security Considerations

- Tokens used in Databricks-to-Open sharing are supported between all cloud environment types.
- Databricks recommends configuring tokens to expire and encouraging recipients to manage their downloaded credential file securely.
- Providers can assign IP Access Lists to restrict recipient access to specific network locations. ^[what-is-the-opensharing-databricks-to-open-sharing-protocol-databricks-on-aws.md, create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Provider Setup

Data providers using Databricks-to-Open sharing must configure the default recipient token lifetime when they enable [OpenSharing](/concepts/opensharing.md) for their Unity Catalog [Metastore](/concepts/metastore.md). ^[what-is-the-opensharing-databricks-to-open-sharing-protocol-databricks-on-aws.md]

## Recipient Properties

Custom recipient properties can be added on the recipient **Overview** tab using the edit icon next to **Recipient properties**. Each property consists of a key-value pair. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing Databricks-to-Open Sharing Protocol](/concepts/opensharing-databricks-to-open-protocol.md)
- [OpenSharing Databricks-to-Databricks Sharing Protocol](/concepts/databricks-to-databricks-opensharing-protocol.md)
- [Delta Sharing Shares](/concepts/delta-sharing.md)
- [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md)
- [IP Access Lists for OpenSharing](/concepts/ip-access-lists-for-opensharing-recipients.md)
- [Recipient Token Lifetime Configuration](/concepts/recipient-token-lifetime.md)

## Sources

- create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
- what-is-the-opensharing-databricks-to-open-sharing-protocol-databricks-on-aws.md

# Citations

1. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
2. [what-is-the-opensharing-databricks-to-open-sharing-protocol-databricks-on-aws.md](/references/what-is-the-opensharing-databricks-to-open-sharing-protocol-databricks-on-aws-e4f6895b.md)
