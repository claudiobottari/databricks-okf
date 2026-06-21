---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ebdfd60bd55fc2ef54ea416d51399b3cf0124b8962d379439782720bde11089e
  pageDirectory: concepts
  sources:
    - distributed-training-with-ray-train-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-integration-in-ray-train-on-databricks
    - MIIRTOD
  citations:
    - file: distributed-training-with-ray-train-databricks-on-aws.md
title: MLflow Integration in Ray Train on Databricks
description: Automatic MLflow logging integration where Databricks injects MLFLOW_RUN_ID and configures the tracking URI so distributed Ray Train jobs can log metrics without explicit credentials.
tags:
  - mlflow
  - databricks
  - ray
  - logging
timestamp: "2026-06-18T15:34:41.729Z"
---

# MLflow Integration in Ray Train on Databricks

**MLflow Integration in Ray Train on Databricks** refers to the automatic and seamless logging of training metrics, parameters, and artifacts when running [Ray Train](/concepts/ray-train-resource-allocation.md) workloads on the Databricks platform. The integration leverages the [AI Runtime CLI](/concepts/ai-runtime-cli.md) (`air`) to inject environment variables and configure the MLflow tracking URI, enabling distributed training scripts to log to the correct MLflow experiment without manual setup of credentials or host information. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Overview

When submitting a Ray Train workload via the `air` CLI (e.g., `air run -f train.yaml`), the AI Runtime automatically sets the `MLFLOW_RUN_ID` environment variable on the compute node and configures the Databricks tracking URI. This allows any MLflow logging calls within the training script to connect to the workspace's MLflow tracking server without requiring `DATABRICKS_HOST` or `DATABRICKS_TOKEN` to be explicitly provided. ^[distributed-training-with-ray-train-databricks-on-aws.md]

Metrics reported through `ray.train.report()` are also automatically logged to MLflow and appear in the experiment specified in the workload YAML's `experiment_name` field. The results are viewable in the workspace MLflow UI under that experiment. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Key Components

### Automatic Experiment Assignment

The workload YAML includes an `experiment_name` field (e.g., `air-ray-train-distributed`) that determines which MLflow experiment receives the run. All metrics and parameters logged during the run appear under this experiment. ^[distributed-training-with-ray-train-databricks-on-aws.md]

### Injected Environment Variables

The AI Runtime injects `MLFLOW_RUN_ID` on the node. This run ID corresponds to the run created by the AI Runtime itself. Training scripts can use this existing run to log additional data or, if preferred, start a nested run. ^[distributed-training-with-ray-train-databricks-on-aws.md]

### Logging Parameters and Metrics

Inside the per-worker training function (`train_func`), developers can call standard MLflow APIs:

- `mlflow.start_run(run_id=os.environ.get("MLFLOW_RUN_ID"))` — attaches to the existing top-level run.
- `mlflow.log_params(...)` — logs model name, learning rate, batch size, etc.
- `mlflow.log_metric("train_loss", value, step=step)` — logs per-step metrics.
- `mlflow.end_run()` — ends the nested run.

The same metrics are also reported via `ray.train.report()` to the Ray framework, ensuring consistency between Ray's built-in metric aggregation and MLflow’s logging. ^[distributed-training-with-ray-train-databricks-on-aws.md]

### Guarding MLflow Calls to Rank 0

In a distributed Ray Train setup, only the rank-0 worker (the first GPU) should perform MLflow logging to avoid duplicate or conflicting writes. The example script gates MLflow calls on two conditions: `rank == 0` and `bool(os.environ.get("MLFLOW_RUN_ID"))`. This ensures logging only occurs on the main worker and only when the run context is properly set (i.e., when running on Databricks). Off-platform runs (e.g., local testing) are unaffected. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Example Workflow

1. **Define a workload YAML** (`train.yaml`) that sets `experiment_name`, `environment` dependencies (including `ray[default,train]` and MLflow), and a `command` that starts a Ray head and runs the training driver.
2. **Write a Ray Train driver** (`train_ray.py`) that uses `ray.train.torch.TorchTrainer`. Inside `train_func`, check for `MLFLOW_RUN_ID` and call MLflow APIs as shown above.
3. **Submit the run** with `air run -f train.yaml --watch`.
4. **Inspect results** in the MLflow experiment UI under the specified `experiment_name`. ^[distributed-training-with-ray-train-databricks-on-aws.md]

## Benefits

- **Zero configuration**: No need to set tracking URI or authentication tokens manually.
- **Automatic experiment alignment**: The experiment name in the YAML directly maps to the MLflow experiment.
- **Combined logging**: Metrics are reported both to Ray Train (for aggregation) and MLflow (for visualization and comparison).
- **Portable code**: The guard on `MLFLOW_RUN_ID` allows the same script to run locally or on Databricks without modification.

## Best Practices

- Always gate MLflow logging on `rank == 0` to avoid duplicated logs from multiple workers. ^[distributed-training-with-ray-train-databricks-on-aws.md]
- Use `mlflow.start_run()` with the injected `MLFLOW_RUN_ID` to attach to the AI Runtime’s run, rather than creating a separate run. ^[distributed-training-with-ray-train-databricks-on-aws.md]
- Log all relevant hyperparameters via `mlflow.log_params` early in training for better run tracking.
- Consider using `ray.train.report` for real-time metric aggregation across workers; MLflow logging then provides a persistent record.

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – The tool for submitting and managing ML workloads on Databricks.
- [Ray Train](/concepts/ray-train-resource-allocation.md) – Distributed training framework used with TorchTrainer.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – The organizational unit for MLflow runs.
- [Distributed Training on Databricks](/concepts/distributed-training-on-databricks.md) – Broader context for multi-GPU and multi-node training.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – Core MLflow component for logging parameters, metrics, and artifacts.

## Sources

- distributed-training-with-ray-train-databricks-on-aws.md

# Citations

1. [distributed-training-with-ray-train-databricks-on-aws.md](/references/distributed-training-with-ray-train-databricks-on-aws-05072d36.md)
