---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8340905d411b3bcfac184808a7f9e067e98540a1045fed03f39206fdbc772908
  pageDirectory: concepts
  sources:
    - track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dual-run-model-job-run-mlflow-run
    - DRM(R+MR
  citations:
    - file: track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md
title: Dual Run Model (Job Run + MLflow Run)
description: Each `air run` submission creates both a Databricks job run (execution tracking) and an MLflow run (experiment tracking), with retries creating new MLflow runs.
tags:
  - mlflow
  - jobs
  - run-management
timestamp: "2026-06-19T23:13:51.902Z"
---

# Dual Run Model (Job Run + [MLflow Run](/concepts/mlflow-run.md))

The **Dual Run Model** refers to the relationship between a single workload submission via the [AI Runtime CLI](/concepts/ai-runtime-cli.md) (`air run`) and the two distinct tracking entities it creates: a **Databricks job run** and an **MLflow run**. One submission always creates one job run and one [MLflow Run](/concepts/mlflow-run.md); a retry creates a new [MLflow Run](/concepts/mlflow-run.md).^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

## How the Two Runs Are Related

The job run is visible on the workspace **Jobs & Pipelines** page and tracks execution details such as status, compute, retries, and driver output. The [MLflow Run](/concepts/mlflow-run.md) is visible in the [MLflow Experiments](/concepts/mlflow-experiment.md) page and tracks the experiment’s parameters, metrics, system metrics, and artifacts. Together, they provide a complete view of both the infrastructure execution and the experimental results of a training or inference workload.^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

## Controlled by Workload YAML Fields

Two fields in the [Workload YAML Configuration](/concepts/workload-yaml-configuration.md) control how the run appears in [MLflow](/concepts/mlflow.md):

- `experiment_name` (Required): Specifies the name of the [MLflow Experiment](/concepts/mlflow-experiment.md) to use. If the experiment does not exist, it is created automatically. Subsequent runs with the same name append new runs to that experiment.
- `mlflow_run_name` (Optional): Sets the name of the individual [MLflow Run](/concepts/mlflow-run.md). If omitted, the run name defaults to the experiment name.
- `max_retries` (Optional): Defines the number of retry attempts. Each retry creates a new [MLflow Run](/concepts/mlflow-run.md) within the same experiment, enabling comparison of attempts. The original submission and all its retries share one job run.^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

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

## Navigation Between Jobs, [MLflow](/concepts/mlflow.md), and Previous Workloads

You can reach a run from three starting points:

- **Jobs run page**: Lists your job runs; each run provides a direct link to its corresponding [MLflow Run](/concepts/mlflow-run.md) and experiment.
- **MLflow Experiments page**: Lists your experiments and their runs.
- **Previous workloads**: The `air get run <job-run-id>` command prints clickable links to the job run, experiment, and [MLflow Run](/concepts/mlflow-run.md). The `air list runs` command lists previous runs and supports filtering.^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

Bash commands:

```bash
air get run <job-run-id>           # Links to the job, experiment, and [[mlflow-run|MLflow Run]]
air list runs                       # List previous runs; filter to find a specific run
```

## System Metrics

GPU, CPU, and memory system metrics are captured automatically for every run — no configuration is required. These metrics appear on the [MLflow](/concepts/mlflow.md) run’s **System metrics** tab.^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

## Log Custom Metrics

The platform sets the `MLFLOW_RUN_ID` environment variable inside the running process, exposing the active [MLflow Run](/concepts/mlflow-run.md) ID. Use the [MLflow Tracking API](/concepts/mlflow-tracking.md) to log custom parameters, metrics, and artifacts to that run. On distributed (multi-node) workloads, all nodes share the same [MLflow Run](/concepts/mlflow-run.md) ID; metrics should be logged only from the rank‑0 process to avoid duplicate recording.^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

Example Python code:

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

## Logs and Artifacts

Use `air logs` to stream or download a run’s logs. You can specify a particular node or download logs to a local directory. Logs are also available as artifacts on the [MLflow Run](/concepts/mlflow-run.md). To persist model checkpoints, write them to a Unity Catalog volume.^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

```bash
air logs <job-run-id>                      # Stream logs from node 0
air logs <job-run-id> --node 2             # Logs from a specific node
air logs <job-run-id> --download-to ./logs/ # Download instead of streaming
```

## Related Concepts

- Job Runs – The Databricks execution record shown on the Jobs & Pipelines page.
- [MLflow Runs](/concepts/mlflow-run.md) – The experiment tracking record for metrics, parameters, and artifacts.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – The container for multiple [MLflow](/concepts/mlflow.md) runs, set via `experiment_name`.
- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – The tool (`air`) that submits dual‑run workloads.
- [MLflow Tracking API](/concepts/mlflow-tracking.md) – Used to log custom metrics from within the training process.
- Unity Catalog Volumes – Recommended location for persisting model checkpoints.

## Sources

- track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md

# Citations

1. [track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md](/references/track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws-f3444863.md)
