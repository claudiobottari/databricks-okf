---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8d2e89be0bd6d7da168ddae115607415593ec815d45b98d5d4e9da07c6a5b196
  pageDirectory: concepts
  sources:
    - data-classification-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-classification-billing-and-usage-tracking
    - Usage Tracking and Data Classification Billing
    - DCBAUT
  citations:
    - file: data-classification-databricks-on-aws.md
title: Data Classification Billing and Usage Tracking
description: Usage and billing for Data Classification can be tracked via the system.billing.usage table or a usage dashboard, with initial scans being more costly than subsequent incremental scans.
tags:
  - data-governance
  - billing
  - cost-optimization
timestamp: "2026-06-19T09:41:08.204Z"
---

# Data Classification Billing and Usage Tracking

**Data Classification Billing and Usage Tracking** refers to the methods and tools available to monitor, query, and understand the costs associated with running [Data Classification](/concepts/data-classification.md) scans in [Unity Catalog](/concepts/unity-catalog.md). Databricks provides multiple ways to track expenses, including querying system tables and using usage dashboards.

## Overview

Data Classification uses serverless compute to scan tables and classify sensitive data. The initial scan of a catalog is more costly than subsequent scans, as later scans are incremental and typically incur lower costs. ^[data-classification-databricks-on-aws.md]

You can view expenses related to Data Classification either by running a query against the `system.billing.usage` table or by viewing the usage dashboard. ^[data-classification-databricks-on-aws.md]

## Querying Usage from `system.billing.usage`

Data Classification expenses are stored in the `system.billing.usage` system table. The following optional fields can be used to break down costs:

- `created_by`: Include to see costs by the user who triggered the usage.
- `catalog_id`: Include to see costs by catalog. The catalog ID is shown in the `system.data_classification.results` table.

^[data-classification-databricks-on-aws.md]

### Example: Usage by Date, User, and Catalog

The following query retrieves Data Classification usage for the last 30 days, grouped by date, user, and catalog:

```sql
SELECT
  usage_date,
  identity_metadata.created_by,
  usage_metadata.catalog_id,
  SUM(usage_quantity) AS dbus
FROM
  system.billing.usage
WHERE
  usage_date >= DATE_SUB(CURRENT_DATE(), 30)
  AND billing_origin_product = 'DATA_CLASSIFICATION'
GROUP BY
  usage_date,
  created_by,
  catalog_id
ORDER BY
  usage_date DESC,
  created_by;
```

^[data-classification-databricks-on-aws.md]

### Example: Total Dollar Cost

To calculate the total dollar cost, join with `system.billing.list_prices`. The following example query uses a named parameter `:add_on_rate` as a multiplier on the list price. Set it to `1` to use the list price directly, or to a value less than `1` to reflect a negotiated discount (for example, `0.9` for a 10% discount):

```sql
SELECT
  u.usage_date,
  SUM(u.usage_quantity * lp.pricing.effective_list.default) * :add_on_rate
    AS `Data Classification Dollar Cost`
FROM system.billing.usage AS u
JOIN system.billing.list_prices AS lp
  ON lp.sku_name = u.sku_name
WHERE
  u.billing_origin_product = 'DATA_CLASSIFICATION'
  AND u.usage_end_time >= lp.price_start_time
  AND (lp.price_end_time IS NULL OR u.usage_end_time < lp.price_end_time)
  AND u.usage_date >= DATE_ADD(CURRENT_DATE(), -30)
GROUP BY
  u.usage_date
ORDER BY
  u.usage_date DESC;
```

^[data-classification-databricks-on-aws.md]

## Viewing Usage from the Usage Dashboard

If you already have a usage dashboard configured in your workspace, you can use it to filter the usage by selecting the **Billing Origin Project** labeled **Data Classification**. If you do not have a usage dashboard configured, you can import one and apply the same filtering. ^[data-classification-databricks-on-aws.md]

For details on setting up usage dashboards, see [Usage Dashboards](/concepts/mlflow-system-tables-dashboards.md). ^[data-classification-databricks-on-aws.md]

## Pricing Model

For detailed pricing information, see the [Databricks pricing page](https://www.databricks.com/product/pricing). The `billing_origin_product` value for Data Classification is `'DATA_CLASSIFICATION'`. ^[data-classification-databricks-on-aws.md]

### Cost Considerations

- **Initial scans** are more costly than incremental scans on the same catalog. ^[data-classification-databricks-on-aws.md]
- **Incremental scans** are optimized to classify only new or changed data, reducing ongoing costs. ^[data-classification-databricks-on-aws.md]
- **Storage** of classification results uses [default storage](/concepts/workspace-default-storage-path.md) and is not billed separately. ^[data-classification-databricks-on-aws.md]

## Related Concepts

- [Data Classification](/concepts/data-classification.md) — The AI-powered feature that scans and tags sensitive data
- System Tables — The `system.billing.usage` and `system.billing.list_prices` tables for cost tracking
- [Usage Dashboards](/concepts/mlflow-system-tables-dashboards.md) — Pre-built dashboards for monitoring Databricks usage
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer where Data Classification operates
- Serverless Compute — The compute model used by Data Classification scans
- [Data Classification System Table Reference](/concepts/data-classification-system-table.md) — Details on the `system.data_classification.results` table

## Sources

- data-classification-databricks-on-aws.md

# Citations

1. [data-classification-databricks-on-aws.md](/references/data-classification-databricks-on-aws-066fe683.md)
