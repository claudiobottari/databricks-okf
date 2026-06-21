---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dcfdcd92a3d1c6bc91d3747cc752d1d7a0a44e07ba2de9f9bce1fe126256bb35
  pageDirectory: concepts
  sources:
    - access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
    - what-is-the-opensharing-databricks-to-databricks-protocol-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - opensharing-sharing-identifier
    - OSI
  citations:
    - file: access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
    - file: what-is-the-opensharing-databricks-to-databricks-protocol-databricks-on-aws.md
title: OpenSharing Sharing Identifier
description: A unique string in the format '<cloud>:<region>:<uuid>' that identifies a Unity Catalog metastore, used to establish Databricks-to-Databricks sharing connections.
tags:
  - identifier
  - unity-catalog
  - metastore
timestamp: "2026-06-19T13:51:39.640Z"
---

# OpenSharing Sharing Identifier

The **OpenSharing Sharing Identifier** is a unique string that identifies a [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md) for the purpose of establishing a secure data sharing connection between two Databricks workspaces. It is a foundational component of the [Databricks-to-Databricks OpenSharing Protocol](/concepts/databricks-to-databricks-opensharing-protocol.md), enabling data providers and recipients to authenticate and connect across different Databricks accounts, cloud regions, or cloud providers.

## Format

The sharing identifier is a string consisting of the [Metastore](/concepts/metastore.md)'s cloud provider, region, and UUID, formatted as:

```
<cloud>:<region>:<uuid>
```

For example: `aws:eu-west-1:b0c978c8-3e68-4cdf-94af-d05c120ed1ef`. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Purpose

In the Databricks-to-Databricks sharing model, the sharing identifier serves as the key identifier that enables the secure connection between the provider's and recipient's Unity Catalog metastores. The data recipient provides this identifier to the data provider, who then uses it to create a recipient object that represents the user or group of users who will access the shared data. ^[what-is-the-opensharing-databricks-to-databricks-protocol-databricks-on-aws.md]

## How to Obtain the Sharing Identifier

### Using Catalog Explorer

1. In your Databricks workspace, click the **Catalog** icon.
2. At the top of the **Catalog** pane, click the gear icon and select **OpenSharing** (alternatively, click **Share > OpenSharing** in the upper-right corner).
3. On the **Shared with me** tab, select your Databricks sharing organization name in the upper right, and select **Copy sharing identifier**.

^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

### Using a Notebook or SQL Query

Use the default SQL function `CURRENT_METASTORE`. A notebook running this function must use a standard or dedicated access mode in the workspace used to access the shared data.

```sql
SELECT CURRENT_METASTORE();
```

^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Role in the Sharing Workflow

The sharing identifier is used in the Databricks-to-Databricks OpenSharing workflow as follows:

1. The data recipient provides their sharing identifier to the data provider over a secure channel.
2. The data provider creates a recipient object in their Unity Catalog [Metastore](/concepts/metastore.md), including the sharing identifier.
3. The provider grants the recipient access to a share (a collection of tables, views, volumes, and notebooks).
4. The share becomes automatically discoverable in the recipient's Databricks workspace without requiring any credential file.

^[what-is-the-opensharing-databricks-to-databricks-protocol-databricks-on-aws.md, access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Comparison with Databricks-to-Open Sharing

The sharing identifier is only used in the **Databricks-to-Databricks** sharing model. In the **Databricks-to-Open** sharing model, recipients receive an activation URL or portal link from the data provider, which they use to download a credential file or URL for accessing the shared data. No sharing identifier is exchanged in that model. ^[access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution that underpins OpenSharing on Databricks
- [Databricks-to-Databricks OpenSharing Protocol](/concepts/databricks-to-databricks-opensharing-protocol.md) — The protocol that uses the sharing identifier for secure connections
- [Databricks-to-Open Sharing Protocol](/concepts/databricks-to-open-sharing-protocol.md) — The alternative protocol for sharing with any computing platform
- [OpenSharing](/concepts/opensharing.md) — The open standard for secure data sharing
- Recipient object — The named object created by the data provider that includes the sharing identifier
- Share — A collection of data assets shared with a recipient

## Sources

- access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
- what-is-the-opensharing-databricks-to-databricks-protocol-databricks-on-aws.md

# Citations

1. [access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md](/references/access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws-7bb360b8.md)
2. [what-is-the-opensharing-databricks-to-databricks-protocol-databricks-on-aws.md](/references/what-is-the-opensharing-databricks-to-databricks-protocol-databricks-on-aws-53f3616c.md)
