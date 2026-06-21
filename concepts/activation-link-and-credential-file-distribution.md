---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 95759ace311a6f7e52a07eea2a4be0bcececfd89e69958cdbe7ad0363adcd845
  pageDirectory: concepts
  sources:
    - create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - activation-link-and-credential-file-distribution
    - Credential File Distribution and Activation Link
    - ALACFD
  citations:
    - file: create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md
title: Activation Link and Credential File Distribution
description: The mechanism by which a Delta Sharing data provider shares connection information with a recipient via a secure activation link that allows one-time download of a credential file containing the bearer token.
tags:
  - delta-sharing
  - security
  - data-sharing
timestamp: "2026-06-18T11:15:38.083Z"
---

# Activation Link and Credential File Distribution

**Activation Link and Credential File Distribution** refers to the workflow by which a data provider shares connection information with non-Databricks recipients who use bearer tokens to access shared data through Databricks-to-Open sharing (OpenSharing). This process is part of the bearer token authentication flow for OpenSharing recipients.

## Overview

When a data provider creates a recipient object in their Unity Catalog [Metastore](/concepts/metastore.md) using the bearer token method, Databricks generates a token, a credential file that includes the token, and an activation link for the provider to share with the recipient. The recipient object has the authentication type of `TOKEN`. The recipient accesses the activation link, downloads the credential file, and uses the credential file to authenticate and get read access to the tables included in the shares they have been granted access to. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Providing the Activation Link to Recipients

After creating a recipient and granting access to shares, the data provider must send the recipient their connection information using a secure channel. This includes the activation link and a link to instructions for using it. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

The credential file can be downloaded only once. Recipients should treat the downloaded credential as a secret and must not share it outside of their organization. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

### Getting the Activation Link

To retrieve a recipient's activation link, the provider can use Catalog Explorer, the Databricks Unity Catalog CLI, or the `DESCRIBE RECIPIENT` SQL command. Once the recipient has downloaded the credential file, the activation link is no longer returned or displayed. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

**Permissions required**: [Metastore](/concepts/metastore.md) admin, user with the `USE RECIPIENT` privilege, or the recipient object owner. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Security Considerations

If a provider has concerns that a credential may have been handled insecurely, they can [rotate a recipient's credential](https://docs.databricks.com/aws/en/delta-sharing/create-recipient-token#rotate-credential) at any time. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

If an activation URL is inadvertently sent to the wrong person or is sent over an insecure channel, Databricks recommends that the provider: ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

1. Revoke the recipient's access to the share.
2. Rotate the recipient and set the existing token to expire immediately.
3. Share the new activation URL with the intended recipient over a secure channel.
4. After the activation URL has been accessed, grant the recipient access to the share again.

## Rotating Tokens and Generating New Activation Links

When a recipient's token is rotated (for example, due to expiration, compromise, or credential loss), a new activation URL is generated. If all recipient tokens have expired, rotating the token replaces the existing activation URL with a new one. Databricks recommends promptly rotating or dropping a recipient whose token has expired. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

If the recipient imported the credential as a provider object in Unity Catalog, they must update the provider object with the Databricks REST API after receiving a new activation link. ^[create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for secure data sharing
- [OpenSharing](/concepts/opensharing.md) — Sharing data with recipients who do not have Databricks workspaces
- [Bearer Token Authentication](/concepts/bearer-token-authentication-for-open-sharing.md) — Authentication method for OpenSharing recipients
- Recipient Object — The Unity Catalog object representing a data sharing recipient
- [Credential Rotation](/concepts/provider-credential-rotation.md) — The process of replacing compromised or expired credentials

## Sources

- create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md

# Citations

1. [create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws.md](/references/create-a-recipient-object-for-non-databricks-users-using-bearer-tokens-databricks-to-open-sharing-databricks-on-aws-6b15f526.md)
