---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 174c896c7229d858b4996de232b17386a7bed4615d418f277adaee55562a02fc
  pageDirectory: concepts
  sources:
    - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - parallel-coordinates-chart-in-mlflow
    - PCCIM
    - Parallel Coordinates Chart
    - parallel coordinates charts
  citations:
    - file: compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
title: Parallel Coordinates Chart in MLflow
description: A visualization type in MLflow used to understand the effect of parameter settings on model performance and investigate relationships between parameters and metrics.
tags:
  - mlflow
  - visualization
  - hyperparameter-tuning
timestamp: "2026-06-19T17:47:31.564Z"
---

```markdown
---
title: Parallel Coordinates Chart in MLflow
summary: A parallel coordinates plot used in MLflow to understand the effect of parameter settings on model performance and to investigate relationships between parameters and metrics.
sources:
  - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T14:19:17.960Z"
updatedAt: "2026-06-19T14:19:17.960Z"
tags:
  - mlflow
  - visualization
  - chart-types
aliases:
  - parallel-coordinates-chart-in-mlflow
  - PCCIM
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

## Parallel Coordinates Chart in MLflow

A **Parallel Coordinates Chart** is a visualization type available in the MLflow UI that helps explore the relationship between hyperparameter settings and model performance metrics across multiple experiment runs. It is particularly useful for understanding how different parameter combinations affect a chosen metric and for identifying parameter ranges that lead to optimal results. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

### Overview

Parallel coordinates plots display each run as a line that passes through a series of parallel vertical axes. Each vertical axis represents a different parameter or metric. By observing the path of these lines, you can visually assess the effect of various parameter settings on model performance and investigate correlations between parameters. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

### Creating a Parallel Coordinates Chart

To create a parallel coordinates plot, use the **Add chart** menu on the Chart view page of an experiment and select **Parallel coordinates**. A dialog will appear where you can select the parameters and metrics you wish to investigate. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

### Interpreting the Chart

In the resulting plot, you can trace the lines of individual runs. Runs highlighted in the chart often show a clear pattern between parameter settings and metric values. For example, the chart can reveal that lower values for a parameter like `max_depth` consistently result in higher values for a metric like `auc`. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

### Related Concepts

- Compare MLflow Runs and Models Using Graphs and Charts — An overview of the visualization options in the MLflow UI.
- [[MLflow Experiment|MLflow Experiments]] — The organizational container for runs that this chart visualizes.
- [[Hyperparameter Tuning]] — The practice of systematically varying model parameters to optimize performance, which parallel coordinates charts help analyze.

### Sources

- compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
```

# Citations

1. [compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md](/references/compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws-ab27c56a.md)
