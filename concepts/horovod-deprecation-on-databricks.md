---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5ad36b577f58e86a5c07053859b0363c9d227a290f38f386f4fe569f496f7664
  pageDirectory: concepts
  sources:
    - horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - horovod-deprecation-on-databricks
    - HDOD
    - Horovod (deprecated)
  citations:
    - file: horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md
title: Horovod Deprecation on Databricks
description: Horovod and HorovodRunner are deprecated in Databricks Runtime ML after version 15.4 LTS ML, with TorchDistributor and tf.distribute.Strategy recommended as replacements.
tags:
  - deprecation
  - databricks
  - horovod
  - migration
timestamp: "2026-06-19T19:06:21.410Z"
---

# Horovod Deprecation on Databricks

**Horovod Deprecation on Databricks** refers to the gradual removal of the [Horovod](https://github.com/horovod/horovod) and [HorovodRunner](https://docs.databricks.com/aws/en/archive/machine-learning/train-model/horovod-spark) packages from Databricks Runtime ML. Support for these packages ended after Databricks Runtime 15.4 LTS ML, and they will no longer be pre‑installed in newer releases. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Deprecation Notice

Databricks officially deprecated Horovod and HorovodRunner in the documentation. As stated in the archived Horovod guide:

> Horovod and HorovodRunner are now deprecated. Releases after 15.4 LTS ML will not have this package pre‑installed.

This means that customers still using Databricks Runtime ML 15.4 LTS or earlier can continue to use Horovod, but any later runtime version will require manual installation (if possible) or migration to alternative frameworks.

## Recommended Alternatives

For distributed deep learning workloads, Databricks recommends the following replacements:

- **PyTorch users:** Use [TorchDistributor](https://docs.databricks.com/aws/en/machine-learning/train-model/distributed-training/#torch-distributor) for distributed training.
- **TensorFlow users:** Use the `tf.distribute.Strategy` API for distributed training.

Both alternatives are native to their respective frameworks and are actively maintained. They provide similar or improved scalability and integration with Databricks clusters.

## Compatibility Notes

- Horovod requires Databricks Runtime ML 7.4 or above. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]
- The `horovod.spark` package does not support pyarrow versions 11.0 and later (relevant [GitHub Issue](https://github.com/horovod/horovod/issues/3829)). Databricks Runtime 15.0 ML includes pyarrow 14.0.1, which is incompatible. To use `horovod.spark` on Databricks Runtime 15.0 ML or above, users must manually downgrade pyarrow to a version below 11.0. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]
- Databricks pre‑installs the `horovod` package with its dependencies. Upgrading or downgrading those dependencies may introduce compatibility issues. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Example Usage (Legacy)

The following basic example shows how `horovod.spark` was used to run a distributed training function. This code will continue to work only on supported runtime versions (≤ 15.4 LTS ML):

```python
def train():
    import horovod.tensorflow as hvd
    hvd.init()

import horovod.spark
horovod.spark.run(train, num_proc=2)
```

For new projects, use the alternatives listed above rather than Horovod.

## Related Concepts

- [TorchDistributor](/concepts/torchdistributor.md) – The recommended distributed training solution for PyTorch on Databricks.
- [tf.distribute.Strategy](/concepts/tfdistributestrategy.md) – The recommended distributed training API for TensorFlow.
- [HorovodRunner](/concepts/horovodrunner.md) – The legacy Databricks integration for Horovod (deprecated).
- [Distributed Deep Learning](/concepts/distributed-deep-learning-on-databricks.md) – Overview of multi‑GPU and multi‑node training.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The machine learning runtime that previously bundled Horovod.

## Sources

- horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md

# Citations

1. [horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md](/references/horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws-513310cf.md)
