---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b771b128f62f5a82f9a28d10ef08958f94e48792b218805a79b2036ab1b03a3b
  pageDirectory: concepts
  sources:
    - deep-learning-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deep-learning-on-databricks
    - DLOD
    - Deep Learning on Databricks (GPU)
    - Deep Learning Training
  citations:
    - file: deep-learning-databricks-on-aws.md
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
title: Deep Learning on Databricks
description: Overview of using PyTorch, TensorFlow, and distributed training to develop and fine-tune deep learning models on the Databricks platform.
tags:
  - deep-learning
  - databricks
  - machine-learning
timestamp: "2026-06-19T09:58:41.185Z"
---

# Deep Learning on Databricks

**Deep Learning on Databricks** refers to the practice of developing, training, and deploying deep learning models using the Databricks platform, which provides integrated support for popular frameworks like PyTorch and TensorFlow, distributed training capabilities, and experiment tracking through MLflow.

## Overview

Databricks Runtime for Machine Learning (Databricks Runtime ML) includes pre-installed deep learning libraries, GPU support, and tools for building and fine-tuning models ranging from small classifiers to large language models. The platform supports single-node training as well as distributed training across multiple GPUs and nodes. ^[deep-learning-databricks-on-aws.md]

For general guidelines on optimizing deep learning workflows, including GPU selection and configuration, see [Best Practices for Deep Learning on Databricks](/concepts/best-practices-for-deep-learning-on-databricks.md). For information about working with large language models and generative AI, see [Large language models and generative AI on Databricks](/concepts/large-language-models-llms-on-databricks.md) and the documentation on building AI agents. ^[deep-learning-databricks-on-aws.md]

## Supported Frameworks

### PyTorch

PyTorch is included in Databricks Runtime ML and provides GPU-accelerated tensor computation and high-level functionalities for building deep learning networks. Users can perform single-node training or distributed training with PyTorch on Databricks. For an end-to-end tutorial notebook using PyTorch and MLflow, see the [MLflow 3 Deep Learning Workflow](/concepts/mlflow-3-deep-learning-workflow.md). ^[deep-learning-databricks-on-aws.md]

### TensorFlow

Databricks Runtime ML includes both TensorFlow and TensorBoard, enabling use of these libraries without installing additional packages. TensorFlow supports deep learning and general numerical computations on CPUs, GPUs, and clusters of GPUs. TensorBoard provides visualization tools to help debug and optimize machine learning and deep learning workflows. See [TensorFlow on Databricks](/concepts/tensorflow-on-databricks.md) for single node and distributed training examples. ^[deep-learning-databricks-on-aws.md]

## Distributed Training

Because deep learning models are data- and computation-intensive, distributed training is important for many workloads. Databricks supports distributed deep learning through integrations with:

- **Ray** — A unified framework for distributed computing
- **TorchDistributor** — A native PyTorch distributed training utility
- **DeepSpeed** — A deep learning optimization library for large model training

For examples of distributed training, see [Distributed Training on Databricks](/concepts/distributed-training-on-databricks.md). ^[deep-learning-databricks-on-aws.md]

For training large models in the 20B to 120B+ parameter range, [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) is the recommended approach. FSDP shards model parameters, gradients, and optimizer states across multiple GPUs to overcome single-GPU memory limitations. ^[deep-learning-databricks-on-aws.md, fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

## Experiment Tracking

Tracking remains a cornerstone of the MLflow ecosystem and is especially vital for the iterative nature of deep learning. Databricks uses [MLflow](/concepts/mlflow.md) to track deep learning training runs and model development, including metrics, parameters, artifacts, and model versions. See [MLflow Tracking](/concepts/mlflow-tracking.md) for more information. ^[deep-learning-databricks-on-aws.md]

## GPU Support

Databricks supports multiple GPU types across all cloud providers for deep learning workloads. [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md) provides high-performance compute for training large language models, natural language processing, object detection and classification, and recommendation engines. A100 GPUs typically have limited capacity in cloud environments, so contacting your cloud provider for resource allocation or reserving capacity in advance is recommended. ^[deep-learning-databricks-on-aws.md, best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Serverless GPU with AI Runtime

For single- and multi-node deep learning workloads, Databricks offers [AI Runtime](/concepts/ai-runtime.md) with serverless GPU capabilities, providing scalable compute without manual infrastructure management. ^[deep-learning-databricks-on-aws.md]

## Related Topics

- [PyTorch on Databricks](/concepts/pytorch-on-databricks.md)
- [TensorFlow on Databricks](/concepts/tensorflow-on-databricks.md)
- [Distributed Training on Databricks](/concepts/distributed-training-on-databricks.md)
- [MLflow Tracking](/concepts/mlflow-tracking.md)
- [Best Practices for Deep Learning on Databricks](/concepts/best-practices-for-deep-learning-on-databricks.md)
- [Large language models and generative AI on Databricks](/concepts/large-language-models-llms-on-databricks.md)
- [AI Runtime](/concepts/ai-runtime.md)
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md)

## Sources

- deep-learning-databricks-on-aws.md
- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md

# Citations

1. [deep-learning-databricks-on-aws.md](/references/deep-learning-databricks-on-aws-50a1d868.md)
2. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
3. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
