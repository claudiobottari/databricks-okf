---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 893afd35f34a61994be0a443b8e154479fdf96cd91fb4efa1913a4c53983b5e1
  pageDirectory: concepts
  sources:
    - combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-to-unity-catalog-table-writing
    - RTUCTW
  citations:
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
title: Ray to Unity Catalog Table Writing
description: Writing Ray datasets directly to Unity Catalog tables using ray.data.Dataset.write_databricks_table() via Unity Catalog Volumes as an intermediary
tags:
  - ray
  - unity-catalog
  - databricks
  - data-writing
timestamp: "2026-06-19T09:17:15.153Z"
---

# Ray to Unity Catalog Table Writing

**Ray to Unity Catalog Table Writing** refers to the methods and patterns for writing data from Ray applications—including Ray Data and Ray Core—to tables managed by [Unity Catalog](/concepts/unity-catalog.md) on Databricks. Because Unity Catalog does not share credentials for writing to tables from non-Spark writers, writing from Ray to Unity Catalog tables requires an intermediate step using Spark.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Overview

Writing data from Ray to Unity Catalog tables is a common need when combining the strengths of both distributed computing engines. Ray excels at machine learning and deep learning workloads, while Spark provides robust data management through Unity Catalog with secure access and lineage tracking. The integration is supported by [Delta Lake](/concepts/delta-lake.md) and Unity Catalog.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Methods for Writing Ray Data to Unity Catalog Tables

### Using `ray.data.Dataset.write_databricks_table` (Ray Data)

For Ray Data datasets, the `ray.data.Dataset.write_databricks_table` function provides a direct integration path. This function writes to Unity Catalog tables by:

1. Temporarily storing the Ray dataset in Unity Catalog Volumes.
2. Reading from Unity Catalog volumes with Spark.
3. Writing to a Unity Catalog table.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

Before calling this function, set the environment variable `_RAY_UC_VOLUMES_FUSE_TEMP_DIR` to a valid and accessible Unity Catalog volume path:^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
import ray
import os

os.environ["_RAY_UC_VOLUMES_FUSE_TEMP_DIR"] = "/Volumes/MyCatalog/MySchema/MyVolume/MyRayData"

ds = ray.data.range(1000)
ds.write_databricks_table()
```

### Writing from Ray Core Applications

For Ray Core applications, there are three main patterns for writing data to Unity Catalog tables from within the Ray task.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

All three patterns are necessary because Unity Catalog currently does not share credentials for writing to tables from non-Spark writers. Therefore, all data being written to a Unity Catalog table from a Ray Core task requires that the data be persisted and then read with Spark, or [Databricks Connect](/concepts/databricks-connect.md) must be set up within the Ray task.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

#### Pattern 1: Persist Output in a Temporary Location

The most common pattern is to store Ray task output in a temporary location (such as DBFS or Unity Catalog volumes), then consolidate the data into a Spark DataFrame. This works best when output data is in tabular form, such as a Pandas DataFrame.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
import os
import uuid
import numpy as np
import pandas as pd

@ray.remote
def write_example(task_id, path_prefix):
    num_rows = 100
    df = pd.DataFrame({
        'foo': np.random.rand(num_rows),
        'bar': np.random.rand(num_rows)
    })
    df.to_csv(os.path.join(path_prefix, f"result_part_{task_id}.csv"))

n_tasks = 10
dbfs_prefix = "/dbfs/<USERNAME>"
path_prefix = os.path.join(dbfs_prefix, f"/ray_tmp/write_task_{uuid.uuid4()}")

tasks = ray.get([write_example.remote(i, path_prefix) for i in range(n_tasks)])

# Read all CSV files into a single DataFrame and write to Unity Catalog
df = spark.read.csv(path_prefix.replace("/dbfs", "dbfs:"), header=True, inferSchema=True)
df.write.format("delta").saveAsTable("catalog.schema.my_table")
```

#### Pattern 2: Connect Using Spark Connect

Ray Core tasks can interact with Spark directly within the remote task using [Spark Connect](/concepts/spark-connect.md). This approach initializes a Spark session on the Ray worker that connects to the Spark cluster running on the driver node.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]

@ray.remote
class SparkHandler:
    def __init__(self, access_token=None, cluster_id=None, host_url=None):
        self.spark = (
            [[databrickssession|DatabricksSession]]
            .builder
            .remote(host=host_url, token=access_token, cluster_id=cluster_id)
            .getOrCreate()
        )
    
    def write_to_catalog(self):
        df = self.spark.sql("select * from samples.nyctaxi.trips")
        df.write.format("delta").mode("overwrite").saveAsTable("catalog.schema.taxi_trips")
        return df.count()

access_token = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()
cluster_id = dbutils.notebook.entry_point.getDbutils().notebook().getContext().clusterId().get()
host_url = f"https://{dbutils.notebook.entry_point.getDbutils().notebook().getContext().tags().get('browserHostName').get()}"

sh = SparkHandler.remote(access_token=access_token, cluster_id=cluster_id, host_url=host_url)
print(ray.get(sh.write_to_catalog.remote()))
```

**Note**: This approach creates a threading lock because it calls a single Spark driver, causing all tasks to wait for preceding Spark tasks to complete. For many concurrent tasks, it is better to persist output and combine later. Databricks recommends using an access token stored in [Databricks secrets](/concepts/databricks-secret-scopes.md) for production use cases.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Best Practices

- Store output data in a non-tabular format using Unity Catalog volumes for governance.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]
- Use the techniques described in the [Ray cluster best practices](/concepts/ray-cluster-scaling-best-practices.md) guide to ensure full cluster utilization.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]
- Set `num_cpus_worker_node` and `num_gpus_worker_node` to match the resources of the Spark worker node so that each Spark worker node launches one Ray worker node that fully utilizes resources.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Related Concepts

- Ray Data — Distributed dataset API in Ray
- Ray Core — Low-level Ray APIs for distributed computing
- [Unity Catalog](/concepts/unity-catalog.md) — Data governance and cataloging system on Databricks
- Unity Catalog Volumes — Storage volumes for non-tabular data
- [Spark Connect](/concepts/spark-connect.md) — API for connecting remote Spark sessions
- [Databricks Connect](/concepts/databricks-connect.md) — Client library for connecting to Databricks clusters
- Combine Ray and Spark in the Same Environment — Overview of Ray-Spark integration patterns
- When to use Spark vs. Ray — Guidance on choosing the right engine

## Sources

- combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

# Citations

1. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
