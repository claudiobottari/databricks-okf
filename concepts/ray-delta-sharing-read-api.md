---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7d3ad6ff71e7720e43975f66f120ca9ec3f3043a7b15c902fde8d67420b6179c
  pageDirectory: concepts
  sources:
    - combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ray-delta-sharing-read-api
    - RDSRA
  citations:
    - file: combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md
title: Ray Delta Sharing Read API
description: Reading data from Databricks Delta Sharing (OpenSharing) tables using ray.data.read_delta_sharing_tables as a more reliable alternative to SQL warehouse queries for external Ray applications
tags:
  - ray
  - delta-sharing
  - databricks
  - data-ingestion
timestamp: "2026-06-19T09:17:35.782Z"
---

# Ray Delta Sharing Read API

The **Ray Delta Sharing Read API** enables Ray applications to read data from Delta Sharing tables without requiring a Databricks cluster or Spark runtime. This API is available through `ray.data.read_delta_sharing_tables()` starting from Ray 2.33 and above. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Overview

Delta Sharing is Databricks' open protocol for secure data sharing across different computing platforms. The Ray Delta Sharing Read API allows Ray applications — both on and off Databricks — to directly load data from [Delta Sharing](/concepts/delta-sharing.md) tables using a profile file and table identifier. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

Reading from Delta Sharing tables is more reliable than reading from a Databricks warehouse cache, which can expire after approximately 2 hours. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## API Usage

### Basic Syntax

The `ray.data.read_delta_sharing_tables()` function accepts the following key parameters: ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

```python
import ray

ds = ray.data.read_delta_sharing_tables(
    url=f"<profile-file-path>#<share-name>.<schema-name>.<table-name>",
    limit=100000,     # Optional: maximum number of rows to read
    version=1,        # Optional: specific table version for time travel
)
```

### Parameters

- **url**: A string combining the path to a Delta Sharing profile file and the fully qualified table identifier, separated by `#`. The format is `<profile-file-path>#<share-name>.<schema-name>.<table-name>`. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]
- **limit** (optional): Specifies the maximum number of rows to read from the table. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]
- **version** (optional): Specifies a particular table version for time travel queries, allowing you to read historical snapshots of the data. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Comparison with Other Read Methods

The table below compares the Ray Delta Sharing Read API to alternative methods for reading Databricks tables from Ray: ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

| Method | API | Requirements | Reliability |
|--------|-----|--------------|-------------|
| Delta Sharing Read | `ray.data.read_delta_sharing_tables()` | Ray 2.33+ only | High (no cache dependency) |
| Warehouse Query | `ray.data.read_databricks_tables()` | Ray 2.8.0+, SQL warehouse access token | Limited (cache expires ~2 hours) |
| Spark Transfer | `ray.data.from_spark()` | Databricks Runtime ML 15.0+, Spark cluster | High (in-memory transfer) |

## Best Practices

- **Cache management**: Databricks warehouses cache query results for approximately 2 hours. For long-running Ray workloads, prefer the Delta Sharing Read API over the warehouse query API to avoid cache expiration issues. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]
- **Materialization**: Even with the Delta Sharing Read API, you can call `ray.data.Dataset.materialize()` to persist the dataset in the Ray distributed object store for repeated access. ^[combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol underlying this API
- Ray Data API — The broader Ray dataset read/write framework
- [Combine Ray and Spark on Databricks](/concepts/ray-and-spark-integration-on-databricks.md) — General guidance for integrating Ray and Spark workloads
- Ray Data from Databricks Warehouse API — Alternative for reading via SQL warehouses

## Sources

- combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md

# Citations

1. [combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws.md](/references/combine-ray-and-spark-in-the-same-environment-on-databricks-databricks-on-aws-47bcb6c6.md)
