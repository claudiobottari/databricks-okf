---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4360c869cd29f328533c67d5cd3620811a84135ec724ded773e7c6c0f33d26af
  pageDirectory: concepts
  sources:
    - horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - horovod-spark-estimator-api-with-pytorch
    - HSEAWP
  citations:
    - file: horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md
title: Horovod Spark Estimator API with PyTorch
description: Using the horovod.spark estimator API to run distributed deep learning training with PyTorch models on Databricks.
tags:
  - pytorch
  - horovod
  - spark
  - distributed-training
timestamp: "2026-06-19T19:06:32.024Z"
---

## Horovod Spark Estimator API with PyTorch

The **Horovod Spark Estimator API with PyTorch** enables distributed training of deep learning models within Apache Spark pipelines using [Horovod](/concepts/horovod.md) and PyTorch. It is provided through the `horovod.spark` package, which exposes an estimator interface that integrates with ML pipelines and supports both Keras and PyTorch backends. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

### Requirements

- Databricks Runtime ML 7.4 or above. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

**Note on pyarrow compatibility:** `horovod.spark` does not support pyarrow versions 11.0 and above. Databricks Runtime 15.0 ML includes pyarrow 14.0.1. To use `horovod.spark` with Databricks Runtime 15.0 ML or above, you must manually install pyarrow, specifying a version below 11.0. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

### Usage Example

A basic distributed training function using `horovod.spark` with PyTorch follows the same pattern as the TensorFlow example. The key steps are:

```python
def train():
    import horovod.torch as hvd
    hvd.init()
    # ... define model, optimizer, wrap with DistributedOptimizer, etc.

import horovod.spark
horovod.spark.run(train, num_proc=2)
```

The `horovod.spark.run` function launches the `train` function across the specified number of Spark tasks (`num_proc`). Inside the function, `hvd.init()` initializes Horovod and `hvd.local_rank()` etc. can be used to assign devices and set up data loading. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

### Deprecation Notice

Horovod and HorovodRunner are now deprecated. Releases after Databricks Runtime 15.4 LTS ML will not have the `horovod` package pre-installed. For distributed deep learning, Databricks recommends using [TorchDistributor](/concepts/torchdistributor.md) for distributed training with PyTorch or the `tf.distribute.Strategy` API for distributed training with TensorFlow. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

### Example Notebooks

Databricks provides the following notebook that demonstrates how to use the Horovod Spark Estimator API with PyTorch:

- Horovod Spark Estimator PyTorch notebook (referenced in the source documentation)

The notebook covers setup, data preparation, model definition, distributed training, and integration with Spark ML pipelines using the estimator API. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

### Related Concepts

- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) – General overview of distributed training on Databricks.
- PyTorch Distributed – Native PyTorch distributed training utilities.
- [TorchDistributor](/concepts/torchdistributor.md) – The recommended tool for PyTorch distributed training on Databricks.
- [Horovod](/concepts/horovod.md) – The underlying distributed framework.
- Keras – The alternative backend supported by `horovod.spark`.

### Sources

- horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md

# Citations

1. [horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md](/references/horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws-513310cf.md)
