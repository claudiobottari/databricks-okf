---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1a1f8a79f5ef84834ef1921ea21e13f8f95d0687fe581104c429fc005293032a
  pageDirectory: concepts
  sources:
    - classic-machine-learning-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-serverless-gpu-cluster
    - DSGC
    - serverless GPU cluster
  citations:
    - file: classic-machine-learning-databricks-on-aws.md
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
title: Databricks Serverless GPU Cluster
description: On-demand GPU compute infrastructure on Databricks used for training deep learning forecasting models
tags:
  - infrastructure
  - gpu
  - databricks
timestamp: "2026-06-19T17:43:09.770Z"
---

Here is the wiki page for "Databricks Serverless GPU Cluster", written based solely on the provided source material.

---

## Databricks Serverless GPU Cluster

A **Databricks Serverless GPU Cluster** is a compute resource on the Databricks platform that provisions GPU-accelerated infrastructure on demand, without requiring users to manage or configure underlying cluster instances. It is designed for deep learning and other GPU-intensive workloads, such as large model training and probabilistic time-series forecasting. ^[classic-machine-learning-databricks-on-aws.md]

### Overview

Serverless GPU clusters eliminate the operational overhead of traditional cluster management. Users select a GPU configuration from the compute selector, and Databricks automatically provisions the required resources for the duration of the workload. This model is particularly suited for tasks that benefit from high floating-point operations per second (FLOPS) and high-bandwidth memory (HBM), such as training large language models or running distributed training jobs. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

### Available Configurations

Databricks Serverless GPU clusters offer several pre-defined configurations. One notable configuration is the **8xH100 Single-Node Configuration**, which provisions eight NVIDIA H100 80GB HBM3 GPUs on a single compute node, providing 640 GB of total GPU memory. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

To select a configuration from a notebook:
1. From the compute selector, choose **Serverless GPU**.
2. In the **Environment** tab, select the desired accelerator (e.g., **8xH100**).
3. Choose the appropriate environment (e.g., **AI v5**), which contains required libraries for distributed GPU workloads.
4. Click **Apply**.

^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

### Use Cases

Serverless GPU clusters are suitable for a variety of deep learning tasks, including:
- **Large model training**: Workloads that require high throughput and large GPU memory, such as Large language model (LLM) training. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]
- **Multi-GPU distributed training**: Jobs that benefit from parallel processing across multiple GPUs on a single node. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]
- **Probabilistic time-series forecasting**: For example, using GluonTS's DeepAR model for electricity consumption forecasting. ^[classic-machine-learning-databricks-on-aws.md]

### Distributed Programming with the `@distributed` Decorator

The `serverless_gpu` Python library provides a `@distributed` decorator for running functions across multiple GPUs on a single node. The `runtime` module provides access to local and global GPU ranks for coordinating work. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

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

- `gpus=8` specifies that the function runs on 8 processes, one per GPU.
- `rt.get_local_rank()` returns the rank of the GPU within the node.
- `rt.get_global_rank()` returns the global rank across all processes.

### Verification

Users can verify the GPU configuration by running the `nvidia-smi` command within the notebook. For an 8xH100 configuration, each GPU reports as an NVIDIA H100 80GB HBM3 with 81,559 MiB of total memory and a maximum power draw of 700 W. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

### Related Concepts

- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md)
- H100 GPU Support on Databricks
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md)
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)

### Sources

- classic-machine-learning-databricks-on-aws.md
- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md

# Citations

1. [classic-machine-learning-databricks-on-aws.md](/references/classic-machine-learning-databricks-on-aws-838aa327.md)
2. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
