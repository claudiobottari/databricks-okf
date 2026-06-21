---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 349ac75b252bdf9b64bd0dfbb620958d1bffd37bd5a5a7f01fd63446cf9a0225
  pageDirectory: concepts
  sources:
    - create-shares-for-opensharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - partition-sharing-and-parameterized-partition-filtering
    - Parameterized Partition Filtering and Partition Sharing
    - PSAPPF
  citations:
    - file: create-shares-for-opensharing-databricks-on-aws.md
title: Partition Sharing and Parameterized Partition Filtering
description: Sharing only a subset of a table's data via partition specifications, including dynamic filtering using recipient properties (CURRENT_RECIPIENT) to deliver different data to different recipients from a single share.
tags:
  - delta-sharing
  - partitioning
  - access-control
timestamp: "2026-06-18T14:55:21.551Z"
---

# Partition Sharing and Parameterized Partition Filtering

**Partition Sharing** refers to sharing only a subset of a table's data by specifying a partition specification when adding a table to a Delta share. **Parameterized Partition Filtering** extends this concept by allowing partition values to be dynamically determined based on recipient properties at query time, rather than being statically defined.

## Overview

When sharing tables through Delta Sharing, data providers may want to restrict recipients to only a portion of a table rather than the entire dataset. Partition sharing enables this by allowing providers to specify which partitions of a table are shared. With parameterized partition filtering, the provider can create a single share that dynamically delivers different partitions to different recipients based on their properties. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Static Partition Sharing

To share only part of a table, provide a partition specification when adding the table to a share. Partitions can be specified using Catalog Explorer, the Databricks Unity Catalog CLI, or SQL commands in a Databricks notebook or the Databricks SQL query editor. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Example

The following SQL example shares specific partitions of the `inventory` table, partitioned by the `year`, `month`, and `date` columns: ^[create-shares-for-opensharing-databricks-on-aws.md]

```sql
ALTER SHARE share_name
ADD TABLE inventory
PARTITION (year = "2021"),
          (year = "2020", month = "Dec"),
          (year = "2019", month = "Dec", date = "2019-12-25");
```

This shares data for the year 2021, December 2020, and December 25, 2019.

## Parameterized Partition Filtering

Parameterized partition filtering uses recipient properties to dynamically filter partitions at query time. This is also known as parameterized partition sharing. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Recipient Properties

Default properties available for filtering include: ^[create-shares-for-opensharing-databricks-on-aws.md]

- `databricks.accountId`: The Databricks account that a data recipient belongs to (Databricks-to-Databricks sharing only)
- `databricks.metastoreId`: The Unity Catalog [Metastore](/concepts/metastore.md) that a data recipient belongs to (Databricks-to-Databricks sharing only)
- `databricks.name`: The name of the data recipient

Custom properties can be created when creating or updating a recipient.

### How It Works

Filtering by recipient property enables providers to share the same tables, using the same share, across multiple Databricks accounts, workspaces, and users while maintaining data boundaries between them. For example, if tables include a Databricks account ID column, a single share can be created with table partitions defined by Databricks account ID. When shared, OpenSharing dynamically delivers to each recipient only the data associated with their Databricks account. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Specifying Parameterized Partitions

To specify a partition that filters by recipient properties, use the `CURRENT_RECIPIENT` SQL function in the partition specification. Recipient properties are available on Databricks Runtime 12.2 or above. ^[create-shares-for-opensharing-databricks-on-aws.md]

Using Catalog Explorer: ^[create-shares-for-opensharing-databricks-on-aws.md]

1. Open the share in Catalog Explorer under **OpenSharing** > **Shared by me**
2. Click **Manage assets > Add data assets**
3. Select the table, then click on the partition column to add a partition
4. Use the following syntax for the partition specification:
   ```
   (<column-name> = CURRENT_RECIPIENT().<property-key>)
   ```
   For example: `(country = CURRENT_RECIPIENT().country)`

Using SQL: ^[create-shares-for-opensharing-databricks-on-aws.md]

```sql
ALTER SHARE share_name
ADD TABLE inventory
PARTITION (country = CURRENT_RECIPIENT().country);
```

### Benefits

Without parameterized partition filtering, providers would need to create a separate share for each recipient. Parameterized partitioning reduces the number of shares needed and simplifies share management. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Cloud Token Eligibility and Partitions

For cloud token (directory-based) access to be used, tables must be shared without a partition filter. If a partition filter is applied, cloud token access is not used. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The framework for sharing data across platforms
- [OpenSharing](/concepts/opensharing.md) — Databricks' implementation of the Delta Sharing protocol
- [Shares, Providers, and Recipients](/concepts/recipient-and-share-model.md) — The sharing model in Unity Catalog
- CURRENT_RECIPIENT Function — SQL function for dynamic partition filtering
- [Create Shares for OpenSharing](/concepts/delta-sharing-open-sharing.md) — How to create and manage shares
- Manage Recipients — Creating recipients and their properties

## Sources

- create-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [create-shares-for-opensharing-databricks-on-aws.md](/references/create-shares-for-opensharing-databricks-on-aws-1ead08f8.md)
