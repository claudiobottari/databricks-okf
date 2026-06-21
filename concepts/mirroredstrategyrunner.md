---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 96251edb3af721d2df625145788a23274a145ec1311b79d1c03a0c60bb31aa67
  pageDirectory: concepts
  sources:
    - distributed-training-with-tensorflow-2-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - mirroredstrategyrunner
    - MirroredStrategy
  citations:
    - file: distributed-training-with-tensorflow-2-databricks-on-aws.md
title: MirroredStrategyRunner
description: Spark-based runner for TensorFlow MirroredStrategy that coordinates distributed training across Spark executors
tags:
  - tensorflow
  - spark
  - distributed-training
timestamp: "2026-06-19T18:38:49.143Z"
---

Here is the wiki page for "MirroredStrategyRunner".

---

## MirroredStrategyRunner

The **MirroredStrategyRunner** is the primary API class in the `spark-tensorflow-distributor` library that enables distributed training of TensorFlow 2 models on Apache Spark clusters using a synchronous, all-reduce distributed training pattern. It is built on top of `tensorflow.distribute.Strategy`, a key feature in TensorFlow 2 for implementing synchronous distributed training across multiple GPUs or TPUs. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## Overview

The `spark-tensorflow-distributor` package is an open-source, native TensorFlow package that helps users perform distributed training on their Spark clusters. The MirroredStrategyRunner provides a high-level API for running a [MirroredStrategy](/concepts/mirroredstrategyrunner.md) within a Spark environment, allowing users to distribute training workloads across Spark workers without needing to manually manage the underlying cluster infrastructure. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## Key Features

- **Synchronous all-reduce training**: Uses all-reduce algorithms to synchronize gradients and model parameters across all participating workers at each training step. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]
- **Spark cluster integration**: Leverages Spark’s distributed execution model to coordinate training across multiple nodes. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]
- **Automatic cluster management**: Handles the lifecycle of TensorFlow processes on Spark workers, including process spawning, synchronization, and resource cleanup. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## How It Works

The MirroredStrategyRunner creates a TensorFlow cluster on each Spark worker node. It then runs the training function on each worker using `MirroredStrategy` to synchronize computation across all workers. The runner automatically handles:

- **Worker discovery**: Discovers available Spark workers and creates a TensorFlow cluster. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]
- **Process management**: Spawns and manages TensorFlow processes on each worker. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]
- **Synchronization**: Coordinates between workers to ensure they all run the same training steps. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]
- **Resource cleanup**: Terminates processes cleanly after training completes. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## Use Cases

The MirroredStrategyRunner is suitable for:

- Training models that fit entirely in GPU memory on a single node but benefit from parallelization across multiple nodes. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]
- Scaling synchronous training to multiple GPUs across Spark cluster nodes. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]
- Training deep learning models where each batch requires large-scale parallel processing. ^[distributed-training-with-tensorflow-2-databricks-on-aws.md]

## Example Usage

```python
from spark_tensorflow_distributor import MirroredStrategyRunner

# Define your model creation function
def create_model():
    return tf.keras.Sequential([...])

# Define your training function
def train_fn():
    strategy = tf.distribute.MirroredStrategy()
    with strategy.scope():
        model = create_model()
        model.compile(...)
        model.fit(train_dataset, ...)

# Run distributed training on Spark
runner = MirroredStrategyRunner(num_workers=4)
runner.run(train_fn)
```

## Related Concepts

- [MirroredStrategy](/concepts/mirroredstrategyrunner.md) — The core TensorFlow distribution strategy.
- TensorFlow 2 — The modern TensorFlow framework.
- Apache Spark — The distributed computing framework.
- [spark-tensorflow-distributor](/concepts/spark-tensorflow-distributor.md) — The package containing MirroredStrategyRunner.
- [Distributed training with TensorFlow](/concepts/distributed-training-with-tensorflow-2.md) — General TensorFlow distributed training concepts.
- Synchronous training — The all-reduce training paradigm.

## Sources

- distributed-training-with-tensorflow-2-databricks-on-aws.md

# Citations

1. [distributed-training-with-tensorflow-2-databricks-on-aws.md](/references/distributed-training-with-tensorflow-2-databricks-on-aws-32a7d205.md)
