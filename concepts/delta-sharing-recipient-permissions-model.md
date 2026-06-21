---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 987286a1f1ece1f3a417c4eb3228edb3b437a07d8744f69cd223e12b3a773254
  pageDirectory: concepts
  sources:
    - create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - delta-sharing-recipient-permissions-model
    - DSRPM
  citations:
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
title: Delta Sharing Recipient Permissions Model
description: The hierarchy of privileges required to create, describe, manage, and grant access to recipients and shares in Unity Catalog, including metastore admin, USE RECIPIENT, CREATE RECIPIENT, and share-level permissions.
tags:
  - delta-sharing
  - permissions
  - authorization
timestamp: "2026-06-19T14:30:56.533Z"
---

# Delta Sharing Recipient Permissions Model

**Delta Sharing Recipient Permissions Model** defines how external users or systems (recipients) authenticate to and are authorized to read data shared through [Delta Sharing](/concepts/delta-sharing.md). In the Databricks-to-Open sharing model, recipients are entities that do not have access to a Unity Catalog–enabled Databricks workspace and use bearer tokens or OIDC federation to access shared data.^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Authentication Types

Recipients in open sharing authenticate via one of two methods:

- **Bearer token (TOKEN)** – A generated token stored in a credential file. The recipient downloads the file via an activation link and uses it to authenticate. The token is valid for a maximum of one year after creation.
- **OIDC federation** – An alternative that offers improved security and convenience (described in a separate article).

When the bearer token method is selected, the recipient object is created with `authentication_type = TOKEN`.^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Recipient Object Creation

To create a recipient, the user must be a **metastore admin** or have the **`CREATE RECIPIENT` privilege** on the Unity Catalog [Metastore](/concepts/metastore.md) where the shared data is registered.^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

Creation can be done via Catalog Explorer, the Databricks Unity Catalog CLI, or the SQL command `CREATE RECIPIENT`. During creation the provider:

1. Specifies a recipient name.
2. Selects **Open** as the recipient type and **Token** as the authentication method.
3. Optionally sets a token lifetime (up to one year). If not specified, the default [Metastore](/concepts/metastore.md) recipient token lifetime is used.
4. Receives an **activation link** to share with the recipient.

The activation link allows the recipient to download a credential file exactly once. The credential must be treated as a secret and not shared outside the recipient organization.^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Granting Access to Shares

After the recipient object exists and the provider has created Delta Sharing shares, the recipient must be granted access to those shares. The provider can use Catalog Explorer, the CLI, or the SQL command `GRANT ON SHARE`. Permissions required are one of:

- [Metastore](/concepts/metastore.md) admin
- Delegated permissions or ownership on both the share and the recipient object: (`USE SHARE` + `SET SHARE PERMISSION`) or share owner **AND** (`USE RECIPIENT`) or recipient owner.

The recipient receives read-only access to the tables included in the granted shares.^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Token Lifecycle and Rotation

Recipients can have at most two tokens at any time: an active token and a rotated token that is in the process of expiring. Token rotation is performed by the recipient object owner via Catalog Explorer or the CLI. The provider can set `--existing-token-expire-in-seconds` to control how quickly the old token expires (set to `0` for immediate expiration).

Databricks recommends rotating a token:

- When the existing token is about to expire.
- If the activation link or credential is lost, compromised, or corrupted.
- After modifying the metastore’s default recipient token lifetime (existing recipients are **not** automatically updated; rotation is required to apply the new lifetime).

If the activation link has never been accessed, rotating the token invalidates it and generates a new one. If all tokens have expired, rotating the token creates a new activation link.^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Security Considerations

- If a credential is inadvertently sent to the wrong party or over an insecure channel, immediately:
  1. Revoke the recipient’s access to the share.
  2. Rotate the token with `--existing-token-expire-in-seconds=0`.
  3. Share the new activation link over a secure channel.
  4. Re‑grant access after the new credential has been downloaded.

- In extreme cases, the provider may drop and re-create the recipient instead of rotating.

- The [Metastore](/concepts/metastore.md) admin (account admin) can modify the **default recipient token lifetime** for the [Metastore](/concepts/metastore.md). Changing this value does **not** affect existing recipients; each recipient must be rotated to adopt the new lifetime.^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Best Practices

- Use OIDC federation instead of bearer tokens where possible for enhanced security.
- Set token lifetimes as short as practical (maximum one year).
- Rotate tokens before expiration and after any security incident.
- Restrict recipient access using [IP Access Lists for OpenSharing Recipients](/concepts/ip-access-lists-for-opensharing-recipients.md).
- Monitor token expiration and promptly rotate or drop recipients with expired tokens.

## Related Concepts

- Delta Sharing shares
- [Open Sharing (Databricks-to-Open)](/concepts/open-sharing-databricks-to-open.md)
- [Manage data recipients for OpenSharing](/concepts/data-recipient-opensharing.md)
- [IP access lists for OpenSharing](/concepts/ip-access-lists-for-opensharing-recipients.md)
- Rotate credentials for open recipients
- OIDC federation for OpenSharing recipients
- [Unity Catalog privileges (CREATE RECIPIENT, USE RECIPIENT)](/concepts/unity-catalog-privileges-and-ownership.md)

## Sources

- create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md

# Citations

1. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
