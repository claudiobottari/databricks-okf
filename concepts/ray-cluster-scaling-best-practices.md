---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5e37db8c9924d4257b8cb597530e2bb9a8e230c41515baccbfab56aafcf31d5f
  pageDirectory: concepts
  sources:
    - scale-ray-clusters-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-cluster-scaling-best-practices
    - RCSBP
    - Ray Cluster Best Practices
    - Ray cluster best practices
    - Ray Cluster Scaling
    - Ray cluster best practice guide
  citations:
    - file: scale-ray-clusters-on-databricks-databricks-on-aws.md
title: Ray Cluster Scaling Best Practices
description: Recommended configurations for Ray worker nodes include minimum 4 CPU cores and 10GB heap memory per node, and setting num_cpus_worker_node to match Spark worker node CPU count for optimal resource utilization.
tags:
  - ray
  - scaling
  - best-practices
  - optimization
timestamp: "2026-06-19T20:19:19.793Z"
---

# Ray Cluster Scaling Best Practices

**Ray Cluster Scaling Best Practices** provides guidance on configuring and optimizing Ray cluster sizes on Databricks for performance, cost efficiency, and resource utilization. Proper scaling configuration ensures that Ray workloads run efficiently while minimizing idle resource costs and avoiding out-of-memory errors.

## Autoscaling Configuration

Starting in Ray 2.8.0, Ray clusters on Databricks support integration with Databricks autoscaling. This integration triggers Databricks cluster autoscaling internally within the Databricks environment. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

For Ray version 2.10 and onwards, use the following API to enable autoscaling:

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

The arguments `min_worker_nodes` and `max_worker_nodes` represent the range of Ray worker nodes to create and utilize for Ray workloads. If `min_worker_nodes` is left undefined, a fixed-size Ray cluster starts with `max_worker_nodes` workers. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

For Ray versions below 2.10, `num_worker_nodes` indicates the maximum number of Ray worker nodes when autoscaling is enabled. The default minimum number of Ray worker nodes is zero, meaning an idle cluster can scale down to zero nodes — this reduces costs but may impact responsiveness. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

### Tuning Autoscaling Speed

Two key arguments control scaling behavior:

- **`autoscale_upscaling_speed`**: The number of nodes allowed to be pending as a multiple of the current number of nodes. Higher values result in more aggressive upscaling. For example, a value of 1.0 means the cluster can grow by at most 100% at any time.
- **`autoscale_idle_timeout_minutes`**: The number of minutes before the autoscaler removes an idle worker node. Smaller values result in more aggressive downscaling.

With Ray 2.9.0 and above, you can set `autoscale_min_worker_nodes` to prevent the Ray cluster from scaling down to zero workers when idle, which would cause the cluster to terminate. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

## Recommended Worker Node Configuration

Databricks recommends the following minimum configuration for each Ray worker node:

- Minimum **4 CPU cores** per Ray worker node
- Minimum **10 GB heap memory** per Ray worker node

When calling `ray.util.spark.setup_ray_cluster`, set `num_cpus_per_node` to a value greater than or equal to 4. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

### Optimal CPU and GPU Allocation

Set `num_cpus_worker_node` to the number of CPU cores per Apache Spark worker node. Similarly, set `num_gpus_worker_node` to the number of GPUs per Spark worker node. With this configuration, each Spark worker node launches exactly one Ray worker node that fully utilizes the resources of each Spark worker node. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

To improve memory monitoring, set the environment variable `RAY_memory_monitor_refresh_ms` to `0` within the Databricks cluster configuration when starting your Spark cluster. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

## Memory Allocation for Ray Worker Nodes

Each Ray worker node uses two types of memory: heap memory and object store memory. The total memory allocated to each Ray worker node is calculated as:

```
RAY_WORKER_NODE_TOTAL_MEMORY = (SPARK_WORKER_NODE_PHYSICAL_MEMORY / MAX_NUMBER_OF_LOCAL_RAY_WORKER_NODES * 0.8)
```

`MAX_NUMBER_OF_LOCAL_RAY_WORKER_NODES` is the maximum number of Ray worker nodes that can be launched on a single Spark worker node, determined by `num_cpus_per_node` or `num_gpus_per_node`. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

If you do not set `object_store_memory_per_node`, the memory is split as:

- Heap memory: `RAY_WORKER_NODE_TOTAL_MEMORY * 0.7`
- Object store memory: `RAY_WORKER_NODE_TOTAL_MEMORY * 0.3`

If you set `object_store_memory_per_node`, heap memory becomes `RAY_WORKER_NODE_TOTAL_MEMORY - object_store_memory_per_node`. Note that object store memory is also capped by the operating system's shared memory (`/dev/shm`):

```
OBJECT_STORE_MEMORY_PER_NODE_CAP = (SPARK_WORKER_NODE_OS_SHARED_MEMORY / MAX_NUMBER_OF_LOCAL_RAY_WORKER_NODES * 0.8)
```

^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

## Head Node Configuration

By default, Databricks restricts resources allocated to the Ray head node to:
- 0 CPU cores
- 0 GPUs
- 128 MB heap memory
- 128 MB object store memory

This is intentional — the Ray head node is typically used only for global coordination, not for running Ray tasks. The Spark driver node resources are shared across multiple users. With Ray 2.8.0 and above, you can configure head node resources using `num_cpus_head_node`, `num_gpus_head_node`, and `object_store_memory_head_node`. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

## Heterogeneous Clusters

You can create a Ray on Spark cluster with different configurations between the head node and worker nodes. However, all Ray worker nodes must have identical configurations. While Databricks clusters do not fully support heterogeneous cluster configurations, you can create a cluster with different driver and worker instance types using a cluster policy. Example policy:

```json
{
  "node_type_id": {
    "type": "fixed",
    "value": "i3.xlarge"
  },
  "driver_node_type_id": {
    "type": "fixed",
    "value": "g4dn.xlarge"
  },
  "spark_version": {
    "type": "fixed",
    "value": "13.x-snapshot-gpu-ml-scala2.12"
  }
}
```

^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

## Hybrid Spark and Ray Workloads

### Memory Configuration

If you run hybrid Spark and Ray workloads in a Databricks cluster, reduce the Spark executor memory to a small value (e.g., `spark.executor.memory 4g`). The Spark executor is a Java process that triggers garbage collection lazily, and the Spark dataset cache consumes significant memory, reducing available memory for Ray. This configuration helps avoid potential out-of-memory errors. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

### Computation Resource Configuration

For hybrid workloads, make either the Databricks cluster nodes or Ray worker nodes auto-scalable:

- With a fixed number of worker nodes: Enable Ray-on-Spark autoscaling. When no Ray workloads are running, the Ray cluster scales down, freeing resources for Spark tasks. When Spark tasks finish and Ray is used again, the Ray cluster scales back up. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

- With both auto-scalable: Configure the Databricks cluster's auto-scalable nodes to a maximum of 10 nodes, the Ray-on-Spark worker nodes to a maximum of 4 nodes, and each Ray worker node to fully utilize Spark worker resources. In this setup, Ray workloads can use at most 4 nodes, while Spark jobs can allocate up to 6 nodes. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Ray on Databricks](/concepts/ray-on-databricks.md)
- Apache Spark
- Distributed Computing
- Autoscaling
- GPU Cluster Configuration

## Sources

- scale-ray-clusters-on-databricks-databricks-on-aws.md

# Citations

1. [scale-ray-clusters-on-databricks-databricks-on-aws.md](/references/scale-ray-clusters-on-databricks-databricks-on-aws-ad8172f6.md)
