---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a03358dbe89d903dd05a6954ea887aa5e26fbef2f5f2703a56a61aef7035daa2
  pageDirectory: concepts
  sources:
    - horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
  confidence: 0.88
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - horovod-network-interface-configuration
    - HNIC
  citations:
    - file: horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
title: Horovod Network Interface Configuration
description: Configuration of OMPI_MCA_btl_tcp_if_include and NCCL_SOCKET_IFNAME environment variables to resolve Open MPI TCP connection issues in multi-node clusters.
tags:
  - networking
  - troubleshooting
  - mpi
timestamp: "2026-06-19T19:05:51.501Z"
---

# Horovod Network Interface Configuration

**Horovod Network Interface Configuration** refers to the set of environment variables used to specify the network interfaces that Open MPI and NCCL should use for inter‑node communication when running distributed training with [HorovodRunner](/concepts/horovodrunner.md) on Databricks. Proper configuration prevents common network‑related errors that can occur when Horovod processes on different cluster nodes attempt to communicate. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Background

HorovodRunner launches Horovod MPI jobs across multiple Spark executors. In multi‑node clusters, MPI and NCCL need to discover the correct network interface for TCP and GPU‑to‑GPU communication. If multiple network interfaces exist (e.g., Docker‑bridged networks, VPC subnets), the default interface selection may be incorrect, leading to the error: ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

```
WARNING: Open MPI accepted a TCP connection from what appears to be another Open MPI process but cannot find a corresponding process entry for that peer
```

This warning indicates that Open MPI processes on different nodes cannot properly identify each other, usually because they are communicating over the wrong network interface. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Solution: Set the Primary Network Interface

To resolve the communication error, set the `OMPI_MCA_btl_tcp_if_include` and `NCCL_SOCKET_IFNAME` environment variables to the name of the primary network interface used for inter‑node communication. On Databricks clusters, the primary interface is typically `eth0`. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

Add the following snippet at the beginning of your Horovod training function (before calling `hvd.init()` or any MPI routine):

```python
import os
os.environ["OMPI_MCA_btl_tcp_if_include"] = "eth0"
os.environ["NCCL_SOCKET_IFNAME"] = "eth0"
```

^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

| Environment Variable | Purpose |
|----------------------|---------|
| `OMPI_MCA_btl_tcp_if_include` | Tells Open MPI which network interface to use for TCP based communication (the BTL (Byte Transfer Layer) TCP module). Setting it to `eth0` forces MPI to use that interface. |
| `NCCL_SOCKET_IFNAME` | Informs the NVIDIA Collective Communications Library (NCCL) which network interface to use for socket‑based inter‑node GPU communication. |

## Determining the Correct Interface Name

On Databricks clusters, `eth0` is the typical primary network interface. If your cluster uses a different naming convention, you can discover the interface name by running a shell command (e.g., `ip link show` or `ifconfig`) inside a notebook cell or via an init script. The chosen interface must be reachable between all worker nodes and should have a stable IP address.

## Placement of Configuration

The environment variables must be set **inside the Python function** that is passed to `HorovodRunner.run()`, because they affect the MPI and NCCL processes started by Horovod. Setting them at the notebook or cluster level before the function runs may not propagate correctly to the MPI subprocesses launched by the barrier execution mode. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Related Concepts

- [HorovodRunner](/concepts/horovodrunner.md) – The Databricks API that wraps Horovod training into a Spark job.
- Open MPI – The MPI implementation used by Horovod for inter‑process communication.
- NCCL – NVIDIA’s collective communications library for GPU‑to‑GPU data transfer.
- [Distributed deep learning on Databricks](/concepts/distributed-deep-learning-on-databricks.md) – General guidance for multi‑node training.
- [Barrier Execution Mode](/concepts/spark-barrier-execution-mode.md) – The Spark execution mode that enables tight synchronization among tasks.
- [Horovod Timeline](/concepts/horovod-timeline.md) – A performance profiling feature (not recommended for production due to overhead).

## Sources

- horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md

# Citations

1. [horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md](/references/horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws-bdb09a88.md)
