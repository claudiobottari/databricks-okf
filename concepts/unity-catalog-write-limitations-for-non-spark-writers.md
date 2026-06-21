---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7fa2cb466e990632d5c8813b72ec33ab9e1c3e499caabf4640c8fca78b4b8cc7
  pageDirectory: concepts
  sources:
    - combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-write-limitations-for-non-spark-writers
    - UCWLFNW
  citations:
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-on-aws.md
title: Unity Catalog Write Limitations for Non-Spark Writers
description: The limitation that Unity Catalog does not share credentials for writing to tables from non-Spark writers, requiring data to be persisted and read with Spark or using Databricks Connect within Ray tasks.
tags:
  - unity-catalog
  - ray
  - spark
  - limitations
  - databricks
timestamp: "2026-06-19T14:18:00.450Z"
---

# Unity Catalog Write Limitations for Non-Spark Writers

**Unity Catalog Write Limitations for Non-Spark Writers** refers to the restriction that Unity Catalog does not share credentials for writing to tables from non-Spark writers, such as Ray Core tasks or other external frameworks. This means that data cannot be directly written from these sources into Unity Catalog tables without an intermediary step.

## Overview

When using Unity Catalog, non-Spark writers — including Ray Core tasks, external applications, and other distributed computing frameworks — cannot directly write to Unity Catalog tables. Unity Catalog does not share the necessary credentials for write operations from these non-Spark sources. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Workarounds

### Pattern 1: Persist Output and Read with Spark

Data written from non-Spark writers must be persisted to a temporary storage location and then read into a Spark DataFrame before being written to a Unity Catalog table. This approach involves:
1. Writing output data to a temporary location such as Unity Catalog Volumes or DBFS
2. Reading the persisted data with Spark
3. Writing the Spark DataFrame to the target Unity Catalog table

^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### Pattern 2: Databricks Connect

Another workaround is to set up [Databricks Connect](/concepts/databricks-connect.md) within the non-Spark task. This allows a Ray Core task or other non-Spark writer to connect to a Spark cluster directly, enabling interactions with Spark DataFrames and tables. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-on-aws.md]

### Writing Ray Data to Unity Catalog Tables

For Ray datasets specifically, Unity Catalog provides the `ray.data.Dataset.write_databricks_table` function, which handles the intermediate steps automatically:
- The Ray dataset is temporarily stored in Unity Catalog Volumes
- Spark reads from the Unity Catalog volumes
- The data is then written to a Unity Catalog table

Before calling this function, the environment variable `_RAY_UC_VOLUMES_FUSE_TEMP_DIR` must be set to a valid Unity Catalog volume path (e.g., `/Volumes/MyCatalog/MySchema/MyVolume/MyRayData`). ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### Third-Party Libraries

Third-party libraries such as `deltalake` from the `delta-rs` project or `deltaray` from the Delta Incubator project can also be used. However, Databricks does not officially support these libraries, and they currently only work with Hive [Metastore](/concepts/metastore.md) tables, not Unity Catalog tables. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Affected Workloads

This limitation affects:
- Ray Core tasks
- External Ray applications running outside of Databricks
- Any non-Spark distributed computing framework attempting to write to Unity Catalog tables directly

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The governance and metadata layer that enforces these write restrictions
- [Ray and Spark Integration](/concepts/ray-and-spark-integration-on-databricks.md) — Combining Ray and Spark workloads on Databricks
- Data Exchange Between Ray and Spark — Patterns for moving data between Ray and Spark
- Unity Catalog Volumes — Temporary storage location used as an intermediary
- [Hive Metastore](/concepts/built-in-hive-metastore.md) — Alternative [Metastore](/concepts/metastore.md) that allows direct writes from non-Spark writers

## Sources

- combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

# Citations

1. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
2. combine-ray-and-spark-in-the-same-environment-on-databricks-on-aws.md
