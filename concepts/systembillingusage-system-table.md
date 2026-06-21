---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c791709320e181853b5d82c78c0d7f6c97f41d2a85c3e1ee975f287d02c75504
  pageDirectory: concepts
  sources:
    - view-data-quality-monitoring-expenses-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - systembillingusage-system-table
    - SST
    - system.billing.list_prices
    - system.billing.usage
  citations:
    - file: view-data-quality-monitoring-expenses-databricks-on-aws.md
title: system.billing.usage system table
description: A Databricks system table used to query billable usage records, including data quality monitoring costs.
tags:
  - billing
  - system-tables
  - data-governance
timestamp: "2026-06-19T23:24:32.501Z"
---

# system.billing.usage system table

The **`system.billing.usage`** system table stores Databricks billable usage records and can be queried to track expenses for features such as [Data Quality Monitoring](/concepts/data-quality-monitoring.md). It is part of the Databricks system tables schema, which provides operational and billing metadata for account administrators. ^[view-data-quality-monitoring-expenses-databricks-on-aws.md]

## Key Columns

When querying `system.billing.usage`, the following columns are relevant for filtering [Data Quality Monitoring](/concepts/data-quality-monitoring.md) costs:

- `usage_date` — The date usage was recorded.
- `usage_quantity` — The quantity of billable usage (e.g., DBUs).
- `billing_origin_product` — The product that generated the usage (e.g., `DATA_QUALITY_MONITORING`).
- `usage_metadata` — A struct containing nested fields such as `schema_id` and `table_id`, used to identify [Anomaly Detection](/concepts/anomaly-detection.md) (schema‑level) and [Data Profiling](/concepts/data-profiling.md) (table‑level) costs.
- `sku_name` — The SKU name, historically used to filter serverless job usage before February 2026.
- `custom_tags` — A map of custom tags; for [Data Profiling](/concepts/data-profiling.md) costs before February 2026, the tag `LakehouseMonitoring` is set to `"true"`.

^[view-data-quality-monitoring-expenses-databricks-on-aws.md]

## Querying [Data Quality Monitoring](/concepts/data-quality-monitoring.md) Expenses

### [Anomaly Detection](/concepts/anomaly-detection.md) Expenses

[Anomaly Detection](/concepts/anomaly-detection.md) is enabled at the **schema** level. To filter for [Anomaly Detection](/concepts/anomaly-detection.md) costs, check that `usage_metadata.schema_id` is not null and `billing_origin_product` is `'DATA_QUALITY_MONITORING'`. ^[view-data-quality-monitoring-expenses-databricks-on-aws.md]

```sql
SELECT usage_date, sum(usage_quantity) as dbus
FROM system.billing.usage
WHERE usage_date >= DATE_SUB(current_date(), 30)
  AND billing_origin_product = "DATA_QUALITY_MONITORING"
  AND usage_metadata.schema_id IS NOT NULL
GROUP BY usage_date
ORDER BY usage_date DESC
```

To view costs for a specific schema, replace `IS NOT NULL` with `= "<schema_id>"`. ^[view-data-quality-monitoring-expenses-databricks-on-aws.md]

### [Data Profiling](/concepts/data-profiling.md) Expenses

[Data Profiling](/concepts/data-profiling.md) is enabled at the **table** level. For expenses recorded starting in February 2026, use the filter `usage_metadata.table_id IS NOT NULL` and `billing_origin_product = 'DATA_QUALITY_MONITORING'`. ^[view-data-quality-monitoring-expenses-databricks-on-aws.md]

```sql
SELECT usage_date, sum(usage_quantity) as dbus
FROM system.billing.usage
WHERE usage_date >= DATE_SUB(current_date(), 30)
  AND billing_origin_product = "DATA_QUALITY_MONITORING"
  AND usage_metadata.table_id IS NOT NULL
GROUP BY usage_date
ORDER BY usage_date DESC
```

To view costs for a specific table, filter by `usage_metadata.table_id = "<table_id>"`. ^[view-data-quality-monitoring-expenses-databricks-on-aws.md]

### Historical Data (Before February 2026)

For [Data Profiling](/concepts/data-profiling.md) expenses recorded **before February 2026**, the `billing_origin_product` was not set to `DATA_QUALITY_MONITORING`. Use a different filter based on `sku_name` and `custom_tags`: ^[view-data-quality-monitoring-expenses-databricks-on-aws.md]

```sql
SELECT usage_date, sum(usage_quantity) as dbus
FROM system.billing.usage
WHERE usage_date >= DATE_SUB(current_date(), 30)
  AND sku_name LIKE "%JOBS_SERVERLESS%"
  AND custom_tags["LakehouseMonitoring"] = "true"
GROUP BY usage_date
ORDER BY usage_date DESC
```

## Billing Portal Alternative

In addition to querying the system table, you can view [Data Profiling](/concepts/data-profiling.md) expenses through the Databricks account console billing portal. On the **Usage** page, select **By tags**, choose tag key `LakehouseMonitoring` and value `true` to filter costs. ^[view-data-quality-monitoring-expenses-databricks-on-aws.md]

## Related Concepts

- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) – Overview of monitoring data quality with Databricks.
- System Tables – Reference for Databricks system table schemas.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that provides system tables.
- Billing – General billing and cost management on Databricks.
- [Anomaly Detection](/concepts/anomaly-detection.md) – Schema‑level monitoring feature.
- [Data Profiling](/concepts/data-profiling.md) – Table‑level monitoring feature.

## Sources

- view-data-quality-monitoring-expenses-databricks-on-aws.md

# Citations

1. [view-data-quality-monitoring-expenses-databricks-on-aws.md](/references/view-data-quality-monitoring-expenses-databricks-on-aws-fc0bd384.md)
