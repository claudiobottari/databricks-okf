---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0f832a3db7844cc0f89591654453794c0abb9cb72e1f170714c8736fb1d54537
  pageDirectory: concepts
  sources:
    - combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-ray-applications-to-databricks
    - ERATD
    - external-ray-applications-to-databricks-connectivity
    - ERATDC
    - external-ray-applications-with-databricks
    - ERAWD
  citations:
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
title: External Ray Applications to Databricks
description: Connecting Ray applications running outside Databricks to Databricks data sources using ray.data.read_databricks_tables (SQL warehouse) and ray.data.read_delta_sharing_tables (Delta Sharing) APIs.
tags:
  - ray
  - databricks
  - external-applications
  - data-access
timestamp: "2026-06-19T14:17:49.033Z"
---

# External Ray Applications to Databricks

**External Ray Applications to Databricks** refers to the ability to connect Ray applications running outside of a Databricks workspace to data stored in [Unity Catalog](/concepts/unity-catalog.md) or other Databricks storage systems. This enables organizations to leverage Ray's distributed computing capabilities for workloads that need to access governed data within Databricks.

## Overview

Databricks provides several mechanisms for external Ray applications to load data from Databricks-managed tables. These approaches allow teams to integrate their existing Ray infrastructure with Databricks' data management and governance features, including [Delta Lake](/concepts/delta-lake.md) and [Unity Catalog](/concepts/unity-catalog.md). ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Reading Data from Databricks Warehouse

For Ray 2.8.0 and above, external Ray applications can connect to Databricks tables using the `ray.data.read_databricks_tables()` API. This method queries data through a Databricks SQL Warehouse. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### Prerequisites

Before using this API, you must set up authentication:

```bash
export DATABRICKS_HOST=adb-<workspace-id>.<random-number>.azuredatabricks.net
```

Set the `DATABRICKS_TOKEN` environment variable to your SQL warehouse access token. If not running on Databricks Runtime, also set the `DATABRICKS_HOST` environment variable to the Databricks workspace URL. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### Usage

```python
import ray

ray_dataset = ray.data.read_databricks_tables(
    warehouse_id='...',  # Databricks SQL warehouse ID
    catalog='catalog_1',  # Unity Catalog name
    schema='db_1',  # Schema name
    query="SELECT title, score FROM movie WHERE year >= 1980",
)
```

The API accepts parameters for the warehouse ID, catalog, schema, and a SQL query to filter the data. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### Caching Considerations

Databricks warehouses can only cache query results for approximately 2 hours. For long-running workloads, call the `ray.data.Dataset.materialize` method to materialize the Ray dataset to the Ray distributed object store, ensuring data persists throughout the job's lifecycle. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Reading Data from OpenSharing Tables

For Ray 2.33 and above, external applications can also read data from Databricks [Delta Sharing](/concepts/delta-sharing.md) tables using the `ray.data.read_delta_sharing_tables()` API. This approach is more reliable than reading from a Databricks warehouse cache because it avoids warehouse query caching limitations. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### Usage

```python
import ray

ds = ray.data.read_delta_sharing_tables(
    url=f"<profile-file-path>#<share-name>.<schema-name>.<table-name>",
    limit=100000,
    version=1,
)
```

The function accepts a Delta Sharing profile URL, an optional row limit, and a version parameter for time-travel queries. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Comparison of Approaches

| Approach | Ray Version | Use Case |
|----------|-------------|----------|
| `read_databricks_tables()` | 2.8.0+ | Querying Unity Catalog tables via SQL Warehouse |
| `read_delta_sharing_tables()` | 2.33+ | More reliable reads using Delta Sharing protocol |

## Best Practices

- For long-running Ray jobs, always materialize datasets using `ray.data.Dataset.materialize()` to avoid cache expiration issues when using the SQL Warehouse approach. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]
- Use the Delta Sharing approach (`read_delta_sharing_tables()`) when available, as it provides more reliable data access without warehouse caching limitations. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]
- Store access tokens in Databricks Secrets rather than using notebook-generated tokens for production use cases. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Limitations

Unity Catalog currently does not share credentials for writing to tables from non-Spark writers. Therefore, any data being written back to Unity Catalog from external Ray applications requires alternative approaches, such as persisting data and then reading it with Spark, or setting up [Databricks Connect](/concepts/databricks-connect.md) within the Ray task. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Related Concepts

- Combine Ray and Spark in the Same Environment — Running Ray and Spark together on Databricks
- Ray Data API — The Ray data processing library
- Databricks SQL Warehouse — The compute endpoint for SQL queries
- [Delta Sharing](/concepts/delta-sharing.md) — Open protocol for secure data sharing
- External Ray Applications to Unity Catalog — Connecting external Ray apps to governed data

## Sources

- combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

# Citations

1. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
