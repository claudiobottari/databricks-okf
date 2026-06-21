---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5cb2832e16fd776b473b83788cd5c60412a1c00edf2e9b72dd55ab9049d28759
  pageDirectory: concepts
  sources:
    - databricks-autologging-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - customizing-autologging-with-exclusive-mode
    - CAWEM
  citations:
    - file: databricks-autologging-databricks-on-aws.md
title: Customizing Autologging with Exclusive Mode
description: Technique to track additional metrics and parameters alongside autologged content by calling mlflow.autolog(exclusive=False) combined with explicit MLflow tracking calls
tags:
  - mlflow
  - tracking
  - python-api
  - customization
timestamp: "2026-06-19T09:46:48.009Z"
---

# Customizing Autologging with Exclusive Mode

**Customizing Autologging with Exclusive Mode** refers to configuring Databricks Autologging's `exclusive` parameter to control how automatically captured training runs interact with explicitly created MLflow runs. The exclusive mode determines whether autologged content can be combined with manually logged metrics, parameters, or artifacts within the same run.

## Overview

Databricks Autologging automatically captures model parameters, metrics, files, and lineage information when training models from supported machine learning libraries. The `exclusive` parameter in `mlflow.autolog()` controls the behavior when users also call `mlflow.start_run()` to create explicit runs in their code.^[databricks-autologging-databricks-on-aws.md]

## Exclusive Mode Behavior

When `exclusive=True`, Databricks Autologging creates its own MLflow runs that are separate from any runs created by the user calling `mlflow.start_run()`. This means that automatic logging and manual logging happen in different runs, preventing any mixing of autologged content with user-tracked content.^[databricks-autologging-databricks-on-aws.md]

When `exclusive=False`, autologged content is saved to the same [MLflow Run](/concepts/mlflow-run.md) as content logged by the user via the MLflow fluent API. This configuration allows users to combine automatically captured training information with manually logged metrics, parameters, and artifacts within a single run.^[databricks-autologging-databricks-on-aws.md]

## Default Configuration

The default `mlflow.autolog()` call on Databricks sets `exclusive=False`. This default allows users to track additional content alongside the automatically captured training information by explicitly starting an [MLflow Run](/concepts/mlflow-run.md).^[databricks-autologging-databricks-on-aws.md]

## When to Use Each Mode

### Exclusive Mode (`exclusive=True`)

Use exclusive mode when you want to keep autologged runs completely separate from runs you create manually. This is useful when:

- You want to clearly distinguish automatically captured training details from custom logging
- You need to avoid any accidental interference between automatic and manual logging

### Non-Exclusive Mode (`exclusive=False`)

Use non-exclusive mode when you need to combine automatically captured training metrics with additional manually tracked content in the same [MLflow Run](/concepts/mlflow-run.md). This is the default configuration and is recommended for most use cases.^[databricks-autologging-databricks-on-aws.md]

## Tracking Additional Content with Non-Exclusive Mode

To track additional metrics, parameters, files, or metadata alongside Databricks Autologging content:

1. Call `mlflow.autolog()` with `exclusive=False`.
2. Start an [MLflow Run](/concepts/mlflow-run.md) using `mlflow.start_run()`. You can wrap this call in `with mlflow.start_run():` for automatic cleanup.
3. Use MLflow Tracking methods, such as `mlflow.log_param()`, to track pre-training content.
4. Train one or more machine learning models in a framework supported by Databricks Autologging.
5. Use MLflow Tracking methods, such as `mlflow.log_metric()`, to track post-training content.
6. If you did not use the context manager, end the [MLflow Run](/concepts/mlflow-run.md) using `mlflow.end_run()`.^[databricks-autologging-databricks-on-aws.md]

### Example

```python
import mlflow

mlflow.autolog(exclusive=False)

with mlflow.start_run():
  mlflow.log_param("example_param", "example_value")
  # <your model training code here>
  mlflow.log_metric("example_metric", 5)
```

^[databricks-autologging-databricks-on-aws.md]

## Important Note

Databricks Autologging is not applied to runs created using the MLflow fluent API with `mlflow.start_run()`. In these cases, you must call `mlflow.autolog()` to save autologged content to the [MLflow Run](/concepts/mlflow-run.md). The `exclusive` parameter determines whether the autologged content appears in the same run or a separate run.^[databricks-autologging-databricks-on-aws.md]

## Related Concepts

- [Databricks Autologging](/concepts/databricks-autologging.md) – The overall automatic logging system
- [MLflow Tracking](/concepts/mlflow-tracking.md) – The underlying tracking system for experiments and runs
- MLflow Autolog Function – The function that controls logging behavior
- [Disabling Databricks Autologging](/concepts/databricks-autologging.md) – How to disable automatic logging
- [Track Additional Content](/concepts/tracking-additional-content-with-autologging.md) – Manual logging alongside autologging

## Sources

- databricks-autologging-databricks-on-aws.md

# Citations

1. [databricks-autologging-databricks-on-aws.md](/references/databricks-autologging-databricks-on-aws-97e315e8.md)
