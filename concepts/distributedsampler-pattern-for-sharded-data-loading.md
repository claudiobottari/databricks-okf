---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0624c2b57de9c2be756599f01bf8d2620f2507bbee7a5990503d8625db7d71c5
  pageDirectory: concepts
  sources:
    - distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - distributedsampler-pattern-for-sharded-data-loading
    - DPFSDL
  citations:
    - file: distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md
title: DistributedSampler Pattern for Sharded Data Loading
description: A PyTorch pattern using DistributedSampler with DataLoader to partition dataset batches across multiple GPU workers in a distributed training setup, with epoch-based shuffling via sampler.set_epoch().
tags:
  - pytorch
  - data-loading
  - distributed-training
timestamp: "2026-06-18T12:07:43.067Z"
---

# DistributedSampler Pattern for Sharded Data Loading

The **DistributedSampler Pattern** is a standard approach for partitioning a dataset across multiple workers in distributed PyTorch training. Each worker receives a unique, non-overlapping shard of the data, ensuring that every sample is processed exactly once per epoch while supporting consistent shuffling across workers. This pattern is essential for [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md), [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md), and other PyTorch Distributed Training strategies.^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Overview

In distributed training, each process (or worker) should work on a different subset of the data to avoid redundant computation. The `DistributedSampler` from `torch.utils.data` assigns each process a slice of the dataset based on the total number of replicas (`world_size`) and the process’s rank. The same sampler also supports per-epoch shuffling, so the data is re-partitioned randomly each epoch when `set_epoch` is called.^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## How It Works

1. **Initialization**: The sampler is created with `num_replicas=world_size` and `rank=rank`. The rank identifies which GPU or process this sampler belongs to.
2. **Sharding**: During iteration, the sampler yields indices for only the subset of the dataset assigned to that rank.
3. **Epoch‑aware shuffling**: Before each epoch, calling `sampler.set_epoch(epoch)` ensures that the shuffle order changes deterministically across epochs, which is important for convergence.
4. **DataLoader integration**: The sampler is passed directly to a `DataLoader` in place of the `shuffle` parameter. The DataLoader’s `shuffle` must be `False` when using a sampler that already handles shuffling.^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Implementation Example

The following pattern appears in a FSDP training function on Databricks serverless GPU compute. The training function runs on 8 H100 GPUs. The `DistributedSampler` is conditionally used when `world_size > 1`:^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

```python
from torch.utils.data import Dataset, DataLoader, DistributedSampler

# After setting up the training process (rank, world_size, device)
dataset = SyntheticDataset(size=10000, input_dim=512, num_classes=10)

if world_size > 1:
    sampler = DistributedSampler(
        dataset,
        num_replicas=world_size,
        rank=rank
    )
    shuffle = False
else:
    sampler = None
    shuffle = True

dataloader = DataLoader(
    dataset,
    batch_size=32,
    shuffle=shuffle,
    sampler=sampler,
    num_workers=num_workers,
    pin_memory=True
)

# Training loop
for epoch in range(num_epochs):
    if sampler:
        sampler.set_epoch(epoch)  # important for correct shuffling across epochs
    # ... forward/backward pass
```

^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

Key points from the source:
- The sampler is created with `num_replicas=world_size` and `rank=rank`.^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]
- `sampler.set_epoch(epoch)` is called at the start of each epoch to reshuffle.^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]
- The `shuffle` parameter in `DataLoader` is set to `False` when a sampler is used.^[distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md]

## Best Practices

- **Always call `set_epoch`** before each epoch when using `DistributedSampler`. Without it, every epoch will use the same shuffle order, which can harm model convergence.
- **Set `shuffle=False`** in the `DataLoader` when using a sampler that handles shuffling — the sampler controls the order.
- **Use `pin_memory=True`** to speed up data transfer to GPU, especially with many `num_workers`.
- **Match `num_replicas` to `world_size`** (the total number of distributed workers) and `rank` to the process index (0‑based). These values are typically set by the framework (e.g., by Databricks’ serverless GPU distributed API).

## Related Concepts

- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – A PyTorch strategy that shards model parameters, gradients, and optimizer states across GPUs; uses DistributedSampler for data sharding.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – Another PyTorch distributed strategy that replicates the model on each GPU and synchronizes gradients; also relies on DistributedSampler.
- DataLoader – PyTorch utility that loads data in parallel; accepts a sampler to control iteration order.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) – Databricks managed GPU infrastructure that automatically provisions compute for distributed workloads.
- PyTorch Distributed Training – General concept of training models across multiple GPUs or nodes.

## Sources

- distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md

# Citations

1. [distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws.md](/references/distributed-training-using-pytorch-fsdp-on-serverless-gpu-compute-databricks-on-aws-e728aa55.md)
