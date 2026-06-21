---
title: Multi-GPU distributed training | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-distributed-training
ingestedAt: "2026-06-18T08:08:35.368Z"
---

This page has notebook examples for multi-GPU distributed training using AI Runtime. These examples demonstrate how to scale training across multiple GPUs and nodes for improved performance.

note

Multi-GPU distributed training is supported on H100 GPUs.

## Choose your parallelism technique[​](#choose-your-parallelism-technique "Direct link to Choose your parallelism technique")

When scaling your model training across multiple GPUs, choosing the right parallelism technique depends on your model size, available GPU memory, and performance requirements.

For detailed information about each technique, see [DDP](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-ddp), [FSDP](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-fsdp), and [DeepSpeed](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-deepspeed).

## Example notebooks by technique and framework[​](#example-notebooks-by-technique-and-framework "Direct link to Example notebooks by technique and framework")

The following table organizes example notebooks by the framework/library you're using and the parallelism technique applied. Multiple notebooks may appear in a single cell.

## Get started[​](#get-started "Direct link to get-started")

Use the following tutorials to get started with the serverless GPU Python library for distributed training:
