---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cfc1bcc35f688db15e4adff8310bfa3d15e99775a70a66817cc2e27f9f96826a
  pageDirectory: concepts
  sources:
    - access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
    - share-data-between-sap-business-data-cloud-bdc-and-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - opensharing
    - Open Sharing
    - Set up OpenSharing
    - Share (OpenSharing)
    - What is OpenSharing?
  citations:
    - file: access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
    - file: share-data-between-sap-business-data-cloud-bdc-and-databricks-databricks-on-aws.md
    - file: opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md
    - file: share-a-genie-space-using-opensharing-databricks-on-aws.md
title: OpenSharing
description: An open standard for secure data sharing, supporting both Databricks-to-Databricks and Databricks-to-Open sharing models.
tags:
  - data-sharing
  - security
  - databricks
timestamp: "2026-06-19T21:55:48.546Z"
---

# OpenSharing

**OpenSharing** is an open standard for secure data sharing that enables organizations to share data and AI assets across organizational boundaries without moving or replicating the underlying data. Built on an open protocol, OpenSharing supports two primary sharing models: Databricks-to-Databricks sharing and Databricks-to-Open sharing. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Overview

In OpenSharing, a *data provider* (a Databricks user or organization) shares data with a *data recipient* (a person or group outside their organization). The shared data remains in place and is not moved or replicated, providing live, zero-copy access. Recipients can read and make copies of the shared data but cannot modify the source data. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

The standard is designed for secure data exchange across different platforms and tools, with support for security protocols such as mutual Transport Layer Security (mTLS) and OpenID Connect (OIDC). ^[share-data-between-sap-business-data-cloud-bdc-and-databricks-databricks-on-aws.md]

## Sharing Models

OpenSharing supports two distinct sharing models, each suited to different recipient scenarios.

### Databricks-to-Databricks Sharing

In the Databricks-to-Databricks model, the recipient must be a user on a Databricks workspace that is enabled for [Unity Catalog](/concepts/unity-catalog.md). The data provider and recipient establish a secure connection using a unique sharing identifier for the recipient's Unity Catalog [Metastore](/concepts/metastore.md). ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

The sharing identifier is a string consisting of the [Metastore](/concepts/metastore.md)'s cloud, region, and UUID, in the format `<cloud>:<region>:<uuid>` (for example, `aws:eu-west-1:b0c978c8-3e68-4cdf-94af-d05c120ed1ef`). Recipients can obtain this identifier using Catalog Explorer or the SQL function `CURRENT_METASTORE`. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

Once the connection is established, the shared data becomes automatically discoverable in the recipient's Databricks workspace without requiring any credential file. Databricks handles the secure connection, and the recipient's team can configure granular access control on the shared data as needed. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

### Databricks-to-Open Sharing

In the Databricks-to-Open sharing model, recipients can use any tool (including Databricks, Apache Spark, pandas, Power BI, or Tableau) to access the shared data. The data provider sends the recipient an activation URL or portal link over a secure channel. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

The recipient follows the link to download a credential file or URL that authenticates them to the data provider's account. Both bearer tokens and OAuth Client Credentials are supported. Access persists as long as the underlying token is valid and the provider continues to share the data. Tokens are valid for a maximum of one year after creation. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

For OIDC federation, recipients use a URL to authenticate via a user-to-machine (U2M) or machine-to-machine (M2M) flow, enabling access from tools like Tableau and Power BI or from Python client applications. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Key Concepts

### Data Provider and Data Recipient

A *data provider* is a Databricks user who shares data using OpenSharing. A *data recipient* is a person or group outside the provider's organization who receives access to the shared data. The shared data is not provided by Databricks directly but by data providers running on Databricks. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

### Shares and Recipients

To share data, a provider creates:
- A *recipient* in their Databricks account to represent the users who will access the data.
- A *share*, which is a representation of the tables, volumes, views, and partitions to be shared. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

### Zero-Copy Sharing

OpenSharing provides live, zero-copy access to shared data. Data remains in place and is not moved or replicated. Updates to the data are available to recipients in near real time. This approach eliminates data silos and reduces the complexity and cost of traditional data extraction. ^[share-data-between-sap-business-data-cloud-bdc-and-databricks-databricks-on-aws.md]

## Integration with SAP Business Data Cloud

The SAP Business Data Cloud (BDC) Connector for Databricks uses OpenSharing to enable seamless data sharing between SAP BDC and Databricks. Organizations can access and analyze SAP BDC data directly from their Databricks workspace that is enabled for Unity Catalog. ^[share-data-between-sap-business-data-cloud-bdc-and-databricks-databricks-on-aws.md]

