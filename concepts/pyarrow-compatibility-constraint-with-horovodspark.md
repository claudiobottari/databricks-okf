---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9c0d01ad57a340c95d3aa457d6a4511f65dc4c0be41f7cfc7c59c9f8db79fc48
  pageDirectory: concepts
  sources:
    - horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pyarrow-compatibility-constraint-with-horovodspark
    - PCCWH
  citations:
    - file: horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md
title: PyArrow Compatibility Constraint with horovod.spark
description: horovod.spark does not support pyarrow versions 11.0 and above, requiring manual installation of pyarrow below version 11.0 for Databricks Runtime 15.0 ML and above.
tags:
  - compatibility
  - pyarrow
  - horovod
  - databricks
timestamp: "2026-06-19T19:06:28.381Z"
---

# PyArrow Compatibility Constraint with horovod.spark

The **PyArrow Compatibility Constraint with horovod.spark** is a known limitation that prevents `horovod.spark` from working with PyArrow versions 11.0 and above. This constraint affects users of Databricks Runtime ML 15.0 and later, which ship with PyArrow 14.0.1 by default. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Constraint Details

`horovod.spark` does not support PyArrow 11.0 or higher due to an incompatibility tracked in a [GitHub issue](https://github.com/horovod/horovod/issues/3829). When using a Databricks Runtime ML version that includes PyArrow 11.0+, `horovod.spark` will fail unless an older version of PyArrow is manually installed. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Workaround

To use `horovod.spark` with Databricks Runtime 15.0 ML or above, you must manually downgrade PyArrow to a version below 11.0. This can be done by installing a specific version (e.g., `pyarrow==10.0.1`) in the cluster's library configuration or within the notebook before importing `horovod.spark`. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Deprecation Context

Horovod and [HorovodRunner](/concepts/horovodrunner.md) are deprecated in Databricks. Releases after Databricks Runtime 15.4 LTS ML will not have the `horovod` package pre-installed. Databricks recommends using [TorchDistributor](/concepts/torchdistributor.md) for distributed training with PyTorch or the `tf.distribute.Strategy` API for distributed training with TensorFlow as alternatives to `horovod.spark`. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Related Concepts

- [horovod.spark](/concepts/horovodspark.md) – The deprecated estimator API for distributed deep learning on Spark.
- PyArrow – The columnar data format library whose version causes the incompatibility.
- [TorchDistributor](/concepts/torchdistributor.md) – The recommended alternative for PyTorch distributed training.
- [tf.distribute.Strategy](/concepts/tfdistributestrategy.md) – The recommended alternative for TensorFlow distributed training.
- [Distributed Deep Learning](/concepts/distributed-deep-learning-on-databricks.md) – The broader practice of training models across multiple GPUs or nodes.

## Sources

- horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md

# Citations

1. [horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md](/references/horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws-513310cf.md)
