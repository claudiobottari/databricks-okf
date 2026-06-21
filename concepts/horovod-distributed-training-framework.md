---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d07080979a1f0eb6b7b9b2caefba9187be51b48499c5c407f0b38b1215dd75ca
  pageDirectory: concepts
  sources:
    - horovod-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - horovod-distributed-training-framework
    - HDTF
    - Training Framework
  citations:
    - file: horovod-databricks-on-aws.md
title: Horovod Distributed Training Framework
description: Horovod is a distributed deep learning training framework supporting TensorFlow, Keras, and PyTorch, now deprecated on Databricks.
tags:
  - machine-learning
  - distributed-training
  - deep-learning
timestamp: "2026-06-19T19:05:08.338Z"
---

# Horovod Distributed Training Framework

**Horovod** is a distributed training framework for TensorFlow, Keras, and PyTorch that enables scaling deep learning models across multiple GPUs and nodes. Originally developed by Uber, Horovod uses a ring-allreduce algorithm for efficient gradient synchronization. Databricks has supported distributed deep learning training using HorovodRunner and the `horovod.spark` package. However, Horovod and HorovodRunner are now deprecated; releases after Databricks Runtime 15.4 LTS ML will not have this package pre-installed. Databricks recommends using [TorchDistributor](/concepts/torchdistributor.md) for distributed training with PyTorch or the `tf.distribute.Strategy` API for distributed training with TensorFlow. ^[horovod-databricks-on-aws.md]

## Requirements

Horovod is pre-installed on [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) clusters. To use Horovod, you must run on a Databricks Runtime ML cluster. ^[horovod-databricks-on-aws.md]

## Usage

To use Horovod on Databricks, you can leverage either HorovodRunner (for notebook-based distributed training) or the `horovod.spark` estimator API for Spark ML pipeline applications using Keras or PyTorch. The following documentation articles provide general information and example notebooks:

- [HorovodRunner: distributed deep learning with Horovod](https://docs.databricks.com/aws/en/archive/machine-learning/train-model/horovod-runner)
- [HorovodRunner examples](https://docs.databricks.com/aws/en/archive/machine-learning/train-model/horovod-runner-examples)
- [`horovod.spark`: distributed deep learning with Horovod](https://docs.databricks.com/aws/en/archive/machine-learning/train-model/horovod-spark)

^[horovod-databricks-on-aws.md]

## Installing a Different Version

To upgrade or downgrade Horovod from the pre-installed version on a Databricks Runtime ML cluster, you must recompile Horovod. The steps are:

1. Uninstall the current version: `%pip uninstall -y horovod`
2. (For GPU clusters) Install CUDA development libraries required for compilation, leaving package versions unchanged.
3. Download the desired version of Horovod's source code and compile with the appropriate flags (e.g., `HOROVOD_WITH_PYTORCH=1`, `HOROVOD_WITH_TENSORFLOW=1`). Example command:

   ```sh
   HOROVOD_VERSION=v0.21.3
   git clone --recursive https://github.com/horovod/horovod.git --branch ${HOROVOD_VERSION}
   cd horovod
   rm -rf build/ dist/
   HOROVOD_WITH_MPI=1 HOROVOD_WITH_TENSORFLOW=1 HOROVOD_WITH_PYTORCH=1 \
   sudo /databricks/python3/bin/python setup.py bdist_wheel
   ```

4. Use `%pip` to reinstall Horovod by specifying the generated wheel path.

^[horovod-databricks-on-aws.md]

## Troubleshooting

**Problem:** Importing `horovod.{torch|tensorflow}` raises `ImportError: Extension horovod.{torch|tensorflow} has not been built`.

**Solution:** This error typically occurs when Horovod is installed before the required library (PyTorch or TensorFlow). Since Horovod is compiled during installation, the framework-specific extensions are not compiled if those packages are absent at installation time. To fix:

1. Verify you are on a Databricks Runtime ML cluster.
2. Ensure the PyTorch or TensorFlow package is already installed.
3. Uninstall Horovod: `%pip uninstall -y horovod`.
4. Install `cmake`: `%pip install cmake`.
5. Reinstall Horovod.

^[horovod-databricks-on-aws.md]

## Related Concepts

- [TorchDistributor](/concepts/torchdistributor.md) — The recommended PyTorch distributed training API for Databricks.
- [tf.distribute.Strategy](/concepts/tfdistributestrategy.md) — The recommended TensorFlow distributed training API.
- [HorovodRunner](/concepts/horovodrunner.md) — Deprecated notebook-based interface for Horovod on Databricks.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The ML-optimized runtime that pre-installs Horovod.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — Native PyTorch distributed training approach.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Memory-efficient distributed training for large models.

## Sources

- horovod-databricks-on-aws.md

# Citations

1. [horovod-databricks-on-aws.md](/references/horovod-databricks-on-aws-49662285.md)
