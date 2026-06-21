---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b574bdb3d04010b0e2f9e5a166add6199a1c4100946e8563218c425e535b5a2e
  pageDirectory: concepts
  sources:
    - build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-dashboarding-on-databricks
    - MDOD
    - Dashboarding on Databricks
  citations:
    - file: build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
title: MLflow Dashboarding on Databricks
description: The practice of building Dashboards in Databricks using MLflow metadata from system tables to analyze experiments and runs across an entire workspace.
tags:
  - mlflow
  - databricks
  - dashboards
  - visualization
timestamp: "2026-06-19T14:10:12.487Z"
---

# MLflow Dashboarding on Databricks

**MLflow Dashboarding on Databricks** refers to the practice of building interactive dashboards using MLflow metadata stored in [system tables](/concepts/mlflow-system-tables.md). These dashboards provide workspace-wide visibility into MLflow experiments and runs, enabling analysis that would be tedious or impractical using the MLflow UI or REST APIs alone. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Dashboard for Single Run Details

A sample dashboard is available (as a JSON file) that replicates the run details page from the MLflow UI. For a given experiment ID, run ID, and metric name, the dashboard displays run details, tags, parameters, and a metric graph. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

To get started, download the [example dashboard JSON](https://docs.databricks.com/aws/en/assets/files/mlflow_system_tables_dashboard.lvdash-c47a9bd31724e4ee62a78acffc600d0b.json) and [import it](https://docs.databricks.com/aws/en/dashboards/automate/import-export) into your workspace. The experiment ID and run ID can be obtained from the run details page URL: `https://<workspace>.databricks.com/ml/experiments/<experiment_id>/runs/<run_id>`. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

Once imported, the dashboard provides input boxes at the top to filter for the relevant run and experiment within the workspace. The queries and plots can be modified to suit specific needs. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Dashboard to Monitor Average GPU Utilization Across Experiments

A separate tab in the same dashboard accepts a metric name and returns summary statistics across all experiments that logged that metric within a given time window. This is particularly useful for analyzing [system metrics](/concepts/mlflow-system-metrics.md) recorded by MLflow, such as CPU, memory, or GPU utilization. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

In the example, experiments with an average GPU utilization below 10% are surfaced, allowing users to identify and investigate inefficient GPU usage across the workspace. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Related Concepts

- [MLflow](/concepts/mlflow.md) — The experiment tracking and model management framework.
- System tables — Databricks tables that store workspace-level metadata, including MLflow tracking data.
- Dashboards — Interactive visualizations built from Databricks SQL queries.
- [MLflow experiments](/concepts/mlflow-experiment.md) — The organizational unit for MLflow runs.
- [MLflow runs](/concepts/mlflow-run.md) — Individual executions of a training or evaluation script.
- Metrics — Numerical values logged during a run (e.g., loss, accuracy, GPU utilization).
- [System metrics](/concepts/mlflow-system-metrics.md) — Performance metrics automatically collected by MLflow (CPU, memory, GPU).

## Sources

- build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md

# Citations

1. [build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md](/references/build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws-bdd77682.md)
