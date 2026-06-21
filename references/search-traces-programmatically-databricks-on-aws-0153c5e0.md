---
title: Search traces programmatically | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/query-via-sdk
ingestedAt: "2026-06-18T08:17:59.981Z"
---

Search and analyze traces programmatically using [`mlflow.search_traces()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.search_traces). This function can query traces stored in the MLflow tracking server, inference tables, or Unity Catalog tables. You can select subsets of traces to analyze or to create evaluation datasets.

## `mlflow.search_traces()` API[​](#mlflowsearch_traces-api "Direct link to mlflowsearch_traces-api")

Python

    def mlflow.search_traces(    experiment_ids: list[str] | None = None,    filter_string: str | None = None,    max_results: int | None = None,    order_by: list[str] | None = None,    extract_fields: list[str] | None = None,    run_id: str | None = None,    return_type: Literal['pandas', 'list'] | None = None,    model_id: str | None = None,    sql_warehouse_id: str | None = None,    include_spans: bool = True,    locations: list[str] | None = None,) -> pandas.DataFrame | list[Trace]

[`mlflow.search_traces()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.search_traces) lets you filter and select data along a few dimensions:

*   Filter by a query string
*   Filter by locations: experiment, run, model, or Unity Catalog schema
*   Limit data: max results, include or exclude spans
*   Adjust return value format: data format, data order

`search_traces()` returns either a pandas DataFrame or a list of [`Trace`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Trace) objects, which can then be analyzed further or reshaped into evaluation datasets. See the [schema details](https://mlflow.org/docs/latest/genai/tracing/search-traces/#return-format) of these return types.

See the [`mlflow.search_traces()` API docs](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.search_traces) for full details.

note

Databricks-managed MLflow and OSS (open source software) MLflow share most search query syntax but have a few field-level differences. See [Differences from OSS MLflow](#differences-from-oss-mlflow) for details.

### `mlflow.search_traces()` parameters[​](#mlflowsearch_traces-parameters "Direct link to mlflowsearch_traces-parameters")

## Search query syntax[​](#search-query-syntax "Direct link to search-query-syntax")

The `filter_string` argument uses a SQL-like query language to filter traces. String values must be wrapped in single quotes (for example, `trace.status = 'OK'`), and numeric values must not be quoted (for example, `trace.execution_time_ms > 1000`). Combine conditions with `AND`. The `OR` operator is not supported.

### Supported filters and comparators[​](#supported-filters-and-comparators "Direct link to Supported filters and comparators")

The following fields and comparators are supported on Databricks-managed MLflow.

### Differences from OSS MLflow[​](#differences-from-oss-mlflow "Direct link to differences-from-oss-mlflow")

The search query syntax on Databricks-managed MLflow closely tracks [OSS MLflow](https://mlflow.org/docs/latest/genai/tracing/search-traces/#search-query-syntax), with the following differences:

### Search for third-party OpenTelemetry spans[​](#search-for-third-party-opentelemetry-spans "Direct link to Search for third-party OpenTelemetry spans")

To search traces ingested from third-party OpenTelemetry tools such as Langfuse, use the `span.attributes.*` prefix instead. See [Search for traces by OTel span attributes](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/third-party/otel-span-attributes#search-for-traces-by-otel-span-attributes).

## Best practices[​](#best-practices "Direct link to Best practices")

### Keyword arguments[​](#keyword-arguments "Direct link to Keyword arguments")

Always use keyword (named) arguments with `mlflow.search_traces()`. It allows positional arguments, but the function arguments are evolving.

Good practice: `mlflow.search_traces(filter_string="trace.status = 'OK'")`

Bad practice: `mlflow.search_traces([], "trace.status = 'OK'")`

### `filter_string` gotchas[​](#filter_string-gotchas "Direct link to filter_string-gotchas")

When searching using the `filter_string` argument to `mlflow.search_traces()`, remember to:

*   Use prefixes: `trace.`, `tag.`, or `metadata.`
*   Use backticks if tag or attribute names have dots: `` tag.`mlflow.traceName` ``
*   Use single quotes only: `'value'` not `"value"`
*   Use Unix timestamp (milliseconds) for time: `1749006880539` not dates
*   Use AND only: No OR support

See [Search query syntax](#search-query-syntax) for the full list of supported fields and operators.

### SQL warehouse integration[​](#-sql-warehouse-integration "Direct link to -sql-warehouse-integration")

`mlflow.search_traces()` can optionally use a Databricks [SQL warehouse](https://docs.databricks.com/aws/en/compute/sql-warehouse/) to improve performance on large trace datasets in inference tables or Unity Catalog tables. Specify your SQL warehouse ID using the `MLFLOW_TRACING_SQL_WAREHOUSE_ID` environment variable.

Execute trace queries using a Databricks SQL warehouse for improved performance on large trace datasets:

Python

    import osos.environ['MLFLOW_TRACING_SQL_WAREHOUSE_ID'] = 'fa92bea7022e81fb'# Use SQL warehouse for better performancetraces = mlflow.search_traces(    filter_string="trace.status = 'OK'",    locations=['my_catalog.my_schema'],)

`mlflow.search_traces()` returns results in memory, which works well for smaller result sets. To handle large result sets, use [`MlflowClient.search_traces()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.client.html#mlflow.client.MlflowClient.search_traces) since it supports pagination.

## Next steps[​](#next-steps "Direct link to Next steps")

*   [Tutorial: Search traces programmatically](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/search-traces-examples) - Run a set of simple examples of `mlflow.search_traces()`
*   [Tutorial: Trace and analyze users and environments](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/add-context-to-traces-tutorial) - Run an example of adding context metadata to traces and analyzing the results
*   [Examples: Analyzing traces](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/observe-with-traces/analyze-traces) - See a variety of examples of trace analysis
*   [Build evaluation datasets](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/build-eval-dataset) - Convert queried traces into test datasets
