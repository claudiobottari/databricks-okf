---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dc7ad91370f84d56fda4c70a8d0884f5b755cfbd6a746a51191cce7a423e880e
  pageDirectory: concepts
  sources:
    - create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - recipient-object-unity-catalog
    - RO(C
  citations:
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
title: Recipient Object (Unity Catalog)
description: A Unity Catalog object that represents a data recipient in Open Sharing, configured with authentication type TOKEN, with an activation link and credential file generated upon creation.
tags:
  - unity-catalog
  - delta-sharing
  - recipient-management
timestamp: "2026-06-19T09:30:20.728Z"
---

Here is the wiki page for "Recipient Object (Unity Catalog)" based solely on the provided source material.

---

## Recipient Object (Unity Catalog)

A **Recipient Object** in [Unity Catalog](/concepts/unity-catalog.md) represents a data consumer in [Delta Sharing](/concepts/delta-sharing.md). It defines who can receive shared data and how they authenticate. Recipients can be other Unity Catalog–enabled Databricks workspaces (Databricks-to-Databricks sharing) or external consumers that do not have a Databricks workspace, which is called **Open Sharing**. This page covers the creation and management of Open Sharing recipients that authenticate with bearer tokens. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Authentication Types

Open Sharing recipients can use one of two authentication flows:

- **Bearer token (`TOKEN`)** — The provider creates a recipient; Databricks generates a bearer token and an activation link. The recipient downloads a credential file via the activation link and uses it to authenticate. The recipient object has an `authentication_type` property set to `TOKEN` for bearer token recipients. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]
- **OIDC Federation** — An alternative flow with enhanced security and convenience. This page focuses on the bearer token flow.

### Creating a Recipient

**Required permissions**: [Metastore](/concepts/metastore.md) admin, or a user with the `CREATE RECIPIENT` privilege on the Unity Catalog [Metastore](/concepts/metastore.md) where the shared data is registered.

Recipients can be created using Catalog Explorer, SQL (`CREATE RECIPIENT`), or the Databricks Unity Catalog CLI. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

#### Steps (Catalog Explorer)

1.  In your Databricks workspace, click **Catalog**.
2.  At the top of the **Catalog** pane, click the gear icon and select **OpenSharing**.
3.  On the **Shared by me** tab, click **New recipient**.
4.  Enter a **Recipient name**.
5.  For **Recipient type**, select **Open**.
6.  Select **Token** as the authentication method.
7.  (Optional) Set a **Token lifetime** expiration time. Tokens are valid for a maximum of one year. If left blank, the default is the metastore-level recipient token lifetime.
8.  (Optional) Add a comment.
9.  Click **Create**. The activation link is shown; copy it to share with the recipient.

After creation, the recipient object has an `authentication_type` of `TOKEN`. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

#### Setting Recipient Properties

After creating the recipient, you can add custom key-value properties on the **Overview** tab by clicking the edit icon next to **Recipient properties**. For details, see [Recipient Properties](/concepts/recipient-properties.md). ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Activation Link

The activation link allows the recipient to download a credential file (which can be done only once). Share this link and instructions for using it over a secure channel. If the link has never been accessed, you can retrieve it later using `DESCRIBE RECIPIENT` (SQL) or via Catalog Explorer. Once the credential file has been downloaded, the activation link is no longer returned or displayed. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Granting Access to Shares

After creating the recipient and creating shares, you must grant the recipient access to those shares. Permissions required: [Metastore](/concepts/metastore.md) admin, or a user with `USE SHARE` + `SET SHARE PERMISSION` (or share owner) **and** `USE RECIPIENT` (or recipient owner). See [Grant Access to Shares](/concepts/granting-share-access-to-recipients.md). ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Token Management

A recipient can have at most two tokens at any time: an active token and a rotated token that is set to expire. Token management includes rotation, lifetime modification, and metastore-level defaults.

#### Rotating a Token

Rotate a token when it is about to expire, if the activation link is compromised, or if the credential file is corrupted or lost.

- **Permissions**: Recipient object owner.
- **Process** (Catalog Explorer): On the recipient details page, under **Token management**, click **Rotate**. Optionally set the existing token to expire immediately (`0` seconds) or after a short period. The new activation link replaces the old one.
- After rotation, share the new activation link with the recipient. The recipient must update their credential accordingly.

Databricks recommends setting `--existing-token-expire-in-seconds` to a short period to minimize the overlap of two active tokens. If compromise is suspected, expire the existing token immediately. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

#### Updating Token Lifetime

To change the lifetime of an existing recipient's token: in Catalog Explorer, on the recipient details page, next to **Token expiration**, click **Update** and set a new lifetime. This does not affect the [Metastore](/concepts/metastore.md) default. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

#### Modifying the [Metastore](/concepts/metastore.md) Default Token Lifetime

Account admins can change the default recipient token lifetime for the entire Unity Catalog [Metastore](/concepts/metastore.md) via the account console. After changing the default, existing recipients are not automatically updated — you must rotate their tokens individually to apply the new lifetime. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Security Considerations

- Treat the credential file as a secret. It must not be shared outside the recipient organization.
- If an activation link is sent to the wrong person or over an insecure channel: revoke the recipient’s access to the share, rotate the token (expire immediately), share a new activation link securely, then re-grant access.
- If the recipient has already downloaded the credential, rotating the token invalidates the old credential and generates a new activation link.
- All recipient tokens issued before December 8, 2025, with expiration dates after December 8, 2026, or with no expiration date, will automatically expire on December 8, 2026. Renew such tokens to avoid breaking changes. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Open Sharing](/concepts/opensharing.md)
- [Bearer Token Authentication](/concepts/bearer-token-authentication-for-delta-sharing.md)
- OIDC Federation
- [Recipient Properties](/concepts/recipient-properties.md)
- [Share Object](/concepts/opensharing-share-object.md)
- [Grant Access to Shares](/concepts/granting-share-access-to-recipients.md)
- [Metastore](/concepts/metastore.md)

### Sources

- create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md

# Citations

1. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
