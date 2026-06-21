---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a3aab98f58879135163580c7e7ed8d629c3d5b7865556554a5004b387b265e5e
  pageDirectory: concepts
  sources:
    - data-profiling-dashboard-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - customizing-databricks-data-profiling-dashboards
    - CDDPD
  citations:
    - file: data-profiling-dashboard-databricks-on-aws.md
title: Customizing Databricks Data Profiling Dashboards
description: The data profiling dashboard is fully customizable and shareable — users can edit date ranges, data slices, models, modify charts, add new charts, and adjust dashboard-level and chart-level parameters.
tags:
  - databricks
  - data-profiling
  - dashboards
  - customization
timestamp: "2026-06-19T18:06:38.736Z"
---

# Customizing Databricks Data Profiling Dashboards

The **Data Profiling Dashboard** is an automatically generated dashboard created when a profile runs. It displays key metrics computed by the profile, with default visualizations that vary by profile type. The dashboard is fully customizable and shareable, just like any other Databricks dashboard. Users can edit parameters, modify charts, and add new visualizations to tailor the dashboard to their monitoring needs. ^[data-profiling-dashboard-databricks-on-aws.md]

## Viewing the Dashboard

To view the dashboard, you must be in the Databricks workspace from which data profiling was enabled. Two navigation paths are available:

- **From Catalog Explorer:** Open the **Catalog** sidebar, navigate to the primary table, click the **Quality** tab, then click **View dashboard**.
- **From the Dashboards list:** Click **Dashboards** in the left sidebar. By default, the list shows dashboards you have access to in reverse chronological order. You can filter by name, last‑modified time period, or owner.

^[data-profiling-dashboard-databricks-on-aws.md]

## Customizing the Dashboard

The dashboard supports user‑editable parameters at both the overall dashboard level and per‑chart level. Parameters allow you to control the date range, data slices, models, and other configuration options. You can also modify the existing charts or add new ones. ^[data-profiling-dashboard-databricks-on-aws.md]

Because the dashboard is a standard Databricks dashboard, all general dashboard customization features are available: editing chart queries, changing visualization types, resizing and rearranging charts, and sharing the dashboard with collaborators. For a full reference on using and customizing dashboards, see the Databricks Dashboards documentation. ^[data-profiling-dashboard-databricks-on-aws.md]

## Refreshing the Dashboard vs. Refreshing the Profile

A common source of confusion is the difference between refreshing the dashboard and refreshing the profile:

- **Profile refresh:** Triggers new calculations of metrics and updates the underlying [Profile Metrics Table](/concepts/profile-metrics-table.md) and [Drift Metrics Table](/concepts/drift-metrics-table.md). This is done using the Refresh a Monitor UI or API, or by scheduling a profile run. The dashboard is **not** automatically updated when the profile refreshes.
- **Dashboard refresh:** Clicking the **Refresh** button on the dashboard re‑runs the queries over the metric tables to update the visualizations. This does **not** trigger any new profile calculations.

Therefore, to see the latest data on the dashboard, you must first refresh the profile (to compute new metrics) and then refresh the dashboard (to fetch the updated metric tables). If you only refresh the dashboard, it will show the existing metrics from the last profile run. ^[data-profiling-dashboard-databricks-on-aws.md]

## Selecting Data to Display

Widgets at the top of the dashboard control which data is included in the visualizations. The available selectors depend on the profile type:

- For **Snapshot** analysis, the widgets allow filtering by the snapshot time.
- For **Timeseries** and **InferenceLog** analysis, additional selectors appear, such as date range and time granularity.

These selectors are user‑editable and let you dynamically adjust the displayed data without modifying the underlying metric tables. ^[data-profiling-dashboard-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) – Overview of statistical analysis on Databricks tables.
- [Profile Metrics Table](/concepts/profile-metrics-table.md) – Stores summary statistics for each column, time window, and slice.
- [Drift Metrics Table](/concepts/drift-metrics-table.md) – Stores statistics that track distribution changes over time.
- Refresh a Monitor – How to trigger profile refreshes manually or on a schedule.
- [Inference Log Analysis](/concepts/inferencelog-analysis.md) – Profile type for monitoring model predictions.
- Time Series Analysis – Profile type for continuous time windows.

## Sources

- data-profiling-dashboard-databricks-on-aws.md

# Citations

1. [data-profiling-dashboard-databricks-on-aws.md](/references/data-profiling-dashboard-databricks-on-aws-7be46e44.md)
