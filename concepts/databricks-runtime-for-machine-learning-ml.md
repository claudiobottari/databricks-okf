---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 29dcd82ca9a0e59d8ca181738ffb227fa4559658761a95588bb06cac21eab03a
  pageDirectory: concepts
  sources:
    - pytorch-databricks-on-aws.md
    - use-xgboost-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-runtime-for-machine-learning-ml
    - DRFML(
    - Databricks Machine Learning Runtime
  citations:
    - file: pytorch-databricks-on-aws.md
    - file: use-xgboost-on-databricks-databricks-on-aws.md
title: Databricks Runtime for Machine Learning (ML)
description: A pre-configured Databricks runtime that includes PyTorch and other ML libraries
tags:
  - databricks
  - machine-learning
  - runtime
timestamp: "2026-06-19T20:00:18.667Z"
---

# Databricks Runtime for Machine Learning (ML)

**Databricks Runtime for Machine Learning (ML)** is a pre-configured cluster runtime environment on Databricks that includes popular machine learning and deep learning libraries. It eliminates the need for users to manually install packages like PyTorch and [XGBoost](/concepts/xgboostspark-module.md), allowing teams to start model training immediately after creating a cluster. ^[pytorch-databricks-on-aws.md, use-xgboost-on-databricks-databricks-on-aws.md]

## Pre-installed Libraries

Databricks Runtime ML includes PyTorch, a GPU-accelerated tensor computation library for building deep learning networks. Users can create a cluster and begin using PyTorch without any additional installation steps; the exact version is listed in the [release notes](https://docs.databricks.com/aws/en/release-notes/runtime/). ^[pytorch-databricks-on-aws.md]

The runtime also bundles XGBoost libraries for both Python and Scala, supporting both single‑node and distributed training workflows. For the version of XGBoost included in a specific Databricks Runtime ML release, refer to the same release notes. ^[use-xgboost-on-databricks-databricks-on-aws.md]

## Benefits

- **Zero‑effort setup**: Because PyTorch and XGBoost are pre‑installed, data scientists and engineers can focus on model development rather than environment configuration. ^[pytorch-databricks-on-aws.md, use-xgboost-on-databricks-databricks-on-aws.md]
- **Single‑node and distributed training**: The runtime supports both single‑node workloads (e.g., using `torch.nn.DataParallel` or the `xgboost` Python package) and distributed training with [TorchDistributor](/concepts/torchdistributor.md) (for PyTorch) or PySpark-based XGBoost estimators. ^[pytorch-databricks-on-aws.md, use-xgboost-on-databricks-databricks-on-aws.md]
- **GPU acceleration**: Deep learning models can leverage GPU clusters out‑of‑the‑box, and the runtime includes CUDA support for PyTorch. ^[pytorch-databricks-on-aws.md]

## Usage

To use Databricks Runtime for ML:

1. When creating a cluster, select the **Databricks Runtime for Machine Learning** version from the runtime drop‑down.
2. Choose the appropriate cluster mode (single node for smaller workloads, multi‑node for distributed training).
3. Start a notebook or job – the ML libraries are immediately available.

If you must use the standard Databricks Runtime instead, you can install PyTorch as a [PyPI library](https://docs.databricks.com/aws/en/libraries/) (on GPU clusters: `torch` and `torchvision`; on CPU clusters: CPU‑only wheel files). XGBoost can similarly be added via `%pip install xgboost==<version>`. ^[pytorch-databricks-on-aws.md, use-xgboost-on-databricks-databricks-on-aws.md]

## Related Concepts

- PyTorch
- [XGBoost](/concepts/xgboostspark-module.md)
- Databricks Runtime
- [TorchDistributor](/concepts/torchdistributor.md)
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- Single Node Cluster

## Sources

- pytorch-databricks-on-aws.md
- use-xgboost-on-databricks-databricks-on-aws.md

# Citations

1. [pytorch-databricks-on-aws.md](/references/pytorch-databricks-on-aws-b092c491.md)
2. [use-xgboost-on-databricks-databricks-on-aws.md](/references/use-xgboost-on-databricks-databricks-on-aws-87750cc6.md)
