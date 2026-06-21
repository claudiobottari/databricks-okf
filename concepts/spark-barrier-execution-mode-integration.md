---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dd7c073169f85027a1a8ffa53b620f405f5a51c26b0e362734f7c48869fb4c64
  pageDirectory: concepts
  sources:
    - horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spark-barrier-execution-mode-integration
    - SBEMI
  citations:
    - file: horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
title: Spark Barrier Execution Mode Integration
description: HorovodRunner integrates Horovod with Spark's barrier execution mode, using BarrierTaskContext to collect executor IPs and trigger MPI jobs via mpirun for stable long-running deep learning training.
tags:
  - spark
  - architecture
  - distributed-computing
timestamp: "2026-06-19T19:05:34.844Z"
---

# Spark Barrier Execution Mode Integration

**Spark Barrier Execution Mode Integration** refers to the use of Apache Spark’s barrier execution mode to embed distributed deep learning frameworks – such as Horovod – as Spark jobs, providing higher stability for long-running training workloads. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Overview

Barrier execution mode is a Spark scheduling feature that launches a set of tasks simultaneously, with all tasks in a stage required to succeed for the stage to complete. This “all-or-nothing” guarantee makes it suitable for frameworks like Horovod that require synchronous communication between workers. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

When a [HorovodRunner](/concepts/horovodrunner.md) job is started, the system integrates Horovod with Spark’s barrier mode. The first executor collects the IP addresses of all task executors using `BarrierTaskContext` and triggers a Horovod MPI job via `mpirun`. Each Python MPI process loads a pickled user program, deserializes it, and runs the distributed training logic. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Key Mechanisms

- **BarrierTaskContext**: An extension of `TaskContext` that provides information about all tasks in the barrier stage, including their IP addresses and ports. The first executor uses this context to orchestrate the MPI ring. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]
- **Embedded MPI**: A Horovod MPI job is started as a Spark job. The barrier stage ensures that all worker processes are launched before any MPI communication begins, preventing race conditions. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]
- **Pickled User Code**: The user’s training function (including all required imports) is pickled on the driver and distributed to each executor. This ensures consistency of the training logic across nodes. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Benefits

- **Stability**: Barrier execution mode eliminates partial failures common in traditional Spark task scheduling. If any task in the barrier stage fails, the entire stage is retried, which aligns with the requirements of synchronous [Distributed Deep Learning](/concepts/distributed-deep-learning-on-databricks.md). ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]
- **Resource Guarantees**: All executors in the barrier stage are allocated simultaneously, reducing the likelihood of stragglers that can impede MPI collective operations. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Usage Context

This integration is primarily used through [HorovodRunner](/concepts/horovodrunner.md), which is now deprecated in Databricks versions after 15.4 LTS ML. For new projects, Databricks recommends using [TorchDistributor](/concepts/torchdistributor.md) for PyTorch or the `tf.distribute.Strategy` API for TensorFlow. Nevertheless, understanding the barrier execution mode pattern remains relevant for custom distributed training setups that require synchronous worker coordination. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Related Concepts

- BarrierTaskContext – The Spark API used to coordinate barrier-stage tasks.
- [HorovodRunner](/concepts/horovodrunner.md) – The deprecated API that leverages barrier execution mode.
- Distributed Training with PyTorch – Modern alternative for PyTorch workloads.
- [TensorFlow Distribution Strategies](/concepts/tensorflowdistributestrategy.md) – Modern alternative for TensorFlow workloads.
- Spark Execution Model – General Spark scheduling and task execution.

## Sources

- horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md

# Citations

1. [horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md](/references/horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws-bdb09a88.md)
