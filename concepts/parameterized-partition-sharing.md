---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fc61a18d747d425fbadd8fcebc342d07b071bb054513f47ff483f99274c97ac2
  pageDirectory: concepts
  sources:
    - create-shares-for-opensharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - parameterized-partition-sharing
    - PPS
    - parameterized-partition-sharing-recipient-properties
    - PPS(P
  citations:
    - file: create-shares-for-opensharing-databricks-on-aws.md
title: Parameterized Partition Sharing
description: A technique using the CURRENT_RECIPIENT() function to dynamically filter table partitions based on recipient properties, enabling a single share to serve multiple recipients with data boundaries maintained.
tags:
  - delta-sharing
  - partitioning
  - access-control
timestamp: "2026-06-19T09:38:26.454Z"
---

# Parameterized Partition Sharing

**Parameterized Partition Sharing** is a feature in [Delta Sharing](/concepts/delta-sharing.md) ([OpenSharing](/concepts/opensharing.md)) that allows data providers to share only a subset of a table's data to each recipient, based on the recipient's properties such as account ID, [Metastore](/concepts/metastore.md) ID, or name. Instead of creating separate shares for each recipient, a single share can dynamically deliver partitioned data to each recipient using recipient-defined property conditions. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Overview

Parameterized partition sharing uses recipient properties to filter table partitions at the time of access. When a provider adds a table to a share with a partition specification that includes a `CURRENT_RECIPIENT()` function call referencing a property key, OpenSharing evaluates the partition condition against the recipient's properties at query time and returns only the matching data. ^[create-shares-for-opensharing-databricks-on-aws.md]

Without parameterized partition sharing, a provider would need to create a distinct share for every recipient that required different subsets of data, even when the data was in the same table. With parameterized partitions, a single share can serve many recipients, each seeing only their own data. ^[create-shares-for-opensharing-databricks-on-aws.md]

## How It Works

### Recipient Properties

Recipient properties are attributes defined on a [recipient](/concepts/data-recipient.md) object that OpenSharing uses to determine which partition to deliver. Default properties include:

- `databricks.accountId` — The Databricks account the recipient belongs to (Databricks-to-Databricks sharing only). ^[create-shares-for-opensharing-databricks-on-aws.md]
- `databricks.metastoreId` — The Unity Catalog [Metastore](/concepts/metastore.md) the recipient belongs to (Databricks-to-Databricks sharing only). ^[create-shares-for-opensharing-databricks-on-aws.md]
- `databricks.name` — The name of the data recipient. ^[create-shares-for-opensharing-databricks-on-aws.md]

Providers can create custom recipient properties by defining them when creating or updating a recipient. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Partition Specification Syntax

When adding a table to a share, the provider specifies a partition condition using the `CURRENT_RECIPIENT()` SQL function:

```
(<column-name> = CURRENT_RECIPIENT().<property-key>)
```

For example:

```
(country = CURRENT_RECIPIENT().country)
```

^[create-shares-for-opensharing-databricks-on-aws.md]

### Supported Partition Formats

Parameterized partitions can be specified using multiple partition keys and multiple value types, including:

- Single-column partitions: `(year = "2022")`
- Multi-column partitions: `(year = "2020", month = "Dec")`
- Combined partitions: `(year = "2021"), (year = "2020", month = "Dec"), (year = "2019", month = "Dec", date = "2019-12-25")`

When using recipient properties, at least one partition condition must reference `CURRENT_RECIPIENT()`.

## How to Use

### Adding a Parameterized Partition in Catalog Explorer

1. Open the share in Catalog Explorer.
2. Click **Manage assets > Add data assets**.
3. Select the table.
4. Under the **Partition** column, click the plus icon.
5. In the **Add partition to the table** dialog, enter the partition specification using the syntax:
   ```
   (<column-name> = CURRENT_RECIPIENT().<property-key>)
   ```
6. Click **Save**.

^[create-shares-for-opensharing-databricks-on-aws.md]

### Using SQL

```sql
ALTER SHARE share_name
ADD TABLE inventory
PARTITION (country = CURRENT_RECIPIENT().country);
```

^[create-shares-for-opensharing-databricks-on-aws.md]

## Requirements

- The provider must have set up OpenSharing for their account. ^[create-shares-for-opensharing-databricks-on-aws.md]
- Recipient properties are available on Databricks Runtime 12.2 or above. ^[create-shares-for-opensharing-databricks-on-aws.md]
- Adding a table to a share with a parameterized partition requires a compute resource (notebook or SQL warehouse) that meets the minimum runtime requirements for the feature. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Use Cases

### Multi-Tenant Data Sharing

When a provider's table contains a column that identifies the tenant (such as an account ID), the provider can create a single share with a partition defined on that column. Each recipient sees only the rows that match their own account property. This eliminates the need to create and maintain separate shares for each tenant. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Compliance and Data Boundaries

Parameterized partition sharing enables providers to maintain strict data boundaries between recipients while using a single share. Each recipient's access is limited to the partition that matches their properties, preventing cross-recipient data access. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Comparison with Static Partitions

| Feature | Static Partition | Parameterized Partition |
|---------|-----------------|-------------------------|
| Condition | Fixed value | `CURRENT_RECIPIENT()` |
| Number of shares required | One per distinct partition | One for all recipients |
| Recipient-specific filtering | Manual per-recipient share creation | Automatic at query time |
| Maintenance | Add/remove partition entries per recipient | None — single share covers all |

## Limitations

- Parameterized partitions are only supported for tables, not for [views](/concepts/shared-views-in-databricks-to-databricks-sharing.md) or streaming tables. ^[create-shares-for-opensharing-databricks-on-aws.md]
- The `CURRENT_RECIPIENT` function is supported in Databricks Runtime 14.2 and above. ^[create-shares-for-opensharing-databricks-on-aws.md]
- When using parameterized partitions, cloud token access (directory-based access mode) is not available. The share is delivered via materialized data. ^[create-shares-for-opensharing-databricks-on-aws.md]
- If the recipient does not have direct access to the underlying data, `LIMIT` clauses and predicate pushdown are not supported. The system fully materializes all query results before returning them to the recipient. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Best Practices

- **Use a single share** with parameterized partitions to reduce administrative overhead. ^[create-shares-for-opensharing-databricks-on-aws.md]
- **Define recipient properties early** when creating recipients, so the properties are available for partition filtering. ^[create-shares-for-opensharing-databricks-on-aws.md]
- **Test partition conditions** with a representative recipient before sharing broadly to verify that the intended data boundaries are enforced.

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for sharing data between Databricks and non-Databricks systems
- [OpenSharing](/concepts/opensharing.md) — The Databricks implementation of the Delta Sharing protocol
- [Recipients](/concepts/data-recipient.md) — The entities that receive shared data
- Shares — The securable objects that define what data is shared
- [Recipient Properties](/concepts/recipient-properties.md) — Customizable attributes used in parameterized partition conditions
- Current_recipient — The SQL function used to access recipient properties
- Table partitions — The subset of a table's data defined by partition columns
- Cloud tokens — Temporary credentials for direct data access

## Sources

- create-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [create-shares-for-opensharing-databricks-on-aws.md](/references/create-shares-for-opensharing-databricks-on-aws-1ead08f8.md)
