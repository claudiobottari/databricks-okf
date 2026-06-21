---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c53147c4ec6355578664d01f1aa6d41bfa440d47a963d97be9b1284e62584dd7
  pageDirectory: concepts
  sources:
    - databricks-autologging-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - autologging-limitations-and-edge-cases
    - Edge Cases and Autologging Limitations
    - ALAEC
  citations:
    - file: databricks-autologging-databricks-on-aws.md
title: Autologging Limitations and Edge Cases
description: Known constraints of Databricks Autologging, including driver-node-only execution, incompatibility with explicit mlflow.start_run(), and unsupported XGBoost scikit-learn integration.
tags:
  - mlflow
  - limitations
  - databricks
timestamp: "2026-06-19T18:08:27.236Z"
---

# Autologging Limitations and Edge Cases

**Autologging Limitations and Edge Cases** describes the known restrictions, unsupported configurations, and subtle behaviors of [Databricks Autologging](/concepts/databricks-autologging.md) that users should understand to avoid unexpected results when capturing MLflow tracking data from model training sessions.

## Driver Node Only

Databricks Autologging is enabled only on the driver node of a Databricks cluster. To use autologging from worker nodes, you must explicitly call `mlflow.autolog()` from within the code executing on each worker. ^[databricks-autologging-databricks-on-aws.md]

## XGBoost scikit-learn Integration Not Supported

The XGBoost scikit-learn integration is not supported by Databricks Autologging. Users training XGBoost models through the scikit-learn wrapper must log metrics and parameters manually. ^[databricks-autologging-databricks-on-aws.md]

## Serverless Compute

Autologging is **not automatically enabled** on serverless compute. For serverless compute clusters, you must explicitly call `mlflow.autolog()` to enable autologging functionality. ^[databricks-autologging-databricks-on-aws.md]

## Fluent API Runs Not Automatically Captured

Databricks Autologging is not applied to MLflow runs created using the fluent API with `mlflow.start_run()`. In these cases, you must call `mlflow.autolog()` to save autologged content to the run. ^[databricks-autologging-databricks-on-aws.md]

## Workspace-Level Disable Requires Cluster Restart

Administrators can disable Databricks Autologging for all clusters in a workspace from the **Advanced** tab of the admin settings page. However, clusters must be restarted for this change to take effect. ^[databricks-autologging-databricks-on-aws.md]

## Mutual Exclusion with Existing Automated Tracking

Databricks Autologging does not change the behavior of existing automated MLflow tracking integrations for [Apache Spark MLlib](/concepts/apache-spark-mllib.md) and Hyperopt. In Databricks Runtime 10.1 ML, disabling the automated MLflow tracking integration for [Apache Spark MLlib](/concepts/apache-spark-mllib.md) `CrossValidator` and `TrainValidationSplit` models also disables the Databricks Autologging feature for all [Apache Spark MLlib](/concepts/apache-spark-mllib.md) models. ^[databricks-autologging-databricks-on-aws.md]

## [MLflow Tracing](/concepts/mlflow-tracing.md) Not Automatically Enabled

[MLflow Tracing](/concepts/mlflow-tracing.md) for integrations such as OpenAI, LangChain, LlamaIndex, and AutoGen is not automatically enabled by Databricks Autologging. For serverless compute, you must explicitly call the framework-specific `autolog()` method (e.g., `mlflow.openai.autolog()`) with `log_traces=True` to enable tracing. ^[databricks-autologging-databricks-on-aws.md]

## Default Configuration Caveats

The default `mlflow.autolog()` call does not log input examples (`log_input_examples=False`). While this is a design choice rather than a limitation, users who rely on input examples for model understanding must enable this parameter explicitly. ^[databricks-autologging-databricks-on-aws.md]

## Related Concepts

- [MLflow Autologging](/concepts/mlflow-autologging.md) — The underlying open-source feature that Databricks Autologging wraps
- [MLflow Tracking](/concepts/mlflow-tracking.md) — The service where autologged data is stored
- Databricks Autologging Customization — How to modify autologging behavior
- [MLflow Tracing](/concepts/mlflow-tracing.md) — A complementary feature for generative AI workloads
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The runtime version that governs autologging availability

## Sources

- databricks-autologging-databricks-on-aws.md

# Citations

1. [databricks-autologging-databricks-on-aws.md](/references/databricks-autologging-databricks-on-aws-97e315e8.md)
