---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9f435558e954da204301733b012fec58dffcf4946d26d47a9c181c38badaf50c
  pageDirectory: concepts
  sources:
    - forecasting-time-series-with-gluonts-databricks-on-aws.md
  confidence: 0.8
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-serverless-gpu-compute-for-ml
    - DSGCFM
  citations:
    - file: forecasting-time-series-with-gluonts-databricks-on-aws.md
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
title: Databricks Serverless GPU Compute for ML
description: A Databricks compute environment (e.g., 1xA10 GPU) optimized for running GPU-accelerated machine learning workloads with Unity Catalog integration.
tags:
  - databricks
  - gpu
  - machine-learning
  - infrastructure
timestamp: "2026-06-19T18:54:11.387Z"
---

Here is the wiki page for "Databricks Serverless GPU Compute for ML".

---

## Databricks Serverless GPU Compute for ML

**Databricks Serverless GPU Compute for ML** is an on-demand compute infrastructure provided by Databricks that provisions GPU resources automatically for machine learning workloads, including model training and time series forecasting. It eliminates the need to manually manage clusters, offering a serverless experience where compute is allocated per notebook session.

### Overview

Serverless GPU Compute allows users to connect a notebook to GPU resources without configuring a cluster. Users select an accelerator type (e.g., 1xA10 or 8xH100) and an environment (e.g., AI v5) from a side panel, and the compute is provisioned automatically. This simplifies starting distributed or single-GPU training jobs, as the infrastructure is abstracted away. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]

### Configurations

Serverless GPU Compute provides a range of GPU configurations to suit different workload needs:

- **Single-GPU (1xA10):** Suitable for model inference or small-scale training with standard GPU memory and throughput. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
- **Multi-GPU (8xH100):** Provision eight NVIDIA H100 80GB HBM3 GPUs on a single node. This configuration provides 640 GB total GPU memory and is intended for large model training tasks that require high FLOPS and memory. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

To select a configuration, open the **Environment** side panel in a notebook, set **Accelerator** to the desired type (e.g., `1xA10` or `8xH100`), and choose the appropriate environment such as **AI v5**, which contains the required libraries for distributed GPU workloads. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md, forecasting-time-series-with-gluonts-databricks-on-aws.md]

### Distributed Programming

For multi-GPU single-node configurations, the `serverless_gpu` Python library provides a `@distributed` decorator. This decorator allows a function to run across multiple processes (one per GPU). The `runtime` module exposes functions such as `get_local_rank()` and `get_global_rank()` for coordinating work. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

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
# result == [0, 1, 2, 3, 4, 5, 6, 7]
```

### Use Cases

Serverless GPU Compute for ML supports a range of deep learning workloads:

- **Time Series Forecasting with GluonTS:** Users can install the GluonTS library with PyTorch support, load datasets (e.g., electricity consumption data), and train models like DeepAR. The compute provides the necessary GPU resources for training and evaluation, and checkpoints can be saved to Unity Catalog volumes. ^[forecasting-time-series-with-gluonts-databricks-on-aws.md]
- **Large Language Model (LLM) Training:** The 8xH100 configuration is designed for large model training that benefits from high throughput and large GPU memory. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]
- **Multi-GPU Distributed Training:** Using the `@distributed` decorator or frameworks like [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) and [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md), users can scale training across all GPUs on a node. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

### Verification

After connecting to serverless GPU compute, users can verify the hardware configuration using standard commands:

```bash
!nvidia-smi
```

In Python, GPU availability can be confirmed with:

```python
import torch
assert torch.cuda.is_available(), 'You need to use GPU compute for this notebook'
```

### Related Concepts

- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [GluonTS](/concepts/gluonts.md)
- [DeepAR](/concepts/deepar.md)
- H100 GPU Support on Databricks
- [Unity Catalog](/concepts/unity-catalog.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)

### Sources

- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
- forecasting-time-series-with-gluonts-databricks-on-aws.md

# Citations

1. [forecasting-time-series-with-gluonts-databricks-on-aws.md](/references/forecasting-time-series-with-gluonts-databricks-on-aws-26a285b9.md)
2. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
