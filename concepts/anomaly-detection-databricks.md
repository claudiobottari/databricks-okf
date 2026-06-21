---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: df844845f6fcac7f458399b35282ec4d4f84de40a8019360da11f3fa67d0a955
  pageDirectory: concepts
  sources:
    - anomaly-detection-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - anomaly-detection-databricks
    - AD(
    - Anomaly Detection Metrics
    - Anomaly Detection on Databricks
    - Anomaly Detection Overview
    - Anomaly detection (data quality)
  citations:
    - file: anomaly-detection-databricks-on-aws.md
    - file: data-quality-monitoring-databricks-on-aws.md
title: Anomaly Detection (Databricks)
description: A Databricks feature that automatically monitors data quality across schema tables by analyzing historical patterns of freshness and completeness.
tags:
  - data-quality
  - monitoring
  - databricks
timestamp: "2026-06-19T22:05:58.080Z"
---

```yaml
---
title: Anomaly Detection (Databricks)
summary: A one-click scalable data quality monitoring feature that automatically assesses table freshness and completeness by analyzing historical data patterns and predicting expected commits and row counts.
sources:
  - anomaly-detection-databricks-on-aws.md
  - data-quality-monitoring-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:46:34.097Z"
updatedAt: "2026-06-19T14:44:16.541Z"
tags:
  - anomaly-detection
  - data-quality
  - monitoring
aliases:
  - anomaly-detection-databricks
  - AD
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Anomaly Detection (Databricks)

**Anomaly Detection** is a one-click data quality monitoring capability in Unity Catalog that automatically evaluates the completeness and freshness of every table in a schema. Using intelligent scanning, it prioritises high-impact tables (based on popularity and downstream usage) and reduces scan frequency for less critical tables, enabling scalable monitoring without per‑table configuration.^[anomaly-detection-databricks-on-aws.md, data-quality-monitoring-databricks-on-aws.md]

## How It Works

Databricks runs a background job that monitors two core metrics for each table:

- **Freshness** – how recently a table has been updated. The system analyses the history of commits to build a per‑table model that predicts when the next commit should occur. If a commit is unusually late, the table is marked as **stale**.^[anomaly-detection-databricks-on-aws.md]
- **Completeness** – whether the number of rows written in the last 24 hours falls within an expected range. The system analyses historical row counts to predict a lower bound. If the actual row count is below that bound, the table is marked as **incomplete**.^[anomaly-detection-databricks-on-aws.md]

Additionally, **percent null** extends the completeness check by column: it predicts the expected percentage of null values per column over 24 hours. If the observed null percentage exceeds the upper bound, the table is also marked incomplete.^[anomaly-detection-databricks-on-aws.md]

Anomaly detection **does not** modify any tables it monitors, nor does it add overhead to jobs that populate those tables.^[anomaly-detection-databricks-on-aws.md]

## Requirements

- A Unity Catalog‑enabled workspace with [serverless compute](https://docs.databricks.com/aws/en/compute/serverless/) available (enabled by default for Unity Catalog workspaces).^[anomaly-detection-databricks-on-aws.md]
- To enable anomaly detection on a schema: `MANAGE SCHEMA` or `MANAGE CATALOG` privilege on that schema.^[anomaly-detection-databricks-on-aws.md]
- To view health indicators: `SELECT` or `BROWSE` privilege on the table.^[anomaly-detection-databricks-on-aws.md]

## Enable Anomaly Detection on a Schema

1. In **Catalog Explorer**, open the schema and click the **Details** tab.
2. Click **Enable**, ensure **Anomaly detection** is toggled on, then click **Save**.
3. A scan begins immediately. Tables are scanned at the frequency they are updated, and results appear after the first scan completes.^[anomaly-detection-databricks-on-aws.md]

To disable the feature, click the pencil icon on the schema’s **Details** tab, toggle the monitoring switch off, and confirm. Disabling deletes all anomaly‑detection data and the background job; this action cannot be undone.^[anomaly-detection-databricks-on-aws.md]

## Health Indicators

After enabling anomaly detection, health indicators appear on the schema and table overview pages in Catalog Explorer. These indicators summarise table health for data consumers without requiring navigation to the full monitoring UI.^[anomaly-detection-databricks-on-aws.md]

The possible states are:

- **Healthy** – no anomalies detected.
- **Unhealthy** – a freshness or completeness anomaly has been detected.
- **Error** – the monitoring scan failed for that table.

Health indicators may be delayed for up to two weeks for tables that were skipped during the initial smart scan; they appear on the next scheduled rescan.^[anomaly-detection-databricks-on-aws.md]

## Viewing Results

### Data Quality Monitoring UI (New)

From the schema’s **Details** tab, click **View results**. The UI shows a summary of overall data quality for the selected schema or catalog (percentage of healthy tables, monitored percentage). Below that, a table lists incidents, filterable by **Unhealthy**, **Healthy**, or **Error**.^[anomaly-detection-databricks-on-aws.md]

- **Unhealthy tab**: Click **Review** on an incident to open details. You can assign the incident to yourself (claim ownership for 7 days) or mark it as **Not an issue** (dismisses the alert for 7 days).^[anomaly-detection-databricks-on-aws.md]
- **Recently Resolved Incidents**: Shows tables that recovered automatically (e.g., after fresh data arrived), helping distinguish transient issues from persistent problems.^[anomaly-detection-databricks-on-aws.md]

### Table Quality Details

The **Table Quality Details** view provides per‑table trend graphs of predicted vs. observed values over the last week. For unhealthy tables, it also lists any upstream jobs identified as root causes. You can access this view from the results UI, the legacy dashboard, or the **Quality** tab on the table page.^[anomaly-detection-databricks-on-aws.md]

### Alerts

To receive notifications when anomalies are detected, set up a Databricks SQL alert on the output table `system.data_quality_monitoring.table_results`.^[anomaly-detection-databricks-on-aws.md]

## Limitations

- Anomaly detection does not support views or foreign tables (e.g., tables backed by external sources like Delta Sharing).^[anomaly-detection-databricks-on-aws.md]
- The completeness check does not consider the fraction of nulls, zeros, or NaN values (the `percent null` metric covers nulls for individual columns, not overall row completeness).^[anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that hosts anomaly detection.
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) – The broader feature set, which includes anomaly detection and data profiling.
- [Data Profiling](/concepts/data-profiling.md) – A complementary capability that provides summary statistics and tracks distribution changes over time.
- [Catalog Explorer](/concepts/catalog-explorer.md) – The UI where health indicators and monitoring controls are surfaced.
- Serverless Compute – Required compute infrastructure for the anomaly detection job.

## Sources

- anomaly-detection-databricks-on-aws.md
- data-quality-monitoring-databricks-on-aws.md

# Citations

1. [anomaly-detection-databricks-on-aws.md](/references/anomaly-detection-databricks-on-aws-a589cd11.md)
2. [data-quality-monitoring-databricks-on-aws.md](/references/data-quality-monitoring-databricks-on-aws-90a47a1b.md)
