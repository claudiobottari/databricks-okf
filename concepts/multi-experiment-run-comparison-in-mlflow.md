---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f682fc749f26904923b11972b7fe54e2902daff920089aaa52ca374b7b316ce1
  pageDirectory: concepts
  sources:
    - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - multi-experiment-run-comparison-in-mlflow
    - MRCIM
  citations:
    - file: compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
title: Multi-Experiment Run Comparison in MLflow
description: The capability to display and compare runs across multiple experiments simultaneously in the MLflow UI.
tags:
  - mlflow
  - experiment-tracking
  - comparison
timestamp: "2026-06-19T14:20:18.527Z"
---

# Multi-Experiment Run Comparison in MLflow

**Multi-Experiment Run Comparison** refers to the ability in [MLflow](/concepts/mlflow.md) to visualize and compare training runs that belong to different experiments side-by-side. This feature enables researchers and engineers to analyze results across multiple experiments without consolidating runs into a single experiment.

## Overview

By default, the MLflow chart view displays runs from a single experiment. However, MLflow provides functionality to compare runs from multiple experiments directly from the runs list page, allowing users to evaluate model performance across different experimental setups in a unified view.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Accessing Multi-Experiment Comparison

To display runs from multiple experiments, navigate to the runs list page and select the option to [compare runs from multiple experiments](https://docs.databricks.com/aws/en/mlflow/runs#compare-runs-from-multiple-expts). This feature is available through the standard MLflow UI workflow for experiment comparison.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Visualization Capabilities

Once multiple experiments are selected, all standard chart view functionality applies:

- **Chart types**: The same chart types available for single-experiment comparison, including [parallel coordinates charts](/concepts/parallel-coordinates-chart-in-mlflow.md), are available for multi-experiment comparisons.
- **Run management**: Users can select, filter, sort, group, and manage runs across experiments using the same controls as single-experiment views.
- **Chart customization**: Charts can be added, edited, resized, or downloaded using the chart controls.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

### Run Selection

To control which runs appear in the multi-experiment view:

1. Click the show-run icon at the top of the runs list to select the number of runs to display (first 10, 20, or all runs).
2. Use the search field to filter runs based on parameter, metric, or tag values.
3. Use the **Sort** dropdown to change the sort order by a parameter.
4. Use the **Group by** dropdown to group runs by parameter value across experiments.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Alternative Analysis Methods

In addition to the UI-based comparison, MLflow metadata for experiments and runs is available in system tables. This allows users to leverage Databricks SQL and lakehouse tooling to create custom visualizations and analysis of experiment data across multiple experiments. See the [MLflow system tables reference](https://docs.databricks.com/aws/en/admin/system-tables/mlflow) for further details.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## MLflow 3 Enhancements

With [MLflow 3](/concepts/mlflow-3.md), the visualization and comparison features described above—including multi-experiment run comparison—are also available for models from the **Models** tab. For more details, see [Track and compare models using MLflow Logged Models](https://docs.databricks.com/aws/en/mlflow/logged-model).^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for MLflow runs
- Chart View in MLflow — The visualization page for comparing runs
- [Parallel Coordinates Chart](/concepts/parallel-coordinates-chart-in-mlflow.md) — A chart type useful for multi-experiment analysis
- [MLflow Run Comparison](/concepts/mlflow-run-comparison.md) — Comparing individual runs within a single experiment
- Tracking and Comparing Models — Model-level comparison features

## Sources

- compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md

# Citations

1. [compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md](/references/compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws-ab27c56a.md)
