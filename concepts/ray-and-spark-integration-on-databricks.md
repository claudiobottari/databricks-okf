---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 99fa7f7aa7fd1b5bb51aefe1fb3cd59c9589c557b62e57a45bcd1912b8666b72
  pageDirectory: concepts
  sources:
    - combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-and-spark-integration-on-databricks
    - Spark Integration on Databricks and Ray
    - RASIOD
    - Combine Ray and Spark in the same environment on Databricks
    - Combine Ray and Spark on Databricks
    - Ray and Spark Integration
  citations:
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-on-aws.md
title: Ray and Spark Integration on Databricks
description: Running Ray and Spark in the same execution environment on Databricks, supported by Delta Lake and Unity Catalog for data management and lineage tracking.
tags:
  - databricks
  - ray
  - spark
  - distributed-computing
timestamp: "2026-06-19T17:46:29.550Z"
---

# Ray and Spark Integration on Databricks

With Databricks, you can run Ray and Spark operations in the same execution environment to leverage the strengths of both distributed computing engines. The integration is supported by [Delta Lake](/concepts/delta-lake.md) and [Unity Catalog](/concepts/unity-catalog.md), which provide robust data management, secure access, and lineage tracking. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Use Cases

The integration covers three primary use cases:
- **Write Spark data to Ray data**: Efficiently transfer data in-memory to Ray.
- **Write Ray data to Spark**: Output data from Ray back to Delta Lake or other storage solutions.
- **Connect external Ray applications to Unity Catalog**: Connect Ray applications outside of Databricks to load data from a Unity Catalog table. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-on-aws.md]

## Create a Distributed Ray Dataset from a Spark DataFrame

Use `ray.data.from_spark()` to read a Spark DataFrame directly from Ray without writing the data to any location. This in-memory transfer is available on Databricks Runtime ML 15.0 and above. To enable the feature, set the Spark cluster configuration `spark.databricks.pyspark.dataFrameChunk.enabled` to `true` before starting the cluster. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-on-aws.md]

```python
ray_ds = ray.data.from_spark(df)
```

**Autoscaling note**: Autoscaling Spark clusters (including those using spot instances) must set the `use_spark_chunk_api` parameter to `False` when calling `from_spark()`. Otherwise, cache misses occur because the cache on a terminated Spark executor is lost. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Write Ray Data to Spark

On Databricks Runtime ML below 15.0, you can write directly to an object store using `ray_dataset.write_parquet()`, then read with Spark. On Unity Catalog-enabled workspaces, use the `ray.data.Dataset.write_databricks_table` function, which temporarily stores the dataset in Unity Catalog Volumes, reads them with Spark, and writes to a Unity Catalog table. Before calling this function, set the environment variable `_RAY_UC_VOLUMES_FUSE_TEMP_DIR` to a valid Unity Catalog volume path, such as `"/Volumes/MyCatalog/MySchema/MyVolume/MyRayData"`. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

For workspaces without Unity Catalog, manually store the Ray dataset as a temporary file (e.g., Parquet in DBFS), then read with Spark and write to a Delta table. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Write Data from Ray Core Applications to Spark

Ray Core (the lower-level APIs of Ray) and Spark workloads can exchange data within the same environment. Three main patterns exist:

### Pattern 1: Persist Output in a Temporary Location

Store Ray task outputs (e.g., CSV files) in DBFS or Unity Catalog volumes, then combine them into a Spark DataFrame. This is suitable when output data is too large to fit in the driver node memory or the shared object store. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
@ray.remote
def write_example(task_id, path_prefix):
    # produce a pandas DataFrame and write to CSV
    ...
# consolidate all CSV files into a Spark DataFrame
df = spark.read.csv(path_prefix.replace("/dbfs", "dbfs:"), header=True, inferSchema=True)
```

### Pattern 2: Connect Using Spark Connect

Ray tasks can use [Spark Connect](/concepts/spark-connect.md) to interact with the Spark cluster running on the driver node. Configure Ray cluster resources to leave CPU/GPU for Spark. This approach creates a threading lock—all Ray tasks wait for preceding Spark tasks to complete—so it is best used when concurrent tasks are few. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
from databricks.connect import [[databrickssession|DatabricksSession]]
sh = SparkHandler.remote(access_token=..., cluster_id=..., host_url=...)
ray.get(sh.test.remote())
```

### Pattern 3: Third-Party Libraries

Libraries such as `deltalake` (from the delta-rs project) and `deltaray` (from the Delta Incubator) can write data from Ray Core tasks directly to Delta Lake or Spark tables. Note that `deltalake` currently works only with Hive [Metastore](/concepts/metastore.md) tables, not Unity Catalog tables. These libraries are not officially supported by Databricks. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
from deltalake import write_deltalake
write_deltalake(table_name, pdf, mode="append")
```

## Connect External Ray Applications to Databricks

### Create a Ray Dataset from a Databricks Warehouse Query

For Ray 2.8.0 and above, external applications can use `ray.data.read_databricks_tables()` to load data from a Unity Catalog table via a Databricks SQL warehouse. Set the environment variables `DATABRICKS_TOKEN` and `DATABRICKS_HOST` (if not on Databricks Runtime) before calling the API. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
ray_dataset = ray.data.read_databricks_tables(
    warehouse_id='...',
    catalog='catalog_1',
    schema='db_1',
    query="SELECT title, score FROM movie WHERE year >= 1980"
)
```

> **Warning**: Warehouse query results are cached for approximately 2 hours. For long-running workloads, call `ray.data.Dataset.materialize` to persist the dataset in the Ray distributed object store. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### Create a Ray Dataset from a Databricks OpenSharing Table

The `ray.data.read_delta_sharing_tables` API (available on Ray 2.33 and above) reads data from [Databricks Delta Sharing](/concepts/opensharing-databricks-delta-sharing.md) tables, which is more reliable than reading from a warehouse cache. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
ds = ray.data.read_delta_sharing_tables(
    url="<profile-file-path>#<share-name>.<schema-name>.<table-name>",
    limit=100000,
    version=1,
)
```

## Best Practices

- Follow the Ray Cluster Best Practices guide to ensure full cluster utilization.
- Use Unity Catalog volumes to store non-tabular output data and provide governance.
- Configure `num_cpus_worker_node` and `num_gpus_worker_node` to match the CPU and GPU counts of the Spark worker node, so each Spark worker node launches one Ray worker node that fully uses the resources. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Limitations

Unity Catalog currently does not share credentials for writing to tables from non-Spark writers. Therefore, writing to a Unity Catalog table from a Ray Core task requires either persisting data and reading it with Spark, or setting up [Databricks Connect](/concepts/databricks-connect.md) within the Ray task. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Related Concepts

- Ray – Distributed computing framework for AI and Python workloads.
- Apache Spark – Distributed data processing engine.
- [Unity Catalog](/concepts/unity-catalog.md) – Fine-grained governance for data and AI assets.
- [Delta Lake](/concepts/delta-lake.md) – Open storage layer for reliable data lakes.
- [Databricks Connect](/concepts/databricks-connect.md) – Client library for connecting to Spark clusters from external applications.
- Ray Core – Low-level Ray APIs for general distributed computing.
- Databricks SQL Warehouse – SQL analytics endpoint for BI and data applications.
- [Delta Sharing](/concepts/delta-sharing.md) – Open protocol for secure data sharing across platforms.

## Sources

- combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

# Citations

1. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
2. combine-ray-and-spark-in-the-same-environment-on-databricks-on-aws.md
