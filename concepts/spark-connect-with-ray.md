---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b856303ef3b61c86ddc796b7cf2f3f9d0857ce73efcce2dafd03628ff0b76ad3
  pageDirectory: concepts
  sources:
    - combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spark-connect-with-ray
    - SCWR
  citations:
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
title: Spark Connect with Ray
description: Using Spark Connect from within Ray remote tasks to allow Ray workers to interact directly with a Spark cluster running on the driver node.
tags:
  - databricks
  - ray
  - spark-connect
  - distributed-computing
timestamp: "2026-06-19T17:46:49.750Z"
---

# Spark Connect with Ray

**Spark Connect with Ray** is a pattern for integrating Ray Core tasks with Apache Spark by using [Spark Connect](/concepts/spark-connect.md) to establish a direct connection between a Ray remote task and a Spark cluster running on the driver node. This allows Ray tasks to read from and write to Spark DataFrames and tables without persisting intermediate data to disk. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Overview

Within a Databricks environment that runs both Ray and Spark, Ray Core tasks can use Spark Connect to create a Spark session that points to the existing Spark cluster. The Ray worker task then interacts with Spark exactly as a normal Spark application would — executing SQL queries, reading DataFrames, or writing to Delta tables — all inside the Ray remote function or class. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

This approach is one of three patterns for writing data from Ray to Spark. The other patterns are persisting output to a temporary location (e.g., Unity Catalog volumes or DBFS) and using third-party libraries such as `deltalake` or `deltaray`. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Configuration

To use Spark Connect inside a Ray task, you must configure the Ray cluster resources so that each Ray worker node reserves enough CPU capacity for the Spark Connect client. For example, if a worker node has 8 CPUs, set `num_cpus_worker_node` to 7, leaving 1 CPU for the Spark Connect process. For larger Spark tasks, allocate a larger share of resources. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Example

The following code creates a Ray remote class that opens a Spark session via [Databricks Connect](/concepts/databricks-connect.md) and runs a Spark SQL query. It then writes the result to a Unity Catalog table. The authentication uses a notebook‑generated token; production use cases should store the token in Databricks secrets. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]
import ray

@ray.remote
class SparkHandler(object):
    def __init__(self, access_token=None, cluster_id=None, host_url=None):
        self.spark = ([[databrickssession|DatabricksSession]]
                      .builder
                      .remote(host=host_url,
                              token=access_token,
                              cluster_id=cluster_id)
                      .getOrCreate()
                      )

    def test(self):
        df = self.spark.sql("select * from samples.nyctaxi.trips")
        df.write.format("delta").mode("overwrite").saveAsTable(
            "catalog.schema.taxi_trips")
        return df.count()

access_token = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()
cluster_id = dbutils.notebook.entry_point.getDbutils().notebook().getContext().clusterId().get()
host_url = f"https://{dbutils.notebook.entry_point.getDbutils().notebook().getContext().tags().get('browserHostName').get()}"

sh = SparkHandler.remote(access_token=access_token,
                         cluster_id=cluster_id,
                         host_url=host_url)
print(ray.get(sh.test.remote()))
```

^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Best Practices

- Use a dedicated access token stored in Databricks Secrets for production workloads, rather than the notebook‑generated token. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]
- Set `num_cpus_worker_node` and `num_gpus_worker_node` to match the resources of the Spark worker node so that each Spark worker node launches one Ray worker node that fully utilizes the underlying hardware. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]
- Because Spark Connect creates a single Spark driver connection, all Ray tasks that use it will be serialized — each task must wait for the preceding Spark task to finish. Therefore, this pattern is recommended only when there are few concurrent tasks. For high‑concurrency scenarios, persist Ray task outputs and then combine them into a single Spark DataFrame at the end. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Limitations

- Spark Connect introduces a threading lock on the single Spark driver connection, causing all Ray tasks to execute sequentially with respect to Spark operations. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]
- [Unity Catalog](/concepts/unity-catalog.md) currently does not share credentials for writing to tables from non‑Spark writers. Therefore, writing data from a Ray Core task directly to a Unity Catalog table via Spark Connect requires that the data be persisted and then read with Spark, or that Databricks Connect is set up inside the Ray task (as shown in the example). ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Combine Ray and Spark in the same environment on Databricks](/concepts/ray-and-spark-integration-on-databricks.md) — Overview of all integration patterns.
- Ray Core — Lower‑level Ray API for building distributed applications.
- [Spark Connect](/concepts/spark-connect.md) — The Apache Spark protocol that decouples the client from the cluster.
- [Databricks Connect](/concepts/databricks-connect.md) — The Databricks client library that uses Spark Connect.
- [Unity Catalog](/concepts/unity-catalog.md) — Centralized data governance catalog on Databricks.
- [Delta Lake](/concepts/delta-lake.md) — Storage layer used by Spark tables.
- [deltalake library](/concepts/delta-lake.md) — Third‑party library for writing Delta tables from Ray (not officially supported).
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — Pre‑built runtime that includes both Ray and Spark.

## Sources

- combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

# Citations

1. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
