---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c74d28f868afa5043b3b94eb8c21e2e6fae18d8b6b26933fbcaf0d25746de687
  pageDirectory: concepts
  sources:
    - horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - horovod-installation-and-compilation-constraints
    - Compilation Constraints and Horovod Installation
    - HIACC
  citations:
    - file: horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
title: Horovod Installation and Compilation Constraints
description: Requirement to reinstall Horovod against the same compiler and CUDA version as the deep learning library (TensorFlow/PyTorch) after upgrading or downgrading those libraries.
tags:
  - installation
  - tensorflow
  - pytorch
  - horovod
timestamp: "2026-06-19T10:48:29.682Z"
---

# Horovod Installation and Compilation Constraints

**Horovod Installation and Compilation Constraints** refers to the specific requirements and limitations that arise when installing or reinstalling Horovod for distributed deep learning on Databricks, particularly after upgrading or downgrading the underlying deep learning framework (TensorFlow, Keras, or PyTorch). Because Horovod is compiled against a specific version of the framework, any change to that framework necessitates a full recompilation of Horovod with matching compiler toolchains and optional NCCL support.

## Overview

Horovod is a distributed training framework that wraps optimizers and uses MPI-like collective communication operations (allreduce, allgather). To function correctly, Horovod must be compiled against the same version of the deep learning library that it will be used with. This means that whenever a user upgrades or downgrades TensorFlow, Keras, or PyTorch on a Databricks cluster, Horovod must be reinstalled and recompiled from source against the new library version. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

**Deprecation notice:** Horovod and HorovodRunner are now deprecated. Releases after 15.4 LTS ML will not have this package pre-installed. Databricks recommends using [TorchDistributor](/concepts/torchdistributor.md) for distributed training with PyTorch or the `tf.distribute.Strategy` API for TensorFlow. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Why Recompilation Is Necessary

Horovod uses C++ extensions that link directly against the framework's runtime. If the framework version changes, the compiled symbols may be incompatible, leading to runtime errors or undefined behavior. A fresh `pip install horovod --force-reinstall --no-deps --no-cache-dir` (with appropriate environment variables) rebuilds Horovod's custom operations against the currently installed framework. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Supported Libraries and Compilation Flags

Horovod can be compiled to support GPU allreduce operations via NCCL. The standard compilation command for TensorFlow on Databricks uses:

- `HOROVOD_GPU_ALLREDUCE=NCCL` — enables NCCL-based GPU communication
- `HOROVOD_CUDA_HOME=/usr/local/cuda` — points to the CUDA installation directory
- A specific version of `g++` that matches the compiler used to build TensorFlow (typically `g++-7`)

These flags and compiler selection must match the environment in which TensorFlow was built. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Environment Variables

The following environment variables are essential for a successful Horovod reinstallation on Databricks GPU clusters:

| Variable | Purpose | Typical Value |
|----------|---------|---------------|
| `HOROVOD_GPU_ALLREDUCE` | Selects the allreduce backend | `NCCL` |
| `HOROVOD_CUDA_HOME` | Path to CUDA installation | `/usr/local/cuda` |

Additionally, the `gcc` alternative must be set to the same major version as the compiler used by the deep learning framework. For TensorFlow this is typically `gcc-7`. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Example Init Script

Databricks recommends appending Horovod reinstallation commands to the existing TensorFlow init script (or creating a dedicated init script). The following Bash snippet demonstrates the required steps:

```bash
add-apt-repository -y ppa:ubuntu-toolchain-r/test
apt update
apt install g++-7 -y
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 60
HOROVOD_GPU_ALLREDUCE=NCCL HOROVOD_CUDA_HOME=/usr/local/cuda pip install horovod==0.18.1 --force-reinstall --no-deps --no-cache-dir
```

^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

This script:
1. Adds the Ubuntu toolchain PPA to obtain `g++-7`.
2. Installs `g++-7`.
3. Sets `gcc` alternative to `gcc-7`.
4. Reinstalls Horovod against the current TensorFlow/PyTorch/Keras version with NCCL GPU support.

## Limitations

- **Compiler mismatch:** If the compiler used to build Horovod differs from the one used to build the deep learning library, runtime errors may occur. The `update-alternatives` step ensures alignment. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]
- **No dependency caching:** The `--no-deps --no-cache-dir` flags prevent pip from re‑resolving dependencies, which is necessary to avoid overwriting environment‑managed packages.
- **Deprecation:** Because Horovod is deprecated, new projects should use the recommended Distributed Training with PyTorch (TorchDistributor) or [Distributed Training with TensorFlow (tf.distribute.Strategy)](/concepts/distributed-training-with-tensorflow-2.md) instead. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Related Concepts

- [HorovodRunner](/concepts/horovodrunner.md) — The Databricks API for launching Horovod jobs as Spark barrier tasks.
- NCCL — NVIDIA Collective Communications Library, used as the GPU allreduce backend.
- CUDA Toolkit — Required for GPU support in Horovod.
- Deep Learning Framework Compatibility — Managing library version mismatches in distributed training.
- Init Scripts on Databricks — Mechanism to run custom setup code on cluster startup.

## Sources

- horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md

# Citations

1. [horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md](/references/horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws-bdb09a88.md)
