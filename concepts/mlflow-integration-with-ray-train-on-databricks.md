---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b61ad869824d4680269ac3849d1b5f58f7946f0a144140f369a2eb811c8882c7
  pageDirectory: concepts
  sources:
    - distributed-training-with-ray-train-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-integration-with-ray-train-on-databricks
    - MIWRTOD
  citations:
    - file: distributed-training-with-ray-train-databricks-on-aws.md
title: MLflow integration with Ray Train on Databricks
description: Automatic MLflow logging setup where AI Runtime injects MLFLOW_RUN_ID and configures the Databricks tracking URI, enabling metric and parameter logging without explicit credentials.
tags:
  - mlflow
  - databricks
  - ray
  - experiment-tracking
timestamp: "2026-06-18T12:08:59.999Z"
---

# MLflow Integration with Ray Train on Databricks

**MLflow Integration with Ray Train on Databricks** refers to the automatic logging of training metrics and parameters when running distributed data-parallel fine-tuning workloads using [Ray Train](/concepts/ray-train-resource-allocation.md) on Databricks. The AI Runtime environment configures MLflow tracking automatically, enabling seamless experiment tracking without manual setup of tracking URIs or authentication credentials.

## Overview

When running distributed training with Ray Train on Databricks, the AI Runtime injects the `MLFLOW_RUN_ID` environment variable and configures the Databricks tracking URI on each compute node. This means that code running inside Ray Train workers can log metrics, parameters, and artifacts to [MLflow experiments](/concepts/mlflow-experiment.md) without explicitly setting `DATABRICKS_HOST` or authentication tokens.^[distributed-training-with-ray-train-databricks-on-aws.md]

The integration works with Ray Train's `TorchTrainer` across single-node or multi-node GPU clusters. Each worker reports metrics via `ray.train.report()`, and the driver process (rank 0) handles MLflow logging.^[distributed-training-with-ray-train-databricks-on-aws.md]

## How It Works

### Automatic MLflow Configuration

The AI Runtime automatically configures MLflow tracking on each node in the Ray cluster. In a typical training script, you can check for the presence of `MLFLOW_RUN_ID` to conditionally start an [MLflow Run](/concepts/mlflow-run.md) only on the rank-0 worker:^[distributed-training-with-ray-train-databricks-on-aws.md]

```python
rank = ray.train.get_context().get_world_rank()
use_mlflow = rank == 0 and bool(os.environ.get("MLFLOW_RUN_ID"))
if use_mlflow:
    mlflow.start_run(run_id=os.environ.get("MLFLOW_RUN_ID"))
    mlflow.log_params({
        "model": MODEL_NAME,
        "lr": config["lr"],
        "batch_size": config["batch_size"]
    })
```

### Logging Metrics During Training

During the training loop, each iteration reports metrics to both Ray Train (for aggregation) and MLflow (for experiment tracking). The rank-0 worker logs metrics per step:^[distributed-training-with-ray-train-databricks-on-aws.md]

```python
step += 1
ray.train.report({"loss": out.loss.item(), "step": step})
if use_mlflow:
    mlflow.log_metric("train_loss", out.loss.item(), step=step)
if step >= config["max_steps"]:
    break
```

## Workload Configuration

To enable MLflow integration with Ray Train, set the `experiment_name` in your workload YAML file. The AI Runtime creates or reuses the specified experiment and assigns a run ID.^[distributed-training-with-ray-train-databricks-on-aws.md]

```yaml
experiment_name: air-ray-train-distributed
```

Metrics reported with `ray.train.report` and logged with MLflow appear in the MLflow experiment named in `experiment_name`, viewable in the workspace MLflow UI.^[distributed-training-with-ray-train-databricks-on-aws.md]

## Best Practices

### Conditional Logging by Rank

Only log to MLflow from the rank-0 worker to avoid duplicate entries and race conditions. Use `ray.train.get_context().get_world_rank()` to identify the rank.^[distributed-training-with-ray-train-databricks-on-aws.md]

### Graceful Off-Platform Fallback

Check for `MLFLOW_RUN_ID` before using it, so the same training script can run outside Databricks (e.g., locally) without errors:^[distributed-training-with-ray-train-databricks-on-aws.md]

```python
use_mlflow = rank == 0 and bool(os.environ.get("MLFLOW_RUN_ID"))
```

### Log Parameters Before Training

Use `mlflow.log_params()` to record hyperparameters and model configuration at the start of training for complete experiment reproducibility.^[distributed-training-with-ray-train-databricks-on-aws.md]

## Viewing Results

After training completes, inspect the run using the Databricks CLI:^[distributed-training-with-ray-train-databricks-on-aws.md]

```bash
air get run <run-id>
air logs <run-id>
```

All logged metrics and parameters are available in the MLflow experiment UI in the Databricks workspace.

## Related Concepts

- [Ray Train](/concepts/ray-train-resource-allocation.md) — Distributed training framework used for data-parallel fine-tuning
- [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md) — System for logging and comparing training runs
- [Distributed Data-Parallel Training](/concepts/distributed-data-parallel-ddp.md) — Training approach where model weights are replicated across GPUs
- [TorchTrainer](/concepts/ray-train-torchtrainer.md) — Ray Train's PyTorch training interface
- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — Command-line tool for submitting training workloads

## Sources

- distributed-training-with-ray-train-databricks-on-aws.md

# Citations

1. [distributed-training-with-ray-train-databricks-on-aws.md](/references/distributed-training-with-ray-train-databricks-on-aws-05072d36.md)
