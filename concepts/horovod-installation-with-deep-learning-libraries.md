---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4f11cc41cbd4b9f38caa67b06225001fe75572040678044f1f6ab54f16ddbf44
  pageDirectory: concepts
  sources:
    - horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - horovod-installation-with-deep-learning-libraries
    - HIWDLL
  citations:
    - file: horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
title: Horovod Installation with Deep Learning Libraries
description: Horovod must be reinstalled after upgrading or downgrading TensorFlow, Keras, or PyTorch, using the same compiler that the deep learning library was built with, and specifying GPU allreduce backend (NCCL).
tags:
  - installation
  - tensorflow
  - pytorch
timestamp: "2026-06-19T19:06:27.630Z"
---

# Horovod Installation with Deep Learning Libraries

**Horovod Installation with Deep Learning Libraries** refers to the process of compiling and installing the Horovod distributed training framework against specific deep learning libraries such as TensorFlow, Keras, or PyTorch. Because Horovod relies on the underlying deep learning library for gradient computation, it must be compiled against the installed version of that library to function correctly. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## When Reinstallation Is Required

If you upgrade or downgrade TensorFlow, Keras, or PyTorch on a Databricks cluster, you must reinstall Horovod so that it is compiled against the newly installed library version. Failure to do so can cause compatibility issues or runtime errors. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

Databricks recommends using the init script from the [TensorFlow installation instructions](https://docs.databricks.com/aws/en/machine-learning/train-model/tensorflow) and appending Horovod‑specific installation code to the end of it. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Installation Steps

The following example demonstrates how to install Horovod with TensorFlow support on a Databricks cluster using an init script: ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

```bash
add-apt-repository -y ppa:ubuntu-toolchain-r/test
apt update
# Using the same compiler that TensorFlow was built with to compile Horovod
apt install g++-7 -y
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 60
HOROVOD_GPU_ALLREDUCE=NCCL HOROVOD_CUDA_HOME=/usr/local/cuda pip install horovod==0.18.1 --force-reinstall --no-deps --no-cache-dir
```

### Key Installation Options

- **`HOROVOD_GPU_ALLREDUCE=NCCL`**: Configures Horovod to use NVIDIA NCCL for GPU allreduce operations, which provides optimal performance on NVIDIA GPUs. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]
- **`HOROVOD_CUDA_HOME=/usr/local/cuda`**: Specifies the CUDA installation directory for compiling GPU‑aware operations. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]
- **`--force-reinstall`**: Ensures Horovod is fully reinstalled even if a previous version exists. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]
- **`--no-deps`**: Prevents pip from automatically upgrading dependency packages during reinstallation. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Compiler Requirements

Horovod must be compiled with the same C++ compiler that was used to build the target deep learning library. In the example above, TensorFlow is compiled with g++-7, so the installation uses `update-alternatives` to set g++-7 as the default compiler before installing Horovod. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Installation for Different Library Combinations

The general approach shown above can be adapted for other deep learning library combinations. See the [Horovod installation instructions](https://github.com/horovod/horovod#install) for guidance on working with PyTorch and other libraries. The key environment variables and compiler settings vary by library. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Related Concepts

- [HorovodRunner](/concepts/horovodrunner.md) — The Databricks API for running Horovod training jobs as Spark jobs.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — General concepts of scaling deep learning across multiple GPUs and nodes.
- NCCL — NVIDIA Collective Communications Library, used by Horovod for GPU communication.
- Init Scripts on Databricks — Mechanism for installing custom libraries and dependencies on cluster startup.
- [TensorFlow Installation on Databricks](/concepts/tensorflow-on-databricks.md) — Official instructions for setting up TensorFlow on the platform.

## Sources

- horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md

# Citations

1. [horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md](/references/horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws-bdb09a88.md)
