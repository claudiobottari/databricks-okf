---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b0b77eb8c7f6b6a5c9e92b8b56ba9c591288f24c8ef96d677ff7b705fa26a234
  pageDirectory: concepts
  sources:
    - track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - run-navigation-and-log-retrieval-commands
    - Log Retrieval Commands and Run Navigation
    - RNALRC
  citations:
    - file: track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md
title: Run Navigation and Log Retrieval Commands
description: The `air get run`, `air list runs`, and `air logs` commands provide navigation between Jobs, MLflow, and previous workloads, as well as streaming/downloading run logs.
tags:
  - cli
  - observability
  - debugging
timestamp: "2026-06-19T23:14:00.341Z"
---

# Run Navigation and Log Retrieval Commands

**Run Navigation and Log Retrieval Commands** are CLI tools provided by the [AI Runtime CLI](/concepts/ai-runtime-cli.md) (`air`) that allow users to locate, inspect, and retrieve logs from previous workload submissions. These commands bridge the gap between Databricks job runs and [MLflow](/concepts/mlflow.md) runs, providing multiple pathways to access run information.

## Overview

Each workload submitted with `air run` creates both a Databricks job run and an [MLflow Run](/concepts/mlflow-run.md). The job run tracks execution details (status, compute, retries, driver output), while the [MLflow Run](/concepts/mlflow-run.md) tracks experiment data (parameters, metrics, system metrics, artifacts). One submission creates one job run and one [MLflow Run](/concepts/mlflow-run.md); a retry creates a new [MLflow Run](/concepts/mlflow-run.md) within the same experiment. ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

## Navigation Commands

### `air get run`

The `air get run <job-run-id>` command retrieves details about a specific run and prints clickable links to the run's job page, experiment, and [MLflow Run](/concepts/mlflow-run.md). This provides a direct entry point to both the operational and experimental views of a workload. ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

### `air list runs`

The `air list runs` command lists all previous runs and supports filtering to find a specific run. This is useful for browsing historical workloads and locating runs by criteria such as status, time range, or experiment name. ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

## Log Retrieval Commands

### `air logs`

The `air logs` command streams or downloads logs from a completed or running workload. It supports the following options: ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

```bash
air logs <job-run-id>              # Stream logs from node 0
air logs <job-run-id> --node 2     # Logs from a specific node
air logs <job-run-id> --download-to ./logs/  # Download instead of streaming
```

- **Default behavior**: Streams logs from node 0.
- **`--node` flag**: Retrieves logs from a specific node in a multi-node workload.
- **`--download-to` flag**: Downloads logs to a local directory instead of streaming them to the terminal.

Logs are also available as artifacts on the corresponding [MLflow Run](/concepts/mlflow-run.md). ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

## Navigation Pathways

Users can access a run from three entry points: ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

1. **Jobs page**: The Jobs run page lists all runs, and each run links to its [MLflow Run](/concepts/mlflow-run.md) and experiment.
2. **MLflow**: The Experiments page lists all [MLflow](/concepts/mlflow.md) experiments, which contain the runs.
3. **Previous workloads**: The `air get run` and `air list runs` commands provide CLI access with clickable links.

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The command-line interface that provides these navigation and log commands.
- [MLflow Run Tracking](/concepts/mlflow-tracking.md) — How [MLflow](/concepts/mlflow.md) tracks parameters, metrics, and artifacts for each run.
- [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md) — The operational view of workload execution.
- [Multi-Node Distributed Training](/concepts/multi-gpu-distributed-training-api.md) — Context for using the `--node` flag with log retrieval.
- [Experiment Tracking and Observability](/concepts/ai-runtime-experiment-tracking-and-observability.md) — Best practices for managing checkpoints and logs.

## Sources

- track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md

# Citations

1. [track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md](/references/track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws-f3444863.md)
