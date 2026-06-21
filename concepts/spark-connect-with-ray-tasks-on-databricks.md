---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8238d54c30efc9cee8f27cbb5f5bb7822e1c15e61b2966da849c370a886980ec
  pageDirectory: concepts
  sources:
    - combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spark-connect-with-ray-tasks-on-databricks
    - SCWRTOD
  citations:
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
title: Spark Connect with Ray Tasks on Databricks
description: Use DatabricksSession and Spark Connect to enable Ray Core tasks to directly interact with a Spark cluster from worker nodes, though tasks become sequential due to a threading lock on the single Spark driver.
tags:
  - ray
  - spark-connect
  - databricks
  - distributed-computing
timestamp: "2026-06-18T11:01:15.433Z"
---

# Spark Connect with Ray Tasks on Databricks

**Spark Connect with Ray Tasks on Databricks** is a pattern that allows Ray Core tasks running on a Databricks cluster to directly interact with Spark using Spark Connect. Instead of persisting data to temporary storage, Ray tasks can create a Spark session that points to the existing Spark cluster on the driver node, enabling seamless data exchange between Ray and Spark within the same execution environment.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Setup

To use Spark Connect inside a Ray task, you must configure Ray cluster resources to allocate space for Spark. For example, if a worker node has 8 CPUs, set `num_cpus_worker_node` to 7, leaving one CPU for Spark. For larger Spark tasks, allocate a larger share of resources.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

Within the Ray task, you create a Spark session using `DatabricksSession.builder.remote()` with the workspace host URL, an access token, and the cluster ID. The cluster ID and host URL can be retrieved from the notebook context, and the access token can be obtained from the notebook’s API token (for testing) or from [Databricks secrets](/concepts/databricks-secret-scopes.md) (recommended for production).^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Example

The following example defines a Ray remote class that creates a Spark session and runs a Spark SQL query, writing the result to a Delta table:^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

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
        df.write.format("delta").mode("overwrite").saveAsTable("catalog.schema.taxi_trips")
        return df.count()

access_token = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()
cluster_id = dbutils.notebook.entry_point.getDbutils().notebook().getContext().clusterId().get()
host_url = f"https://{dbutils.notebook.entry_point.getDbutils().notebook().getContext().tags().get('browserHostName').get()}"

sh = SparkHandler.remote(access_token=access_token,
                         cluster_id=cluster_id,
                         host_url=host_url)
print(ray.get(sh.test.remote()))
```

## Considerations

Because Spark Connect connects all Ray tasks to a single Spark driver, a threading lock is created. This causes all Ray tasks to wait for preceding Spark tasks to complete. For workloads with many concurrent Ray tasks, the sequential behavior of Spark operations can become a bottleneck. In such situations, Databricks recommends the alternative pattern of persisting output to temporary storage (e.g., Unity Catalog volumes or DBFS) and then consolidating all data into a single [Spark DataFrame](/concepts/spark-dataframe-evaluation-pattern.md) at the end before writing to the output table.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Security

The example above uses a notebook-generated token, which is suitable for development. For production use cases, store the access token in [Databricks secrets](/concepts/databricks-secret-scopes.md) and retrieve it inside the Ray task to avoid hard‑coding credentials.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Related Concepts

- Ray – Distributed computing framework for AI and Python workloads
- [Spark Connect](/concepts/spark-connect.md) – Decoupled client‑server architecture for Apache Spark
- [DatabricksSession](/concepts/databrickssession.md) – Session builder for connecting to Databricks clusters
- [Unity Catalog](/concepts/unity-catalog.md) – Centralised governance layer for data and AI assets
- [Delta Lake](/concepts/delta-lake.md) – Storage layer that brings ACID transactions to Spark
- [Databricks secrets](/concepts/databricks-secret-scopes.md) – Secure service for storing API keys and credentials
- Ray Core – Lower‑level APIs for building distributed applications

## Sources

- combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

# Citations

1. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
