---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 37ee1399322a1df27efc7f332534ba12550942fda8fd1a883e53e441dffa1a5e
  pageDirectory: concepts
  sources:
    - databricks-autologging-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - supported-ml-frameworks-for-autologging
    - SMFFA
    - supported-frameworks-for-databricks-autologging
    - SFFDA
    - supported-ml-frameworks-for-databricks-autologging
    - SMFFDA
  citations:
    - file: databricks-autologging-databricks-on-aws.md
title: Supported ML Frameworks for Autologging
description: The list of machine learning frameworks compatible with Databricks Autologging, including scikit-learn, TensorFlow, PyTorch Lightning, XGBoost, and others.
tags:
  - machine-learning
  - frameworks
  - mlflow
  - compatibility
timestamp: "2026-06-19T18:08:20.157Z"
---

Here is the wiki page for "Supported ML Frameworks for Autologging".

---

## Supported ML Frameworks for Autologging

**Supported ML Frameworks for Autologging** refers to the set of machine learning and deep learning libraries for which [Databricks Autologging](/concepts/databricks-autologging.md) can automatically capture model parameters, metrics, files, and lineage information. When you train a model from a supported framework in an interactive Python notebook on a Databricks cluster, the training session is automatically recorded as an [MLflow Tracking](/concepts/mlflow-tracking.md) run. ^[databricks-autologging-databricks-on-aws.md]

### Available Frameworks

Autologging is available for the following ML frameworks:

- scikit-learn
- [Apache Spark MLlib](/concepts/apache-spark-mllib.md)
- TensorFlow
- Keras
- [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md)
- [XGBoost](/concepts/xgboostspark-module.md)
- LightGBM
- [Gluon](/concepts/gluonts.md)
- Fast.ai
- statsmodels
- PaddlePaddle
- OpenAI
- LangChain

^[databricks-autologging-databricks-on-aws.md]

### Environment and Compute Support

Databricks Autologging is supported in interactive Python notebooks. It is generally available in all regions with Databricks Runtime 10.4 LTS ML or above, and available in select preview regions with Databricks Runtime 9.1 LTS ML or above. ^[databricks-autologging-databricks-on-aws.md]

Autologging is not automatically enabled on serverless compute. For serverless compute clusters, you must explicitly call `mlflow.autolog()` to enable the functionality. ^[databricks-autologging-databricks-on-aws.md]

### Tracing Support for Generative AI

For generative AI workloads that rely on [MLflow Tracing](/concepts/mlflow-tracing.md), several framework integrations include trace enablement within their autolog implementations. These integrations allow you to control tracing support by calling the framework-specific `autolog()` function with `log_traces=True`. The supported integrations are:

- OpenAI
- LangChain
- LangGraph
- LlamaIndex
- [AutoGen](/concepts/autogen-auto-tracing.md)

^[databricks-autologging-databricks-on-aws.md]

For serverless compute clusters, tracing autologging is not automatically enabled. You must explicitly enable autologging for the specific framework integration you want to trace. ^[databricks-autologging-databricks-on-aws.md]

### Limitations

The following limitations apply to supported frameworks:

- The XGBoost scikit-learn integration is not supported. ^[databricks-autologging-databricks-on-aws.md]
- Autologging is enabled only on the driver node of a Databricks cluster. To use autologging from worker nodes, you must explicitly call `mlflow.autolog()` from within the code executing on each worker. ^[databricks-autologging-databricks-on-aws.md]

### Related Concepts

- [MLflow Automatic Logging](/concepts/mlflow-autologging.md) – Details on each framework's specific autologging behavior.
- [Databricks Autologging](/concepts/databricks-autologging.md) – Overview of configuration, customization, and administration.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – The underlying service that stores autologged run data.
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) – Where autologged models can be logged and managed.
- [OpenAI Autologging](/concepts/mlflow-openai-autolog.md) – Dedicated support for generative AI trace logging.

### Sources

- databricks-autologging-databricks-on-aws.md

# Citations

1. [databricks-autologging-databricks-on-aws.md](/references/databricks-autologging-databricks-on-aws-97e315e8.md)
