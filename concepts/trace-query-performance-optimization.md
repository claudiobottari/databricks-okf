---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b0c5b71189c45fa47ead1215138a9f4ed5f7b61138d0730dc6a80f847a87f246
  pageDirectory: concepts
  sources:
    - query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-query-performance-optimization
    - TQPO
    - Query Performance Optimization
    - Query performance optimization
    - Query Optimization
  citations:
    - file: query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md
title: Trace Query Performance Optimization
description: Techniques for diagnosing and improving slow trace queries including materialized views, SQL warehouse sizing, and filtering strategies.
tags:
  - performance
  - tracing
  - databricks-sql
  - optimization
timestamp: "2026-06-19T20:02:44.586Z"
---

# Trace Query Performance Optimization

**Trace Query Performance Optimization** refers to techniques for improving the speed and efficiency of querying trace data stored in [Unity Catalog](/concepts/unity-catalog.md) via the [MLflow Tracing](/concepts/mlflow-tracing.md) system. Trace data is stored in OpenTelemetry format, and Databricks SQL views are automatically created to facilitate querying. For large trace volumes, query performance on these views can degrade, requiring optimization strategies. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

## Performance Challenges

The MLflow service creates Databricks SQL views (`{table_prefix}_trace_unified` and `{table_prefix}_trace_metadata`) that transform OpenTelemetry data into the MLflow format. While these views are convenient, **query performance can degrade** when trace volumes become large. The unified view in particular, which includes full span data and assessments, is more computationally expensive to scan. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

## Optimization Strategies

### 1. Use Materialized Views

To maintain performance on large trace volumes, create a **materialized view** over the Databricks SQL views and incrementally update it. Materialized views precompute and store the query results, reducing repeated scan overhead. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

### 2. Use the API for Recent Data

For best performance on recent data, **query traces using the MLflow SDK** (the API) rather than querying the views directly. The MLflow Python SDK (`mlflow.search_traces`, `mlflow.get_trace`) executes queries against a specified Databricks SQL warehouse and is optimized for low-latency access. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

### 3. Optimize Query Filtering

When querying views, performance can be improved by:
- **Tightening upper and lower bounds** on `trace.timestamp_ms` to reduce the scan range.
- **Removing unnecessary filter predicates** where possible.
- Using a **larger SQL warehouse** for consistently slow queries. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

## Monitoring and Diagnosis

To diagnose slow queries, inspect query profiles in the SQL warehouse **Query History**:

1. Go to the **SQL warehouses** page in your Databricks workspace.
2. Select your SQL warehouse and click the **Query history** tab.
3. Look for queries with **MLflow** specified as the source.
4. Click a query to view its query profile.

Key metrics to examine:

- **Scheduling time**: If scheduling time is high, queries are waiting due to heavy load on the warehouse. Switch to a different SQL warehouse using the drop-down menu in the MLflow UI or configure a different warehouse in your client.
- **Overall query performance**: For consistently slow queries, use a larger SQL warehouse, tighten timestamp bounds, and remove filter predicates. ^[query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- Databricks SQL warehouses – Compute resources that execute trace queries.
- [Materialized Views](/concepts/materialized-views-in-databricks.md) – Cached query results for performance.
- [MLflow SDK](/concepts/mlflow.md) – API for querying traces programmatically.
- OpenTelemetry – Trace data format used in Unity Catalog.
- [Unity Catalog](/concepts/unity-catalog.md) – Centralized metadata and storage for trace data.
- Query Profiles – Diagnostic tool for analyzing query execution.

## Sources

- query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md

# Citations

1. [query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws.md](/references/query-opentelemetry-traces-stored-in-unity-catalog-databricks-on-aws-046b043a.md)
