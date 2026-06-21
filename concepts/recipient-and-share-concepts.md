---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2670364e4a271da171220471c11fa5c8213e7235d3a0a33cae6f8bd90cfbe343
  pageDirectory: concepts
  sources:
    - access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - recipient-and-share-concepts
    - share concepts and Recipient
    - RASC
    - Recipient|recipients
    - Shares, Providers, and Recipients
    - Shares, providers, and recipients
  citations:
    - file: access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
title: Recipient and share concepts
description: Fundamental OpenSharing abstractions where a provider creates a 'recipient' to represent the data consumer and a 'share' representing the tables, volumes, and views to be shared.
tags:
  - data-sharing
  - abstractions
  - databricks
timestamp: "2026-06-18T10:38:08.216Z"
---

# Recipient and Share Concepts

**Recipient** and **Share** are two core abstractions in [OpenSharing](/concepts/opensharing.md) (formerly Delta Sharing) that model the two sides of a secure data-sharing relationship: the consuming organization or person (*recipient*) and the collection of data objects being made available (*share*). A data provider in Databricks creates both entities in their Unity Catalog [Metastore](/concepts/metastore.md) to enable secure, governed data sharing with consumers outside their organization.^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Overview

OpenSharing is an open standard for secure data sharing. A Databricks user (the *data provider*) can use OpenSharing to share data with a person or group outside their organization—the *data recipient*. The provider creates a **recipient** to represent the external consumer and a **share** to define which tables, volumes, and views are made available.^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

Two sharing models exist:

- **Databricks-to-Databricks sharing**: Both parties use Databricks workspaces with [Unity Catalog](/concepts/unity-catalog.md) enabled. The recipient provides their [Metastore](/concepts/metastore.md)'s unique sharing identifier, and the provider uses that to create the sharing connection. Shared data becomes automatically discoverable in the recipient's workspace.
- **Databricks-to-Open sharing (open sharing)**: The recipient can use any tool (including Databricks, Apache Spark, pandas, or Power BI) to access the data. The provider sends an activation URL or portal link over a secure channel.

^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Recipient

A **recipient** is a logical representation, created in the data provider's Unity Catalog [Metastore](/concepts/metastore.md), that identifies a specific person, group, or organization outside the provider's boundary that will receive access to shared data.^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

### Recipient Types

| Sharing Model | Recipient Representation | How Access Is Established |
|---|---|---|
| **Databricks-to-Databricks** | A recipient object linked to the consumer's [Metastore](/concepts/metastore.md) UUID | The provider uses the recipient's sharing identifier to create a direct, workspace-integrated connection. No credential file is needed. |
| **Databricks-to-Open (bearer token)** | A recipient associated with a downloadable credential file | The provider sends an activation URL; the recipient follows it to download a bearer-token credential file (once only). |
| **Databricks-to-Open (OIDC federation)** | A recipient associated with an OIDC federation URL | The provider sends a portal URL; the recipient authenticates via OpenID Connect (OIDC) using their own identity provider. |

^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

### Recipient in the Databricks-to-Databricks Model

In the Databricks-to-Databricks model, the recipient is a Databricks workspace user whose Unity Catalog [Metastore](/concepts/metastore.md) has a unique **sharing identifier**—a string in the format `<cloud>:<region>:<uuid>` (e.g., `aws:eu-west-1:b0c978c8-3e68-4cdf-94af-d05c120ed1ef`). The provider obtains this identifier and uses it to create a secure sharing connection. The shared data then becomes available in the recipient's workspace, where a team member can configure granular access controls.^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

To retrieve the sharing identifier:

- **Via Catalog Explorer**: Click **Catalog**, then the gear icon, select **OpenSharing**, and on the **Shared with me** tab, select your organization name and **Copy sharing identifier**.
- **Via SQL**: Use `SELECT CURRENT_METASTORE()` (requires a standard or dedicated access mode compute resource).

^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

### Recipient in the Databricks-to-Open Sharing Model

In the open sharing model, the provider creates a recipient and then sends the recipient an **activation URL** or **portal URL** over a secure channel. The recipient follows the link to download a credential file (for bearer tokens) or receives a URL (for OIDC federation). The credential file can be downloaded only once; if the activation link is visited again after download, the button is disabled. If the activation link is lost before use, the recipient must contact the data provider.^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

The credential file must be stored in a secure location and not shared with anyone outside the authorized user group. Databricks recommends using a password manager for internal sharing. Access persists as long as the underlying token is valid and the provider continues to share the data. Tokens are valid for a maximum of one year after creation. Providers manage token expiration and rotation.^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Share

A **share** is a representation of the tables, volumes, and views that a data provider intends to make available to one or more recipients. It is the container of the data objects being shared. When a provider creates a share, they specify which securable objects (tables, volumes, or views) are included. The share is then attached to one or more recipients to grant them access.^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

### What a Share Contains

- **Tables** and their partitions
- **Volumes**
- **Views** (logical representations of data)

The share defines the scope of data that a recipient can read and copy, but the recipient cannot modify the source data. Updates to the shared data are available to the recipient in near real time.^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## How Recipients and Shares Work Together

The provider-recipient-share relationship follows this flow:

1. **Provider identifies the recipient**: The provider determines who will receive the data and creates a recipient object in their [Metastore](/concepts/metastore.md).
2. **Provider defines the share**: The provider creates a share containing the specific tables, volumes, and views to be shared.
3. **Provider attaches the share to the recipient**: The recipient is associated with the share, establishing the access grant.
4. **Recipient accesses the data**: The recipient uses the appropriate method (direct integration via sharing identifier, credential file, or OIDC federation URL) to read the data.

The provider manages all aspects: creating and modifying recipients and shares, managing token expiration and rotation, and controlling what data is included in the share. Recipients only consume the data; they cannot modify the source.^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Security Considerations

- **Sharing identifiers**: The recipient's sharing identifier acts as a lookup key. Databricks may collect information about data recipients' use of and access to shared data (including identifying individuals or companies accessing the data using the credential file) and may share it with the applicable data provider.
- **Activation URLs**: Must not be shared with unauthorized parties. The credential file can be downloaded only once.
- **Credential files**: Must be stored securely. Databricks recommends password managers for internal sharing.
- **Token validity**: Bearer tokens are valid for a maximum of one year. Providers manage rotation and expiration.

## Best Practices

- **Use VPC gateway endpoints or interface endpoints for S3** instead of NAT gateways for in-region storage access to reduce costs and enhance security.^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]
- **Don't share activation links** with anyone outside the authorized recipient group.
- **Store credential files in a password manager** if you need to share them internally.
- **Audit access** using Databricks Audit Logs to monitor who in your organization is accessing which shared data.

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The open standard for secure data sharing
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that manages recipients and shares
- Delta Sharing Data Provider — The role and responsibilities of data providers
- [Delta Sharing Data Recipient](/concepts/delta-sharing-recipient-object.md) — How to read shared data as a recipient
- [OpenSharing OIDC Federation](/concepts/opensharing-with-oidc-federation.md) — Authentication using OpenID Connect
- Databricks Audit Logs — Monitoring data sharing access

## Sources

- access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md

# Citations

1. [access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md](/references/access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws-7bb360b8.md)
