---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 90671d4f205933c1cd9c67af879d5390b3ee4ed7021758b6e0bbb3251202efae
  pageDirectory: concepts
  sources:
    - create-shares-for-opensharing-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dynamic-views-with-current_recipient
    - DVWC
    - Dynamic Views with CURRENT_RECIPIENT
  citations:
    - file: create-shares-for-opensharing-databricks-on-aws.md
title: Dynamic Views with CURRENT_RECIPIENT()
description: Using dynamic views with the CURRENT_RECIPIENT() SQL function to enforce row-level and column-level security based on recipient properties, enabling fine-grained access control in shared data.
tags:
  - delta-sharing
  - security
  - views
  - access-control
timestamp: "2026-06-19T14:38:41.190Z"
---

# Dynamic Views with CURRENT_RECIPIENT()

**Dynamic Views with CURRENT_RECIPIENT()** refers to the use of the `CURRENT_RECIPIENT()` SQL function inside a [dynamic view definition](/concepts/dynamic-views-for-fine-grained-access.md) to enforce fine-grained row-level and column-level access control in [Delta Sharing](/concepts/delta-sharing.md). This enables a data provider to create a single view that automatically returns different subsets of data to different recipients based on properties defined on each recipient object. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Overview

In Delta Sharing, dynamic views are read-only objects that can be shared with recipients. When a provider shares a dynamic view that includes `CURRENT_RECIPIENT()`, the query engine evaluates the function at runtime for each recipient query. The function returns a structure containing the recipient’s default and custom properties, which can be used in `WHERE` clauses, `CASE` expressions, or partition filters to restrict data visibility. This pattern avoids the need to create separate views or shares for each recipient. ^[create-shares-for-opensharing-databricks-on-aws.md]

## The `CURRENT_RECIPIENT()` Function

`CURRENT_RECIPIENT()` returns the properties of the recipient that is querying the view. These properties serve as input to the view’s SQL logic, enabling dynamic filtering or masking. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Recipient Properties

Default properties provided by Databricks include:

- **`databricks.accountId`** – The Databricks account ID of the recipient (available only in Databricks-to-Databricks sharing). ^[create-shares-for-opensharing-databricks-on-aws.md]
- **`databricks.metastoreId`** – The Unity Catalog [Metastore](/concepts/metastore.md) ID of the recipient (available only in Databricks-to-Databricks sharing). ^[create-shares-for-opensharing-databricks-on-aws.md]
- **`databricks.name`** – The name of the data recipient. ^[create-shares-for-opensharing-databricks-on-aws.md]

Providers can also create custom properties when creating or updating a recipient definition. These custom properties are then accessible via `CURRENT_RECIPIENT()`. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Use Cases

### Row-Level Security

By placing a comparison between a table column and a recipient property in the `WHERE` clause of the view, the provider can restrict which rows a recipient sees. For example, a view can return only rows where a `country` column matches the recipient’s `country` property. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Column-Level Security

`CURRENT_RECIPIENT()` can be used in a `CASE` statement to return different values for a column depending on the recipient. This enables the exclusion or transformation of sensitive columns for specific recipients. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Data Masking

The function can dynamically transform column values, showing original data to authorized recipients and masked values (e.g., truncated credit card numbers) to others. ^[create-shares-for-opensharing-databricks-on-aws.md]

### Parameterized Partition Sharing

In addition to row filters inside a view, `CURRENT_RECIPIENT()` can be used in a **partition specification** when adding a table to a share. This allows the share to deliver only the data partitions that match the recipient’s properties, without requiring a view. For example:

```sql
ALTER SHARE share_name ADD TABLE inventory PARTITION (country = CURRENT_RECIPIENT().country);
```

This is known as parameterized partition sharing and is supported in Catalog Explorer via the **Partition** column when adding assets. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Requirements

- The view must meet all requirements for view sharing within Delta Sharing. ^[create-shares-for-opensharing-databricks-on-aws.md]
- The `CURRENT_RECIPIENT` function is supported in **Databricks Runtime 14.2** and above. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Limitations

- All limitations for general view sharing apply. Views cannot reference [shared tables](/concepts/feature-table.md) or other shared views, and they cannot reference foreign tables (including foreign Iceberg tables). ^[create-shares-for-opensharing-databricks-on-aws.md]
- If the recipient does not have direct access to the underlying data (e.g., open sharing recipients), `LIMIT` clauses and predicate pushdown are not supported. The system fully materializes all query results before returning them to the recipient, regardless of any query filters applied. ^[create-shares-for-opensharing-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The framework for sharing data across platforms.
- Dynamic Views — General concept of views that evaluate logic at query time.
- [Recipient Properties](/concepts/recipient-properties.md) — Configurable attributes assigned to data recipients.
- [Parameterized Partition Sharing](/concepts/parameterized-partition-sharing.md) — Using `CURRENT_RECIPIENT()` in partition filters.
- [OpenSharing](/concepts/opensharing.md) — The Databricks implementation of the Delta Sharing protocol.
- [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md) — Alternative ABAC-based approach for access control.

## Sources

- create-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [create-shares-for-opensharing-databricks-on-aws.md](/references/create-shares-for-opensharing-databricks-on-aws-1ead08f8.md)
