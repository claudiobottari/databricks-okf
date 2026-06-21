---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 84b32c6519681f6514d6bf57360bc9b0f21fd65eb6c0fd790b89b605085a605d
  pageDirectory: concepts
  sources:
    - horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - horovodspark-package
  citations:
    - file: horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md
title: horovod.spark Package
description: A Spark estimator API package for distributed deep learning training with Horovod, supporting Keras and PyTorch on Databricks.
tags:
  - distributed-training
  - spark
  - horovod
  - deep-learning
timestamp: "2026-06-19T19:06:18.398Z"
---

# horovod.spark Package

The **`horovod.spark`** package is part of the [Horovod](/concepts/horovod.md) distributed deep learning framework and provides an estimator API that can be used in Apache Spark ML pipelines with Keras and PyTorch. It enables distributed training of machine learning models by combining Horovod’s efficient allreduce operations with Spark’s cluster-computing capabilities. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Deprecation

**Horovod and HorovodRunner are now deprecated.** Databricks Runtime ML releases after 15.4 LTS ML will not have the `horovod` package pre-installed. For distributed deep learning, Databricks recommends using [TorchDistributor](/concepts/torchdistributor.md) for distributed training with PyTorch or the `tf.distribute.Strategy` API for distributed training with TensorFlow. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Requirements

- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) 7.4 or above. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

- **pyarrow compatibility**: Horovod Spark does not support pyarrow versions 11.0 and above due to a known issue (see [GitHub Issue #3829](https://github.com/horovod/horovod/issues/3829)). Databricks Runtime 15.0 ML includes pyarrow version 14.0.1, so to use `horovod.spark` with Databricks Runtime 15.0 ML or later, you must manually install a pyarrow version below 11.0. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Usage

The core entry point is `horovod.spark.run()`, which launches a distributed training function across multiple Spark executors. The training function must initialize Horovod (`hvd.init()`) and perform the usual Horovod-based training steps. The following basic example runs a distributed training function with two processes:

```python
def train():
    import horovod.tensorflow as hvd
    hvd.init()
    # ... model definition and training loop ...

import horovod.spark
horovod.spark.run(train, num_proc=2)
```

^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Notes on Custom Callbacks and Model Saving

When using `horovod.spark` with custom callbacks in Keras, models must be saved in the TensorFlow SavedModel format:

- With TensorFlow 2.x, use the `.tf` suffix in the file name.
- With TensorFlow 1.x, set the option `save_weights_only=True`. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Example Notebooks

The source documentation provides example notebooks demonstrating the Horovod Spark Estimator API with Keras and with PyTorch. These notebooks illustrate end‑to‑end workflows for training models using `horovod.spark`. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Related Concepts

- [Horovod](/concepts/horovod.md)
- [HorovodRunner](/concepts/horovodrunner.md)
- [TorchDistributor](/concepts/torchdistributor.md)
- [tf.distribute.Strategy](/concepts/tfdistributestrategy.md)
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md)

## Sources

- horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md

# Citations

1. [horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md](/references/horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws-513310cf.md)
