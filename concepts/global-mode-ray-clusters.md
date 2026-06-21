---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 681e14fbe95fec11b5c08748c407eb88517c3e022c3e5c96e79d1001194e5da1
  pageDirectory: concepts
  sources:
    - create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - global-mode-ray-clusters
    - GMRC
    - Global Ray clusters
  citations:
    - file: create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
title: Global mode Ray clusters
description: Shared Ray clusters accessible by all users attached to a Databricks cluster, created via setup_global_ray_cluster, with no automatic shutdown timeout
tags:
  - ray
  - databricks
  - multi-user
timestamp: "2026-06-18T14:49:40.392Z"
---

# Global Mode Ray Clusters

**Global mode Ray clusters** are a type of [Ray cluster](/concepts/global-mode-ray-cluster.md) on Databricks that allows all users attached to a Databricks compute resource to share and use the same Ray cluster. Unlike single-user Ray clusters, global mode clusters persist until explicitly interrupted and do not have automatic shutdown timeouts. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Overview

Introduced with Ray 2.9.0 and above, global mode Ray clusters enable multi-user collaboration on the same Databricks cluster. They are created using the `setup_global_ray_cluster()` API instead of the standard `setup_ray_cluster()` API. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

This mode is useful when multiple team members need to submit Ray tasks to the same cluster without each user creating their own Ray instance. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Creating a Global Mode Ray Cluster

To create a global mode Ray cluster, start by creating a Databricks notebook job and attaching it to a shared mode Databricks cluster. Then run the following command: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
from ray.util.spark import setup_global_ray_cluster

setup_global_ray_cluster(
  max_worker_nodes=2,
  ...  # other arguments are the same as with the `setup_ray_cluster` API
)
```

The call is blocking and remains active until one of the following occurs:
- You click the **Interrupt** button on the notebook command cell.
- You detach the notebook from the Databricks cluster.
- You terminate the Databricks cluster.

Otherwise, the global mode Ray cluster continues to run and remains available for task submission by authorized users. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Connecting to a Global Mode Ray Cluster

Once a global mode Ray cluster is active, any user attached to the same Databricks cluster can connect to it by running `ray.init()` in their notebook. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
import ray
ray.init(ignore_reinit_error=True)
```

## Key Properties

Global mode Ray clusters have the following characteristics: ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

- **Single active cluster**: In a Databricks cluster, you can only create one active global mode Ray cluster at a time.
- **Multi-user access**: The active global mode Ray cluster can be used by all users in any attached Databricks notebook.
- **No automatic timeout**: Global mode Ray clusters do not have the automatic shutdown timeout that single-user Ray clusters have (30 minutes of inactivity). They remain up until the `setup_global_ray_cluster` call is explicitly interrupted.

## Resource Contention

Because multiple users can access the same global mode Ray cluster simultaneously, resource contention might be an issue. Users should be aware of this when planning workloads on shared global mode clusters. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Comparison with Single-User Ray Clusters

| Feature | Global Mode | Single-User Mode |
|---------|-------------|-----------------|
| API | `setup_global_ray_cluster()` | `setup_ray_cluster()` |
| User scope | All users on the Databricks cluster | Current notebook user only |
| Automatic shutdown | No (must be interrupted) | Yes (30 min inactivity or notebook detach) |
| Maximum per Databricks cluster | 1 | Multiple |

## Best Practices

- Use global mode Ray clusters when multiple team members need to share computational resources for Ray workloads. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]
- Monitor resource usage to avoid contention between users. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]
- Ensure the `setup_global_ray_cluster` call is explicitly interrupted when the cluster is no longer needed to free up resources. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Ray Cluster](/concepts/global-mode-ray-cluster.md) — The underlying Ray compute infrastructure
- Single-User Ray Clusters — User-specific Ray clusters with automatic timeouts
- Ray Setup API — The `setup_ray_cluster()` and `setup_global_ray_cluster()` APIs
- Scaling Ray Clusters on Databricks — Auto-scaling configurations for Ray workloads
- Databricks GPU Support — GPU configuration for Ray clusters

## Sources

- create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md

# Citations

1. [create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md](/references/create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws-68773ede.md)
