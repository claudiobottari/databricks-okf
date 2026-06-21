---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 672b0aa7c1cff71742806406f51cd89d3333e657afdbb3ad6f8620eb32cd574c
  pageDirectory: concepts
  sources:
    - combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-ray-applications-to-databricks-connectivity
    - ERATDC
  citations:
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
title: External Ray Applications to Databricks Connectivity
description: Connecting Ray applications running outside Databricks to Unity Catalog tables via SQL warehouses (ray.data.read_databricks_tables) and Delta Sharing (ray.data.read_delta_sharing_tables)
tags:
  - ray
  - databricks
  - connectivity
  - delta-sharing
timestamp: "2026-06-19T09:17:27.706Z"
---

# External Ray Applications to Databricks Connectivity

**External Ray Applications to Databricks Connectivity** refers to the methods and APIs that allow Ray applications running outside of a Databricks environment to read data from Databricks tables, including Unity Catalog tables and Delta Sharing tables. This connectivity enables organizations to leverage Ray's distributed computing capabilities for data processing and machine learning workloads while maintaining access to governed data stored in Databricks.

## Overview

Ray applications external to Databricks can connect to Databricks data sources using dedicated Ray APIs. These APIs provide direct access to data without requiring the application to run inside a Databricks cluster or runtime environment. The primary methods are reading from Databricks SQL warehouses and reading from Delta Sharing (OpenSharing) tables. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Creating a Ray Dataset from a Databricks Warehouse Query

For Ray 2.8.0 and above, external Ray applications can use the `ray.data.read_databricks_tables` API to load data from Unity Catalog tables via a Databricks SQL warehouse. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### Prerequisites

Before using this API, you must configure authentication credentials:

1. Set the `DATABRICKS_TOKEN` environment variable to your SQL warehouse access token.
2. If not running on Databricks Runtime, set the `DATABRICKS_HOST` environment variable to the Databricks workspace URL. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

Example environment variable setup:

```
export DATABRICKS_HOST=adb-<workspace-id>.<random-number>.azuredatabricks.net
```

### API Usage

The `ray.data.read_databricks_tables()` function accepts a warehouse ID, catalog name, schema name, and a SQL query: ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
import ray

ray_dataset = ray.data.read_databricks_tables(
    warehouse_id='...',  # Databricks SQL warehouse ID
    catalog='catalog_1',  # Unity Catalog name
    schema='db_1',  # Schema name
    query="SELECT title, score FROM movie WHERE year >= 1980",
)
```

### Cache Limitations

Databricks warehouses can only cache query results for approximately 2 hours. For long-running workloads, call the `ray.data.Dataset.materialize` method to materialize the Ray dataset to the Ray distributed object store. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Creating a Ray Dataset from a Databricks Delta Sharing Table

An alternative and more reliable method is reading from Databricks [Delta Sharing](/concepts/delta-sharing.md) (OpenSharing) tables. Reading from OpenSharing tables avoids the cache expiration issues associated with warehouse queries. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

The `ray.data.read_delta_sharing_tables` API is available on Ray 2.33 and above: ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
import ray

ds = ray.data.read_delta_sharing_tables(
    url=f"<profile-file-path>#<share-name>.<schema-name>.<table-name>",
    limit=100000,
    version=1,
)
```

## Comparison of Connectivity Methods

| Method | Ray Version Requirement | Key Advantage | Key Limitation |
|--------|------------------------|---------------|----------------|
| `read_databricks_tables` | 2.8.0+ | Direct SQL warehouse access | Cache expires after ~2 hours |
| `read_delta_sharing_tables` | 2.33+ | No cache expiration; more reliable | Requires Delta Sharing setup |

## Related Concepts

- [Ray and Spark Integration on Databricks](/concepts/ray-and-spark-integration-on-databricks.md) – Running Ray and Spark together in the same environment.
- [Unity Catalog](/concepts/unity-catalog.md) – The data governance layer for Databricks tables.
- [Delta Sharing](/concepts/delta-sharing.md) – The open protocol for sharing data across platforms.
- Ray Data API – The Ray library for distributed data loading and transformation.
- Databricks SQL Warehouses – The compute endpoints for SQL queries on Databricks.

## Sources

- combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

# Citations

1. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
