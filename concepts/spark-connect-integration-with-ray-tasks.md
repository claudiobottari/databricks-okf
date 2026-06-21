---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3757b93ebfe6cc027c7475d22da8c9e801519bdf161eb19726c66117cbccbcc3
  pageDirectory: concepts
  sources:
    - combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - spark-connect-integration-with-ray-tasks
    - SCIWRT
  citations:
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
title: Spark Connect Integration with Ray Tasks
description: Using DatabricksSession and Spark Connect within Ray remote tasks to directly interact with Spark DataFrames and tables from Ray workers
tags:
  - ray
  - spark-connect
  - databricks
  - remote-tasks
timestamp: "2026-06-19T09:17:46.999Z"
---

---
title: Spark Connect Integration with Ray Tasks
summary: How to use Spark Connect within Ray Core tasks to interact with Spark clusters, enabling direct DataFrame operations from Ray workers.
sources:
  - combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:13:02.271Z"
updatedAt: "2026-06-18T11:13:02.271Z"
tags:
  - ray
  - spark
  - spark-connect
  - databricks
  - distributed-computing
aliases:
  - spark-connect-integration-with-ray-tasks
  - SCIRWT
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Spark Connect Integration with Ray Tasks

**Spark Connect Integration with Ray Tasks** refers to the ability to use [Spark Connect](/concepts/spark-connect.md) within Ray Core remote tasks to directly connect to a running Spark cluster. This allows Ray tasks to read from and write to Spark DataFrames and tables without persisting data to intermediate storage, enabling tight coupling between the two distributed computing frameworks in a single Databricks environment.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Overview

Databricks supports combining Ray and Spark in the same execution environment. [Spark Connect](/concepts/spark-connect.md) provides a decoupled client-server architecture for Spark that can be used from Ray Core tasks. By setting up a Spark Connect client inside a Ray remote task, the task can execute Spark SQL queries, read DataFrames from Unity Catalog tables, and write results back to Delta tables. This pattern is one of three approaches for writing data from Ray Core to Spark (the others being persisting to temporary storage and using third-party libraries).^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## How It Works

The integration uses the `DatabricksSession` builder from the [Databricks Connect](/concepts/databricks-connect.md) library (`databricks.connect`). Inside a Ray remote task, a `DatabricksSession` is created with the `remote()` method, specifying the workspace host URL, a personal access token, and the cluster ID. This session communicates with the Spark cluster running on the driver node of the Databricks cluster.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

Because each Ray task creates its own Spark Connect session, all tasks share the same Spark driver. This creates a threading lock on the driver, causing tasks to execute sequentially — each task waits for the preceding Spark operation to complete before proceeding. For workloads with many concurrent Ray tasks, sequential execution may become a bottleneck.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Example

The following example defines a Ray remote actor (`SparkHandler`) that opens a Spark Connect session, runs a SQL query, writes the result to a Delta table, and returns the row count:^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

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

### Token Management

The example above uses a notebook-generated token (`dbutils.notebook.entry_point.getDbutils()...`). For production use cases, Databricks recommends storing the access token in Databricks Secrets and retrieving it securely rather than embedding it in code.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Resource Configuration

To use Spark Connect inside Ray tasks, the Ray cluster must be configured to reserve resources for Spark. For instance, if a worker node has 8 CPUs, the `num_cpus_worker_node` should be set to 7, leaving 1 CPU for the Spark Connect client or other Spark processes. For larger Spark tasks, a larger share of resources should be allocated.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Best Practices

- Use Databricks Secrets for access tokens instead of notebook-generated tokens in production.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]
- Limit the number of concurrent Ray tasks that use Spark Connect, because all tasks share a single Spark driver and will execute sequentially.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]
- For workloads with many concurrent tasks, consider persisting Ray task outputs to temporary storage (such as Unity Catalog Volumes or DBFS) and then consolidating into a single Spark DataFrame at the end, rather than using Spark Connect inside each task.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Limitations

- **Sequential execution**: All Ray tasks using Spark Connect share the same Spark driver on the driver node, creating a threading lock. Tasks wait for preceding Spark operations to finish, so concurrency is limited.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]
- **Resource contention**: If CPU resources are not properly allocated between Ray and Spark, performance may degrade.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]
- **Not suited for high concurrency**: The sequential behavior makes this pattern better suited for workloads with a small number of tasks.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Combine Ray and Spark on Databricks](/concepts/ray-and-spark-integration-on-databricks.md) — Overview of all integration patterns
- Ray Core — Low-level Ray API for distributed task and actor programming
- [Spark Connect](/concepts/spark-connect.md) — Decoupled client-server Spark architecture
- [Databricks Connect](/concepts/databricks-connect.md) — Library for connecting to Databricks clusters from external applications
- [Spark DataFrames](/concepts/saving-spark-dataframes-to-tfrecords.md) — The primary data structure used in Spark
- [Delta Lake](/concepts/delta-lake.md) — Storage layer for Spark with ACID transactions
- [Unity Catalog](/concepts/unity-catalog.md) — Data governance solution for Databricks
- Databricks Secrets — Secure storage for API tokens and credentials

## Sources

- combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

# Citations

1. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
