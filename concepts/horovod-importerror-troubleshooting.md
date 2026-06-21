---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b0d4a75ca96d526d30cdc00bd258fd2886b2b441fe9f845d1d168c2886cc9ab6
  pageDirectory: concepts
  sources:
    - horovod-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - horovod-importerror-troubleshooting
    - HIT
  citations:
    - file: horovod-databricks-on-aws.md
title: Horovod ImportError Troubleshooting
description: A common error where importing horovod.torch or horovod.tensorflow fails because the extension was not built during installation, typically due to missing required libraries at compile time.
tags:
  - troubleshooting
  - horovod
  - installation-errors
timestamp: "2026-06-19T10:48:04.875Z"
---

# Horovod ImportError Troubleshooting

**Horovod ImportError Troubleshooting** addresses the common error `ImportError: Extension horovod.{torch|tensorflow} has not been built` that occurs when importing Horovod with a specific deep learning framework (PyTorch or TensorFlow) in Databricks. This page explains the root cause, environment prerequisites, and step-by-step resolution. ^[horovod-databricks-on-aws.md]

## Error Message

The error appears as:

```
ImportError: Extension horovod.{torch|tensorflow} has not been built
```

The exact extension name depends on the framework used (e.g., `horovod.torch` or `horovod.tensorflow`). ^[horovod-databricks-on-aws.md]

## Cause

Horovod is compiled at installation time. The framework-specific extensions (`horovod.torch`, `horovod.tensorflow`) are only compiled if the corresponding deep learning package (PyTorch or TensorFlow) is already present in the environment when Horovod is installed. If Horovod is installed (or reinstalled) before the framework, those extensions are not built, leading to the `ImportError`. ^[horovod-databricks-on-aws.md]

## Environment Prerequisites

Before attempting any fix, verify the following:

- The cluster runs **Databricks Runtime ML** (Horovod comes pre-installed on these runtimes). ^[horovod-databricks-on-aws.md]
- The target deep learning framework (PyTorch or TensorFlow) is already installed. On Databricks Runtime ML, both are included by default, but manual environment modifications may remove them.

## Resolution Steps

1. **Uninstall Horovod**  
   Use `%pip` to remove the existing Horovod installation:
   ```python
   %pip uninstall -y horovod
   ```
   ^[horovod-databricks-on-aws.md]

2. **Install `cmake`**  
   `cmake` is required for compiling Horovod:
   ```python
   %pip install cmake
   ```
   ^[horovod-databricks-on-aws.md]

3. **Reinstall Horovod**  
   Reinstall Horovod using `%pip`. The default version (pre-packaged with the runtime) will be pulled automatically:
   ```python
   %pip install horovod
   ```
   Ensure that the deep learning framework you intend to use (PyTorch or TensorFlow) is still installed in the current environment before running this step. ^[horovod-databricks-on-aws.md]

After these steps, the extension should compile correctly, and the import should succeed.

## Deprecation Notice

Horovod and [HorovodRunner](/concepts/horovodrunner.md) are now deprecated. Releases after Databricks Runtime 15.4 LTS ML will not have Horovod pre-installed. For distributed deep learning, Databricks recommends:

- **[TorchDistributor](/concepts/torchdistributor.md)** for distributed training with PyTorch.
- **`tf.distribute.Strategy`** API for distributed training with TensorFlow.

^[horovod-databricks-on-aws.md]

## Related Concepts

- [HorovodRunner](/concepts/horovodrunner.md) — High-level API for distributed training with Horovod.
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Overview of distributed deep learning on Databricks.
- [TorchDistributor](/concepts/torchdistributor.md) — Recommended alternative for PyTorch distributed training.
- [TensorFlow Strategy](/concepts/tensorflowdistributestrategy.md) — Recommended alternative for TensorFlow distributed training.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The pre-configured runtime that includes Horovod.
- Install a different version of Horovod — Advanced steps for custom Horovod builds.

## Sources

- horovod-databricks-on-aws.md

# Citations

1. [horovod-databricks-on-aws.md](/references/horovod-databricks-on-aws-49662285.md)
