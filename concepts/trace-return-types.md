---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 60326e68a47cf7130d06a9decfb2f68d2c1872cb2330ddf6ca41d3774dd50a48
  pageDirectory: concepts
  sources:
    - search-traces-programmatically-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-return-types
    - TRT
  citations:
    - file: search-traces-programmatically-databricks-on-aws.md
title: Trace Return Types
description: mlflow.search_traces() returns results as either pandas DataFrames or lists of MLflow Trace objects, enabling further analysis or evaluation dataset creation.
tags:
  - mlflow
  - data-formats
  - tracing
timestamp: "2026-06-19T20:19:59.760Z"
---

## Trace Return Types

When querying traces programmatically using [`mlflow.search_traces()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.search_traces), the function can return results in one of two formats: a **pandas DataFrame** or a **list of [`Trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace) objects**. The `return_type` parameter controls which format is returned. ^[search-traces-programmatically-databricks-on-aws.md]

### pandas DataFrame

When `return_type='pandas'` (or when `return_type` is not specified, as the default behavior on Databricks-managed MLflow often defaults to a DataFrame), the function returns a `pandas.DataFrame` where each row represents a trace and columns correspond to trace fields. This format is convenient for downstream analysis, visualization, and transformation into evaluation datasets. ^[search-traces-programmatically-databricks-on-aws.md]

### List of Trace Objects

When `return_type='list'`, the function returns a `list[Trace]` — a Python list of [`mlflow.entities.Trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace) objects. Each `Trace` object provides programmatic access to trace attributes, spans, and metadata. This format is useful when you need to iterate over traces and inspect individual properties or convert them into custom data structures. ^[search-traces-programmatically-databricks-on-aws.md]

### Default Behavior

The default value of `return_type` is `None`, which means the function returns a default format (typically a pandas DataFrame on Databricks-managed MLflow). It is best practice to always use keyword arguments with `mlflow.search_traces()` because the function signature is evolving. ^[search-traces-programmatically-databricks-on-aws.md]

### Performance Considerations

`mlflow.search_traces()` returns results in memory. For small to moderate result sets, either return type works well. For large result sets, consider using [`MlflowClient.search_traces()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.client.html#mlflow.client.MlflowClient.search_traces) instead, as it supports pagination and can handle larger volumes of data. ^[search-traces-programmatically-databricks-on-aws.md]

### Schema Details

For detailed information about the columns in the DataFrame or the attributes of the `Trace` objects, see the [MLflow search traces return format documentation](https://mlflow.org/docs/latest/genai/tracing/search-traces/#return-format). ^[search-traces-programmatically-databricks-on-aws.md]

## Related Concepts

- mlflow.search_traces() API|search_traces API – The function that returns these trace objects
- [Trace Object](/concepts/mlflow-trace-object.md) – The MLflow entity representing a single trace
- MLflowClient – Client class with paginated `search_traces()` for large datasets
- Span – A sub‑component of a trace
- Pandas DataFrame – The data structure used for tabular return

## Sources

- search-traces-programmatically-databricks-on-aws.md

# Citations

1. [search-traces-programmatically-databricks-on-aws.md](/references/search-traces-programmatically-databricks-on-aws-0153c5e0.md)
