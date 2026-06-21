---
title: Deep learning | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/train-model/deep-learning
ingestedAt: "2026-06-18T08:13:18.098Z"
---

This article gives a brief introduction to using PyTorch, Tensorflow, and distributed training for developing and fine-tuning deep learning models on Databricks. It also includes links to pages with example notebooks illustrating how to use those tools.

*   For general guidelines on optimizing deep learning workflows on Databricks, see [Best practices for deep learning on Databricks](https://docs.databricks.com/aws/en/machine-learning/train-model/dl-best-practices).
*   For information about working with large language models and generative AI on Databricks, see:
    *   [Build AI agents on Databricks](https://docs.databricks.com/aws/en/agents/).
    *   [Machine learning on Databricks](https://docs.databricks.com/aws/en/machine-learning/).

*   For information and guidance on using serverless GPU with AI Runtime for single and multi-node deep learning workloads, see [AI Runtime](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/).

## PyTorch[​](#pytorch "Direct link to PyTorch")

PyTorch is included in Databricks Runtime ML and provides GPU accelerated tensor computation and high-level functionalities for building deep learning networks. You can perform single node training or distributed training with PyTorch on Databricks. See [PyTorch](https://docs.databricks.com/aws/en/machine-learning/train-model/pytorch). For an end-to-end tutorial notebook using PyTorch and MLflow, see [MLflow 3 deep learning workflow](https://docs.databricks.com/aws/en/mlflow/mlflow3-dl-workflow).

## TensorFlow[​](#tensorflow "Direct link to TensorFlow")

Databricks Runtime ML includes TensorFlow and TensorBoard, so you can use these libraries without installing any packages. TensorFlow supports deep-learning and general numerical computations on CPUs, GPUs, and clusters of GPUs. TensorBoard provides visualization tools to help you debug and optimize machine learning and deep learning workflows. See [TensorFlow](https://docs.databricks.com/aws/en/machine-learning/train-model/tensorflow) for single node and distributed training examples.

## Distributed training[​](#distributed-training "Direct link to Distributed training")

Because deep learning models are data and computation-intensive, distributed training can be important. For examples of distributed deep learning using integrations with Ray, TorchDistributor, and DeepSpeed see [Distributed training](https://docs.databricks.com/aws/en/machine-learning/train-model/distributed-training/).

## Track deep learning model development[​](#track-deep-learning-model-development "Direct link to Track deep learning model development")

Tracking remains a cornerstone of the MLflow ecosystem and is especially vital for the iterative nature of deep learning. Databricks uses MLflow to track deep learning training runs and model development. See [Track model development using MLflow](https://docs.databricks.com/aws/en/mlflow/tracking).
