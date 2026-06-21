---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f2db0ff6f8082a73fd8293d689afdb4de6bb10c4c8147fc502373e10b779e497
  pageDirectory: concepts
  sources:
    - manage-data-recipients-for-opensharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - recipient-properties-for-data-filtering
    - RPFDF
  citations:
    - file: manage-data-recipients-for-opensharing-databricks-on-aws.md
title: Recipient Properties for Data Filtering
description: Predefined (databricks.accountId, databricks.metastoreId, databricks.name) and custom properties (e.g., 'country') attached to recipient objects that enable partition filtering of shared tables and dynamic view row/column-level access control, allowing the same share to serve multiple recipients with different data boundaries.
tags:
  - delta-sharing
  - access-control
  - data-filtering
  - opensharing
timestamp: "2026-06-19T19:24:21.970Z"
---

# Recipient Properties for Data Filtering

**Recipient Properties for Data Filtering** are predefined and custom key-value pairs attached to an [OpenSharing](/concepts/opensharing.md) recipient object that enable providers to refine data sharing access. By using these properties, providers can share different table partitions with different recipients or create dynamic views that filter rows and columns based on the recipient's identity or attributes. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## Overview

Recipient objects include properties that providers can use to implement fine-grained access control within the same share. For example, a provider can use recipient properties to share different table partitions with different recipients, enabling the same shares to be used with multiple recipients while maintaining data boundaries between them. Recipient properties can also be used in dynamic views that limit recipient access to table data at the row or column level. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## Predefined Properties

The predefined properties start with `databricks.` and include the following:

- `databricks.accountId`: The Databricks account that a data recipient belongs to (Databricks-to-Databricks sharing only).
- `databricks.metastoreId`: The Unity Catalog [Metastore](/concepts/metastore.md) that a data recipient belongs to (Databricks-to-Databricks sharing only).
- `databricks.name`: The name of the data recipient.

^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## Custom Properties

Providers can create custom properties with any key-value pair. A practical example is a `country` property: if a provider attaches `'country' = 'us'` to a recipient, they can partition table data by country and share only rows containing US data with recipients that have that property assigned. Custom properties can also be used in dynamic views to restrict row or column access based on recipient properties. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## Requirements

You must use a SQL warehouse or compute running Databricks Runtime 12.2 or above to work with recipient properties. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## Managing Recipient Properties

### Viewing Properties

To view recipient properties, navigate to the recipient details page in Catalog Explorer, use the `DESCRIBE RECIPIENT` SQL command, or use the Databricks Unity Catalog CLI. The properties section displays both predefined and custom properties. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

**Permissions required**: You must be a [Metastore](/concepts/metastore.md) admin, have the `USE RECIPIENT` privilege, or be the recipient object owner. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

### Adding or Updating Properties

Properties can be added when creating a recipient or updated for an existing recipient using Catalog Explorer, the Databricks Unity Catalog CLI, or SQL commands. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

**Permissions required**: You must be a [Metastore](/concepts/metastore.md) admin or have the `CREATE RECIPIENT` privilege for the Unity Catalog [Metastore](/concepts/metastore.md). To update an existing recipient's properties, you must be the recipient owner. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

In Catalog Explorer:
1. Navigate to the recipient details page under **OpenSharing > Shared by me > Recipients**.
2. Under **Recipient properties**, click the edit icon.
3. Enter a property name (**Key**) and **Value**.
4. Click **Save**.

^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

### Using SQL Commands

Use the `ALTER RECIPIENT` SQL command to update recipient properties. For example:

```sql
ALTER RECIPIENT recipient_name SET PROPERTIES ('country' = 'us');
```

^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## Use Cases

### Partition Filtering

Recipient properties enable providers to share table partitions selectively. By matching partition columns to recipient property values, different recipients see only the data relevant to them. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

### Dynamic Row and Column Filtering

Providers can add dynamic views to a share that use recipient properties to limit access to specific rows or columns. For example, a view can check `databricks.name` or a custom property like `country` to determine which rows the recipient can query. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing Recipients](/concepts/opensharing-recipient.md) — The named objects representing users or groups with whom data is shared
- [OpenSharing Shares](/concepts/opensharing-share.md) — Collections of tables and views shared with recipients
- Dynamic Views — Views that filter data based on recipient properties
- Table Partitioning — A technique for organizing table data by column values
- [Unity Catalog](/concepts/unity-catalog.md) — The [Metastore](/concepts/metastore.md) governing data access and permissions

## Sources

- manage-data-recipients-for-opensharing-databricks-on-aws.md

# Citations

1. [manage-data-recipients-for-opensharing-databricks-on-aws.md](/references/manage-data-recipients-for-opensharing-databricks-on-aws-073afd50.md)
