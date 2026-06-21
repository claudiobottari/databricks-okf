---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e2a5ca359d3de4abb7b7136657d07ed8c419278c80c6001800941f7034174b3d
  pageDirectory: concepts
  sources:
    - anomaly-detection-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - metastore-level-quality-dashboard
    - MQD
  citations:
    - file: anomaly-detection-databricks-on-aws.md
title: Metastore-Level Quality Dashboard
description: A downloadable Lakeview dashboard template that provides a workspace-wide view of all data quality results across the metastore using the system.data_quality_monitoring.table_results table.
tags:
  - data-quality
  - dashboard
  - monitoring
timestamp: "2026-06-19T22:06:24.258Z"
---

# Metastore-Level Quality Dashboard

The **Metastore-Level Quality Dashboard** is a downloadable Lakeview dashboard template that provides a single view of all data quality monitoring results across the entire [Metastore](/concepts/metastore.md). It is built on the `system.data_quality_monitoring.table_results` system table and aggregates anomaly detection outcomes for every schema and table under monitoring. ^[anomaly-detection-databricks-on-aws.md]

## Access Requirements

To use the dashboard, you must have access to the `system.data_quality_monitoring.table_results` table. By default, only account administrators have access to this table. Account admins can grant `SELECT` or other privileges to additional users or groups as needed. Without access to this system table, the dashboard will not display data. ^[anomaly-detection-databricks-on-aws.md]

## How to Import the Dashboard

1. Download the template file: [metastore-quality-dashboard.lvdash.json](https://docs.databricks.com/aws/en/assets/files/metastore-quality-dashboard.lvdash-f0c55012cc8f965edeeb5034e570c80a.json). ^[anomaly-detection-databricks-on-aws.md]
2. In the workspace sidebar, click **Dashboards**.
3. In the upper-right corner, select **Import dashboard from file** from the **Create dashboard** drop-down menu.
4. In the dialog, click **Choose file**, navigate to the downloaded `.lvdash.json` file, and click **Import dashboard**.

The dashboard is imported and appears immediately. You can then share it with other workspace users. ^[anomaly-detection-databricks-on-aws.md]

## Usage

Once imported, the dashboard displays quality results for all tables across the [Metastore](/concepts/metastore.md). It provides a centralized view for monitoring the health of every schema enrolled in anomaly detection. Administrators can use it to quickly identify unhealthy tables without navigating to individual schema dashboards. ^[anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) – The underlying mechanism that monitors table freshness and completeness.
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) – The broader feature set for tracking data quality in Unity Catalog.
- System Tables – The `system.data_quality_monitoring.table_results` table that powers the dashboard.
- [Unity Catalog](/concepts/unity-catalog.md) – The metastore-level data governance platform.
- Lakeview Dashboard – The visualization technology used for the dashboard template.
- [Health Indicators](/concepts/health-indicators-databricks.md) – Summary statuses shown per table that feed into the dashboard.

## Sources

- anomaly-detection-databricks-on-aws.md

# Citations

1. [anomaly-detection-databricks-on-aws.md](/references/anomaly-detection-databricks-on-aws-a589cd11.md)
