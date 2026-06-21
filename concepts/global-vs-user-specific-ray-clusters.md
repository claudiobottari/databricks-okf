---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 34c28220e40332266d04309df913e65fcda217c9f05d4ab7c961d02f1eb2a030
  pageDirectory: concepts
  sources:
    - create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - global-vs-user-specific-ray-clusters
    - GVURC
  citations:
    - file: create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
title: Global vs User-Specific Ray Clusters
description: "Two lifecycle modes for Ray clusters on Databricks: single-user clusters tied to notebook sessions and shared global clusters accessible by all workspace users."
tags:
  - ray
  - databricks
  - cluster-management
timestamp: "2026-06-18T11:16:36.694Z"
---

# Global vs User-Specific Ray Clusters

**Global vs User-Specific Ray Clusters** describes two modes for running Ray compute clusters on Databricks: user-specific clusters that are tied to a single notebook user and automatically shut down after inactivity, and global clusters that are shared across all users attached to the Databricks compute resource and remain active until explicitly stopped.

## User-Specific Ray Clusters

A user-specific (also called single-user) Ray cluster is created using the `ray.util.spark.setup_ray_cluster` API. This type of cluster is only available to the current notebook user. It is automatically shut down after the notebook is detached from the Databricks cluster or after 30 minutes of inactivity (no tasks submitted to Ray).^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
import ray
from ray.util.spark import setup_ray_cluster, shutdown_ray_cluster

setup_ray_cluster(
  max_worker_nodes=1,
  collect_log_to_path="/dbfs/path/to/ray_collected_logs"
)

ray.init(ignore_reinit_error=True)
```

User-specific clusters support both fixed-size and auto-scaling configurations. Fixed-size clusters specify a maximum number of worker nodes, while auto-scaling clusters can dynamically adjust based on workload.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Global Ray Clusters

Global mode Ray clusters, available with Ray 2.9.0 and above, are created using the `setup_global_ray_cluster` API. A global mode cluster allows all users attached to the Databricks compute resource to use the Ray cluster. This mode does not have the automatic inactivity timeout that applies to user-specific clusters.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
from ray.util.spark import setup_global_ray_cluster

setup_global_ray_cluster(
  max_worker_nodes=2,
  # other arguments are the same as setup_ray_cluster
)
```

The `setup_global_ray_cluster` call is blocking and remains active until it is interrupted by clicking the "Interrupt" button on the notebook command cell, detaching the notebook from the Databricks cluster, or terminating the Databricks cluster. Otherwise, the global mode Ray cluster continues running and is available for task submission by authorized users.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Key Differences

| Feature | User-Specific Cluster | Global Cluster |
|---------|----------------------|----------------|
| **Scope** | Single notebook user only | All users on the Databricks cluster |
| **Lifetime** | Auto-shutdown after 30 min inactivity | No automatic shutdown timeout |
| **Creation API** | `setup_ray_cluster()` | `setup_global_ray_cluster()` |
| **Concurrent instances** | Multiple allowed | One per Databricks cluster |
| **Suitable for** | Development, single-user tasks | Shared workloads, multi-user access |

Compared to user-specific clusters, global clusters are intended for scenarios where multiple users need to share the same Ray compute resource without each user starting their own cluster. However, because multiple users can access this Ray cluster, resource contention might be an issue.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Choosing Between Modes

Use a user-specific Ray cluster when:
- You are developing or debugging in a single notebook.
- You want the cluster to shut down automatically after idle periods.
- You do not need to share the Ray compute with other users.

Use a global Ray cluster when:
- Multiple users on the same Databricks cluster need to submit Ray tasks.
- You need the Ray cluster to remain available across notebook sessions without being interrupted by notebook detachment.
- You are running production workloads that require persistent availability.

## Related Concepts

- [Ray on Databricks](/concepts/ray-on-databricks.md) — Overview of running Ray on Databricks
- [Scale Ray clusters on Databricks](/concepts/ray-cluster-on-databricks.md) — Auto-scaling Ray clusters
- Setup Ray Cluster API — The `setup_ray_cluster()` API for user-specific clusters
- Setup Global Ray Cluster API — The `setup_global_ray_cluster()` API for global mode
- Ray Client — Connecting to remote Ray clusters
- Ray Dashboard — Monitoring Ray cluster state and performance

## Sources

- create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md

# Citations

1. [create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md](/references/create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws-68773ede.md)
