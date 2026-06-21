---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a09d339a2a381a6774ac5c127e2d7e99d7b175627b7fdb5a0a87e0c53cb751b2
  pageDirectory: concepts
  sources:
    - create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - fixed-size-vs-auto-scaling-ray-clusters
    - FVARC
    - Auto-scaling Ray Clusters
    - Autoscaling Ray Clusters
    - autoscaling clusters
  citations:
    - file: create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
title: Fixed-Size vs Auto-Scaling Ray Clusters
description: Ray cluster sizing strategies on Databricks, including fixed-size clusters with explicit worker counts and auto-scaling clusters that adjust capacity dynamically.
tags:
  - ray
  - databricks
  - scaling
timestamp: "2026-06-18T11:16:17.253Z"
---

# Fixed-Size vs Auto-Scaling Ray Clusters

**Fixed-size Ray clusters** and **auto-scaling Ray clusters** are two modes for running Ray compute on Databricks. The choice between them depends on workload characteristics, resource predictability, and cost optimization requirements.

## Overview

A Ray cluster on Databricks runs on top of a Databricks Spark cluster. You create a Ray cluster using the `ray.util.spark.setup_ray_cluster` API within a notebook attached to a Databricks cluster. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Fixed-Size Ray Clusters

In a fixed-size Ray cluster, you specify the exact number of worker nodes using the `max_worker_nodes` parameter. The cluster launches the specified number of workers and maintains that size throughout its lifetime. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
import ray
from ray.util.spark import setup_ray_cluster, shutdown_ray_cluster

setup_ray_cluster(
  max_worker_nodes=1,
  collect_log_to_path="/dbfs/path/to/ray_collected_logs"
)

ray.init(ignore_reinit_error=True)
```

^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Characteristics

- **Predictable resource allocation** — The number of worker nodes remains constant, making resource planning straightforward.
- **No scaling delays** — Workers are available immediately after startup; there is no wait for nodes to spin up or down during execution.
- **Suitable for steady-state workloads** — Ideal for workloads with consistent, predictable resource demands over time.

### Resource Configuration

You can also specify CPU and GPU resources per node for both head and worker nodes: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
setup_ray_cluster(
  min_worker_nodes=2,
  max_worker_nodes=4,
  num_cpus_per_node=8,
  num_gpus_per_node=1,
  num_cpus_head_node=8,
  num_gpus_head_node=1,
  collect_log_to_path="/dbfs/path/to/ray_collected_logs"
)
```

^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Auto-Scaling Ray Clusters

Auto-scaling Ray clusters dynamically adjust the number of worker nodes based on workload demand. For detailed instructions on setting up auto-scaling, see [Scale Ray clusters on Databricks](/concepts/ray-cluster-on-databricks.md). ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Characteristics

- **Dynamic resource allocation** — Worker nodes scale up during peak demand and scale down when demand decreases.
- **Cost optimization** — Resources are only provisioned when needed, reducing idle resource costs.
- **Suitable for variable workloads** — Ideal for workloads with fluctuating demand or periodic processing needs.

### Configuration

Auto-scaling is configured through the `min_worker_nodes` and `max_worker_nodes` parameters: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
setup_ray_cluster(
  min_worker_nodes=2,
  max_worker_nodes=4,
  num_cpus_per_node=8,
  num_gpus_per_node=1,
  num_cpus_head_node=8,
  num_gpus_head_node=1,
  collect_log_to_path="/dbfs/path/to/ray_collected_logs"
)
```

^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Comparison

| Aspect | Fixed-Size | Auto-Scaling |
|--------|------------|--------------|
| Worker node count | Constant (set via `max_worker_nodes`) | Dynamic (between `min_worker_nodes` and `max_worker_nodes`) |
| Resource availability | Immediate | Subject to scaling latency |
| Cost efficiency | Lower for variable workloads | Higher for variable workloads |
| Use case | Steady-state, predictable workloads | Variable, bursty, or periodic workloads |
| Configuration parameter | `max_worker_nodes` | `min_worker_nodes` and `max_worker_nodes` |

## Session Management

By default, when you create a Ray cluster in a notebook, it is only available to the current notebook user. The cluster automatically shuts down after the notebook is detached from the cluster or after 30 minutes of inactivity (no tasks submitted to Ray). For a cluster shared across all users that is not subject to notebook activity, use the `setup_global_ray_cluster` API instead. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Best Practices

- **For non-GPU workloads**, set `spark.task.resource.gpu.amount` to 0 in the Spark cluster configuration to reserve GPU resources for Ray tasks only. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]
- **Set a log output location** using `collect_log_to_path` with a path starting with `/dbfs/` or a Unity Catalog Volume path to preserve logs after cluster termination. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]
- **Prerequisites**: Databricks Runtime 12.2 LTS ML and above, with dedicated or no isolation shared access mode. Ray clusters are not supported on [serverless compute](/concepts/serverless-gpu-compute.md). ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Ray on Databricks](/concepts/ray-on-databricks.md) — Overview of Ray integration with Databricks
- [Scale Ray clusters on Databricks](/concepts/ray-cluster-on-databricks.md) — Detailed guide on auto-scaling configuration
- Databricks Spark cluster — The underlying compute infrastructure for Ray clusters
- [Global Ray clusters](/concepts/global-mode-ray-clusters.md) — Shared-mode Ray clusters accessible by multiple users

## Sources

- create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md

# Citations

1. [create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md](/references/create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws-68773ede.md)
