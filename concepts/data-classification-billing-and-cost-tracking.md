---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4540c0255c3b0d08dd0016bb27b0720f394c565484210e4b3e5f10cae25a110a
  pageDirectory: concepts
  sources:
    - data-classification-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-classification-billing-and-cost-tracking
    - Cost Tracking and Data Classification Billing
    - DCBACT
  citations:
    - file: data-classification-databricks-on-aws.md
title: Data Classification Billing and Cost Tracking
description: The ability to query Data Classification expenses via the system.billing.usage system table and usage dashboard, with initial scans costing more than subsequent incremental scans.
tags:
  - billing
  - cost-management
  - databricks
timestamp: "2026-06-18T14:58:29.217Z"
---

# Data Classification Billing and Cost Tracking

**Data Classification Billing and Cost Tracking** refers to how usage of Databricks Data Classification is metered and how administrators can monitor related expenses. Data Classification uses serverless compute to scan tables, and costs are reflected in the account’s billing system. Storage of classification results uses [default storage](/concepts/workspace-default-storage-path.md) and is not billed separately.^[data-classification-databricks-on-aws.md]

## How Billing Works

Data Classification is billed per usage, primarily based on the compute resources consumed during scanning. The initial scan of a catalog is more costly than subsequent scans, because later scans are incremental and typically incur lower costs. For detailed pricing, see the [Databricks pricing page](https://www.databricks.com/product/pricing).^[data-classification-databricks-on-aws.md]

## Viewing Expenses

You can track Data Classification costs using two methods: querying the [system.billing.usage](/concepts/systembillingusage-system-table.md) system table or using a pre-configured usage dashboard.

### Querying `system.billing.usage`

The `system.billing.usage` table records all billable usage events. To isolate Data Classification costs, filter by `billing_origin_product = 'DATA_CLASSIFICATION'`. The table includes optional fields `created_by` (the user who triggered the usage) and `catalog_id` (the catalog the usage is associated with). The catalog ID can be found in the `system.data_classification.results` table.

Example query for the last 30 days by day, user, and catalog:^[data-classification-databricks-on-aws.md]

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

To calculate the total dollar cost, join with `system.billing.list_prices`. The following example uses a named parameter `:add_on_rate` to apply a negotiated discount (set to `1` for the list price):^[data-classification-databricks-on-aws.md]

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

### Using the Usage Dashboard

If you already have a usage dashboard configured in your workspace, you can filter it by selecting the **Billing Origin Project** labeled `Data Classification`. If no dashboard is configured, you can import one; for details, see Usage dashboards.^[data-classification-databricks-on-aws.md]

## Related Concepts

- [Data Classification](/concepts/data-classification.md) – The overall feature for automatic sensitive data tagging.
- System Tables – The `system.billing.usage` and `system.billing.list_prices` tables used for cost queries.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer in which Data Classification operates.
- Serverless Compute – Required for running Data Classification scans.
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) – Using classification results to define access policies.

## Sources

- data-classification-databricks-on-aws.md

# Citations

1. [data-classification-databricks-on-aws.md](/references/data-classification-databricks-on-aws-066fe683.md)
