---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 239aa9a7d70e1fd6caeac9bcabe524bfee0d3633824f553a84f4801cb2eaa39c
  pageDirectory: concepts
  sources:
    - scale-ray-clusters-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-on-spark-cluster-architecture
    - ROSCA
  citations:
    - file: scale-ray-clusters-on-databricks-databricks-on-aws.md
title: Ray on Spark Cluster Architecture
description: Ray on Spark creates a Ray cluster via a background Apache Spark job where each Spark task creates a Ray worker node, and the Ray head node runs on the Spark driver, with API version differences between Ray <2.10 and >=2.10.
tags:
  - ray
  - spark
  - architecture
  - cluster-setup
timestamp: "2026-06-19T20:19:16.060Z"
---

# Ray on Spark Cluster Architecture

**Ray on Spark Cluster Architecture** describes how Ray clusters are deployed and managed within Apache Spark environments on Databricks. This integration allows users to run distributed Ray workloads alongside Spark jobs, leveraging the same infrastructure while benefiting from Ray's flexible task and actor programming model.

## Overview

When a Ray cluster is started on Databricks using Spark, the `ray.util.spark.setup_ray_cluster` API creates a Ray cluster on top of Apache Spark. Internally, it creates a background Spark job. Each Spark task in that job creates a Ray worker node, while the Ray head node is created on the Spark driver. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

## Cluster Components

### Head Node

The Ray head node is responsible for global coordination of the Ray cluster. By default, Databricks restricts resources allocated to the head node to:
- 0 CPU cores
- 0 GPUs
- 128 MB heap memory
- 128 MB object store memory

This conservative default preserves resources on the Spark driver side, which may be shared with multiple users. With Ray 2.8.0 and above, you can configure the head node's resources using `num_cpus_head_node`, `num_gpus_head_node`, and `object_store_memory_head_node` arguments in the `setup_ray_cluster` API. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

### Worker Nodes

Each Spark task creates one Ray worker node. The number of worker nodes is determined by the `min_worker_nodes` and `max_worker_nodes` arguments (for Ray 2.10+) or `num_worker_nodes` (for earlier versions). Each worker node can be configured with a specific number of CPU cores (`num_cpus_worker_node`, default: 1) or GPUs (`num_gpus_worker_node`, default: 0). ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

## Autoscaling

Starting with Ray 2.8.0, Ray clusters on Databricks support integration with Databricks autoscaling. When enabled, the autoscaling mechanism triggers Databricks cluster autoscaling internally. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

For Ray versions below 2.10, when autoscaling is enabled, `num_worker_nodes` indicates the maximum number of Ray worker nodes, with a default minimum of zero workers. This means an idle Ray cluster can scale down to zero workers, reducing costs but potentially impacting responsiveness. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

For Ray 2.10 and onwards, you specify `min_worker_nodes` and `max_worker_nodes` to define the allowed range. If `min_worker_nodes` is left undefined, a fixed-size cluster is started with `max_worker_nodes` workers. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

### Autoscaling Configuration

Two key parameters control scaling behavior:
- `autoscale_upscaling_speed`: The number of nodes allowed to be pending as a multiple of the current node count. Higher values mean more aggressive upscaling.
- `autoscale_idle_timeout_minutes`: The number of minutes before an idle worker node is removed. Lower values mean more aggressive downscaling.

With Ray 2.9.0 and above, you can set `autoscale_min_worker_nodes` to prevent the cluster from scaling down to zero workers when idle. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

## Memory Allocation for Worker Nodes

Each Ray worker node uses two types of memory: heap memory and object store memory. The allocation is calculated as follows:

- Total memory per Ray worker node: `RAY_WORKER_NODE_TOTAL_MEMORY = (SPARK_WORKER_NODE_PHYSICAL_MEMORY / MAX_NUMBER_OF_LOCAL_RAY_WORKER_NODES * 0.8)`
- If `object_store_memory_per_node` is not set: heap memory = total memory × 0.7, object store memory = total memory × 0.3
- If `object_store_memory_per_node` is set: heap memory = total memory - argument value
- Object store memory is capped by operating system shared memory: `OBJECT_STORE_MEMORY_PER_NODE_CAP = (SPARK_WORKER_NODE_OS_SHARED_MEMORY / MAX_NUMBER_OF_LOCAL_RAY_WORKER_NODES * 0.8)`

`MAX_NUMBER_OF_LOCAL_RAY_WORKER_NODES` is determined by the `num_cpus_per_node` or `num_gpus_per_node` argument. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

## Heterogeneous Clusters

You can create a Ray on Spark cluster with different configurations between the Ray head node and Ray worker nodes. However, all Ray worker nodes must share the same configuration. While Databricks clusters do not fully support heterogeneous clusters, you can set different driver and worker instance types using a cluster policy. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

## Recommended Configuration

For optimal performance, Databricks recommends:
- Minimum 4 CPU cores per Ray worker node (`num_cpus_per_node >= 4`)
- Minimum 10 GB heap memory for each Ray worker node
- Setting `num_cpus_worker_node` to match the number of CPU cores per Spark worker node, so each Spark worker node launches exactly one Ray worker node that fully utilizes its resources
- Setting the environment variable `RAY_memory_monitor_refresh_ms` to `0` in the Databricks cluster configuration when starting the Spark cluster ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

## Hybrid Spark and Ray Workloads

When running hybrid Spark and Ray workloads on the same Databricks cluster:

- Reduce Spark executor memory to a small value (e.g., `spark.executor.memory 4g`) to avoid out-of-memory errors caused by lazy Java garbage collection and Spark dataset caching.
- Enable Ray-on-Spark autoscaling so Ray releases resources when idle, allowing Spark to use them.
- Configure both the Databricks cluster and Ray-on-Spark cluster for autoscaling. For example, with a Databricks cluster that can scale to 10 nodes, you could configure Ray to use at most 4 nodes, leaving up to 6 nodes for Spark jobs. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

## Related Concepts

- Ray — The distributed computing framework
- [Ray Autoscaling](/concepts/ray-on-databricks-autoscaling.md) — Dynamic scaling of Ray worker nodes
- Databricks Autoscaling — Infrastructure-level autoscaling on Databricks
- [Distributed Training](/concepts/workload-yaml-for-distributed-training.md) — Training large models across multiple nodes
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — On-demand GPU resources on Databricks
- [8xH100 Single-Node Configuration](/concepts/8xh100-single-node-configuration.md) — Multi-GPU configuration for distributed workloads

## Sources

- scale-ray-clusters-on-databricks-databricks-on-aws.md

# Citations

1. [scale-ray-clusters-on-databricks-databricks-on-aws.md](/references/scale-ray-clusters-on-databricks-databricks-on-aws-ad8172f6.md)
