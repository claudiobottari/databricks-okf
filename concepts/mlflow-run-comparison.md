---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: eacae217fcedffa87a9d610b211ca05e628904085049a1042371ec52c64a66d5
  pageDirectory: concepts
  sources:
    - view-training-results-with-mlflow-runs-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-run-comparison
    - MRC
    - Run Comparison
  citations:
    - file: view-training-results-with-mlflow-runs-databricks-on-aws.md
title: MLflow Run Comparison
description: A feature to compare multiple MLflow runs from single or multiple experiments in tabular format with parameter and metric side-by-side views, diff toggling, and visualization support.
tags:
  - mlflow
  - experiment-tracking
  - visualization
timestamp: "2026-06-19T23:25:37.287Z"
---

# [MLflow Run](/concepts/mlflow-run.md) Comparison

**MLflow Run Comparison** is a feature that allows you to compare the results of multiple [MLflow](/concepts/mlflow.md) runs side by side, either from a single experiment or from multiple experiments. The comparison page presents information about selected runs in tabular format, including run parameters, metrics, and visualizations. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

## Overview

An [MLflow Run](/concepts/mlflow-run.md) corresponds to a single execution of model code, recording parameters, metrics, tags, artifacts, and other metadata. The run comparison feature enables you to analyze and contrast these recorded values across different runs to identify the best-performing model configurations. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

## Comparing Runs from a Single Experiment

To compare runs from a single experiment:

1. On the [MLflow Experiment](/concepts/mlflow-experiment.md) details page, select two or more runs by clicking the checkbox to the left of each run, or select all runs by checking the box at the top of the column.
2. Click **Compare**. The Comparing `<N>` Runs screen appears, displaying the selected runs in tabular format. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

## [Comparing Runs from Multiple Experiments](/concepts/comparing-runs-from-multiple-experiments.md)

To compare runs from multiple experiments:

1. On the experiments page, select the experiments you want to compare by clicking the box at the left of the experiment name.
2. Click **Compare (n)** (where **n** is the number of experiments selected). A screen appears showing all runs from the selected experiments.
3. Select two or more runs by clicking the checkbox to the left of each run, or select all runs by checking the box at the top of the column.
4. Click **Compare**. The Comparing `<N>` Runs screen appears. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

## Comparison Page Layout

The **Comparing Runs** page presents information about the selected runs in tabular format. The **Parameters** and **Metrics** tables display the run parameters and metrics from all selected runs. The columns in these tables are identified by the **Run details** table immediately above. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

For simplicity, you can hide parameters and metrics that are identical in all selected runs by toggling the **Show diff only** button. This helps focus attention on the differences between runs. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

## Visualizations

You can also create visualizations of run results and tables of run information, run parameters, and metrics. For more details, see Compare MLflow runs and models using graphs and charts. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

## Comparing Runs Using System Tables

[MLflow](/concepts/mlflow.md) metadata for experiments and runs is also available in system tables, where you can leverage Databricks SQL and all the lakehouse tooling Databricks offers to analyze your experiment data. For more details, see the [MLflow System Tables](/concepts/mlflow-system-tables.md) reference. ^[view-training-results-with-mlflow-runs-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiment](/concepts/mlflow-experiment.md) — The organizational unit for [MLflow](/concepts/mlflow.md) runs
- [MLflow Run](/concepts/mlflow-run.md) — A single execution of model code
- [MLflow Tracking](/concepts/mlflow-tracking.md) — The API for logging parameters, metrics, and artifacts
- Compare MLflow runs and models using graphs and charts — Creating visualizations for run comparison
- [MLflow System Tables](/concepts/mlflow-system-tables.md) — System tables for analyzing experiment data with SQL

## Sources

- view-training-results-with-mlflow-runs-databricks-on-aws.md

# Citations

1. [view-training-results-with-mlflow-runs-databricks-on-aws.md](/references/view-training-results-with-mlflow-runs-databricks-on-aws-c299681f.md)
