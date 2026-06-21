---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1b6f5b8bf07780ddf96466cef5d833e157939d1ed9478644cccba58dc6602e49
  pageDirectory: concepts
  sources:
    - view-data-quality-monitoring-expenses-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-profiling-expense-tracking
    - DPET
    - Data profiling expenses
  citations:
    - file: view-data-quality-monitoring-expenses-databricks-on-aws.md
title: Data profiling expense tracking
description: Technique to isolate data profiling costs by filtering on a non-null table_id in the billing usage table.
tags:
  - billing
  - data-profiling
  - data-quality
timestamp: "2026-06-19T23:24:40.292Z"
---

# [Data Profiling](/concepts/data-profiling.md) Expense Tracking

**Data Profiling Expense Tracking** refers to methods for monitoring the cost incurred by [Data Profiling](/concepts/data-profiling.md) workloads on Databricks. [Data Profiling](/concepts/data-profiling.md) is enabled at the table level, and its expenses appear under the `DATA_QUALITY_MONITORING` billing product. Users can inspect costs by querying the system billing table or through the billing portal. ^[view-data-quality-monitoring-expenses-databricks-on-aws.md]

## Querying the System Table

To view [Data Profiling](/concepts/data-profiling.md) expenses using SQL, query `system.billing.usage`. [Data Profiling](/concepts/data-profiling.md) is billed per table, so a non-null `usage_metadata.table_id` identifies profiling-related usage. For results created from **February 2026 onward**, the `billing_origin_product` is `DATA_QUALITY_MONITORING`. ^[view-data-quality-monitoring-expenses-databricks-on-aws.md]

Example query to retrieve [Data Profiling](/concepts/data-profiling.md) costs for the last 30 days:

```sql
SELECT usage_date, sum(usage_quantity) as dbus
FROM system.billing.usage
WHERE usage_date >= DATE_SUB(current_date(), 30)
  AND billing_origin_product = "DATA_QUALITY_MONITORING"
  AND usage_metadata.table_id is NOT NULL
GROUP BY usage_date
ORDER BY usage_date DESC
```

To filter costs attributed to a specific table, add a `WHERE` clause on `usage_metadata.table_id = "<table_id>"`. ^[view-data-quality-monitoring-expenses-databricks-on-aws.md]

### Querying Legacy Records (Before February 2026)

For usage records created before February 2026, the billing product identifier is different. Use the `sku_name` condition with `%JOBS_SERVERLESS%` and the custom tag `LakehouseMonitoring` set to `true`:

```sql
SELECT usage_date, sum(usage_quantity) as dbus
FROM system.billing.usage
WHERE usage_date >= DATE_SUB(current_date(), 30)
  AND sku_name like "%JOBS_SERVERLESS%"
  AND custom_tags["LakehouseMonitoring"] = "true"
GROUP BY usage_date
ORDER BY usage_date DESC
```

^[view-data-quality-monitoring-expenses-databricks-on-aws.md]

## Using the Billing Portal

Expenses can also be checked through the Databricks account console billing portal:

1. Log in to the [Databricks account console](https://accounts.cloud.databricks.com/login).
2. In the sidebar, click the **Usage** icon.
3. On the Usage page, select **By tags**.
4. In the first drop-down menu, select **LakehouseMonitoring** as the tag key.
5. In the second drop-down menu, select **true** as the tag value. The UI will show `LakehouseMonitoring(1)` to indicate the selection is active.

The portal then displays all costs tagged with `LakehouseMonitoring = true`, which includes both [Data Profiling](/concepts/data-profiling.md) and [Anomaly Detection](/concepts/anomaly-detection.md) usage. ^[view-data-quality-monitoring-expenses-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) — The process of computing statistical summaries for tables.
- [Anomaly Detection Expenses](/concepts/anomaly-detection-expense-tracking.md) — A separate cost category (identified by a non-null `schema_id`) within `DATA_QUALITY_MONITORING`.
- Databricks Billing — Overview of the system billing tables and usage tracking.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that enables [Data Profiling](/concepts/data-profiling.md) on tables.

## Sources

- view-data-quality-monitoring-expenses-databricks-on-aws.md

# Citations

1. [view-data-quality-monitoring-expenses-databricks-on-aws.md](/references/view-data-quality-monitoring-expenses-databricks-on-aws-fc0bd384.md)
