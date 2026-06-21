---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e8233160b2f4a135e262a4b912b5122d4f28cff1939b7e8cdd4755c4077af2e8
  pageDirectory: concepts
  sources:
    - track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-experiment-configuration-for-air-runs
    - MECFAR
  citations:
    - file: track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md
title: MLflow Experiment Configuration for Air Runs
description: The YAML fields `experiment_name` (required) and `mlflow_run_name` (optional) control how runs are organized in MLflow experiments.
tags:
  - mlflow
  - yaml-config
  - experiment-tracking
timestamp: "2026-06-19T23:13:52.849Z"
---

# [MLflow Experiment](/concepts/mlflow-experiment.md) Configuration for Air Runs

Workloads submitted with `air run` are tracked as **both** a Databricks job run and an [MLflow Run](/concepts/mlflow-run.md). The job run tracks execution details — status, compute, retries, and driver output — while the [MLflow Run](/concepts/mlflow-run.md) tracks experiment data: parameters, metrics, system metrics, and artifacts. ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

One submission creates exactly one job run and one [MLflow Run](/concepts/mlflow-run.md). If a retry occurs (via `max_retries`), each retry creates a **new** [MLflow Run](/concepts/mlflow-run.md) in the same experiment. ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

## Configuration Fields

The workload YAML defines two fields that control [MLflow Experiment](/concepts/mlflow-experiment.md) behavior:

| Field | Required | Description |
|-------|----------|-------------|
| `experiment_name` | Yes | Creates an [MLflow Experiment](/concepts/mlflow-experiment.md) with this name if one does not exist, or appends a new run to an existing experiment. An experiment can hold many runs. |
| `mlflow_run_name` | No | Sets the run name. If omitted, the run name defaults to the value of `experiment_name`. |
| `max_retries` | No | Controls the number of automatic retries. Each retry attempt is a new [MLflow Run](/concepts/mlflow-run.md), so you can compare attempts across retries in the same experiment. |

^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

Example YAML:

```yaml
experiment_name: my-training
mlflow_run_name: baseline-lr3e5
compute:
  num_accelerators: 8
  accelerator_type: GPU_8xH100
command: torchrun --nproc_per_node=8 train.py
max_retries: 2
```

^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

## System Metrics

GPU, CPU, and memory system metrics are captured automatically for every Air run. No configuration is required. These metrics appear on the [MLflow Run](/concepts/mlflow-run.md)'s **System metrics** tab. ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

## Custom Metrics

The platform creates the [MLflow Run](/concepts/mlflow-run.md) and exposes its ID to the training process through the `MLFLOW_RUN_ID` environment variable. You can use the [MLflow Tracking API](/concepts/mlflow-tracking.md) to log your own parameters, metrics, and artifacts to that run.

On distributed (multi‑node) workloads, every node shares the same [MLflow Run](/concepts/mlflow-run.md). You should log from the rank‑0 process only to ensure each metric is recorded once:

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

## Navigating Between Jobs, [MLflow](/concepts/mlflow.md), and Previous Workloads

You can reach a run from three places:

- **Jobs run page** — Each run links to its [MLflow Run](/concepts/mlflow-run.md) and experiment.
- **MLflow Experiments page** — Lists all [MLflow](/concepts/mlflow.md) experiments.
- **Previous workloads** — The `air get run <job-run-id>` command prints clickable links to the job, experiment, and [MLflow Run](/concepts/mlflow-run.md). `air list runs` lists previous runs and allows filtering to find a specific run.

^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

## Logs and Artifacts

Use `air logs` to stream or download a run’s logs:

```bash
air logs <job-run-id>          # Stream logs from node 0
air logs <job-run-id> --node 2 # Logs from a specific node
air logs <job-run-id> --download-to ./logs/  # Download instead of streaming
```

Logs are also available as artifacts on the [MLflow Run](/concepts/mlflow-run.md). To persist model checkpoints, write them to a [Unity Catalog](/concepts/unity-catalog.md) volume. ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The command-line interface used to submit Air runs.
- [MLflow Experiment](/concepts/mlflow-experiment.md) — The organizational unit that groups related [MLflow](/concepts/mlflow.md) runs.
- [MLflow Run](/concepts/mlflow-run.md) — A single execution of experiment code.
- [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md) — The job-run view of the same workload.
- [System Metrics](/concepts/mlflow-system-metrics.md) — Automatically captured GPU/CPU/memory metrics.
- [MLflow Tracking API](/concepts/mlflow-tracking.md) — API for logging custom parameters, metrics, and artifacts.
- [Unity Catalog](/concepts/unity-catalog.md) — Recommended location for storing model checkpoints.

## Sources

- track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md

# Citations

1. [track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md](/references/track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws-f3444863.md)
