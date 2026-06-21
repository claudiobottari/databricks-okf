---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bf9811c25f055a2358e999f34f2142ffd382eaa5fd9250bb2f13edc3e50ef1ea
  pageDirectory: concepts
  sources:
    - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-system-tables-for-experiment-analysis
    - MSTFEA
  citations:
    - file: compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
title: MLflow System Tables for Experiment Analysis
description: The availability of MLflow experiment and run metadata in Databricks system tables, enabling use of Databricks SQL and lakehouse tooling for custom visualization and analysis.
tags:
  - mlflow
  - databricks
  - sql
  - system-tables
timestamp: "2026-06-18T11:04:14.849Z"
---

# MLflow System Tables for Experiment Analysis

**MLflow System Tables for Experiment Analysis** refers to the system tables in Databricks that expose MLflow experiment and run metadata, enabling you to analyze experiment data using Databricks SQL and all the lakehouse tooling Databricks offers. These tables make MLflow metadata available for querying, visualization, and integration with broader data governance workflows. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Overview

MLflow metadata for experiments and runs is stored in system tables, where you can leverage SQL-based querying and visualization tools to analyze your experiment data at scale. This approach complements the MLflow UI's chart view page, which provides interactive visualizations for comparing runs within an experiment. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Available Data

The MLflow system tables contain metadata about:

- **Experiments** — Metadata about experiment configurations, creation times, and lifecycle states.
- **Runs** — Detailed information about individual runs, including parameters, metrics, tags, and artifacts.
- **Models** — Information about logged models and their versions.

For the complete schema and field descriptions, see the MLflow system tables reference in the Databricks documentation. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Querying Experiment Data

You can query MLflow system tables using standard SQL, enabling you to:

- Analyze run performance across multiple experiments.
- Track parameter configurations and their impact on metrics.
- Identify best-performing runs for model selection.
- Create custom reports and dashboards.

Example queries can combine data from multiple experiments, apply filters, and aggregate results — capabilities that extend beyond the per-experiment view in the MLflow UI. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Visualization and Analysis

Because the data is in system tables, you can use any Databricks SQL visualization tool to create charts, graphs, and dashboards for experiment analysis. This includes:

- Building custom visualizations beyond the default parallel coordinates, scatter plots, and line charts available in the MLflow UI.
- Creating recurring reports that track experiment trends over time.
- Combining experiment metadata with other data sources in the lakehouse for holistic analysis.

For information about the built-in chart view page in the MLflow UI, see Compare MLflow runs and models using graphs and charts. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Integration with Data Governance

MLflow system tables can be used in conjunction with other governance features, such as:

- [System Tags](/concepts/system-tags.md) — Predefined tags that can be applied to experiments and runs for access control.
- [Audit Log System Table](/concepts/audit-log-system-table-requirements.md) — For auditing changes to experiments and model registries.
- ABAC policies — For implementing attribute-based access control on experiment data exposed through system tables.

## Related Concepts

- [MLflow](/concepts/mlflow.md) — The open-source machine learning lifecycle platform
- [MLflow experiments](/concepts/mlflow-experiment.md) — Containers for organizing MLflow runs
- [MLflow runs](/concepts/mlflow-run.md) — Individual executions of machine learning code
- Databricks SQL — The SQL query engine for the Databricks Lakehouse Platform
- System tables — Databricks-managed tables that store account-level metadata
- Compare MLflow runs and models using graphs and charts — The built-in visualization tools in the MLflow UI
- [MLflow Logged Models](/concepts/mlflow-loggedmodel.md) — Models tracked and compared using MLflow's model registry

## Sources

- compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md

# Citations

1. [compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md](/references/compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws-ab27c56a.md)
