---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 30382c83ca1a5c3a5daa7f61bb1a5d6c5f9fcdca279c5e66e8dea47c64c6a0f5
  pageDirectory: concepts
  sources:
    - data-profiling-dashboard-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-profiling-dashboard-filters
    - DPDF
  citations:
    - file: data-profiling-dashboard-databricks-on-aws.md
title: Data Profiling Dashboard Filters
description: Widgets at the top of the dashboard that control which data is displayed, with different selectors for Snapshot, Timeseries, and InferenceLog analysis profiles.
tags:
  - databricks
  - data-profiling
  - filters
  - profile-types
timestamp: "2026-06-18T11:31:05.777Z"
---

# Data Profiling Dashboard Filters

**Data Profiling Dashboard Filters** are user-editable controls that allow you to customize the data displayed in the automatically generated dashboard that is created when a data profile runs. These filters enable you to adjust the date range, data slices, models, and other parameters without modifying the underlying profile or metric tables. ^[data-profiling-dashboard-databricks-on-aws.md]

## Overview

When a profile runs, it creates a dashboard that displays key metrics computed by the profile. The dashboard includes user-editable parameters for both the entire dashboard and for each chart, allowing you to customize the view according to your needs. You can also modify the charts shown or add new ones. ^[data-profiling-dashboard-databricks-on-aws.md]

## Filter Types

The filters available depend on the profile type. The dashboard displays different selectors for each analysis type: ^[data-profiling-dashboard-databricks-on-aws.md]

- **Snapshot analysis** — Shows the default selectors for controlling data displayed
- **Timeseries analysis** — Displays different selectors appropriate for time-based data
- **InferenceLog analysis** — Shows selectors relevant to inference log data

The widgets at the top of the dashboard control what data is included in the visualizations. ^[data-profiling-dashboard-databricks-on-aws.md]

## Using Filters

### Selecting Data to Display

Use the widgets at the top of the dashboard to control what data is included. The filters allow you to customize: ^[data-profiling-dashboard-databricks-on-aws.md]

- Date range
- Data slices
- Models
- Other parameters as configured

### Dashboard-Level Parameters

Parameters can be set at the dashboard level, affecting all charts, or at the individual chart level, allowing fine-grained control over specific visualizations. ^[data-profiling-dashboard-databricks-on-aws.md]

## Relationship with Profile Refreshes

The dashboard filters operate independently from profile calculations: ^[data-profiling-dashboard-databricks-on-aws.md]

- **Filtering does not trigger profile recalculations.** Changing filters only runs queries over the existing metric tables that the dashboard uses to generate visualizations.
- **Profile refreshes are separate.** To update the data in the metric tables, you must trigger a profile refresh using the UI or the API, or set up a scheduled run.
- **Dashboard updates are separate.** After a profile refresh updates the metric tables, you must click the **Refresh** button on the dashboard to update the visualizations shown.

## Best Practices

- **Refresh the profile first, then the dashboard.** When you trigger a profile refresh, the metric tables are updated, but the dashboard is not automatically updated. Always click **Refresh** on the dashboard after a profile refresh to see the latest metrics. ^[data-profiling-dashboard-databricks-on-aws.md]
- **Use filters to narrow focus.** Apply filters to examine specific time periods, data slices, or models without affecting the underlying profile calculations.
- **Customize charts as needed.** Filters complement the ability to modify existing charts or add new ones to the dashboard.

## Related Concepts

- [Data profiling dashboard](/concepts/data-profiling-dashboard.md) — The dashboard automatically created when a profile runs
- [Data Profiling](/concepts/data-profiling.md) — The process of profiling data quality metrics
- [Profile Refresh](/concepts/profile-refresh-mechanism.md) — Triggering recalculation of profile metrics
- [Catalog Explorer](/concepts/catalog-explorer.md) — UI for navigating to the dashboard from the primary table
- Dashboards in Databricks — General platform for creating and customizing dashboards

## Sources

- data-profiling-dashboard-databricks-on-aws.md

# Citations

1. [data-profiling-dashboard-databricks-on-aws.md](/references/data-profiling-dashboard-databricks-on-aws-7be46e44.md)
