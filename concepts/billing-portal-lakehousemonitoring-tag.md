---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ebb5260f10979fe22618b3c7531e2a3594516a99e88738f49ea5923d8d03cbef
  pageDirectory: concepts
  sources:
    - view-data-quality-monitoring-expenses-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - billing-portal-lakehousemonitoring-tag
    - BPLT
  citations:
    - file: view-data-quality-monitoring-expenses-databricks-on-aws.md
title: Billing portal LakehouseMonitoring tag
description: A method to view data profiling expenses via the Databricks account console billing portal using the LakehouseMonitoring tag key set to true.
tags:
  - billing
  - billing-portal
  - tagging
timestamp: "2026-06-19T23:25:09.407Z"
---

# Billing portal LakehouseMonitoring tag

The **Billing portal LakehouseMonitoring tag** is a custom tag filter available in the Databricks account console billing portal that allows you to view [Data Profiling](/concepts/data-profiling.md) expenses for [Lakehouse Monitoring](/concepts/lakehouse-monitoring.md). This tag is used as an alternative to querying the `system.billing.usage` system table. ^[view-data-quality-monitoring-expenses-databricks-on-aws.md]

## Usage

To check [Data Profiling](/concepts/data-profiling.md) expenses using the billing portal with the LakehouseMonitoring tag: ^[view-data-quality-monitoring-expenses-databricks-on-aws.md]

1. Log in to the [Databricks account console](https://accounts.cloud.databricks.com/login).
2. In the sidebar, click the **Usage** icon.
3. On the Usage page, select **By tags**.
4. In the first drop-down menu, select **LakehouseMonitoring** as the tag key.
5. In the second drop-down menu, select **true** as the tag value. After selection, the UI displays `true` and the second drop-down menu shows `LakehouseMonitoring(1)` to indicate that one tag key is selected.

## Applicability

The LakehouseMonitoring tag applies to [Data Profiling](/concepts/data-profiling.md) results created **before February 2026**. For results created starting in February 2026, the recommended approach is to query the `system.billing.usage` system table using the `billing_origin_product` filter set to `DATA_QUALITY_MONITORING` combined with a non-null `table_id`. ^[view-data-quality-monitoring-expenses-databricks-on-aws.md]

The query equivalent for older records using this tag is: ^[view-data-quality-monitoring-expenses-databricks-on-aws.md]

```sql
SELECT usage_date, sum(usage_quantity) as dbus
FROM system.billing.usage
WHERE
  usage_date >= DATE_SUB(current_date(), 30) AND
  sku_name like "%JOBS_SERVERLESS%" AND
  custom_tags["LakehouseMonitoring"] = "true"
GROUP BY usage_date
ORDER BY usage_date DESC
```

## Related Concepts

- [Data profiling expenses](/concepts/data-profiling-expense-tracking.md) — Overview of costs associated with [Data Profiling](/concepts/data-profiling.md)
- [Anomaly detection expenses](/concepts/anomaly-detection-expense-tracking.md) — Costs related to [Anomaly Detection](/concepts/anomaly-detection.md) monitoring
- [system.billing.usage](/concepts/systembillingusage-system-table.md) — The system table for querying billing records
- [DATA_QUALITY_MONITORING](/concepts/data-quality-monitoring.md) — The billing origin product for newer profiling records
- [Lakehouse Monitoring](/concepts/lakehouse-monitoring.md) — The overall monitoring framework for data quality

## Sources

- view-data-quality-monitoring-expenses-databricks-on-aws.md

# Citations

1. [view-data-quality-monitoring-expenses-databricks-on-aws.md](/references/view-data-quality-monitoring-expenses-databricks-on-aws-fc0bd384.md)
