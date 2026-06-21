---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0a8eac60f1314f65f4f66b010893ce3a19c866859c95391ef4c2d6abe21541ca
  pageDirectory: concepts
  sources:
    - fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - fsdp-vs-ddp-distributed-data-parallel
    - FVD(DP
    - DDP (Distributed Data Parallel)
  citations:
    - file: fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md
title: FSDP vs DDP (Distributed Data Parallel)
description: Comparison between FSDP and DDP, where DDP is simpler and recommended for smaller models that fit in a single GPU's memory, while FSDP provides better memory efficiency for large models.
tags:
  - distributed-training
  - comparison
  - deep-learning
timestamp: "2026-06-19T10:40:50.173Z"
---

Here is the wiki page for "FSDP vs DDP (Distributed Data Parallel)" based on the provided source material.

---

## FSDP vs DDP (Distributed Data Parallel)

**FSDP (Fully Sharded Data Parallel)** and **DDP (Distributed Data Parallel)** are two fundamental strategies for distributing deep learning training across multiple GPUs. DDP replicates the full model on every GPU and synchronizes gradients, while FSDP shards model parameters, gradients, and optimizer states across GPUs to reduce per-device memory.

### When to Use Each Strategy

The choice between FSDP and DDP depends primarily on whether the model fits in a single GPU's memory: ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

- **DDP** is the simpler default for models that are small enough to fit entirely within a single GPU's memory. Every GPU holds a complete copy of the model, gradients, and optimizer states. Gradients are averaged across GPUs at each step. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]
- **FSDP** becomes necessary when the model is too large to fit in a single GPU's memory. By sharding (also called "sharding") all three components — parameters, gradients, and optimizer states — across the available GPUs, FSDP reduces the memory footprint per GPU and enables training of models that would otherwise be impossible with DDP. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### Parameter Scale Guidance

- **DDP:** Appropriate for smaller models that fit in one GPU's memory. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]
- **FSDP:** Recommended for [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md). FSDP is the standard choice for training models in the 20B to 120B+ parameter range. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### Memory Efficiency Trade-offs

FSDP offers a better trade-off for memory efficiency compared to DDP. While DDP is simpler to implement for models that fit in a single GPU, it provides no memory efficiency improvements for the model itself. FSDP, by sharding the parameters, can train significantly larger models on the same hardware, but at the cost of additional communication overhead due to the sharding and gathering phases. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### Alternatives

For advanced memory optimization features beyond what FSDP offers, practitioners may consider [DeepSpeed](/concepts/deepspeed.md), which provides additional strategies such as ZeRO optimization stages. ^[fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md]

### Summary Table

| Feature | DDP | FSDP |
|---------|-----|------|
| Model parameters | Replicated on all GPUs | Sharded across GPUs |
| Per-GPU memory | Full model | Reduced (proportional to shard size) |
| Best fit | Small models (fit in one GPU) | Large models (20B+) |
| Complexity | Lower | Higher |
| Communication overhead | Gradient synchronization only | Parameter gather/scatter + gradient sync |

### Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [DeepSpeed](/concepts/deepspeed.md)
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md)
- Large Language Model Training
- GPU Memory Optimization

### Sources

- fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md

# Citations

1. [fully-sharded-data-parallel-fsdp-training-databricks-on-aws.md](/references/fully-sharded-data-parallel-fsdp-training-databricks-on-aws-50fc8f20.md)
