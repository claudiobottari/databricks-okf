---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5b504c23cee53ffe4b34b0a92826af39b7db851a66283fca54fcd2572ae7bfae
  pageDirectory: concepts
  sources:
    - combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - ray-cluster-resource-configuration-for-spark
    - RCRCFS
  citations:
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
    - file: |-
        combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

        ### GPU Allocation

        Set `num_gpus_worker_node` equal to the number of GPUs per Spark worker node. This ensures that the single Ray worker launched per Spark worker node can fully utilize the GPU resources of that node. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

        ### One Ray Worker per Spark Worker Node

        In this configuration
    - file: each Spark worker node launches exactly one Ray worker node
    - file: |-
        and that Ray worker uses the full CPU and GPU capacity of the Spark worker node (minus the Spark reservation). This model avoids resource contention by keeping the mapping simple and predictable. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

        ## Autoscaling Considerations

        When autoscaling Spark clusters (including those using spot instances) are used with `ray.data.from_spark()`
    - file: the `use_spark_chunk_api` parameter **must** be set to `False`. Otherwise
    - file: cache misses occur because the cache on a terminated Spark executor is lost when the executor is decommissioned. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
    - file: |-
        combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

        ## Best Practices

        - Always apply the resource configuration guidelines above to ensure the cluster is fully utilized. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
        - For non‑tabular data
    - file: consider using [[Unity Catalog
    - file: |-
        combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
        - When possible
    - file: use the techniques described in the Ray cluster best practice guide (see [[Ray Cluster Scaling Best Practices|Ray cluster best practices
    - file: |-
        combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

        ## Limitations

        Unity Catalog does not share credentials for writing to tables from non‑Spark writers. Consequently
    - file: data written from a Ray Core task to a Unity Catalog table must first be persisted and then read with Spark
    - file: |-
        or Spark Connect must be set up within the Ray task. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

        ## Related Concepts

        - Ray
        - Apache Spark
        - [[Databricks Runtime ML
title: Ray Cluster Resource Configuration for Spark
description: Best practices for configuring CPU and GPU allocations when running Ray and Spark together on shared worker nodes, including num_cpus_worker_node and num_gpus_worker_node settings.
tags:
  - ray
  - spark
  - cluster-configuration
  - resource-management
timestamp: "2026-06-18T14:39:48.981Z"
---

# Ray Cluster Resource Configuration for Spark

When running Ray and Spark in the same execution environment on Databricks, you must explicitly configure Ray cluster resources so that both frameworks can coexist without starving each other. This page covers the key resource allocation parameters and best practices for co-locating Ray workers with Spark executors. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Overview

The most common pattern for integrating Ray Core tasks with Spark is to use [Spark Connect](/concepts/spark-connect.md) inside Ray remote tasks. In this setup, Ray workers need to share the underlying node resources with the Spark driver or executor processes. If Ray consumes all available CPUs or GPUs, Spark tasks may be unable to run, leading to hangs or failures. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Key Configuration Parameters

Two critical parameters control resource allocation per Ray worker node:

| Parameter | Purpose | Recommendation |
|-----------|---------|----------------|
| `num_cpus_worker_node` | Number of CPUs allocated to the Ray worker | Set to the number of CPU cores on the Spark worker node, minus a reservation for Spark. |
| `num_gpus_worker_node` | Number of GPUs allocated to the Ray worker | Set to the number of GPUs per Spark worker node. |

^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Resource Allocation Recommendations

### CPU Allocation

The `num_cpus_worker_node` value should reflect the CPU capacity of the Spark worker node *after* reserving resources for Spark itself. For example, if a worker node has 8 CPUs, set `num_cpus_worker_node` to 7, leaving 1 CPU for the Spark executor. For larger Spark tasks, Databricks recommends allocating a larger share of resources to Spark. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

### GPU Allocation

Set `num_gpus_worker_node` equal to the number of GPUs per Spark worker node. This ensures that the single Ray worker launched per Spark worker node can fully utilize the GPU resources of that node. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

### One Ray Worker per Spark Worker Node

In this configuration, each Spark worker node launches exactly one Ray worker node, and that Ray worker uses the full CPU and GPU capacity of the Spark worker node (minus the Spark reservation). This model avoids resource contention by keeping the mapping simple and predictable. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

## Autoscaling Considerations

When autoscaling Spark clusters (including those using spot instances) are used with `ray.data.from_spark()`, the `use_spark_chunk_api` parameter **must** be set to `False`. Otherwise, cache misses occur because the cache on a terminated Spark executor is lost when the executor is decommissioned. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
ray_ds = ray.data.from_spark(df, use_spark_chunk_api=False)
```

## Using Spark Connect with Resource Configuration

When Ray Core tasks communicate with Spark via Spark Connect, they call a single Spark driver, which creates a *threading lock*. All concurrent Ray tasks must wait for the preceding Spark task to complete. Therefore, this pattern is best suited for workloads with a small number of concurrent tasks; for high concurrency, it is more efficient to persist output data to a temporary location and then read it with Spark. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

## Best Practices

- Always apply the resource configuration guidelines above to ensure the cluster is fully utilized. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
- For non‑tabular data, consider using [Unity Catalog](/concepts/unity-catalog.md) volumes to store output and provide governance. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
- When possible, use the techniques described in the Ray cluster best practice guide (see [Ray cluster best practices](/concepts/ray-cluster-scaling-best-practices.md)). ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

## Limitations

Unity Catalog does not share credentials for writing to tables from non‑Spark writers. Consequently, data written from a Ray Core task to a Unity Catalog table must first be persisted and then read with Spark, or Spark Connect must be set up within the Ray task. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

## Related Concepts

- Ray
- Apache Spark
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md)
- [Spark Connect](/concepts/spark-connect.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- Autoscaling on Databricks

## Sources

- combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

# Citations

1. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
2. combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

### GPU Allocation

Set `num_gpus_worker_node` equal to the number of GPUs per Spark worker node. This ensures that the single Ray worker launched per Spark worker node can fully utilize the GPU resources of that node. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

### One Ray Worker per Spark Worker Node

In this configuration
3. each Spark worker node launches exactly one Ray worker node
4. and that Ray worker uses the full CPU and GPU capacity of the Spark worker node (minus the Spark reservation). This model avoids resource contention by keeping the mapping simple and predictable. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

## Autoscaling Considerations

When autoscaling Spark clusters (including those using spot instances) are used with `ray.data.from_spark()`
5. the `use_spark_chunk_api` parameter **must** be set to `False`. Otherwise
6. cache misses occur because the cache on a terminated Spark executor is lost when the executor is decommissioned. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
7. combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

## Best Practices

- Always apply the resource configuration guidelines above to ensure the cluster is fully utilized. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
- For non‑tabular data
8. consider using [[Unity Catalog
9. combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
- When possible
10. use the techniques described in the Ray cluster best practice guide (see [[Ray Cluster Scaling Best Practices|Ray cluster best practices
11. combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

## Limitations

Unity Catalog does not share credentials for writing to tables from non‑Spark writers. Consequently
12. data written from a Ray Core task to a Unity Catalog table must first be persisted and then read with Spark
13. or Spark Connect must be set up within the Ray task. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

## Related Concepts

- Ray
- Apache Spark
- [[Databricks Runtime ML
