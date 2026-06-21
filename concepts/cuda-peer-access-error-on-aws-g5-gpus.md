---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bf26d9a1561f00f4481b081cdabb4314a1f8e308ad7efa4020f0ebe9484d08af
  pageDirectory: concepts
  sources:
    - distributed-training-with-torchdistributor-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cuda-peer-access-error-on-aws-g5-gpus
    - CPAEOAGG
  citations:
    - file: distributed-training-with-torchdistributor-databricks-on-aws.md
title: CUDA Peer Access Error on AWS G5 GPUs
description: A specific distributed training error (peer access not supported) encountered on AWS G5 GPU instances, resolved by disabling NCCL P2P
tags:
  - troubleshooting
  - cuda
  - aws
  - g5-gpu
  - nccl
timestamp: "2026-06-18T15:34:57.467Z"
---

# CUDA Peer Access Error on AWS G5 GPUs

**CUDA Peer Access Error on AWS G5 GPUs** is a distributed training error that occurs when using NVIDIA G5 GPU instances on AWS with PyTorch's distributed data parallel (DDP) training. The error manifests as `peer access is not supported between these two devices` and is caused by a limitation in how G5 GPUs handle peer-to-peer GPU memory access over the NVLink or PCIe bus.

## Error Message

When this error occurs, PyTorch raises a CUDA failure with the following message:

```
peer access is not supported between these two devices
```

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Cause

The error is specific to the G5 suite of GPUs available on AWS. These GPUs do not support direct peer-to-peer memory access between devices, which is a requirement for certain distributed training configurations using NCCL (NVIDIA Collective Communications Library). When PyTorch attempts to enable peer-to-peer access during distributed training initialization, the unsupported hardware configuration causes a CUDA error. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Solution

To resolve this error, disable the NCCL peer-to-peer feature by setting the following environment variable in your training code:

```python
import os
os.environ["NCCL_P2P_DISABLE"] = "1"
```

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

This environment variable tells NCCL to avoid attempting peer-to-peer GPU memory transfers and instead use alternative communication paths (e.g., through the CPU or system memory). This workaround allows distributed training to proceed on G5 GPUs without requiring hardware peer-to-peer support. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Related Tuning

After disabling peer-to-peer access, you may also need to configure the network interface for NCCL communication. If you encounter an `ncclInternalError: Internal check failed` error during multi-node training, add the following environment variable:

```python
os.environ["NCCL_SOCKET_IFNAME"] = "eth0"
```

This ensures NCCL uses the primary network interface for GPU communication when peer-to-peer is disabled. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Related Concepts

- [TorchDistributor](/concepts/torchdistributor.md) — PySpark module for distributed PyTorch training on Spark clusters.
- Distributed Training with PyTorch — General guidance for setting up multi-GPU training.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — PyTorch's standard approach for distributed training across multiple GPUs.
- NCCL Configuration — Environment variables for tuning NCCL collective operations.
- NCCL P2P Disable — Broader discussion of when to disable peer-to-peer communication.
- AWS G5 Instance Types — GPU instances with NVIDIA A10G Tensor Core GPUs.

## Sources

- distributed-training-with-torchdistributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-torchdistributor-databricks-on-aws.md](/references/distributed-training-with-torchdistributor-databricks-on-aws-8705ab32.md)
