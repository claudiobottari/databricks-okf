---
title: Distributed training with DeepSpeed distributor | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/train-model/distributed-training/deepspeed
ingestedAt: "2026-06-18T08:13:21.294Z"
---

This article describes how to perform distributed training on PyTorch ML models using the [DeepSpeed distributor](https://github.com/deepspeedai/DeepSpeed).

The DeepSpeed distributor is built on top of [TorchDistributor](https://docs.databricks.com/aws/en/machine-learning/train-model/distributed-training/spark-pytorch-distributor) and is a recommended solution for customers with models that require higher compute power, but are limited by memory constraints.

The [DeepSpeed](https://deepspeed.readthedocs.io/en/latest/training.html) library is an open-source library developed by Microsoft and is available in Databricks Runtime 14.0 ML or above. It offers optimized memory usage, reduced communication overhead, and advanced pipeline parallelism that allow for scaling of models and training procedures that would otherwise be unattainable on standard hardware.

The following are example scenarios where the DeepSpeed distributor is beneficial:

*   Low GPU memory.
*   Large model training.
*   Large input data, like during batch inference.

## Example notebook for distributed training with DeepSpeed[​](#example-notebook-for-distributed-training-with-deepspeed "Direct link to Example notebook for distributed training with DeepSpeed")

The following notebook example demonstrates how to perform distributed training with DeepSpeed distributor.

#### Fine-tune Llama 2 7B Chat with DeepspeedTorchDistributor notebook
