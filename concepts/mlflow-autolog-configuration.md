---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 247224a65a0a747b3ec5e9d468884fa52f6f8a8f519db3f56c471731087ab7b2
  pageDirectory: concepts
  sources:
    - databricks-autologging-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-autolog-configuration
    - MAC
  citations:
    - file: databricks-autologging-databricks-on-aws.md
title: MLflow autolog() Configuration
description: The default configuration parameters and customization options for mlflow.autolog() including log_models, log_input_examples, log_model_signatures, disable, exclusive, disable_for_unsupported_versions, and silent flags.
tags:
  - mlflow
  - configuration
  - machine-learning
timestamp: "2026-06-19T14:44:58.338Z"
---

Here is the wiki page for "MLflow autolog() Configuration", written based solely on the provided source material. The page has been updated with citations and the `## Sources` section.

---

# MLflow autolog() Configuration

**MLflow autolog() Configuration** refers to the process of customizing how [`mlflow.autolog()`](https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.autolog) captures model parameters, metrics, files, and lineage information during model training sessions. The function provides several configuration parameters that allow you to control which aspects of training are automatically tracked. ^[databricks-autologging-databricks-on-aws.md]

## Overview

[MLflow Autologging](/concepts/mlflow-autologging.md)](https://docs.databricks.com/aws/en/mlflow/databricks-autologging) automatically records model lineage information, parameters, and metrics to [MLflow Tracking](/concepts/mlflow-tracking.md) when you train models in supported frameworks. The default configuration provides a sensible baseline, but you can customize behavior for specific use cases. ^[databricks-autologging-databricks-on-aws.md]

## Default Configuration

When Databricks Autologging is enabled, it calls `mlflow.autolog()` with the following default parameters: ^[databricks-autologging-databricks-on-aws.md]

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

`mlflow.autolog()` provides several parameters to control logging behavior: ^[databricks-autologging-databricks-on-aws.md]

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `log_models` | bool | `True` | Enable or disable model logging |
| `log_datasets` | bool | - | Enable or disable dataset logging |
| `log_input_examples` | bool | `False` | Collect input examples |
| `log_model_signatures` | bool | `True` | Log model signatures |
| `silent` | bool | `False` | Configure warnings display |
| `disable` | bool | `False` | Disable autologging |
| `exclusive` | bool | `False` | Control run exclusivity |
| `disable_for_unsupported_versions` | bool | `True` | Disable logging for unsupported library versions |

## Disabling Autologging

### Per Workspace
Administrators can disable Databricks Autologging for all clusters in a workspace from the **Advanced** tab of the admin settings page. Clusters must be restarted for this change to take effect. ^[databricks-autologging-databricks-on-aws.md]

### Per Notebook
To disable autologging in a specific notebook session, call `mlflow.autolog()` with `disable=True`: ^[databricks-autologging-databricks-on-aws.md]

```python
import mlflow
mlflow.autolog(disable=True)
```

## Tracking Additional Content

To supplement autologged content with additional metrics, parameters, files, or metadata: ^[databricks-autologging-databricks-on-aws.md]

1. Call `mlflow.autolog()` with `exclusive=False`
2. Start an [MLflow Run](/concepts/mlflow-run.md) using `mlflow.start_run()`
3. Use [MLflow Tracking methods](/concepts/mlflow-tracking.md) such as `mlflow.log_param()` to track pre-training content
4. Train one or more models in a supported framework
5. Use `mlflow.log_metric()` to track post-training content
6. End the run with `mlflow.end_run()` if not using a context manager

```python
import mlflow

mlflow.autolog(exclusive=False)

with mlflow.start_run():
    mlflow.log_param("example_param", "example_value")
    # <your model training code here>
    mlflow.log_metric("example_metric", 5)
```

## Serverless Compute Considerations

Autologging is **not automatically enabled** on serverless compute clusters. For serverless compute, you must explicitly call `mlflow.autolog()` to enable autologging functionality. ^[databricks-autologging-databricks-on-aws.md]

## [MLflow Tracing](/concepts/mlflow-tracing.md) Enablement

For tracing support, certain framework integrations require explicit autolog enablement: ^[databricks-autologging-databricks-on-aws.md]

```python
import mlflow

# Enable tracing for LlamaIndex
mlflow.llama_index.autolog(log_traces=True)
```

Supported integrations with trace enablement include OpenAI, LangChain, LangGraph, LlamaIndex, and [AutoGen](/concepts/autogen-auto-tracing.md). ^[databricks-autologging-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) — The backend where autologged data is stored
- [Databricks Autologging](/concepts/databricks-autologging.md) — The Databricks-specific autologging implementation
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — For managing logged model files
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizational unit for runs
- [Supported ML Frameworks for Autologging](/concepts/supported-ml-frameworks-for-autologging.md) — Frameworks like scikit-learn, TensorFlow, PyTorch Lightning, XGBoost, and others

## Sources

- databricks-autologging-databricks-on-aws.md

# Citations

1. [databricks-autologging-databricks-on-aws.md](/references/databricks-autologging-databricks-on-aws-97e315e8.md)
