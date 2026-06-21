---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cb8e6bbc7d1a79737eaeda85ecfb6abec7fdf49fea73b47935fbd3939246a74b
  pageDirectory: concepts
  sources:
    - ai-runtime-cli-examples-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-node-fsdp-fine-tuning-on-databricks
    - MFFOD
  citations:
    - file: ai-runtime-cli-examples-databricks-on-aws.md
title: Multi-node FSDP Fine-tuning on Databricks
description: Pattern for supervised fine-tuning of large language models (e.g., Llama-3.1-8B) across multiple nodes (e.g., 16 H100 GPUs on 2 nodes) using PyTorch FSDP and torchrun on Databricks AI Runtime
tags:
  - fine-tuning
  - distributed-training
  - llm
  - fsdp
timestamp: "2026-06-19T22:02:29.454Z"
---

```markdown
---
title: Multi-node FSDP fine-tuning on Databricks
summary: A distributed-training pattern for supervised fine-tuning of Llama-3.1-8B across 16 H100 GPUs (2 nodes) using torchrun and PyTorch Fully Sharded Data Parallel (FSDP), with MLflow logging and Unity Catalog checkpointing.
sources:
  - ai-runtime-cli-examples-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T13:56:32.095Z"
updatedAt: "2026-06-19T13:56:32.095Z"
tags:
  - distributed-training
  - llm-fine-tuning
  - FSDP
  - databricks
aliases:
  - multi-node-fsdp-fine-tuning-on-databricks
  - MFFOD
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 1
---

# Multi-node FSDP Fine-tuning on Databricks

**Multi-node FSDP fine-tuning on Databricks** refers to the practice of fine-tuning large language models across multiple compute nodes using [[Fully Sharded Data Parallel (FSDP)]] in PyTorch, orchestrated via the [[AI Runtime CLI]]. This approach enables training of models that are too large for a single GPU by sharding model parameters, gradients, and optimizer states across GPUs on multiple nodes.

## Overview

The Databricks [[AI Runtime CLI]] provides a built-in example called *Multi-node LLM fine-tuning with FSDP* that demonstrates the full workflow. The example performs supervised fine-tuning of a Llama-3.1-8B model across 16 H100 GPUs spread across 2 nodes (8 GPUs per node). It uses `torchrun` for launch coordination and PyTorch's native FSDP implementation for memory-efficient sharded training. Training artifacts—metrics, model checkpoints, and configuration—are logged to [[MLflow]] and saved to a [[Unity Catalog]] volume. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Example Configuration

| Aspect | Detail |
|--------|--------|
| Model | Llama-3.1-8B |
| GPUs | 16 × H100 (2 nodes, 8 GPUs per node) |
| Parallelism strategy | PyTorch Fully Sharded Data Parallel (FSDP) |
| Launcher | `torchrun` |
| Logging | MLflow |
| Checkpoint destination | Unity Catalog volume |

The workload YAML that defines this pipeline is available as a reference for adapting to other models and cluster sizes. ^[ai-runtime-cli-examples-databricks-on-aws.md]

## Key Technologies

- [[Fully Sharded Data Parallel (FSDP)]] – PyTorch sharding strategy that reduces per-GPU memory footprint.
- torchrun – Elastic launch utility for distributed PyTorch jobs.
- H100 GPU Support on Databricks – The underlying GPU infrastructure used for the workload.
- [[Supervised Fine-Tuning (SFT)]] – The training objective for the example.
- [[AI Runtime CLI]] – The command-line tool used to submit the workload.
- [[MLflow]] – Tracks experiments, metrics, and model versions.
- [[Unity Catalog]] – Governed storage location for checkpoints and datasets.

## Related Concepts

- Multi-node Distributed Training
- FSDP Sharding Strategies
- Llama 3.1
- Single-Node FSDP Fine-tuning
- DeepSpeed Alternatives on Databricks

## Sources

- ai-runtime-cli-examples-databricks-on-aws.md
```

# Citations

1. [ai-runtime-cli-examples-databricks-on-aws.md](/references/ai-runtime-cli-examples-databricks-on-aws-9e5abf7f.md)
