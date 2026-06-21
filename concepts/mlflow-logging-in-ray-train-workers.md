---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c789067d4dbb67db900f14a01b1f66f8b0e9f15e8a482c0f64b18522df898a77
  pageDirectory: concepts
  sources:
    - distributed-training-with-ray-train-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-logging-in-ray-train-workers
    - MLIRTW
  citations:
    - file: distributed-training-with-ray-train-databricks-on-aws.md
title: MLflow Logging in Ray Train Workers
description: Pattern for conditionally starting MLflow runs inside Ray Train workers using the MLFLOW_RUN_ID environment variable injected by the Databricks AI Runtime, enabling per-worker metric logging without explicit credentials.
tags:
  - mlflow
  - experiment-tracking
  - databricks
timestamp: "2026-06-19T18:37:56.312Z"
---

# MLflow Logging in Ray Train Workers

**MLflow Logging in Ray Train Workers** refers to the mechanism by which metrics, parameters, and run metadata are tracked using [MLflow](/concepts/mlflow.md) from within Ray Train worker processes during distributed training jobs. This integration enables centralized experiment tracking even when training is distributed across multiple GPUs or nodes.

## Overview

When running [Ray Train](/concepts/ray-train-resource-allocation.md) workloads on [Databricks AI Runtime](/concepts/databricks-ai-runtime.md), the environment automatically injects the `MLFLOW_RUN_ID` environment variable and configures the Databricks tracking URI on each compute node. This eliminates the need to manually set `DATABRICKS_HOST` or `DATABRICKS_TOKEN` for MLflow logging within the training script. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Conditional MLflow Usage

In distributed training scenarios, only a single worker — typically rank 0 — should perform MLflow logging to avoid duplicate or conflicting log entries. The recommended pattern is to check both the worker rank and the presence of `MLFLOW_RUN_ID` before starting an [MLflow Run](/concepts/mlflow-run.md). ^[distributed-training-with-ray-train-databricks-on-aws.md]

```python
use_mlflow = rank == 0 and bool(os.environ.get("MLFLOW_RUN_ID"))
```

This conditional check serves two purposes:
1. It restricts logging to the rank 0 worker only, preventing duplicate metric logging across all workers.
2. It gates on `MLFLOW_RUN_ID` so the script runs cleanly off-platform (for example, locally) where the variable is unset. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Logging Pattern

Within a Ray Train worker function, MLflow logging follows this standard flow:

1. **Start a run** using the injected run ID: `mlflow.start_run(run_id=os.environ.get("MLFLOW_RUN_ID"))`
2. **Log parameters** with `mlflow.log_params()` — common entries include model name, learning rate, and batch size.
3. **Log metrics** during the training loop with `mlflow.log_metric()` — for example, logging `train_loss` at each step.
4. **End the run** with `mlflow.end_run()` after training completes. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Where Results Land

Metrics reported with `ray.train.report()` and also logged with MLflow both appear in the MLflow experiment named in the workload configuration's `experiment_name` field. These results are viewable in the workspace MLflow UI. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Related Concepts

- [Ray Train](/concepts/ray-train-resource-allocation.md) — The distributed training framework that launches worker processes across GPUs.
- [MLflow Tracking](/concepts/mlflow-tracking.md) — The API for logging parameters, metrics, and artifacts during ML experiments.
- [Databricks AI Runtime](/concepts/databricks-ai-runtime.md) — The runtime environment that injects MLflow configuration into compute nodes.
- [TorchTrainer](/concepts/ray-train-torchtrainer.md) — Ray Train's trainer class for PyTorch models, commonly used with MLflow logging.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — The parallelism strategy typically combined with MLflow tracking.

## Sources

- distributed-training-with-ray-train-databricks-on-aws.md

# Citations

1. [distributed-training-with-ray-train-databricks-on-aws.md](/references/distributed-training-with-ray-train-databricks-on-aws-05072d36.md)
