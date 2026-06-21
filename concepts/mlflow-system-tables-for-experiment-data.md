---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b51d475a8905640849036fafe48641563034544a8a2070afb7a8cc39077ee064
  pageDirectory: concepts
  sources:
    - compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-system-tables-for-experiment-data
    - MSTFED
  citations:
    - file: compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md
title: MLflow System Tables for Experiment Data
description: MLflow metadata stored in Databricks system tables, enabling SQL-based querying and lakehouse visualization of experiment data.
tags:
  - mlflow
  - databricks
  - sql
  - data-analysis
timestamp: "2026-06-18T14:40:31.467Z"
---

# MLflow System Tables for Experiment Data

**MLflow System Tables for Experiment Data** provide an alternative way to access [MLflow experiments|experiment](/concepts/mlflow-experiment.md) and [MLflow runs|run](/concepts/mlflow-run.md) metadata by querying system tables with Databricks SQL. This approach lets you leverage the full power of the lakehouse ecosystem — including SQL analytics, dashboards, and collaborative notebooks — to analyze and visualize your MLflow experiment data outside of the native MLflow UI. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Overview

While the MLflow UI offers built-in chart views for comparing runs within an experiment, the same metadata is also stored in system tables. By querying these tables, you can build custom reports, join experiment data with other lakehouse tables, and use all the tooling Databricks provides for data analysis and visualization. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

This capability is especially useful when you need to:

- Aggregate metrics across many experiments.
- Create periodic dashboards for model performance tracking.
- Perform ad-hoc SQL analysis on experiment metadata.
- Combine run data with other operational or business data.

## How to Access

Query the system tables using Databricks SQL or any SQL-compatible tool connected to the lakehouse. For the complete schema and table list, refer to the official **MLflow system tables reference** documentation. ^[compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md]

## Related Concepts

- Databricks SQL – The query engine used to access system tables.
- System tables – The broader Databricks system table infrastructure.
- Lakehouse – The architecture that unifies data and AI workloads.
- [MLflow experiments](/concepts/mlflow-experiment.md) – The organizational unit containing runs.
- [MLflow runs](/concepts/mlflow-run.md) – Individual training or evaluation executions.
- Compare MLflow runs using graphs and charts – The native MLflow UI approach for visualizing experiment data.

## Sources

- compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md

# Citations

1. [compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws.md](/references/compare-mlflow-runs-and-models-using-graphs-and-charts-databricks-on-aws-ab27c56a.md)
