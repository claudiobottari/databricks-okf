---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ca3522f8ee67be771d133d4f4afa79d5e7207d2fc5579a9a19b4f87f384fcedb
  pageDirectory: concepts
  sources:
    - large-language-models-llms-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributed-multi-gpu-training-for-llms
    - DMTFL
  citations:
    - file: large-language-models-llms-databricks-on-aws.md
title: Distributed Multi-GPU Training for LLMs
description: Training approach that distributes LLM workloads across multiple GPUs using Databricks' distributed training API
tags:
  - machine-learning
  - distributed-training
  - gpu
  - databricks
timestamp: "2026-06-19T19:11:52.724Z"
---

## Distributed Multi-GPU Training for LLMs

**Distributed Multi-GPU Training for LLMs** refers to the practice of scaling large language model (LLM) training across multiple graphics processing units (GPUs) to reduce training time and accommodate model sizes that exceed single-device memory. On Databricks, this training is supported through a dedicated API for multi-GPU workloads.

## Databricks Support

Databricks provides two tiers of GPU compute for LLM fine-tuning:

- **AI Runtime for single-node tasks** is in **Public Preview**. It supports workloads that fit within the memory of a single GPU node, using optimized libraries and notebook examples.
- **The distributed training API for multi-GPU workloads** remains in **Beta**. This API enables users to distribute model training across multiple GPUs, which is essential for large-scale fine-tuning of LLMs.

These tools are part of the Databricks AI Runtime, which includes curated notebook examples for various fine-tuning approaches. ^[large-language-models-llms-databricks-on-aws.md]

## Supported Techniques

The provided notebook examples demonstrate two main fine-tuning strategies:

- **Parameter-Efficient Fine-Tuning**: Low-Rank Adaptation (LoRA) is available, allowing efficient adaptation of large models by training only a small set of additional parameters.
- **Full Supervised Fine-Tuning**: Complete retraining of all model parameters on a labeled dataset, requiring more GPU memory and compute.

Both methods can be run on multi-GPU configurations using the distributed training API. ^[large-language-models-llms-databricks-on-aws.md]

## Video Demo

A video walkthrough of the "Fine-tune Llama-3.2-3B with Unsloth" example notebook is available, providing a step-by-step guide to multi-GPU fine-tuning on Databricks. ^[large-language-models-llms-databricks-on-aws.md]

## Related Concepts

- [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md)
- Fine-tuning
- [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md)
- [AI Runtime](/concepts/ai-runtime.md)
- Public Preview
- Beta

## Sources

- large-language-models-llms-databricks-on-aws.md

# Citations

1. [large-language-models-llms-databricks-on-aws.md](/references/large-language-models-llms-databricks-on-aws-bfc38cd2.md)
