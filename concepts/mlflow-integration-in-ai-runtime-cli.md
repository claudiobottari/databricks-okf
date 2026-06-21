---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 632d9442dd23e78754cc7546e0077e1f21d6ce34f18742ff209df85e8f47995e
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-integration-in-ai-runtime-cli
    - MIIARC
  citations:
    - file: ai-runtime-cli-databricks-on-aws.md
title: MLflow integration in AI Runtime CLI
description: AI Runtime CLI integrates with MLflow for tracking runs of distributed training workloads.
tags:
  - mlflow
  - experiment-tracking
  - databricks
timestamp: "2026-06-19T13:56:18.478Z"
---

# MLflow integration in AI Runtime CLI

The **MLflow integration in AI Runtime CLI** enables automatic tracking of distributed training jobs submitted through the `air` command-line interface. When you submit a workload using the CLI, AI Runtime automatically creates an [MLflow Run](/concepts/mlflow-run.md) that captures hyperparameters, metrics, output model artifacts, and system metrics for each training job. ^[ai-runtime-cli-databricks-on-aws.md]

## Overview

The AI Runtime CLI (`air`) is a command-line tool for submitting and managing distributed training workloads on [AI Runtime](/concepts/ai-runtime.md), the on-demand serverless GPU compute platform on Databricks. The CLI integrates with [MLflow](/concepts/mlflow.md) to automatically track runs, providing visibility into training progress and results from the Databricks workspace. ^[ai-runtime-cli-databricks-on-aws.md]

When a workload completes, you can view its results in the **MLflow experiment** associated with the job in the Databricks workspace. The MLflow experiment page displays the tracked parameters, metrics, and artifacts logged during training. ^[ai-runtime-cli-databricks-on-aws.md]

## Automatic Run Tracking

### What Gets Tracked

For each submitted workload, AI Runtime automatically tracks:

- **Hyperparameters**: Values defined in the [Workload YAML Configuration](/concepts/workload-yaml-configuration.md), including any sweep-parameters used for hyperparameter tuning
- **Metrics**: Numeric values logged by the training code during execution (such as loss, accuracy, and validation scores)
- **Output model artifacts**: Model files and checkpoints produced by the training job
- **System metrics**: Resource utilization data, including GPU and memory usage

### Monitoring Runs

Run tracking happens automatically — no additional MLflow client code is required in your training script. After submitting a workload with `air submit`, the CLI output includes a link to the MLflow experiment page where you can monitor progress in real time. ^[ai-runtime-cli-databricks-on-aws.md]

## Viewing Results

### Experiment Page

1. Navigate to the **Experiments** section in the Databricks workspace sidebar.
2. Find the experiment associated with your job. The experiment name is derived from the job name specified in the YAML configuration.
3. Click on the experiment to view individual runs, each corresponding to a submitted workload.

### Run Details Page

From the experiment page, click on a specific run to see:

- **Parameters**: All hyperparameters and configuration values
- **Metrics**: Charts showing metric progression over training steps
- **Artifacts**: Links to saved model files and other outputs
- **Job Run Page**: A link to the corresponding Databricks job run page for infrastructure-level details

### Job Run Page

The **Jobs run page** provides infrastructure-level details about the workload execution, including:

- **Logs**: Standard output and error logs from the training job
- **Environment**: GPU configuration and runtime environment details
- **Status**: Job status, duration, and resource utilization

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) — The command-line interface for submitting distributed training workloads
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for organizing and comparing runs
- Track runs with MLflow and the Jobs run page — Detailed guide on accessing and interpreting run data
- Workload YAML reference — Configuration reference for defining training jobs
- [Hyperparameter Tuning](/concepts/hyperparameter-tuning.md) — Automating search over hyperparameter values using sweep parameters
- [Distributed Training on AI Runtime](/concepts/distributed-training-on-ai-runtime.md) — Overview of serverless GPU distributed training

## Sources

- ai-runtime-cli-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-databricks-on-aws.md](/references/ai-runtime-cli-databricks-on-aws-802adcdc.md)
