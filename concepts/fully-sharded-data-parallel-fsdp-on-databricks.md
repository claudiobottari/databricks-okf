---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d6a19b57c39993d1f5aa8734013cbe438f097a0bffaeb4c5b337c8a367f6601e
  pageDirectory: concepts
  sources:
    - multi-gpu-workload-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - fully-sharded-data-parallel-fsdp-on-databricks
    - FSDP(OD
    - Fully Sharded Data Parallel (FSDP) training on Databricks
  citations:
    - file: multi-gpu-workload-databricks-on-aws.md
title: Fully Sharded Data Parallel (FSDP) on Databricks
description: Memory-efficient training for large models using PyTorch FSDP, supported by the serverless_gpu @distributed API.
tags:
  - pytorch
  - distributed-training
  - databricks
  - memory-optimization
timestamp: "2026-06-19T19:47:51.781Z"
---

# Fully Sharded Data Parallel (FSDP) on Databricks

**Fully Sharded Data Parallel (FSDP)** is a memory-efficient distributed training technique supported on Databricks through the [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) infrastructure. FSDP shards model parameters, gradients, and optimizer states across multiple GPUs, drastically reducing per‑GPU memory usage and enabling training of large models that do not fit in a single GPU. ^[multi-gpu-workload-databricks-on-aws.md]

On Databricks, FSDP is one of the three major distributed training libraries integrated with the `@distributed` API from the `serverless_gpu` Python library. The other supported libraries are [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) and [DeepSpeed](/concepts/deepspeed.md). The `@distributed` decorator abstracts GPU provisioning, environment setup, and workload distribution, allowing you to use FSDP with minimal code changes. ^[multi-gpu-workload-databricks-on-aws.md]

## When to Use FSDP

FSDP is best suited for models that **do not fit in a single GPU’s memory**, such as large language model (LLM) training with tens of billions of parameters. The following table from the Databricks documentation summarises the trade‑offs between the three supported approaches:

| Library | Best suited for | Memory efficiency |
|---------|----------------|-------------------|
| DDP | Models that fit in a single GPU | Low |
| FSDP | Models that do not fit in a single GPU | High (shards parameters) |
| DeepSpeed | When advanced memory optimization features are required | Very high |

^[multi-gpu-workload-databricks-on-aws.md]

FSDP provides a good balance between memory savings and ease of use for most large‑model training scenarios. If you need even more aggressive memory optimizations, consider DeepSpeed. ^[multi-gpu-workload-databricks-on-aws.md]

## Using FSDP with the `@distributed` API

To run an FSDP training job on Databricks:

1. **Select an 8xH100 accelerator** – FSDP requires a multi‑GPU node. The [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) provides 8 H100 GPUs on a single node, which is the recommended setup for distributed training. ^[multi-gpu-workload-databricks-on-aws.md]
2. **Use the `@distributed` decorator** – Import `serverless_gpu` and decorate your training function with `@distributed(gpus=8, gpu_type='H100')`. ^[multi-gpu-workload-databricks-on-aws.md]
3. **Wrap your FSDP model** – Inside the decorated function, apply `torch.distributed.fsdp.FullyShardedDataParallel` to your model instead of `DistributedDataParallel`. The API supports all standard PyTorch FSDP options. ^[multi-gpu-workload-databricks-on-aws.md]
4. **Data loading** – Place data loading inside the decorated function to avoid pickle size limits. Use `DistributedSampler` to partition data across GPUs. ^[multi-gpu-workload-databricks-on-aws.md]

### Example skeleton

```python
from serverless_gpu import distributed

@distributed(gpus=8, gpu_type='H100')
def train_with_fsdp(epochs: int, batch_size: int):
    import torch.distributed as dist
    from torch.distributed.fsdp import FullyShardedDataParallel as FSDP
    # ... setup model, wrap with FSDP, create dataloader, run training loop ...

train_with_fsdp.distributed(epochs=3, batch_size=32)
```

^[multi-gpu-workload-databricks-on-aws.md]

The `@distributed` API automatically handles process initialisation (`dist.init_process_group("nccl")`) when you call `setup()` inside the function, or you can rely on the API’s built‑in environment variables (`LOCAL_RANK`, `RANK`, `WORLD_SIZE`). ^[multi-gpu-workload-databricks-on-aws.md]

## Related Concepts

- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – Simpler approach for models that fit in a single GPU.
- [DeepSpeed](/concepts/deepspeed.md) – Advanced memory optimisation library with ZeRO stages.
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) – The recommended hardware for running FSDP on Databricks.
- [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) – The parameter range where FSDP is particularly effective.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – The on‑demand infrastructure that powers FSDP workloads.

## Sources

- multi-gpu-workload-databricks-on-aws.md

# Citations

1. [multi-gpu-workload-databricks-on-aws.md](/references/multi-gpu-workload-databricks-on-aws-c6af01f5.md)
