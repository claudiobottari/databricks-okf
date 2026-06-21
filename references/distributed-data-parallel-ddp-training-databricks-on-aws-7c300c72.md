---
title: Distributed Data Parallel (DDP) training | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-ddp
ingestedAt: "2026-06-18T08:08:32.515Z"
---

This page has notebook examples for using [Distributed Data Parallel (DDP)](https://docs.pytorch.org/docs/stable/nn.html#module-torch.nn.parallel) training on AI Runtime. DDP is the most common parallelism technique for distributed training, where the full model is replicated on each GPU and data batches are split across GPUs.

## When to use DDP[​](#when-to-use-ddp "Direct link to When to use DDP")

Use DDP when:

*   Your model fits completely in a single GPU's memory
*   You want to scale training by increasing data throughput
*   You need the simplest distributed training approach with automatic support in most frameworks

For larger models that don't fit in single GPU memory, consider [FSDP](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-fsdp) or [DeepSpeed](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-deepspeed) instead.

## Examples[​](#examples "Direct link to Examples")

## Training a simple multilayer perceptron (MLP) neural network using PyTorch DDP[​](#training-a-simple-multilayer-perceptron-mlp-neural-network-using-pytorch-ddp "Direct link to training-a-simple-multilayer-perceptron-mlp-neural-network-using-pytorch-ddp")

The following notebook demonstrates distributed training of a simple multilayer perceptron (MLP) neural network using PyTorch's DDP module on Databricks with serverless GPU resources.

#### PyTorch DDP

## Training a two-tower recommender system using PyTorch Lightning[​](#training-a-two-tower-recommender-system-using-pytorch-lightning "Direct link to training-a-two-tower-recommender-system-using-pytorch-lightning")

This notebook demonstrates how to train a two-tower recommendation model using PyTorch Lightning on AI Runtime. PyTorch Lightning provides a high-level interface that automatically handles DDP configuration for multi-GPU training. The example includes data preparation using Mosaic Streaming (MDS) format and distributed training across A10 or H100 GPUs.

See the [Deep learning recommendation examples](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-recommendation) page for the complete notebooks, including:

*   Data preparation and MDS format conversion
*   Two-tower recommender training with PyTorch Lightning
