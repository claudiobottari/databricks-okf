---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bc2bec465ee1497bbf6b1a5a2d53cec91250e51f548e72684c6bc4f98c4390c9
  pageDirectory: concepts
  sources:
    - deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md
  confidence: 0.7
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - horovod-for-distributed-deep-learning-on-databricks
    - HFDDLOD
  citations:
    - file: deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md
title: Horovod for Distributed Deep Learning on Databricks
description: The integration of Uber's Horovod distributed training framework within the Databricks environment for scaling deep learning workloads
tags:
  - distributed-training
  - horovod
  - databricks
timestamp: "2026-06-18T11:47:40.122Z"
---

# Horovod for Distributed Deep Learning on Databricks

**Horovod** is a distributed deep learning framework that enables scalable training across multiple GPUs and machines on Databricks. It uses the HorovodRunner API to distribute TensorFlow, Keras, and PyTorch training jobs across a Spark cluster, reducing training time for large models while maintaining code simplicity. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

## Overview

Horovod provides a straightforward approach to distributed training by implementing the all-reduce algorithm for gradient synchronization. On Databricks, the [HorovodRunner](/concepts/horovodrunner.md) wraps Horovod operations, allowing data scientists to convert single-node training scripts into distributed training jobs with minimal code changes. ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

### Key Features

- **Minimal code changes**: Convert single-node training scripts to distributed with only a few modifications
- **Multi-GPU support**: Leverage all available GPUs across cluster worker nodes
- **Framework agnostic**: Works with TensorFlow, Keras, PyTorch, and Apache MXNet
- **Integration with Spark**: Launch distributed training directly from a Spark cluster

## Development Workflow

The recommended development workflow for Horovod on Databricks follows a two-stage process:

### Stage 1: Prepare and Tune on a Single Node

Before scaling to distributed training, develop and tune your model on a single node. This involves:

1. **Prepare data** for distributed training by partitioning or creating a data pipeline compatible with distributed loading
2. **Write a standard training script** using your chosen framework (TensorFlow/Keras, PyTorch, etc.)
3. **Validate the model** on a single GPU to ensure correctness and convergence

### Stage 2: Scale with HorovodRunner

Once the model performs correctly on a single node, add Horovod-specific calls to enable distributed training:

1. **Initialize Horovod** with `hvd.init()`
2. **Pin GPU** to the local process: `tf.config.experimental.set_visible_devices(gpus[hvd.local_rank()], 'GPU')`
3. **Scale the learning rate** by the number of workers: `lr * hvd.size()`
4. **Wrap the optimizer** with `hvd.DistributedOptimizer(optimizer)`
5. **Broadcast initial variable states** from rank 0 to all processes: `hvd.broadcast_variables(model.variables, root_rank=0)`
6. **Ensure each worker loads a unique shard** of the training data

## TensorFlow and Keras MNIST Example

The following example demonstrates training a neural network on the [MNIST Dataset](/concepts/mnist-dataset.md) using Horovod with TensorFlow and Keras on Databricks: ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

```python
import horovod.tensorflow.keras as hvd
import tensorflow as tf

# Initialize Horovod
hvd.init()

# Pin GPU to be used by this process
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    tf.config.experimental.set_visible_devices(
        gpus[hvd.local_rank()], 'GPU')

# Build the model
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
])

# Scale learning rate with number of workers
opt = tf.optimizers.Adam(0.001 * hvd.size())

# Wrap optimizer for distributed training
opt = hvd.DistributedOptimizer(opt)

# Compile with the wrapped optimizer
model.compile(optimizer=opt,
              loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Broadcast initial variable states from rank 0
callbacks = [
    hvd.callbacks.BroadcastGlobalVariablesCallback(0),
]

# Ensure each worker processes a unique shard of the data
# (Use appropriate data partitioning strategy)

model.fit(x_train, y_train,
          batch_size=64,
          callbacks=callbacks,
          epochs=10,
          verbose=1 if hvd.rank() == 0 else 0)
```

### Key Code Modifications for Horovod

- **`hvd.init()`** — Initializes Horovod across all processes
- **`hvd.local_rank()`** — Gets the local GPU rank for device pinning
- **`hvd.size()`** — Returns the total number of worker processes
- **`hvd.DistributedOptimizer()`** — Wraps the optimizer to synchronize gradients across workers
- **`BroadcastGlobalVariablesCallback(0)`** — Ensures all workers start with identical model weights
- **`hvd.rank() == 0`** — Restricts verbose output to the primary worker only

## Using HorovodRunner on Databricks

To launch a Horovod training job on a Databricks cluster, use the [HorovodRunner](/concepts/horovodrunner.md) API: ^[deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md]

```python
from sparkdl import HorovodRunner

# Create a HorovodRunner with the specified number of GPUs
hr = HorovodRunner(np=2)  # Use 2 GPUs

# Run the training function
hr.run(train_hvd)
```

### Parameters

- **`np`**: The number of processes to run across the cluster. On GPU clusters, use `np` equal to the total number of available GPUs.

## Best Practices

- **Prepare data with distributed loading**: Use tf.data or a similar API to ensure each worker loads a unique shard of the training data. Avoid loading the entire dataset into memory on the driver.
- **Scale learning rate**: Multiply the single-node learning rate by `hvd.size()` to maintain effective learning dynamics with larger batch sizes.
- **Use gradient compression**: Enable `hvd.Compression.fp16` in the `DistributedOptimizer` to reduce communication overhead when training with large models.
- **Monitor with [MLflow](/concepts/mlflow.md)**: Log metrics, parameters, and the trained model to track experiments across distributed runs.

## Limitations and Considerations

- Horovod requires a cluster with GPUs configured on each worker node
- Network latency between workers can impact scaling efficiency for small models
- Not all Keras callbacks are compatible with distributed training — use Horovod-specific callbacks where available

## Related Concepts

- [HorovodRunner](/concepts/horovodrunner.md) — The Databricks API for launching Horovod distributed training
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — General concepts for scaling machine learning workloads
- GPU Clusters on Databricks — Configuring clusters with GPU support
- TensorFlow with Horovod — Specific integration details for TensorFlow
- PyTorch Distributed Training — Alternative approach using PyTorch's native distributed module
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Experiment tracking for distributed runs

## Sources

- deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md

# Citations

1. [deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws.md](/references/deep-learning-using-tensorflow-with-horovodrunner-for-mnist-databricks-on-aws-06d44e07.md)
