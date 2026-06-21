---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7e07fccd86ecd6c8cbf0f075513153a3fec9c00d7edfa758814a002a95c4a1b8
  pageDirectory: concepts
  sources:
    - anomaly-detection-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-anomaly-detection
    - DAD
    - default storage for anomaly detection
  citations:
    - file: anomaly-detection-databricks-on-aws.md
title: Databricks Anomaly Detection
description: Automated monitoring of data quality across tables in a schema using historical pattern analysis to detect freshness and completeness anomalies
tags:
  - data-quality
  - monitoring
  - databricks
timestamp: "2026-06-19T14:00:15.215Z"
---

# Databricks Anomaly Detection

**Databricks Anomaly Detection** is a built-in data quality monitoring feature within [Unity Catalog](/concepts/unity-catalog.md) that automatically evaluates the **freshness** and **completeness** of tables in a schema. It analyzes historical patterns to detect when a table is stale or has an unusually low row count, surfacing results in [Catalog Explorer](/concepts/catalog-explorer.md) and a dedicated results UI.^[anomaly-detection-databricks-on-aws.md]

## Overview

Anomaly detection runs as a background job that monitors every table in a schema. It requires no user‑provided thresholds; instead, it builds a per‑table model from commit history and row‑count history to predict expected behavior. The feature does **not** modify monitored tables or add overhead to jobs that populate them.^[anomaly-detection-databricks-on-aws.md]

Results are stored in the `system.data_quality_monitoring.table_results` system table using default storage; users are not billed for this storage.^[anomaly-detection-databricks-on-aws.md]

## Requirements

- A workspace with [Unity Catalog](/concepts/unity-catalog.md) enabled.
- Serverless Compute must be available (enabled by default in Unity‑Catalog workspaces).
- To **enable** anomaly detection on a schema: `MANAGE SCHEMA` or `MANAGE CATALOG` privilege.
- To **view** health indicators: `SELECT` or `BROWSE` privilege on the table.^[anomaly-detection-databricks-on-aws.md]

## How It Works

### Freshness

**Freshness** measures how recently a table has been updated. The background job analyzes commit history, builds a model predicting the next commit time, and marks a table as **stale** if a commit arrives later than expected.^[anomaly-detection-databricks-on-aws.md]

### Completeness

**Completeness** evaluates the number of rows written in the last 24 hours. Based on historical row counts, a predicted range is generated. If the actual row count falls below the lower bound, the table is marked as **incomplete**.^[anomaly-detection-databricks-on-aws.md]

### Percent Null (Completeness detail)

**Percent null** enriches completeness by column: for each column, the system predicts the expected percentage of null rows in the last 24 hours. If observed null percentage exceeds the upper bound, the table is marked incomplete.^[anomaly-detection-databricks-on-aws.md]

### Scan Scheduling

Databricks uses *intelligent scanning* to automate table scan frequencies, prioritizing high‑impact tables (by popularity and downstream usage) and reducing frequency for less critical tables. Tables can be manually excluded via the `excluded_table_full_names` parameter in the [Create Monitor](https://docs.databricks.com/api/workspace/dataquality/createmonitor#anomaly_detection_config-excluded_table_full_names) or [Update Monitor](https://docs.databricks.com/api/workspace/dataquality/updatemonitor) API.^[anomaly-detection-databricks-on-aws.md]

## Enabling and Disabling Anomaly Detection

### Enable

1. In Catalog Explorer, navigate to the schema.
2. Click the **Details** tab.
3. Click **Enable**, ensure **Anomaly detection** is toggled on, and click **Save**.
4. A scan is initiated. For schemas enabled before September 24, 2025, the first scan runs “backtesting” against two weeks of historical data.

After the scan, health indicators appear on table pages, and results are available in the Data Quality Monitoring UI.^[anomaly-detection-databricks-on-aws.md]

### Disable

1. On the schema’s **Details** tab, click the pencil icon.
2. Toggle off anomaly detection in the **Data Quality Monitoring** dialog.
3. Click **Save**.

Disabling deletes the anomaly detection job, all anomaly detection tables, and associated information. This action cannot be undone.^[anomaly-detection-databricks-on-aws.md]

## Health Indicators

After enabling, each table in the schema shows a health indicator in Catalog Explorer (users need `SELECT` or `BROWSE`). The indicator statuses are:

| Icon | Status | Description |
|------|--------|-------------|
| Green checkmark | Healthy | No anomalies detected. |
| Yellow triangle | Warning | Anomaly detected (partial issue). |
| Red exclamation mark | Unhealthy | Anomaly detected (severe issue). |
| Grey dash | No data | Not yet evaluated. |

Smart scanning may delay initial indicators for some tables by up to two weeks.^[anomaly-detection-databricks-on-aws.md]

## Results and Incident Management

### Data Quality Monitoring UI

The results UI provides [Catalog and Schema](/concepts/catalog-and-schema.md) dropdowns. Users with `MANAGE` or `SELECT` on a catalog can view incidents for all schemas in that catalog. Selecting a specific schema shows only its incidents.^[anomaly-detection-databricks-on-aws.md]

The page displays:
- **Summary**: percentage of healthy tables and percentage of schemas/tables monitored.
- **Incidents Table**: lists unhealthy, healthy, or error tables (filterable by tab).
- **Recently Resolved Incidents**: tables that auto‑recovered from unhealthy to healthy within the last seven days. This helps distinguish transient issues from persistent ones.^[anomaly-detection-databricks-on-aws.md]

### Managing Unhealthy Incidents

From the **Unhealthy** tab, click **Review** to open incident details. Two actions are available:
- **Assign to me**: Marks the incident as being investigated (status remains unhealthy; assignment lasts 7 days).
- **Not an issue**: Dismisses the incident as a false positive (status changes to healthy; dismissal lasts 7 days).^[anomaly-detection-databricks-on-aws.md]

## Table Quality Details

The **Table Quality Details** view provides per‑table graphs of predicted vs. observed values over the last week. It also displays upstream jobs identified as the root cause of failures. This view can be accessed from:
- The new Data Quality Monitoring UI (review link).
- The legacy Lakeview dashboard (table name link).
- The table’s **Quality** tab in Catalog Explorer.^[anomaly-detection-databricks-on-aws.md]

## Alerts

Databricks SQL alerts can be configured on the `system.data_quality_monitoring.table_results` table. See [Alerts for anomaly detection](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/anomaly-detection/alerts).^[anomaly-detection-databricks-on-aws.md]

## Limitations

- Does **not** support views or foreign tables.
- Completeness does **not** consider null fractions, zero values, or NaN.^[anomaly-detection-databricks-on-aws.md]

## Legacy Features

The current version of anomaly detection (October 2025 onward) replaces the earlier *Data Quality Dashboard* and *job parameter configuration* interface. Legacy users may still find:
- The older **Data Quality Monitoring dashboard** at `/Shared/Databricks Quality Monitoring/Data Quality Monitoring`, which offered a quality overview and incident table.
- Job‑task parameters for customizing freshness/completeness evaluation (no longer supported for new customers after July 21, 2025).

Databricks recommends enabling the new UI for existing schemas by toggling anomaly detection off and on again.^[anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- Serverless Compute
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md)
- System Tables
- [Databricks SQL Alerts](/concepts/databricks-sql-alerts.md)

## Sources

- anomaly-detection-databricks-on-aws.md

# Citations

1. [anomaly-detection-databricks-on-aws.md](/references/anomaly-detection-databricks-on-aws-a589cd11.md)
