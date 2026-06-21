---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 940d4a3e5debe488eb48218d095c7b18b08a3edafa134033146ca6fc9c54ec89
  pageDirectory: concepts
  sources:
    - combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-spark-resource-allocation-best-practices-on-databricks
    - RRABPOD
  citations:
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
title: Ray-Spark Resource Allocation Best Practices on Databricks
description: Configure Ray worker nodes to match Spark worker node resources by setting num_cpus_worker_node and num_gpus_worker_node appropriately, ensuring one Ray worker per Spark worker for full resource utilization.
tags:
  - ray
  - spark
  - resource-allocation
  - best-practices
timestamp: "2026-06-18T11:01:49.161Z"
---

## Ray-Spark Resource Allocation Best Practices on Databricks

Running Ray and Apache Spark in the same Databricks execution environment lets teams leverage the strengths of both distributed computing engines. Effective resource allocation is critical to avoid contention and ensure that both frameworks can operate efficiently. This page outlines best practices for configuring CPU, GPU, and memory resources when integrating Ray with Spark on Databricks.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### Cluster Configuration for Mixed Workloads

The most fundamental practice is to align the Ray worker node resource counts with those of the Spark worker node. Each Spark worker node should launch one Ray worker node that fully utilizes the same resources. To achieve this:

- Set `num_cpus_worker_node` to match the number of CPU cores on the Spark worker node.
- Set `num_gpus_worker_node` to match the number of GPUs on the Spark worker node.

This one-to-one mapping avoids resource fragmentation and ensures that Ray tasks can access the full capacity of the underlying hardware.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### Allocating Resources for Spark Connect

When using [Spark Connect](/concepts/spark-connect.md) from within a Ray Core task, you must configure the Ray cluster to reserve a portion of the node’s resources for the Spark driver. Because Spark Connect spawns a separate process on the Ray worker node, leaving no room for it can cause resource starvation. For example, if a worker node has 8 CPUs, set `num_cpus_worker_node` to 7 and leave 1 CPU free for Spark. For larger Spark tasks, allocate a proportionally larger share.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

Note that the Spark Connect approach funnels all Ray tasks through a single Spark driver, creating a threading lock. Consequently, concurrent tasks will complete sequentially as each waits for the preceding Spark task to finish. This pattern is therefore best suited for scenarios with few concurrent Ray tasks. For high concurrency, persist intermediate data to a temporary location and consolidate into a Spark DataFrame afterward.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### Autoscaling Considerations for Data Transfers

When transferring data from Spark to Ray using `ray.data.from_spark()`, autoscaling Spark clusters (including those using spot instances) **must** set the `use_spark_chunk_api` parameter to `False`. Failure to do so results in cache misses because the executor cache is lost when an executor terminates during scale-down. This applies to Databricks Runtime ML 15.0 and above, where in-memory Spark-to-Ray transfers are supported.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### Handling Large Outputs from Ray Core

When the output of a Ray Core task is too large to fit in the memory of the driver node or the shared object store, avoid holding all results in memory. Instead, persist each task’s output to temporary storage (such as Unity Catalog Volumes or DBFS) and then read the consolidated files into a Spark DataFrame. This pattern is the most common for writing data from Ray to Spark and works well with tabular outputs like Pandas DataFrames.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### Using Unity Catalog Volumes for Governance

For non-tabular output data, consider storing it in Unity Catalog Volumes. This provides governance, lineage tracking, and secure access while keeping data accessible to both Ray and Spark. Volumes are especially useful when the intermediate data does not need to be written to a Delta table immediately.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### Limitations That Affect Resource Planning

Unity Catalog currently does not share write credentials to non-Spark writers. Therefore, any Ray Core task that writes to a Unity Catalog table must use one of two workarounds:

- Persist the data to a temporary location, then read it with Spark and write to the Unity Catalog table.
- Set up [Databricks Connect](/concepts/databricks-connect.md) within the Ray task so that Spark can perform the write.

Both approaches require additional resource planning — the temporary‑storage path incurs I/O overhead, while Spark Connect consumes driver resources on the Ray worker node as described above.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### General Recommendations

- Always follow the techniques in the official Ray cluster best practices guide (external) to ensure the cluster is fully utilized.
- When writing data from Ray Core to Spark via temporary files, use an in‑node scratch directory (e.g., a mounted volume) rather than network storage to reduce latency.
- For workloads that involve both high‑throughput data processing and low‑latency inference, consider splitting the cluster into separate pools for Spark and Ray to avoid resource contention — but if co‑location is required, the resource‑alignment rules above should be carefully applied.

## Related Concepts

- [Ray on Databricks](/concepts/ray-on-databricks.md)
- Spark on Databricks
- [Unity Catalog](/concepts/unity-catalog.md)
- Unity Catalog Volumes
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md)
- [Spark Connect](/concepts/spark-connect.md)
- [Databricks Connect](/concepts/databricks-connect.md)
- [Delta Lake](/concepts/delta-lake.md)

## Sources

- combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

# Citations

1. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
