---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6b47bd265231d5b4aaa47f24e9ee98112e2c0e07ee8c34cd77bd119009b0a510
  pageDirectory: concepts
  sources:
    - ai-runtime-example-notebooks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - fine-tuning-large-language-models-with-ai-runtime
    - FLLMWAR
    - Fine-tuning Large Language Models
  citations:
    - file: ai-runtime-example-notebooks-databricks-on-aws.md
title: Fine-tuning large language models with AI Runtime
description: Notebook examples for fine-tuning LLMs on Databricks AI Runtime, including parameter-efficient methods.
tags:
  - databricks
  - llm
  - fine-tuning
timestamp: "2026-06-18T14:23:36.775Z"
---

Here is the wiki page for "Fine-tuning large language models with AI Runtime", based solely on the provided source material.

---

## Fine-tuning large language models with AI Runtime

**Fine-tuning large language models with AI Runtime** refers to the process of adapting a pre-trained LLM to a specific downstream task using the GPU-accelerated capabilities of [AI Runtime for single-node tasks](/concepts/ai-runtime-for-single-node-tasks.md). This involves taking a model that has been trained on a broad corpus and further training it on a smaller, task-specific dataset.

### Overview

AI Runtime provides resources and example notebooks specifically designed for fine-tuning large language models. These examples cover a range of techniques, with a particular emphasis on [parameter-efficient fine-tuning methods](/concepts/parameter-efficient-fine-tuning-peft.md). These methods allow for task adaptation by updating only a small fraction of the model's parameters, which significantly reduces the computational cost and memory requirements compared to full fine-tuning. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

### Examples and Resources

The primary resource for getting started is the set of example notebooks provided for using AI Runtime with GPUs. These notebooks serve as templates and guides for implementing LLM fine-tuning workflows. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

| Resource | Description |
|----------|-------------|
| [Large language models (LLMs)](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/examples/gpu-llms) | Example notebooks for fine-tuning large language models, including parameter-efficient methods. |

### Related Concepts

- [Parameter-efficient fine-tuning](/concepts/parameter-efficient-fine-tuning-peft.md)
- [AI Runtime for single-node tasks](/concepts/ai-runtime-for-single-node-tasks.md)
- [Serverless GPU API](/concepts/serverless-gpu-api.md)
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- [GPU-accelerated machine learning](/concepts/gpu-accelerated-xgboost-training.md)

### Sources

- ai-runtime-example-notebooks-databricks-on-aws.md

# Citations

1. [ai-runtime-example-notebooks-databricks-on-aws.md](/references/ai-runtime-example-notebooks-databricks-on-aws-09849715.md)
