---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a5a2bc6162ad28f8c1f4f949fa37cff78ac47e57f212253feb625ae2e9ad3151
  pageDirectory: concepts
  sources:
    - view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-search-and-filtering
    - Filtering and MLflow Trace Search
    - MTSAF
    - Trace Search and Filtering
    - Trace Filtering
    - Trace Search and Discovery
  citations:
    - file: view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md
title: MLflow Trace Search and Filtering
description: Capabilities to narrow down traces using a search bar (by Request content), structured Filters dropdown (by attributes, assessments, state, tags), Sort dropdown, and Columns dropdown to customize the trace list.
tags:
  - mlflow
  - tracing
  - ui
  - filtering
timestamp: "2026-06-19T23:25:06.187Z"
---

# [[mlflow-trace|MLflow Trace]] Search and Filtering

**MLflow Trace Search and Filtering** refers to the capabilities within the Databricks [MLflow](/concepts/mlflow.md) UI and SDK that allow users to find, narrow down, and analyze [Traces](/concepts/traces.md) logged to an [MLflow Experiment](/concepts/mlflow-experiment.md). These tools help developers and operators debug issues, monitor application behavior, and assess performance across large numbers of [Traces](/concepts/traces.md).

## Overview

All captured [Traces](/concepts/traces.md) are logged to an [MLflow Experiment](/concepts/mlflow-experiment.md) and can be accessed through the [MLflow](/concepts/mlflow.md) UI in a Databricks workspace. [Traces](/concepts/traces.md) are stored and served by the managed [MLflow Tracking](/concepts/mlflow-tracking.md) service when `MLFLOW_TRACKING_URI` is set to `databricks`, requiring no additional hosting. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

From the experiment view, users click the **Traces** tab to see a list of all [Traces](/concepts/traces.md) logged to that experiment. The trace list provides a high-level overview with sortable columns including Trace ID, Request, Response, Session, User, Execution time, Request time, Run name, Source, State, Trace name, [Assessments](/concepts/assessments.md), and Tags. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

## Search and Filter Capabilities

### Search Bar

The search bar (often labeled "Search evaluations by request" or similar) allows quick text-based searching of the **Request** (input) field content. This is useful for finding [Traces](/concepts/traces.md) that contain specific user prompts or input patterns. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

### Filters Dropdown

For structured filtering, the "Filters" dropdown lets users build queries based on multiple criteria:

- **Attributes**: Such as `Request` content, `Session time`, `Execution time`, or `Request time`
- **Assessments**: Filter by the presence or specific values of [Assessments](/concepts/assessments.md) like `my_scorer` or `professional`
- **State**: Filter by trace status (`OK`, `ERROR`, `IN_PROGRESS`)
- **Trace name**, **Session**, **User**, and **Tags** (e.g., `tags.persona = 'expert'`)

^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

### Sort Dropdown

The "Sort" dropdown orders [Traces](/concepts/traces.md) by various columns such as `Request time` or `Execution time`. Sorting by `Execution time` in descending order is a common technique for identifying latency bottlenecks. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

### Columns Dropdown

Users can customize which columns are visible in the trace list, including specific tags or assessment metrics. This enables a focused view tailored to specific debugging or monitoring needs. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

## Metadata Filters

The [MLflow](/concepts/mlflow.md) UI supports filtering [Traces](/concepts/traces.md) using search queries against metadata fields. Examples include:

```
# Find all [[traces|Traces]] for a specific user
metadata.`mlflow.trace.user` = 'user-123'

# Find all [[traces|Traces]] in a session
metadata.`mlflow.trace.session` = 'session-abc-456'

# Find [[traces|Traces]] for a user within a specific session
metadata.`mlflow.trace.user` = 'user-123' AND metadata.`mlflow.trace.session` = 'session-abc-456'

# Find [[traces|Traces]] from production environment
metadata.`mlflow.source.type` = 'production'

# Find [[traces|Traces]] from a specific app version
metadata.app_version = '1.0.0'
```

^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

## Common Debugging Scenarios

### Identify Slow [Traces](/concepts/traces.md) (Latency Bottlenecks)

From the trace list view, use the "Sort" dropdown to sort by "Execution time" in descending order, bringing the slowest [Traces](/concepts/traces.md) to the top. In the detailed trace view, the "Trace breakdown" panel's waterfall chart visually highlights operations that took the longest. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

### Find [Traces](/concepts/traces.md) from a Particular User

If user information is tracked and available as a filter option, select or enter the specific user ID in the "Filters" dropdown under "Attributes" or a dedicated "User" filter. Alternatively, if user IDs are stored as tags (e.g., `mlflow.trace.user`), use the search bar with a query like `tags.[MLflow](/concepts/mlflow.md).trace.user = 'user_example_123'`. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

### Locate [Traces](/concepts/traces.md) with Failures (Errors)

In the "Filters" dropdown, select the `State` attribute and choose `ERROR` to see only failed [Traces](/concepts/traces.md). When examining an error trace, select the span marked with an error in the "Trace breakdown" and navigate to its "Events" tab to view the exception message and stack trace. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

### Identify [Traces](/concepts/traces.md) with Negative Feedback or Issues

If collecting user feedback or running evaluations that result in [Assessments](/concepts/assessments.md) (e.g., a boolean `is_correct` or a numeric `relevance_score`), the "Filters" dropdown may allow filtering by assessment names and values (e.g., `is_correct = false` or `relevance_score < 0.5`). Opening a trace and checking the "[Assessments](/concepts/assessments.md)" panel shows logged feedback, scores, and rationales. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

## Limitations

The trace list returns at most **1,000 traces**. Filters and trace ID search apply only to this set, not the full experiment, so older [Traces](/concepts/traces.md) in large experiments might not appear. To find an older trace, narrow the time range to include it. ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

Experiments not in [Unity Catalog](/concepts/unity-catalog.md) are capped at **100,000 traces**. To remove both limits and search across all [Traces](/concepts/traces.md) in a time range, migrate to [traces in Unity Catalog](/concepts/model-traces-in-unity-catalog.md). ^[view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The core tracing framework for instrumenting AI applications
- [MLflow Experiments](/concepts/mlflow-experiment.md) – The organizational unit for [MLflow](/concepts/mlflow.md) runs and [Traces](/concepts/traces.md)
- [Trace Detail View](/concepts/mlflow-trace-detail-view.md) – Exploring individual trace content and span breakdowns
- [Traces in Unity Catalog](/concepts/model-traces-in-unity-catalog.md) – Scalable trace storage with no trace count limits
- [Query Traces via SDK](/concepts/searching-otel-traces-via-mlflow-sdk.md) – Programmatic trace search and analysis for custom workflows

## Next Steps

- [Query traces via SDK](/concepts/searching-otel-traces-via-mlflow-sdk.md) – Programmatically search and analyze [Traces](/concepts/traces.md) for custom workflows
- Build evaluation datasets – Select and convert [Traces](/concepts/traces.md) into test data for systematic evaluation and quality improvement

## Sources

- view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md

# Citations

1. [view-traces-in-the-databricks-mlflow-ui-databricks-on-aws.md](/references/view-traces-in-the-databricks-mlflow-ui-databricks-on-aws-d0ec6f89.md)
