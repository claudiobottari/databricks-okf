---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7ef6b36a75a2270a7b05babf82c6510225f547959bcc80476ff8c440f93c950c
  pageDirectory: concepts
  sources:
    - view-data-quality-monitoring-expenses-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - legacy-data-profiling-billing-query-pattern
    - LDPBQP
    - Anomaly detection billing query pattern
  citations:
    - file: view-data-quality-monitoring-expenses-databricks-on-aws.md
title: Legacy data profiling billing query pattern
description: Pre-February 2026 query pattern for data profiling expenses using sku_name containing JOBS_SERVERLESS and custom_tags['LakehouseMonitoring'] instead of table_id filter.
tags:
  - billing
  - data-profiling
  - legacy
timestamp: "2026-06-19T23:24:55.811Z"
---

# Legacy [Data Profiling](/concepts/data-profiling.md) Billing Query Pattern

The **legacy [Data Profiling](/concepts/data-profiling.md) billing query pattern** refers to the SQL query used to retrieve billing usage for [Data Profiling](/concepts/data-profiling.md) on Databricks before the introduction of structured metadata filters in February 2026. This older pattern relies on the `sku_name` and `custom_tags` columns instead of `usage_metadata.table_id` and the `billing_origin_product` field.

## Overview

[Data Profiling](/concepts/data-profiling.md) billing usage is recorded in the `system.billing.usage` system table. Up to January 2026 (inclusive), the costs associated with [Data Profiling](/concepts/data-profiling.md) were identified by matching `sku_name` against a `JOBS_SERVERLESS`‑like pattern and checking the presence of a `LakehouseMonitoring` tag. Starting from February 2026, a newer pattern using `billing_origin_product = "DATA_QUALITY_MONITORING"` and `usage_metadata.table_id is NOT NULL` became available. The legacy pattern remains useful for queries covering dates before the change. ^[view-data-quality-monitoring-expenses-databricks-on-aws.md]

## When to Use the Legacy Pattern

Use the legacy query when the billing usage date is **before February 2026**. For records dated February 2026 or later, the modern query should be preferred because it is more precise (filtering on `table_id` and `billing_origin_product`). ^[view-data-quality-monitoring-expenses-databricks-on-aws.md]

## Legacy Query

The legacy SQL filters on `sku_name` containing `%JOBS_SERVERLESS%` and the custom tag `LakehouseMonitoring` set to `true`. The query aggregates usage by date:

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

The `sku_name` filter isolates serverless job usage, and the `custom_tags` filter narrows the result to the [Data Profiling](/concepts/data-profiling.md) workload. ^[view-data-quality-monitoring-expenses-databricks-on-aws.md]

## Alternative: Billing Portal

You can also view [Data Profiling](/concepts/data-profiling.md) expenses through the Databricks Account Console billing portal using the `LakehouseMonitoring` tag. In the account console, navigate to the **Usage** page, select **By tags**, choose `LakehouseMonitoring` as the tag key and `true` as the tag value. This method works for both legacy and current usage as long as the tag is present. ^[view-data-quality-monitoring-expenses-databricks-on-aws.md]

## Migration to Modern Pattern

If you are still using the legacy pattern, consider switching to the modern query (filtering on `billing_origin_product` and `usage_metadata.table_id`) for improved accuracy, especially for profiles created from February 2026 onward. The modern pattern also allows filtering by a specific table ID. ^[view-data-quality-monitoring-expenses-databricks-on-aws.md]

## Related Concepts

- Data quality monitoring expenses – Overview of billing for [Data Profiling](/concepts/data-profiling.md) and [Anomaly Detection](/concepts/anomaly-detection.md).
- Unity Catalog billing – How [Unity Catalog](/concepts/unity-catalog.md) costs are tracked across system tables.
- System tables billing – Reference for the `system.billing.usage` table and its schema.
- [Anomaly detection billing query pattern](/concepts/legacy-data-profiling-billing-query-pattern.md) – Similar query pattern using `usage_metadata.schema_id`.
- [LakehouseMonitoring tag](/concepts/lakehouse-monitoring.md) – Custom tag used to tag [Data Profiling](/concepts/data-profiling.md) workloads in billing records.

## Sources

- view-data-quality-monitoring-expenses-databricks-on-aws.md

# Citations

1. [view-data-quality-monitoring-expenses-databricks-on-aws.md](/references/view-data-quality-monitoring-expenses-databricks-on-aws-fc0bd384.md)
