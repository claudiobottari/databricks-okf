---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bc55fcedb321b968db3e96677e36b3169d7263d9fa527df444557015a5301b1c
  pageDirectory: concepts
  sources:
    - distributed-training-with-torchdistributor-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - torchdistributor-common-errors-and-environment-variables
    - Environment Variables and TorchDistributor Common Errors
    - TCEAEV
  citations:
    - file: distributed-training-with-torchdistributor-databricks-on-aws.md
title: TorchDistributor Common Errors and Environment Variables
description: Troubleshooting guide for CUDA peer access, NCCL internal errors, and Gloo connection failures when using TorchDistributor
tags:
  - troubleshooting
  - pytorch
  - distributed-training
timestamp: "2026-06-19T18:38:30.247Z"
---

# TorchDistributor Common Errors and Environment Variables

**TorchDistributor** is an open-source module in PySpark that enables distributed training with PyTorch on Spark clusters. It initializes the environment and communication channels between workers, utilizing the CLI command `torch.distributed.run` to run distributed training across worker nodes. When working with TorchDistributor, several common errors may arise, many of which can be resolved by setting specific environment variables. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Common Errors

### Pickling Errors (Object Not Found)

A common error for the notebook workflow is that objects cannot be found or pickled when running distributed training. This occurs when library import statements are not distributed to other executors. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

**Solution:** Include all import statements (for example, `import torch`) both at the top of the training function that is called with `TorchDistributor(...).run(<func>)` and inside any other user-defined functions called in the training method. Additionally, move imports such as `import torch` within the training function to avoid common pickling errors. The `device_id` that models and data are tied to is determined by `device_id = int(os.environ["LOCAL_RANK"])`. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### CUDA Failure: `peer access is not supported between these two devices`

This error can occur on the G5 suite of GPUs on AWS when using multiple GPUs that cannot directly access each other's memory. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

**Solution:** Add the following snippet in your training code to disable peer-to-peer access:

```python
import os
os.environ["NCCL_P2P_DISABLE"] = "1"
```

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### NCCL Failure: `ncclInternalError: Internal check failed.`

When encountered during multi-node training, this error typically indicates a problem with network communication among GPUs. The issue arises when NCCL (NVIDIA Collective Communications Library) cannot use certain network interfaces for GPU communication. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

**Solution:** Add the following snippet in your training code to use the primary network interface:

```python
import os
os.environ["NCCL_SOCKET_IFNAME"] = "eth0"
```

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Gloo Failure: `RuntimeError: Connection refused`

This error can occur when using Gloo for distributed training on CPU instances, indicating a network connection issue between workers. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

**Solution:** Add the following snippet in your training code:

```python
import os
os.environ["GLOO_SOCKET_IFNAME"] = "eth0"
```

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Environment Variables Reference

| Environment Variable | Purpose | When to Use |
|---------------------|---------|-------------|
| `NCCL_P2P_DISABLE` | Disables peer-to-peer GPU communication | When encountering CUDA peer access errors, particularly on G5 GPUs on AWS |
| `NCCL_SOCKET_IFNAME` | Specifies the network interface for NCCL communication | When encountering NCCL internal errors during multi-node training |
| `GLOO_SOCKET_IFNAME` | Specifies the network interface for Gloo communication | When encountering Gloo connection refused errors on CPU instances |
| `LOCAL_RANK` | Provides the local rank of the process (set automatically by torch.distributed.run) | Used within training functions to determine device assignment |

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Best Practices

When writing training functions for TorchDistributor, always move necessary imports inside the training function to prevent pickling errors. Use `os.environ["LOCAL_RANK"]` to determine the device ID for model and data placement. For GPU training, use the `"nccl"` backend, and for CPU training, use the `"gloo"` backend when initializing the process group with `dist.init_process_group(backend)`. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Related Concepts

- [TorchDistributor API](/concepts/torchdistributor-api-methods.md) — The PySpark module for distributed PyTorch training
- [PyTorch Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — The underlying distributed training paradigm
- NCCL — NVIDIA Collective Communications Library for GPU communication
- Gloo — Collective communications library for CPU-based distributed training
- torch.distributed.run — The CLI command used by TorchDistributor under the hood
- Distributed Training with PyTorch — General distributed training strategies

## Sources

- distributed-training-with-torchdistributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-torchdistributor-databricks-on-aws.md](/references/distributed-training-with-torchdistributor-databricks-on-aws-8705ab32.md)
