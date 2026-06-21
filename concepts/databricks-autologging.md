---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 76316d19500649dc2fe25795f8442e425f4feec1c79f84a6259fc68321c0f77f
  pageDirectory: concepts
  sources:
    - apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
    - databricks-autologging-databricks-on-aws.md
    - hyperparameter-tuning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-autologging
    - Disabling Databricks Autologging
  citations:
    - file: databricks-autologging-databricks-on-aws.md
    - file: apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md
title: Databricks Autologging
description: A Databricks feature that enables automatic MLflow tracking by default on supported runtimes, including MLflow PySpark ML autologging.
tags:
  - databricks
  - mlflow
  - machine-learning
timestamp: "2026-06-19T22:07:14.316Z"
---

# Databricks Autologging

**Databricks Autologging** is a feature that automatically captures model parameters, metrics, files, and lineage information when you train models from a variety of popular machine learning libraries in an interactive Databricks Python notebook. Training sessions are recorded as [MLflow Tracking](/concepts/mlflow-tracking.md) runs, and model files are also tracked so they can be easily logged to the [MLflow Model Registry](/concepts/mlflow-model-registry.md). ^[databricks-autologging-databricks-on-aws.md]

## How It Works

When you attach an interactive Python notebook to a Databricks cluster, Databricks Autologging calls `mlflow.autolog()` to set up tracking for your model training sessions. The default configuration for this call uses the following settings: ^[databricks-autologging-databricks-on-aws.md]

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

You can [customize the autologging configuration](/concepts/mlflowautolog-configuration.md) by calling `mlflow.autolog()` with different parameters. ^[databricks-autologging-databricks-on-aws.md]

Autologging is not automatically enabled on serverless compute. For serverless clusters, you must explicitly call `mlflow.autolog()` to enable the functionality. ^[databricks-autologging-databricks-on-aws.md]

### [MLflow Tracing](/concepts/mlflow-tracing.md) Enablement

[MLflow Tracing](/concepts/mlflow-tracing.md) uses the `autolog` feature within respective model framework integrations to control the enabling or disabling of tracing support for integrations that support tracing. For example, to enable tracing when using a LlamaIndex model, call `mlflow.llama_index.autolog(log_traces=True)`. On serverless compute clusters, tracing autologging must be explicitly enabled for each framework integration (e.g., `mlflow.openai.autolog()` or `mlflow.langchain.autolog()`). Supported integrations with trace enablement include OpenAI, LangChain, LangGraph, LlamaIndex, and AutoGen. ^[databricks-autologging-databricks-on-aws.md]

## Requirements

- Databricks Autologging is generally available in all regions with Databricks Runtime 10.4 LTS ML or above.
- It is available in select preview regions with Databricks Runtime 9.1 LTS ML or above.

^[databricks-autologging-databricks-on-aws.md]

## Usage

To use Databricks Autologging, train a machine learning model in a supported framework using an interactive Databricks Python notebook. Autologging automatically records model lineage information, parameters, and metrics to MLflow Tracking. ^[databricks-autologging-databricks-on-aws.md]

### Customize Logging Behavior

Use `mlflow.autolog()` to configure parameters such as `log_models`, `log_datasets`, `log_input_examples`, `log_model_signatures`, and `silent`. ^[databricks-autologging-databricks-on-aws.md]

### Track Additional Content

When you want to track additional metrics, parameters, files, or metadata in autologged runs, follow these steps: ^[databricks-autologging-databricks-on-aws.md]

1. Call `mlflow.autolog(exclusive=False)`.
2. Start an [MLflow Run](/concepts/mlflow-run.md) with `mlflow.start_run()` (wrap in `with mlflow.start_run()` to auto-end the run).
3. Use MLflow Tracking methods (e.g., `mlflow.log_param()`, `mlflow.log_metric()`) before and after model training.
4. If you did not use the context manager, call `mlflow.end_run()` to close the run.

Example: ^[databricks-autologging-databricks-on-aws.md]

```python
import mlflow
mlflow.autolog(exclusive=False)
with mlflow.start_run():
    mlflow.log_param("example_param", "example_value")
    # <your model training code here>
    mlflow.log_metric("example_metric", 5)
```

Autologging is not applied to runs created using the MLflow fluent API with `mlflow.start_run()` unless you explicitly call `mlflow.autolog()` first. ^[databricks-autologging-databricks-on-aws.md]

### Disable Databricks Autologging

To disable autologging in an interactive notebook, call `mlflow.autolog(disable=True)`. Administrators can disable autologging for all clusters in a workspace from the **Advanced** tab of the admin settings page; clusters must be restarted for the change to take effect. ^[databricks-autologging-databricks-on-aws.md]

## Supported Environments and Frameworks

Databricks Autologging is supported in interactive Python notebooks and works with the following ML frameworks: ^[databricks-autologging-databricks-on-aws.md]

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

For detailed information about each framework, see the [MLflow automatic logging documentation](/concepts/mlflow-autologging.md). ^[databricks-autologging-databricks-on-aws.md]

## Security and Data Management

All model training information tracked with Databricks Autologging is stored in MLflow Tracking and secured by [MLflow Experiment permissions](/concepts/mlflow-experiment-permission-levels-for-apps.md). You can share, modify, or delete this information using the MLflow Tracking API or UI. ^[databricks-autologging-databricks-on-aws.md]

## Administration

Administrators can enable or disable Databricks Autologging for all interactive notebook sessions in a workspace from the **Advanced** tab of the admin settings page. Changes do not take effect until the cluster is restarted. ^[databricks-autologging-databricks-on-aws.md]

## Limitations

- Databricks Autologging is enabled only on the **driver node** of your Databricks cluster. To use autologging from worker nodes, you must explicitly call `mlflow.autolog()` from within the code executing on each worker. ^[databricks-autologging-databricks-on-aws.md]
- The **XGBoost scikit-learn integration** is not supported. ^[databricks-autologging-databricks-on-aws.md]

## [Apache Spark MLlib](/concepts/apache-spark-mllib.md), Hyperopt, and Automated MLflow Tracking

Databricks Autologging does not change the behavior of existing automated MLflow tracking integrations for [Apache Spark MLlib](/concepts/apache-spark-mllib.md) and [Hyperopt](/concepts/hyperopt.md). In Databricks Runtime 10.1 ML, disabling the automated MLflow tracking integration for Spark MLlib `CrossValidator` and `TrainValidationSplit` models also disables Databricks Autologging for all [Apache Spark MLlib](/concepts/apache-spark-mllib.md) models. ^[databricks-autologging-databricks-on-aws.md]

The old MLlib automated MLflow tracking is deprecated on clusters running Databricks Runtime 10.1 ML and above, and is disabled by default on clusters running Databricks Runtime 10.2 ML and above. Databricks recommends using `mlflow.pyspark.ml.autolog()` instead, which is enabled by default with Databricks Autologging. ^[apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md]

## Sources

- databricks-autologging-databricks-on-aws.md
- apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md

# Citations

1. [databricks-autologging-databricks-on-aws.md](/references/databricks-autologging-databricks-on-aws-97e315e8.md)
2. [apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws.md](/references/apache-spark-mllib-and-automated-mlflow-tracking-databricks-on-aws-ff362b6f.md)
