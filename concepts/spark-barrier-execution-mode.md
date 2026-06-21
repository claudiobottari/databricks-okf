---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0610126b6c927890daf180b787fadf63bab330c85899dbb58f4b6e3d89191933
  pageDirectory: concepts
  sources:
    - horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spark-barrier-execution-mode
    - SBEM
    - Barrier Execution Mode
    - Barrier execution mode
  citations:
    - file: horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md
title: Spark Barrier Execution Mode
description: Spark execution mode that enables synchronous, long-running distributed training by providing task executors with topology awareness via BarrierTaskContext.
tags:
  - spark
  - distributed-computing
timestamp: "2026-06-19T10:48:12.153Z"
---

# Spark Barrier Execution Mode

**Spark Barrier Execution Mode** is a Spark scheduling mechanism that enables the embedding of MPI-based distributed deep learning jobs, such as [Horovod](/concepts/horovod.md), as a Spark job. It was introduced via [SPARK-24374](https://issues.apache.org/jira/browse/SPARK-24374) and is a core component of [HorovodRunner](/concepts/horovodrunner.md) on Databricks. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Overview

Barrier execution mode differs from standard Spark task scheduling in that it launches all tasks of a stage simultaneously and prevents speculative execution. This ensures that every executor participating in the barrier stage is alive and ready, which is essential for synchronised distributed training frameworks like Horovod. The mode provides a stable environment for long-running deep learning training jobs on Spark. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## How It Works

When HorovodRunner is used, a Horovod MPI job is embedded as a Spark job using barrier execution mode. The first executor collects the IP addresses of all task executors using the BarrierTaskContext API and then triggers a Horovod job via `mpirun`. The user’s training method is pickled on the driver, distributed to Spark workers, and deserialised by each MPI process. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

The key steps are:

1. The driver creates a barrier stage with as many tasks as the number of nodes (`np` parameter).
2. Each executor enters the barrier stage and obtains a `BarrierTaskContext`.
3. The first executor (rank 0) reads the network addresses of all barrier tasks from `BarrierTaskContext` and launches `mpirun` across the participating nodes.
4. Each MPI process loads and runs the pickled training method.

## Benefits

By integrating MPI-based training with Spark’s barrier mode, Databricks achieves higher stability for long-running deep learning jobs compared to earlier approaches. The barrier guarantees that all workers are present before computation begins, reducing the risk of stragglers or task failures that would disrupt synchronised allreduce operations. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Relationship to HorovodRunner

Spark Barrier Execution Mode is the underlying mechanism that allows [HorovodRunner](/concepts/horovodrunner.md) to run distributed training reliably within a Spark cluster. Without barrier mode, Horovod’s MPI job could not be scheduled as a Spark job while preserving the required synchronisation guarantees. ^[horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md]

## Related Concepts

- BarrierTaskContext – The Spark API used to coordinate barrier tasks.
- [Horovod](/concepts/horovod.md) – A distributed training framework that uses MPI for allreduce.
- [HorovodRunner](/concepts/horovodrunner.md) – A Databricks API that wraps Horovod jobs using barrier execution mode.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) – An alternative distributed training strategy.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) – A memory-efficient distributed training approach.

## Sources

- horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md

# Citations

1. [horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws.md](/references/horovodrunner-distributed-deep-learning-with-horovod-databricks-on-aws-bdb09a88.md)
