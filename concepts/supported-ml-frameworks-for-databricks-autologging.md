---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3a6e2704aca9002e08f37bb3f9664fd5f6e885efba2a22342e9ba61a176e6929
  pageDirectory: concepts
  sources:
    - databricks-autologging-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - supported-ml-frameworks-for-databricks-autologging
    - SMFFDA
  citations:
    - file: databricks-autologging-databricks-on-aws.md
title: Supported ML Frameworks for Databricks Autologging
description: The comprehensive list of machine learning frameworks supported by Databricks Autologging including scikit-learn, Apache Spark MLlib, TensorFlow, Keras, PyTorch Lightning, XGBoost, LightGBM, Gluon, Fast.ai, statsmodels, PaddlePaddle, OpenAI, and LangChain.
tags:
  - databricks
  - ml-frameworks
  - machine-learning
timestamp: "2026-06-19T14:44:37.483Z"
---

# Supported ML Frameworks for Databricks Autologging

**Databricks Autologging** automatically captures model parameters, metrics, files, and lineage information when you train models from a variety of popular machine learning libraries. Training sessions are recorded as [MLflow tracking runs](/concepts/mlflow-tracking.md), and model files are tracked for easy logging to the [MLflow Model Registry](/concepts/mlflow-model-registry.md).^[databricks-autologging-databricks-on-aws.md]

## How Autologging Works

When you attach an interactive Python notebook to a Databricks cluster, Databricks Autologging calls `mlflow.autolog()` to automatically set up tracking for model training sessions. The default configuration logs model signatures and models, but does not log input examples by default. You can customize this behavior using [mlflow.autolog()](/concepts/mlflow-autologging.md) parameters.^[databricks-autologging-databricks-on-aws.md]

> **Note:** Autologging is not automatically enabled on serverless compute. For serverless compute clusters, you must explicitly call `mlflow.autolog()` to enable autologging functionality.^[databricks-autologging-databricks-on-aws.md]

## Supported ML Frameworks

Databricks Autologging supports the following ML frameworks in interactive Python notebooks:^[databricks-autologging-databricks-on-aws.md]

### Traditional Machine Learning Frameworks

- **scikit-learn** — Popular library for classical ML algorithms
- **Apache Spark MLlib** — Distributed ML library for Spark
- **XGBoost** — Gradient boosting framework
- **LightGBM** — Gradient boosting framework by Microsoft
- **statsmodels** — Statistical modeling and inference library

### Deep Learning Frameworks

- **TensorFlow** — Google's deep learning framework
- **Keras** — High-level neural networks API
- **PyTorch Lightning** — Lightweight PyTorch wrapper for research and production
- **Gluon** — Apache MXNet's imperative and symbolic deep learning API
- **Fast.ai** — Library simplifying training of neural networks
- **PaddlePaddle** — Baidu's deep learning platform

### Generative AI Frameworks

- **OpenAI** — Supports autologging for OpenAI model calls (via [OpenAI autologging](https://mlflow.org/docs/latest/llms/openai/autologging.html))
- **LangChain** — Framework for developing LLM applications (via [LangChain autologging](https://mlflow.org/docs/latest/llms/langchain/autologging.html))

For detailed information about each supported framework's specific autologging behavior, see the [MLflow automatic logging documentation](/concepts/mlflow-autologging.md).^[databricks-autologging-databricks-on-aws.md]

## [MLflow Tracing](/concepts/mlflow-tracing.md) Support

For generative AI workloads, several framework integrations support tracing via their autolog implementations. To enable tracing, use the framework-specific `autolog()` function with `log_traces=True`. The following integrations support trace enablement:^[databricks-autologging-databricks-on-aws.md]

- **OpenAI** — `mlflow.openai.autolog(log_traces=True)`
- **LangChain** — `mlflow.langchain.autolog(log_traces=True)`
- **LangGraph** — `mlflow.langchain.autolog(log_traces=True)`
- **LlamaIndex** — `mlflow.llama_index.autolog(log_traces=True)`
- **AutoGen** — `mlflow.autogen.autolog(log_traces=True)`

> **Note:** For serverless compute clusters, autologging for tracing is not automatically enabled. You must explicitly enable autologging for the specific framework integrations you want to trace.^[databricks-autologging-databricks-on-aws.md]

## Requirements

- Databricks Autologging is generally available in all regions with Databricks Runtime 10.4 LTS ML or above.^[databricks-autologging-databricks-on-aws.md]
- Available in select preview regions with Databricks Runtime 9.1 LTS ML or above.^[databricks-autologging-databricks-on-aws.md]

## Limitations

- Databricks Autologging is enabled only on the **driver node** of your Databricks cluster. To use autologging from worker nodes, you must explicitly call `mlflow.autolog()` from within the code executing on each worker.^[databricks-autologging-databricks-on-aws.md]
- The **XGBoost scikit-learn integration** is not supported.^[databricks-autologging-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) — The underlying system for recording training runs
- Databricks Autologging Customization — How to modify autologging behavior
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — For managing and deploying logged models
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — ML-optimized runtime versions

## Sources

- databricks-autologging-databricks-on-aws.md

# Citations

1. [databricks-autologging-databricks-on-aws.md](/references/databricks-autologging-databricks-on-aws-97e315e8.md)
