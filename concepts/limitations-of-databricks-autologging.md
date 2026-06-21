---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 94182d5b32eb03676141a60a87937339def5f8059ea8fec6fa813c1a2eca5560
  pageDirectory: concepts
  sources:
    - databricks-autologging-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - limitations-of-databricks-autologging
    - LODA
  citations:
    - file: databricks-autologging-databricks-on-aws.md
title: Limitations of Databricks Autologging
description: Known limitations including driver-node-only execution, unsupported XGBoost scikit-learn integration, and interaction with Spark MLlib and Hyperopt integrations
tags:
  - databricks
  - mlflow
  - limitations
timestamp: "2026-06-19T09:46:53.934Z"
---

# Limitations of Databricks Autologging

**Databricks Autologging** automatically captures model parameters, metrics, files, and lineage information during model training sessions. While it provides seamless tracking for many machine learning workflows, several limitations should be considered when planning your experimentation and production pipelines.

## Scope of Automatic Enablement

Databricks Autologging is enabled only on the **driver node** of a Databricks cluster. If your code executes model training on worker nodes — for example, in distributed training with `SparkTrials` or worker-parallel operations — autologging does **not** automatically capture tracking data from those workers. To use autologging on worker nodes, you must explicitly call `mlflow.autolog()` from within the code executing on each worker. ^[databricks-autologging-databricks-on-aws.md]

## Serverless Compute

Autologging is **not automatically enabled** on serverless compute clusters. For serverless compute, you must explicitly call `mlflow.autolog()` to enable autologging functionality. ^[databricks-autologging-databricks-on-aws.md]

Similarly, for [MLflow Tracing](/concepts/mlflow-tracing.md) on serverless compute, autologging for tracing is not automatically enabled. You must explicitly enable tracing autolog for each framework integration you want to instrument (for example, `mlflow.openai.autolog()` or `mlflow.langchain.autolog()`). ^[databricks-autologging-databricks-on-aws.md]

## Interaction with Explicit MLflow Runs

Databricks Autologging is **not** applied to runs created using the MLflow fluent API with `mlflow.start_run()`. If you explicitly start an [MLflow Run](/concepts/mlflow-run.md), you must call `mlflow.autolog()` to save autologged content to that run. ^[databricks-autologging-databricks-on-aws.md]

To combine autologging with explicit logging, you must call `mlflow.autolog()` with `exclusive=False`. This allows you to use `mlflow.start_run()` alongside autologging, enabling you to track content both before and after model training within the same [MLflow Run](/concepts/mlflow-run.md). ^[databricks-autologging-databricks-on-aws.md]

## Framework-Specific Limitations

### XGBoost scikit-learn Integration

The XGBoost scikit-learn integration is **not supported** by Databricks Autologging. If you train XGBoost models using the scikit-learn wrapper interface, autologging will not capture tracking information. ^[databricks-autologging-databricks-on-aws.md]

### Supported Frameworks

While Databricks Autologging supports many popular ML frameworks (scikit-learn, [Apache Spark MLlib](/concepts/apache-spark-mllib.md), TensorFlow, Keras, PyTorch Lightning, XGBoost, LightGBM, Gluon, Fast.ai, statsmodels, PaddlePaddle, OpenAI, and LangChain), it does **not** support all machine learning libraries. Unsupported frameworks require manual MLflow tracking calls. ^[databricks-autologging-databricks-on-aws.md]

## Relationship with Other Automated Tracking

Databricks Autologging **does not change** the behavior of existing automated MLflow tracking integrations for [Apache Spark MLlib](/concepts/apache-spark-mllib.md) and [Hyperopt](/concepts/hyperopt.md). These integrations continue to operate independently. ^[databricks-autologging-databricks-on-aws.md]

Note that in Databricks Runtime 10.1 ML, disabling the automated MLflow tracking integration for [Apache Spark MLlib](/concepts/apache-spark-mllib.md) `CrossValidator` and `TrainValidationSplit` models also disables Databricks Autologging for all [Apache Spark MLlib](/concepts/apache-spark-mllib.md) models. ^[databricks-autologging-databricks-on-aws.md]

## Administration and Restart Requirements

Administrators can enable or disable Databricks Autologging for all interactive notebook sessions across a workspace from the **Advanced** tab of the admin settings page. However, changes do **not** take effect until the cluster is restarted. ^[databricks-autologging-databricks-on-aws.md]

## Default Configuration Trade-Offs

The default autologging configuration does **not** automatically capture input examples (`log_input_examples=False`). If you need input examples for model understanding or debugging, you must explicitly enable this parameter when calling `mlflow.autolog()`. ^[databricks-autologging-databricks-on-aws.md]

## Related Concepts

- [Databricks Autologging](/concepts/databricks-autologging.md) — Core feature documentation
- [MLflow Tracking](/concepts/mlflow-tracking.md) — How autologged data is stored and managed
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — Where model files can be logged from autologging
- Serverless Compute — Compute environment where autologging is not automatic
- Hyperopt Integration — Automated tracking that operates independently of autologging
- Apache Spark MLlib Integration — Another independent automated tracking integration

## Sources

- databricks-autologging-databricks-on-aws.md

# Citations

1. [databricks-autologging-databricks-on-aws.md](/references/databricks-autologging-databricks-on-aws-97e315e8.md)
