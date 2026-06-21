---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 71ce53ae4bb152cbc3b63bcda847d87c742954ad06a74f1fff3b80ebcc6738c9
  pageDirectory: concepts
  sources:
    - create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - single-user-vs-global-ray-clusters
    - SVGRC
    - Single-User Ray Clusters
    - Single-User Ray Cluster
  citations:
    - file: create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
title: Single-User vs Global Ray Clusters
description: "Two modes for Ray clusters on Databricks: user-scoped clusters with auto-shutdown and shared global clusters without timeout"
tags:
  - ray
  - databricks
  - cluster-modes
timestamp: "2026-06-19T09:31:36.820Z"
---

# Single-User vs Global Ray Clusters

**Single-User vs Global Ray Clusters** describes the two distinct modes for running Ray clusters on Databricks. The choice between a user-specific (single-user) Ray cluster and a global Ray cluster determines who can submit tasks, how long the cluster remains active, and whether multiple users can share the same Ray instance.

## Overview

Ray clusters on Databricks can be created in two modes: single-user (also called "dedicated") mode and global mode. The mode you choose affects the cluster's lifecycle, availability, and access control. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Prerequisites

To create any Ray cluster on Databricks, you must have access to a Databricks all-purpose compute resource using **Databricks Runtime 12.2 LTS ML and above** with either **Dedicated (formerly single user)** or **No Isolation Shared** access mode. Ray clusters are not supported on serverless compute. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

With Databricks Runtime ML 15.0 and later, Ray is pre-installed on Databricks clusters. For earlier runtimes, you must install Ray manually using `%pip install ray[default]>=2.3.0`. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Single-User (User-Specific) Ray Clusters

A single-user Ray cluster is created within a notebook using the `setup_ray_cluster()` API and is available **only to the current notebook user**. This is the default behavior. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Key Characteristics

- **Scope**: The Ray cluster is tied to the active notebook session. Only the user who created the cluster can submit tasks to it. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]
- **Automatic shutdown**: The single-user Ray cluster shuts down automatically when the notebook is **detached from the cluster** or after **30 minutes of inactivity** (no tasks submitted to Ray). ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]
- **Use case**: Ideal for development work, experimentation, and tasks where only one user needs access to the Ray resources. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Creating a Single-User Ray Cluster

```python
from ray.util.spark import setup_ray_cluster, shutdown_ray_cluster

setup_ray_cluster(
  max_worker_nodes=1,
  collect_log_to_path="/dbfs/path/to/ray_collected_logs"
)

ray.init(ignore_reinit_error=True)
```

^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Global Ray Clusters

Introduced in **Ray 2.9.0 and above**, a global mode Ray cluster allows **all users attached to the same Databricks compute resource** to use the Ray cluster. It is created using the `setup_global_ray_cluster()` API. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Key Characteristics

- **Multi-user access**: Any user with an attached notebook can connect to the active global Ray cluster by calling `ray.init()`. Because multiple users can access the same Ray cluster, resource contention may occur. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]
- **No automatic timeout**: A global mode Ray cluster **does not have the 30-minute inactivity timeout** that single-user clusters have. It remains active until the `setup_global_ray_cluster` call is interrupted, the notebook is detached, or the Databricks cluster is terminated. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]
- **Singleton**: Only **one active global mode Ray cluster** can exist at a time within a single Databricks cluster. Creating a new global cluster requires stopping the existing one first. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

### Creating a Global Ray Cluster

Global mode Ray clusters are started from a **notebook job** attached to a shared-mode Databricks cluster. The call is **blocking** — it remains active until interrupted. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
from ray.util.spark import setup_global_ray_cluster

setup_global_ray_cluster(
  max_worker_nodes=2,
  ...  # other arguments are the same as with setup_ray_cluster
)
```

^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Comparison Summary

| Feature | Single-User (Dedicated) | Global |
|---|---|---|
| **Access** | Only current notebook user | All users on the cluster |
| **Automatic shutdown** | Yes (30 min inactivity or detach) | No (must be interrupted manually) |
| **Maximum active clusters** | Multiple possible per cluster | One at a time |
| **Creation API** | `setup_ray_cluster()` | `setup_global_ray_cluster()` |
| **Introduced in** | Ray 2.3.0+ | Ray 2.9.0+ |
| **Resource contention** | None (single user) | Possible (multiple users) |

^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Choosing Between Modes

- **Use Single-User mode** for development, experimentation, and cases where only one notebook user needs Ray resources. It provides automatic cleanup and reduced resource contention. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]
- **Use Global mode** when multiple users need to access the same Ray cluster for shared workloads, production monitoring, or longer-running tasks that should not be interrupted by inactivity timeouts. ^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Ray on Databricks](/concepts/ray-on-databricks.md)
- Ray Cluster Lifecycle Management
- Ray Auto-Scaling
- Ray GPU Clusters
- Ray Dashboard
- [Ray Client Remote Connection](/concepts/ray-client-remote-connection.md)
- [Ray Log Collection](/concepts/ray-log-collection-on-databricks.md)

## Sources

- create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md

# Citations

1. [create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md](/references/create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws-68773ede.md)
