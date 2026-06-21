---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 42c7b16bbeb824823bbd5b2f891d606a0a443b67e41504d4b075ed3330cf04ea
  pageDirectory: concepts
  sources:
    - combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-spark-integration-on-databricks
    - RIOD
  citations:
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
title: Ray-Spark Integration on Databricks
description: Architecture and patterns for running Ray and Spark in the same execution environment on Databricks, leveraging Delta Lake and Unity Catalog for data management.
tags:
  - databricks
  - ray
  - spark
  - distributed-computing
timestamp: "2026-06-19T14:17:32.206Z"
---

# Ray-Spark Integration on Databricks

**Ray-Spark Integration on Databricks** refers to the ability to run Ray and Apache Spark operations in the same execution environment, combining the strengths of both distributed computing engines. This integration is supported by [Delta Lake](/concepts/delta-lake.md) and [Unity Catalog](/concepts/unity-catalog.md), which provide robust data management, secure access, and lineage tracking.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

The integration enables several common use cases: transferring data in-memory from Spark to Ray, writing Ray data back to Delta Lake or other storage via Spark, and connecting external Ray applications to Unity Catalog tables.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Create a Distributed Ray Dataset from a Spark DataFrame

To create a distributed Ray dataset from a Spark DataFrame, use the `ray.data.from_spark()` function. This reads a Spark DataFrame directly from Ray without writing data to an intermediate location, provided that the Spark cluster configuration `spark.databricks.pyspark.dataFrameChunk.enabled` is set to `true` before starting the cluster. This feature is available on [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) 15.0 and above.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

If you are using an autoscaling Spark cluster (including those with spot instances), you must set the `use_spark_chunk_api` parameter to `False` to avoid cache misses when executors terminate.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
ray_ds = ray.data.from_spark(df, use_spark_chunk_api=False)
```

## Write Ray Data to Spark

Ray data can be written to Spark by first persisting it to a location that Spark can access. For Unity Catalog enabled workspaces, use the `ray.data.Dataset.write_databricks_table` function, which temporarily stores the Ray dataset in Unity Catalog Volumes, reads from those volumes with Spark, and writes to a Unity Catalog table. The environment variable `_RAY_UC_VOLUMES_FUSE_TEMP_DIR` must point to a valid Unity Catalog volume path before calling this function.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
ds = ray.data.from_spark(df)
ds.write_databricks_table()
```

For workspaces without Unity Catalog, store the Ray dataset as a temporary file (e.g., Parquet in DBFS) and then read it with Spark to write to a Delta table.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
ds.write_parquet(tmp_path)
df = spark.read.parquet(tmp_path)
df.write.format("delta").saveAsTable(table_name)
```

## Write Data from Ray Core Applications to Spark

Ray Core (the lower-level APIs of Ray) can also exchange data with Spark. Three main patterns are available.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### Pattern 1: Persist output in a temporary location

The most common approach: Ray tasks write output data (e.g., as CSV files) to a temporary location such as Unity Catalog Volumes or DBFS. The Ray driver then reads those files and consolidates them into a Spark DataFrame. This is recommended when Ray task outputs are too large to fit in the driver node’s memory.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### Pattern 2: Connect using Spark Connect

Ray tasks can interact with Spark directly inside remote tasks by using [Spark Connect](/concepts/spark-connect.md). Each Ray worker sets up a Spark session pointing to the cluster running on the driver node. Because this approach uses a single Spark driver, tasks become sequential; it is best suited for scenarios with few concurrent tasks. In production, use a Databricks access token stored in secrets rather than a notebook-generated token.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### Pattern 3: Third-party libraries

Libraries such as `deltalake` (from the delta-rs project) or `deltaray` (from the Delta Incubator) can write data from Ray Core tasks to Delta Lake or Spark tables. These libraries are not officially supported by Databricks, and the `deltalake` approach currently works only with [Hive metastore](/concepts/built-in-hive-metastore.md) tables, not Unity Catalog tables.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Connect External Ray Applications to Databricks

### Create Ray dataset from a Databricks warehouse query

For Ray 2.8.0 and above, use the `ray.data.read_databricks_tables` API to load data from a Unity Catalog table via a Databricks SQL Warehouse. Set the `DATABRICKS_TOKEN` environment variable (and `DATABRICKS_HOST` if not running on Databricks Runtime). Because warehouse query results are cached for approximately two hours, materialize the Ray dataset with `ray.data.Dataset.materialize` for long-running workloads.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
ray_dataset = ray.data.read_databricks_tables(
    warehouse_id='...',
    catalog='catalog_1',
    schema='db_1',
    query="SELECT title, score FROM movie WHERE year >= 1980",
)
```

### Create Ray dataset from a Databricks Open Sharing table

For Ray 2.33 and above, use `ray.data.read_delta_sharing_tables` to read from [Delta Sharing](/concepts/delta-sharing.md) tables. This method is more reliable than reading from a warehouse cache.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
ds = ray.data.read_delta_sharing_tables(
    url="<profile-file-path>#<share-name>.<schema-name>.<table-name>",
    limit=100000,
    version=1,
)
```

## Best Practices

- Follow the Ray cluster best practice guide to ensure full cluster utilization.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]
- Use Unity Catalog Volumes to store non-tabular output data with governance.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]
- Configure `num_cpus_worker_node` and `num_gpus_worker_node` to match the resources of the Spark worker node, launching one Ray worker node per Spark worker node for full resource utilization.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Limitations

Unity Catalog currently does not share credentials for writing to tables from non-Spark writers. Any data written to a Unity Catalog table from a Ray Core task must be persisted and then read with Spark, or [Databricks Connect](/concepts/databricks-connect.md) must be set up inside the Ray task.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- Apache Spark
- Ray
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- [Spark Connect](/concepts/spark-connect.md)
- Databricks SQL Warehouse
- [Delta Sharing](/concepts/delta-sharing.md)
- [Hive metastore](/concepts/built-in-hive-metastore.md)
- Unity Catalog Volumes
- [Databricks Connect](/concepts/databricks-connect.md)

## Sources

- combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

# Citations

1. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
