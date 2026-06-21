---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 28cea114cb982122f6f71b2235fd033ff4cfbcb9bda73efae80f0b3a5801ff98
  pageDirectory: concepts
  sources:
    - create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - global-mode-ray-cluster
    - GMRC
    - Global Ray Cluster
    - Ray Cluster
    - Ray cluster
    - global-mode-ray-clusters
    - Global Ray clusters
  citations:
    - file: create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md
title: Global Mode Ray Cluster
description: A shared Ray cluster on Databricks accessible by multiple users with no automatic inactivity timeout, started via setup_global_ray_cluster
tags:
  - ray
  - databricks
  - multi-user
timestamp: "2026-06-19T17:58:04.759Z"
---

# Global Mode Ray Cluster

**Global Mode Ray Cluster** refers to a Ray cluster running on a Databricks compute resource that is accessible to all users attached to that Databricks cluster. Unlike single-user Ray clusters, a global mode cluster persists until explicitly interrupted and does not have an automatic shutdown timeout, making it suitable for shared workloads across multiple users.

## Overview

Introduced with Ray 2.9.0 and above, global mode Ray clusters allow multiple users attached to the same Databricks compute resource to connect to and submit tasks on a single Ray cluster. This capability enables collaborative Ray workloads in a shared Databricks environment.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Starting a Global Mode Ray Cluster

To create a global mode Ray cluster, use the `ray.util.spark.setup_global_ray_cluster` API. This is a blocking call that remains active until interrupted by clicking the "Interrupt" button on the notebook command cell, detaching the notebook from the Databricks cluster, or terminating the Databricks cluster.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

```python
from ray.util.spark import setup_global_ray_cluster

setup_global_ray_cluster(
  max_worker_nodes=2,
  ...  # other arguments are the same as with the `setup_ray_cluster` API.
)
```

It is recommended to start the global mode Ray cluster from a Databricks notebook job attached to a shared mode Databricks cluster.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Properties

Global mode Ray clusters have the following defining characteristics:^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

- **Single active cluster per Databricks cluster:** Only one active global mode Ray cluster can exist on a given Databricks compute resource at a time.
- **Multi-user access:** All users with access to the Databricks cluster can use the global mode Ray cluster from any attached Databricks notebook. Users call `ray.init()` to connect to the active global mode Ray cluster.
- **No automatic timeout:** Unlike single-user Ray clusters, global mode Ray clusters do not have a 30-minute inactivity shutdown timeout. The cluster remains active until the `setup_global_ray_cluster` call is explicitly interrupted.
- **Resource contention:** Because multiple users can submit tasks simultaneously, resource contention may occur.

## Comparison with Single-User Ray Clusters

| Feature | Single-User Ray Cluster | Global Mode Ray Cluster |
|---------|------------------------|-------------------------|
| API | `setup_ray_cluster()` | `setup_global_ray_cluster()` |
| User scope | Current notebook user only | All users on the Databricks cluster |
| Auto-shutdown | After 30 minutes of inactivity or notebook detach | None (persists until interrupted) |
| Connection method | Automatic via `ray.init()` in same notebook | `ray.init()` from any attached notebook |
| Shared state | No | Yes |

## Requirements

To create a global mode Ray cluster:^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

- Databricks Runtime 12.2 LTS ML and above
- Dedicated (formerly single user) or no isolation shared access modes
- Ray 2.9.0 or above (preinstalled on Databricks Runtime ML 15.0+)

Global mode Ray clusters are not supported on serverless compute.^[create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md]

## Use Cases

Global mode Ray clusters are particularly useful when:

- Multiple team members need to share a single Ray cluster for collaborative development
- Long-running Ray applications must stay active beyond a single notebook session
- Resource pooling across user workloads is desirable

## Related Concepts

- [Ray Clusters on Databricks](/concepts/ray-cluster-on-databricks.md) — General Ray cluster creation and configuration
- [Single-User Ray Cluster](/concepts/single-user-vs-global-ray-clusters.md) — Ray clusters scoped to an individual notebook user
- Ray Util Spark API — The `ray.util.spark` module for cluster management
- Databricks Shared Compute — Shared access mode compute resources

## Sources

- create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md

# Citations

1. [create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws.md](/references/create-and-connect-to-ray-clusters-on-databricks-databricks-on-aws-68773ede.md)