When SAP BDC shares are mounted to Unity Catalog catalogs, semantic metadata such as table and column comments, primary keys, foreign keys, and governance tags syncs automatically into Unity Catalog, making SAP data more understandable and discoverable. This metadata can be used across Databricks, including in Catalog Explorer, SQL queries, Genie Spaces, and governance policies. ^[share-data-between-sap-business-data-cloud-bdc-and-databricks-databricks-on-aws.md]

To establish a connection between Databricks and SAP BDC, a Databricks workspace admin with `CREATE PROVIDER` and `CREATE RECIPIENT` privileges and an SAP BDC admin must coordinate. The process involves exchanging connection identifiers and invitation links to set up a secure Third Party Connection. ^[share-data-between-sap-business-data-cloud-bdc-and-databricks-databricks-on-aws.md]

## Security and Governance

OpenSharing implements security protocols including mutual Transport Layer Security (mTLS) and OpenID Connect (OIDC) for safe data exchanges. When integrated with Unity Catalog, full governance and auditing capabilities are maintained. ^[share-data-between-sap-business-data-cloud-bdc-and-databricks-databricks-on-aws.md]

Databricks may collect information about data recipients' use of and access to the shared data (including identifying any individual or company who accesses the data using the credential file) and may share it with the applicable data provider. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## SecureConnect Firewall Configuration

When a provider enables [OpenSharing SecureConnect](/concepts/opensharing-secureconnect.md), recipients on classic compute and open recipients must allowlist Databricks inbound IP addresses for the provider's cloud and region to access shares. Recipients on serverless compute do not need to configure their egress firewall because Databricks routes serverless traffic to SecureConnect internally. The following limitations apply: mTLS is not enabled for recipients using classic compute, mTLS is not enabled for OIDC recipients, and serverless Databricks recipients using a Databricks-to-Open credential in the same region as the provider are not supported. ^[opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md]

## Sharing Genie Spaces (Beta)

OpenSharing allows sharing a Genie Space with users outside your organization. When you share a Genie Space, Databricks creates a point-in-time snapshot of the space's data assets and instructions and makes it available to selected recipients. Recipients can mount the share to create a local Genie Space pre-loaded with the data and instructions. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

Requirements include the [Genie Agent Sharing Preview](/concepts/genie-agent-sharing-preview.md) enabled at the account level, `CREATE SHARE` privilege on the Unity Catalog [Metastore](/concepts/metastore.md), `CAN EDIT` or higher on the Genie Space, and `SELECT` on all data assets. The snapshot is captured at the time you click **Share**. You can add more recipients to the same snapshot, but cannot modify the data assets in the share after creation. Limitations include: the share is a snapshot only, the Genie Space configuration must be less than 256 KB when compressed, and Genie Spaces that include metric views cannot be shared. ^[share-a-genie-space-using-opensharing-databricks-on-aws.md]

## Best Practices

- **Protect activation links**: Don't share activation links with anyone. A credential file can be downloaded only once. If you lose the activation link before using it, contact the data provider. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]
- **Store credentials securely**: Don't share credential files with anyone outside the group of users who should have access to the shared data. Databricks recommends using a password manager for sharing within your organization. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]
- **Use VPC gateway endpoints**: Use VPC gateway endpoints or interface endpoints for S3 instead of NAT gateways for in-region storage access whenever possible to reduce costs and enhance security. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]
- **Monitor access**: If you have access to a Databricks workspace, use Databricks audit logs to understand who in your organization is accessing which data using OpenSharing. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that integrates with OpenSharing
- [Delta Sharing](/concepts/delta-sharing.md) — The underlying protocol for OpenSharing data exchange
- [SAP Business Data Cloud Connector](/concepts/sap-business-data-cloud-bdc-connector.md) — Integration that uses OpenSharing for SAP data sharing
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md) — Permissions required for setting up OpenSharing connections
- OIDC Federation — Authentication method supported in the Databricks-to-Open model
- Genie Space — A conversational analytics feature that can be shared via OpenSharing

## Sources

- access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
- share-data-between-sap-business-data-cloud-bdc-and-databricks-databricks-on-aws.md
- grant-sap-business-data-cloud-bdc-recipients-access-to-opensharing-data-shares-databricks-on-aws.md
- manage-access-to-opensharing-data-shares-for-providers-databricks-on-aws.md
- opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md
- share-a-genie-space-using-opensharing-databricks-on-aws.md

# Citations

1. [access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md](/references/access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws-7bb360b8.md)
2. [share-data-between-sap-business-data-cloud-bdc-and-databricks-databricks-on-aws.md](/references/share-data-between-sap-business-data-cloud-bdc-and-databricks-databricks-on-aws-2f32cce2.md)
3. [opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws.md](/references/opensharing-recipient-firewall-configuration-for-secureconnect-databricks-on-aws-029f12f3.md)
4. [share-a-genie-space-using-opensharing-databricks-on-aws.md](/references/share-a-genie-space-using-opensharing-databricks-on-aws-d29bfca3.md)
