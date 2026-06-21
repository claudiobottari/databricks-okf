---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 83c52d3961bb16140fdd7960b1d552d62aa3b5e11061c44a2cd40d2815f24ad8
  pageDirectory: concepts
  sources:
    - data-profiling-dashboard-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dashboard-refresh-mechanism
    - DRM
    - DLRM
  citations:
    - file: data-profiling-dashboard-databricks-on-aws.md
title: Dashboard Refresh Mechanism
description: A two-step process where profile calculations must be refreshed to update metric tables, then the dashboard must be separately refreshed to reflect the new data.
tags:
  - databricks
  - data-profiling
  - dashboard
  - workflow
timestamp: "2026-06-18T11:30:10.064Z"
---

# Dashboard Refresh Mechanism

The **Dashboard Refresh Mechanism** describes the process by which data displayed on a data profiling dashboard is updated. The dashboard itself does not compute metrics — it visualizes data stored in underlying metric tables that are populated by profile runs. Refreshing the dashboard and refreshing the profile are two distinct operations that must be performed in sequence to see updated data. ^[data-profiling-dashboard-databricks-on-aws.md]

## Refresh Flow

### Triggering a Profile Refresh

To update the underlying data, you must trigger a profile refresh. This can be done using the UI or the API, or by setting up a scheduled run. The profile refresh recalculates metrics and updates the metric tables. ^[data-profiling-dashboard-databricks-on-aws.md]

- **UI**: Navigate to the primary table in Catalog Explorer, open the **Quality** tab, and use the refresh option.
- **API**: Use the appropriate API endpoint to trigger a profile refresh programmatically.
- **Schedule**: Configure recurring profile runs using the UI or API to automate refreshes.

The metric tables and the dashboard are updated separately. When you trigger a profile refresh, the metric tables are updated, but the dashboard itself is not automatically updated. ^[data-profiling-dashboard-databricks-on-aws.md]

### Refreshing the Dashboard Display

After the profile refresh has updated the metric tables, you must refresh the dashboard to see the new data. To do this, click the **Refresh** button on the dashboard. This action runs the queries that the dashboard uses to generate visualizations, reading from the metric tables. ^[data-profiling-dashboard-databricks-on-aws.md]

Clicking **Refresh** on the dashboard does **not** trigger profile calculations. It only updates the visualizations by re-running queries against the existing metric tables. Conversely, modifying the dashboard (for example, editing charts or adding new ones) does not trigger profile recalculations. ^[data-profiling-dashboard-databricks-on-aws.md]

### Complete Refresh Sequence

To fully update the data shown on the dashboard, you must perform both steps in order:

1. **Refresh the profile** to update the metric tables with new calculations.
2. **Refresh the dashboard** to update the visualizations with the latest data from the metric tables.

Performing only one of these steps will result in stale or mismatched data.

## Related Concepts

- [Data profiling dashboard](/concepts/data-profiling-dashboard.md) — The dashboard that displays profile metrics and statistics
- [Data Profiling](/concepts/data-profiling.md) — The process of computing quality metrics for tables
- [Profile Schedules](/concepts/profile-refresh-and-scheduling.md) — Automated schedule configuration for recurring profile runs
- [Metric Tables](/concepts/profile-metric-tables.md) — Underlying tables populated by profile runs that the dashboard queries

## Sources

- data-profiling-dashboard-databricks-on-aws.md

# Citations

1. [data-profiling-dashboard-databricks-on-aws.md](/references/data-profiling-dashboard-databricks-on-aws-7be46e44.md)
