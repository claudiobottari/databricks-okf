---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 32b6f4bd7ff0229664d19d93c81022f0bed89f511ea639d37f137386a351766c
  pageDirectory: concepts
  sources:
    - databricks-autologging-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflowautolog-configuration
    - Customizing Autologging Configuration
    - customize the autologging configuration
  citations:
    - file: databricks-autologging-databricks-on-aws.md
title: mlflow.autolog() Configuration
description: The Python API function used to enable, disable, and customize Databricks Autologging behavior with parameters like log_models, log_input_examples, and log_model_signatures.
tags:
  - mlflow
  - python-api
  - configuration
timestamp: "2026-06-19T18:08:45.909Z"
---

# mlflow.autolog() Configuration

**mlflow.autolog() Configuration** refers to the parameters and settings available when using the `mlflow.autolog()` function to automatically capture model training information — including parameters, metrics, files, and lineage data — from supported machine learning frameworks. This configuration is central to [Databricks Autologging](/concepts/databricks-autologging.md) and [MLflow Tracking](/concepts/mlflow-tracking.md) workflows.

## Overview

The `mlflow.autolog()` function enables automatic tracking of model training sessions. When called, it sets up logging for supported machine learning libraries, capturing training parameters, metrics, and model artifacts as MLflow Tracking Runs. On Databricks, this function is automatically called when you attach an interactive Python notebook to a cluster (except on serverless compute, where it must be explicitly invoked). ^[databricks-autologging-databricks-on-aws.md]

## Default Configuration

The default configuration for `mlflow.autolog()` on Databricks is: ^[databricks-autologging-databricks-on-aws.md]

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

## Configuration Parameters

### Core Logging Controls

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `log_models` | bool | `True` | Whether to log trained models |
| `log_datasets` | bool | Varies | Whether to log input datasets |
| `log_input_examples` | bool | `False` | Whether to collect and log input examples |
| `log_model_signatures` | bool | `True` | Whether to log model signatures (input/output schemas) |

### Operational Controls

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `disable` | bool | `False` | When `True`, disables autologging entirely |
| `exclusive` | bool | `False` | When `True`, prevents additional manual logging alongside autologging |
| `disable_for_unsupported_versions` | bool | `True` | Whether to disable autologging for unsupported framework versions |
| `silent` | bool | `False` | Whether to suppress warning messages during autologging |

^[databricks-autologging-databricks-on-aws.md]

## Disabling Autologging

To disable Databricks Autologging in an interactive Python notebook, call `mlflow.autolog()` with `disable=True`: ^[databricks-autologging-databricks-on-aws.md]

```python
import mlflow
mlflow.autolog(disable=True)
```

Administrators can also disable autologging for all clusters in a workspace from the **Advanced** tab of the admin settings page. Clusters must be restarted for this change to take effect. ^[databricks-autologging-databricks-on-aws.md]

## Using Autologging with Manual Tracking

To combine automatic logging with additional [MLflow Tracking](/concepts/mlflow-tracking.md) content, call `mlflow.autolog()` with `exclusive=False`, then manually start a run and log extra parameters, metrics, or files: ^[databricks-autologging-databricks-on-aws.md]

```python
import mlflow

mlflow.autolog(exclusive=False)

with mlflow.start_run():
    mlflow.log_param("example_param", "example_value")
    # <your model training code here>
    mlflow.log_metric("example_metric", 5)
```

## [MLflow Tracing](/concepts/mlflow-tracing.md) Enablement

`mlflow.autolog()` controls the enabling of tracing support for framework integrations that support it. For example, to enable tracing for LlamaIndex: ^[databricks-autologging-databricks-on-aws.md]

```python
import mlflow
mlflow.llama_index.autolog(log_traces=True)
```

On serverless compute clusters, tracing autologging is not automatically enabled and must be explicitly called. The following integrations support trace enablement through autolog: ^[databricks-autologging-databricks-on-aws.md]

- OpenAI (`mlflow.openai.autolog()`)
- LangChain (`mlflow.langchain.autolog()`)
- LangGraph (`mlflow.langchain.autolog()`)
- LlamaIndex (`mlflow.llama_index.autolog()`)
- [AutoGen](/concepts/autogen-auto-tracing.md) (`mlflow.autogen.autolog()`)

## Supported Frameworks

Databricks Autologging supports the following ML frameworks via `mlflow.autolog()`: ^[databricks-autologging-databricks-on-aws.md]

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

## Important Notes

- Autologging is not automatically enabled on serverless compute; you must explicitly call `mlflow.autolog()`. ^[databricks-autologging-databricks-on-aws.md]
- Databricks Autologging is not applied to runs created using `mlflow.start_run()` directly. In such cases, call `mlflow.autolog()` explicitly. ^[databricks-autologging-databricks-on-aws.md]
- Autologging is enabled only on the driver node of your cluster. To use it from worker nodes, call `mlflow.autolog()` explicitly from worker code. ^[databricks-autologging-databricks-on-aws.md]
- The XGBoost scikit-learn integration is not supported. ^[databricks-autologging-databricks-on-aws.md]

## Related Concepts

- [Databricks Autologging](/concepts/databricks-autologging.md)
- [MLflow Tracking](/concepts/mlflow-tracking.md)
- MLflow Tracking Runs
- [MLflow Model Registry](/concepts/mlflow-model-registry.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- [OpenAI Autologging](/concepts/mlflow-openai-autolog.md)

## Sources

- databricks-autologging-databricks-on-aws.md

# Citations

1. [databricks-autologging-databricks-on-aws.md](/references/databricks-autologging-databricks-on-aws-97e315e8.md)
