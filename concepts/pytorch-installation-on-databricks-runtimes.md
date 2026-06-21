---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dd5bc38c5ac85a077c61e386e2500ec48dec0f87409238f84d8b37c335964bcf
  pageDirectory: concepts
  sources:
    - pytorch-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pytorch-installation-on-databricks-runtimes
    - PIODR
  citations:
    - file: pytorch-databricks-on-aws.md
title: PyTorch Installation on Databricks Runtimes
description: Methods for installing PyTorch on Databricks Runtime vs Databricks Runtime for ML, including GPU and CPU cluster differences
tags:
  - installation
  - pytorch
  - databricks
timestamp: "2026-06-19T20:00:27.636Z"
---

# PyTorch Installation on Databricks Runtimes

**PyTorch Installation on Databricks Runtimes** describes the methods for installing and using the PyTorch deep learning framework on Databricks clusters. PyTorch provides GPU-accelerated tensor computation and high-level functionalities for building deep learning networks. ^[pytorch-databricks-on-aws.md]

## Overview

PyTorch is included in [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) (Databricks Runtime ML). If you are using the standard Databricks Runtime, PyTorch must be installed manually as a PyPI library. Databricks recommends using Databricks Runtime ML whenever possible, as it includes PyTorch pre-installed and ready to use. ^[pytorch-databricks-on-aws.md]

## Installation Methods

### Databricks Runtime for ML

Databricks Runtime for Machine Learning includes PyTorch by default. You can create a cluster using Databricks Runtime ML and start using PyTorch immediately without any additional installation steps. For the specific version of PyTorch included in your Databricks Runtime ML version, refer to the Databricks Runtime release notes. ^[pytorch-databricks-on-aws.md]

### Standard Databricks Runtime

If you must use the standard Databricks Runtime, PyTorch can be installed as a Databricks PyPI library. The installation method differs based on whether you are using GPU or CPU clusters. ^[pytorch-databricks-on-aws.md]

#### GPU Clusters

On GPU clusters, install `pytorch` and `torchvision` by specifying the following PyPI packages:

- `torch==1.5.0`
- `torchvision==0.6.0`

^[pytorch-databricks-on-aws.md]

#### CPU Clusters

On CPU clusters, install `pytorch` and `torchvision` using the following [Python Wheel Files](/concepts/python-wheel-files.md):

```
https://download.pytorch.org/whl/cpu/torch-1.5.0%2Bcpu-cp37-cp37m-linux_x86_64.whl
https://download.pytorch.org/whl/cpu/torchvision-0.6.0%2Bcpu-cp37-cp37m-linux_x86_64.whl
```

^[pytorch-databricks-on-aws.md]

## Single Node and Distributed Training

For testing and migrating single-machine workflows, use a [Single Node cluster](/concepts/single-node-clusters-for-pytorch.md). For distributed training options, see the [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) documentation. ^[pytorch-databricks-on-aws.md]

## Monitoring and Debugging

To monitor and debug your PyTorch models, consider using [TensorBoard](/concepts/tensorboard-on-databricks.md), which is supported on Databricks. ^[pytorch-databricks-on-aws.md]

## Related Concepts

- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- [TensorBoard](/concepts/tensorboard-on-databricks.md)
- [PyTorch DistributedDataParallel](/concepts/distributed-data-parallel-ddp.md)
- [TorchDistributor](/concepts/torchdistributor.md)

## Sources

- pytorch-databricks-on-aws.md

# Citations

1. [pytorch-databricks-on-aws.md](/references/pytorch-databricks-on-aws-b092c491.md)
