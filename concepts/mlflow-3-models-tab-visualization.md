---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 979f9f5169a746cca7766c2d9cc4d7b130dcabfc30f413320bbeba7b8e7ce29d
  pageDirectory: concepts
  sources:
    - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-3-models-tab-visualization
    - M3MTV
  citations:
    - file: compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
title: MLflow 3 Models Tab Visualization
description: Extension of chart view and visualization features (previously only for runs) to models from the Models tab in MLflow 3.
tags:
  - mlflow
  - visualization
  - model-registry
timestamp: "2026-06-19T09:18:54.794Z"
---

# MLflow 3 Models Tab Visualization

**MLflow 3 Models Tab Visualization** refers to the visualization capabilities available in the **Models** tab of the MLflow UI when using MLflow 3. These features allow users to compare, analyze, and visualize model runs and their associated metrics, parameters, and tags through interactive charts and graphs.

## Overview

With MLflow 3, all chart view features that were previously available only for experiments are now also available for models from the **Models** tab. This enables users to apply the same visualization and comparison tools to logged models that they use for comparing experiment runs.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

The Models tab visualization provides a collection of charts that compare the runs associated with a model. Users can customize this page by:

- Selecting specific runs to include
- Modifying existing charts
- Creating new charts
- Applying various sorting, filtering, and grouping options to runs

## Accessing the Models Tab Visualization

To display the chart view for models, click the **Chart view** icon on the experiment details page. This same icon, when applied to the Models tab, provides the same visualization capabilities for model runs.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Key Features

### Chart Management

Charts on the Models tab support the following interactions:

- **Move and resize** charts to customize the layout
- **Enlarge** charts to full screen for detailed viewing
- **Edit, delete, or download** charts using the kebab menu at the upper-right corner of each chart
- **Hover** over chart lines to display run details and tooltip information^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

### Run Selection

By default, charts display the most recent 10 runs. Users can adjust this by clicking the **Show run** icon to display the first 10, 20, or all runs. Runs that appear in charts are indicated with a colored dot, while hidden runs appear with a grayed-out dot.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

### Run Management

To manage runs in the visualization:

- **Select runs** by checking the box next to the run
- **Delete, compare, or add/remove tags** for selected runs using the action buttons that appear after selection^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

### Filtering and Sorting

Users can filter runs based on parameter or metric values or by tag using the search field. Additionally, the **Sort** dropdown menu allows sorting by parameters, and the **Group by** dropdown menu enables grouping runs by parameter value.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Creating New Visualizations

Users can add custom charts by clicking **Add chart** and selecting from chart types, including:

### Parallel Coordinates Chart

A **parallel coordinates plot** is useful for understanding the effect of parameter settings on model performance and investigating relationships between parameters and metrics. To create this chart:

1. Select **Parallel coordinates** from the menu
2. In the dialog, select the parameters and metrics to investigate

This chart type helps identify patterns, such as when lower values for certain parameters (e.g., `max_depth`) result in higher values for specific metrics (e.g., `auc`).^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Related Concepts

- Compare MLflow Runs and Models Using Graphs and Charts — Detailed documentation on chart view features
- [Track and Compare Models Using MLflow Logged Models](/concepts/mlflow-loggedmodel.md) — Information on model tracking and comparison
- [MLflow System Tables Reference](/concepts/mlflow-system-tables.md) — How MLflow metadata is available in system tables for further visualization
- Databricks SQL — Tooling for visualizing experiment data from system tables

## Sources

- compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md

# Citations

1. [compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md](/references/compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws-ab27c56a.md)
