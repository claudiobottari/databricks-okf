---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 215d10924bf1138fb74091aa5f81a72d44dc4ee83482eb440adea7670ccf4cbc
  pageDirectory: concepts
  sources:
    - horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - horovod-on-spark
    - HOS
    - Horovod Spark
  citations:
    - file: horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md
title: Horovod on Spark
description: A distributed deep learning package providing an estimator API for training Keras and PyTorch models on Apache Spark clusters.
tags:
  - distributed-deep-learning
  - spark
  - horovod
timestamp: "2026-06-19T10:48:33.207Z"
---

---
title: Horovod on Spark
summary: Using the `horovod.spark` package to perform distributed deep learning training with Keras and PyTorch on Databricks.
sources:
  - horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:08:33.206Z"
updatedAt: "2026-06-18T11:08:33.206Z"
tags:
  - databricks
  - distributed-training
  - horovod
  - deep-learning
aliases:
  - Horovod on Spark
  - hos
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Horovod on Spark

**Horovod on Spark** refers to the use of the `horovod.spark` package to perform distributed deep learning training within Apache Spark pipelines on Databricks. The package provides an estimator API that integrates with both Keras and PyTorch models, allowing users to scale training across multiple workers. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Requirements

- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) 7.4 or above. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]
- `horovod.spark` does not support PyArrow versions 11.0 and above. Databricks Runtime 15.0 ML includes PyArrow 14.0.1; to use `horovod.spark` with that runtime or later, you must manually install a PyArrow version below 11.0. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]
- Databricks installs the `horovod` package with dependencies. Upgrading or downgrading these dependencies may cause compatibility issues. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Usage

A basic distributed training function using `horovod.spark` takes the following form:

```python
def train():
    import horovod.tensorflow as hvd
    hvd.init()
import horovod.spark
horovod.spark.run(train, num_proc=2)
```

The `train()` function initialises Horovod with `hvd.init()` and can then use `hvd.allreduce`, `hvd.DistributedOptimizer`, etc., on each worker. The call to `horovod.spark.run()` launches the function across the specified number of Spark processes (`num_proc`). ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

### Keras and PyTorch Estimators

`horovod.spark` provides an estimator API that works with Keras and PyTorch models. When using custom callbacks with Keras, models must be saved in the TensorFlow SavedModel format. For TensorFlow 2.x use the `.tf` suffix; for TensorFlow 1.x set `save_weights_only=True`. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Deprecation Notice

Horovod and [HorovodRunner](/concepts/horovodrunner.md) are deprecated. Releases after Databricks Runtime ML 15.4 LTS will not have the `horovod` package pre-installed. For distributed deep learning, Databricks recommends migrating to [TorchDistributor](/concepts/torchdistributor.md) for PyTorch or the `tf.distribute.Strategy` API for TensorFlow. ^[horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Related Concepts

- [TorchDistributor](/concepts/torchdistributor.md) — Recommended replacement for PyTorch distributed training.
- [tf.distribute.Strategy](/concepts/tfdistributestrategy.md) — Recommended replacement for TensorFlow distributed training.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — Common parallelism strategy used by Horovod and its successors.
- [HorovodRunner](/concepts/horovodrunner.md) — Deprecated Databricks utility for running Horovod jobs.
- Keras — High-level neural network API supported by `horovod.spark`.
- PyTorch — Deep learning framework supported by `horovod.spark`.

## Sources

- horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md

# Citations

1. [horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws.md](/references/horovodspark-distributed-deep-learning-with-horovod-databricks-on-aws-513310cf.md)
