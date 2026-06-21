---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 47e113d2dc07a282a6a0d7aa43e04e0a2e2a67a045227f1472deb83fc0e9da12
  pageDirectory: concepts
  sources:
    - databricks-autologging-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-autologging-administration
    - DAA
  citations:
    - file: databricks-autologging-databricks-on-aws.md
title: Databricks Autologging Administration
description: Workspace-level controls allowing administrators to enable or disable Databricks Autologging for all interactive notebook sessions across their workspace via the admin settings page, requiring cluster restart to take effect.
tags:
  - databricks
  - administration
  - mlflow
timestamp: "2026-06-19T14:45:39.859Z"
---

# Databricks Autologging Administration

**Databricks Autologging Administration** refers to the ability for workspace administrators to manage, enable, or disable the automated MLflow tracking feature globally across their Databricks workspace. This includes controlling access to Databricks Autologging for all interactive notebook sessions, managing serverless compute configurations, and ensuring proper policy enforcement.

## Overview

Databricks Autologging automatically captures model parameters, metrics, files, and lineage information when you train models from a variety of popular machine learning libraries. Training sessions are recorded as [MLflow tracking runs](/concepts/mlflow-tracking.md), and model files are tracked so you can easily log them to the [MLflow Model Registry](/concepts/mlflow-model-registry.md). ^[databricks-autologging-databricks-on-aws.md]

The feature is generally available in all regions with Databricks Runtime 10.4 LTS ML or above, and in select preview regions with Databricks Runtime 9.1 LTS ML or above. ^[databricks-autologging-databricks-on-aws.md]

## Admin-Level Controls

Administrators can enable or disable Databricks Autologging for all interactive notebook sessions across their workspace from the **Advanced** tab of the admin settings page. Changes do not take effect until the cluster is restarted. ^[databricks-autologging-databricks-on-aws.md]

### Disabling Autologging for All Clusters

To disable Databricks Autologging for all clusters in a workspace:

1. Navigate to the **Advanced** tab of the admin settings page.
2. Disable the feature.
3. Restart all clusters for the change to take effect.

## How It Works

When you attach an interactive Python notebook to a Databricks cluster, Databricks Autologging calls `mlflow.autolog()` to set up tracking for your model training sessions. The default configuration is: ^[databricks-autologging-databricks-on-aws.md]

```python
mlflow.autolog(
    log_input_examples=False,
    log_model_signatures=True,
    log_models=True,
    disable=False,
    exclusive=False,
    disable_for_unsupported_versions=True,
    silent=False
)
```

### Serverless Compute Considerations

Autologging is not automatically enabled on serverless compute. For serverless compute clusters, you must explicitly call `mlflow.autolog()` to enable the functionality. ^[databricks-autologging-databricks-on-aws.md]

Similarly, for serverless compute clusters, autologging for [MLflow Tracing](/concepts/mlflow-tracing.md) is not automatically enabled. You must explicitly enable autologging for the specific framework integrations you want to trace. ^[databricks-autologging-databricks-on-aws.md]

## Customizing Logging Behavior

Users can customize logging behavior on a per-session basis using `mlflow.autolog()` configuration parameters. These include: ^[databricks-autologging-databricks-on-aws.md]

- `log_models`: Enable or disable model logging.
- `log_datasets`: Log datasets used during training.
- `log_input_examples`: Collect input examples.
- `log_model_signatures`: Log model signatures.
- `silent`: Configure warnings.

### Tracking Additional Content

To track additional metrics, parameters, files, and metadata with MLflow runs created by Databricks Autologging, follow these steps in a Databricks interactive Python notebook: ^[databricks-autologging-databricks-on-aws.md]

1. Call `mlflow.autolog()` with `exclusive=False`.
2. Start an [MLflow Run](/concepts/mlflow-run.md) using `mlflow.start_run()`.
3. Use MLflow Tracking methods like `mlflow.log_param()` to track pre-training content.
4. Train one or more machine learning models in a supported framework.
5. Use methods like `mlflow.log_metric()` to track post-training content.
6. End the run using `mlflow.end_run()`.

Example: ^[databricks-autologging-databricks-on-aws.md]

```python
import mlflow
mlflow.autolog(exclusive=False)
with mlflow.start_run():
    mlflow.log_param("example_param", "example_value")
    # <your model training code here>
    mlflow.log_metric("example_metric", 5)
```

## Disabling Autologging for Individual Sessions

To disable Databricks Autologging in a single notebook, call `mlflow.autolog(disable=True)`. Administrators can also disable it for all clusters in a workspace from the admin settings page. Clusters must be restarted for this change to take effect. ^[databricks-autologging-databricks-on-aws.md]

## Security and Data Management

All model training information tracked with Databricks Autologging is stored in MLflow Tracking and secured by [MLflow Experiment permissions](/concepts/mlflow-experiment-permission-levels-for-apps.md). You can share, modify, or delete model training information using the MLflow Tracking API or UI. ^[databricks-autologging-databricks-on-aws.md]

## [MLflow Tracing](/concepts/mlflow-tracing.md) Enablement

[MLflow Tracing](/concepts/mlflow-tracing.md) uses the `autolog` feature within respective model framework integrations to control tracing support. For example, to enable tracing for a LlamaIndex model, use `mlflow.llama_index.autolog(log_traces=True)`. ^[databricks-autologging-databricks-on-aws.md]

Supported integrations with trace enablement include: ^[databricks-autologging-databricks-on-aws.md]

- OpenAI
- LangChain
- LangGraph
- LlamaIndex
- AutoGen

## Supported Environments and Frameworks

Databricks Autologging is supported in interactive Python notebooks for the following ML frameworks: ^[databricks-autologging-databricks-on-aws.md]

- scikit-learn
- [Apache Spark MLlib](/concepts/apache-spark-mllib.md)
- TensorFlow
- Keras
- PyTorch Lightning
- XGBoost
- LightGBM
- Gluon
- Fast.ai
- statsmodels
- PaddlePaddle
- OpenAI
- LangChain

For more information about each framework, see [MLflow automatic logging](/concepts/mlflow-autologging.md). ^[databricks-autologging-databricks-on-aws.md]

## Limitations

- Databricks Autologging is enabled only on the driver node of your Databricks cluster. To use autologging from worker nodes, you must explicitly call `mlflow.autolog()` from within the code executing on each worker. ^[databricks-autologging-databricks-on-aws.md]
- The XGBoost scikit-learn integration is not supported. ^[databricks-autologging-databricks-on-aws.md]

## Related Concepts

- [MLflow Autolog](/concepts/mlflow-autologging.md) — The underlying MLflow functionality for automatic logging.
- Admin Settings Page — Where administrators configure workspace-wide settings.
- [MLflow Tracking](/concepts/mlflow-tracking.md) — The system where autologged data is stored.
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — Where logged models can be registered and managed.
- [MLflow Experiment Permissions](/concepts/mlflow-experiment-permission-levels-for-apps.md) — Access control for experiment data.
- Serverless Compute — Compute environment where autologging is not automatically enabled.
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Trace logging for generative AI workloads.

## Sources

- databricks-autologging-databricks-on-aws.md

# Citations

1. [databricks-autologging-databricks-on-aws.md](/references/databricks-autologging-databricks-on-aws-97e315e8.md)
