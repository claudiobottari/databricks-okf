---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 789f7e04e2632a1ecb40fe6d0bddd88634b31b6d61bec780f563b26b5f148d88
  pageDirectory: concepts
  sources:
    - track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automatic-system-metrics-capture
    - ASMC
  citations:
    - file: track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md
title: Automatic System Metrics Capture
description: GPU, CPU, and memory system metrics are captured automatically for every run without configuration, viewable in the MLflow run's System metrics tab.
tags:
  - mlflow
  - monitoring
  - system-metrics
timestamp: "2026-06-19T23:13:52.596Z"
---

# Automatic System Metrics Capture

**Automatic System Metrics Capture** is a built-in feature of the [AI Runtime CLI](/concepts/ai-runtime-cli.md) (Beta) that records GPU, CPU, and memory utilization for every workload submitted with `air run`. These metrics are collected without any user configuration and are immediately available for review.

## Overview

Each workload submitted with `air run` becomes both a Databricks Job Run and an [MLflow Run](/concepts/mlflow-run.md). As part of the [MLflow Run](/concepts/mlflow-run.md), the platform automatically captures system-level metrics for the duration of the job. ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

The captured metrics include:
- GPU utilization and memory
- CPU utilization
- Memory (RAM) usage

No configuration or code changes are required to enable this collection. ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

## Viewing System Metrics

System metrics are displayed on the **System metrics** tab of the corresponding [MLflow Run](/concepts/mlflow-run.md). Users can navigate to this tab from the [MLflow Run](/concepts/mlflow-run.md) page to view time-series charts of GPU, CPU, and memory usage. ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

Access to the [MLflow Run](/concepts/mlflow-run.md) is available through:
- The **Jobs** run page, which links to the [MLflow Run](/concepts/mlflow-run.md) and experiment.
- The **Experiments** page in the [MLflow](/concepts/mlflow.md) UI.
- The `air get run <job-run-id>` command, which prints clickable links to the job run, experiment, and [MLflow Run](/concepts/mlflow-run.md). ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – The command-line interface used to submit workloads.
- [MLflow Runs](/concepts/mlflow-run.md) – The tracking entity that stores parameters, metrics, and artifacts.
- Job Runs – The job execution record in the Databricks workspace.
- [System Metrics](/concepts/mlflow-system-metrics.md) – The broad concept of infrastructure-level monitoring data.
- [Experiment Tracking](/concepts/mlflow-experiment-tracking.md) – The practice of logging and comparing runs in [MLflow](/concepts/mlflow.md) experiments.
- Custom Metrics – Manually logged metrics via the [MLflow Tracking](/concepts/mlflow-tracking.md) API.

## Sources

- track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md

# Citations

1. [track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md](/references/track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws-f3444863.md)
