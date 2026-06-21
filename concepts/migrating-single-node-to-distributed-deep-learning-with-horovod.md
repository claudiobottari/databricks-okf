---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7700223f01819eab1404c8501209141992ff9022cf9d4dab340d69c1cb4aad2b
  pageDirectory: concepts
  sources:
    - horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
  confidence: 0.92
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - migrating-single-node-to-distributed-deep-learning-with-horovod
    - MSTDDLWH
  citations:
    - file: horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
title: Migrating Single-Node to Distributed Deep Learning with Horovod
description: A six-step workflow for converting single-node deep learning code (TensorFlow, Keras, PyTorch) to distributed training using Horovod, then wrapping it for HorovodRunner.
tags:
  - migration
  - deep-learning
  - best-practices
timestamp: "2026-06-19T19:06:20.756Z"
---

---
title: "Migrating Single-Node to Distributed Deep Learning with Horovod"
summary: A step-by-step guide for converting single-node deep learning code to distributed training using Horovod and HorovodRunner on Databricks.
sources:
  - horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
kind: guide
createdAt: "2026-06-19T12:00:00.000Z"
updatedAt: "2026-06-19T12:00:00.000Z"
tags:
  - distributed-training
  - horovod
  - deep-learning
  - migration
aliases:
  - migrating-to-horovod
  - single-node-to-distributed-horovod
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Migrating Single-Node to Distributed Deep Learning with Horovod

**Migrating Single-Node to Distributed Deep Learning with Horovod** describes the process of adapting deep learning training code—written for a single GPU or CPU—to run across multiple workers using [Horovod](/concepts/horovod.md) and [HorovodRunner](/concepts/horovodrunner.md) on Databricks. This migration enables scaling of model training by distributing computation across multiple GPUs and nodes. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

> **Note:** Horovod and HorovodRunner are now deprecated. For distributed deep learning, Databricks recommends using [TorchDistributor](/concepts/torchdistributor.md) for PyTorch or the `tf.distribute.Strategy` API for TensorFlow. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Overview

HorovodRunner is a general API that launches [Horovod](/concepts/horovod.md) training jobs as Spark jobs. It integrates Horovod with Spark's barrier execution mode, providing higher stability for long-running deep learning training jobs. The API pickles the user's training method on the driver and distributes it to Spark workers. The first executor collects IP addresses of all task executors using `BarrierTaskContext` and triggers a Horovod job using `mpirun`. Each Python MPI process deserializes and runs the pickled user program. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## General Migration Workflow

The migration from single-node to distributed training with Horovod follows three main steps: ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

### Step 1: Prepare Single-Node Code

Prepare and test the single-node training code using TensorFlow, Keras, or PyTorch. Ensure the code runs correctly on a single GPU before attempting distributed migration. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

### Step 2: Migrate to Horovod

Follow the standard [Horovod](/concepts/horovod.md) usage patterns to adapt the training loop. Key modifications include: ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

1. **Initialize Horovod**: Add `hvd.init()` to initialize the Horovod environment.
2. **Pin GPUs**: Use `config.gpu_options.visible_device_list` to assign one GPU per process based on the local rank. This ensures the first process gets the first GPU, the second gets the second GPU, and so forth.
3. **Shard the dataset**: Use dataset sharding so each worker reads a unique subset of the data.
4. **Scale the learning rate**: Multiply the learning rate by the number of workers to compensate for the increased effective batch size in synchronous distributed training.
5. **Wrap the optimizer**: Replace the standard optimizer with `hvd.DistributedOptimizer`, which averages gradients using allreduce or allgather before applying them.
6. **Broadcast initial variables**: Add `hvd.BroadcastGlobalVariablesHook(0)` (or `hvd.broadcast_global_variables` for non-`MonitoredTrainingSession` usage) to ensure consistent initialization across all workers.
7. **Save checkpoints on rank 0 only**: Modify checkpoint saving to occur only on worker 0 to prevent corruption from concurrent writes.

### Step 3: Migrate to HorovodRunner

Wrap the complete training procedure into a single Python function. Create a `HorovodRunner` instance initialized with the desired number of processes (`np`), then pass the training function to its `run` method. Test first in local mode (`np=-n` for driver-only subprocesses) before running in distributed mode. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

Example:

```python
hr = HorovodRunner(np=2)

def train():
    import tensorflow as tf
    hvd.init()
    # ... training code with Horovod hooks ...

hr.run(train)
```

## Avoiding Common Errors

A frequent error occurs when TensorFlow or PyTorch objects cannot be found or pickled. This happens when library import statements are not distributed to other executors. To avoid this issue, include all import statements (e.g., `import tensorflow as tf`) *both* at the top of the Horovod training method and inside any other user-defined functions called within the training method. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Updating Deep Learning Libraries

If you upgrade or downgrade TensorFlow, Keras, or PyTorch, you must reinstall Horovod so that it is compiled against the newly installed library. For example, after upgrading TensorFlow, append Horovod installation code (with appropriate compiler flags like `HOROVOD_GPU_ALLREDUCE=NCCL`) to the cluster's init script. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Limitations

- HorovodRunner will not work if `np` is set to greater than 1 and the notebook imports from relative files in workspace files. In such cases, consider using [horovod.spark](/concepts/horovodspark.md) instead. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]
- Network communication issues between nodes can arise. To resolve errors like `Open MPI accepted a TCP connection from what appears to be another Open MPI process but cannot find a corresponding process entry`, add the following to your training code to specify the primary network interface: ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

```python
import os
os.environ["OMPI_MCA_btl_tcp_if_include"]="eth0"
os.environ["NCCL_SOCKET_IFNAME"]="eth0"
```

## Related Concepts

- [Horovod](/concepts/horovod.md) — The distributed training framework underlying HorovodRunner.
- [HorovodRunner](/concepts/horovodrunner.md) — The API for launching Horovod jobs as Spark jobs on Databricks.
- [TorchDistributor](/concepts/torchdistributor.md) — The recommended alternative for distributed PyTorch training.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — A common parallelism strategy.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — Memory-efficient training for very large models.
- Single-Node Training — The baseline before migration.
- [Barrier Execution Mode](/concepts/spark-barrier-execution-mode.md) — Spark's execution mode used by HorovodRunner for stable distributed training.

## Sources

- horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md

# Citations

1. [horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md](/references/horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws-bdb09a88.md)
