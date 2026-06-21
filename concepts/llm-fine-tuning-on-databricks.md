---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2a00c009a2f5e1384b399eb2804b9e262fe9027f09ee0a148ff2acd42ddb6571
  pageDirectory: concepts
  sources:
    - ai-runtime-example-notebooks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - llm-fine-tuning-on-databricks
    - LFOD
    - Fine-Tuning in Databricks
    - Fine-tuning on Databricks
    - GPU Fine-tuning on Databricks
    - Fine-tuning LLMs
    - LLM Fine-tuning
    - LLM Fine‑Tuning
    - LLM fine-tuning
  citations:
    - file: ai-runtime-example-notebooks-databricks-on-aws.md
title: LLM fine-tuning on Databricks
description: Notebook examples for fine-tuning large language models on AI Runtime, including parameter-efficient methods.
tags:
  - llm
  - fine-tuning
  - databricks
timestamp: "2026-06-19T17:31:47.926Z"
---

# LLM Fine-tuning on Databricks

**LLM Fine-tuning on Databricks** refers to the adaptation of pre-trained large language models to specific tasks using the Databricks platform. Databricks provides example notebooks that demonstrate how to fine‑tune LLMs, including parameter‑efficient methods, through its AI Runtime. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Overview

AI Runtime for single‑node tasks (including fine‑tuning) is in **Public Preview**. The distributed training API for multi‑GPU workloads remains in **Beta**. The example notebooks cover both single‑node and multi‑GPU fine‑tuning workflows and are available in the Databricks documentation. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Supported Approaches

The provided notebooks include examples for parameter‑efficient fine‑tuning methods. Parameter‑efficient techniques update only a small subset of model parameters while keeping the majority of the pre‑trained weights frozen, reducing memory and compute requirements. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

The notebooks also cover full fine‑tuning and distributed training across multiple GPUs, though the distributed API is still in Beta. ^[ai-runtime-example-notebooks-databricks-on-aws.md]

## Related Concepts

- [AI Runtime](/concepts/ai-runtime.md) – The runtime environment that hosts the fine‑tuning notebooks.
- [Parameter-Efficient Fine-Tuning (PEFT)](/concepts/parameter-efficient-fine-tuning-peft.md) – Methods referenced in the example notebooks.
- [Distributed Training on Databricks](/concepts/distributed-training-on-databricks.md) – Multi‑GPU fine‑tuning capabilities (Beta).
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md) – GPU infrastructure commonly used for LLM workloads.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) – High‑performance GPU configuration for training.
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) – Large‑model training strategies such as FSDP.
- [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md) – Recommended for monitoring fine‑tuning experiments.

## Sources

- ai-runtime-example-notebooks-databricks-on-aws.md

# Citations

1. [ai-runtime-example-notebooks-databricks-on-aws.md](/references/ai-runtime-example-notebooks-databricks-on-aws-09849715.md)
