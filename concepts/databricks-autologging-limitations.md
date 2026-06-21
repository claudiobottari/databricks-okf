---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 370c76b3898e81134d9b4dcb6475ad79b6e289de2f98ac59379d356603474a04
  pageDirectory: concepts
  sources:
    - databricks-autologging-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-autologging-limitations
    - DAL
    - Databricks Autologging Customization
  citations:
    - file: databricks-autologging-databricks-on-aws.md
title: Databricks Autologging Limitations
description: Key constraints including that autologging is only enabled on the driver node, must be explicitly enabled on worker nodes, and the XGBoost scikit-learn integration is not supported.
tags:
  - databricks
  - limitations
  - mlflow
timestamp: "2026-06-19T14:44:37.417Z"
---

# Databricks Autologging Limitations

**Databricks Autologging Limitations** refers to the known constraints and restrictions that apply when using Databricks Autologging to automatically capture model parameters, metrics, files, and lineage information during model training sessions.

## Driver Node Only

Databricks Autologging is enabled only on the **driver node** of your Databricks cluster. To use autologging from worker nodes, you must explicitly call `mlflow.autolog()` from within the code executing on each worker.^[databricks-autologging-databricks-on-aws.md]

## XGBoost Scikit-Learn Integration

The XGBoost scikit-learn integration is **not supported** by Databricks Autologging. If you are using XGBoost through its scikit-learn wrapper API, you must manually configure MLflow logging.^[databricks-autologging-databricks-on-aws.md]

## Not Applied to MLflow Fluent API Runs

Databricks Autologging is **not applied** to runs created using the MLflow fluent API with `mlflow.start_run()`. In these cases, you must call `mlflow.autolog()` explicitly to save autologged content to the [MLflow Run](/concepts/mlflow-run.md).^[databricks-autologging-databricks-on-aws.md]

## Serverless Compute

Autologging is **not automatically enabled** on [serverless compute](/concepts/serverless-gpu-compute.md) clusters. For serverless compute, you must explicitly call `mlflow.autolog()` to enable autologging functionality. Similarly, for tracing on serverless compute, you must explicitly enable autologging for the specific framework integration (for example, `mlflow.openai.autolog()` or `mlflow.langchain.autolog()`).^[databricks-autologging-databricks-on-aws.md]

## Cluster Restart Required for Admin Changes

When an administrator enables or disables Databricks Autologging for all clusters in a workspace from the admin settings page, the change does **not** take effect until the cluster is restarted.^[databricks-autologging-databricks-on-aws.md]

## Existing Automated Integrations Unchanged

Databricks Autologging does **not** change the behavior of existing automated MLflow tracking integrations for [Apache Spark MLlib](/concepts/apache-spark-mllib.md) and [Hyperopt](/concepts/hyperopt.md). These integrations continue to work as before.^[databricks-autologging-databricks-on-aws.md]

## Related Concepts

- [Databricks Autologging](/concepts/databricks-autologging.md) — The core feature and its configuration
- [MLflow Automatic Logging](/concepts/mlflow-autologging.md) — The underlying `mlflow.autolog()` function
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Where autologged data is stored
- MLflow Fluent API — The API that bypasses automatic autologging
- Serverless Compute on Databricks — Compute type requiring explicit autologging
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Trace enablement via autolog for supported frameworks

## Sources

- databricks-autologging-databricks-on-aws.md

# Citations

1. [databricks-autologging-databricks-on-aws.md](/references/databricks-autologging-databricks-on-aws-97e315e8.md)
