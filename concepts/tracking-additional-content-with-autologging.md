---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ab81dce243c311dd3aa57d48f4d5af237a17539c0781ded86cbe5e6aeca6f60a
  pageDirectory: concepts
  sources:
    - databricks-autologging-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tracking-additional-content-with-autologging
    - TACWA
    - Track Additional Content
  citations:
    - file: databricks-autologging-databricks-on-aws.md
title: Tracking Additional Content with Autologging
description: The pattern and best practice for adding extra metrics, parameters, files, and metadata to MLflow runs created by Databricks Autologging by calling mlflow.autolog() with exclusive=False and wrapping training in an mlflow.start_run() context.
tags:
  - mlflow
  - databricks
  - workflow
  - machine-learning
timestamp: "2026-06-19T14:44:42.448Z"
---

Based on the provided source material, here is the wiki page.

---

## Tracking Additional Content with Autologging

**Tracking Additional Content with Autologging** refers to the process of manually logging custom metrics, parameters, files, and metadata to an [MLflow Run](/concepts/mlflow-run.md) that is automatically created by [Databricks Autologging](/concepts/databricks-autologging.md). This allows users to augment the automatically captured training information with their own specific data.

### Why It Is Needed

Databricks Autologging automatically records model parameters, metrics, files, and lineage information during model training. However, it is not applied to runs created using the [MLflow](/concepts/mlflow.md) fluent API with `mlflow.start_run()`. When a user calls `mlflow.start_run()`, they must also call `mlflow.autolog()` to save autologged content to that [MLflow Run](/concepts/mlflow-run.md). ^[databricks-autologging-databricks-on-aws.md]

### Procedure

To track additional content in an interactive Databricks Python notebook, follow these steps:

1.  **Call** `mlflow.autolog()` with `exclusive=False`.
2.  **Start** an [MLflow Run](/concepts/mlflow-run.md) using `mlflow.start_run()`. This call can be wrapped in a `with mlflow.start_run():` block to automatically end the run upon completion.
3.  **Use** MLflow Tracking methods, such as `mlflow.log_param()`, to track pre-training content.
4.  **Train** one or more machine learning models in a framework supported by Databricks Autologging.
5.  **Use** MLflow Tracking methods, such as `mlflow.log_metric()`, to track post-training content.
6.  **End** the [MLflow Run](/concepts/mlflow-run.md) using `mlflow.end_run()` if a `with mlflow.start_run():` block was not used in Step 2. ^[databricks-autologging-databricks-on-aws.md]

### Example

The following Python code demonstrates the procedure:

```python
import mlflow

mlflow.autolog(exclusive=False)

with mlflow.start_run():
  mlflow.log_param("example_param", "example_value")
  # <your model training code here>
  mlflow.log_metric("example_metric", 5)
```

^[databricks-autologging-databricks-on-aws.md]

### Related Concepts

- [Databricks Autologging](/concepts/databricks-autologging.md)
- [MLflow Tracking](/concepts/mlflow-tracking.md)
- [MLflow Model Registry](/concepts/mlflow-model-registry.md)
- MLflow Autolog API

### Sources

- databricks-autologging-databricks-on-aws.md

# Citations

1. [databricks-autologging-databricks-on-aws.md](/references/databricks-autologging-databricks-on-aws-97e315e8.md)
