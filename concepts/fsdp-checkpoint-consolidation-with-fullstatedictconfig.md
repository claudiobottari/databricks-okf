---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5a56671bf494eb9e339c06528236b93c731713e9902858f9b3a59ff22ff55735
  pageDirectory: concepts
  sources:
    - multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - fsdp-checkpoint-consolidation-with-fullstatedictconfig
    - FCCWF
  citations:
    - file: multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md
title: FSDP Checkpoint Consolidation with FullStateDictConfig
description: A pattern for saving FSDP-sharded models that gathers the full state dict from all ranks onto CPU of rank 0 and writes a consolidated checkpoint (via save_pretrained) to shared storage like Unity Catalog volumes.
tags:
  - distributed-training
  - pytorch
  - model-serialization
timestamp: "2026-06-19T19:48:56.480Z"
---

# FSDP Checkpoint Consolidation with FullStateDictConfig

**FSDP Checkpoint Consolidation with FullStateDictConfig** is a technique used in PyTorch's [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) to gather the full model state from all distributed ranks into a single, consolidated checkpoint on CPU memory. This approach is essential for saving fine-tuned models trained across multiple GPUs and nodes into a format that can be loaded on a single device for inference or further fine-tuning. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

## Overview

When training large language models (LLMs) with FSDP, model parameters are sharded across all GPUs (ranks) to reduce memory footprint. Standard FSDP checkpoints are sharded — each rank saves only its portion of the model — which is not a complete model that can be loaded on a single GPU. The `FullStateDictConfig` enables rank 0 to gather all shards, reconstruct the full state dictionary on CPU, and save it as a consolidated checkpoint. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

## Configuration

The `FullStateDictConfig` is imported from `torch.distributed.fsdp` and configured with two key parameters: ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

```python
from torch.distributed.fsdp import FullStateDictConfig

save_policy = FullStateDictConfig(
    offload_to_cpu=True,
    rank0_only=True
)
```

### Parameters

- **`offload_to_cpu=True`**: When rank 0 gathers the full state dict, it offloads the tensors to CPU memory rather than holding them on the GPU. This prevents out-of-memory errors on rank 0's GPU, especially for large models where the full parameter count exceeds available GPU memory. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]
- **`rank0_only=True`**: Only rank 0 collects the full state dict. Other ranks return an empty state dict, avoiding redundant memory usage and unnecessary communication. This ensures that only one process performs the consolidation and subsequent save operation. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

## Usage Pattern

The consolidation is performed by wrapping the `model.state_dict()` call inside a `FSDP.state_dict_type` context manager: ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

```python
from torch.distributed.fsdp import FSDP, StateDictType

save_policy = FullStateDictConfig(offload_to_cpu=True, rank0_only=True)
with FSDP.state_dict_type(model, StateDictType.FULL_STATE_DICT, save_policy):
    cpu_state = model.state_dict()
```

After gathering the consolidated state dict on rank 0, the checkpoint is saved using the underlying model's `save_pretrained()` method, passing the CPU state dict: ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

```python
if rank == 0:
    os.makedirs(output_dir, exist_ok=True)
    model.module.save_pretrained(output_dir, state_dict=cpu_state)
    tokenizer.save_pretrained(output_dir)
```

## Complete Example from Multi-Node Training

In a multi-node FSDP fine-tuning setup (e.g., Llama-3.1-8B across 16 H100 GPUs on 2 nodes), the checkpoint consolidation completes the training workflow. After the training loop finishes, rank 0 gathers the full state dict to CPU and writes the consolidated checkpoint to a Unity Catalog Volume: ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

```python
save_policy = FullStateDictConfig(offload_to_cpu=True, rank0_only=True)
with FSDP.state_dict_type(model, StateDictType.FULL_STATE_DICT, save_policy):
    cpu_state = model.state_dict()
if rank == 0:
    os.makedirs(output_dir, exist_ok=True)
    model.module.save_pretrained(output_dir, state_dict=cpu_state)
    tokenizer.save_pretrained(output_dir)
    print(f"Saved checkpoint to {output_dir}", flush=True)
```

## Benefits

- **Single-file checkpoint**: The consolidated checkpoint can be loaded on any single GPU, regardless of how many GPUs were used during training. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]
- **CPU offloading**: Avoids GPU OOM errors by gathering the full state dict on CPU rather than GPU memory. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]
- **Minimal communication overhead**: Only rank 0 participates in gathering the full state dict; other ranks remain idle during the operation. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]
- **Compatibility with Hugging Face transformers**: The consolidated state dict can be passed directly to `save_pretrained()`, producing checkpoints compatible with the Hugging Face ecosystem. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

## Considerations

- The consolidation step occurs after training completes and requires all ranks to synchronize (typically via `dist.barrier()`) before proceeding. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]
- `offload_to_cpu=True` requires sufficient CPU RAM on rank 0 to hold the full model parameters. For very large models (e.g., 70B+ parameters), this may require tens to hundreds of GB of CPU memory. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]
- The checkpoint is saved only from rank 0. Ensure that the output directory is accessible from rank 0's filesystem, such as a shared Unity Catalog Volume or a mounted cloud storage path. ^[multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md]

## Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — Simpler alternative that does not require checkpoint consolidation
- torchrun — The launcher used to start multi-process distributed training
- [Large Language Model (LLM) Fine-tuning](/concepts/multi-node-llm-fine-tuning-with-fsdp.md)
- [Multi-Node Distributed Training](/concepts/multi-gpu-distributed-training-api.md)

## Sources

- multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md

# Citations

1. [multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws.md](/references/multi-node-llm-fine-tuning-with-fsdp-databricks-on-aws-d26ca320.md)
