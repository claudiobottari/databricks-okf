---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2e8e6b93abe29d2cac508e1592462e90b724f6e7e9915261297375307de50e18
  pageDirectory: concepts
  sources:
    - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - run-management-in-mlflow-ui
    - RMIMU
  citations:
    - file: compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
title: Run Management in MLflow UI
description: Features for managing MLflow runs including selecting runs to display, deleting, comparing, adding/editing tags, filtering by parameter/metric values or tags, sorting by parameters, and grouping by parameter values.
tags:
  - mlflow
  - experiment-tracking
  - workflow
timestamp: "2026-06-19T09:18:27.895Z"
---

# Run Management in MLflow UI

**Run Management in MLflow UI** refers to the tools and workflows available in the MLflow user interface for organizing, comparing, filtering, sorting, and visualizing experiment runs. The MLflow UI provides both a runs list page for viewing individual training results and a chart view page for comparing runs through visualizations.

## Chart View Overview

The chart view page displays a collection of charts comparing the runs of an experiment. By default, charts show the most recent 10 runs. You can customize this page by selecting which runs to display, modifying existing charts, and creating new charts. With [MLflow 3](/concepts/mlflow-3.md), these chart features are also available for models from the **Models** tab. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

To access the chart view, click the **Chart view** icon on the experiment details page. Charts can be moved, resized, or enlarged to full screen. A kebab menu at the upper-right of each chart provides options to edit, delete, or download the chart. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Selecting Runs to Display

You can control which runs appear in the charts by using the show/hide run menu at the top of the runs list. This menu lets you display the first 10, first 20, or all runs. Runs shown on the charts are indicated by a colored dot, while hidden runs appear with a grayed-out dot. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Managing Runs

To manage runs, check the box next to one or more runs. When runs are selected, the **Delete**, **Compare**, and **Add tags** buttons appear, allowing you to perform batch operations on the selected runs. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Filtering Runs

Use the search field to the right of the **Chart view** icon to filter runs based on parameter values, metric values, or tags. This helps narrow down the displayed runs to those matching specific criteria. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Sorting Runs

To change the sort order of runs shown in the charts, select the parameter to sort by from the **Sort** dropdown menu. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Grouping Runs

To group runs by parameter value, select one or more parameters from the **Group by** dropdown menu. This organizes runs into clusters based on shared parameter values. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Creating New Visualizations

To add a chart, click **Add chart** and select the type of chart to create from the dropdown menu. Available chart types allow you to customize how run data is visualized. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

### Parallel Coordinates Chart

A parallel coordinates plot helps you understand the effect of parameter settings on model performance and investigate relationships between parameters and metrics. To create one, select **Parallel coordinates** from the **Add chart** menu, then choose the parameters and metrics to explore. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Interaction with Charts

As you roll your cursor over the lines on a chart, details for that run appear, with lines highlighting to show run information. This provides a quick way to inspect individual run results within the chart view. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational container for runs
- [Compare runs from multiple experiments](/concepts/comparing-runs-from-multiple-experiments.md) — Viewing runs across experiment boundaries
- [Track and compare models using MLflow Logged Models](/concepts/mlflow-loggedmodel.md) — Model-level comparison in MLflow 3
- [MLflow System Tables](/concepts/mlflow-system-tables.md) — Accessing run metadata for advanced analysis with Databricks SQL
- [View training results with MLflow runs](/concepts/filtering-and-sorting-mlflow-runs.md) — The runs list page interface

## Sources

- compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md

# Citations

1. [compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md](/references/compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws-ab27c56a.md)
