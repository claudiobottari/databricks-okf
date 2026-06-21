---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 55b74ae128dd77bc1aefdb58621fd11aeaed91278e56e7cfb72dde41eaf7beaa
  pageDirectory: concepts
  sources:
    - distributed-training-with-torchdistributor-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - torchdistributor-troubleshooting-gloo-connection-refused
    - TTGCR
  citations:
    - file: distributed-training-with-torchdistributor-databricks-on-aws.md
title: "TorchDistributor Troubleshooting: Gloo Connection Refused"
description: Error when using Gloo backend for distributed CPU training, resolved by setting the GLOO_SOCKET_IFNAME=eth0 environment variable.
tags:
  - troubleshooting
  - cpu
  - distributed-training
timestamp: "2026-06-18T12:09:32.535Z"
---

# TorchDistributor Troubleshooting: Gloo Connection Refused

The **Gloo Connection Refused** error occurs when using the Gloo backend for distributed training with [TorchDistributor](/concepts/torchdistributor.md) on CPU instances. Gloo is the communication backend used by PyTorch’s `torch.distributed` when GPUs are not available; it relies on network sockets for inter-process communication. If Gloo attempts to bind to or connect through a network interface that is not properly configured or is unreachable, it raises a `RuntimeError: Connection refused`. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Error Message

The error appears as:

```
RuntimeError: Connection refused
```

This typically surfaces during `dist.init_process_group(backend="gloo")` or when workers attempt to connect to each other. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Cause

Gloo selects a default network interface (often `lo` or a Docker bridge) that may not be reachable by other processes in the cluster. On cloud instances, especially those with multiple virtual network interfaces, the chosen interface may be isolated from the worker nodes, causing connection timeouts or immediate refusals. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

## Solution

Force Gloo to use the primary network interface by setting the `GLOO_SOCKET_IFNAME` environment variable to `"eth0"` (or the appropriate interface for your environment). Add the following snippet at the top of your training function: ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

```python
import os
os.environ["GLOO_SOCKET_IFNAME"] = "eth0"
```

After this change, Gloo will communicate over `eth0`, which is typically the primary internal network interface on cloud VM instances. ^[distributed-training-with-torchdistributor-databricks-on-aws.md]

### Verifying the fix

1. Set the environment variable before calling `dist.init_process_group()`.
2. Run the training with the same `TorchDistributor` configuration.
3. If the error persists, check the network interface names available on your nodes (e.g., with `ip link show`) and substitute the correct interface name for `eth0`.

## Related Troubleshooting

Similar backend-specific environment variables exist for NCCL failures. For GPU-based training, you may also need to set `NCCL_P2P_DISABLE="1"` or `NCCL_SOCKET_IFNAME="eth0"`. See [TorchDistributor Troubleshooting: NCCL Internal Error](/concepts/torchdistributor-troubleshooting-nccl-and-gpu-communication-errors.md) and TorchDistributor Troubleshooting: CUDA Peer Access.

## Related Concepts

- [TorchDistributor](/concepts/torchdistributor.md) — The PySpark module for distributed PyTorch training
- Gloo backend — The default CPU communication backend in PyTorch Distributed
- NCCL backend — The GPU-accelerated communication backend
- Distributed training with PyTorch — General patterns for data-parallel training
- PySpark ML — The machine learning library in Spark
- Environment variables for distributed training — Common variables that control interface and transport selection

## Sources

- distributed-training-with-torchdistributor-databricks-on-aws.md

# Citations

1. [distributed-training-with-torchdistributor-databricks-on-aws.md](/references/distributed-training-with-torchdistributor-databricks-on-aws-8705ab32.md)
