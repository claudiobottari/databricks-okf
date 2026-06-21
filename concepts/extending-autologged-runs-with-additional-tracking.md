---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 271c4a6e0ff608bd0e78e65110a7b63375aa5fd4812b8abd2f0b1df1ea68804b
  pageDirectory: concepts
  sources:
    - databricks-autologging-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - extending-autologged-runs-with-additional-tracking
    - EARWAT
  citations:
    - file: databricks-autologging-databricks-on-aws.md
title: Extending Autologged Runs with Additional Tracking
description: Pattern for combining automatic autologging with manual MLflow tracking calls (log_param, log_metric) by setting exclusive=False and wrapping training code inside mlflow.start_run().
tags:
  - mlflow
  - pattern
  - workflow
timestamp: "2026-06-18T11:33:11.975Z"
---

# Extending Autologged Runs with Additional Tracking

**Extending Autologged Runs with Additional Tracking** refers to the practice of supplementing the metrics, parameters, files, and metadata that [Databricks Autologging](/concepts/databricks-autologging.md) automatically captures for MLflow runs with additional custom tracking information. While Databricks Autologging automatically records model parameters, metrics, and lineage information when training models from supported libraries, you can add extra content before and after model training using [MLflow Tracking](/concepts/mlflow-tracking.md) methods. ^[databricks-autologging-databricks-on-aws.md]

## Overview

Databricks Autologging calls `mlflow.autolog()` to set up automatic tracking when you attach an interactive Python notebook to a Databricks cluster. The default configuration logs model signatures, models, and other information, but you may want to track additional content such as custom parameters, evaluation metrics, or files that autologging does not capture by default. ^[databricks-autologging-databricks-on-aws.md]

## When to Extend Autologged Runs

You need to extend autologged runs when you want to:

- Track custom parameters that are not automatically captured by the model framework.
- Log additional evaluation metrics computed outside the model training loop.
- Record pre-processing steps or data transformations before model training.
- Save custom artifacts or files associated with a training run.
- Add post-training analysis or validation results.

## How to Extend Autologged Runs

### Prerequisites

- An interactive Databricks Python notebook attached to a cluster running Databricks Runtime 10.4 LTS ML or above (or 9.1 LTS ML in select preview regions). ^[databricks-autologging-databricks-on-aws.md]
- [MLflow](/concepts/mlflow.md) installed in your environment.

### Step-by-Step Process

To extend autologged runs with additional content: ^[databricks-autologging-databricks-on-aws.md]

1. **Call `mlflow.autolog()` with `exclusive=False`.** This prevents autologging from creating its own separate run and allows you to log additional content to the same run.

2. **Start an [MLflow Run](/concepts/mlflow-run.md) using `mlflow.start_run()`.** You can wrap this call in `with mlflow.start_run()` to automatically end the run after completion.

3. **Use MLflow Tracking methods** (such as `mlflow.log_param()`) to track pre-training content before model training.

4. **Train one or more machine learning models** in a framework supported by Databricks Autologging.

5. **Use MLflow Tracking methods** (such as `mlflow.log_metric()`) to track post-training content after model training.

6. **If you did not use `with mlflow.start_run()` in Step 2, end the [MLflow Run](/concepts/mlflow-run.md) using `mlflow.end_run()`.**

### Example

The following example demonstrates extending an autologged run with custom parameters and metrics: ^[databricks-autologging-databricks-on-aws.md]

```python
import mlflow

mlflow.autolog(exclusive=False)

with mlflow.start_run():
    # Log pre-training content
    mlflow.log_param("example_param", "example_value")
    
    # <your model training code here>
    # Databricks Autologging automatically logs model parameters, metrics, etc.
    
    # Log post-training content
    mlflow.log_metric("example_metric", 5)
```

## Important Notes

### Autologging Behavior

Databricks Autologging is not applied to runs created using the MLflow fluent API with `mlflow.start_run()`. In those cases, you must explicitly call `mlflow.autolog()` to allow autologged content to be saved to the [MLflow Run](/concepts/mlflow-run.md). Setting `exclusive=False` ensures autologging content is captured within the same run. ^[databricks-autologging-databricks-on-aws.md]

### Supported Content Types

You can use all standard [MLflow Tracking methods](/concepts/mlflow-tracking.md) to extend autologged runs, including:

- `mlflow.log_param()` for parameters
- `mlflow.log_metric()` for metrics
- `mlflow.log_artifact()` for files
- `mlflow.log_dict()` for structured data
- `mlflow.log_figure()` for figures
- `mlflow.set_tag()` for tags

## Use Cases

### Logging Pre-Training Parameters

You can log parameters that define the training configuration, such as learning rates, batch sizes, or data split ratios, before the model training code executes. This allows you to track the full context of each run in [MLflow Tracking](/concepts/mlflow-tracking.md). ^[databricks-autologging-databricks-on-aws.md]

### Logging Post-Training Metrics

After model training completes, you can compute and log additional metrics such as validation accuracy, inference latency, or model size on disk. These metrics help you evaluate model quality beyond what autologging captures. ^[databricks-autologging-databricks-on-aws.md]

### Logging Custom Artifacts

You can save custom plots, configuration files, or preprocessed datasets as artifacts associated with the run. These artifacts can be viewed and downloaded from the [MLflow UI](/concepts/mlflow.md) alongside the automatically logged model files. ^[databricks-autologging-databricks-on-aws.md]

## Related Concepts

- [Databricks Autologging](/concepts/databricks-autologging.md) — Automatic MLflow tracking for model training
- [MLflow Tracking](/concepts/mlflow-tracking.md) — The API for logging parameters, metrics, and artifacts
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizational units for MLflow runs
- MLflow Training Runs — Records of model training sessions
- [Customizing Autologging Configuration](/concepts/mlflowautolog-configuration.md) — Adjusting autologging behavior with `mlflow.autolog()`
- [Security and Data Management for Autologging](/concepts/security-and-data-management-for-autologging.md) — Securing tracked model training information

## Sources

- databricks-autologging-databricks-on-aws.md

# Citations

1. [databricks-autologging-databricks-on-aws.md](/references/databricks-autologging-databricks-on-aws-97e315e8.md)
