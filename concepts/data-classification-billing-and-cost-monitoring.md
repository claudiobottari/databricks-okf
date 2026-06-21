---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5755795ee1e42683e4ce915446b4e55f60d7f57f7f0181c7feb9d0a78bb13983
  pageDirectory: concepts
  sources:
    - data-classification-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-classification-billing-and-cost-monitoring
    - Cost Monitoring and Data Classification Billing
    - DCBACM
    - Cost Monitoring for Data Classification
  citations:
    - file: data-classification-databricks-on-aws.md
title: Data Classification Billing and Cost Monitoring
description: How to view and understand Databricks Data Classification expenses using the system.billing.usage table and usage dashboards, with initial scans costing more than incremental scans.
tags:
  - billing
  - cost-management
  - monitoring
timestamp: "2026-06-19T18:04:20.768Z"
---

# Data Classification Billing and Cost Monitoring

**Data Classification Billing and Cost Monitoring** refers to the methods and tools available to track, query, and visualize expenses incurred by Databricks Data Classification operations within Unity Catalog. Understanding these costs helps data teams manage their budget and optimize scanning behavior.

## Overview

Databricks Data Classification uses serverless compute resources to run its AI-driven scanning agent, which automatically classifies and tags sensitive data in Unity Catalog tables. These scans consume billable compute resources, and the associated costs can be monitored through system tables and usage dashboards. ^[data-classification-databricks-on-aws.md]

The initial scan of a catalog is more costly than subsequent scans, as later scans are incremental and typically incur lower costs. ^[data-classification-databricks-on-aws.md]

## Viewing Data Classification Expenses

Data Classification expenses can be viewed through two primary methods: querying the `system.billing.usage` system table or using a configured usage dashboard.

### Querying the `system.billing.usage` Table

You can query Data Classification expenses from the [system.billing.usage](/concepts/systembillingusage-system-table.md) system table. Two optional fields help break down costs:

- `created_by`: Use this field to see costs by the user who triggered the usage.
- `catalog_id`: Use this field to see costs by catalog. The catalog ID is shown in the `system.data_classification.results` table.

^[data-classification-databricks-on-aws.md]

#### Example: Usage by Date, User, and Catalog (Last 30 Days)

```sql
SELECT
  usage_date,
  identity_metadata.created_by,
  usage_metadata.catalog_id,
  SUM(usage_quantity) AS dbus
FROM system.billing.usage
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

#### Example: Total Dollar Cost (Last 30 Days)

To calculate the total dollar cost, join with `system.billing.list_prices`. The following example uses a named parameter `:add_on_rate` as a multiplier on the list price. Set it to `1` to use the list price directly, or to a value less than `1` to reflect a negotiated discount (e.g., `0.9` for a 10% discount).

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

### Viewing Usage from the Usage Dashboard

If you already have a usage dashboard configured in your workspace, you can filter the usage by selecting the **Billing Origin Project** labeled **'Data Classification'**. If you do not have a usage dashboard configured, you can import one and apply the same filtering. For details, see [Usage Dashboards](/concepts/mlflow-system-tables-dashboards.md). ^[data-classification-databricks-on-aws.md]

## Storage Costs

Databricks Data Classification uses [default storage](/concepts/workspace-default-storage-path.md) to store classification results. You are not billed for this storage. ^[data-classification-databricks-on-aws.md]

## Cost Optimization

Because scanning is incremental and optimized — leveraging Unity Catalog and the Data Intelligence Engine to intelligently determine when to scan data — subsequent scans are typically less expensive than the initial full scan. There is no manual configuration required to enable this optimization. ^[data-classification-databricks-on-aws.md]

## Related Concepts

- [Data Classification](/concepts/data-classification.md) — The AI-driven feature for automatically classifying and tagging sensitive data in Unity Catalog.
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform where Data Classification operates.
- System Tables — System-managed tables that provide billing and usage data.
- [Usage Dashboards](/concepts/mlflow-system-tables-dashboards.md) — Pre-built or custom dashboards for visualizing Databricks usage and costs.
- Serverless Compute — The compute infrastructure required for Data Classification operations.
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — Governance controls that can be applied based on classification results.

## Sources

- data-classification-databricks-on-aws.md

# Citations

1. [data-classification-databricks-on-aws.md](/references/data-classification-databricks-on-aws-066fe683.md)
