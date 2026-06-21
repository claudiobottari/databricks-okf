---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6c4e210c1bd4ab5536831c05ed69099e18d6cdb5a6d878adc24051e4e56c4aa3
  pageDirectory: concepts
  sources:
    - build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - mlflow-system-metrics
    - MSM
    - System Metrics
    - System metrics
    - system metrics
  citations:
    - file: build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
title: MLflow System Metrics
description: System-level metrics (CPU, memory, GPU utilization) recorded by MLflow during runs and exposed via system tables for workspace-wide monitoring and analysis.
tags:
  - mlflow
  - metrics
  - monitoring
  - system
timestamp: "2026-06-19T14:10:23.913Z"
---

# MLflow System Metrics

**MLflow System Metrics** are system-level resource utilization metrics automatically recorded by MLflow during run execution. These metrics capture real-time hardware usage—including CPU, memory, and GPU utilization—and are stored in system tables, enabling workspace-wide monitoring and optimization of ML workloads.^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Overview

MLflow logs system metrics alongside user-defined training metrics during each run. The data can be queried through [MLflow System Tables](/concepts/mlflow-system-tables.md), allowing users to analyze resource consumption across experiments without iterating through individual runs via the UI or REST API.^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Available Metrics

The documented system metrics include:

- CPU utilization
- Memory utilization
- GPU utilization

These metrics are recorded automatically by MLflow and are accessible in system tables under the metric name that corresponds to each resource.^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Monitoring with Dashboards

Using Databricks Dashboards built on top of system tables, you can create visualizations that summarize system metrics across all experiments within a given time window. For example, a dashboard can display average GPU utilization per experiment and highlight runs where GPU usage is below 10%, indicating potential resource waste.^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

To get started, download a pre-built dashboard JSON file and import it into your workspace. The dashboard's fourth tab accepts a metric name and time range, then returns summary statistics (average, min, max) for that metric across all experiments.^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) – The core logging component that records system metrics
- [MLflow System Tables](/concepts/mlflow-system-tables.md) – SQL-queryable tables storing MLflow metadata
- Databricks Dashboards – Visualization platform for analyzing system and user metrics
- [MLflow Experiments](/concepts/mlflow-experiment.md) – Organizational units for grouping related runs
- [GPU Utilization Monitoring](/concepts/gpu-utilization-monitoring-dashboard.md) – Practical use case for system metrics

## Sources

- build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md

# Citations

1. [build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md](/references/build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws-bdd77682.md)
