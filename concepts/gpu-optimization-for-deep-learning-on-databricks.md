---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7838bf27784aac9d5a2bf4b4ea5e6307965935a0ade54948c6bc8fb34d47e840
  pageDirectory: concepts
  sources:
    - best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gpu-optimization-for-deep-learning-on-databricks
    - GOFDLOD
  citations:
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
title: GPU Optimization for Deep Learning on Databricks
description: Best practices for GPU selection (including A100 GPUs), GPU scheduling, and leveraging Single Node GPU clusters for cost-effective deep learning development.
tags:
  - gpu
  - optimization
  - databricks
timestamp: "2026-06-19T09:09:50.158Z"
---

# GPU Optimization for Deep Learning on Databricks

**GPU Optimization for Deep Learning on Databricks** encompasses best practices for selecting, configuring, and utilizing GPU resources to maximize performance and cost-efficiency when training and deploying deep learning models on the Databricks platform.

## Overview

Databricks provides pre-built deep learning infrastructure with [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md), which includes common deep learning libraries like TensorFlow, PyTorch, and Keras, along with built-in, pre-configured GPU support including drivers and supporting libraries. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## GPU Selection

### A100 GPUs

NVIDIA A100 GPUs are an efficient choice for many deep learning tasks, including training and tuning large language models, natural language processing, object detection and classification, and recommendation engines. Databricks supports A100 GPUs on all cloud providers. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Availability Considerations

A100 GPUs usually have limited capacity in cloud environments. Databricks recommends contacting your cloud provider for resource allocation or reserving capacity in advance to ensure availability for workloads. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Inference-Optimized GPUs

To minimize costs during inference, consider inference-optimized GPUs such as Amazon EC2 G4 and G5 instances. There is no clear universal recommendation, as the best choice depends on model size, data dimensions, and other variables. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Cluster Configuration

### Single Node Clusters

A [Single Node GPU cluster](/concepts/single-node-gpu-clusters-for-deep-learning.md) (driver only) is typically fastest and most cost-effective for deep learning model development. One node with 4 GPUs is likely to be faster than 4 worker nodes with 1 GPU each, because distributed training incurs network communication overhead. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

Single Node clusters are a good option during fast, iterative development and for training models on small- to medium-size data. If your dataset is large enough to make training slow on a single machine, consider moving to multi-GPU and distributed compute. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### GPU Scheduling

To maximize your GPUs for distributed deep learning training and inference, optimize GPU scheduling. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Cluster Policies

You can create cluster policies to guide data scientists toward appropriate GPU configurations, such as using a Single Node cluster for development and an autoscaling cluster for large jobs. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Performance Optimization Techniques

### Batch Size Tuning

Batch size tuning helps optimize GPU utilization. If the batch size is too small, the calculations cannot fully use the GPU capabilities. Use cluster metrics to view GPU metrics and adjust accordingly. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

Adjust batch size in conjunction with the learning rate. A good rule of thumb: when increasing batch size by \(n\), increase the learning rate by \(\sqrt{n}\). When tuning manually, try changing batch size by a factor of 2 or 0.5. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Early Stopping

Early stopping monitors a metric calculated on the validation set and stops training when the metric stops improving, saving GPU compute resources. Each deep learning library provides a native API for early stopping, such as the EarlyStopping callback in TensorFlow/Keras and PyTorch Lightning. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Transfer Learning

[Transfer Learning](/concepts/transfer-learning.md) starts with a previously trained model and modifies it for your application, significantly reducing the time required to train and tune a new model on GPUs. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Monitoring GPU Performance

### TensorBoard

[TensorBoard](/concepts/tensorboard-on-databricks.md) is preinstalled in Databricks Runtime ML and can be used within a notebook or in a separate tab to monitor training progress. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Cluster Metrics

Cluster metrics are available in all Databricks runtimes and allow you to examine network, processor, and memory usage to inspect for bottlenecks, including GPU utilization. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Data Loading for GPU Efficiency

### Delta Lake for I/O Optimization

Cloud data storage is typically not optimized for I/O, which can be a challenge for deep learning models that require large datasets. Databricks Runtime ML includes [Delta Lake](/concepts/delta-lake.md) to optimize data throughput for deep learning applications. Databricks recommends using Delta Lake tables for data storage to simplify ETL and access data efficiently. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Streaming Approaches for Large Datasets

For very large datasets that do not fit in memory, use streaming approaches to avoid GPU idle time:
- PyTorch IterableDataset for custom streaming logic
- [Hugging Face datasets](/concepts/hugging-face-datasets-on-databricks.md) with streaming for datasets hosted on the Hub or in volumes
- Ray Data for distributed batch data processing

^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Moving to Distributed Training

When a dataset is large enough to make single-machine training slow, transition to distributed training. Databricks Runtime ML includes [TorchDistributor](/concepts/torchdistributor.md), [DeepSpeed](/concepts/deepspeed.md), and Ray to facilitate this transition. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

- [TorchDistributor](/concepts/torchdistributor.md) is an open-source module in PySpark that facilitates distributed training with PyTorch on Spark clusters, allowing you to launch PyTorch training jobs as Spark jobs. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]
- [Optuna](/concepts/optuna.md) provides adaptive hyperparameter tuning that can help optimize GPU utilization across distributed setups. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Inference Optimization

### Online Serving

The best option for low-latency serving is online serving behind a REST API. Databricks [Model Serving](/concepts/model-serving.md) supports custom models in MLflow format, state-of-the-art open models via [Foundation Model APIs](/concepts/foundation-model-apis.md), and externally hosted models. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Batch Inference

For batch and streaming scoring, separate preprocessing from inference to allow selecting different hardware for each job. Use CPUs for ETL and GPUs for inference to optimize cost and performance. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

Use Spark Pandas UDFs to scale batch and streaming inference across a cluster. When you log a model from Databricks, MLflow automatically provides inference code to apply the model as a pandas UDF. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Environment Customization

You can customize the development environment at multiple levels:
- Use notebook-scoped Python libraries for specific library versions without affecting other cluster users
- Install libraries at the cluster level to standardize versions for a team or project
- Set up Databricks jobs to ensure repeated tasks run in consistent environments

^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- GPU Scheduling
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- [Model Serving](/concepts/model-serving.md)
- [Delta Lake](/concepts/delta-lake.md)
- [MLflow Tracking](/concepts/mlflow-tracking.md)

## Sources

- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md

# Citations

1. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
