---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fdc56c3f3a6fd0a999052b9d321b28de67fd1162d7b9318bfee1485d1c33b911
  pageDirectory: concepts
  sources:
    - create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - recipient-token-lifetime-configuration
    - RTLC
  citations:
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
title: Recipient Token Lifetime Configuration
description: Configurable expiration settings for recipient bearer tokens, set at creation time or via metastore-level defaults, with a maximum validity of one year and the ability to update or rotate tokens.
tags:
  - delta-sharing
  - configuration
  - token-lifetime
timestamp: "2026-06-19T17:57:03.556Z"
---

# Recipient Token Lifetime Configuration

**Recipient Token Lifetime Configuration** refers to the policies and procedures that control the expiration period of bearer tokens used for Databricks-to-Open sharing. The lifetime determines how long a recipient can use a credential to access shared data before the token becomes invalid. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Default Lifetime

The default lifetime for all newly created recipients in a Unity Catalog [Metastore](/concepts/metastore.md) is defined by the account-level **OpenSharing recipient token lifetime** setting. This default can be modified only by an account admin. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Setting a Token Lifetime During Recipient Creation

When you create a recipient through Catalog Explorer, a Databricks Unity Catalog CLI command, or the `CREATE RECIPIENT` SQL command, you may optionally set the token lifetime at creation time. If you enable **Set expiration** but leave the field blank, the lifetime defaults to the value configured in the [Metastore](/concepts/metastore.md) settings. A token can be valid for a maximum of one year after creation. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Updating an Existing Recipient’s Token Lifetime

To change the expiration of an existing recipient token, use Catalog Explorer. **Required permission**: Recipient object owner.

1. In your Databricks workspace, click **Catalog**.
2. At the top of the Catalog pane, click the **Gear** icon and select **OpenSharing**.
3. In the left pane, expand **OpenSharing** and select **Shared by me**.
4. Click **Recipients** and select the recipient.
5. In the rightmost column, under **Token management**, next to **Token expiration**, click **Update**.
6. Set the new token lifetime in the dialog.
7. Click **Save**.

^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Modifying the [Metastore](/concepts/metastore.md) Default Token Lifetime

To change the default recipient token lifetime for your entire Unity Catalog [Metastore](/concepts/metastore.md), use Catalog Explorer or the Databricks Unity Catalog CLI. **Required permission**: Account admin.

1. Log in to the account console.
2. In the sidebar, click **Catalog**.
3. Click the [Metastore](/concepts/metastore.md) name.
4. Under **OpenSharing recipient token lifetime**, click **Edit**.
5. Enable **Set expiration**.
6. Enter a number of seconds, minutes, hours, or days and select the unit of measure.
7. Click **Save**.

^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Important Expiration Rule

All Databricks-to-Open sharing recipient tokens issued before December 8, 2025, with expiration dates after December 8, 2026, or with no expiration date, automatically expire on December 8, 2026. If you currently use recipient tokens with long or unlimited lifetimes, review your integrations and renew tokens as needed to avoid breaking changes after this date. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Applying Lifetime Changes to Existing Recipients

The recipient token lifetime for existing recipients is **not** updated automatically when you change the default recipient token lifetime for a [Metastore](/concepts/metastore.md). To apply the new token lifetime to a given recipient, you must rotate their token. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

See [Rotate Recipient Token](/concepts/recipient-token-rotation.md) and Manage Recipient Tokens for detailed procedures.

## Security Considerations

Databricks recommends rotating tokens when the existing token is about to expire, the activation URL is lost or compromised, the credential is corrupted or compromised, or the [Metastore](/concepts/metastore.md) default lifetime has been changed. If you suspect compromise, set the existing token to expire immediately (`--existing-token-expire-in-seconds 0`). ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Related Concepts

- Recipient Token
- [Open Sharing](/concepts/opensharing.md)
- Token Rotation
- Manage Recipient Tokens
- Recipient Object

## Sources

- create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md

# Citations

1. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
