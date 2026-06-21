---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bc5c252150e30af55289c40d341079674254cde6e81cc7eb8355ec3d84d58e87
  pageDirectory: concepts
  sources:
    - data-profiling-dashboard-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-profiling-dashboard-databricks
    - DPD(
  citations:
    - file: data-profiling-dashboard-databricks-on-aws.md
title: Data Profiling Dashboard (Databricks)
description: An auto-generated dashboard in Databricks that displays key metrics computed by a data profile run, organized into sections based on profile type.
tags:
  - data-governance
  - databricks
  - data-profiling
  - dashboards
timestamp: "2026-06-19T18:06:32.439Z"
---

```yaml
---
title: Data Profiling Dashboard (Databricks)
summary: An automatically generated dashboard that visualizes key metrics computed by a data profiling run in Databricks Unity Catalog.
sources:
  - data-profiling-dashboard-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T09:44:05.124Z"
updatedAt: "2026-06-19T09:44:05.124Z"
tags:
  - databricks
  - data-profiling
  - dashboard
  - unity-catalog
aliases:
  - data-profiling-dashboard-databricks
  - DPD
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Data Profiling Dashboard (Databricks)

The **Data Profiling Dashboard** is an automatically generated dashboard in Databricks that visualizes key metrics computed by a data profiling run on a Unity Catalog table. It provides a user-editable interface for exploring data quality statistics and trends over time. ^[data-profiling-dashboard-databricks-on-aws.md]

## Overview

When a data profile runs on a table, it creates a dashboard that displays the computed metrics. The visualizations included in the default dashboard configuration depend on the profile type — **Snapshot**, **Timeseries**, or **InferenceLog** — and the different metrics are organized into sections. The left side of the dashboard shows lists of the metrics and statistics included in the tables and charts. ^[data-profiling-dashboard-databricks-on-aws.md]

The dashboard is created in the user's account and is customizable and shareable like any other Databricks dashboard. Users can modify the charts shown or add new ones. ^[data-profiling-dashboard-databricks-on-aws.md]

## Parameters and Customization

The dashboard has user-editable parameters for both the entire dashboard and for each individual chart, allowing customization of:

- Date range
- Data slices
- Models (where applicable)
- Other query filters

Users can also modify existing charts or add new ones. For general information about using and customizing dashboards, including adding new charts, editing charts, and viewing queries, see the Dashboards documentation. ^[data-profiling-dashboard-databricks-on-aws.md]

## Viewing the Dashboard

To view the data profiling dashboard, you must use the Databricks workspace from which data profiling was enabled. Two navigation paths are available:

1. **Via Catalog Explorer**: In the left sidebar, click **Catalog** to open the Catalog Explorer UI. Navigate to the primary table, then click the **Quality** tab, and select **View dashboard**.

2. **Via Dashboards list**: In the left sidebar, click **Dashboards**. By default, the dashboard listing page shows dashboards you have access to, sorted in reverse chronological order. You can filter the list by name, last modified time period, or owner. ^[data-profiling-dashboard-databricks-on-aws.md]

## Refreshing the Dashboard

The dashboard displays metrics that have been calculated by the profile. Refreshing the data involves two separate steps:

1. **Trigger a profile refresh**: Use the UI or the API to recalculate the profile metrics. The metric tables are updated when the profile runs, but the dashboard is **not** automatically updated.

2. **Refresh the dashboard**: Click the **Refresh** button on the dashboard. This runs the queries over the metric tables that the dashboard uses to generate visualizations. It does **not** trigger profile calculations — it only re-fetches the latest data from the already-computed metric tables.

You cannot refresh the metrics directly from the dashboard, and modifying the dashboard does not trigger statistic recalculation. To update the data in the tables used for visualizations, you must refresh the profile and then refresh the dashboard. ^[data-profiling-dashboard-databricks-on-aws.md]

## Selecting Data to Display

Use the widgets at the top of the dashboard to control what data is included. The specific selectors available depend on the profile type:

- For **Snapshot** analysis, the screenshot shows filters such as date range and data slices.
- For **Timeseries** analysis, different selectors appear.
- For **InferenceLog** analysis, different selectors appear. ^[data-profiling-dashboard-databricks-on-aws.md]

## Related Concepts

- [[Data Profiling]] — The foundational process that generates the metrics displayed in the dashboard
- [[Unity Catalog]] — The governance layer that stores the tables being profiled
- [[Data Quality Monitoring]] — Broader practice of monitoring data quality over time
- Databricks Dashboards — General dashboard platform used by the profiling dashboard

## Sources

- data-profiling-dashboard-databricks-on-aws.md
```

# Citations

1. [data-profiling-dashboard-databricks-on-aws.md](/references/data-profiling-dashboard-databricks-on-aws-7be46e44.md)
