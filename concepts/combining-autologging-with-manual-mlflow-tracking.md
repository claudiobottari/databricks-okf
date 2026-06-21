---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9af19645bdfc22e8a7eabd4a73659083162a26a33eb5dcd536c4a2ee1cf67d7b
  pageDirectory: concepts
  sources:
    - databricks-autologging-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - combining-autologging-with-manual-mlflow-tracking
    - CAWMMT
  citations:
    - file: databricks-autologging-databricks-on-aws.md
title: Combining Autologging with Manual MLflow Tracking
description: A pattern using mlflow.autolog(exclusive=False) and mlflow.start_run() to augment automatically captured autologging data with additional custom metrics, parameters, and artifacts.
tags:
  - mlflow
  - workflow
  - integration
timestamp: "2026-06-18T15:02:22.375Z"
---

# Combining Autologging with Manual MLflow Tracking

**Combining Autologging with Manual MLflow Tracking** refers to the practice of using [Databricks Autologging](/concepts/databricks-autologging.md) together with explicit [MLflow Tracking](/concepts/mlflow-tracking.md) API calls (such as `mlflow.start_run()`, `mlflow.log_param()`, or `mlflow.log_metric()`) within the same [MLflow Run](/concepts/mlflow-run.md). This approach allows you to leverage automatic logging of model parameters, metrics, and artifacts while also recording additional custom information that autologging does not capture.

## When to Combine

Databricks Autologging is enabled automatically in interactive Python notebooks on Databricks (for supported frameworks). However, autologging is **not** applied to runs that are created explicitly using `mlflow.start_run()`. If you create a run manually via the fluent API, Databricks Autologging will not automatically log content to that run unless you also call `mlflow.autolog()` and configure it appropriately. ^[databricks-autologging-databricks-on-aws.md]

Therefore, combining the two is necessary whenever you want to:

- Add pre‑training or post‑training parameters and metrics that autologging does not capture.
- Control the run lifecycle (e.g., using a `with mlflow.start_run():` block) while still benefiting from automatic framework logging.

## How to Combine Manual and Automatic Tracking

To mix manual MLflow Tracking with Databricks Autologging, follow these steps: ^[databricks-autologging-databricks-on-aws.md]

1. **Call `mlflow.autolog()` with `exclusive=False`**.  
   The `exclusive=False` argument tells MLflow not to block manual logging inside runs. This ensures that autologging can write to runs you start manually. ^[databricks-autologging-databricks-on-aws.md]

2. **Start an MLflow run** using `mlflow.start_run()`.  
   You can wrap this call in a `with mlflow.start_run():` block; when you do so, the run is ended automatically after the block completes. ^[databricks-autologging-databricks-on-aws.md]

3. **Log pre‑training content** using MLflow Tracking methods, such as `mlflow.log_param()`. ^[databricks-autologging-databricks-on-aws.md]

4. **Train one or more models** in a framework supported by Databricks Autologging (e.g., scikit‑learn, XGBoost, PyTorch Lightning). Autologging will automatically capture parameters, metrics, and model artifacts from this training. ^[databricks-autologging-databricks-on-aws.md]

5. **Log post‑training content** using MLflow Tracking methods, such as `mlflow.log_metric()`. ^[databricks-autologging-databricks-on-aws.md]

6. **End the MLflow run** using `mlflow.end_run()` if you did not use the `with` statement in step 2. ^[databricks-autologging-databricks-on-aws.md]

### Example

```python
import mlflow

mlflow.autolog(exclusive=False)

with mlflow.start_run():
    mlflow.log_param("example_param", "example_value")
    # <your model training code here>
    mlflow.log_metric("example_metric", 5)
```

## Important Notes

- Databricks Autologging is **not** applied to runs created with `mlflow.start_run()` unless you explicitly call `mlflow.autolog()` with `exclusive=False`. ^[databricks-autologging-databricks-on-aws.md]
- The combination works inside interactive Python notebooks on Databricks. For serverless compute, autologging is not automatically enabled; you must call `mlflow.autolog()` explicitly. ^[databricks-autologging-databricks-on-aws.md]

## Related Concepts

- [Databricks Autologging](/concepts/databricks-autologging.md) – Automatic tracking for supported ML frameworks.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – The underlying API for logging runs, parameters, metrics, and artifacts.
- [mlflow.autolog()](/concepts/mlflow-autologging.md) – The function that controls autologging behaviour.
- [MLflow Runs](/concepts/mlflow-run.md) – The fundamental unit of tracking in MLflow.
- Serverless Compute on Databricks – Environment where autologging must be manually enabled.

## Sources

- databricks-autologging-databricks-on-aws.md

# Citations

1. [databricks-autologging-databricks-on-aws.md](/references/databricks-autologging-databricks-on-aws-97e315e8.md)
