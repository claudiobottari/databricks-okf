---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e12fbd370063b896cf605d999604560689ec389634fc009604bb0e6087178bb0
  pageDirectory: concepts
  sources:
    - anomaly-detection-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - table-quality-details-databricks
    - TQD(
  citations:
    - file: anomaly-detection-databricks-on-aws.md
title: Table Quality Details (Databricks)
description: A detailed view showing trends and anomaly reasons for specific tables, including predicted vs observed values and upstream root cause analysis
tags:
  - data-quality
  - ui
  - troubleshooting
timestamp: "2026-06-19T14:01:02.329Z"
---

# Table Quality Details (Databricks)

**Table Quality Details** is a component of [Anomaly Detection](/concepts/anomaly-detection.md) in Databricks that provides an in-depth view of data quality trends and anomaly detection results for individual tables within a schema monitored by [Data Quality Monitoring](/concepts/data-quality-monitoring.md). It allows users to investigate why specific anomalies were flagged, view historical predictions versus observed values, and identify root causes such as upstream jobs. ^[anomaly-detection-databricks-on-aws.md]

## Accessing Table Quality Details

The Table Quality Details view can be accessed from multiple entry points in the Databricks ecosystem:

- **From the Results UI (new experience):** Click the review link in the incidents list for an unhealthy table.
- **From the Monitoring Dashboard (legacy Lakeview dashboard):** Click the table name in the **Quality Overview** tab.
- **From the UC Table viewer:** Visit the **Quality** tab on the table page.

All paths lead to the same unified **Table Quality Details** view for the selected table. ^[anomaly-detection-databricks-on-aws.md]

## What the Table Quality Details View Shows

The Table Quality Details UI organizes information into several sections. For a given table, it shows summaries from each quality check, including graphs of predicted and observed values at each evaluation timestamp. The graphs plot results from the last 1 week of data. ^[anomaly-detection-databricks-on-aws.md]

### Key Quality Metrics

Two primary metrics are tracked:

- **Freshness:** How recently the table has been updated. A model predicts the next expected commit time; if a commit is unusually late, the table is marked as stale.
- **Completeness:** The number of rows expected to be written in the last 24 hours. A range is predicted from historical row counts; if actual rows fall below the lower bound, the table is marked as incomplete.

**Percent null** is an additional metric for completeness, representing the percentage of rows expected to have null values for a given column. Predicted ranges versus observed values are displayed. ^[anomaly-detection-databricks-on-aws.md]

### Root Cause Analysis

If a table fails quality checks, the UI displays a table of upstream jobs that were identified as the root cause. This helps users quickly pinpoint the source of data quality degradation without manual investigation. ^[anomaly-detection-databricks-on-aws.md]

### Predicted vs Observed Values

The view includes graphs plotting predicted and observed values at each evaluation timestamp, covering the last 1 week of data. This enables users to visually compare expected behavior against actual behavior, identify anomalies, and understand when issues began. ^[anomaly-detection-databricks-on-aws.md]

## Health Indicators

After anomaly detection is enabled on a schema, health indicators appear in [Catalog Explorer](/concepts/catalog-explorer.md) for each table. These provide a summary of table health for data consumers and business users. Users need `SELECT` or `BROWSE` permissions to view the health indicator status. ^[anomaly-detection-databricks-on-aws.md]

## Use Cases

Table Quality Details is useful for:

- **Data consumers:** Quickly assess whether a table is reliable and fresh enough for downstream workloads.
- **Data engineers:** Diagnose why a table is flagged as unhealthy, including identifying upstream job delays.
- **Data quality teams:** Monitor trends over time and automate responses to persistent quality issues.

It supports both reactive and proactive data quality management by providing a single pane of glass for quality status, root cause, and historical trends. ^[anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md)
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md)
- [Freshness](/concepts/freshness-data-quality.md)
- [Completeness](/concepts/data-completeness.md)
- [Percent Null](/concepts/percent-null.md)
- [Root Cause Analysis](/concepts/inference-tables-for-root-cause-analysis.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- [Unity Catalog](/concepts/unity-catalog.md)

## Sources

- anomaly-detection-databricks-on-aws.md

# Citations

1. [anomaly-detection-databricks-on-aws.md](/references/anomaly-detection-databricks-on-aws-a589cd11.md)
