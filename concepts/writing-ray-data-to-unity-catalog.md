---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 86bc350245a587ff0195a26b8dee92c8f60058a2f366788eb06fdf793aef4b54
  pageDirectory: concepts
  sources:
    - combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - writing-ray-data-to-unity-catalog
    - WRDTUC
    - Write Ray Data to Spark
  citations:
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
title: Writing Ray Data to Unity Catalog
description: Writing Ray datasets back to Unity Catalog tables using ray.data.Dataset.write_databricks_table(), which stages data in Unity Catalog Volumes before writing with Spark.
tags:
  - databricks
  - ray
  - unity-catalog
  - data-transfer
timestamp: "2026-06-19T17:46:34.729Z"
---

```markdown
---
title: Writing Ray Data to Unity Catalog
summary: Using ray.data.Dataset.write_databricks_table() and other patterns to write Ray datasets to Unity Catalog tables, including limitations and best practices.
sources:
  - combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:39:20.862Z"
updatedAt: "2026-06-18T14:39:20.862Z"
tags:
  - ray
  - unity-catalog
  - databricks
  - data-writing
aliases:
  - writing-ray-data-to-unity-catalog
  - WRDTUC
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Writing Ray Data to Unity Catalog

**Writing Ray Data to Unity Catalog** refers to the process of persisting datasets produced by Ray (either from `ray.data.Dataset` or from Ray Core tasks) into [[Unity Catalog]] tables on Databricks. Because Unity Catalog does not expose write credentials to non‑Spark engines, writing from Ray requires indirection: data is first staged in a Unity Catalog Volumes or other location and then ingested by Spark, or a Spark session is established inside the Ray task using [[Databricks Connect]]. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Using `write_databricks_table` for Ray Data Datasets

For Unity Catalog–enabled workspaces, the recommended approach is to call `ray.data.Dataset.write_databricks_table()`. This function automatically stages the Ray dataset in a Unity Catalog Volume, reads it with Spark, and writes it to the target Unity Catalog table. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

Before calling the function, set the environment variable `_RAY_UC_VOLUMES_FUSE_TEMP_DIR` to a valid, accessible Unity Catalog volume path:

```python
import os
os.environ["_RAY_UC_VOLUMES_FUSE_TEMP_DIR"] = "/Volumes/MyCatalog/MySchema/MyVolume/MyRayData"
```

Then write the dataset:

```python
ray.data.Dataset.write_databricks_table()
```

This method is available on Databricks Runtime ML 15.0 and above and handles the complete pipeline from Ray to Unity Catalog transparently. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Writing from Ray Core Applications

When working with Ray Core tasks, two patterns can write data into Unity Catalog tables:

- **Pattern 1 – Persist to a temporary location.** Store each task’s output (e.g., a CSV file) in a temporary location such as a Unity Catalog Volume or DBFS. After all tasks complete, the Ray driver thread reads the files with Spark and consolidates them into a final DataFrame for writing to a Unity Catalog table. This approach works well for large outputs that exceed driver memory. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

- **Pattern 2 – Connect using Databricks Connect.** Inside a Ray remote task, create a `DatabricksSession` that points to the same cluster. The Ray task can then directly write a Spark DataFrame to a Unity Catalog table using `df.write.format("delta").mode("overwrite").saveAsTable("catalog.schema.table")`. Because this path uses a single Spark driver, tasks are effectively serialized; it is best suited for low‑concurrency workloads. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

Third‑party libraries such as `delta-rs` or `deltaray` are **not** supported for Unity Catalog tables; they currently work only with Hive [[metastore|Metastore]] tables. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Limitations

Unity Catalog does not share write credentials with non‑Spark writers. As a result, any attempt to write to a Unity Catalog table from a Ray Core task must either persist the data and then use Spark to load it, or establish a Spark session via Databricks Connect inside the Ray task. Direct writes using the Ray or Python file system are not possible. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Related Concepts

- Ray Data – High‑level API for distributed datasets in Ray.
- [[Unity Catalog]] – The governance and access control system for Databricks.
- Unity Catalog Volumes – Storage volumes used as staging areas for Ray‑to‑Spark writes.
- [[Databricks Connect]] – Library that allows external applications to connect to a Databricks Spark cluster.
- [[Delta Sharing]] – Alternative method for reading data from Databricks into Ray.
- [[Spark DataFrame Evaluation Pattern|Spark DataFrame]] – The Spark structure used to ingest staged data before writing to Unity Catalog.

## Sources

- combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
```

# Citations

1. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
