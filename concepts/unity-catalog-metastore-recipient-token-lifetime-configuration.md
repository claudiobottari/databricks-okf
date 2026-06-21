---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 38162c6fe1bcb9774355131bd53072cdd6100e088ae1a65394721e206869540a
  pageDirectory: concepts
  sources:
    - create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-metastore-recipient-token-lifetime-configuration
    - UCMRTLC
  citations:
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
title: Unity Catalog Metastore Recipient Token Lifetime Configuration
description: The ability for account admins to set a default token lifetime for all new OpenSharing recipients at the metastore level, which does not automatically apply to existing recipients.
tags:
  - delta-sharing
  - administration
  - databricks
timestamp: "2026-06-19T14:30:39.467Z"
---

# Unity Catalog [Metastore](/concepts/metastore.md) Recipient Token Lifetime Configuration

**Unity Catalog [Metastore](/concepts/metastore.md) Recipient Token Lifetime Configuration** refers to the setting that determines the default expiration period for bearer tokens issued to [Open Sharing](/concepts/opensharing.md) recipients in a [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md). This configuration is managed at the [Metastore](/concepts/metastore.md) level by an account admin and affects tokens created for non-Databricks users who access shared data via the Databricks-to-Open sharing bearer token flow.

## Overview

When a data provider creates an Open Sharing recipient using the bearer token method, the token can be assigned a specific lifetime at creation time. If no explicit expiration is set, the token defaults to the lifetime value configured for the [Metastore](/concepts/metastore.md). This default token lifetime applies to all new bearer tokens created by any data provider in that [Metastore](/concepts/metastore.md). ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Default Lifetime

The default recipient token lifetime can be set to any duration up to a maximum of **one year (365 days)** after token creation. The unit of measure can be seconds, minutes, hours, or days. This maximum applies both to the metastore-level default and to individual token lifetimes set at recipient creation. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Modifying the Metastore-Level Default

To modify the default recipient token lifetime for the entire [Metastore](/concepts/metastore.md), an account admin uses the Databricks account console. The steps are:

1. Log in to the [account console](https://accounts.cloud.databricks.com/).
2. Navigate to **Catalog** and click the [Metastore](/concepts/metastore.md) name.
3. Under **OpenSharing recipient token lifetime**, click **Edit**.
4. Enable **Set expiration**.
5. Enter a numeric value and select the unit of measure (seconds, minutes, hours, or days).
6. Click **Save**.

The change only applies to recipients created after the modification; existing recipients retain their originally assigned token lifetime. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Effect on Existing Recipients

Changing the metastore-level default token lifetime **does not automatically update** the token lifetimes of existing recipients. To apply a new lifetime to an existing recipient, the provider must rotate the recipient's token. See Rotate a Recipient Token for instructions. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Token Lifetime at Recipient Creation

When creating a recipient, the provider can optionally override the [Metastore](/concepts/metastore.md) default by setting a specific token lifetime. This is done in Catalog Explorer under the **Set expiration** option. If left blank, the token lifetime defaults to the [Metastore](/concepts/metastore.md) configuration. The maximum allowed for any individual token is also one year from creation time. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Expiration Enforcement

Tokens with no explicit expiration date (or a very long lifetime) may be subject to forced expiration by platform policy. For example, all Databricks-to-Open sharing recipient tokens issued before December 8, 2025, with expiration dates after December 8, 2026, or with no expiration date, automatically expire on December 8, 2026. Providers should review long-lived tokens and rotate them as needed to avoid disruptions. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Related Concepts

- [Open Sharing](/concepts/opensharing.md) — The category of sharing that includes bearer token authentication
- Bearer Token Recipient — A non-Databricks user granted data access via token
- [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md) — The top-level container for schemas, tables, and sharing configurations
- Rotate a Recipient Token — The process of refreshing a token and generating a new activation URL
- [Recipient Token Lifetime](/concepts/recipient-token-lifetime.md) — The expiration duration assigned to a specific token

## Sources

- create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md

# Citations

1. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
