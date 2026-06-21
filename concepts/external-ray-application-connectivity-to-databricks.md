---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: af84ef61b5931d4f4cf498686b716f6b5069579c04c2900f864e692fe1c5959e
  pageDirectory: concepts
  sources:
    - combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-ray-application-connectivity-to-databricks
    - ERACTD
  citations:
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
title: External Ray Application Connectivity to Databricks
description: Connect Ray applications outside Databricks to Unity Catalog tables using ray.data.read_databricks_tables() for SQL warehouse queries (Ray 2.8.0+) and ray.data.read_delta_sharing_tables() for Delta Sharing tables (Ray 2.33+).
tags:
  - ray
  - databricks
  - unity-catalog
  - external-connectivity
timestamp: "2026-06-18T11:01:17.269Z"
---

# External Ray Application Connectivity to Databricks

**External Ray Application Connectivity to Databricks** refers to the methods and APIs that allow Ray applications running outside of a Databricks environment to access and load data from Databricks-managed sources, including [Unity Catalog](/concepts/unity-catalog.md) tables and [Delta Sharing](/concepts/delta-sharing.md) tables. This connectivity enables organizations to leverage Ray's distributed computing capabilities while maintaining Databricks as their central data governance layer.

## Reading from Databricks SQL Warehouses

For Ray 2.8.0 and above, external Ray applications can connect to Databricks Unity Catalog tables using the `ray.data.read_databricks_tables` API. This function queries a Databricks SQL warehouse and returns a Ray dataset.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### Prerequisites

Before calling the API, you must set environment variables for authentication:

- `DATABRICKS_TOKEN` — A SQL warehouse access token. If you're not running your program on Databricks Runtime, you must also set this variable.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]
- `DATABRICKS_HOST` — The Databricks workspace URL (required only when not running on Databricks Runtime). Example: `adb-<workspace-id>.<random-number>.azuredatabricks.net`.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### API Usage

```python
import ray

ray_dataset = ray.data.read_databricks_tables(
    warehouse_id='...',  # Databricks SQL warehouse ID
    catalog='catalog_1',  # Unity Catalog name
    schema='db_1',  # Schema name
    query="SELECT title, score FROM movie WHERE year >= 1980",
)
```

^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

### Cache Duration Consideration

Databricks warehouses can only cache query results for approximately 2 hours. For long-running workloads, you should call the `ray.data.Dataset.materialize` method to materialize the Ray dataset to the Ray distributed object store, preventing data loss if the warehouse cache expires.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Reading from Delta Sharing Tables

For Ray 2.33 and above, external Ray applications can read data from Databricks [Delta Sharing](/concepts/delta-sharing.md) tables using the `ray.data.read_delta_sharing_tables` API. This method is more reliable than reading from a Databricks warehouse cache because it does not depend on cache expiration.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
import ray

ds = ray.data.read_delta_sharing_tables(
    url=f"<profile-file-path>#<share-name>.<schema-name>.<table-name>",
    limit=100000,
    version=1,
)
```

^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Architecture Overview

External Ray applications connect to Databricks through REST API-based communication rather than running directly on Databricks compute. The connectivity patterns differ based on the data source:

- **SQL warehouses**: The Ray application sends SQL queries to a Databricks SQL warehouse endpoint, which executes the query and returns results. The warehouse acts as the query engine and data access point.
- **Delta Sharing**: The Ray application reads directly from a Delta Sharing endpoint using the open Delta Sharing protocol, providing a more direct and cache-independent data path.

In both cases, authentication is managed through access tokens, and Unity Catalog governs which tables and data the external application can access.

## Use Cases

External Ray Application Connectivity is particularly valuable for:

- Integrating Ray-based machine learning pipelines with governed data stored in Databricks.
- Performing distributed data preprocessing or feature engineering using Ray while relying on Unity Catalog for data discovery and access control.
- Building Ray-based applications that need to consume curated datasets from Databricks without running workloads inside the Databricks environment.
- Combining data from Databricks with data from other sources within a single Ray application.

## Limitations

- Unity Catalog currently does not share credentials for writing to tables from non-Spark writers. Therefore, all data being written to a Unity Catalog table from external Ray tasks must be persisted and then read with Spark, or [Databricks Connect](/concepts/databricks-connect.md) must be set up within the Ray task.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Best Practices

- For long-running workloads, always materialize Ray datasets to avoid data loss from warehouse cache expiration. Use `ray.data.Dataset.materialize()` after reading from Databricks.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]
- Prefer [Delta Sharing](/concepts/delta-sharing.md) for reading data when available, as it provides a more reliable data access path compared to SQL warehouse caching.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]
- Store access tokens in a secure secrets manager (such as [Databricks secrets](/concepts/databricks-secret-scopes.md)) rather than hard-coding them in application code.^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Ray and Spark Integration on Databricks](/concepts/ray-and-spark-integration-on-databricks.md) — Running Ray and Spark together in the same Databricks environment
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance layer governing access to tables
- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for sharing data across platforms
- Databricks SQL Warehouses — The compute endpoints used for querying
- Databricks Secrets — Secure storage for access tokens and credentials
- [Databricks Connect](/concepts/databricks-connect.md) — A client library for connecting external applications to Databricks clusters

## Sources

- combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

# Citations

1. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
