---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1dda2536869ba0264cc0cbbd5d88f556daa41e5a06b19cfa86cb94ff770979b6
  pageDirectory: concepts
  sources:
    - distributed-training-using-deepspeed-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-ai-runtime-for-distributed-training
    - DARFDT
  citations:
    - file: distributed-training-using-deepspeed-databricks-on-aws.md
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
title: Databricks AI Runtime for Distributed Training
description: A Databricks platform runtime that supports distributed training frameworks including DeepSpeed, DDP, and FSDP on AWS.
tags:
  - databricks
  - machine-learning
  - platform
timestamp: "2026-06-19T10:18:11.363Z"
---

Here is the wiki page for **Databricks AI Runtime for Distributed Training**, based solely on the provided source material and written in the requested style.

---

## Databricks AI Runtime for Distributed Training

**Databricks AI Runtime for Distributed Training** provides built-in support and notebooks for running distributed deep learning workloads across GPU clusters. The runtime supports multiple data-parallel training paradigms, including [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md), [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md), and [DeepSpeed](/concepts/deepspeed.md).

The AI Runtime is pre-configured with PyTorch and other common deep learning libraries, enabling users to launch distributed jobs without manually configuring core libraries. Databricks recommends selecting a training method based on model size and memory requirements, and provides reference notebooks for each approach. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

## Supported Training Strategies

### DeepSpeed

The AI Runtime includes DeepSpeed, a library that provides advanced memory optimization through its ZeRO (Zero Redundancy Optimizer) stages. DeepSpeed enables efficient training of large models ranging from 1 billion to over 100 billion parameters. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

Use DeepSpeed when:
- You need advanced memory optimization beyond standard FSDP.
- You want fine-grained control over optimizer state sharding via ZeRO Stage 1, 2, or 3.
- You require additional features like gradient accumulation fusion or CPU offloading. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

### FSDP (Fully Sharded Data Parallel)

The runtime supports PyTorch-native FSDP for training large models that cannot fit into the memory of a single GPU. FSDP shards model parameters, gradients, and optimizer states across GPUs. This approach is typically used for models in the 20B to 120B+ parameter range. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### DDP (Distributed Data Parallel)

For models that fit within a single GPU's memory, the runtime supports standard DDP. This approach is simpler to implement than FSDP but offers no memory efficiency improvements for the model itself. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### A100 GPU Support

The AI Runtime supports A100 GPUs across all cloud providers, which are considered efficient for deep learning tasks such as LLM training, NLP, and recommendation engines. However, A100 GPUs typically have limited capacity in cloud environments, so users should contact their cloud provider or reserve capacity in advance. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Selecting a Training Strategy

Databricks provides the following guidance for choosing a strategy:

| Strategy | Best For |
|----------|----------|
| DDP | Simpler use cases; models that fit in a single GPU |
| FSDP | Standard large model training (20B to 120B+ parameters) |
| DeepSpeed | Advanced memory optimization; models from 1B to 100B+ parameters; when features like CPU offloading are needed |

For simpler use cases, consider DDP. For PyTorch-native large model training, use FSDP. For models requiring more sophisticated memory optimization beyond what FSDP offers, use DeepSpeed. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

## Availability

A100 GPU instances are available across all major clouds (AWS, Azure, GCP). For the complete list of supported GPU instance types, see the Databricks documentation on supported instance types. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [DeepSpeed](/concepts/deepspeed.md)
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md)
- [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md)
- GPU Scheduling

## Sources

- distributed-training-using-deepspeed-databricks-on-aws.md
- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md

# Citations

1. [distributed-training-using-deepspeed-databricks-on-aws.md](/references/distributed-training-using-deepspeed-databricks-on-aws-9ac82396.md)
2. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
3. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
