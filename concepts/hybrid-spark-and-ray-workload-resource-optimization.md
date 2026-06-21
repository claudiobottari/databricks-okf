---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 017f750f147cef1421140e772add751dba7dfc2bb88e3ee65eda3c73fe493a3e
  pageDirectory: concepts
  sources:
    - scale-ray-clusters-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - hybrid-spark-and-ray-workload-resource-optimization
    - Ray Workload Resource Optimization and Hybrid Spark
    - HSARWRO
  citations:
    - file: scale-ray-clusters-on-databricks-databricks-on-aws.md
title: Hybrid Spark and Ray Workload Resource Optimization
description: Best practices for running concurrent Spark and Ray workloads on Databricks, including reducing Spark executor memory to avoid OOM errors and enabling Ray-on-Spark autoscaling to dynamically share cluster resources.
tags:
  - ray
  - spark
  - databricks
  - hybrid-workloads
  - optimization
timestamp: "2026-06-19T20:18:48.786Z"
---

# Hybrid Spark and Ray Workload Resource Optimization

When running hybrid workloads that combine Apache Spark and Ray in a single Databricks cluster, careful resource configuration is required to avoid memory pressure, out‑of‑memory errors, and sub‑optimal throughput. The two engines share the same worker nodes, and without tuning they can compete for memory and compute resources.

## Memory Resource Configuration

The Apache Spark executor is a Java process that triggers garbage collection lazily, and the Spark dataset cache can consume a large amount of executor memory. This reduces the memory available for Ray. To avoid Out of Memory Errors in hybrid clusters, Databricks recommends reducing `spark.executor.memory` to a small value — for example, `4g` — in the cluster configuration. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

## Compute Resource Configuration

For computation resources, the recommendation is to make **either** the underlying cluster nodes **or** the Ray worker nodes auto‑scalable. The goal is to allow one engine to release resources when idle so the other engine can use them.

- **Fixed‑size Databricks cluster, auto‑scaling Ray cluster**: If you have a fixed number of worker nodes available, enable Ray on Spark autoscaling. When no Ray workloads are running, the Ray cluster scales down, freeing resources for Apache Spark tasks. When Spark tasks finish and Ray is needed again, the Ray cluster scales back up. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

- **Both clusters auto‑scalable**: You can also make both the Databricks cluster and the Ray‑on‑Spark cluster auto‑scalable. For example, configure the Databricks cluster to a maximum of 10 nodes and the Ray‑on‑Spark worker nodes to a maximum of 4 nodes, with each Ray worker node fully utilizing the resources of one Spark worker. Under this setup, Ray workloads can use at most 4 nodes, while Spark jobs can allocate the remaining 6 nodes. ^[scale-ray-clusters-on-databricks-databricks-on-aws.md]

## Best Practices Summary

- Reduce Spark executor memory (`spark.executor.memory`) to a small value (e.g., `4g`) to leave more memory for Ray.
- Ensure that at least one of the two layers (cluster nodes or Ray workers) is auto‑scalable so compute resources are dynamically shared.
- When using [Ray on Spark Autoscaling](/concepts/ray-on-databricks-autoscaling.md), set `min_worker_nodes` and `max_worker_nodes` appropriately to control the range of Ray workers.

## Related Concepts

- Ray on Spark
- Ray Cluster Autoscaling
- Apache Spark Configuration
- Out of Memory Errors
- Databricks Cluster Autoscaling
- Heterogeneous Clusters on Databricks

## Sources

- scale-ray-clusters-on-databricks-databricks-on-aws.md

# Citations

1. [scale-ray-clusters-on-databricks-databricks-on-aws.md](/references/scale-ray-clusters-on-databricks-databricks-on-aws-ad8172f6.md)
