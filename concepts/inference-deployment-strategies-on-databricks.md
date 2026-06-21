---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 88a5b1a047e2760e827c407139dc66b7ce4aa10da846bab0304aded87f0ba64b
  pageDirectory: concepts
  sources:
    - best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - inference-deployment-strategies-on-databricks
    - IDSOD
  citations:
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
title: Inference Deployment Strategies on Databricks
description: Options for deploying deep learning models for online serving via Model Serving (custom, foundation, external models), batch inference with Spark Pandas UDFs, and streaming inference
tags:
  - databricks
  - inference
  - model-serving
  - mlflow
timestamp: "2026-06-18T14:33:39.756Z"
---

# Inference Deployment Strategies on Databricks

**Inference Deployment Strategies on Databricks** covers the methods and best practices for deploying trained machine learning models to serve predictions — both in real-time (online) and in high-throughput batch or streaming modes — using the Databricks platform.

## Overview

Databricks provides multiple deployment patterns to match latency, throughput, and cost requirements. The choice depends on model size, expected request volume, and whether the workload is interactive or scheduled. All deployment paths are simplified by [MLflow](/concepts/mlflow.md), which can log any deep learning model, including custom preprocessing and postprocessing logic. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

Models can be registered in [Models in Unity Catalog](/concepts/models-in-unity-catalog.md) or in the [Workspace Model Registry](/concepts/workspace-model-registry.md) and then deployed for batch, streaming, or online inference. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Online Serving

Online serving is the best option for low-latency inference behind a REST API. Databricks provides [Model Serving](/concepts/model-serving.md) for this purpose, offering a unified interface to deploy, govern, and query AI models. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

Model Serving supports three categories of models:

- **Custom models** – Python models packaged in the MLflow format, such as scikit-learn, XGBoost, PyTorch, and Hugging Face transformer models. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]
- **Foundation Model APIs** – State-of-the-art open models that support optimized inference. Base models like Meta-Llama-3.3-70B-Instruct, GTE-Large, and Gemma-3-12B are available with pay-per-token pricing. For workloads requiring performance guarantees and fine-tuned variants, you can deploy with provisioned throughput. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]
- **External models** – Models hosted outside Databricks, such as OpenAI’s GPT-4 and Anthropic’s Claude. Endpoints serving these models can be centrally governed, and administrators can establish rate limits and access control. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

Alternatively, MLflow provides APIs for deploying to various managed services for online inference, as well as APIs for creating Docker containers for custom serving solutions. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Batch and Streaming Inference

Batch and streaming inference supports high-throughput, low-cost scoring at latencies as low as minutes. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

To scale batch and streaming inference across a cluster, use Spark Pandas UDFs. When you log a model from Databricks, MLflow automatically provides inference code to apply the model as a pandas UDF. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Data Preparation for Batch Inference

If data will be accessed more than once for inference, consider creating a preprocessing job to ETL the data into a [Delta Lake](/concepts/delta-lake.md) table before running the inference job. This separates ingestion cost from inference and allows different hardware for each step (e.g., CPUs for ETL and GPUs for inference). ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Best Practices

### GPU Selection for Inference

To minimize costs, consider both CPUs and inference-optimized GPUs such as Amazon EC2 G4 and G5 instances. The best choice depends on model size, data dimensions, and other variables. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Use Delta Lake for Data

Databricks recommends using Delta Lake tables for data storage. Delta Lake simplifies ETL and enables efficient data access for both training and inference. For images, Delta Lake helps optimize ingestion; see the reference solution for image ETL. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Simplify Deployment with MLflow

MLflow can log any deep learning model, including custom preprocessing and postprocessing logic. Models can then be registered in [Unity Catalog](/concepts/unity-catalog.md) or the workspace model registry and deployed to batch, streaming, or online inference endpoints. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Related Concepts

- [MLflow](/concepts/mlflow.md)
- [Model Serving](/concepts/model-serving.md)
- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [Models in Unity Catalog](/concepts/models-in-unity-catalog.md)
- [Workspace Model Registry](/concepts/workspace-model-registry.md)
- Spark Pandas UDFs
- [Delta Lake](/concepts/delta-lake.md)
- Batch Inference
- Online Inference

## Sources

- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md

# Citations

1. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
