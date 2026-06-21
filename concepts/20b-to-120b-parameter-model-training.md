---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9161eaec01dff578fa7d4cef48e48e39e09bbf55b9aa3bbeb73c8bec5ca13255
  pageDirectory: concepts
  sources:
    - fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - 20b-to-120b-parameter-model-training
    - 2T1PMT
    - Large Model Training
    - larger model training
  citations:
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
title: 20B to 120B+ Parameter Model Training
description: The parameter range where FSDP is particularly useful, enabling training of models between 20 billion and 120+ billion parameters
tags:
  - model-scaling
  - large-language-models
  - distributed-training
timestamp: "2026-06-18T12:26:53.977Z"
---

Here is the wiki page for "20B to 120B+ Parameter Model Training", written based solely on the provided source material.

---

## 20B to 120B+ Parameter Model Training

**20B to 120B+ Parameter Model Training** refers to the specific techniques and infrastructure required to train large language models (LLMs) and other deep learning models that contain between 20 billion and over 120 billion parameters. Due to their immense size, these models cannot fit into the memory of a single GPU, requiring specialized distributed training strategies.

### Overview

Training models in the 20B to 120B+ parameter range necessitates advanced memory optimization techniques. Standard data parallelism is often insufficient because even a single copy of the model parameters, gradients, and optimizer states exceeds the memory capacity of a single GPU. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### Recommended Approach: Fully Sharded Data Parallel (FSDP)

The primary recommended approach for training models of this scale is [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md). FSDP shards model parameters, gradients, and optimizer states across multiple GPUs. This sharding significantly reduces the per-GPU memory footprint, enabling the training of very large models that would otherwise be impossible. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

FSDP offers a better trade-off for memory efficiency compared to standard [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md). While DDP is simpler for models that fit in a single GPU, FSDP becomes the necessary choice for models that do not. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### Alternative Approaches

For models that require even more advanced memory optimization features, practitioners may consider alternatives like [DeepSpeed](/concepts/deepspeed.md), which provides additional strategies beyond what FSDP offers out-of-the-box. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### When to Use Each Strategy

- **DDP:** Best suited for models that fit within a single GPU's memory. It is simpler to implement but offers no memory efficiency improvements for the model itself. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]
- **FSDP:** The standard choice for training models in the 20B to 120B+ parameter range to overcome single-GPU memory limitations. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]
- **DeepSpeed:** Considered when more sophisticated memory optimization features beyond FSDP are required. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [DeepSpeed](/concepts/deepspeed.md)
- [Large Language Models (LLMs)](/concepts/large-language-models-llms-on-databricks.md)
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)

### Sources

- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md

# Citations

1. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
