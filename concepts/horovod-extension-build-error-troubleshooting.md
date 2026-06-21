---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 485e409228ba6890e70426737ae4e404499a27f2e23c39e9bbea4894a2ecb522
  pageDirectory: concepts
  sources:
    - horovod-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - horovod-extension-build-error-troubleshooting
    - HEBET
  citations:
    - file: horovod-databricks-on-aws.md
title: Horovod Extension Build Error Troubleshooting
description: Common ImportError for horovod.{torch|tensorflow} caused by missing required libraries at install time, resolved by reinstalling Horovod after the required framework.
tags:
  - troubleshooting
  - installation
  - databricks
timestamp: "2026-06-19T19:05:22.691Z"
---

# Horovod Extension Build Error Troubleshooting

**Horovod Extension Build Error Troubleshooting** covers the diagnosis and resolution of `ImportError` issues that occur when attempting to use Horovod's framework-specific extensions (such as `horovod.torch` or `horovod.tensorflow`) after installation.

## Overview

When importing a Horovod framework extension, users may encounter the following error:

```
ImportError: Extension horovod.{torch|tensorflow} has not been built
```

This error indicates that Horovod was installed before the required deep learning framework (PyTorch or TensorFlow) was present in the environment. Since Horovod compiles its framework-specific extensions during installation, these extensions will not be built if the corresponding packages are not available at installation time. ^[horovod-databricks-on-aws.md]

## Common Causes

The primary cause is an incorrect installation order. Horovod's extensions are compiled as part of its installation process. If a user installs or upgrades Horovod when PyTorch or TensorFlow is not yet installed (or is subsequently removed or changed), the compiled extensions will be missing or mismatched with the framework version. ^[horovod-databricks-on-aws.md]

On Databricks, this typically occurs when:
- An environment update goes wrong and breaks the dependency order
- A user manually installs a different version of Horovod without first ensuring the framework is present
- The environment is not a [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) cluster, which pre-installs these dependencies

## Resolution Steps

To resolve the import error and rebuild Horovod with the correct extensions, follow these steps in order:

### 1. Verify the Cluster Type

Ensure you are using a [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) cluster. Horovod and its framework extensions are pre-installed and tested on these runtimes. Using a non-ML cluster will require manual installation of all dependencies. ^[horovod-databricks-on-aws.md]

### 2. Confirm Framework Installation

Verify that PyTorch or TensorFlow is already installed in the environment:

```python
import torch  # or import tensorflow
```

If the framework is not present, install it first before proceeding. ^[horovod-databricks-on-aws.md]

### 3. Uninstall Horovod

Remove the existing Horovod installation that was built without the required extensions:

```python
%pip uninstall -y horovod
```

^[horovod-databricks-on-aws.md]

### 4. Install cmake

The `cmake` build tool is required for compiling Horovod from source:

```python
%pip install cmake
```

^[horovod-databricks-on-aws.md]

### 5. Reinstall Horovod

Reinstall Horovod with the appropriate framework flags so that the extensions are compiled against the currently installed frameworks:

#### CPU cluster:
```sh
HOROVOD_WITH_MPI=1 HOROVOD_WITH_TENSORFLOW=1 HOROVOD_WITH_PYTORCH=1 pip install horovod
```

#### GPU cluster:
```sh
HOROVOD_GPU_OPERATIONS=NCCL HOROVOD_WITH_MPI=1 HOROVOD_WITH_TENSORFLOW=1 HOROVOD_WITH_PYTORCH=1 pip install horovod
```

^[horovod-databricks-on-aws.md]

## Advanced: Recompiling from Source

For users who need to install a specific version of Horovod (upgrade or downgrade), the recommended approach involves downloading the source code and compiling with the correct flags. This process includes:

1. Uninstalling the current Horovod version
2. Installing CUDA development libraries (for GPU-accelerated clusters) to ensure compatibility
3. Cloning the desired Horovod version from GitHub
4. Building the Python wheel with framework flags
5. Installing the wheel using `%pip install --no-cache-dir`

For detailed steps with specific version examples, refer to the "Install a different version of Horovod" section in the official documentation. ^[horovod-databricks-on-aws.md]

## Deprecation Notice

Horovod and [HorovodRunner](/concepts/horovodrunner.md) are now deprecated. Releases after Databricks Runtime 15.4 LTS ML will not have Horovod pre-installed. Databricks recommends migrating to [TorchDistributor](/concepts/torchdistributor.md) for distributed training with PyTorch or the `tf.distribute.Strategy` API for distributed training with TensorFlow. ^[horovod-databricks-on-aws.md]

## Related Concepts

- [HorovodRunner](/concepts/horovodrunner.md) — The deprecated distributed training runner for Horovod workloads
- [Distributed Deep Learning](/concepts/distributed-deep-learning-on-databricks.md) — Overview of distributed training approaches on Databricks
- [TorchDistributor](/concepts/torchdistributor.md) — The recommended PyTorch distributed training API
- TensorFlow Distributed Training — The recommended TensorFlow distributed training API
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The runtime environment with pre-installed ML libraries

## Sources

- horovod-databricks-on-aws.md

# Citations

1. [horovod-databricks-on-aws.md](/references/horovod-databricks-on-aws-49662285.md)
