---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f8452b2000674e3a1e6ad675e19ef2cb52ce30f92e803362987bb467e23c72de
  pageDirectory: concepts
  sources:
    - best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-for-deep-learning-model-management
    - MFDLMM
  citations:
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: MLflow for Deep Learning Model Management
description: Using MLflow for tracking experiments, autologging, model deployment, and model serving for deep learning models on Databricks.
tags:
  - mlflow
  - model-management
  - deep-learning
timestamp: "2026-06-19T17:41:13.545Z"
---

# MLflow for Deep Learning Model Management

**MLflow for Deep Learning Model Management** refers to the use of MLflow as the central platform for tracking, versioning, deploying, and governing deep learning models throughout the machine learning lifecycle. MLflow is integrated into Databricks and provides built-in tools that simplify model development, experiment tracking, and production deployment for deep learning workloads.

## Overview

Databricks Runtime for Machine Learning includes integrated MLflow for model development tracking, deployment, and serving. MLflow is the recommended tool for all model training workflows on Databricks and is used in conjunction with deep learning frameworks like TensorFlow, PyTorch, and Keras. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

MLflow can log any deep learning model, including custom preprocessing and postprocessing logic. Models can be registered in the [Workspace Model Registry](/concepts/workspace-model-registry.md) or in [Models in Unity Catalog](/concepts/models-in-unity-catalog.md) for centralized governance. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Experiment Tracking and Autologging

MLflow tracking enables experiment organization and metric comparison across training runs. The recommended approach for all model training on Databricks is to use both [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) and MLflow tracking with autologging enabled. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

Autologging automatically records parameters, metrics, and model artifacts without requiring explicit logging calls in the training code. This feature is particularly valuable for iterative deep learning development where tracking hyperparameters and results across many experiments is essential. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Model Deployment and Serving

MLflow simplifies deployment and model serving for deep learning models across multiple inference modalities. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Online Serving

For low-latency serving, Databricks provides [Model Serving](/concepts/model-serving.md) for online inference behind a REST API. Model Serving supports:

- **Custom models** packaged in the MLflow format, including PyTorch, TensorFlow, Hugging Face transformers, and other deep learning frameworks.
- **Foundation Model APIs** for state-of-the-art open models such as Meta-Llama-3.3-70B-Instruct, GTE-Large, and Gemma-3-12B, available with pay-per-token pricing or provisioned throughput.
- **External models** hosted outside of Databricks, such as OpenAI's GPT-4 and Anthropic's Claude, which can be centrally governed with rate limits and access control.

^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Batch and Streaming Inference

Batch and streaming scoring supports high-throughput, low-cost inference at latencies as low as minutes. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

When a model is logged from Databricks, MLflow automatically provides inference code to apply the model as a Spark Pandas UDF, enabling scalable batch and streaming inference across a cluster. Separating preprocessing from inference—for example, using CPUs for ETL and GPUs for inference—allows optimizing cost and performance for each stage. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Serverless Workload Management

MLflow can create serverless workloads for production monitoring, synthetic evaluation set generation, and agent evaluation. When a workspace disables the default serverless budget policy, MLflow returns a `403 PERMISSION_DENIED` error. To resolve this, a serverless budget policy must be set on the MLflow experiment using the experiment UI or the `mlflow.set_experiment_tag()` API with the `mlflow.workload_creation_policy_id` tag. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

Users and service principals must have permission to use the budget policy they assign. MLflow will use the specified policy for every serverless workload it creates for that experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Related Concepts

- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – Pre-built runtime with GPU support and MLflow integration.
- [Model Serving](/concepts/model-serving.md) – Online inference platform for deployed MLflow models.
- [Workspace Model Registry](/concepts/workspace-model-registry.md) – Model catalog for versioning and stage transitions.
- [Models in Unity Catalog](/concepts/models-in-unity-catalog.md) – Centralized model governance with Unity Catalog.
- Spark Pandas UDF – Scaling deep learning inference across clusters.
- 403 PERMISSION_DENIED Serverless Budget Policy Error – Troubleshooting serverless budget policy issues.

## Sources

- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
2. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
