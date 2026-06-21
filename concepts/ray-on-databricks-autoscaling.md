---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dfcac5fb8fd633ae7aeb34ae51211f2d673806884c64e3a7f46b2a3d6e2ae127
  pageDirectory: concepts
  sources:
    - scale-ray-clusters-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-on-databricks-autoscaling
    - RODA
    - Databricks Autoscaling
    - Ray Autoscaling
    - Ray on Spark Autoscaling
  citations:
    - file: scale-ray-clusters-on-databricks-databricks-on-aws.md
title: Ray on Databricks Autoscaling
description: Ray clusters on Databricks support integration with Databricks autoscaling, allowing Ray worker nodes to scale up and down based on workload demand using min/max worker node parameters.
tags:
  - ray
  - databricks
  - autoscaling
  - cluster-management
timestamp: "2026-06-19T20:18:40.532Z"
---

# Ray on Databricks Autoscaling

**Ray on Databricks Autoscaling** refers to the integration between Ray clusters and Databricks cluster autoscaling, allowing Ray worker nodes to dynamically scale up and down based on workload demand. This feature is available in Ray 2.8.0 and above and helps optimize resource utilization and cost efficiency. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

## Overview

When autoscaling is enabled, the Ray cluster triggers Databricks cluster autoscaling internally within the Databricks environment. This allows the Ray cluster to automatically adjust the number of worker nodes based on current workload requirements, scaling up when demand increases and scaling down during idle periods. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

## Enabling Autoscaling

### Ray Version 2.10 and Above

For Ray 2.10 and later, use the `setup_ray_cluster` API with `min_worker_nodes` and `max_worker_nodes` parameters to define the scaling range: ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

```python
from ray.util.spark import setup_ray_cluster, shutdown_ray_cluster

setup_ray_cluster(
    min_worker_nodes=2,
    max_worker_nodes=4,
    num_cpus_per_node=4,
    collect_log_to_path="/dbfs/path/to/ray_collected_logs"
)

ray.init(ignore_reinit_error=True)
```

The `min_worker_nodes` and `max_worker_nodes` arguments represent the range of Ray worker nodes to create and utilize. If `min_worker_nodes` is left undefined, a fixed-size Ray cluster will be started with `max_worker_nodes` number of workers available. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

### Ray Version Below 2.10

For Ray versions below 2.10, use the `autoscale=True` parameter with `num_worker_nodes` indicating the maximum number of Ray worker nodes: ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

```python
from ray.util.spark import setup_ray_cluster

setup_ray_cluster(
    num_worker_nodes=8,
    autoscale=True,
)
```

When autoscaling is enabled, the default minimum number of Ray worker nodes is zero. This means the Ray cluster can scale down to zero worker nodes when idle, which can significantly reduce costs but may impact fast responsiveness. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

## Autoscaling Configuration Parameters

### Upscaling and Downscaling Speed

The following arguments configure the scaling behavior: ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

- **`autoscale_upscaling_speed`**: Represents the number of nodes allowed to be pending as a multiple of the current number of nodes. Higher values result in more aggressive upscaling. For example, a value of 1.0 means the cluster can grow by at most 100% at any time.
- **`autoscale_idle_timeout_minutes`**: The number of minutes that must pass before the autoscaler removes an idle worker node. Smaller values result in more aggressive downscaling.

### Minimum Worker Nodes (Ray 2.9.0+)

With Ray 2.9.0 and above, you can set `autoscale_min_worker_nodes` to prevent the Ray cluster from scaling down to zero workers when idle, which would otherwise cause the cluster to terminate. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

## Scaling Best Practices

### Hybrid Spark and Ray Workloads

When running hybrid Spark and Ray workloads in a Databricks cluster, it is recommended to make either cluster nodes or Ray worker nodes auto-scalable: ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

- **Fixed Databricks cluster with Ray autoscaling**: If you have a fixed number of worker nodes available, enable Ray-on-Spark autoscaling. When no Ray workloads are running, the Ray cluster scales down, freeing resources for Apache Spark tasks. When Spark tasks finish and Ray is needed again, the Ray cluster scales up.
- **Both auto-scalable**: You can configure both Databricks and Ray-on-Spark clusters to be auto-scalable. For example, configure the Databricks cluster's auto-scalable nodes to a maximum of 10 nodes, and the Ray-on-Spark worker nodes to a maximum of 4 nodes. Ray workloads can then use at most 4 nodes, while Spark jobs can allocate up to 6 nodes.

### Memory Configuration

To avoid out-of-memory errors in hybrid workloads, reduce Spark executor memory to a small value (e.g., `spark.executor.memory 4g`). The Apache Spark executor is a Java process that triggers garbage collection lazily, and the Spark dataset cache can consume significant memory, reducing available memory for Ray. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

### CPU and GPU Configuration

Set `num_cpus_worker_node` to the number of CPU cores per Apache Spark worker node, and `num_gpus_worker_node` to the number of GPUs per Apache Spark worker node. This configuration ensures each Spark worker node launches one Ray worker node that fully utilizes the resources of each Spark worker node. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

Set the environment variable `RAY_memory_monitor_refresh_ms` to `0` within the Databricks cluster configuration when starting your Apache Spark cluster. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Ray on Databricks](/concepts/ray-on-databricks.md) — Overview of running Ray clusters on Databricks
- [Ray Cluster Configuration](/concepts/ray-gpu-cluster-configuration.md) — Tuning Ray cluster settings for optimal performance
- Databricks Cluster Autoscaling — General Databricks cluster autoscaling capabilities
- Heterogeneous Clusters — Configuring different instance types for head and worker nodes
- Ray Head Node Configuration — Resource allocation for the Ray head node

## Sources

- scale-ray-clusters-on-databricks-databricks-on-aws.md

# Citations

1. [scale-ray-clusters-on-databricks-databricks-on-aws.md](/references/scale-ray-clusters-on-databricks-databricks-on-aws-ad8172f6.md)
