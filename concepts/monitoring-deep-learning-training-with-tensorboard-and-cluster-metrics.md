---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6f581c155fba2644408fe5ee21f8ca012d5eefa379a0af233295bafc4972fcb3
  pageDirectory: concepts
  sources:
    - best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - monitoring-deep-learning-training-with-tensorboard-and-cluster-metrics
    - Cluster Metrics and Monitoring Deep Learning Training with TensorBoard
    - MDLTWTACM
  citations:
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
title: Monitoring Deep Learning Training with TensorBoard and Cluster Metrics
description: Using pre-installed TensorBoard and Databricks cluster metrics (network, processor, memory, GPU) to inspect bottlenecks and monitor training processes.
tags:
  - monitoring
  - tensorboard
  - deep-learning
  - databricks
timestamp: "2026-06-19T09:11:46.942Z"
---

# Monitoring Deep Learning Training with TensorBoard and Cluster Metrics

**Monitoring Deep Learning Training with TensorBoard and Cluster Metrics** refers to the practice of using two complementary tools to observe, analyze, and debug deep learning model training runs on Databricks. [TensorBoard](/concepts/tensorboard-on-databricks.md) provides insight into model-internal metrics like loss curves and activation histograms, while cluster metrics surface infrastructure-level data such as network I/O, CPU utilization, and memory pressure. Together they help practitioners identify performance bottlenecks and training anomalies early in the development cycle. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Overview

TensorBoard is pre-installed in [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) (Databricks Runtime ML) and can be used directly within a notebook or in a separate browser tab. No additional installation or library management is required to begin using it. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

Cluster metrics are available in **all** Databricks runtimes, not only the ML-focused runtime. They expose real-time and historical data about network, processor, and memory usage across cluster nodes, making it possible to inspect for I/O or compute bottlenecks that slow down training. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Using TensorBoard

TensorBoard provides a dashboard for visualizing training dynamics. Common use cases include monitoring:

- **Loss and accuracy curves** – Track whether the model is converging or overfitting.
- **Activation histograms** – Detect vanishing or exploding gradients.
- **Model graph structure** – Verify that the computational graph is correctly defined.
- **Per-layer statistics** – Spot layers that are not learning (e.g., dead ReLU units).

Because TensorBoard reads the same [MLflow](/concepts/mlflow.md) log directory that Databricks autologging writes to, it can display metrics from a live run without extra configuration. For detailed setup instructions, see the [TensorBoard on Databricks](/concepts/tensorboard-on-databricks.md) page. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Using Cluster Metrics

Cluster metrics are accessed from the cluster UI or via the Databricks API. The metrics panel shows:

- **Network throughput** – Indicates whether data loading is saturating the network link.
- **CPU utilization** – Reveals whether preprocessing (e.g., data augmentation, tokenization) is competing for compute that should be used by the GPU.
- **Memory (RAM) usage** – Helps detect out-of-memory conditions on the driver or workers.
- **GPU utilization** – Shows whether GPUs are idle while waiting for data from the CPU or network.

Databricks documentation provides a step-by-step guide for viewing these metrics under the cluster management page. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Recommended Workflow

1. **Start with a Single Node cluster** – A driver-only GPU cluster is typically fastest and most cost-effective for early development because distributed training incurs network communication overhead. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]
2. **Monitor with TensorBoard** – Open TensorBoard in a separate tab while the training script runs. Watch for flat or oscillating loss curves that suggest a learning rate or batch size problem. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]
3. **Check cluster metrics** – If training appears slower than expected, switch to the cluster metrics panel and look for a network, CPU, or memory bottleneck. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]
4. **Iterate** – Adjust batch size, learning rate, or data loading strategy based on what the metrics show. For example, if GPU utilization is low but CPU is maxed out, the data pipeline is the bottleneck. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Related Concepts

- [TensorBoard on Databricks](/concepts/tensorboard-on-databricks.md)
- Cluster Metrics
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- [Autologging](/concepts/mlflow-autologging.md)
- [MLflow Tracking](/concepts/mlflow-tracking.md)
- GPU Scheduling
- Batch Size Tuning
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md)
- [Deep learning best practices on Databricks](/concepts/deep-learning-best-practices-on-databricks.md)

## Sources

- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md

# Citations

1. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
