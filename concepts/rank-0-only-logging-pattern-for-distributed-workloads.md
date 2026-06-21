---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 982564de6bf889a9ea0394222b9148f15fd4eeb92444ee894f44b8704ca35ab1
  pageDirectory: concepts
  sources:
    - track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - rank-0-only-logging-pattern-for-distributed-workloads
    - ROLPFDW
  citations:
    - file: track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md
title: Rank-0 Only Logging Pattern for Distributed Workloads
description: On multi-node workloads, all nodes share the same MLflow run ID; logging should only be done from the rank-0 process to avoid duplicate metric recording.
tags:
  - distributed-computing
  - mlflow
  - best-practice
timestamp: "2026-06-19T23:14:00.116Z"
---

# Rank-0 Only Logging Pattern for Distributed Workloads

The **Rank-0 Only Logging Pattern** is a best practice for logging metrics, parameters, and artifacts in distributed training workloads where multiple processes (ranks) run in parallel across GPUs or nodes. In this pattern, only the process with rank 0 logs data to the experiment tracking system, ensuring each metric is recorded exactly once.

## Overview

In distributed training, all nodes share the same [MLflow Run](/concepts/mlflow-run.md) ID. If every process logs the same metrics independently, the experiment tracking system receives duplicate entries for the same metric at the same step. The rank-0 only pattern prevents this duplication by having a single designated process handle all logging. ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

## Implementation

The pattern is implemented by checking the process rank before calling any logging API. Only the process where the rank equals 0 performs the logging operations. ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

```python
import os
import [[mlflow|MLflow]]

# Log from rank 0 only; all nodes share the same MLFLOW_RUN_ID.
if os.environ.get("RANK", "0") == "0":
    with [[mlflow|MLflow]].start_run(run_id=os.environ["MLFLOW_RUN_ID"]):
        [[mlflow|MLflow]].log_param("learning_rate", 3e-4)
        for step, loss in enumerate(training_losses):
            [[mlflow|MLflow]].log_metric("train_loss", loss, step=step)
```

^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

### Key Points

- The `MLFLOW_RUN_ID` environment variable is automatically set by the platform and is shared across all nodes in a distributed workload. ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]
- The `RANK` environment variable identifies which process is rank 0. The default value `"0"` ensures single-process workloads also log correctly. ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]
- This pattern applies to logging custom parameters, metrics, and artifacts using the [MLflow Tracking API](/concepts/mlflow-tracking.md). ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

## Benefits

- **Deduplication**: Each metric is recorded exactly once, preventing duplicate entries in the experiment tracking system. ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]
- **Consistency**: All logging comes from a single source, ensuring coherent metric sequences and timestamps. ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]
- **Performance**: Reduces unnecessary logging overhead on non-rank-0 processes. ^[track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md]

## Related Concepts

- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — The broader context where this pattern is applied.
- [MLflow Tracking API](/concepts/mlflow-tracking.md) — The API used to log metrics, parameters, and artifacts.
- [Fully Sharded Data Parallel (FSDP)](/concepts/fully-sharded-data-parallel-fsdp.md) — A common distributed training strategy that uses multiple ranks.
- [Distributed Data Parallel (DDP)](/concepts/distributed-data-parallel-ddp.md) — Another parallelism strategy where rank-0 logging is recommended.
- [System Metrics](/concepts/mlflow-system-metrics.md) — GPU, CPU, and memory metrics that are captured automatically for every run without requiring rank-0 logic.

## Sources

- track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md

# Citations

1. [track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws.md](/references/track-runs-with-mlflow-and-the-jobs-run-page-databricks-on-aws-f3444863.md)
