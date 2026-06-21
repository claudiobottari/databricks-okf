---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dc93797f4debfd5d5a50162cb35cc6ad745c556fd73351fe43ce87fb2b8d6758
  pageDirectory: concepts
  sources:
    - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - grouping-runs-by-parameter
    - GRBP
  citations:
    - file: compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
title: Grouping Runs by Parameter
description: Feature to group MLflow runs by one or more parameter values for comparative analysis in chart views.
tags:
  - mlflow
  - visualization
  - experiment-tracking
timestamp: "2026-06-18T14:40:28.174Z"
---

# Grouping Runs by Parameter

**Grouping Runs by Parameter** is a feature in the [MLflow UI](/concepts/mlflow.md) chart view that lets you organize runs by their parameter values. This makes it easier to compare runs that share the same hyperparameters and to spot patterns across different parameter combinations.

## Overview

On the chart view page of an MLflow experiment, you can group displayed runs by one or more parameters using the **Group by** dropdown menu. When you select a parameter, runs with the same value for that parameter are collected together in the charts. Selecting multiple parameters creates nested groupings. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

Grouping is complementary to filtering and sorting runs. You can first filter runs by a parameter or metric value, then group the remaining runs by another parameter to focus on a specific subset. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Usage

1. Navigate to the experiment details page in the MLflow UI.
2. Click the **Chart view** icon to open the chart view page.
3. From the **Group by** dropdown menu, select one or more parameters to group by. The charts will update to reflect the grouping.

To ungroup, clear the selection from the **Group by** menu. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Related Features

- **Filter Runs** – Search runs by parameter, metric, or tag values.
- **Sort Runs** – Change the order of runs displayed in charts.
- **[Parallel Coordinates Chart](/concepts/parallel-coordinates-chart-in-mlflow.md)** – A visualization that shows the relationship between parameter settings and metrics across runs. Grouping by parameter can help populate this chart with the runs you want to compare.
- **[Run Comparison](/concepts/mlflow-run-comparison.md)** – Compare selected runs side-by-side.
- **[Chart View](/concepts/mlflow-chart-view.md)** – The page where grouping, filtering, and chart customization are available.

## Availability

Grouping runs by parameter is available for experiments. With MLflow 3, these chart view features are also available for models from the **Models** tab. For more information, see [Track and compare models using MLflow Logged Models](https://docs.databricks.com/aws/en/mlflow/logged-model). ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Sources

- compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md

# Citations

1. [compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md](/references/compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws-ab27c56a.md)
