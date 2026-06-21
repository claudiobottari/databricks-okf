---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b5c0d4ca10b68591a5bf317421d4b8f119f2f15958e5cde5c58257e6b4cab306
  pageDirectory: concepts
  sources:
    - combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-data-to-unity-catalog-via-write_databricks_table
    - RDTUCVW
    - Ray Data write_databricks_table
  citations:
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
title: Ray Data to Unity Catalog via write_databricks_table()
description: Write Ray datasets directly to Unity Catalog tables using ray.data.Dataset.write_databricks_table(), which stages data through Unity Catalog Volumes and requires the _RAY_UC_VOLUMES_FUSE_TEMP_DIR environment variable.
tags:
  - ray
  - unity-catalog
  - databricks
  - data-writing
timestamp: "2026-06-18T11:01:01.184Z"
---

Here is the wiki page for "Ray Data to Unity Catalog via `write_databricks_table()`".

---

The `ray.data.Dataset.write_databricks_table()` function is the primary direct method for writing a Ray Data dataset to a [Unity Catalog](/concepts/unity-catalog.md) table on Databricks. It bridges Ray and Apache Spark by temporarily staging the Ray dataset in Unity Catalog Volumes, reading that staged data with Spark, and finally writing it to the target Unity Catalog table.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Prerequisites

Before calling `write_databricks_table()`, you must set the environment variable `_RAY_UC_VOLUMES_FUSE_TEMP_DIR` to a valid, accessible Unity Catalog volume path. The volume is used as a temporary staging area during the transfer. Without this environment variable set, the function will fail.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

Example path:

```
/Volumes/MyCatalog/MySchema/MyVolume/MyRayData
```

## Usage

The function reads a Ray Data dataset and writes it directly to a Unity Catalog table without manual intermediate file writes. The following example writes a dataset to the table `my_db.my_table`: ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
import os

# Must be set
os.environ["_RAY_UC_VOLUMES_FUSE_TEMP_DIR"] = "/Volumes/MyCatalog/MySchema/MyVolume/MyRayData"

ds = ray.data.from_spark(df)
ds.write_databricks_table("my_db.my_table")
```

## How it works

The function performs the following internal steps: ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

1. The Ray dataset is temporarily stored in the Unity Catalog volume path specified by `_RAY_UC_VOLUMES_FUSE_TEMP_DIR`.
2. Spark reads the staged data from the Unity Catalog volume.
3. Spark writes the data into the target Unity Catalog table.

This two-phase approach is necessary because [Unity Catalog](/concepts/unity-catalog.md) currently does not share credentials for writing to tables from non-Spark writers (such as Ray). Therefore, all data written to a Unity Catalog table from a Ray Core task must be persisted and then read with Spark, or [Databricks Connect](/concepts/databricks-connect.md) must be set up within the Ray task.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Limitations

- Unity Catalog does not share credentials for writes from non-Spark writers, so direct Ray-to-table writes without Spark staging are not possible.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]
- The `_RAY_UC_VOLUMES_FUSE_TEMP_DIR` environment variable must be set to a valid, accessible volume path before calling the function.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Related Concepts

- Ray Data — The Ray-native distributed dataset representation
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance layer that manages the target table
- Unity Catalog Volumes — The staging directory for the write operation
- [Databricks Connect](/concepts/databricks-connect.md) — Alternative method for Ray tasks to interact with Spark

## Sources

- combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

# Citations

1. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
