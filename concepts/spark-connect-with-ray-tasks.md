---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3183f51bdbd3dd6924ae3ed0637943540bbc25ba22d164a630c4995c63f8dfe3
  pageDirectory: concepts
  sources:
    - combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spark-connect-with-ray-tasks
    - SCWRT
  citations:
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
title: Spark Connect with Ray Tasks
description: Using Databricks Connect (Spark Connect) to allow Ray Core tasks to directly interact with a Spark cluster from within remote Ray tasks, with considerations for threading locks and resource allocation.
tags:
  - ray
  - spark-connect
  - databricks
  - distributed-computing
timestamp: "2026-06-19T14:17:51.610Z"
---

# Spark Connect with Ray Tasks

**Spark Connect with Ray Tasks** is a pattern for integrating Ray Core applications with Apache Spark within the same Databricks environment. It enables Ray tasks running on worker nodes to directly interact with a Spark cluster by establishing a Spark Connect session from within the remote task, allowing data to be written to Spark tables without intermediate storage.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Overview

When running both Ray and Spark workloads in the same execution environment, Ray Core tasks sometimes need to write output data directly to Spark tables or DataFrames. While the simplest approach is to persist Ray output to a temporary location like DBFS or Unity Catalog Volumes and then read it with Spark, this pattern introduces storage latency and management overhead. Spark Connect provides an alternative that allows Ray tasks to communicate directly with the Spark driver.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## How It Works

Spark Connect enables a remote client to connect to a Spark cluster using a lightweight gRPC protocol. By using the [Databricks Connect](/concepts/databricks-connect.md) SDK (`databricks.connect`) inside a Ray remote task or actor, you can create a `DatabricksSession` that points to the same Spark cluster running from the driver node. This session then behaves like a standard Spark session, capable of running SQL queries, reading DataFrames, and writing to Delta tables.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Implementation

### Setting Up the Spark Handler Actor

A common implementation pattern is to define a Ray actor that holds a Spark Connect session and exposes methods for Spark operations:^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]
import ray

@ray.remote
class SparkHandler(object):
    def __init__(self, access_token=None, cluster_id=None, host_url=None):
        self.spark = (
            [[databrickssession|DatabricksSession]]
            .builder
            .remote(host=host_url,
                    token=access_token,
                    cluster_id=cluster_id)
            .getOrCreate()
        )

    def test(self):
        df = self.spark.sql("select * from samples.nyctaxi.trips")
        df.write.format("delta").mode("overwrite").saveAsTable(
            "catalog.schema.taxi_trips"
        )
        return df.count()
```

### Passing Authentication and Cluster Metadata

The Ray actor needs authentication credentials and cluster identifiers to establish the Spark Connect session. These can be obtained from the notebook context:^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
access_token = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()
cluster_id = dbutils.notebook.entry_point.getDbutils().notebook().getContext().clusterId().get()
host_url = f"https://{dbutils.notebook.entry_point.getDbutils().notebook().getContext().tags().get('browserHostName').get()}"

sh = SparkHandler.remote(
    access_token=access_token,
    cluster_id=cluster_id,
    host_url=host_url
)

print(ray.get(sh.test.remote()))
```

### Access Token Management

The example above uses the notebook-generated token for simplicity. For production use cases, Databricks recommends storing access tokens in Databricks Secrets rather than embedding them in code or passing them through notebook contexts.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Resource Allocation Considerations

To use Spark Connect within Ray tasks, you must configure Ray cluster resources to allocate space for the Spark session. For example, if a worker node has 8 CPUs, set `num_cpus_worker_node` to 7, leaving 1 CPU for Spark. For larger Spark tasks, allocate a larger share of resources to avoid contention.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Performance Characteristics

Spark Connect calls from multiple Ray tasks all route through a single Spark driver. This creates a **threading lock** — each Ray task that invokes a Spark operation waits for preceding Spark tasks to complete before proceeding. Consequently, concurrent Ray tasks experience sequential execution for their Spark operations.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### When to Use

- **Low concurrency:** Suitable when the number of concurrent Ray tasks making Spark calls is small.
- **Direct table writes:** Recommended when Ray tasks need to write results directly to Delta tables without intermediate file storage.

### When to Avoid

- **High concurrency:** If many Ray tasks need to write to Spark simultaneously, the threading lock creates a bottleneck. In these situations, prefer Pattern 1: Persist output in a temporary location, which writes Ray outputs to DBFS or Unity Catalog Volumes and then consolidates them into a single Spark DataFrame at the end.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Integration with Delta Lake and Unity Catalog

When writing to Delta tables via Spark Connect, the data is immediately available in the Unity Catalog [Metastore](/concepts/metastore.md). This contrasts with third-party libraries like `deltalake` which currently only support Hive [Metastore](/concepts/metastore.md) tables and cannot write directly to Unity Catalog tables.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Limitations

- Spark Connect from Ray tasks uses a single Spark driver connection, creating a serialization bottleneck for concurrent operations.
- All Spark operations go through a single thread — Ray tasks making concurrent Spark calls will block on each other.
- For Unity Catalog writes from Ray, Spark Connect is one of only two supported approaches (the other being persisting to storage then reading with Spark). Unity Catalog currently does not share credentials for direct writes from non-Spark writers.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Related Concepts

- Ray Core — Low-level Ray API used for distributed task execution
- [Databricks Connect](/concepts/databricks-connect.md) — SDK that enables remote Spark session connections
- [Ray and Spark Integration](/concepts/ray-and-spark-integration-on-databricks.md) — The broader framework for combining Ray and Spark workloads
- Unity Catalog Volumes — Storage location for persisting Ray output when not using Spark Connect
- [Delta Lake](/concepts/delta-lake.md) — Storage format used for tables written through Spark Connect

## Sources

- combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

# Citations

1. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
