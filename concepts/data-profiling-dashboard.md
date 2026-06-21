---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ed91d78d8a93a710d85a0b3c7a3aff75b749271fa93eb0f32a9320fbb643d485
  pageDirectory: concepts
  sources:
    - data-profiling-dashboard-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-profiling-dashboard
    - DPD
  citations:
    - file: data-profiling-dashboard-databricks-on-aws.md
title: Data profiling dashboard
description: A dashboard automatically created by Databricks when a data profile is run, displaying key metrics computed by the profile in customizable visualizations.
tags:
  - databricks
  - data-profiling
  - dashboard
  - data-quality
timestamp: "2026-06-18T15:00:17.318Z"
---

# Data Profiling Dashboard

The **Data Profiling Dashboard** is an automatically generated dashboard in Databricks that displays key metrics computed by a [Data Profile](/concepts/data-profile-databricks.md) run. When a profile is executed against a table in [Unity Catalog](/concepts/unity-catalog.md), Databricks creates this dashboard to visualize the statistical summaries and quality metrics calculated during profiling. ^[data-profiling-dashboard-databricks-on-aws.md]

## Dashboard Contents

The visualizations included in the default dashboard configuration depend on the profile type (Snapshot, Timeseries, or InferenceLog). Metrics are organized into sections, with the left side of the dashboard showing lists of the metrics and statistics included in the tables and charts. ^[data-profiling-dashboard-databricks-on-aws.md]

## Customization

The dashboard has user-editable parameters for both the entire dashboard and for each individual chart, allowing you to customize the date range, data slices, models, and other display options. You can also modify the charts shown or add new ones. The dashboard is created in the user's account and is customizable and shareable like any dashboard. For general information about using and customizing dashboards, including adding new charts, editing charts, viewing queries, and so on, see the Dashboards documentation. ^[data-profiling-dashboard-databricks-on-aws.md]

## Viewing the Dashboard

To view the data profiling dashboard, you must use the Databricks workspace from which data profiling was enabled. There are two ways to access it: ^[data-profiling-dashboard-databricks-on-aws.md]

1. **From Catalog Explorer**: Click **Catalog** in the left sidebar to open Catalog Explorer. Navigate to the primary table, click the **Quality** tab, then click **View dashboard**.
2. **From the Dashboards listing**: Click **Dashboards** in the left sidebar. By default, the listing shows dashboards you have access to, sorted in reverse chronological order. You can filter by name, last modified time period, or owner.

## Refreshing the Dashboard

The dashboard displays metrics that have been calculated by the profile. To update the values shown, you must trigger a profile refresh using the Create Monitor UI or Create Monitor API, or set up a scheduled run. You cannot refresh the metrics from the dashboard itself, and modifying the dashboard does not recalculate statistics. ^[data-profiling-dashboard-databricks-on-aws.md]

The metric tables and the dashboard are updated separately: ^[data-profiling-dashboard-databricks-on-aws.md]

- When you trigger a profile refresh, the metric tables are updated, but the dashboard is not automatically updated.
- When you click **Refresh** on the dashboard, it runs the queries over the metric tables to regenerate visualizations — it does not trigger profile calculations.

To see updated data in the dashboard, you must first refresh the profile, then refresh the dashboard. ^[data-profiling-dashboard-databricks-on-aws.md]

## Selecting Data to Display

Use the widgets at the top of the dashboard to control what data is included. For **Snapshot** analysis, specific filters are shown; for **Timeseries** and **InferenceLog** analysis, different selectors appear. ^[data-profiling-dashboard-databricks-on-aws.md]

## Related Concepts

- [Data Profile](/concepts/data-profile-databricks.md) — The profiling process that generates metrics for the dashboard
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — The broader monitoring framework in Unity Catalog
- Create Monitor UI — How to set up profiling and monitoring through the interface
- Create Monitor API — How to set up profiling and monitoring programmatically
- Dashboards — General documentation for working with Databricks dashboards

## Sources

- data-profiling-dashboard-databricks-on-aws.md

# Citations

1. [data-profiling-dashboard-databricks-on-aws.md](/references/data-profiling-dashboard-databricks-on-aws-7be46e44.md)
