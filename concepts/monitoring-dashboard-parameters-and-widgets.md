---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ae7d4a97a2d339e600f5ddb2f5b198d9451fbc0167f42c255629a3f747c7d529
  pageDirectory: concepts
  sources:
    - data-profiling-dashboard-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - monitoring-dashboard-parameters-and-widgets
    - widgets and Monitoring dashboard parameters
    - MDPAW
  citations:
    - file: data-profiling-dashboard-databricks-on-aws.md
title: Monitoring dashboard parameters and widgets
description: User-editable widgets at the top of the dashboard that control data filtering by date range, data slices, models, and other parameters, varying by analysis type.
tags:
  - databricks
  - dashboard
  - filtering
  - parameters
timestamp: "2026-06-18T15:00:49.028Z"
---

# Monitoring Dashboard Parameters and Widgets

**Monitoring dashboard parameters and widgets** refer to the interactive controls built into the [Data profiling dashboard](/concepts/data-profiling-dashboard.md) that allow users to customize the metrics, time ranges, and data slices displayed without modifying the underlying profile configuration. These controls make the dashboard a flexible, live viewer over the profile’s computed metric tables.

## Overview

When a [profile](/concepts/data-profiling.md) run completes, it creates a dashboard that visualizes key metrics. The dashboard comes with **user-editable parameters** at two levels:

- **Dashboard-level parameters** control global scope, such as date range, data slices, or model selection.
- **Chart-level parameters** apply to individual visualizations, enabling per-chart filtering or dimension switching.

These parameters are added automatically during dashboard creation and can be further customized or augmented by the user. ^[data-profiling-dashboard-databricks-on-aws.md]

## Dashboard Widgets

At the top of the dashboard, **widgets** (also called selectors) allow the user to pick which data to display. The available widgets depend on the profile type:

- **Snapshot analysis**: filters such as `Snapshot` selector appear.
- **Timeseries analysis**: different selectors (e.g., time range, aggregation window) are shown.
- **InferenceLog analysis**: a separate set of selectors specific to inference monitoring.

For example, the screenshot in the documentation shows filters labelled `Snapshot` for snapshot profile dashboards. Timeseries and InferenceLog dashboards present alternative selector sets. ^[data-profiling-dashboard-databricks-on-aws.md]

## Refresh and Data Lifecycle

The dashboard displays metrics that have been calculated by a profile run, but it does **not** recompute those metrics. To update the values shown, a two-step process is required:

1. **Trigger a profile refresh** (via UI or API) to recompute the metric tables.
2. **Click the Refresh button** on the dashboard to re-run the dashboard queries against the updated metric tables.

Refreshing the dashboard alone does not trigger profile calculations; it only re-reads the metric tables. Conversely, updating the profile tables does not automatically update the dashboard—the dashboard must be explicitly refreshed. ^[data-profiling-dashboard-databricks-on-aws.md]

## Customization

Because the dashboard is a standard Databricks Dashboard, it is fully customizable and sharable. Users can:

- Edit existing charts.
- Add new charts.
- Modify chart queries.
- Adjust dashboard and chart parameters.
- Share the dashboard with others.

For general guidance on using and customizing dashboards, including editing charts, viewing queries, and adding new visualizations, refer to the Dashboards documentation. ^[data-profiling-dashboard-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) – The process that generates the metric tables underlying this dashboard.
- [Data profiling dashboard](/concepts/data-profiling-dashboard.md) – The automatically created dashboard that hosts these parameters and widgets.
- Schedule monitoring – How to set up periodic profile runs so dashboard data stays current.
- [Unity Catalog Quality Monitoring](/concepts/unity-catalog-data-quality-monitoring.md) – The broader framework for data quality monitoring.
- Dashboard Parameters – General concept of parameters in Databricks dashboards.
- [Catalog Explorer](/concepts/catalog-explorer.md) – How to access the dashboard from the table’s **Quality** tab.

## Sources

- data-profiling-dashboard-databricks-on-aws.md

# Citations

1. [data-profiling-dashboard-databricks-on-aws.md](/references/data-profiling-dashboard-databricks-on-aws-7be46e44.md)
