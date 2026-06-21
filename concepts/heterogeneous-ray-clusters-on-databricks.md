---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7f5694ee8bb61611671161c4ca5fd3c4f09b80f131d561c464f4a5a2db9a24f0
  pageDirectory: concepts
  sources:
    - scale-ray-clusters-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - heterogeneous-ray-clusters-on-databricks
    - HRCOD
    - Heterogeneous Clusters on Databricks
    - Heterogeneous Ray Clusters
  citations:
    - file: scale-ray-clusters-on-databricks-databricks-on-aws.md
title: Heterogeneous Ray Clusters on Databricks
description: Ray on Spark clusters allow different configurations between head and worker nodes, but all worker nodes must share the same configuration; Databricks supports this via cluster policies with different driver and worker instance types.
tags:
  - ray
  - databricks
  - heterogeneous-clusters
  - cluster-policy
timestamp: "2026-06-19T20:18:43.811Z"
---

# Heterogeneous Ray Clusters on Databricks

**Heterogeneous Ray Clusters on Databricks** refer to the ability to run a Ray on Spark cluster where the Ray head node and Ray worker nodes can use different hardware configurations, while all Ray worker nodes within the same cluster must share an identical configuration. This approach can lead to more efficient and cost-effective training runs by matching resource types to the roles they perform. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

## Capabilities and Limitations

Databricks clusters do not provide full native support for heterogeneous worker nodes. However, you can create a Databricks cluster with different driver and worker instance types by applying a Databricks Cluster Policy. This policy-based approach allows the Ray head node (which runs on the Spark driver) to use a different instance type than the Ray worker nodes (which run on Spark executors). Critically, all Ray worker nodes must use exactly the same instance type; mixing different worker types within a single Ray cluster is not supported. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

## Configuring a Heterogeneous Cluster via Cluster Policy

To set up a heterogeneous Ray cluster, define a cluster policy that specifies a fixed `node_type_id` for worker nodes and a fixed `driver_node_type_id` for the driver node. The following example policy uses an `i3.xlarge` instance type for workers and a `g4dn.xlarge` instance type for the driver, with a GPU-enabled Spark version: ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

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

This policy enforces that the driver (which hosts the Ray head node) uses a GPU-capable instance while the workers use a CPU‑only instance. All worker nodes remain homogeneous. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

## Related Concepts

- Ray on Spark – The framework that launches Ray clusters inside Apache Spark.
- Databricks Cluster Policies – Administrative tools for enforcing cluster configuration rules.
- [Autoscaling Ray Clusters](/concepts/fixed-size-vs-auto-scaling-ray-clusters.md) – Scaling Ray worker nodes up and down based on workload.
- Ray Head Node Configuration – How to allocate CPU, GPU, and memory resources to the head node.
- Memory Allocation for Ray Worker Nodes – Details on heap and object store memory per worker.

## Sources

- scale-ray-clusters-on-databricks-databricks-on-aws.md

# Citations

1. [scale-ray-clusters-on-databricks-databricks-on-aws.md](/references/scale-ray-clusters-on-databricks-databricks-on-aws-ad8172f6.md)
