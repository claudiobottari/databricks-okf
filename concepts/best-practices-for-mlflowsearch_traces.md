---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4ebc643f1dd7ff1a1fd14b068f0c334eab74a6c67c261a9ccac87358c54eb062
  pageDirectory: concepts
  sources:
    - search-traces-programmatically-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - best-practices-for-mlflowsearch_traces
    - BPFM
  citations:
    - file: search-traces-programmatically-databricks-on-aws.md
title: Best Practices for mlflow.search_traces()
description: Recommended practices including using keyword arguments, proper filter_string formatting (prefixes, single quotes, backticks, timestamps), and avoiding unsupported operators like OR.
tags:
  - mlflow
  - best-practices
  - tracing
timestamp: "2026-06-19T20:20:14.641Z"
---

# Best Practices for mlflow.search_traces()

The `mlflow.search_traces()` function is the primary API for programmatically querying and analyzing traces stored in MLflow. Following best practices ensures reliable, performant, and maintainable trace analysis code.

## Use Keyword Arguments

Always use keyword (named) arguments when calling `mlflow.search_traces()`. The function supports positional arguments, but the argument list is evolving across MLflow versions. Using keyword arguments makes your code more resilient to API changes and easier to read. ^[search-traces-programmatically-databricks-on-aws.md]

**Good practice:**
```python
mlflow.search_traces(filter_string="trace.status = 'OK'")
```

**Bad practice:**
```python
mlflow.search_traces([], "trace.status = 'OK'")
```

^[search-traces-programmatically-databricks-on-aws.md]

## Construct Filter Strings Carefully

The `filter_string` argument uses a SQL-like query language with specific syntax rules. Adhering to these rules prevents common errors:

- **Use the correct prefix:** Field names must be prefixed with `trace.`, `tag.`, or `metadata.` (e.g., `trace.status = 'OK'`). ^[search-traces-programmatically-databricks-on-aws.md]
- **Escape dots in tag names:** If a tag or attribute name contains dots, wrap it in backticks. For example: `` tag.`mlflow.traceName` ``. ^[search-traces-programmatically-databricks-on-aws.md]
- **Use single quotes only:** String values must be enclosed in single quotes (`'value'`), not double quotes. ^[search-traces-programmatically-databricks-on-aws.md]
- **Use Unix timestamps for time fields:** Time-based filters require Unix timestamps in milliseconds (e.g., `1749006880539`), not date strings. ^[search-traces-programmatically-databricks-on-aws.md]
- **Use AND only, never OR:** The query language supports combining conditions with `AND` but does **not** support the `OR` operator. ^[search-traces-programmatically-databricks-on-aws.md]

## Leverage SQL Warehouse for Large Datasets

For improved performance when querying large trace datasets stored in inference tables or [Unity Catalog](/concepts/unity-catalog.md) tables, configure `mlflow.search_traces()` to use a Databricks SQL warehouse. Set the `MLFLOW_TRACING_SQL_WAREHOUSE_ID` environment variable with your SQL warehouse ID before calling the function. ^[search-traces-programmatically-databricks-on-aws.md]

```python
import os
os.environ['MLFLOW_TRACING_SQL_WAREHOUSE_ID'] = 'fa92bea7022e81fb'

traces = mlflow.search_traces(
    filter_string="trace.status = 'OK'",
    locations=['my_catalog.my_schema'],
)
```

^[search-traces-programmatically-databricks-on-aws.md]

## Handle Large Result Sets with Pagination

`mlflow.search_traces()` returns results in memory, which works well for smaller result sets. For large result sets, use `MlflowClient.search_traces()` instead, as it supports pagination for fetching results in manageable batches. ^[search-traces-programmatically-databricks-on-aws.md]

## Choose the Right Return Type

The function can return either a pandas DataFrame or a list of [Trace](/concepts/traces.md) objects. Use the `return_type` parameter to control the output format based on your downstream needs — DataFrames are convenient for analysis and visualization, while Trace objects provide full access to the trace entity API. ^[search-traces-programmatically-databricks-on-aws.md]

## Consider Databricks vs. OSS MLflow Differences

While Databricks-managed MLflow and open-source MLflow share most search query syntax, there are some field-level differences. Consult the Differences from OSS MLflow documentation to ensure your queries behave as expected on your platform. ^[search-traces-programmatically-databricks-on-aws.md]

## Search Third-Party OpenTelemetry Spans Correctly

When searching traces ingested from third-party OpenTelemetry tools (e.g., Langfuse), use the `span.attributes.*` prefix instead of the standard `trace.` prefix. See [Search for traces by OTel span attributes](/concepts/span-attributes-and-search.md) for details. ^[search-traces-programmatically-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- Trace entity
- Search query syntax
- [SQL warehouse for tracing](/concepts/sql-warehouse-integration-for-trace-search.md)
- [Build evaluation datasets from traces](/concepts/evaluation-datasets.md)

## Sources

- search-traces-programmatically-databricks-on-aws.md

# Citations

1. [search-traces-programmatically-databricks-on-aws.md](/references/search-traces-programmatically-databricks-on-aws-0153c5e0.md)
