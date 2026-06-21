---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 50c8ee0d31b0dacaf6e35008f158b69d7a823614ec79e1dbe195c99be1e16581
  pageDirectory: concepts
  sources:
    - combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - writing-ray-data-to-unity-catalog-tables
    - WRDTUCT
  citations:
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
title: Writing Ray Data to Unity Catalog Tables
description: The ray.data.Dataset.write_databricks_table function for writing Ray datasets to Unity Catalog tables via temporary storage in Unity Catalog Volumes.
tags:
  - ray
  - unity-catalog
  - data-writing
  - databricks
timestamp: "2026-06-19T14:18:05.121Z"
---

Here is the wiki page for "Writing Ray Data to Unity Catalog Tables".

---

## Writing Ray Data to Unity Catalog Tables

**Writing Ray Data to Unity Catalog Tables** refers to the process of persisting the results of Ray data processing pipelines into [Unity Catalog](/concepts/unity-catalog.md)-governed tables on Databricks. This operation bridges the gap between Ray's distributed computing capabilities and Databricks' unified data governance, enabling teams to use Ray for complex transformations while storing the output in a secure, cataloged location for downstream consumption by Apache Spark or other tools. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Primary Method: `ray.data.Dataset.write_databricks_table`

The primary and recommended approach for writing Ray data to Unity Catalog tables is the `ray.data.Dataset.write_databricks_table` function, available in the Ray data module. This function is designed for Unity Catalog-enabled workspaces and handles the entire write workflow transparently. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### How It Works

Internally, `write_databricks_table` performs the following steps:

1.  **Temporary Storage in Unity Catalog Volumes**: The Ray dataset is first written to a temporary location within a Unity Catalog Volume.
2.  **Read by Spark**: Spark then reads the data from the Unity Catalog volume.
3.  **Write to Unity Catalog Table**: Finally, Spark writes the data to the specified Unity Catalog table.

^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### Prerequisites

Before you can use `write_databricks_table`, you must set the environment variable `"_RAY_UC_VOLUMES_FUSE_TEMP_DIR"` to a valid, accessible Unity Catalog volume path. This path serves as the staging area for the data. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

**Example:**

```python
import os
os.environ["_RAY_UC_VOLUMES_FUSE_TEMP_DIR"] = "/Volumes/MyCatalog/MySchema/MyVolume/MyRayData"
```

Ensure that the specified volume exists and that the running user or service principal has write permissions to it. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### Usage

```python
import ray

# Assume you have a Ray Dataset 'ds'
ds = ray.data.from_items([{"id": 1, "value": "a"}, {"id": 2, "value": "b"}])

# Write the dataset to a Unity Catalog table
ds.write_databricks_table(table_name="my_catalog.my_schema.my_table")
```

^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Alternative Method: Persisting via Spark Parquet

For workspaces that are not Unity Catalog-enabled or for users who prefer a more explicit workflow, you can write a Ray dataset to a Parquet file in DBFS and then read it with Spark to write to a table. This is a fallback method. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
import ray

# Assume you have a Ray Dataset 'ds'
tmp_path = "/tmp/my_ray_data.parquet"
ds.write_parquet(tmp_path)

# Read the Parquet file with Spark and write to a Unity Catalog table
df = spark.read.parquet(tmp_path)
df.write.format("delta").saveAsTable("my_catalog.my_schema.my_table")
```

^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Writing from Ray Core Applications

For Ray Core applications (lower-level Ray API), writing to Unity Catalog follows one of three patterns:

- **Persist output to a temporary location** (e.g., DBFS or Unity Catalog volumes) and then read with Spark.
- **Use [Spark Connect](/concepts/spark-connect.md)** to directly connect a Ray task to a Spark cluster.
- **Use third-party libraries** like `deltalake` or `deltaray` (though these have limitations with Unity Catalog).

For Unity Catalog tables, the first pattern is most common because Unity Catalog does not share credentials for writing from non-Spark writers. Therefore, the data must be persisted and then read with Spark. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Best Practices

- **Always set `_RAY_UC_VOLUMES_FUSE_TEMP_DIR`** to a volume path with write access before calling `write_databricks_table`. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]
- **For large datasets**, the temporary storage method is preferred over in-memory transfers to avoid driver-node memory limits. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]
- **Use Unity Catalog Volumes** for staging non-tabular data to provide governance and lineage. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Limitations

Currently, Unity Catalog does not share credentials for writing to tables from non-Spark writers. This means all data written to a Unity Catalog table from a Ray Core task must go through a two-step process: persist to a temporary location, then read with Spark. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Related Concepts

- Ray Data — The distributed dataset abstraction for Ray
- [Unity Catalog](/concepts/unity-catalog.md) — The governance catalog for Databricks assets
- Unity Catalog Volumes — Storage volumes for staging data
- DBFS — Databricks File System for temporary storage
- [Delta Lake](/concepts/delta-lake.md) — The storage format for Unity Catalog tables
- [Spark Connect](/concepts/spark-connect.md) — A method for connecting Ray tasks to Spark
- Combine Ray and Spark — General guidance for co-locating both frameworks
- from_spark() — The inverse operation for bringing Spark data into Ray

## Sources

- combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

# Citations

1. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
