---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c1c4fa5753726a2ca9437217f32bf5b93ce479fc00aa33698ad1b043c4c6d63b
  pageDirectory: concepts
  sources:
    - horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - horovodrunner-deprecation
    - horovodrunner-deprecation-on-databricks
    - HDOD
  citations:
    - file: horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
title: HorovodRunner Deprecation
description: Horovod and HorovodRunner are deprecated in Databricks ML runtime 15.4 LTS and later, with recommended replacements being TorchDistributor for PyTorch and tf.distribute.Strategy for TensorFlow.
tags:
  - databricks
  - deprecation
  - migration
timestamp: "2026-06-19T19:05:45.682Z"
---

# HorovodRunner Deprecation

**HorovodRunner Deprecation** refers to the planned removal of the pre‑installed Horovod and HorovodRunner packages from Databricks Runtime ML. As of Runtime 15.4 LTS ML, these packages are deprecated and will not be included in future releases. Users are advised to migrate to native distributed training frameworks. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Overview

HorovodRunner is a Databricks API that runs distributed deep learning workloads using the [Horovod](/concepts/horovod.md) framework. It integrates Horovod with Spark’s barrier execution mode, packaging training code on the driver and distributing it to workers via MPI. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]  
The API supports TensorFlow, Keras, and PyTorch models. However, Horovod and HorovodRunner are now deprecated and will not receive further development or bug fixes. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Deprecation Timeline

- **Current status**: Deprecated in all Databricks Runtime ML releases after 15.4 LTS. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]  
- **Future releases**: The packages will no longer be pre‑installed. Users who still require HorovodRunner can attempt to install it manually, but compatibility with newer runtime versions is not guaranteed. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Impact

### No New Features

Active development of HorovodRunner and the `horovod.spark` package has ceased. No new features, performance improvements, or security patches will be provided by Databricks. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

### Compatibility Risks

Because HorovodRunner depends on specific versions of deep learning libraries and MPI configurations, future Databricks Runtime ML updates may break existing workflows that rely on it. Known limitations of HorovodRunner (e.g., issues with workspace file imports when `np>1`, and MPI network communication errors) may become more severe as the runtime evolves. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Recommended Alternatives

Databricks officially recommends migrating to the following natively supported distributed training APIs:

- **[TorchDistributor](/concepts/torchdistributor.md)** – For distributed PyTorch training. It integrates with PyTorch’s `DistributedDataParallel` and is the preferred replacement for HorovodRunner when using PyTorch. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]  
- **`tf.distribute.Strategy` API** – For distributed TensorFlow training. Strategies such as `MirroredStrategy` and `MultiWorkerMirroredStrategy` provide built-in distribution support without external dependencies. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

Both alternatives are actively maintained and available in current Databricks Runtime ML versions.

## Migration Guidance

### For PyTorch Users

1. Replace HorovodRunner calls with the [TorchDistributor](/concepts/torchdistributor.md) API.  
2. Adapt training scripts to use `torch.distributed` primitives (e.g., `DistributedDataParallel`).  
3. Remove Horovod-specific code such as `hvd.init()`, `hvd.DistributedOptimizer`, and `hvd.broadcast_global_variables`.

### For TensorFlow / Keras Users

1. Replace HorovodRunner invocations with `tf.distribute.MultiWorkerMirroredStrategy` or `tf.distribute.MirroredStrategy`.  
2. Wrap model creation and training inside the strategy’s scope.  
3. Remove Horovod hooks and use TensorFlow’s native learning rate scaling and checkpoint logic.

### General Steps

- Audit existing notebooks and pipelines that use `HorovodRunner` or `horovod.spark`.  
- Test migrated code in a development environment with the target Databricks Runtime ML version.  
- Verify that distributed training performance meets requirements using the new API.

## Related Concepts

- [TorchDistributor](/concepts/torchdistributor.md)  
- [tf.distribute.Strategy](/concepts/tfdistributestrategy.md)  
- [Distributed Training on Databricks](/concepts/distributed-training-on-databricks.md)  
- [Horovod](/concepts/horovod.md)  
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md)

## Sources

- horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md

# Citations

1. [horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md](/references/horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws-bdb09a88.md)
