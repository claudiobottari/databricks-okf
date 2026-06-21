---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6d80e164b1c3b3f10428c155edec1f7836de84596b37621d50594a549ee80723
  pageDirectory: concepts
  sources:
    - create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - open-sharing-databricks-to-open
    - OS(
    - Delta Sharing (Databricks-to-Open)
  citations:
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
title: Open Sharing (Databricks-to-Open)
description: A Delta Sharing authentication flow that allows data providers to share data with recipients who do not have access to a Unity Catalog-enabled Databricks workspace, using bearer tokens or OIDC federation.
tags:
  - delta-sharing
  - authentication
  - data-sharing
timestamp: "2026-06-19T09:30:04.891Z"
---

# Open Sharing (Databricks-to-Open)

**Open Sharing**, also called _Databricks-to-Open sharing_, is a [Delta Sharing](/concepts/delta-sharing.md) authentication model that enables a Databricks data provider to securely share data with recipients who do not have access to a Unity Catalog-enabled Databricks workspace. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Overview

In Open Sharing, the provider creates a recipient object in their Unity Catalog [Metastore](/concepts/metastore.md) and generates a bearer token (or, alternatively, uses [OIDC federation](/concepts/oidc-federation-policy.md)) that the recipient uses to authenticate. This is distinct from the _Databricks-to-Databricks_ sharing model, where both parties have access to Databricks workspaces. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Authentication Methods

Open Sharing supports two authentication flows:

- **Bearer token flow**: The provider chooses the bearer token method when creating the recipient. Databricks generates a token, a credential file that includes the token, and an activation link to share with the recipient. The recipient object has `authentication_type` set to `TOKEN`. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]
- **OIDC federation flow**: An alternative that offers security and convenience advantages over the bearer token flow. See [Enable OpenID Connect (OIDC) federation for OpenSharing recipients](/concepts/oidc-federation-for-opensharing.md). ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Token Lifecycle

- **Maximum lifetime**: Tokens are valid for a maximum of one year after creation. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]
- **Automatic expiration**: All Databricks-to-Open sharing recipient tokens issued before December 8, 2025, with expiration dates after December 8, 2026, or with no expiration date, automatically expire on December 8, 2026. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]
- **Default token lifetime**: The [Metastore](/concepts/metastore.md) configuration sets a default recipient token lifetime. Existing recipients do not automatically inherit changes to this default; they must have their token rotated to apply the new lifetime. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Creating a Recipient

To create a recipient for Open Sharing, use Catalog Explorer, the Databricks Unity Catalog CLI, or the `CREATE RECIPIENT` SQL command.

**Required permissions**: [Metastore](/concepts/metastore.md) admin or a user with the `CREATE RECIPIENT` privilege on the Unity Catalog [Metastore](/concepts/metastore.md) where the data is registered. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Steps (Catalog Explorer)

1. In your Databricks workspace, click **Catalog**.
2. At the top of the Catalog pane, click the gear icon and select **OpenSharing** (or click **Share > OpenSharing** in the upper-right corner).
3. On the **Shared by me** tab, click **New recipient**.
4. Enter the **Recipient name**.
5. For **Recipient type**, select **Open**.
6. Select **Token**.
7. (Optional) Set the **Token lifetime** expiration time. If **Set expiration** is selected and left blank, the token lifetime defaults to the [Metastore](/concepts/metastore.md) configuration value.
8. (Optional) Add a comment.
9. Click **Create**.
10. Copy the activation link.

^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Recipient Properties

The recipient can have custom properties added via the **Edit icon** next to **Recipient properties** on the recipient's **Overview** tab. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Activation Link

The activation link is available from the recipient details page. If the recipient has already downloaded the credential file, the activation link is not returned or displayed. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

**Required permissions** to view the activation link: [Metastore](/concepts/metastore.md) admin, user with the `USE RECIPIENT` privilege, or the recipient object owner. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Sharing Data

After creating the recipient and creating shares, the provider can grant the recipient access to those shares. Required permissions include:
- [Metastore](/concepts/metastore.md) admin; or
- Delegated permissions or ownership on both the share and the recipient objects (`USE SHARE` + `SET SHARE PERMISSION` or share owner; and `USE RECIPIENT` or recipient owner).

^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Token Rotation

You may need to rotate a recipient's token in these circumstances:
- The existing token is about to expire.
- The activation URL is lost or compromised.
- The credential is corrupted, lost, or compromised after download.
- The recipient token lifetime for a [Metastore](/concepts/metastore.md) has been modified.

^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Rotation Process

1. Open the recipient details in Catalog Explorer.
2. In the **Token management** section, next to **Token expiration**, click **Rotate**.
3. Set the existing token to expire immediately or after a set period.
4. Click **Rotate**.
5. Copy the new activation link and share it securely.

^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

**Important**: At any given time, a recipient can have at most two tokens: an active token and a rotated token. Attempting to rotate again while a rotated token is still valid results in an error. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Security Considerations

- The credential file can be downloaded only once.
- Recipients should treat the downloaded credential as a secret and not share it outside their organization.
- If a credential may have been handled insecurely, rotate the token immediately (set `--existing-token-expire-in-seconds` to `0`).

^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for secure data sharing.
- [Bearer Token](/concepts/oidc-vs-bearer-token-authentication.md) — The authentication credential used in the token flow.
- OIDC Federation — An alternative authentication flow for Open Sharing.
- Recipient Object — The Unity Catalog object representing the sharing recipient.
- [Recipient Properties](/concepts/recipient-properties.md) — Custom metadata properties for recipients.

## Sources
- create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md

# Citations

1. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
