---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f5a9dc588d70edba40fc21ac8024a81ae19a46e479392b708a91c37b3fd8e6d5
  pageDirectory: concepts
  sources:
    - ai-runtime-example-notebooks-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - parameter-efficient-fine-tuning-peft-for-llms
    - PF(FL
  citations:
    - file: ai-runtime-example-notebooks-databricks-on-aws.md
title: Parameter-Efficient Fine-Tuning (PEFT) for LLMs
description: Techniques for fine-tuning large language models with fewer computational resources by updating only a subset of model parameters, as demonstrated in Databricks AI Runtime notebooks.
tags:
  - machine-learning
  - large-language-models
  - fine-tuning
timestamp: "2026-06-19T13:58:07.747Z"
---

# Parameter-Efficient Fine-Tuning (PEFT) for LLMs

**Parameter-Efficient Fine-Tuning (PEFT)** refers to a set of techniques that adapt large language models (LLMs) to downstream tasks by updating only a small fraction of the model’s total parameters while keeping the vast majority frozen. This approach drastically reduces the memory and compute required for fine-tuning, making it feasible to customize LLMs on modest hardware. Common PEFT methods include LoRA, Adapters, Prefix Tuning, and Prompt Tuning.

## Databricks Support

Databricks provides example notebooks for fine-tuning large language models, including parameter-efficient methods, as part of the AI Runtime. These examples demonstrate how to apply PEFT techniques within the Databricks environment, leveraging GPU acceleration for efficient training. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

The AI Runtime for single-node tasks is in **Public Preview**, while the distributed training API for multi-GPU workloads remains in **Beta**. Users can access the LLM-related notebook examples under the [Large language models (LLMs)] section of the AI Runtime examples gallery. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) – The Databricks environment that provides pre-configured GPU clusters and optimized libraries for deep learning.
- [LoRA (Low-Rank Adaptation)](/concepts/lora-low-rank-adaptation.md) – A popular PEFT technique that injects trainable low-rank matrices into the model.
- Fine-Tuning in Databricks – General guidance for adapting pre‑trained models on the platform.
- GPU-Accelerated Training on Databricks – Using GPUs for efficient fine-tuning.

## Sources

- ai-runtime-example-notebooks-databricks-on-aws.md

# Citations

1. [ai-runtime-example-notebooks-databricks-on-aws.md](/references/ai-runtime-example-notebooks-databricks-on-aws-09849715.md)
