---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 669fce44367520a115fc8b2b56bc2bcb85d2f066987b9695fbced8933cc686ad
  pageDirectory: concepts
  sources:
    - scale-ray-clusters-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-head-node-resource-configuration
    - RHNRC
    - Ray Head Node Configuration
    - Ray Worker Node Resource Configuration
  citations:
    - file: scale-ray-clusters-on-databricks-databricks-on-aws.md
title: Ray Head Node Resource Configuration
description: Databricks restricts Ray head node resources by default (0 CPU, 0 GPU, 128 MB memory) since it's used for coordination, but allows configuration of CPU, GPU, and memory for the head node via setup_ray_cluster API parameters.
tags:
  - ray
  - databricks
  - resource-allocation
  - cluster-configuration
timestamp: "2026-06-19T20:18:38.771Z"
---

# Ray Head Node Resource Configuration

**Ray Head Node Resource Configuration** refers to the settings that control how many CPU cores, GPUs, and memory resources are allocated to the Ray head node when running Ray on Apache Spark within Databricks. Proper configuration of these resources is important for balancing coordination overhead with resource efficiency on the Spark driver node.

## Default Resource Allocation

By default, Databricks restricts resources allocated to the Ray head node to the following minimum values:

- **0 CPU cores**
- **0 GPUs**
- **128 MB heap memory**
- **128 MB object store memory**

This conservative default exists because the Ray head node is typically used only for global coordination, not for executing Ray tasks. The Apache Spark driver node resources are shared across multiple users, so the default setting conserves resources on the driver side. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

## Configuring Head Node Resources

With Ray 2.8.0 and above, you can override the default resource allocation for the Ray head node using the following arguments in the `setup_ray_cluster` API:

- **`num_cpus_head_node`**: Sets the number of CPU cores allocated to the Ray head node.
- **`num_gpus_head_node`**: Sets the number of GPUs allocated to the Ray head node.
- **`object_store_memory_head_node`**: Sets the object store memory size for the Ray head node.

These arguments allow you to dedicate more resources to the head node when it needs to perform additional coordination or lightweight computation tasks. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

## Relationship to Heterogeneous Clusters

The head node resource configuration is part of Databricks' support for [Heterogeneous Ray Clusters](/concepts/heterogeneous-ray-clusters-on-databricks.md), where the Ray head node and Ray worker nodes can have different configurations. While all Ray worker nodes must share the same configuration, the head node can be configured independently. This enables more efficient and cost-effective training runs by allowing the head node to use a different instance type than the worker nodes. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

## Best Practices

When configuring head node resources, consider the following:

- If the head node is only performing coordination tasks, the default minimal allocation is appropriate and conserves driver resources.
- If the head node needs to run lightweight tasks or handle significant metadata, increase `num_cpus_head_node` and memory settings accordingly.
- For GPU workloads, only allocate GPUs to the head node (`num_gpus_head_node`) if the head node will directly execute GPU tasks; otherwise, keep the default of 0 GPUs.

## Related Concepts

- Ray Cluster Autoscaling — Configuring dynamic scaling of Ray worker nodes.
- Ray Worker Node Resource Configuration — Resource allocation for Ray worker nodes.
- [Heterogeneous Ray Clusters](/concepts/heterogeneous-ray-clusters-on-databricks.md) — Using different configurations for head and worker nodes.
- [Ray on Databricks](/concepts/ray-on-databricks.md) — Overview of running Ray clusters on the Databricks platform.
- Apache Spark Driver Node — The node that hosts the Ray head node and shares resources with other users.

## Sources

- scale-ray-clusters-on-databricks-databricks-on-aws.md

# Citations

1. [scale-ray-clusters-on-databricks-databricks-on-aws.md](/references/scale-ray-clusters-on-databricks-databricks-on-aws-ad8172f6.md)
