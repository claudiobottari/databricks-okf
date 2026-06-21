---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b6df13791081319f9a793171fd9ccf865513d21cc8a4d3887a45b3073eab508c
  pageDirectory: concepts
  sources:
    - create-shares-for-opensharing-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - recipient-property-based-partition-filtering
    - RPPF
  citations:
    - file: create-shares-for-opensharing-databricks-on-aws.md
title: Recipient Property-based Partition Filtering
description: A technique that uses recipient properties (like databricks.accountId) to dynamically deliver only the relevant partition of a table to each recipient, enabling multi-tenant data sharing with a single share object.
tags:
  - delta-sharing
  - partitioning
  - multi-tenancy
timestamp: "2026-06-19T14:39:06.730Z"
---

```markdown
# Recipient Property-based Partition Filtering

**Recipient Property-based Partition Filtering** is a technique in [[OpenSharing]] that allows data providers to share a single table partition across multiple recipients while dynamically delivering only the data that is relevant to each recipient. This approach uses data recipient properties — also known as parameterized partition sharing — to control data boundaries without creating separate shares for each recipient.

## Overview

Instead of creating a separate share for each recipient, providers can define table partitions that reference recipient properties. When a recipient queries the shared data, [[OpenSharing]] dynamically evaluates the recipient's properties and returns only the rows that match. This simplifies share management and ensures data isolation between tenants, accounts, or users. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Default Recipient Properties

The following default properties are available for partition filtering:

- `databricks.accountId`: The Databricks account that a data recipient belongs to ([[Databricks-to-Databricks sharing]] only).
- `databricks.metastoreId`: The Unity Catalog [[metastore|Metastore]] that a data recipient belongs to (Databricks-to-Databricks sharing only).
- `databricks.name`: The name of the data recipient.

^[create-shares-for-opensharing-databricks-on-aws.md]

Providers can also create custom properties when creating or updating a recipient. ^[create-shares-for-opensharing-databricks-on-aws.md]

## How It Works

If a provider's table includes a column such as `account_id` or `country`, they can define a partition filter that maps that column to a recipient property. For example, a partition specification like `(country = CURRENT_RECIPIENT().country)` ensures that each recipient only sees rows where the `country` column matches their assigned `country` property. ^[create-shares-for-opensharing-databricks-on-aws.md]

Without dynamic partition filtering by property, the provider would have to create a separate share for each recipient, which becomes unmanageable at scale. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Specifying Property-Based Partitions

Providers can add property-based partitions using either [[Catalog Explorer]] or the `CURRENT_RECIPIENT` SQL function.

**Using Catalog Explorer:**
1. Open the share and click **Manage assets > Add data assets**.
2. Select the table.
3. Click the **Partition** column and use the syntax: `(<column-name> = CURRENT_RECIPIENT().<property-key>)`
4. Click **Save**.

^[create-shares-for-opensharing-databricks-on-aws.md]

**Using SQL:**
```sql
ALTER SHARE share_name
ADD TABLE inventory
PARTITION (country = CURRENT_RECIPIENT().country);
```

^[create-shares-for-opensharing-databricks-on-aws.md]

## Requirements

- Recipient property-based partition filtering is available on Databricks Runtime 12.2 or above. ^[create-shares-for-opensharing-databricks-on-aws.md]
- The table must be partitioned by the column used in the filter.
- The provider must create recipients with the appropriate properties before sharing.

## Use Cases

- **Multi-tenant data sharing**: A single share delivers data to different Databricks accounts, with each account only seeing its own rows.
- **Regional data isolation**: Recipients in different geographic regions receive only the data relevant to their region.
- **Cross-organization collaboration**: Different partner organizations access a shared dataset, with each organization scoped to its own data segment.

## Related Concepts

- [[OpenSharing]] — The data sharing framework that supports recipient property-based filtering
- Table Partitions — Partition specifications that limit which rows are shared
- [[Recipient Properties]] — Custom attributes assigned to data recipients
- CURRENT_RECIPIENT Function — SQL function that returns the current recipient's properties
- Dynamic Views — An alternative approach to fine-grained access control using views
- [[Databricks-to-Databricks Sharing]] — Sharing protocol that supports default account and [[metastore|Metastore]] properties
- [[Catalog Explorer]] — UI tool for managing shares and partitions

## Sources

- create-shares-for-opensharing-databricks-on-aws.md
```

# Citations

1. [create-shares-for-opensharing-databricks-on-aws.md](/references/create-shares-for-opensharing-databricks-on-aws-1ead08f8.md)
