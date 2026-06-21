---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cbbb1095222ce980420c8b060258d5e6ba9e822c3d44da71c8d0920daeb14efe
  pageDirectory: concepts
  sources:
    - scale-ray-clusters-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-worker-node-memory-allocation
    - RWNMA
  citations:
    - file: scale-ray-clusters-on-databricks-databricks-on-aws.md
title: Ray Worker Node Memory Allocation
description: Memory allocation for Ray worker nodes is determined by physical memory per Spark worker, number of local Ray nodes, and configurable object store memory, with heap and object store split ratios and OS shared memory caps.
tags:
  - ray
  - memory-management
  - resource-allocation
  - databricks
timestamp: "2026-06-19T20:18:50.967Z"
---

# Ray Worker Node Memory Allocation

**Ray Worker Node Memory Allocation** refers to the mechanism by which memory is distributed to each Ray worker node when a Ray cluster is started on Apache Spark via Databricks. The allocation logic determines both heap memory (used for Python objects, tasks, and actors) and object store memory (used for shared memory objects and distributed data transfers). Understanding this allocation is critical for tuning Ray performance and avoiding out-of-memory errors.

## Total Memory per Ray Worker Node

The total memory available to a single Ray worker node is derived from the physical memory of the underlying Apache Spark worker node. It is calculated using the following formula: ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

```
RAY_WORKER_NODE_TOTAL_MEMORY = (SPARK_WORKER_NODE_PHYSICAL_MEMORY / MAX_NUMBER_OF_LOCAL_RAY_WORKER_NODES) * 0.8
```

Where:

- `SPARK_WORKER_NODE_PHYSICAL_MEMORY` is the total physical RAM of the Spark worker node.
- `MAX_NUMBER_OF_LOCAL_RAY_WORKER_NODES` is the maximum number of Ray worker nodes that can be launched on that Spark worker node. This value is determined by the `num_cpus_per_node` or `num_gpus_per_node` argument passed to `setup_ray_cluster`.
- The factor `0.8` reserves 20% of the available memory for non-Ray processes (e.g., the operating system, Spark executor overhead).

## Default Heap and Object Store Memory Split

If the `object_store_memory_per_node` argument is **not** explicitly set, the total memory is split into heap memory and object store memory using a 70/30 ratio: ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

```
RAY_WORKER_NODE_HEAP_MEMORY      = RAY_WORKER_NODE_TOTAL_MEMORY * 0.7
OBJECT_STORE_MEMORY_PER_NODE     = RAY_WORKER_NODE_TOTAL_MEMORY * 0.3
```

Heap memory is used for executing Ray tasks and storing actor state, while object store memory (backed by Apache Arrow’s plasma store) is used for passing large objects between tasks and managing distributed references.

## Custom Object Store Memory

If the user provides a value for `object_store_memory_per_node`, the heap memory is recomputed to use the remaining portion of total memory: ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

```
RAY_WORKER_NODE_HEAP_MEMORY = RAY_WORKER_NODE_TOTAL_MEMORY - argument_object_store_memory_per_node
```

In this case, the object store memory is set exactly to the user‑specified value, and the heap memory adjusts accordingly.

## Shared Memory Cap

The object store memory per Ray worker node is ultimately capped by the operating system’s shared memory size (`/dev/shm`). The maximum possible object store memory is: ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

```
OBJECT_STORE_MEMORY_PER_NODE_CAP = (SPARK_WORKER_NODE_OS_SHARED_MEMORY / MAX_NUMBER_OF_LOCAL_RAY_WORKER_NODES) * 0.8
```

`SPARK_WORKER_NODE_OS_SHARED_MEMORY` is the size of the `/dev/shm` filesystem on the Spark worker node. The factor `0.8` again reserves overhead for the operating system. If the calculated object store memory exceeds this cap, it will be clamped to the cap value.

## Best Practices

### Reduce Spark Executor Memory for Hybrid Workloads

When running hybrid Apache Spark and Ray workloads on the same cluster, it is recommended to reduce `spark.executor.memory` to a small value (e.g., `4g`). The Spark executor JVM tends to hold onto memory lazily, and the Spark dataset cache can consume significant memory, leaving less room for Ray. Reducing the Spark executor memory helps avoid out-of-memory errors on the worker node. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

### Set CPU Cores per Node to Match the Spark Worker

To maximize resource utilization, set `num_cpus_per_node` (or `num_gpus_per_node`) to the total number of CPU cores (or GPUs) available on the Spark worker node. This ensures that only one Ray worker node runs per Spark worker, consuming all of the latter’s resources. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

### Disable Memory Monitoring Refresh

Set the environment variable `RAY_memory_monitor_refresh_ms` to `0` in the Databricks cluster configuration to disable periodic memory monitoring and reduce overhead. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Ray on Databricks](/concepts/ray-on-databricks.md) – Overview of Ray cluster integration with Databricks.
- Ray Cluster Autoscaling – Configuring the dynamic scale‑up/down of Ray worker nodes.
- Ray Head Node Configuration – Resource allocation for the Ray head node (typically 0 CPU, 0 GPU).
- [Heterogeneous Ray Clusters](/concepts/heterogeneous-ray-clusters-on-databricks.md) – Using different instance types for head and workers via cluster policies.
- Spark Executor Memory Tuning – Adjusting Spark memory settings to coexist with Ray.
- Object Store Memory in Ray – Detailed behavior of shared memory and plasma store.

## Sources

- scale-ray-clusters-on-databricks-databricks-on-aws.md

# Citations

1. [scale-ray-clusters-on-databricks-databricks-on-aws.md](/references/scale-ray-clusters-on-databricks-databricks-on-aws-ad8172f6.md)
