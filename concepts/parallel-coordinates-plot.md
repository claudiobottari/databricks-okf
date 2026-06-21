---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ff27bb304d86f2193805d15ecea5e86eb588f5a345fbf3146dfde6c8b788ddc8
  pageDirectory: concepts
  sources:
    - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - parallel-coordinates-plot
    - PCP
    - Parallel coordinates
    - parallel coordinates plots
    - mlflow-parallel-coordinates-plot
    - MPCP
    - parallel-coordinates-plot-for-mlflow
    - PCPFM
  citations:
    - file: compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
title: Parallel Coordinates Plot
description: A visualization type in MLflow for understanding the effect of parameter settings on model performance by investigating relationships between parameters and metrics.
tags:
  - mlflow
  - visualization
  - data-analysis
timestamp: "2026-06-19T09:18:11.718Z"
---

# Parallel Coordinates Plot

A **parallel coordinates plot** is a visualization technique used to understand the effect of parameter settings on model performance and investigate relationships between parameters and metrics. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Overview

In a parallel coordinates plot, each variable (parameter or metric) is represented as a vertical axis, and each data point (such as an [MLflow Run](/concepts/mlflow-run.md)) is drawn as a line that intersects each axis at the value of the corresponding variable. This allows viewers to visually trace how changes in parameter values correlate with changes in metrics across multiple runs. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Usage in MLflow

The parallel coordinates chart is available as a visualization option in the MLflow UI's chart view page. To create one, navigate to the experiment details page, click **Add chart**, and select **Parallel coordinates** from the dropdown menu. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

In the setup dialog, select the parameters and metrics to investigate. The resulting plot displays runs as colored lines connecting their parameter values to their resulting metric values. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Interpreting Results

The plot helps identify patterns across runs. For example, highlighting a subset of runs in the black boxes may reveal that lower values for one parameter (e.g., `max_depth`) consistently result in higher values for a target metric (e.g., `auc`). ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Related Concepts

- Compare MLflow runs and models using graphs and charts
- [MLflow experiments](/concepts/mlflow-experiment.md)
- [MLflow runs](/concepts/mlflow-run.md)
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md)
- [Experiment tracking](/concepts/mlflow-experiment-tracking.md)

## Sources

- compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md

# Citations

1. [compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md](/references/compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws-ab27c56a.md)
