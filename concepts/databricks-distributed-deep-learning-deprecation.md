---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4520805d8d73fb1da46f0672903575aa0e1052ad941a0f15dde490e106d51675
  pageDirectory: concepts
  sources:
    - horovod-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-distributed-deep-learning-deprecation
    - DDDLD
  citations:
    - file: horovod-databricks-on-aws.md
title: Databricks Distributed Deep Learning Deprecation
description: Databricks deprecated Horovod and HorovodRunner after ML 15.4 LTS, recommending TorchDistributor for PyTorch and tf.distribute.Strategy for TensorFlow.
tags:
  - databricks
  - deprecation
  - deep-learning
timestamp: "2026-06-19T19:05:25.316Z"
---

# Databricks Distributed Deep Learning Deprecation

**Databricks Distributed Deep Learning Deprecation** refers to the formal end-of-life status of [Horovod](/concepts/horovod.md) and [HorovodRunner](/concepts/horovodrunner.md) as distributed training frameworks on the Databricks platform. As of Databricks Runtime 15.4 LTS ML and later releases, these packages are no longer pre-installed, and Databricks recommends migrating to alternative distributed training solutions. ^[horovod-databricks-on-aws.md]

## Deprecated Components

The following components are deprecated:

- **Horovod** — A distributed training framework for TensorFlow, Keras, and PyTorch. ^[horovod-databricks-on-aws.md]
- **HorovodRunner** — A Databricks-specific API for running Horovod training jobs. ^[horovod-databricks-on-aws.md]
- **`horovod.spark`** — The Spark ML pipeline estimator API for Keras and PyTorch. ^[horovod-databricks-on-aws.md]

## Timeline

Releases after **Databricks Runtime 15.4 LTS ML** will not have Horovod or HorovodRunner pre-installed. ^[horovod-databricks-on-aws.md]

## Recommended Alternatives

Databricks recommends the following replacements for distributed deep learning:

| Framework | Recommended Alternative |
|-----------|------------------------|
| PyTorch | [TorchDistributor](/concepts/torchdistributor.md) for distributed training |
| TensorFlow | `tf.distribute.Strategy` API for distributed training |

^[horovod-databricks-on-aws.md]

## Impact on Existing Workloads

Users with existing Horovod-based workloads should migrate to the recommended alternatives. For users who still need to use Horovod on older Databricks Runtime ML versions, the package remains available as pre-installed on those versions. ^[horovod-databricks-on-aws.md]

## Custom Installation (Not Recommended)

While Horovod can still be manually installed on Databricks Runtime ML clusters by recompiling from source, this approach is not recommended for new workloads. The manual installation process involves:

1. Uninstalling the pre-installed Horovod version
2. Installing CUDA development libraries (for GPU clusters)
3. Cloning the Horovod source code and compiling with appropriate flags
4. Reinstalling Horovod from the compiled wheel

^[horovod-databricks-on-aws.md]

## Troubleshooting

If importing `horovod.{torch|tensorflow}` raises `ImportError: Extension horovod.{torch|tensorflow} has not been built`, this typically indicates that Horovod was installed before the required library (PyTorch or TensorFlow). The solution involves ensuring the required framework is installed, then uninstalling and reinstalling Horovod with `cmake` available. ^[horovod-databricks-on-aws.md]

## Related Concepts

- [TorchDistributor](/concepts/torchdistributor.md) — The recommended PyTorch distributed training solution
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — A common PyTorch parallelism strategy
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Memory-efficient training for large models
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Overview of distributed training approaches on Databricks
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The ML-optimized runtime version affected by this deprecation

## Sources

- horovod-databricks-on-aws.md

# Citations

1. [horovod-databricks-on-aws.md](/references/horovod-databricks-on-aws-49662285.md)
