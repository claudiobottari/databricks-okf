---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d56749abaa0bb634ca8edd14ca85511452d84590f3590f3c8f276737055b10eb
  pageDirectory: concepts
  sources:
    - best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
    - deep-learning-databricks-on-aws.md
    - distributed-training-databricks-on-aws.md
    - machine-learning-on-databricks-databricks-on-aws.md
    - tensorflow-databricks-on-aws.md
    - train-ai-and-ml-models-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - distributed-training-on-databricks
    - DTOD
    - XGBoost Distributed Training on Databricks
  citations:
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
    - file: distributed-training-databricks-on-aws.md
    - file: tensorflow-databricks-on-aws.md
title: Distributed Training on Databricks
description: Moving from single-node to distributed deep learning training using built-in tools like TorchDistributor, DeepSpeed, and Ray.
tags:
  - distributed-training
  - deep-learning
  - pytorch
  - spark
timestamp: "2026-06-19T17:41:19.467Z"
---

# Distributed Training on Databricks

**Distributed Training on Databricks** refers to the tools and practices for training deep learning models across multiple nodes using Databricks’ managed infrastructure. Databricks provides built‑in libraries such as TorchDistributor, DeepSpeed, and Ray to facilitate the move from single‑node to distributed training. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md] All distributed training should be tracked with **MLflow** for experiment management and reproducibility. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

---

## Available Tools

### TorchDistributor

TorchDistributor is an open‑source module in PySpark that enables distributed training with PyTorch on Spark clusters. It lets you launch PyTorch training jobs as Spark jobs by initializing the environment and communication channels between workers and using the `torch.distributed.run` CLI command. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md, distributed-training-databricks-on-aws.md]

### DeepSpeed

DeepSpeed, developed by Microsoft, is an open‑source library built on top of TorchDistributor. It is recommended for models that require higher compute power but are limited by memory constraints, offering optimized memory usage, reduced communication overhead, and advanced pipeline parallelism. ^[distributed-training-databricks-on-aws.md]

### Ray

Ray is an open‑source framework for parallel computing that scales ML workflows and AI applications. On Databricks, Ray can be used for distributed deep learning training and inference. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md, distributed-training-databricks-on-aws.md]

### TensorFlow `tf.distribute.Strategy`

TensorFlow’s built‑in `tf.distribute.Strategy` API supports single‑node and distributed training on CPUs, GPUs, and clusters of GPUs. Databricks Runtime ML includes TensorFlow and TensorBoard with no additional installation. ^[tensorflow-databricks-on-aws.md] However, TensorFlow will be removed in the next major Databricks Runtime ML version; Databricks recommends installing your own versions as needed. ^[tensorflow-databricks-on-aws.md]

---

## Compute Environments

### Databricks Runtime for Machine Learning

Databricks Runtime for Machine Learning provides a pre‑built deep learning environment with common libraries such as TensorFlow, PyTorch, and Keras, as well as pre‑configured GPU support. It includes all workspace capabilities: cluster creation, library management, Git folders, Jobs, and integrated MLflow. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Single Node Cluster

A [Single Node](https://docs.databricks.com/aws/en/compute/configure#single-node) (driver‑only) GPU cluster is typically the fastest and most cost‑effective choice for deep learning model development. One node with 4 GPUs is likely faster than 4 worker nodes with 1 GPU each because distributed training incurs network communication overhead. Use Single Node clusters for fast iterative development and small‑ to medium‑sized datasets. If your dataset is large enough to make training slow on a single machine, consider moving to multi‑GPU and distributed compute. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### GPU Selection

A100 GPUs are an efficient choice for many deep learning tasks, including training and tuning large language models, natural language processing, object detection and classification, and recommendation engines. Databricks supports A100 GPUs on all clouds. Due to limited availability, contact your cloud provider for resource allocation or reserve capacity in advance. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

---

## Best Practices for Training

### Start with a Single Node Cluster

Begin development on a Single Node cluster before moving to distributed training. This approach is faster for iterative work and reduces complexity. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Monitor with TensorBoard and Cluster Metrics

TensorBoard is pre‑installed in Databricks Runtime ML and can be used within notebooks or in a separate tab. Cluster metrics for network, processor, and memory usage help inspect for bottlenecks. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Optimize Performance

- **Early stopping**: Monitor a validation metric and stop training when improvement ceases. Each deep learning library provides native early‑stopping callbacks (e.g., TensorFlow/Keras `EarlyStopping`, PyTorch Lightning `early_stopping`). ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]
- **Batch size tuning**: Adjust batch size along with learning rate. A common rule: when increasing batch size by *n*, increase learning rate by sqrt(*n*). Try changing batch size by a factor of 2 or 0.5 and use cluster metrics to view GPU utilization. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]
- **Transfer learning**: Start with a pre‑trained model and modify it for your application to significantly reduce training and tuning time. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Move to Distributed Training Only When Necessary

Databricks recommends training neural networks on a single machine whenever possible, because distributed code is more complex and slower due to communication overhead. Consider distributed training only if your model or data are too large to fit in memory on a single machine. ^[distributed-training-databricks-on-aws.md]

### Use Optuna for Hyperparameter Tuning

Optuna provides adaptive hyperparameter tuning and is available in Databricks Runtime ML. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

---

## Related Concepts

- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) – Strategies for very large models requiring FSDP.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) – A serverless GPU configuration for high‑throughput training.
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md) – Detailed notes on A100 availability and use.
- [TorchDistributor](/concepts/torchdistributor.md) – PySpark module for distributed PyTorch training.
- [DeepSpeed](/concepts/deepspeed.md) – Advanced memory optimization for large models.
- Ray – Distributed computing framework on Databricks.
- [MLflow](/concepts/mlflow.md) – Experiment tracking and model management.
- TensorFlow – Deep learning framework with distributed training support.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – Memory‑efficient training for models with 20B+ parameters.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – Simpler parallel training for models fitting on a single GPU.

---

## Sources

- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
- distributed-training-databricks-on-aws.md
- tensorflow-databricks-on-aws.md
- deep-learning-databricks-on-aws.md
- machine-learning-on-databricks-databricks-on-aws.md
- train-ai-and-ml-models-databricks-on-aws.md

# Citations

1. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
2. [distributed-training-databricks-on-aws.md](/references/distributed-training-databricks-on-aws-826bf389.md)
3. [tensorflow-databricks-on-aws.md](/references/tensorflow-databricks-on-aws-9b7ef20f.md)
