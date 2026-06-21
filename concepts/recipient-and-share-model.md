---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 482bb7c72408b38740d462ce942a63ff45652554c0900cfa40bc68b2e10728e0
  pageDirectory: concepts
  sources:
    - access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - recipient-and-share-model
    - Share Model and Recipient
    - RASM
    - Share, Provider, Recipient Model
  citations:
    - file: access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
title: Recipient and Share Model
description: The core abstraction in OpenSharing where a data provider creates a 'recipient' representing authorized users and a 'share' representing the tables, volumes, and views to be shared with that recipient.
tags:
  - data-sharing
  - databricks
  - abstraction-model
timestamp: "2026-06-19T17:25:09.046Z"
---

# Recipient and Share Model

The **Recipient and Share Model** is the framework used by [OpenSharing](/concepts/opensharing.md) to represent and manage data shared between a data provider and a data recipient. In this model, the data provider creates two logical objects—a *recipient* and a *share*—to control who can access which data and under what conditions. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Overview

In the OpenSharing standard, a Databricks user (the *data provider*) shares data with a person or group outside their organization (the *data recipient*). The provider creates two distinct objects: a **recipient** that identifies the external user or organization, and a **share** that represents the collection of tables, volumes, and views to be shared. The recipient and share are then linked by the provider's OpenSharing infrastructure. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Recipient

A **recipient** is a representation of the external user or organization that will access the shared data. The data provider creates the recipient in their Databricks account. The recipient object stores identity information and access credentials used to establish the secure sharing connection. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

In the [Databricks-to-Databricks Sharing Model](/concepts/databricks-to-databricks-sharing-model.md), the recipient is created after the recipient provides the provider with a sharing identifier, which is a string in the format `<cloud>:<region>:<uuid>` that uniquely identifies the recipient's Unity Catalog [Metastore](/concepts/metastore.md). ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Share

A **share** is a logical container that represents the specific data assets (tables, volumes, and views) to be shared with a recipient. The data provider creates the share and populates it with the data they wish to grant access to. Multiple recipients can be granted access to the same share, or a single share can contain data for a specific recipient. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

The share does not contain the actual data; rather, it is a representation that points to the underlying Unity Catalog objects. Updates to the source data are available to recipients in near real time. Recipients can read and make copies of the shared data but cannot modify the source data. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Relationship to Sharing Models

The Recipient and Share Model applies to both the Databricks-to-Databricks sharing model and the [Databricks-to-Open Sharing Model](/concepts/databricks-to-open-sharing-model.md):

- **Databricks-to-Databricks model:** The provider creates the recipient using the recipient's sharing identifier. No credential file is needed; the secure connection is managed by Databricks, and the shared data becomes automatically discoverable in the recipient's workspace. Granular access control can be configured by the recipient's team. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]
- **Databricks-to-Open sharing model:** The provider creates the recipient and share, then sends the recipient an activation URL or portal link. The recipient follows the link to download a credential file (for bearer tokens) or a URL (for [OIDC federation](/concepts/oidc-federation-policy.md)). The credential file or URL is used to authenticate and access the shared data using any compatible tool, including Databricks, Apache Spark, pandas, Power BI, and Tableau. Bearer tokens are valid for a maximum of one year after creation; providers manage token expiration and rotation. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Lifecycle and Management

- **Creation:** The provider creates the recipient and share objects in their Databricks account. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]
- **Access duration:** Access persists as long as the underlying token is valid (for bearer tokens) or as long as the provider continues to share the data, depending on the authentication method. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]
- **Updates:** Changes to the source data are available to recipients in near real time. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]
- **Revocation:** The provider can revoke access by modifying or deleting the recipient or share objects. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Security Considerations

- Activation links should not be shared with anyone not intended to have access. A credential file can be downloaded only once; if the activation link is visited after download, the download button is disabled. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]
- Credential files should be stored securely and not shared outside the group of authorized users. Databricks recommends using a password manager for internal sharing. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]
- Databricks may collect information about recipients' use of and access to shared data and may share it with the applicable data provider. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The open standard for secure data sharing that defines the recipient and share model.
- [Unity Catalog](/concepts/unity-catalog.md) — The Databricks data governance solution that enables Databricks-to-Databricks sharing.
- [Delta Sharing](/concepts/delta-sharing.md) — The underlying protocol implementation for OpenSharing.
- [Sharing Identifier](/concepts/sharing-identifier.md) — The unique [Metastore](/concepts/metastore.md) identifier used to establish Databricks-to-Databricks connections.
- Credential File — The authentication artifact used in the Databricks-to-Open sharing model with bearer tokens.
- OIDC Federation — An alternative authentication method for Databricks-to-Open sharing.

## Sources

- access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md

# Citations

1. [access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md](/references/access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws-7bb360b8.md)
