---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: df82231ce297d9a6acea5ddc6fe56f1ab92e7b795ded4cbdfcd3c440c4e14721
  pageDirectory: concepts
  sources:
    - pytorch-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - single-node-clusters-for-pytorch
    - SNCFP
    - Single Node Clusters
    - Single Node cluster
  citations:
    - file: pytorch-databricks-on-aws.md
title: Single Node Clusters for PyTorch
description: Using single-node Databricks clusters to test and migrate single-machine PyTorch workflows
tags:
  - databricks
  - pytorch
  - clusters
timestamp: "2026-06-19T20:00:41.545Z"
---

# Single Node Clusters for PyTorch

**Single Node Clusters for PyTorch** refers to the use of a Single Node Cluster configuration on Databricks to run PyTorch training workloads that were originally designed for single-machine workflows. This setup is particularly useful for testing and migrating local machine learning code to the Databricks platform without requiring distributed computing infrastructure. ^[pytorch-databricks-on-aws.md]

## Overview

PyTorch is a Python package that provides GPU-accelerated tensor computation and high-level functionalities for building deep learning networks. For licensing details, see the PyTorch license on GitHub. ^[pytorch-databricks-on-aws.md]

To test and migrate single-machine workflows, Databricks recommends using a Single Node cluster. For distributed training options for deep learning, refer to the distributed training documentation. ^[pytorch-databricks-on-aws.md]

## PyTorch Installation

### Databricks Runtime for ML

[Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) includes PyTorch by default, so you can create a cluster and start using PyTorch immediately. For the version of PyTorch installed in a specific Databricks Runtime ML version, see the release notes. ^[pytorch-databricks-on-aws.md]

### Databricks Runtime (Standard)

Databricks recommends using the PyTorch included in Databricks Runtime for Machine Learning. However, if you must use the standard Databricks Runtime, PyTorch can be installed as a Databricks PyPI library. The following example shows how to install PyTorch 1.5.0: ^[pytorch-databricks-on-aws.md]

- On GPU clusters, install `pytorch` and `torchvision` by specifying:
  - `torch==1.5.0`
  - `torchvision==0.6.0`
- On CPU clusters, install `pytorch` and `torchvision` using the following [Python Wheel Files](/concepts/python-wheel-files.md):
  - `https://download.pytorch.org/whl/cpu/torch-1.5.0%2Bcpu-cp37-cp37m-linux_x86_64.whl`
  - `https://download.pytorch.org/whl/cpu/torchvision-0.6.0%2Bcpu-cp37-cp37m-linux_x86_64.whl`

## Monitoring with TensorBoard

To monitor and debug PyTorch models, consider using [TensorBoard](/concepts/tensorboard-on-databricks.md), which is supported on Databricks. ^[pytorch-databricks-on-aws.md]

## Related Concepts

- Single Node Cluster
- PyTorch
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- [TensorBoard](/concepts/tensorboard-on-databricks.md)
- [TorchDistributor](/concepts/torchdistributor.md)

## Sources

- pytorch-databricks-on-aws.md

# Citations

1. [pytorch-databricks-on-aws.md](/references/pytorch-databricks-on-aws-b092c491.md)
