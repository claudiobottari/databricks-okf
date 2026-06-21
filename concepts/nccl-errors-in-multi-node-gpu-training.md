---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fd33a4a6dcef945d29badf739c2945b9a70d4673a490c86ccf53f8d7b4e5cc33
  pageDirectory: concepts
  sources:
    - distributed-training-with-torchdistributor-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - nccl-errors-in-multi-node-gpu-training
    - NEIMGT
    - NCCL Errors in Distributed GPU Training
  citations:
    - file: distributed-training-with-torchdistributor-databricks-on-aws.md
title: NCCL Errors in Multi-Node GPU Training
description: Common NCCL failures on Databricks including peer access issues on G5 GPUs and network interface misconfiguration, with environment variable workarounds.
tags:
  - troubleshooting
  - gpu
  - nccl
timestamp: "2026-06-19T10:20:18.218Z"
---

# NCCL Errors in Multi-Node GPU Training

**NCCL Errors in Multi-Node GPU Training** refer to a class of failures originating from the NVIDIA Collective Communications Library (NCCL) when it is unable to establish or maintain proper GPU-to-GPU communication across multiple nodes in a distributed training cluster. These errors typically manifest as `ncclInternalError: Internal check failed` and are the most common symptom of network-related problems in multi-node GPU setups.

## Common Error Message

The most frequently seen NCCL error in multi-node training is:

```
NCCL failure: ncclInternalError: Internal check failed.
```

^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Root Cause

This error indicates that NCCL cannot use certain network interfaces for GPU communication. During distributed training, NCCL attempts to establish communication channels between GPUs on different nodes. When the default network interface selection fails — for example, because the selected interface is not the primary one used for inter-node GPU traffic — the connection attempt fails with an internal consistency check error. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Resolution

The standard fix is to force NCCL to use the primary network interface by setting the `NCCL_SOCKET_IFNAME` environment variable to `"eth0"` (or, more generally, the name of the interface that carries GPU communication traffic): ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

```python
import os
os.environ["NCCL_SOCKET_IFNAME"] = "eth0"
```

This snippet should be added **before** NCCL initialization — typically at the top of the training script, before any `torch.distributed.init_process_group` call — so that NCCL binds its sockets to the correct interface during process group setup. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## When to Apply the Fix

This workaround is recommended **only** when the NCCL `Internal check failed` error is observed. If training runs without errors, no change is needed. The fix is environment-specific: it should be tested and then permanently included in the training script if it resolves the problem. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Related Errors

- **CUDA failure: `peer access is not supported between these two devices`** — A different NCCL configuration error that occurs specifically on the G5 suite of GPUs (AWS). The fix is `os.environ["NCCL_P2P_DISABLE"] = "1"`. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]
- **Gloo failure: `RuntimeError: Connection refused`** — A similar socket-interface error for the Gloo backend (used for CPU-based distributed training). The fix is `os.environ["GLOO_SOCKET_IFNAME"] = "eth0"`. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Related Concepts

- NCCL (NVIDIA Collective Communications Library) — The underlying communication library for GPU training across multiple nodes.
- [TorchDistributor](/concepts/torchdistributor.md) — PySpark module that uses `torch.distributed.run` under the hood; NCCL errors often surface through its `.run()` calls.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — The PyTorch parallel strategy that relies on NCCL for multi-GPU communication.
- Gloo Backend — CPU-based alternative to NCCL; used when GPUs are not available.
- Network Interface Selection — The `NCCL_SOCKET_IFNAME` and `GLOO_SOCKET_IFNAME` environment variables that control which network interface NCCL (and Gloo) bind to.
- Peer Access Errors — Related NCCL configuration errors for specific GPU families like the G5 suite on AWS.

## Sources

- distributed-training-with-torchdistributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-torchdistributor-databricks-on-aws.md](/references/distributed-training-with-torchdistributor-databricks-on-aws-8705ab32.md)
