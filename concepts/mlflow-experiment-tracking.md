---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8cf1892820bcbacb33abdf9bfa38b04a64688d2462f2fa35dab0d19f43d587c2
  pageDirectory: concepts
  sources:
    - mlflow-api-reference-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-experiment-tracking
    - MET
    - Experiment Tracking
    - Experiment tracking
    - experiment tracking
  citations:
    - file: mlflow-api-reference-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: MLflow Experiment Tracking
description: The MLflow capability to create, list, get, and manage experiments and runs programmatically via the REST API
tags:
  - mlflow
  - experiments
  - tracking
timestamp: "2026-06-19T19:38:07.893Z"
---

# MLflow Experiment Tracking

**MLflow Experiment Tracking** is the component of the open-source [MLflow](/concepts/mlflow.md) platform that records and queries machine learning experiments, runs, parameters, metrics, and artifacts. It provides a REST API for programmatic interaction and is integrated into [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) as a managed service. ^[mlflow-api-reference-databricks-on-aws.md]

## Overview

The open-source MLflow REST API allows you to create, list, and get experiments and runs, and to log parameters, metrics, and artifacts. ^[mlflow-api-reference-databricks-on-aws.md] Experiments serve as organizational units that group together related runs, each run capturing a single execution of a training script. Users can compare runs, visualize metrics, and retrieve artifacts (such as models or plots) through the API or the MLflow UI.

Databricks provides a managed version of the MLflow server, which includes experiment tracking and the [Model Registry](/concepts/mlflow-model-registry.md), eliminating the need to operate the MLflow server infrastructure. ^[mlflow-api-reference-databricks-on-aws.md]

## Key Concepts

- **Experiment**: A logical grouping of runs. Each experiment has a name, ID, and optional tags. Tags can be used to attach metadata, such as a serverless budget policy for controlling serverless workload spending. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]
- **Run**: A single execution of a machine learning task. A run belongs to one experiment and can log parameters, metrics, tags, and artifacts.
- **Parameters**: Key-value pairs representing input settings (e.g., learning rate, number of layers).
- **Metrics**: Numeric values tracked over time (e.g., accuracy, loss).
- **Artifacts**: Files produced by a run (e.g., model binaries, plots, data files).

## API Reference

The MLflow REST API is available in two versions:

- **Databricks MLflow REST API 2.0**: A workspace-level API for managing experiments and runs on Databricks. See the [Databricks API reference](https://docs.databricks.com/api/workspace/experiments). ^[mlflow-api-reference-databricks-on-aws.md]
- **Open Source MLflow REST API**: The community API specification. See the [open-source reference](https://mlflow.org/docs/latest/rest-api.html). ^[mlflow-api-reference-databricks-on-aws.md]

Both APIs support the same core operations for experiment tracking.

## Configuration: Serverless Budget Policy

In Databricks, MLflow experiments can be assigned a serverless budget policy to control spending on serverless workloads that the experiment creates (e.g., scheduled scorers, synthetic evaluation set generation, agent evaluation). If the workspace disables its default budget policy, MLflow returns a `403 PERMISSION_DENIED` error unless a specific policy is set on the experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

To set a budget policy, use the MLflow experiment tag `mlflow.workload_creation_policy_id`:

```python
import mlflow

mlflow.set_experiment_tag(
    experiment_id="<your-experiment-id>",
    key="mlflow.workload_creation_policy_id",
    value="<your-policy-id>",
)
```

This ensures that all serverless workloads triggered from the experiment use the specified policy. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Databricks Managed Version

The Databricks Runtime for Machine Learning includes a managed MLflow server, so experiment tracking and the Model Registry are available without additional setup. Users interact with experiment tracking through the Databricks UI, the MLflow Python client, or the REST API directly. ^[mlflow-api-reference-databricks-on-aws.md]

## Related Concepts

- [MLflow](/concepts/mlflow.md) – The overall open-source platform.
- [Model Registry](/concepts/mlflow-model-registry.md) – Component for model versioning and lifecycle management.
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) – Mechanism for controlling serverless workload costs on Databricks.
- 403 PERMISSION_DENIED Serverless Budget Policy Error – Common error when no budget policy is assigned.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – The runtime that bundles MLflow.
- [Parameter tuning](/concepts/hyperparameter-tuning.md) – Workflow commonly tracked with experiments.

## Sources

- mlflow-api-reference-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [mlflow-api-reference-databricks-on-aws.md](/references/mlflow-api-reference-databricks-on-aws-472f1a07.md)
2. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
