---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 63ed29a164834efd2f6531686ff8f6fe5dfe9ff6cf7a43ce32fe7b432ca4458c
  pageDirectory: concepts
  sources:
    - distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - apply_fsdp-sharding-pattern
    - ASP
  citations:
    - file: distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
title: apply_fsdp Sharding Pattern
description: A design pattern that applies FSDP sharding to individual transformer layers using fully_shard() before sharding the entire model, enabling distributed training of modular architectures.
tags:
  - pytorch
  - distributed-training
  - design-pattern
timestamp: "2026-06-19T18:36:55.495Z"
---

# apply_fsdp Sharding Pattern

**`apply_fsdp`** is a utility function used in the PyTorch [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) training example on Databricks serverless GPU compute. It applies FSDP sharding to a model by wrapping each transformer layer and then the entire model with `torch.distributed.fsdp.fully_shard`. The function is defined in the tutorial notebook "Distributed training using PyTorch FSDP on serverless GPU compute". ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Purpose

The primary goal of `apply_fsdp` is to enable distributed training of large models that would not fit in a single GPU’s memory. By sharding model parameters, gradients, and optimizer states across multiple GPUs, FSDP reduces the per-GPU memory footprint. The function wraps each individual transformer layer (e.g., `TransformerBlock`) with `fully_shard`, and then applies `fully_shard` to the entire model. This two‑level sharding pattern is typical for transformer architectures. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Function Signature and Behavior

The function is defined as follows:

```python
def apply_fsdp(model, world_size):
    """Apply FSDP to the model"""
    if world_size > 1:
        print("Applying FSDP to model layers...")
        # Apply fsdp to each transformer layer
        for i, layer in enumerate(model.layers):
            fully_shard(layer)
            print(f"Applied FSDP to layer {i}")
        # Apply FSDP to the entire model
        fully_shard(model)
        print("Applied FSDP to entire model")
    else:
        print("Single GPU detected, skipping FSDP setup")
    return model
```

^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

- **Parameters**:
  - `model`: A PyTorch `nn.Module`, expected to have a `.layers` attribute that is an iterable of sub‑modules (e.g., a `ModuleList` of `TransformerBlock`s).
  - `world_size`: An integer representing the total number of GPUs in the distributed environment.
- **Return value**: The same model instance with FSDP sharding applied (if `world_size > 1`), or unchanged if running on a single GPU.

## Usage in the Training Workflow

Inside the distributed training function `run_fsdp_training`, the model is created, moved to the GPU, and then passed to `apply_fsdp`:

```python
model = SimpleTransformer(...).to(device)
model = apply_fsdp(model, world_size)
```

^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

This ensures that all layers are properly sharded before the training loop begins. The function is called from a function decorated with `@distributed`, which provisions the GPUs and sets up the distributed process group. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Context: Model Architecture

`apply_fsdp` is designed for the `SimpleTransformer` class used in the tutorial. That class contains a `ModuleList` of `TransformerBlock` layers. Each `TransformerBlock` includes MultiheadAttention, LayerNorm, and an MLP. The sharding pattern first wraps each block individually (allowing fine‑grained communication scheduling) and then wraps the whole model. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Relation to PyTorch FSDP

The function uses `torch.distributed.fsdp.fully_shard`, which is the newer, simpler API introduced in PyTorch 2.0+ for applying FSDP to a model. Unlike the older `FullyShardedDataParallel` wrapper, `fully_shard` allows composable sharding: each sub‑module can be sharded independently, and the final `fully_shard(model)` call handles the top‑level communication. The `apply_fsdp` pattern exemplifies this composable approach. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## When FSDP Is Skipped

If `world_size` is 1 (i.e., the training runs on a single GPU), the function skips all FSDP wrapping and prints a message. This makes the code safe to run in both single‑GPU and multi‑GPU environments without modification. ^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – Overview of the sharding strategy.
- [fully_shard](/concepts/fully-sharded-data-parallel-fsdp.md) – The PyTorch API used inside `apply_fsdp`.
- SimpleTransformer – The model architecture that `apply_fsdp` is designed for.
- [@distributed Decorator](/concepts/distributed-decorator.md) – The serverless GPU API that provisions GPUs and calls the training function.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – An alternative data‑parallel strategy for smaller models.

## Sources

- distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md

# Citations

1. [distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md](/references/distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws-e728aa55.md)
