---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7b07c3353fa4a137f3f07735c1f5771504a2461193c7980558461fce9370fee8
  pageDirectory: concepts
  sources:
    - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - comparing-runs-from-multiple-experiments
    - CRFME
    - Compare Runs from Multiple Experiments
    - Compare runs from multiple experiments
    - Comparing Runs Across Experiments
  citations:
    - file: compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
title: Comparing Runs from Multiple Experiments
description: Ability to display and compare MLflow runs across different experiments for broader analysis.
tags:
  - mlflow
  - experiment-tracking
  - comparison
timestamp: "2026-06-18T14:40:28.659Z"
---

# Comparing Runs from Multiple Experiments

**Comparing Runs from Multiple Experiments** refers to the ability to display and analyze MLflow runs that belong to different experiments side‑by‑side. This feature is available from the MLflow UI and helps users evaluate model performance, parameter settings, and metrics across training runs that were logged under separate experiments.

## Overview

The standard **Chart view** page in the MLflow UI provides a collection of charts comparing the runs of a *single* experiment. You can customize this page by selecting which runs to include, modifying existing charts, and creating new charts.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

To view runs from *multiple* experiments together, a dedicated workflow is available. From the experiment details page, follow the link to the **Compare runs from multiple experiments** documentation.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## How to Access

On the experiment details page, click the **Chart view** icon. Then use the link provided in the page heading to select runs from multiple experiments. (The exact steps are described in the official Databricks documentation under “Compare runs from multiple experiments”.)

## Related Visualizations

Once runs from multiple experiments are displayed, the same kind of chart customizations available for single‑experiment comparisons apply:

- **Parallel coordinates charts** to explore relationships between parameters and metrics.
- **Run selection**, filtering by parameter / metric values, sorting, and grouping by parameter values.^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

These features help identify how changes in hyperparameters affect model quality across different experiments.

## Related Concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md) – The organizational unit for runs.
- [MLflow Runs](/concepts/mlflow-run.md) – Individual training executions.
- [Chart View](/concepts/mlflow-chart-view.md) – The visualization dashboard for comparing runs.
- [Parallel Coordinates Plot](/concepts/parallel-coordinates-plot.md) – A chart type for high‑dimensional parameter space exploration.

## Sources

- compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md

# Citations

1. [compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md](/references/compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws-ab27c56a.md)
