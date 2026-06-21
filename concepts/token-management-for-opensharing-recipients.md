---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9a2ffee1f9cdbcdb3bd2e419e681e570e07b463996825292e4fb36a067894cd5
  pageDirectory: concepts
  sources:
    - manage-data-recipients-for-opensharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - token-management-for-opensharing-recipients
    - TMFOR
  citations:
    - file: manage-data-recipients-for-opensharing-databricks-on-aws.md
title: Token Management for OpenSharing Recipients
description: For recipients using bearer token authentication (Databricks-to-Open sharing), providers can view/copy authentication links, rotate bearer tokens, and manage activation links. Tokens are invalidated when a recipient is deleted.
tags:
  - delta-sharing
  - authentication
  - security
  - databricks
timestamp: "2026-06-19T19:24:03.367Z"
---

# Token Management for OpenSharing Recipients

**Token Management for OpenSharing Recipients** refers to the administrative tasks related to managing bearer tokens used by recipients in a Databricks-to-Open sharing scenario. These tokens authenticate non-Databricks users when accessing shared data.

## Overview

For recipients using Databricks-to-Open sharing with bearer tokens, token management includes rotating or updating the bearer token. This is performed by the provider through the recipient details page in Catalog Explorer. The token management options are available under the **Token Management** section of the recipient details. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

Token management is relevant for recipients whose authentication type is `TOKEN`. Other authentication types (`DATABRICKS`, `OAUTH_CLIENT_CREDENTIALS`, `OIDC_FEDERATION`) do not use bearer tokens. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## Token Lifecycle

### Activation Link

When a token-authenticated recipient is created, an activation link is generated. This link allows the recipient to download their credential. The provider can view and copy the **Authentication link** from the recipient details page. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

### Token Rotation

Providers can rotate the bearer token for a recipient. This is done from the recipient details page by:

1. Navigating to the recipient details via **Catalog > Gear icon > OpenSharing > Shared by me > Recipients**, then selecting the recipient.
2. Under **Token Management**, clicking to rotate or update the bearer token.

^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## Token Invalidation

When a provider deletes a recipient, any tokens that the recipient used in a Databricks-to-Open sharing scenario are **invalidated**. After deletion, the users represented by that recipient can no longer access the shared data. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## Viewing Token-Related Details

Viewing recipient details, including token-related information, requires specific permissions:

- [Metastore](/concepts/metastore.md) admin
- User with the `USE RECIPIENT` privilege
- Recipient object owner

Token-related details visible on the recipient details page include:

- Token lifetime
- Activation link
- Activation status (whether the credential has been downloaded)
- IP access lists, if assigned

^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing Recipients](/concepts/opensharing-recipient.md) — The named objects representing users or groups with whom data is shared
- [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md) — Sharing data with non-Databricks users using bearer tokens
- [IP Access Lists for OpenSharing](/concepts/ip-access-lists-for-opensharing-recipients.md) — Optional restriction of recipient access by IP address
- Recipient Authentication Types — Including DATABRICKS, TOKEN, OAUTH_CLIENT_CREDENTIALS, and OIDC_FEDERATION
- OpenSharing Security — Overall security model for data sharing

## Sources

- manage-data-recipients-for-opensharing-databricks-on-aws.md

# Citations

1. [manage-data-recipients-for-opensharing-databricks-on-aws.md](/references/manage-data-recipients-for-opensharing-databricks-on-aws-073afd50.md)
