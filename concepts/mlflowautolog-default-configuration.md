---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 98c2aece2e81fbe9228c9a756b3e86b00602de74dff82e1d85bfb0a775a1f33d
  pageDirectory: concepts
  sources:
    - databricks-autologging-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflowautolog-default-configuration
    - MDC
  citations:
    - file: databricks-autologging-databricks-on-aws.md
title: mlflow.autolog() Default Configuration
description: Default parameter values for mlflow.autolog() on Databricks, including log_models, log_model_signatures, and disabling of input examples
tags:
  - mlflow
  - configuration
  - python-api
timestamp: "2026-06-19T09:45:45.964Z"
---

# mlflow.autolog() Default Configuration

**mlflow.autolog() Default Configuration** refers to the set of parameter values that [Databricks Autologging](/concepts/databricks-autologging.md) uses when it automatically calls [`mlflow.autolog()`](https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.autolog) on interactive Python notebooks attached to a Databricks cluster. This configuration determines which aspects of model training are automatically captured as MLflow tracking runs.

## Overview

When you attach an interactive Python notebook to a Databricks cluster (running Databricks Runtime 10.4 LTS ML or above), Databricks Autologging invokes `mlflow.autolog()` with a specific set of default parameters to enable tracking for supported machine learning frameworks. The default configuration is designed to capture essential model metadata while allowing users to customize behavior as needed. ^[databricks-autologging-databricks-on-aws.md]

## Default Parameters

The exact default call issued by Databricks Autologging is as follows: ^[databricks-autologging-databricks-on-aws.md]

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

| Parameter | Default Value | Description |
|-----------|---------------|-------------|
| `log_input_examples` | `False` | Whether to collect and log input examples from the training data. |
| `log_model_signatures` | `True` | Whether to infer and log the model signature (input/output schema). |
| `log_models` | `True` | Whether to log the trained model as an MLflow artifact. |
| `disable` | `False` | Whether to disable autologging entirely for the session. |
| `exclusive` | `False` | Whether autologged runs should be exclusive (i.e., do not allow user-created runs within the same autolog context). |
| `disable_for_unsupported_versions` | `True` | Whether to silently disable autologging when the framework version is not supported. |
| `silent` | `False` | Whether to suppress informational messages from autologging. |

## Customization

Users can override any of these defaults by calling `mlflow.autolog()` with different parameter values in their notebook. For example, to enable input example logging: ^[databricks-autologging-databricks-on-aws.md]

```python
import mlflow
mlflow.autolog(log_input_examples=True)
```

The `mlflow.autolog()` function also supports additional parameters beyond the default set, such as `log_datasets` for logging dataset information. ^[databricks-autologging-databricks-on-aws.md]

## Important Notes

- **Serverless compute**: Autologging is **not** automatically enabled on serverless compute clusters. On such clusters, you must explicitly call `mlflow.autolog()` to enable the feature. ^[databricks-autologging-databricks-on-aws.md]
- **Manual run creation**: If you create MLflow runs using `mlflow.start_run()` (the fluent API), Databricks Autologging does not automatically apply to those runs. You must call `mlflow.autolog()` with `exclusive=False` to have autologged content saved to the run. ^[databricks-autologging-databricks-on-aws.md]
- **Administration**: Workspace administrators can disable Databricks Autologging globally from the **Advanced** tab of the admin settings page. Changes require a cluster restart. ^[databricks-autologging-databricks-on-aws.md]

## Related Concepts

- [Databricks Autologging](/concepts/databricks-autologging.md) – The overarching feature that calls `mlflow.autolog()`.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – The underlying system that stores autologged runs.
- [Model Signatures](/concepts/model-signatures-in-unity-catalog.md) – How `log_model_signatures=True` captures input/output schemas.
- Input Examples – How `log_input_examples` can capture sample inputs.
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) – Where logged models can be registered.

## Sources

- databricks-autologging-databricks-on-aws.md

# Citations

1. [databricks-autologging-databricks-on-aws.md](/references/databricks-autologging-databricks-on-aws-97e315e8.md)
