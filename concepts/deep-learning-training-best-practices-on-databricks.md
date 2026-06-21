---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f6ecb745b1bb4b907fce949cb11a1642530207a38a367e494beb0d3671c7d883
  pageDirectory: concepts
  sources:
    - best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deep-learning-training-best-practices-on-databricks
    - DLTBPOD
  citations:
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
title: Deep Learning Training Best Practices on Databricks
description: Key training optimization techniques including early stopping, batch size tuning with learning rate adjustment, transfer learning, and moving to distributed training.
tags:
  - training
  - deep-learning
  - optimization
timestamp: "2026-06-19T09:09:58.738Z"
---

# Deep Learning Training Best Practices on Databricks

Deep learning on Databricks benefits from a pre-built infrastructure with **Databricks Runtime for Machine Learning (Databricks Runtime ML)**, which includes common libraries such as TensorFlow, PyTorch, and Keras, along with built-in, pre-configured GPU support including drivers and supporting libraries. It also integrates all Databricks workspace capabilities: cluster management, library and environment management, Git-based code management, jobs and APIs, and MLflow for tracking and deployment.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

This article covers recommended practices for resource and environment management, data loading, training, and inference on Databricks.

## Resource and Environment Management

### Customize the development environment

You can customize your deep learning environment at the notebook, cluster, and job levels:

- Use notebook-scoped Python libraries or [notebook-scoped R libraries](/concepts/compute-scoped-vs-notebook-scoped-library-installation.md) to use specific library versions without affecting other cluster users.
- Install libraries at the cluster level to standardize versions for a team or a project.
- Set up a Databricks job to ensure repeated tasks run in a consistent, unchanging environment.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Use cluster policies

Create cluster policies to guide data scientists toward appropriate choices—for example, using a Single Node cluster for development and an autoscaling cluster for large jobs.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Consider A100 GPUs

For training and tuning large language models, natural language processing, object detection and classification, and recommendation engines, **A100 GPUs** are an efficient choice. Databricks supports A100 GPUs on all clouds. Because A100 GPUs often have limited availability, contact your cloud provider for resource allocation or consider reserving capacity in advance.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### GPU scheduling

To maximize GPU utilization for distributed deep learning training and inference, optimize GPU scheduling.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Best Practices for Loading Data

Cloud storage is typically not optimized for I/O, which can be a bottleneck for large deep learning datasets. Databricks Runtime ML includes [Delta Lake](/concepts/delta-lake.md) to optimize data throughput. Databricks recommends using Delta Lake tables for data storage; Delta Lake simplifies ETL and improves access efficiency, especially for images. The reference solution for image applications provides an example of optimizing ETL for images with Delta Lake.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

For very large datasets that do not fit in memory, use streaming approaches:

- PyTorch IterableDataset for custom streaming logic.
- [Hugging Face datasets](/concepts/hugging-face-datasets-on-databricks.md) with streaming for datasets hosted on the Hub or in volumes.
- Ray Data for distributed batch data processing.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Best Practices for Training Deep Learning Models

Databricks recommends using Databricks Runtime for Machine Learning and [MLflow Tracking](/concepts/mlflow-tracking.md) with [autologging](/concepts/mlflow-autologging.md) for all model training.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Start with a Single Node cluster

A Single Node (driver only) GPU cluster is typically fastest and most cost-effective for deep learning model development. One node with 4 GPUs is likely faster than 4 worker nodes with 1 GPU each because distributed training incurs network communication overhead. Use a Single Node cluster during fast, iterative development and for training on small- to medium-size data. If your dataset is large enough to slow single-machine training, consider moving to multi-GPU or distributed compute.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Use TensorBoard and cluster metrics

[TensorBoard](/concepts/tensorboard-on-databricks.md) is preinstalled in Databricks Runtime ML and can be used within a notebook or in a separate tab. Cluster metrics (network, processor, memory usage) are available in all Databricks runtimes to inspect for bottlenecks.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Optimize performance

#### Early stopping

Early stopping monitors a validation metric and halts training when improvement stops. Use the native API from your deep learning library—for example, the EarlyStopping callback in TensorFlow/Keras or the [PyTorch Lightning](/concepts/pytorch-lightning-for-ddp.md) early stopping callback.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

#### Batch size tuning

Tune batch size to optimize GPU utilization. If the batch size is too small, the GPU is underused. Adjust batch size together with learning rate: when you increase batch size by `n`, increase learning rate by `sqrt(n)`. Try changing batch size by a factor of 2 or 0.5, then continue tuning manually or with an automated tool like [Optuna](/concepts/optuna.md).^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

#### Transfer learning

Start with a previously trained model and modify it for your application. Transfer learning can significantly reduce training and tuning time. See [Featurization for Transfer Learning](/concepts/featurization-for-transfer-learning.md) for details and an example.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Move to distributed training

Databricks Runtime ML includes [TorchDistributor](/concepts/torchdistributor.md), [DeepSpeed](/concepts/deepspeed.md), and Ray to facilitate the move from single-node to distributed training.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

- **TorchDistributor**: An open-source PySpark module that launches PyTorch training jobs as Spark jobs. See Distributed training with TorchDistributor.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]
- **Optuna**: Provides adaptive hyperparameter tuning for machine learning.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Best Practices for Inference

### Online serving

For low-latency serving behind a REST API, the best option is online serving. Databricks [Model Serving](/concepts/model-serving.md) provides a unified interface to deploy, govern, and query AI models. It supports:

- **Custom models**: Python models in MLflow format, such as scikit-learn, XGBoost, PyTorch, and Hugging Face transformers.
- **Foundation Model APIs**: State-of-the-art open models (e.g., Meta-Llama-3.3-70B-Instruct, GTE-Large, Gemma-3-12B) with pay-per-token pricing; for workloads requiring performance guarantees, use provisioned throughput.
- **External models**: Models hosted outside Databricks, such as GPT-4 and Claude, with central governance and rate limits.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

Alternatively, MLflow provides APIs for deploying to various managed services and for creating Docker containers for custom serving.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Batch and streaming inference

Batch and streaming scoring supports high-throughput, low-cost inference with latencies as low as minutes. See [Deploy models for batch inference and prediction](/concepts/batch-inference-pipelines.md).^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

- If data will be accessed for inference multiple times, create a preprocessing job to ETL data into a [Delta Lake Table](/concepts/delta-lake-table.md) before inference. This spreads the cost of ingestion across reads and allows different hardware for ETL (CPUs) and inference (GPUs).
- Use Spark Pandas UDFs to scale batch and streaming inference across a cluster. When you log a model from Databricks, MLflow automatically provides inference code to apply the model as a Pandas UDF. For large deep learning models, further optimize your pipeline—see the reference solution for image ETL.^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Sources

- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md

# Citations

1. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
