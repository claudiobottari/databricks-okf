---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 569a7cd3f1cc9d02616c49661038631de79f687ad50185204736a64d0a836ae0
  pageDirectory: concepts
  sources:
    - distributed-training-with-torchdistributor-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - gloo-errors-in-distributed-cpu-training
    - GEIDCT
    - NCCL Errors in Distributed GPU Training
  citations:
    - file: distributed-training-with-torchdistributor-databricks-on-aws.md
title: Gloo Errors in Distributed CPU Training
description: Connection refused errors when using the Gloo backend for distributed training on CPU instances, resolved by setting the GLOO_SOCKET_IFNAME environment variable.
tags:
  - troubleshooting
  - cpu
  - gloo
timestamp: "2026-06-19T10:19:50.022Z"
---

# Gloo Errors in Distributed CPU Training

**Gloo Errors in Distributed CPU Training** refer to runtime failures that occur when using the Gloo backend for distributed training on CPU instances. The most common manifestation is a `RuntimeError: Connection refused` error, which indicates that the Gloo communication library cannot establish network connections between worker processes.

## Error Message

When this error occurs during distributed training, it typically appears as:

```
RuntimeError: Connection refused
```

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Cause

The Gloo backend, which is the default communication backend for CPU-based distributed training in PyTorch, relies on network interfaces to establish connections between worker processes. When Gloo cannot identify or use the correct network interface for inter-process communication, it fails to establish connections, resulting in a "Connection refused" error. This issue commonly arises in cloud environments where multiple network interfaces may be present. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Solution

To resolve this error, explicitly specify the network interface that Gloo should use for communication. Set the `GLOO_SOCKET_IFNAME` environment variable to the primary network interface (typically `eth0`): ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

```python
import os
os.environ["GLOO_SOCKET_IFNAME"] = "eth0"
```

This environment variable should be set in your training code before initializing the distributed process group. The `eth0` interface is the standard primary network interface in most cloud environments, but you may need to verify the correct interface name for your specific infrastructure. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Related Concepts

- [TorchDistributor](/concepts/torchdistributor.md) — PySpark module for launching distributed PyTorch training jobs
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — PyTorch's distributed training paradigm
- [NCCL Errors in Distributed GPU Training](/concepts/nccl-errors-in-multi-node-gpu-training.md) — Similar network communication errors for GPU training
- GPU Scheduling — Optimizing GPU utilization for distributed training
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — General concepts for multi-worker model training

## Sources

- distributed-training-with-torchdistributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-torchdistributor-databricks-on-aws.md](/references/distributed-training-with-torchdistributor-databricks-on-aws-8705ab32.md)
