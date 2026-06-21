---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 778c354e17d62b11d8a87cd485aaea9f2a3783e7c227b45c770dfcdc21cd218f
  pageDirectory: concepts
  sources:
    - best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-inference-best-practices-on-databricks
    - MIBPOD
  citations:
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
title: Model Inference Best Practices on Databricks
description: Strategies for online, batch, and streaming inference including MLflow deployment, Model Serving, Foundation Model APIs, external models, and Pandas UDFs.
tags:
  - inference
  - mlflow
  - model-serving
  - databricks
timestamp: "2026-06-19T09:10:02.793Z"
---

# Model Inference Best Practices on Databricks

**Model Inference Best Practices on Databricks** covers proven strategies for deploying trained models to production for low‑latency online serving, high‑throughput batch scoring, and streaming inference. The guidance draws on built‑in tools in [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) and [MLflow](/concepts/mlflow.md), as well as cloud‑specific hardware choices.

## Overview

Inference workloads can be cost‑sensitive and latency‑sensitive. Databricks recommends evaluating both CPUs and inference‑optimized GPUs (such as Amazon EC2 G4 and G5 instances) to minimize costs. The best choice depends on model size, data dimensions, and throughput requirements. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Online Serving (REST API)

For low‑latency serving, the recommended approach is online inference behind a REST API. Databricks [Model Serving](/concepts/model-serving.md) provides a unified interface to deploy, govern, and query AI models. Supported model types include:

- **Custom models** – Python models packaged in MLflow format (e.g., scikit‑learn, XGBoost, PyTorch, Hugging Face transformers).  
- **Foundation Model APIs** – State‑of‑the‑art open models (e.g., Meta‑Llama‑3.3‑70B‑Instruct, GTE‑Large, Gemma‑3‑12B) available with pay‑per‑token pricing or provisioned throughput for performance guarantees.  
- **External models** – Models hosted outside Databricks (e.g., OpenAI GPT‑4, Anthropic Claude), centrally governed with rate limits and access control.  

Alternatively, MLflow provides APIs for deploying to managed services or creating Docker containers for custom serving solutions. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Batch and Streaming Inference

Batch and streaming scoring supports high‑throughput, low‑cost inference at latencies as low as minutes. Key practices include:

- **Separate preprocessing from inference.** If data will be read multiple times, run a preprocessing job to [Delta Lake](/concepts/delta-lake.md) tables before inference. This spreads ingestion cost across reads and allows different hardware for each stage (e.g., CPUs for ETL, GPUs for inference). ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]
- **Use Spark Pandas UDFs** to scale inference across a cluster. When you log a model from Databricks, MLflow automatically generates inference code that applies the model as a pandas UDF. Further optimization is possible for large deep learning models (see the reference solution for image ETL). ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Model Deployment with MLflow

MLflow simplifies the entire deployment lifecycle:

- Log any deep learning model, including custom preprocessing and postprocessing logic.  
- Register models in [Models in Unity Catalog](/concepts/models-in-unity-catalog.md) or the [Workspace Model Registry](/concepts/workspace-model-registry.md) to deploy for batch, streaming, or online inference.  
- Automatic inference code snippets are provided from logged runs, reducing boilerplate. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Hardware Considerations

A100 GPUs are efficient for deep learning inference, especially for large models. However, A100 capacity is often limited; contact your cloud provider or reserve capacity in advance. For many tasks, inference‑optimized GPUs (e.g., G4, G5) can be more cost‑effective. There is no universal recommendation—benchmark on representative data. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Data Preparation for Inference

- Use [Delta Lake](/concepts/delta-lake.md) tables for storage to simplify ETL and improve data throughput.  
- For large datasets that do not fit in memory, employ streaming approaches such as PyTorch IterableDataset, [Hugging Face datasets](/concepts/hugging-face-datasets-on-databricks.md) with streaming, or Ray Data for distributed batch processing. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Monitoring and Performance

- Monitor GPU utilization using cluster metrics to tune batch sizes and avoid under‑utilization.  
- For online endpoints, track latency, throughput, and error rates via [Model Serving monitoring](/concepts/databricks-model-serving-monitoring.md) (available in Databricks).  

## Related Concepts

- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – Pre‑built runtime with GPU support and deep learning libraries.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – Logging experiments and model artifacts.
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md) – Specific guidance for A100 GPUs.
- Spark Pandas UDFs – Scalable inference on Spark.
- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md) – Unified endpoint deployment.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Managed serving of open models.
- [Delta Lake](/concepts/delta-lake.md) – Optimized storage for training and inference data.

## Sources

- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md

# Citations

1. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
