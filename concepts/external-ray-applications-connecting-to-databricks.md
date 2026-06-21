---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9222b8d38b3b1e7525c6ee06b708fbbb0d005db21106cd0ac9974fd26f595add
  pageDirectory: concepts
  sources:
    - combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-ray-applications-connecting-to-databricks
    - ERACTD
  citations:
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
title: External Ray Applications Connecting to Databricks
description: Connecting Ray applications running outside of Databricks to Unity Catalog tables using ray.data.read_databricks_tables() or Delta Sharing with ray.data.read_delta_sharing_tables().
tags:
  - databricks
  - ray
  - unity-catalog
  - delta-sharing
  - external-applications
timestamp: "2026-06-19T17:46:42.885Z"
---

# External Ray Applications Connecting to Databricks

**External Ray Applications Connecting to Databricks** refers to the capability for Ray applications running outside the Databricks environment (for example, on a local machine, a different cluster, or a cloud instance) to read data from Databricks-managed tables, including [Unity Catalog](/concepts/unity-catalog.md) tables and [Delta Sharing](/concepts/delta-sharing.md) tables. This integration allows external Ray workloads to leverage Databricks’ data governance and storage without requiring Ray to run inside a Databricks cluster. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Reading from a Databricks SQL Warehouse

For Ray 2.8.0 and above, external applications can use the `ray.data.read_databricks_tables()` API to load data from a Unity Catalog table by connecting to a Databricks SQL Warehouse. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### Configuration

Before calling the API, set the following environment variables:

- `DATABRICKS_TOKEN` – a SQL warehouse access token.
- `DATABRICKS_HOST` – the Databricks workspace URL (only required when not running on Databricks Runtime). ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### API Example

```python
import ray

ray_dataset = ray.data.read_databricks_tables(
    warehouse_id='...',          # Databricks SQL warehouse ID
    catalog='catalog_1',         # Unity Catalog name
    schema='db_1',               # Schema name
    query="SELECT title, score FROM movie WHERE year >= 1980",
)
```

^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### Cache Limitation

Databricks SQL warehouses cache query results for approximately two hours. For long-running Ray workloads that need to access the data repeatedly, call `ray.data.Dataset.materialize` to materialize the dataset into the Ray distributed object store, avoiding cache expiration. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Reading from a Databricks Delta Sharing Table

For Ray 2.33 and above, external applications can read data from [Delta Sharing](/concepts/delta-sharing.md) (OpenSharing) tables using the `ray.data.read_delta_sharing_tables()` API. This method is more reliable than reading from a warehouse cache because it does not depend on the warehouse’s query result cache. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### API Example

```python
import ray

ds = ray.data.read_delta_sharing_tables(
    url=f"<profile-file-path>#<share-name>.<schema-name>.<table-name>",
    limit=100000,
    version=1,
)
```

^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Related Concepts

- Ray – Distributed computing framework.
- [Unity Catalog](/concepts/unity-catalog.md) – Databricks’ unified governance solution for data and AI assets.
- [Delta Sharing](/concepts/delta-sharing.md) – Open protocol for sharing data across platforms.
- Databricks SQL Warehouse – Compute resource for SQL queries and BI workloads.
- Ray Data – Ray’s distributed dataset API.
- Combine Ray and Spark in the Same Environment – Running Ray and Spark together on Databricks.

## Sources

- combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

# Citations

1. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
