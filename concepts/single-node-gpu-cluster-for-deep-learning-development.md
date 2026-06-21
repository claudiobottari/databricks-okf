---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: de967b3a4e4f0f999272a6362faf6e5f22eccb059acdbb14ba736dc2bffda752
  pageDirectory: concepts
  sources:
    - best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - single-node-gpu-cluster-for-deep-learning-development
    - SNGCFDLD
  citations:
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
    - file: get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md
title: Single Node GPU Cluster for Deep Learning Development
description: Best practice of using a single-node GPU cluster (driver only) for fast, cost-effective iterative deep learning model development before scaling to distributed training.
tags:
  - deep-learning
  - clusters
  - cost-optimization
timestamp: "2026-06-19T17:41:14.627Z"
---

# Single Node GPU Cluster for Deep Learning Development

A **Single Node GPU Cluster** is a compute cluster consisting of one driver node equipped with one or more GPUs, with no separate worker nodes. On Databricks, this is configured as a Single Node Cluster (driver-only) using a GPU instance type or as a serverless GPU session such as the [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md).

## Overview

A single-node GPU cluster provides all GPU resources on a single machine. This design eliminates network communication overhead between nodes, making it typically faster and more cost-effective for deep learning model development than a multi‑node setup with one GPU per node. For example, one node with 4 GPUs is likely to train faster than four worker nodes with 1 GPU each, because distributed training across nodes incurs cross‑node communication delays. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Benefits

- **Faster iteration** – No inter‑node network latency; all GPUs share a high‑bandwidth interconnect within the node.
- **Cost‑effective** – Avoids the overhead of maintaining multiple worker nodes; ideal for development and small‑ to medium‑size workloads.
- **Simplified setup** – A single node is easier to monitor and debug than a multi‑node cluster.
- **Pre‑configured environment** – Databricks Runtime for Machine Learning includes GPU drivers, TensorFlow, PyTorch, Keras, and other deep learning libraries. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## When to Use a Single Node GPU Cluster

A single node GPU cluster is the recommended starting point for:

- Fast, iterative model development and experimentation.
- Training models on small‑ to medium‑size datasets.
- Hyperparameter tuning and prototyping.

If the dataset is large enough that training becomes slow on a single machine, consider moving to [Multi-Node Distributed Training](/concepts/multi-gpu-distributed-training-api.md) or scaling up to a serverless configuration like the 8xH100 single node for larger models. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Configurations

### Traditional Single Node Cluster (Driver Only)

On Databricks, create a GPU Cluster and select **Single Node** mode. The cluster consists of one node (the driver) with GPUs. Supported GPU types include [A100 GPUs](/concepts/a100-gpu-support-on-databricks.md) and other instances available across clouds. A100 GPUs are efficient for many deep learning tasks but may have limited availability; contact your cloud provider to reserve capacity. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Serverless 8xH100 Single‑Node Configuration

Databricks Serverless GPU compute offers a predefined 8xH100 single‑node configuration that provisions eight NVIDIA H100 80 GB HBM3 GPUs on a single node. This configuration is intended for large model training where high FLOPS and large GPU memory are needed. To select it from a notebook:

1. Choose **Serverless GPU** from the compute selector.
2. In the **Environment** tab, select **8xH100** for your accelerator.
3. Choose the **AI v5** environment.
4. Click **Apply**.

After connecting, use `nvidia-smi` to verify eight H100 GPUs. The `serverless_gpu` library provides a `@distributed` decorator to run functions across all GPUs on the node. ^[get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md]

## Limitations

- Single node GPU clusters are not suitable for very large datasets or models that require the combined memory and compute of many nodes.
- For training models in the [20B to 120B+ Parameter Model Training](/concepts/20b-to-120b-parameter-model-training.md) range, single‑node configurations may be insufficient; distributed strategies like [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) or [DeepSpeed](/concepts/deepspeed.md) across multiple nodes are required.

## Related Concepts

- GPU Scheduling – Optimizing GPU utilization within a node.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – A common parallelism strategy used on multi‑GPU single nodes.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – Pre‑built runtime with GPU support.
- Cluster Policies – Guide users to select single‑node or multi‑node clusters appropriately.

## Sources

- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
- get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md

# Citations

1. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
2. [get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws.md](/references/get-started-serverless-gpu-compute-with-h100-gpus-databricks-on-aws-047f70e1.md)
