---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ab22554b9b10994cd6f1c6e9f908c5387aa0745362d697a1bcd78d1c5529ce25
  pageDirectory: concepts
  sources:
    - build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - single-run-details-dashboard
    - SRDD
  citations:
    - file: build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
title: Single Run Details Dashboard
description: A pre-built example dashboard that replicates the MLflow run details page using system table queries, filterable by experiment ID, run ID, and metric name
tags:
  - mlflow
  - dashboards
  - databricks
  - visualization
timestamp: "2026-06-19T17:41:28.737Z"
---

# Single Run Details Dashboard

The **Single Run Details Dashboard** is a reusable dashboards visualization that replicates the information shown on an [MLflow Run](/concepts/mlflow-run.md) details page, built using MLflow metadata stored in [system tables](/concepts/mlflow-system-tables.md). It allows users to analyze individual MLflow runs from across the entire workspace without having to repeatedly open the MLflow UI or call REST APIs. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Overview

The dashboard is provided as a downloadable JSON file and can be imported into a Databricks workspace. It displays run-level details, tags, parameters, and a metric graph for a given combination of experiment ID, run ID, and metric name. The experiment ID and run ID can be obtained from the [MLflow Run](/concepts/mlflow-run.md) details page – both in the UI and directly from the URL, which follows the pattern `https://<workspace>.databricks.com/ml/experiments/<experiment_id>/runs/<run_id>`. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Features

- **Run-level details**: Shows metadata of a specific run.
- **Tags and parameters**: Lists all tags and parameters logged for that run.
- **Metric graph**: Plots the trajectory of a selected metric over time for the run.
- **Flexible filtering**: Users can input an experiment ID, run ID, and metric name via the dashboard's input boxes to filter data for any run within the workspace. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Usage

1. Download the example dashboard JSON file from the [Databricks documentation](https://docs.databricks.com/aws/en/assets/files/mlflow_system_tables_dashboard.lvdash-c47a9bd31724e4ee62a78acffc600d0b.json) or from the referenced [GitHub Gist](https://gist.github.com/ian-ack-db/684a83040a557f92f1668449c0df75df).
2. Import the JSON file into your workspace using the [dashboard import/export functionality](https://docs.databricks.com/aws/en/dashboards/automate/import-export#import).
3. Use the input boxes at the top of the dashboard to select an experiment, run, and metric name.
4. Customize the underlying queries and visualizations as needed. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Related Dashboard Tab

The same dashboard template also includes a fourth tab that accepts a metric name and returns summary statistics across all experiments that log that metric within a given time window. This can be used to monitor system metrics recorded by MLflow (for example, CPU, memory, or GPU utilization) and identify inefficient resource usage across the workspace. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md)
- System Tables
- Dashboards
- Metric Graph
- [GPU Utilization Dashboard](/concepts/gpu-utilization-monitoring-dashboard.md)

## Sources

- build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md

# Citations

1. [build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md](/references/build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws-bdd77682.md)
