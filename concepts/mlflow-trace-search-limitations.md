---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a4cab727ec633186572e71f43678ec2bca1fb533e0d7dcd0d3cec2f527a7fe4a
  pageDirectory: concepts
  sources:
    - tracing-faq-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-search-limitations
    - MTSL
  citations:
    - file: tracing-faq-databricks-on-aws.md
title: MLflow Trace Search Limitations
description: The trace list returns only the most recent 1,000 traces by default; older traces require narrowed time filters or migration to Unity Catalog to remove limits.
tags:
  - mlflow
  - tracing
  - search
  - databricks
timestamp: "2026-06-19T23:11:35.543Z"
---

# [[mlflow-trace|MLflow Trace]] Search Limitations

**MLflow Trace Search Limitations** refers to the constraints and quotas that affect how users can search, retrieve, and paginate trace data when using [MLflow Tracing](/concepts/mlflow-tracing.md) on Databricks. These limitations are primarily related to the number of results returned by a search query, the total trace capacity of an experiment, and the infrastructure for handling large-scale trace analysis.

## Default Trace Result Limit

By default, the trace list in the [MLflow](/concepts/mlflow.md) UI returns only the most recent 1,000 [Traces](/concepts/traces.md). If an older trace falls outside this window, it will not appear in search results — even when you search by the exact Trace ID. ^[tracing-faq-databricks-on-aws.md]

To locate an older trace, you can narrow the time range filter to create a smaller window of results. Once the trace falls within the 1,000 most recent entries for that specific period, the ID search will find it. Alternatively, if you know the experiment ID and trace ID, you can navigate directly using the URL: `<workspace-url>/ml/experiments/<experiment-id>/[Traces](/concepts/traces.md)/<trace-id>`. ^[tracing-faq-databricks-on-aws.md]

## Experiment Trace Cap

Experiments that are not stored in [Unity Catalog](/concepts/unity-catalog.md) are capped at a total of 100,000 [Traces](/concepts/traces.md). Once this limit is reached, no new [Traces](/concepts/traces.md) can be logged to that experiment. ^[tracing-faq-databricks-on-aws.md]

To remove both the 1,000-result default limit and the 100,000-trace cap, you can migrate your [Traces](/concepts/traces.md) to [Unity Catalog](/concepts/unity-catalog.md). [Traces](/concepts/traces.md) in [Unity Catalog](/concepts/unity-catalog.md) are not subject to these limits, enabling search across all [Traces](/concepts/traces.md) in a given time range. ^[tracing-faq-databricks-on-aws.md]

## Large-Scale Trace Search

When using `mlflow.search_traces()`, the result set may become too large for the client to handle efficiently. The [MLflow](/concepts/mlflow.md) API provides pagination through the [`MlflowClient.search_traces()`](https://[MLflow](/concepts/mlflow.md).org/docs/latest/api_reference/python_api/[MLflow](/concepts/mlflow.md).client.html#mlflow.client.MlflowClient.search_traces) method. However, for use cases that do not require pagination, `mlflow.search_traces()` is recommended because it provides more functionality and convenient defaults. ^[tracing-faq-databricks-on-aws.md]

For large-scale trace analysis in production, Databricks recommends using [Production Monitoring](/concepts/production-monitoring.md) to log [Traces](/concepts/traces.md) to [Delta tables](/concepts/delta-lake-table.md) in [Unity Catalog](/concepts/unity-catalog.md). This approach bypasses the API search limitations entirely and allows you to query trace data with SQL. See the documentation on [trace agents deployed on Databricks](/concepts/custom-agents-deployment-for-genai-on-databricks.md) for production tracing guidance. ^[tracing-faq-databricks-on-aws.md]

## Rate Limits and Quotas

When using [MLflow Tracing](/concepts/mlflow-tracing.md) within a Databricks workspace, resource quotas and rate limits apply to ensure service stability and fair usage. These limits are documented in the general Databricks resource limits reference. ^[tracing-faq-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- Trace ID
- [Experiments](/concepts/mlflow-experiment.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Production Monitoring](/concepts/production-monitoring.md)
- [Delta Tables](/concepts/delta-lake-table.md)
- Pagination

## Sources

- tracing-faq-databricks-on-aws.md

# Citations

1. [tracing-faq-databricks-on-aws.md](/references/tracing-faq-databricks-on-aws-83ee1878.md)
