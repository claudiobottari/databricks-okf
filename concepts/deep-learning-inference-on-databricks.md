---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5c4e7d8c37070e58b3f7f0f904cc4f7459dad25b89bd3415de3ef71390d33d9f
  pageDirectory: concepts
  sources:
    - best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deep-learning-inference-on-databricks
    - DLIOD
  citations:
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
title: Deep Learning Inference on Databricks
description: Strategies for online, batch, and streaming inference including Model Serving, Pandas UDFs, and considerations for CPU vs GPU selection.
tags:
  - inference
  - model-serving
  - deep-learning
timestamp: "2026-06-19T17:42:15.439Z"
---

# Deep Learning Inference on Databricks

**Deep Learning Inference on Databricks** refers to the set of best practices and built‑in tools for serving predictions from deep learning models at scale using Databricks infrastructure. The platform supports online, batch, and streaming inference, and provides optimized GPU and CPU options to balance latency and cost.

## Overview

Databricks recommends using [MLflow](/concepts/mlflow.md) to simplify model deployment and serving for any deep learning model, including custom preprocessing and postprocessing logic. Models can be registered in the [Workspace Model Registry](/concepts/workspace-model-registry.md) or stored as [Models in Unity Catalog](/concepts/models-in-unity-catalog.md), and then deployed for batch, streaming, or online inference. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

To minimize inference costs, consider both CPUs and inference‑optimized GPUs (e.g., Amazon EC2 G4 and G5 instances). The best choice depends on model size, data dimensions, and other workload variables. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Online Serving

The primary option for low‑latency deep learning inference is online serving behind a REST API. Databricks provides [Model Serving](/concepts/model-serving.md) for this purpose. Model Serving offers a unified interface to deploy, govern, and query AI models and supports three categories of models: ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

- **Custom models** – Python models packaged in the MLflow format, such as PyTorch, Hugging Face transformers, scikit‑learn, and XGBoost.
- **Foundation Model APIs** – State‑of‑the‑art open models (e.g., Meta‑Llama‑3.3‑70B‑Instruct, GTE‑Large, Gemma‑3‑12B) available with pay‑per‑token pricing, or provisioned throughput for fine‑tuned variants.
- **External models** – Models hosted outside Databricks (e.g., OpenAI GPT‑4, Anthropic Claude). Endpoints for these models can be centrally governed with rate limits and access control.

Alternatively, MLflow provides [APIs](https://mlflow.org/docs/latest/python_api/index.html) for deploying to various managed services, and [APIs for creating Docker containers](https://mlflow.org/docs/latest/cli.html#mlflow-models-build-docker) for custom serving solutions. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Batch and Streaming Inference

Batch and streaming scoring support high‑throughput, low‑cost inference at latencies as low as minutes. Key recommendations include: ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

- **Preprocess data into Delta Lake tables** – If the same data will be accessed for inference more than once, run a preprocessing job to ETL the data into a [Delta Lake](/concepts/delta-lake.md) table before inference. This spreads the cost of ingestion across multiple reads and allows different hardware for ETL (e.g., CPUs) and inference (e.g., GPUs).
- **Use Spark Pandas UDFs for scaling** – [Pandas UDFs](/concepts/scalar-iterator-pandas-udfs.md) (user‑defined functions) enable batch and streaming inference across a cluster. When a model is logged from Databricks, MLflow automatically provides inference code to apply the model as a Pandas UDF. The [reference solution for image ETL](https://docs.databricks.com/aws/en/machine-learning/reference-solutions/images-etl-inference) shows how to further optimize inference pipelines for large deep learning models.

## Related Concepts

- [MLflow](/concepts/mlflow.md) – Model tracking, packaging, and deployment framework.
- [Model Serving](/concepts/model-serving.md) – Databricks' unified interface for online inference.
- [Pandas UDFs](/concepts/scalar-iterator-pandas-udfs.md) – User‑defined functions for scaling inference across clusters.
- [Delta Lake](/concepts/delta-lake.md) – Storage layer recommended for efficient data access during inference.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – Pre‑built runtime including deep learning libraries and GPU support.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Curated foundation models available for pay‑per‑token serving.
- [External Models](/concepts/external-models.md) – Hosted models governed centrally through Databricks.

## Sources

- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md

# Citations

1. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
