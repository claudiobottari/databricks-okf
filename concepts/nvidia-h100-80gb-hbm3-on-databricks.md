---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b52d21e084b6eea4c4c89822a27af68c3874de586194b73cf586f77596e57747
  pageDirectory: concepts
  sources:
    - get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - nvidia-h100-80gb-hbm3-on-databricks
    - NH8HOD
  citations:
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
title: NVIDIA H100 80GB HBM3 on Databricks
description: Configuration and use of NVIDIA H100 80GB HBM3 GPUs via Databricks Serverless GPU compute for large model training
tags:
  - nvidia
  - gpu
  - hardware
  - h100
timestamp: "2026-06-19T10:44:58.844Z"
---

Here is the wiki page for "NVIDIA H100 80GB HBM3 on Databricks", written based solely on the provided source material.

---

## NVIDIA H100 80GB HBM3 on Databricks

**NVIDIA H100 80GB HBM3 on Databricks** refers to the availability and usage of NVIDIA H100 GPUs with 80GB of HBM3 memory for high-performance deep learning workloads on the Databricks platform, primarily through [Databricks Serverless GPU Compute](/concepts/databricks-serverless-gpu-compute.md).

### Overview

The NVIDIA H100 80GB HBM3 GPU is a high-performance accelerator available on Databricks for demanding machine learning tasks. Compared to lower-tier GPUs like A10s, H100s offer larger floating-point operations per second (FLOPS) and higher-bandwidth memory (HBM3). ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

### When to Use H100 GPUs

H100 GPUs are recommended for large model **training** where high throughput and/or large GPU memory (80GB HBM3 per GPU) is needed. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

### Getting Started with Serverless GPU Compute

To use H100 GPUs on Databricks, you must configure a [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) cluster and select the appropriate accelerator option.

1.  From the compute selector, select **Serverless GPU**.
2.  In the "Environment" tab, select **8xH100** for your accelerator. This option provides 8 H100 chips on a single node.
3.  Choose the **AI v5** environment from the right panel.
4.  Click **Apply**.

### Verifying the GPU Connection

Use the `nvidia-smi` command in a Databricks notebook to confirm that you are connected to the H100 GPUs and to check their memory and utilization. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

### Running Distributed Workloads

Databricks provides the `serverless_gpu` Python library to run distributed GPU workloads directly from notebooks. The library includes a `@distributed` decorator to distribute functions across multiple GPUs on a single node. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

```python
from serverless_gpu import distributed
from serverless_gpu import runtime as rt

@distributed(
    gpus=8,
    gpu_type='h100',
)
def hello_world(name: str) -> list[int]:
    if rt.get_local_rank() == 0:
        print('hello world', name)
    return rt.get_global_rank()

result = hello_world.distributed('SGC')
```

The function above runs on 8 processes, one per GPU on the node. The `runtime` module provides access to local and global GPU ranks. The expected result is a list from 0 to 7: `[0, 1, 2, 3, 4, 5, 6, 7]`. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

### Related Concepts

- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The compute infrastructure for running H100 workloads.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — The AI runtime environment that includes necessary libraries.
- [Distributed Training on Databricks](/concepts/distributed-training-on-databricks.md) — Advanced multi-GPU and multi-node training techniques.
- GPU Scheduling — Optimizing utilization for H100 workloads.

### Sources

- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md

# Citations

1. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
