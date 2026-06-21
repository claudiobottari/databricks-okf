---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f19d5afcdb057451edd2215e8f829bb08f9ba694fbc7fe169b39ebbda0903bfe
  pageDirectory: concepts
  sources:
    - distributed-training-using-deepspeed-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cpu-offloading-in-deepspeed
    - COID
    - NVMe Offloading in DeepSpeed
  citations:
    - file: distributed-training-using-deepspeed-databricks-on-aws.md
title: CPU Offloading in DeepSpeed
description: A feature of DeepSpeed ZeRO that allows offloading optimizer states, gradients, or parameters to CPU memory to reduce GPU memory usage during large model training.
tags:
  - memory-optimization
  - distributed-training
timestamp: "2026-06-19T10:18:06.101Z"
---

Here is a wiki page on the topic of CPU Offloading in DeepSpeed, based on the provided source material.

---

## CPU Offloading in DeepSpeed

**CPU Offloading** in [DeepSpeed](/concepts/deepspeed.md) is a ZeRO-based memory optimization technique that reduces GPU memory pressure during large-model training by moving optimizer states, gradients, or parameters to host CPU memory and NVMe storage. It is part of DeepSpeed’s broader ZeRO-Offload strategy and is particularly useful when model size exceeds available GPU memory.

### Overview

CPU Offloading is a key feature of [ZeRO (Zero Redundancy Optimizer)](/concepts/zero-zero-redundancy-optimizer.md) Stage 2 and Stage 3 in DeepSpeed. When enabled, the optimizer states and gradients are stored on the CPU during training, freeing GPU memory for larger batch sizes or model parameters. This is a critical technique for training large models (e.g., 1B to 100B+ parameters) when GPU memory is constrained. ^[distributed-training-using-deepspeed-databricks-on-aws.md]

DeepSpeed’s CPU Offload feature is distinct from NVMe Offloading which offloads to disk. Both are part of DeepSpeed’s memory optimization toolkit.

### When to Use CPU Offloading

Use CPU Offloading when:

- You need advanced memory optimization beyond standard [FSDP](/concepts/fsdp-fully-sharded-data-parallel.md) (Fully Sharded Data Parallel) or [DDP](/concepts/distributed-data-parallel-ddp-training.md) (Distributed Data Parallel).
- You require fine-grained control over optimizer state sharding (ZeRO-Offload can be used with ZeRO Stage 2 or 3).
- You need additional features like gradient accumulation fusion or CPU offloading.
- You are working with large language models (1B to 100B+ parameters) where GPU memory is a bottleneck.

^[distributed-training-using-deepspeed-databricks-on-aws.md]

### How It Works

CPU Offloading moves optimizer states and gradients to CPU memory, reducing GPU memory usage. This is configured within a DeepSpeed configuration file (`.json`). The primary configuration parameters for CPU offloading are:

- `"offload_optimizer"`: Controls whether optimizer states are offloaded to CPU or NVMe.
- `"device"`: Specifies the target device for offloading (e.g., `"cpu"`).
- `"pin_memory"`: A boolean flag that enables pinned memory on the CPU, which can improve transfer speed between GPU and CPU.
- `"ratio"`: (Optional) The ratio of optimizer states to offload. Default is 1.0 (all states).

#### Example Configuration

A typical DeepSpeed configuration file enabling CPU offloading for the optimizer looks like:

```json
{
  "zero_optimization": {
    "stage": 2,
    "allgather_bucket_size": 5e8,
    "allreduce_bucket_size": 5e8,
    "contiguous_gradients": true,
    "overlap_comm": true,
    "reduce_scatter": true,
    "reduce_bucket_size": 5e8,
    "offload_optimizer": {
      "device": "cpu",
      "pin_memory": true
    }
  }
}
```

**Note:** In this example, `"stage": 2` means optimizer state partitioning (ZeRO Stage 2). CPU offloading can also be configured for ZeRO Stage 3 (parameter partitioning).

### Prerequisites

- [DeepSpeed](/concepts/deepspeed.md) must be installed on the cluster (e.g., `pip install deepspeed`).
- The cluster must have sufficient CPU RAM to hold the offloaded optimizer states.
- Pinned memory (via `pin_memory: true`) can improve performance but requires more CPU memory.

### Performance Considerations

- **CPU offloading increases CPU memory usage** – The offloaded optimizer states reside entirely in CPU RAM. Ensure your cluster has enough CPU memory.
- **Pinned memory** (`pin_memory`) can improve GPU-to-CPU transfer speed but requires that the CPU memory is not swappable.
- **NVMe offloading** (not covered here) is an alternative for even larger offloads, using NVMe storage instead of CPU RAM. See NVMe Offloading in DeepSpeed.

### Alternatives

- [FSDP](/concepts/fsdp-fully-sharded-data-parallel.md) – PyTorch-native, simpler, but lacks CPU offloading.
- [DDP](/concepts/distributed-data-parallel-ddp-training.md) – Standard distributed data parallel, no CPU offload.

### Related Concepts

- ZeRO-Offload
- [Gradient Accumulation](/concepts/gradient-accumulation-fusion.md)
- Mixed Precision Training
- [Large Model Training](/concepts/20b-to-120b-parameter-model-training.md)

### Sources

- distributed-training-using-deepspeed-databricks-on-aws.md

# Citations

1. [distributed-training-using-deepspeed-databricks-on-aws.md](/references/distributed-training-using-deepspeed-databricks-on-aws-9ac82396.md)
