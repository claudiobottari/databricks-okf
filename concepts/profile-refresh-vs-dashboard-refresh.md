---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 94ce06f37bafec7e4ca289a8c0f1c41994959657fbe8687a158e63b705ed9a93
  pageDirectory: concepts
  sources:
    - data-profiling-dashboard-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - profile-refresh-vs-dashboard-refresh
    - PRVDR
  citations:
    - file: data-profiling-dashboard-databricks-on-aws.md
title: Profile Refresh vs Dashboard Refresh
description: The distinction between refreshing the underlying profile metrics (via UI/API/schedule) and refreshing the dashboard's visualizations (via dashboard Refresh button); both must be done independently.
tags:
  - databricks
  - data-profiling
  - dashboard
  - workflow
timestamp: "2026-06-19T09:44:18.129Z"
---

# Profile Refresh vs Dashboard Refresh

**Profile Refresh** and **Dashboard Refresh** are two distinct operations in the Databricks [Data Profiling](/concepts/data-profiling.md) workflow. A profile refresh recalculates the underlying metrics from the source table, while a dashboard refresh loads the latest results from those metric tables into the dashboard visualizations. They must be performed sequentially to see up‑to‑date data: first refresh the profile, then refresh the dashboard. ^[data-profiling-dashboard-databricks-on-aws.md]

## How Profile Refresh Works

A profile refresh triggers the profiling engine to re‑run its computations against the monitored table. This updates the metric tables that store the computed statistics, such as row counts, null fractions, and distribution summaries. You can initiate a profile refresh through the Catalog Explorer UI or the API, and you can also set up a scheduled run to perform it automatically. ^[data-profiling-dashboard-databricks-on-aws.md]

Profile refresh is the only way to recalculate metrics. You **cannot** refresh profile metrics from the dashboard itself. ^[data-profiling-dashboard-databricks-on-aws.md]

## How Dashboard Refresh Works

The dashboard displays visualizations based on the data stored in the metric tables. When you click the **Refresh** button on the dashboard, it runs the underlying queries against those metric tables again, pulling the most recent data into the charts. This action **does not** trigger a new profile calculation — it simply re‑reads whatever data is already in the tables. ^[data-profiling-dashboard-databricks-on-aws.md]

If you modify the dashboard (e.g., change chart types or parameters), the statistics are **not** recalculated. You must still run a separate profile refresh to recompute the underlying data. ^[data-profiling-dashboard-databricks-on-aws.md]

## Key Differences

| Aspect | Profile Refresh | Dashboard Refresh |
|--------|----------------|-------------------|
| **What it does** | Recomputes profile metrics from the source table | Re‑queries the metric tables to load latest values |
| **How to trigger** | UI (Catalog Explorer), API, scheduled run | Click the **Refresh** button on the dashboard |
| **Affects metric tables** | Yes – updates the stored statistics | No – uses existing data |
| **Affects dashboard visuals** | Only after a subsequent dashboard refresh | Yes – displays latest data from metric tables |
| **When to use** | When new data has arrived in the source table | After a profile refresh has completed |

## Best Practices

To ensure the dashboard shows accurate, up‑to‑date metrics, always perform the operations in order:

1. **Refresh the profile** (or let a scheduled run do it).
2. **Refresh the dashboard** to see the newly computed values. ^[data-profiling-dashboard-databricks-on-aws.md]

If you only refresh the dashboard, you will see the same old metrics. If you only refresh the profile, the dashboard will remain unchanged until you manually refresh it.

## Related Concepts

- [Data Profiling](/concepts/data-profiling.md) – Introduction to the profiling feature.
- Create a Data Profile Monitor (UI) – How to set up and schedule profiles.
- [Create a Data Profile Monitor (API)](/concepts/databricks-data-profiling-api.md) – Programmatic profile management.
- Dashboards on Databricks – General dashboard usage and customization.
- [Catalog Explorer](/concepts/catalog-explorer.md) – UI for viewing table quality and dashboard links.

## Sources

- data-profiling-dashboard-databricks-on-aws.md

# Citations

1. [data-profiling-dashboard-databricks-on-aws.md](/references/data-profiling-dashboard-databricks-on-aws-7be46e44.md)
