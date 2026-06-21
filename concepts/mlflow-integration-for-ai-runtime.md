---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6478261be364f4d33e7a1aad7ab17a156468b7307eea72e7f640ab1d55adbd5f
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-quickstart-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-integration-for-ai-runtime
    - MIFAR
  citations:
    - file: ai-runtime-cli-quickstart-databricks-on-aws.md
title: MLflow Integration for AI Runtime
description: Automatic tracking of training workload metrics, parameters, artifacts, and logs in MLflow experiments and runs, viewable in the Databricks workspace UI
tags:
  - mlflow
  - experiment-tracking
  - observability
timestamp: "2026-06-18T14:22:38.562Z"
---

# MLflow Integration for AI Runtime

The **AI Runtime CLI** natively integrates with **MLflow** to provide end-to-end experiment tracking, logging, and artifact management for training workloads. Every submission via the CLI creates a new [MLflow Run](/concepts/mlflow-run.md) inside a specified MLflow experiment, making it easy to compare metrics, parameters, and outputs across runs in the workspace UI. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Experiment Tracking

In the [AI Runtime YAML config](), the `experiment_name` field identifies the MLflow experiment under which the run is created. A single experiment can hold many runs, enabling iterative experimentation. When a workload is submitted with `air run`, the CLI automatically creates a run in that experiment and attaches the job’s metadata to it. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## What Gets Captured

Each [MLflow Run](/concepts/mlflow-run.md) captures the full set of information needed to reproduce and analyze a training job: ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

- **Metrics** – Training loss, accuracy, etc.
- **Parameters** – Hyperparameters, configuration values.
- **Artifacts** – Model checkpoints, plots, and other output files.
- **Logs** – Standard output and error streams from all compute nodes.

All of this data is immediately viewable in the workspace **MLflow UI** — the `air run` command prints clickable links to both the experiment and the specific run. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Viewing Runs and Logs

Beyond the MLflow UI, the CLI provides dedicated commands to inspect runs and retrieve logs: ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

- `air list runs` – List recent or active runs for the workspace.
- `air logs <run-id>` – Stream logs from a run’s first node (default). Use `--node` to select a different node and `--download-to` to save logs locally.
- `air cancel <run-id>` – Stop a running job.

The output of `air run` also includes the run ID, which is used with these commands to inspect progress and collect results. ^[ai-runtime-cli-quickstart-databricks-on-aws.md]

## Workflow Example

A typical workflow using MLflow integration:

1. Author a `train.yaml` with an `experiment_name` and a training command.
2. Submit with `air run --file train.yaml`.
3. After submission, open the MLflow experiment link to monitor metrics.
4. Use `air logs <run-id>` to tail the training output.
5. After completion, compare multiple runs in the MLflow UI to select the best model.

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – Command-line tool for submitting and managing serverless GPU workloads.
- [AI Runtime YAML Config](/concepts/databricks-ai-runtime-cli-yaml-config.md) – Full reference for the YAML specification, including `experiment_name` and `code_source`.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – The organizational unit for training runs; supports comparison and search.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – The underlying API that logs metrics, parameters, and artifacts.
- [Serverless GPU Environments](/concepts/serverless-gpu-environment.md) – The compute environment versions used by AI Runtime.

## Sources

- ai-runtime-cli-quickstart-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-quickstart-databricks-on-aws.md](/references/ai-runtime-cli-quickstart-databricks-on-aws-87563c23.md)
