---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bdef1f1940067873f28f89b020d484494b09ac2f418dbc1bbfc828aa6fe753e3
  pageDirectory: concepts
  sources:
    - distributed-training-with-torchdistributor-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - nccl-and-gloo-environment-variable-fixes-for-distributed-training
    - Gloo Environment Variable Fixes for Distributed Training and NCCL
    - NAGEVFFDT
    - Environment variables for distributed training
  citations:
    - file: distributed-training-with-torchdistributor-databricks-on-aws.md
title: NCCL and Gloo Environment Variable Fixes for Distributed Training
description: Environment variable configurations (NCCL_P2P_DISABLE, NCCL_SOCKET_IFNAME, GLOO_SOCKET_IFNAME) to resolve common GPU/CPU distributed training failures on Databricks
tags:
  - troubleshooting
  - nccl
  - gloo
  - environment-variables
  - databricks
timestamp: "2026-06-18T15:35:18.564Z"
---

# NCCL and Gloo Environment Variable Fixes for Distributed Training

**NCCL and Gloo Environment Variable Fixes for Distributed Training** documents the known environment variable workarounds required when running distributed PyTorch training on certain GPU and CPU hardware configurations. These fixes address specific network communication failures in NVIDIA Collective Communications Library (NCCL) and Gloo backends that can occur when using [TorchDistributor](/concepts/torchdistributor.md) on Spark clusters. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Overview

Distributed training with PyTorch relies on either the NCCL backend (for GPU-based training) or the Gloo backend (for CPU-based training) to handle communication between processes. Certain cloud instance types or network configurations can cause these backends to fail with specific error messages. The fixes described in this page—set via environment variables—override the backend's default behavior to select a usable communication path. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## NCCL Fixes

### Peer access: `peer access is not supported between these two devices`

This error occurs on the G5 suite of GPU instances on AWS. To resolve it, disable NCCL's peer-to-peer (P2P) access by adding the following to your training code: ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

```python
import os
os.environ["NCCL_P2P_DISABLE"] = "1"
```

### Internal check: `ncclInternalError: Internal check failed.`

This error arises during multi-node training when NCCL cannot use certain network interfaces for GPU communication. To resolve it, force NCCL to use the primary network interface by setting: ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

```python
import os
os.environ["NCCL_SOCKET_IFNAME"] = "eth0"
```

## Gloo Fix

### Connection refused: `RuntimeError: Connection refused`

This error can occur when using the Gloo backend for distributed training on CPU instances. To resolve it, force Gloo to use the primary network interface: ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

```python
import os
os.environ["GLOO_SOCKET_IFNAME"] = "eth0"
```

## When to Apply These Fixes

Apply these environment variable fixes in the training function that you pass to `TorchDistributor.run()`. The following table summarizes when each fix is needed: ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

| Environment Variable | Backend | Target Hardware | When to Use |
|---|---|---|---|
| `NCCL_P2P_DISABLE` | NCCL | GPU (G5 instances on AWS) | Peer access error between devices |
| `NCCL_SOCKET_IFNAME` | NCCL | GPU (multi-node) | Internal check failure during inter-node communication |
| `GLOO_SOCKET_IFNAME` | Gloo | CPU | Connection refused error |

## Best Practices

- Add these environment variable assignments inside the training function that `TorchDistributor` executes, not in the top-level notebook scope, to ensure they are distributed to all worker processes. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]
- After applying the fix, initialize the distributed process group using `dist.init_process_group(backend)` and choose the backend based on whether you are using GPUs. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]
- For GPU training, set `backend = "nccl"`; for CPU training, set `backend = "gloo"`. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Related Concepts

- [TorchDistributor](/concepts/torchdistributor.md) – The PySpark module that launches distributed PyTorch training on Spark clusters.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – The PyTorch wrapper for model parallelism.
- NCCL – NVIDIA collective communication library for GPU communication.
- Gloo – A CPU-based communication backend.
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md) – GPU instances where NCCL fixes may be needed.
- Spark 3.4 – The minimum Spark version required for TorchDistributor.

## Sources

- distributed-training-with-torchdistributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-torchdistributor-databricks-on-aws.md](/references/distributed-training-with-torchdistributor-databricks-on-aws-8705ab32.md)
