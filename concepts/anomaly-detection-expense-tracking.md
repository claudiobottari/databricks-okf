---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b077cb93f8b2726af3e0255ca932bbe8ed1e4e7e16d820d474ce819103c84b0c
  pageDirectory: concepts
  sources:
    - view-data-quality-monitoring-expenses-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - anomaly-detection-expense-tracking
    - ADET
    - Anomaly Detection Expenses
    - Anomaly detection expenses
  citations:
    - file: view-data-quality-monitoring-expenses-databricks-on-aws.md
title: Anomaly detection expense tracking
description: Technique to isolate anomaly detection costs by filtering on a non-null schema_id in the billing usage table.
tags:
  - billing
  - anomaly-detection
  - data-quality
timestamp: "2026-06-19T23:24:35.583Z"
---

# [Anomaly Detection](/concepts/anomaly-detection.md) Expense Tracking

**Anomaly Detection Expense Tracking** refers to the process of monitoring and querying the costs associated with [Anomaly Detection](/concepts/anomaly-detection.md) workloads within [Data Quality Monitoring](/concepts/data-quality-monitoring.md) on Databricks. These expenses are recorded in the system billing table and can be filtered to isolate costs related to schema-level [Anomaly Detection](/concepts/anomaly-detection.md). ^[view-data-quality-monitoring-expenses-databricks-on-aws.md]

## Overview

[Anomaly Detection](/concepts/anomaly-detection.md) is enabled at the **schema level** in [Unity Catalog](/concepts/unity-catalog.md). Consequently, all costs incurred by [Anomaly Detection](/concepts/anomaly-detection.md) runs are tracked with a non‑null `schema_id` in the billing metadata. The `billing_origin_product` for these entries is `DATA_QUALITY_MONITORING`. ^[view-data-quality-monitoring-expenses-databricks-on-aws.md]

To retrieve all [Anomaly Detection](/concepts/anomaly-detection.md) expenses, query the system table `system.billing.usage` and filter for rows where `usage_metadata.schema_id IS NOT NULL` and `billing_origin_product = 'DATA_QUALITY_MONITORING'`. This filter excludes costs from [Data Profiling](/concepts/data-profiling.md), which is enabled at the table level and uses a `table_id` instead. ^[view-data-quality-monitoring-expenses-databricks-on-aws.md]

## Querying [Anomaly Detection](/concepts/anomaly-detection.md) Expenses

The following SQL query returns the total DBUs consumed by [Anomaly Detection](/concepts/anomaly-detection.md) over the last 30 days, grouped by date: ^[view-data-quality-monitoring-expenses-databricks-on-aws.md]

```sql
SELECT usage_date, sum(usage_quantity) as dbus
FROM system.billing.usage
WHERE
  usage_date >= DATE_SUB(current_date(), 30) AND
  billing_origin_product = "DATA_QUALITY_MONITORING" AND
  usage_metadata.schema_id is NOT NULL
GROUP BY usage_date
ORDER BY usage_date DESC
```

### Filtering by a Specific Schema

To view costs attributed to a particular schema, add a filter on the `schema_id` value. The `schema_id` corresponds to the [Unity Catalog](/concepts/unity-catalog.md) schema where [Anomaly Detection](/concepts/anomaly-detection.md) is enabled. ^[view-data-quality-monitoring-expenses-databricks-on-aws.md]

```sql
SELECT usage_date, sum(usage_quantity) as dbus
FROM system.billing.usage
WHERE
  usage_date >= DATE_SUB(current_date(), 30) AND
  billing_origin_product = "DATA_QUALITY_MONITORING" AND
  usage_metadata.schema_id = "<schema_id>"
GROUP BY usage_date
ORDER BY usage_date DESC
```

Replace `<schema_id>` with the actual identifier of the schema you want to examine.

## Related Concepts

- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) – The overall framework that includes [Anomaly Detection](/concepts/anomaly-detection.md) and [Data Profiling](/concepts/data-profiling.md).
- [Anomaly Detection](/concepts/anomaly-detection.md) – The capability that triggers these expenses, monitored at the schema level.
- [Data profiling expense tracking](/concepts/data-profiling-expense-tracking.md) – The analogous tracking for table-level profiling costs.
- [system.billing.usage](/concepts/systembillingusage-system-table.md) – The system table containing all billable usage records.
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) that supports schema-level monitoring.

## Sources

- view-data-quality-monitoring-expenses-databricks-on-aws.md

# Citations

1. [view-data-quality-monitoring-expenses-databricks-on-aws.md](/references/view-data-quality-monitoring-expenses-databricks-on-aws-fc0bd384.md)
