---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c43cacf2bbfd391db6e282cb2fae806705a0f14a2da3ae458c03735d83c39133
  pageDirectory: concepts
  sources:
    - horovodrunner-examples-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - horovodrunner-deprecation-on-databricks
    - HDOD
  citations:
    - file: horovodrunner-examples-databricks-on-aws.md
title: HorovodRunner deprecation on Databricks
description: Horovod and HorovodRunner are deprecated on Databricks as of ML releases after 15.4 LTS; users must migrate to alternative distributed training APIs.
tags:
  - machine-learning
  - distributed-training
  - databricks
  - deprecation
timestamp: "2026-06-19T19:05:55.531Z"
---

# HorovodRunner Deprecation on Databricks

**HorovodRunner** was a Databricks utility that simplified running [Horovod](https://horovod.ai/) distributed training jobs within a Spark cluster. It allowed users to scale deep learning training across multiple GPUs using Horovod’s collective communication primitives, often used with TensorFlow and PyTorch. ^[horovodrunner-examples-databricks-on-aws.md]

## Deprecation Announcement

Horovod and HorovodRunner are now **deprecated** on Databricks. Releases after **15.4 LTS ML** will not have the HorovodRunner package pre-installed. Existing users must migrate to supported alternatives before upgrading beyond that runtime version. ^[horovodrunner-examples-databricks-on-aws.md]

## Recommended Alternatives

For distributed deep learning, Databricks recommends the following built-in APIs, depending on the framework in use:

- **PyTorch**: Use [TorchDistributor](https://docs.databricks.com/aws/en/machine-learning/train-model/distributed-training/#torch-distributor), the native Databricks wrapper for PyTorch’s `DistributedDataParallel` (DDP). ^[horovodrunner-examples-databricks-on-aws.md]
- **TensorFlow**: Use the `tf.distribute.Strategy` API, which provides high-level distribution strategies such as `MirroredStrategy` and `MultiWorkerMirroredStrategy`. ^[horovodrunner-examples-databricks-on-aws.md]

Both alternatives are actively maintained and integrate directly with Databricks clusters without requiring a separate Horovod installation.

## Migration Guidance

Users currently relying on HorovodRunner should:

1. Assess their existing training code and framework (PyTorch or TensorFlow).
2. Refactor the training loop to use the corresponding recommended API.
3. Test on a non‑ML runtime (or a runtime ≤ 15.4 LTS ML) until the migration is complete.
4. Avoid upgrading to runtime versions **after 15.4 LTS ML** until the migration is finished, as HorovodRunner will no longer be available as a pre‑installed package. ^[horovodrunner-examples-databricks-on-aws.md]

For step‑by‑step examples, refer to the Databricks documentation on distributed training with TorchDistributor or `tf.distribute.Strategy`.

## Related Concepts

- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- [TorchDistributor](/concepts/torchdistributor.md)
- [tf.distribute.Strategy](/concepts/tfdistributestrategy.md)
- [PyTorch DistributedDataParallel](/concepts/distributed-data-parallel-ddp.md)
- TensorFlow MirroredStrategy
- GPU Training on Databricks
- ML Runtime Versioning

## Sources

- horovodrunner-examples-databricks-on-aws.md

# Citations

1. [horovodrunner-examples-databricks-on-aws.md](/references/horovodrunner-examples-databricks-on-aws-de1151e3.md)
