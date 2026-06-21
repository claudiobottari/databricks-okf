---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ef3d58ae86bc2a83dee1b945e0b81dd6ba2165a56967f5a66dd6f575a02e1ec5
  pageDirectory: concepts
  sources:
    - combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - external-ray-applications-with-databricks
    - ERAWD
  citations:
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
title: External Ray Applications with Databricks
description: Connecting external Ray applications to Databricks using ray.data.read_databricks_tables() (via SQL warehouse) and ray.data.read_delta_sharing_tables() (via Delta Sharing/OpenSharing).
tags:
  - ray
  - databricks
  - external-connections
  - delta-sharing
timestamp: "2026-06-18T14:39:25.139Z"
---

Here is the wiki page for **External Ray Applications with Databricks**, based solely on the provided source material.

---

# External Ray Applications with Databricks

**External Ray Applications with Databricks** refers to the practice of running Ray applications outside a Databricks environment (for example, on a separate cluster or local machine) while still reading data from Databricks tables, such as those managed by [Unity Catalog](/concepts/unity-catalog.md). This pattern allows teams to use Ray's flexible distributed computing capabilities for tasks like large-scale data transformation, machine learning inference, or simulation, without moving the data out of the governance and access controls provided by Databricks. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Prerequisites

To connect an external Ray application to Databricks, you must have a valid Databricks access token and know the workspace URL. Set the following environment variables:

- `DATABRICKS_TOKEN` – A SQL warehouse access token or personal access token.
- `DATABRICKS_HOST` – The workspace URL, for example `adb-<workspace-id>.<random-number>.azuredatabricks.net`. This variable is required only when running outside a Databricks Runtime. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Connecting via a Databricks SQL Warehouse

For Ray 2.8.0 and above, use the `ray.data.read_databricks_tables()` API to load data directly from a Unity Catalog table through a Databricks SQL Warehouse. The method accepts a warehouse ID, [Catalog and Schema](/concepts/catalog-and-schema.md) names, and a SQL query. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
import ray

ray_dataset = ray.data.read_databricks_tables(
    warehouse_id='...',
    catalog='catalog_1',
    schema='db_1',
    query="SELECT title, score FROM movie WHERE year >= 1980",
)
```

### Cache Considerations

Warehouse query results are cached for approximately 2 hours. For long-running Ray workloads that need to keep the dataset available beyond that window, call `ray.data.Dataset.materialize()` to materialize the dataset into the Ray distributed object store before processing. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Connecting via a Delta Sharing (OpenSharing) Table

For Ray 2.33 and above, you can read data from [Delta Sharing](/concepts/delta-sharing.md) OpenSharing tables using the `ray.data.read_delta_sharing_tables()` API. This method is considered more reliable than reading from a warehouse cache because it avoids the caching expiry limitation. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
import ray

ds = ray.data.read_delta_sharing_tables(
    url=f"<profile-file-path>#<share-name>.<schema-name>.<table-name>",
    limit=100000,
    version=1,
)
```

The URL follows the format described in the Delta Sharing profile file: `<profile-file-path>#<share-name>.<schema-name>.<table-name>`. The `limit` and `version` parameters are optional. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Best Practices

- **Cache materialization**: For long-running external Ray applications that use the warehouse query method, materialize the dataset to avoid cache expiry. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]
- **Use OpenSharing tables when possible**: They are more reliable for large or long-running workloads because they do not depend on the warehouse query cache. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Limitations

- Databricks warehouses can only cache query results for approximately 2 hours. Without materialization, external Ray applications that take longer than that may lose cached data. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Related Concepts

- Ray Data – The standard dataset abstraction used when reading from Databricks.
- Databricks SQL Warehouse – The compute endpoint used for warehouse-based queries.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that secures and manages the tables read by external Ray applications.
- [Delta Sharing](/concepts/delta-sharing.md) – The open protocol used by the OpenSharing table method.
- Ray – The distributed computing framework.
- [Combine Ray and Spark on Databricks](/concepts/ray-and-spark-integration-on-databricks.md) – The companion pattern for running Ray and Spark within a single Databricks environment, which also includes data transfer methods and best practices.

## Sources

- combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

# Citations

1. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
