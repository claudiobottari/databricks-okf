---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dd83f08616b6374e05f942530ca4fa51009484d2c5633333ff377e700db50490
  pageDirectory: concepts
  sources:
    - track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-mlflow-logging-via-mlflow_run_id
    - CMLVM
  citations:
    - file: track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md
title: Custom MLflow Logging via MLFLOW_RUN_ID
description: The platform exposes the MLflow run ID via the `MLFLOW_RUN_ID` environment variable, allowing users to log custom parameters, metrics, and artifacts using the MLflow tracking API.
tags:
  - mlflow
  - logging
  - custom-metrics
timestamp: "2026-06-19T23:13:52.633Z"
---

# Custom [MLflow](/concepts/mlflow.md) Logging via `MLFLOW_RUN_ID`

**Custom [MLflow](/concepts/mlflow.md) Logging via `MLFLOW_RUN_ID`** refers to the practice of using the `MLFLOW_RUN_ID` environment variable — automatically set by the platform during [AI Runtime CLI](/concepts/ai-runtime-cli.md) workloads — to programmatically log custom parameters, metrics, and artifacts to an existing [MLflow](/concepts/mlflow.md) run from within a training process.

## Overview

When you submit a workload using `air run`, the platform creates an [MLflow Run](/concepts/mlflow-run.md) and exposes its unique ID to the training process through the `MLFLOW_RUN_ID` environment variable. You can then use the [MLflow Tracking API](/concepts/mlflow-tracking.md) to log additional data to that same run, supplementing the automatic capture of system metrics (GPU, CPU, memory). ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

## Usage

To log custom metrics from your training script, retrieve the run ID from the environment variable and use `mlflow.start_run()` with that ID. On distributed (multi-node) workloads, all nodes share the same `MLFLOW_RUN_ID`. To avoid duplicate log entries, log only from the rank-0 process:

```python
import os
import [[mlflow|MLflow]]

# Log from rank 0 only; all nodes share the same MLFLOW_RUN_ID.
if os.environ.get("RANK", "0") == "0":
    with [[mlflow|MLflow]].start_run(run_id=os.environ["MLFLOW_RUN_ID"]):
        [[mlflow|MLflow]].log_param("learning_rate", 3e-4)
        for step, loss in enumerate(training_losses):
            [[mlflow|MLflow]].log_metric("train_loss", loss, step=step)
```

^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

## Key Details

- **Environment variable**: `MLFLOW_RUN_ID` is set automatically by the platform for every `air run` submission. ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]
- **Single run per submission**: One submission creates one job run and one [MLflow Run](/concepts/mlflow-run.md). A retry (governed by `max_retries` in the workload YAML) creates a new [MLflow Run](/concepts/mlflow-run.md). ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]
- **Distributed consistency**: On multi-node workloads, the same `MLFLOW_RUN_ID` is shared across all nodes. Log only from rank 0 to ensure each metric is recorded exactly once. ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]
- **What you can log**: Custom parameters (via `log_param`), metrics (via `log_metric`), and artifacts. System metrics (GPU, CPU, memory) are captured automatically and do not require custom logging. ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

## Comparison with Automatic Logging

| Aspect | Automatic System Metrics | Custom Logging via `MLFLOW_RUN_ID` |
|---|---|---|
| Coverage | GPU, CPU, memory metrics captured for every run | User-defined parameters, metrics, and artifacts |
| Configuration | None required | Uses `mlflow.start_run(run_id=...)` in code |
| Granularity | Fixed set of metrics | Any user-defined value or step-wise metric |
| Distributed handling | Handled automatically | Must restrict to rank 0 to avoid duplicates |

^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The CLI tool (`air`) used to submit workloads.
- [MLflow Tracking API](/concepts/mlflow-tracking.md) — The API for logging parameters, metrics, and artifacts.
- Track runs with MLflow and the Jobs run page — Overview of the experiment tracking integration.
- [Experiment Tracking and Observability](/concepts/ai-runtime-experiment-tracking-and-observability.md) — Patterns for checkpointing and managing artifacts.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Distributed training technique commonly used alongside custom [MLflow](/concepts/mlflow.md) logging.

## Sources

- track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md

# Citations

1. [track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md](/references/track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws-f3444863.md)
