---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 85907e4d6fade1233b684aa730541c32ae62d26ef2e5c3d249f57da0495f9951
  pageDirectory: concepts
  sources:
    - create-shares-for-opensharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - parameterized-partition-sharing-recipient-properties
    - PPS(P
  citations:
    - file: create-shares-for-opensharing-databricks-on-aws.md
title: Parameterized Partition Sharing (Recipient Properties)
description: A technique for sharing table partitions that match data recipient properties (e.g., databricks.accountId, databricks.metastoreId, databricks.name, or custom properties). Enables a single share to dynamically deliver different data to different recipients while maintaining data boundaries, using the CURRENT_RECIPIENT() SQL function.
tags:
  - delta-sharing
  - data-governance
  - partitioning
timestamp: "2026-06-19T18:02:07.111Z"
---

# Parameterized Partition Sharing (Recipient Properties)

**Parameterized Partition Sharing (Recipient Properties)** is a feature in [OpenSharing](/concepts/opensharing.md) that enables dynamic partition filtering based on recipient-specific properties. It allows data providers to share the same tables using a single share while automatically delivering only the data relevant to each recipient, maintaining data boundaries between different Databricks accounts, workspaces, and users. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Overview

When sharing table partitions, providers can specify partition filters that reference recipient properties rather than static values. This approach uses the `CURRENT_RECIPIENT()` SQL function to dynamically evaluate which partition each recipient should see at query time. ^[create-shares-for-opensharing-databricks-on-aws.md]

Without parameterized partition sharing, providers would need to create a separate share for each recipient, which becomes impractical when managing many recipients. Parameterized partitions solve this by enabling a single share to serve multiple recipients with distinct data boundaries. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Default Recipient Properties

The following default properties are available for use in partition specifications:

- `databricks.accountId`: The Databricks account that a data recipient belongs to (Databricks-to-Databricks sharing only).
- `databricks.metastoreId`: The Unity Catalog [Metastore](/concepts/metastore.md) that a data recipient belongs to (Databricks-to-Databricks sharing only).
- `databricks.name`: The name of the data recipient.

^[create-shares-for-opensharing-databricks-on-aws.md]

## Custom Recipient Properties

In addition to the default properties, providers can create any custom property when creating or updating a recipient. These custom properties can then be used in partition specifications to filter data based on arbitrary attributes defined by the provider. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Requirements

Recipient properties are available on Databricks Runtime 12.2 or above. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Specifying Parameterized Partitions

To specify a partition that filters by recipient properties, use the `CURRENT_RECIPIENT()` SQL function with the following syntax:

```
(<column-name> = CURRENT_RECIPIENT().<property-key>)
```

For example, if a table includes a `country` column and each recipient has a `country` property, the partition specification would be:

```
(country = CURRENT_RECIPIENT().country)
```

^[create-shares-for-opensharing-databricks-on-aws.md]

### Using Catalog Explorer

1. In your Databricks workspace, navigate to **Catalog** and open the **OpenSharing** settings.
2. On the **Shared by me** tab, select the share you want to update.
3. Click **Manage assets > Add data assets**.
4. Select the catalog, database, and table to share.
5. Under the **Partition** column, click the add icon.
6. In the **Add partition to the table** dialog, enter the property-based partition specification using the `CURRENT_RECIPIENT()` syntax.
7. Click **Save**.

^[create-shares-for-opensharing-databricks-on-aws.md]

## Example Use Case

Consider a scenario where tables include a Databricks account ID column. A provider can create a single share with table partitions defined by Databricks account ID. When the share is accessed, OpenSharing dynamically delivers to each recipient only the data associated with their Databricks account. This eliminates the need to create and manage separate shares for each recipient account. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The data sharing framework that supports parameterized partitions.
- [Recipient Properties](/concepts/recipient-properties.md) — The properties defined on recipients that drive dynamic partition filtering.
- CURRENT_RECIPIENT Function — The SQL function used to access recipient properties in partition specifications.
- [Create Shares for OpenSharing](/concepts/delta-sharing-open-sharing.md) — The process of creating and managing shares.
- Manage Recipients — Creating and updating recipients with custom properties.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that manages shares and recipients.

## Sources

- create-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [create-shares-for-opensharing-databricks-on-aws.md](/references/create-shares-for-opensharing-databricks-on-aws-1ead08f8.md)
