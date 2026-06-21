---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: adc604c80ffe7c0e8757816b764fab9366fb811eb6d3ac9c90a94a820e43bcab
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-integration-for-distributed-training-runs
    - MIFDTR
  citations:
    - file: ai-runtime-cli-databricks-on-aws.md
title: MLflow Integration for Distributed Training Runs
description: Integration between the AI Runtime CLI and MLflow for tracking distributed training runs, combined with visibility in the Databricks Jobs run page
tags:
  - mlflow
  - experiment-tracking
  - databricks
  - mlops
timestamp: "2026-06-19T22:03:09.243Z"
---

# MLflow Integration for Distributed Training Runs

**MLflow Integration for Distributed Training Runs** refers to the built-in mechanisms by which [MLflow](/concepts/mlflow.md) automatically tracks and logs distributed training workloads executed on [AI Runtime](/concepts/ai-runtime.md), the on-demand serverless GPU compute platform on Databricks. This integration provides visibility into training progress, hyperparameters, metrics, and artifacts without requiring manual instrumentation.

## Overview

When distributed training runs are submitted via the [AI Runtime CLI](/concepts/ai-runtime-cli.md) (`air` command) or through the in-notebook Python API (`@distributed` decorator), MLflow automatically captures run metadata and training metrics. This integration works out-of-the-box, eliminating the need for users to write explicit MLflow logging calls within their training scripts. ^[ai-runtime-cli-databricks-on-aws.md]

The AI Runtime CLI uses YAML-based job configuration and integrates with MLflow to track runs, making it suitable for users who want to submit GPU training workloads from a local laptop or code editor without opening a notebook. ^[ai-runtime-cli-databricks-on-aws.md]

## Tracking Mechanisms

MLflow integration for distributed training runs provides the following tracking capabilities:

- **Automatic experiment tracking**: Each distributed training run is automatically logged to an MLflow experiment, capturing parameters, metrics, and artifacts.
- **Run metadata**: Information about the training job, including GPU configuration, node count, and job parameters, is recorded in the [MLflow Run](/concepts/mlflow-run.md).
- **Metric logging**: Training metrics such as loss and accuracy are logged over time, enabling visualization and comparison across runs.
- **Artifact storage**: Model checkpoints, training logs, and other output files are stored as MLflow artifacts for later retrieval and analysis.
- **Parameter capture**: Training hyperparameters and configuration values are automatically recorded.

## Workflow Support

The MLflow integration supports two primary workflows for distributed training:

```yaml
# Example YAML configuration for the AI Runtime CLI
# This configuration specifies a distributed training job
# that will be automatically tracked by MLflow
name: distributed-training-job
runtime:
  type: gpu
  gpu_type: h100
  gpus_per_node: 8
  num_nodes: 4
code:
  entry_point: train.py
  workspace_path: /Users/username/project
```

^[ai-runtime-cli-databricks-on-aws.md]

1. **YAML-based job configuration**: Users define distributed training jobs declaratively in YAML files that can be checked into source control. The AI Runtime CLI submits these jobs, and MLflow automatically tracks the resulting runs. ^[ai-runtime-cli-databricks-on-aws.md]

2. **In-notebook Python API**: The `@distributed` decorator from the `serverless_gpu` library allows running functions across multiple GPUs. MLflow tracks the runs spawned from these notebook-based workflows. ^[ai-runtime-cli-databricks-on-aws.md]

## Run Tracking and Visualization

MLflow runs for distributed training jobs can be viewed and compared through:

- The **MLflow experiment UI** within Databricks, where all tracked runs for an experiment are displayed with their parameters, metrics, and artifacts.
- The **Jobs run page**, which provides additional context about the underlying compute resources and job execution details. ^[ai-runtime-cli-databricks-on-aws.md]

Users can compare runs across different hyperparameter configurations, GPU configurations (such as [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) vs. multi-node setups), and training approaches to identify the optimal setup for their model.

## Benefits

The automatic MLflow integration for distributed training runs provides several advantages:

- **Reduced boilerplate**: No need to write explicit `mlflow.log_param()`, `mlflow.log_metric()`, or `mlflow.log_artifact()` calls within training scripts.
- **Consistent tracking**: All distributed training jobs are tracked uniformly, ensuring reproducibility and comparability.
- **Operational visibility**: Teams can monitor training progress, debug issues, and audit historical runs.
- **Model lineage**: The integration preserves the full lineage from training configuration to produced model artifacts.

## Related Concepts

- [AI Runtime CLI](/concepts/ai-runtime-cli.md) – The command-line interface for submitting and managing distributed training workloads.
- [AI Runtime](/concepts/ai-runtime.md) – The on-demand serverless GPU compute platform on Databricks.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – The organizational unit for organizing and comparing MLflow runs.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – The core MLflow component for logging parameters, metrics, and artifacts.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – The broader concept of training models across multiple GPUs and nodes.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) – A specific GPU configuration commonly used for distributed training.
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) – Large model training scenarios that benefit from distributed training with MLflow tracking.

## Sources

- ai-runtime-cli-databricks-on-aws.md

# Citations

1. [ai-runtime-cli-databricks-on-aws.md](/references/ai-runtime-cli-databricks-on-aws-802adcdc.md)
