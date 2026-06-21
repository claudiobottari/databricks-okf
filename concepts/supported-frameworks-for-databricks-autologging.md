---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8ea723914d2a65c0b5392963afc04776aa4f1f450c6e8bde4ab0733b5266e6e8
  pageDirectory: concepts
  sources:
    - databricks-autologging-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - supported-frameworks-for-databricks-autologging
    - SFFDA
  citations:
    - file: databricks-autologging-databricks-on-aws.md
title: Supported Frameworks for Databricks Autologging
description: The list of ML frameworks (scikit-learn, Spark MLlib, TensorFlow, Keras, PyTorch Lightning, XGBoost, LightGBM, Gluon, Fast.ai, statsmodels, PaddlePaddle, OpenAI, LangChain) for which Databricks Autologging natively captures training metrics.
tags:
  - mlflow
  - frameworks
  - machine-learning
timestamp: "2026-06-18T11:32:50.665Z"
---

# Supported Frameworks for Databricks Autologging

**Databricks Autologging** automatically captures model parameters, metrics, files, and lineage information during model training in interactive Python notebooks, recording each training session as an [MLflow Tracking](/concepts/mlflow-tracking.md) run. It is enabled by default on Databricks clusters (except serverless compute) via a background call to [`mlflow.autolog()`](https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.autolog). ^[databricks-autologging-databricks-on-aws.md]

## Requirements

- Databricks Autologging is generally available in all regions with **Databricks Runtime 10.4 LTS ML** or above.
- It is available in select preview regions with Databricks Runtime 9.1 LTS ML or above.
- Autologging is **not automatically enabled** on serverless compute. On serverless clusters you must explicitly call `mlflow.autolog()` to enable it. ^[databricks-autologging-databricks-on-aws.md]

## Supported ML Frameworks

Databricks Autologging supports the following machine learning frameworks when used in interactive Python notebooks attached to a compatible cluster: ^[databricks-autologging-databricks-on-aws.md]

| Framework | Notes |
|-----------|-------|
| scikit-learn | |
| [Apache Spark MLlib](/concepts/apache-spark-mllib.md) | See also [Apache Spark MLlib and MLflow Tracking](/concepts/mllib-automated-mlflow-tracking.md). |
| TensorFlow | |
| Keras | |
| PyTorch Lightning | |
| XGBoost | The XGBoost scikit‑learn integration is **not** supported. |
| LightGBM | |
| Gluon | |
| Fast.ai | |
| statsmodels | |
| PaddlePaddle | |
| OpenAI | Automatically logs traces; see [OpenAI Autologging](/concepts/mlflow-openai-autologging.md). |
| LangChain | Automatically logs traces; see LangChain Autologging. |

For detailed information about each framework’s autologging capabilities, see the [MLflow automatic logging documentation](https://mlflow.org/docs/latest/tracking/autolog.html). ^[databricks-autologging-databricks-on-aws.md]

## [MLflow Tracing](/concepts/mlflow-tracing.md) Frameworks (Autolog‑Based)

[MLflow Tracing](/concepts/mlflow-tracing.md) uses the `autolog` mechanism of framework integrations to enable or disable trace capture. The following integrations support trace enablement through their autolog functions: ^[databricks-autologging-databricks-on-aws.md]

- **OpenAI** – `mlflow.openai.autolog(log_traces=True)`
- **LangChain** – `mlflow.langchain.autolog(log_traces=True)`
- **LangGraph** – `mlflow.langchain.autolog(log_traces=True)` (shared with LangChain)
- **LlamaIndex** – `mlflow.llama_index.autolog(log_traces=True)`
- **AutoGen** – `mlflow.autogen.autolog(log_traces=True)`

On serverless compute, tracing autologging is not active by default; you must explicitly call the framework-specific autolog function with `log_traces=True`. ^[databricks-autologging-databricks-on-aws.md]

## Limitations

- Autologging is enabled only on the **driver node** of the cluster. To use it from worker nodes, call `mlflow.autolog()` explicitly in the code running on the workers.
- The XGBoost scikit‑learn integration is **not** supported.
- Databricks Autologging does **not** apply to runs created using the MLflow fluent API (`mlflow.start_run()`). In those cases, call `mlflow.autolog()` explicitly to capture autologged content. ^[databricks-autologging-databricks-on-aws.md]

## Related Concepts

- [Databricks Autologging](/concepts/databricks-autologging.md) – Overview and customization
- [MLflow Tracking](/concepts/mlflow-tracking.md) – The system that stores autologging results
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) – Model lifecycle management
- [OpenAI Autologging](/concepts/mlflow-openai-autologging.md) – Trace logging for OpenAI models
- LangChain Autologging – Trace logging for LangChain/LangGraph models
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) (if applicable)

## Sources

- databricks-autologging-databricks-on-aws.md

# Citations

1. [databricks-autologging-databricks-on-aws.md](/references/databricks-autologging-databricks-on-aws-97e315e8.md)
