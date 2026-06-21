---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8bce4c0238960818a1791b7a6418315ef5e06fc396a92423d5afc9b76bce7b95
  pageDirectory: concepts
  sources:
    - data-profiling-dashboard-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - metric-tables-vs-dashboard-separation
    - MTVDS
  citations:
    - file: data-profiling-dashboard-databricks-on-aws.md
title: Metric tables vs dashboard separation
description: The architectural separation where profile updates write to metric tables, but the dashboard runs separate SQL queries over those tables, requiring independent refresh operations.
tags:
  - databricks
  - architecture
  - data-profiling
  - refresh
timestamp: "2026-06-18T15:00:47.797Z"
---

# Metric Tables vs Dashboard Separation

**Metric tables vs dashboard separation** refers to the architectural distinction in Databricks data profiling where metric tables and dashboards are updated independently. Understanding this separation is critical for troubleshooting why dashboard visualizations may not reflect the most recent profile run.

## Overview

When a [Data Profiling](/concepts/data-profiling.md) monitor runs in [Unity Catalog](/concepts/unity-catalog.md), it generates two distinct artifacts that are not automatically synchronized:

1. **Metric tables** — The underlying datasets that store computed profile statistics and metrics.
2. **Dashboard** — A visualization layer that queries the metric tables to display charts and summaries.

These two components are updated through separate processes, and refreshing one does not automatically refresh the other. ^[data-profiling-dashboard-databricks-on-aws.md]

## How Updates Differ

### Triggering a Profile Refresh

When you trigger a profile refresh (via the [UI](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/create-monitor-ui#refresh), the [API](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/create-monitor-api#refresh), or a [schedule](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/create-monitor-ui#schedule)), only the **metric tables** are updated. The dashboard is **not** automatically updated. ^[data-profiling-dashboard-databricks-on-aws.md]

### Refreshing the Dashboard

Clicking the **Refresh** button on the dashboard does **not** trigger profile calculations. Instead, it re-runs the queries that the dashboard uses to generate visualizations, reading from the metric tables. To see updated data on the dashboard, you must: ^[data-profiling-dashboard-databricks-on-aws.md]

1. Refresh the profile to update metric tables.
2. Then refresh the dashboard to pull the new values from those tables.

> You can't refresh the metrics from the dashboard. When you modify the dashboard, statistics aren't recalculated.
> ^[data-profiling-dashboard-databricks-on-aws.md]

## Practical Implications

- **Stale dashboards**: A dashboard may show outdated values if the profile has run but the dashboard has not been refreshed.
- **Dashboard modifications are visual only**: Editing charts, adding new visualizations, or modifying dashboard parameters does not trigger any new profile calculations. ^[data-profiling-dashboard-databricks-on-aws.md]
- **Two-step refresh workflow**: To get current data, always check that both the profile and the dashboard have been refreshed.

## Best Practices

- Establish a routine where scheduled profile runs are followed by a dashboard refresh to ensure consistency.
- When troubleshooting discrepancies between expected and displayed metrics, verify both the last profile run time and the last dashboard refresh time.
- If you customize the dashboard extensively, document that the underlying metric tables are only updated by profile runs—not by dashboard edits.

## Related Concepts

- [Data profiling dashboard](/concepts/data-profiling-dashboard.md) — The dashboard artifact itself, including its viewing and filtering options.
- [Data Profiling in Unity Catalog](/concepts/data-profiling-in-unity-catalog.md) — The broader framework for monitoring data quality.
- Monitor scheduling — How to set up automated profile runs.

## Sources

- data-profiling-dashboard-databricks-on-aws.md

# Citations

1. [data-profiling-dashboard-databricks-on-aws.md](/references/data-profiling-dashboard-databricks-on-aws-7be46e44.md)
