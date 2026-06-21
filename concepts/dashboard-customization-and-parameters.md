---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 26c07e832e447c8213ebd85c63fe9d6f041d2c4569e4a5e217486723a1c52b4e
  pageDirectory: concepts
  sources:
    - data-profiling-dashboard-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dashboard-customization-and-parameters
    - Parameters and Dashboard Customization
    - DCAP
  citations:
    - file: data-profiling-dashboard-databricks-on-aws.md
title: Dashboard Customization and Parameters
description: User-editable parameters for both the entire dashboard and individual charts, allowing customization of date range, data slices, models, and chart modifications.
tags:
  - databricks
  - dashboard
  - customization
  - parameters
timestamp: "2026-06-18T11:29:55.435Z"
---

---
title: Dashboard Customization and Parameters
summary: How to customize the data profiling dashboard, including user-editable parameters for date range, data slices, and models, as well as chart modifications.
sources:
  - data-profiling-dashboard-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:35:00.000Z"
updatedAt: "2026-06-18T11:35:00.000Z"
tags:
  - databricks
  - dashboard
  - data-profiling
  - customization
aliases:
  - dashboard-customization-and-parameters
  - DCAP
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Dashboard Customization and Parameters

The data profiling dashboard, automatically created when a [Data Profiling](/concepts/data-profiling.md) run completes, provides interactive controls that let you customize which data is displayed and how it appears. The dashboard is fully customizable and shareable, just like any other Databricks dashboard. ^[data-profiling-dashboard-databricks-on-aws.md]

## Parameters and Customization

The dashboard includes user-editable parameters at two levels: the entire dashboard and individual charts. These parameters allow you to adjust the **date range**, **data slices**, **models**, and other dimensions. The left side of the dashboard shows lists of the metrics and statistics included in the tables and charts. ^[data-profiling-dashboard-databricks-on-aws.md]

You can modify the charts shown in the dashboard, add new charts, edit existing charts, view the underlying queries – all using the standard dashboard editing capabilities. For general information about customizing dashboards, see Dashboards. ^[data-profiling-dashboard-databricks-on-aws.md]

## Selecting Data to Display

Widgets at the top of the dashboard control which data is included in the visualizations. The available selectors depend on the profile type:

- **Snapshot** analysis – specific filters appear (see screenshot in documentation).
- **Timeseries** and **InferenceLog** analysis – different selectors are shown.

These widgets allow you to slice the metric data dynamically without re-running the profile. ^[data-profiling-dashboard-databricks-on-aws.md]

## Refreshing Dashboard Data

The dashboard displays metrics calculated by the most recent profile run. To update the values shown, you must first trigger a new profile refresh (via [Create a monitor UI](/concepts/data-quality-monitoring-ui.md) or Create a monitor API), then click the **Refresh** button on the dashboard. The metric tables and the dashboard are updated separately:

- A profile refresh updates the underlying metric tables.
- Clicking **Refresh** on the dashboard re-runs the queries against those metric tables to generate fresh visualizations.
- Refreshing the dashboard does **not** trigger profile calculations – you must perform both steps to see new data.

Modifying the dashboard (e.g., changing charts or parameters) does **not** recalculate the profile statistics. ^[data-profiling-dashboard-databricks-on-aws.md]

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) – The process that generates the metrics displayed in this dashboard.
- Dashboards – General Databricks dashboard documentation covering editing, sharing, and query viewing.
- [Create a monitor UI](/concepts/data-quality-monitoring-ui.md) – How to trigger a manual profile refresh from the UI.
- Create a monitor API – How to programmatically refresh the profile and set schedules.

## Sources

- data-profiling-dashboard-databricks-on-aws.md

# Citations

1. [data-profiling-dashboard-databricks-on-aws.md](/references/data-profiling-dashboard-databricks-on-aws-7be46e44.md)
