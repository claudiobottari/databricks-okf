---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 450d507d91b74d1a9060430775270af226884e5fb7f0dc79c64c71d78f726855
  pageDirectory: concepts
  sources:
    - distributed-training-with-torchdistributor-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - torchdistributor-troubleshooting-nccl-and-gpu-communication-errors
    - "GPU Communication Errors and TorchDistributor Troubleshooting: NCCL"
    - TTNAGCE
  citations:
    - file: distributed-training-with-torchdistributor-databricks-on-aws.md
title: "TorchDistributor Troubleshooting: NCCL and GPU Communication Errors"
description: CUDA peer access errors on G5 GPUs and NCCL internal errors in multi-node training, resolved by setting NCCL_P2P_DISABLE=1 and NCCL_SOCKET_IFNAME=eth0 environment variables.
tags:
  - troubleshooting
  - gpu
  - nvidia
  - distributed-training
timestamp: "2026-06-18T12:09:25.844Z"
---

# TorchDistributor Troubleshooting: NCCL and GPU Communication Errors

When running distributed training with [TorchDistributor](/concepts/torchdistributor.md) on GPU clusters, users may encounter errors related to NCCL (NVIDIA Collective Communications Library) and GPU communication. These errors typically arise from network configuration issues, hardware incompatibilities, or environment setup problems that prevent proper communication between distributed worker processes. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Common Errors and Solutions

### CUDA Failure: `peer access is not supported between these two devices`

This error occurs on the G5 suite of GPUs on AWS. It indicates that direct peer-to-peer memory access between GPU devices is not supported by the hardware configuration. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

**Solution:** Disable NCCL peer-to-peer communication by setting the following environment variable in your training code:

```python
import os
os.environ["NCCL_P2P_DISABLE"] = "1"
```

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### NCCL Failure: `ncclInternalError: Internal check failed.`

This error typically occurs during multi-node training and indicates a problem with network communication among GPUs. NCCL cannot use certain network interfaces for GPU communication, resulting in internal consistency check failures. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

**Solution:** Specify the primary network interface for NCCL communication:

```python
import os
os.environ["NCCL_SOCKET_IFNAME"] = "eth0"
```

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Gloo Failure: `RuntimeError: Connection refused`

This error may occur when using Gloo for distributed training on CPU instances. It indicates that the backend cannot establish connections between distributed worker processes. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

**Solution:** Set the Glo socket interface name:

```python
import os
os.environ["GLOO_SOCKET_IFNAME"] = "eth0"
```

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Root Causes and Context

### NCCL Backend Requirements

NCCL is the preferred backend for GPU-based distributed training in PyTorch. It requires proper network configuration to enable efficient GPU-to-GPU communication. When NCCL cannot identify or use the correct network interfaces, communication failures occur. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Hardware and Environment Factors

The G5 GPU suite on AWS has specific limitations regarding peer-to-peer GPU communication, which may require disabling NCCL P2P. Similarly, multi-node setups may need explicit network interface specification when multiple interfaces are available. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## General Troubleshooting Approach

1. **Identify the backend** - Determine whether you are using NCCL (for GPU) or Gloo (for CPU) as your distributed communication backend.
2. **Check network configuration** - Verify that network interfaces are properly configured and accessible across all worker nodes.
3. **Apply environment variables** - Set the appropriate environment variable (`NCCL_P2P_DISABLE`, `NCCL_SOCKET_IFNAME`, or `GLOO_SOCKET_IFNAME`) before initializing the distributed process group.
4. **Test with single node first** - If possible, test your distributed setup on a single node before scaling to multi-node configurations.

## Related Concepts

- [TorchDistributor](/concepts/torchdistributor.md) - The PySpark module for distributed PyTorch training
- [DistributedDataParallel](/concepts/distributed-data-parallel-ddp.md) - PyTorch's distributed training paradigm
- NCCL - NVIDIA's collective communications library
- Gloo - A collective communications library for CPU-based training
- PySpark ML - Apache Spark's machine learning framework
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) - General concepts of multi-worker model training
- GPU Communication - Hardware and protocol considerations for GPU clusters

## Sources

- distributed-training-with-torchdistributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-torchdistributor-databricks-on-aws.md](/references/distributed-training-with-torchdistributor-databricks-on-aws-8705ab32.md)
