---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 89d5b21222194a78d9f0e04c56e29d5bf59abf9ff36850718f3849ff48125205
  pageDirectory: concepts
  sources:
    - databricks-autologging-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-autolog-configuration-parameters
    - MACP
  citations:
    - file: databricks-autologging-databricks-on-aws.md
title: MLflow Autolog Configuration Parameters
description: A set of configurable parameters (log_input_examples, log_model_signatures, log_models, disable, exclusive, disable_for_unsupported_versions, silent) that control what and how Databricks Autologging captures during model training.
tags:
  - mlflow
  - configuration
  - machine-learning
timestamp: "2026-06-18T11:32:39.417Z"
---

# MLflow Autolog Configuration Parameters

**MLflow Autolog Configuration Parameters** control the automatic capture of model parameters, metrics, files, and lineage information when training models in Databricks. Databricks Autologging calls `mlflow.autolog()` with a default set of parameters when an interactive Python notebook is attached to a supported cluster. Users can override these defaults to customize logging behavior. ^[databricks-autologging-databricks-on-aws.md]

## Overview

Databricks Autologging automatically records model training sessions as [MLflow Tracking](/concepts/mlflow-tracking.md) runs. It uses the `mlflow.autolog()` function to set up tracking for supported ML frameworks. The default configuration is applied unless explicitly overridden. Users can call `mlflow.autolog()` with custom parameters to enable or disable specific features such as model logging, input examples, and model signatures. ^[databricks-autologging-databricks-on-aws.md]

## Default Configuration

When a notebook is attached to a Databricks cluster, Autologging applies the following default call to `mlflow.autolog()`: ^[databricks-autologging-databricks-on-aws.md]

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

## Parameter Descriptions

### `log_input_examples`

Boolean. When `True`, MLflow logs input examples from the training dataset. Default is `False`. ^[databricks-autologging-databricks-on-aws.md]

### `log_model_signatures`

Boolean. When `True`, MLflow infers and logs the model signature (input and output schema). Default is `True`. ^[databricks-autologging-databricks-on-aws.md]

### `log_models`

Boolean. When `True`, the trained model is automatically logged as an MLflow model artifact. Default is `True`. ^[databricks-autologging-databricks-on-aws.md]

### `log_datasets`

Boolean. When `True`, MLflow logs the dataset used for training as a dataset artifact. This parameter is mentioned in the documentation but is not part of the default call. Users can set it explicitly. ^[databricks-autologging-databricks-on-aws.md]  

*(Note: The source text states that `mlflow.autolog()` "provides configuration parameters to enable ... log datasets" but does not list `log_datasets` in the default code block. It is an available parameter that can be overridden.)*

### `disable`

Boolean. When `True`, Autologging is completely disabled. Default is `False`. ^[databricks-autologging-databricks-on-aws.md]

### `exclusive`

Boolean. When `False` (default), autologged content is added to an existing [MLflow Run](/concepts/mlflow-run.md) started with `mlflow.start_run()`. When `True`, autologging creates its own runs and does not nest under user-started runs. Default is `False`. ^[databricks-autologging-databricks-on-aws.md]

### `disable_for_unsupported_versions`

Boolean. When `True`, Autologging is automatically disabled for unsupported versions of ML frameworks. Default is `True`. ^[databricks-autologging-databricks-on-aws.md]

### `silent`

Boolean. When `True`, suppresses warnings and informational messages from autologging. Default is `False`. ^[databricks-autologging-databricks-on-aws.md]

## Customizing Logging Behavior

Users can override any default parameter by calling `mlflow.autolog()` with the desired values before training. For example: ^[databricks-autologging-databricks-on-aws.md]

```python
import mlflow
mlflow.autolog(log_models=False, log_input_examples=True)
```

This configuration logs input examples but does not log model artifacts.

## Tracking Additional Content

To supplement autologged content with custom metrics or parameters, call `mlflow.autolog(exclusive=False)` and then use `mlflow.start_run()`. Within the run, you can call `mlflow.log_param()` or `mlflow.log_metric()` alongside model training. ^[databricks-autologging-databricks-on-aws.md]

## Disabling Autologging

### In a Notebook

Call `mlflow.autolog(disable=True)`: ^[databricks-autologging-databricks-on-aws.md]

```python
import mlflow
mlflow.autolog(disable=True)
```

### Workspace-Wide

Administrators can disable Databricks Autologging for all clusters in a workspace from the **Advanced** tab of the admin settings page. Clusters must be restarted for the change to take effect. ^[databricks-autologging-databricks-on-aws.md]

## [MLflow Tracing](/concepts/mlflow-tracing.md) Enablement

For supported integrations (OpenAI, LangChain, LangGraph, LlamaIndex, AutoGen), [MLflow Tracing](/concepts/mlflow-tracing.md) is controlled via autolog parameters in the framework-specific `autolog()` functions. For example, to enable tracing for LlamaIndex: ^[databricks-autologging-databricks-on-aws.md]

```python
import mlflow
mlflow.llama_index.autolog(log_traces=True)
```

Tracing is not auto-enabled on serverless compute; users must explicitly call the framework-specific `autolog()` with `log_traces=True`. ^[databricks-autologging-databricks-on-aws.md]

## Serverless Compute Considerations

Autologging is **not** automatically enabled on serverless compute clusters. Users must explicitly call `mlflow.autolog()` to enable automatic tracking. Similarly, for tracing, framework-specific autolog calls must be made manually. ^[databricks-autologging-databricks-on-aws.md]

## Related Concepts

- [Databricks Autologging](/concepts/databricks-autologging.md) — The overall feature that calls `mlflow.autolog()` automatically
- [MLflow Tracking](/concepts/mlflow-tracking.md) — The system where autologged parameters, metrics, and models are stored
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — Where logged models can be registered for production use
- [MLflow Autolog](/concepts/mlflow-autologging.md) — The underlying OSS function referenced by Databricks Autologging
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Trace capture for generative AI workloads, controlled via autolog parameters

## Sources

- databricks-autologging-databricks-on-aws.md

# Citations

1. [databricks-autologging-databricks-on-aws.md](/references/databricks-autologging-databricks-on-aws-97e315e8.md)
